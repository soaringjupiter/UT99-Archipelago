import asyncio
import urllib.parse
from copy import deepcopy

import Utils
from CommonClient import (
    CommonContext,
    get_base_parser,
    gui_enabled,
    logger,
)
from NetUtils import JSONMessagePart, JSONtoTextParser, NetworkItem, encode
from worlds.ut99 import UT99World

PROXY_PORT = 8787


class UT99JSONToText(JSONtoTextParser):
    # strip out color codes
    def _handle_color(self, node: JSONMessagePart) -> str:
        return self._handle_text(node)


class UT99Context(CommonContext):
    game = "Unreal Tournament 1999"
    items_handling = 0b111

    def __init__(self, server_address: str, password: str | None):
        super().__init__(server_address, password)
        self.ut_queue: asyncio.Queue[str] = asyncio.Queue()

        self.ut_parser = UT99JSONToText(self)

    async def server_auth(self, password_requested: bool = False):
        if password_requested and not self.password:
            await super().server_auth(password_requested)

        await self.get_username()
        await self.send_connect()

    def is_ut_alive(self) -> bool:
        return self.is_ut_connected

    async def push_ut(self, text: str):
        await self.ut_queue.put(text)

    def on_print_json(self, args: dict):
        text = self.ut_parser(deepcopy(args["data"]))
        asyncio.create_task(self.push_ut(f"chat {text}"))
        super().on_print_json(args)

    def on_package(self, cmd: str, args: dict):
        if cmd == "ReceivedItems":
            self.handle_items(args)
        elif cmd == "Connected":
            self.handle_connected(args)
        elif cmd == "RoomInfo":
            self.room_info_copy = encode([args])
        else:
            asyncio.create_task(self.push_ut(f"ap {cmd} {args}"))

    def handle_items(self, args: dict):
        start_idx = args["index"]
        items: list[NetworkItem] = [NetworkItem(*i) for i in args["items"]]
        if start_idx == 0:
            new = items
            self.items_received = items
        else:
            new = items[len(self.items_received) :]
            self.items_received.extend(new)

        for net_item in new:
            map_name = self.item_names.lookup_in_game(net_item.item)
            asyncio.create_task(self.push_ut(f"unlock {map_name}"))

    async def check_location(self, loc_name: str):
        loc_id = UT99World.location_name_to_id.get(loc_name)
        if loc_id is None:
            logger.warning("unknown location from ut: %s", loc_name)
            return
        await self.check_locations({loc_id})

    def handle_connected(self, args: dict):
        for item in self.items_received:
            map_name = self.item_names.lookup_in_slot(item.item)
            short = map_name.split(" - ")[0]
            asyncio.create_task(self.push_ut(f"unlock {short}"))
        self.ut_server_task: asyncio.Task[None] | None = None
        asyncio.get_event_loop().create_task(self.start_ut_server())

    async def start_ut_server(self):
        async def handler(reader: asyncio.StreamReader, writer: asyncio.StreamWriter):
            try:
                await writer.drain()
                while not reader.at_eof():
                    line = (await reader.readline()).decode().strip()
                    if not line:
                        continue
                    await self.process_ut_line(line, writer)
            finally:
                writer.close()
                await writer.wait_closed()

        self.ut_server_task = await asyncio.start_server(
            handler,
            "127.0.0.1",
            PROXY_PORT,
        )
        addr = self.ut_server_task.sockets[0].getsockname()
        logger.info(f"ut99 bridge listening on {addr}")

    async def process_ut_line(self, line: str, writer: asyncio.StreamWriter):
        if line.startswith("GET "):
            logger.debug("ut99: %s", line)
            try:
                path = line.split(" ", 2)[1]
                path = urllib.parse.unquote(path)
            except Exception:
                logger.warning("malformed request line: %s", line)
                await self.http_response(writer, 400, "bad request")
                return

            if path.startswith("/beat"):
                query = urllib.parse.urlparse(path).query
                qs = urllib.parse.parse_qs(query)
                loc = qs.get("m", [""])[0]
                if loc:
                    await self.check_location(loc)
                    await self.http_response(writer, 200, "ok")
                else:
                    await self.http_response(writer, 400, "missing m param")
            elif path.startswith("/poll"):
                payload_lines: list[str] = []
                for net_item in self.items_received:
                    full_name = self.item_names.lookup_in_slot(net_item.item)
                    short = full_name.split(" - ")[0]
                    payload_lines.append(f"unlock {short}")
                body = "\n".join(payload_lines)
                await self.http_response(writer, 200, body)
            else:
                await self.http_response(writer, 404, "what r u doin")

    async def http_response(self, w: asyncio.StreamWriter, code: int, body: str):
        reason = {200: "OK", 400: "Bad Request", 404: "Not Found"}.get(code, "OK")
        header = (
            f"HTTP/1.1 {code} {reason}\r\n"
            f"Connection: close\r\n"
            f"Content-Length: {len(body.encode())}\r\n"
            f"Content-Type: text/plain\r\n\r\n"
        )
        w.write(header.encode() + body.encode())
        await w.drain()
        w.close()
        await w.wait_closed()


def launch():
    async def main():
        parser = get_base_parser("ut99 <-> archipelago bridge")
        args = parser.parse_args()

        ctx = UT99Context(args.connect, args.password)

        if gui_enabled:
            ctx.run_gui()
        ctx.run_cli()

        await ctx.exit_event.wait()

    Utils.init_logging("UT99Client")
    import colorama

    colorama.just_fix_windows_console()
    asyncio.run(main())
    colorama.deinit()


if __name__ == "__main__":
    launch()
