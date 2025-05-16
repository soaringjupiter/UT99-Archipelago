import asyncio
import urllib.parse
from copy import deepcopy
from typing import Dict, List

import Utils
from CommonClient import (
    ClientCommandProcessor,
    CommonContext,
    get_base_parser,
    gui_enabled,
    logger,
)
from NetUtils import JSONMessagePart, JSONtoTextParser, NetworkItem, encode

from worlds.ut99 import UT99World

PROXY_PORT = 8787


# json to plain text converter
class UT99JSONToText(JSONtoTextParser):
    # strip out color codes
    def _handle_color(self, node: JSONMessagePart) -> str:  # type: ignore [override]
        return self._handle_text(node)


# main context <-> archipelago
class UT99Context(CommonContext):
    game = "Unreal Tournament 1999"
    items_handling = 0b111

    def __init__(self, server_address: str, password: str | None):
        super().__init__(server_address, password)
        self.ut_queue: asyncio.Queue[str] = asyncio.Queue()

        # for printing archipelago messages into ut
        self.ut_parser = UT99JSONToText(self)

        # start tiny tcp server the moment we boot
        self.ut_server_task: asyncio.Task[None] | None = None
        asyncio.get_event_loop().create_task(self.start_ut_server())

    async def server_auth(self, password_requested: bool = False):
        if password_requested and not self.password:
            await super().server_auth(password_requested)

        await self.get_username()  # ask user for slot if needed
        await self.send_connect()  # fire the normal Connect packet

    def is_ut_alive(self) -> bool:
        return self.is_ut_connected

    async def push_ut(self, text: str):
        # enqueue plain text to be sent to ut99
        await self.ut_queue.put(text)

    def on_print_json(self, args: Dict):
        # any printjson packet is sent to the ut99 server
        text = self.ut_parser(deepcopy(args["data"]))
        asyncio.create_task(self.push_ut(f"chat {text}"))

        # keep vanilla behaviour too
        super().on_print_json(args)

    def on_package(self, cmd: str, args: Dict):
        if cmd == "ReceivedItems":
            self.handle_items(args)
        elif cmd == "Connected":
            # send missing info once game logs in
            self.handle_connected(args)
        elif cmd == "RoomInfo":
            # keep a copy so we can replay it to later ut connections
            self.room_info_copy = encode([args])
        else:
            asyncio.create_task(self.push_ut(f"ap {cmd} {args}"))

    def handle_items(self, args: Dict):
        start_idx = args["index"]
        items: List[NetworkItem] = [NetworkItem(*i) for i in args["items"]]
        if start_idx == 0:
            new = items
            self.items_received = items
        else:
            new = items[len(self.items_received) :]
            self.items_received.extend(new)

        for net_item in new:
            map_name = self.item_names.lookup_in_game(net_item.item)
            # they're stored as "DM-Foo - Unlock"
            short = map_name.split(" - ")[0]
            asyncio.create_task(self.push_ut(f"unlock {short}"))

    async def check_location(self, loc_name: str):
        loc_id = UT99World.location_name_to_id.get(loc_name)
        if loc_id is None:
            logger.warning("unknown location from ut: %s", loc_name)
            return
        await self.check_locations({loc_id})

    def handle_connected(self, args: Dict):
        """
        immediately tell ut which maps are already unlocked when we launch.
        """
        # iterate over every unlock present in our inventory
        for item in self.items_received:
            map_name = self.item_names.lookup_in_slot(item.item)
            short = map_name.split(" - ")[0]
            asyncio.create_task(self.push_ut(f"unlock {short}"))

    # tiny server for the game
    async def start_ut_server(self):
        async def handler(reader: asyncio.StreamReader, writer: asyncio.StreamWriter):
            try:
                await writer.drain()

                # continually read lines (terminated by \n or \r\n)
                while not reader.at_eof():
                    line = (await reader.readline()).decode().strip()
                    if not line:
                        continue
                    await self.process_ut_line(line, writer)
            finally:
                # tidy up if the map went away
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
        # rudimentary http parser
        # ut99 is sending GET /beat?m=DM-Pressure%20-%20Beaten HTTP/1.1
        # we only care about the path, not the headers
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
                # cheap long-poll: immediately dump queued msgs (if any)
                payload_lines: List[str] = []
                for net_item in self.items_received:
                    full_name = self.item_names.lookup_in_slot(net_item.item)
                    short = full_name.split(" - ")[0]
                    payload_lines.append(f"unlock {short}")
                body = "\n".join(payload_lines)
                await self.http_response(writer, 200, body)
            else:
                await self.http_response(writer, 404, "what r u doin")
        # ignore the rest of the http chatter (Host:, etc.)

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
