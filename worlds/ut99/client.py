import asyncio
import json
from copy import deepcopy

import Utils
from CommonClient import (
    CommonContext,
    get_base_parser,
    gui_enabled,
    logger,
)
from NetUtils import JSONMessagePart, JSONtoTextParser, NetworkItem, encode
from worlds.ut99 import UT99World, location_table

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
        self.tcp_server = None
        self.tcp_clients = set()

    async def server_auth(self, password_requested: bool = False):
        if password_requested and not self.password:
            await super().server_auth(password_requested)
        await self.get_username()
        await self.send_connect()

    def is_ut_alive(self) -> bool:
        return self.is_ut_connected

    async def push_ut(self, action: str, **kwargs):
        # Send a JSON message to all connected UT clients
        msg = {"action": action}
        msg.update(kwargs)
        data = json.dumps(msg) + "\n"
        for writer in list(self.tcp_clients):
            try:
                writer.write(data.encode())
                await writer.drain()
            except Exception:
                self.tcp_clients.discard(writer)

    def on_print_json(self, args: dict):
        text = self.ut_parser(deepcopy(args["data"]))
        # if player name is in the text
        is_from_self = text.startswith(f"{self.username}: ")
        if not is_from_self:
            asyncio.create_task(self.push_ut("chat", msg=text))
        super().on_print_json(args)

    def on_package(self, cmd: str, args: dict):
        if cmd == "ReceivedItems":
            self.handle_items(args)
        elif cmd == "Connected":
            self.handle_connected(args)
        elif cmd == "RoomInfo":
            self.room_info_copy = encode([args])
        else:
            asyncio.create_task(self.push_ut("ap", cmd=cmd, args=args))

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
            asyncio.create_task(self.push_ut("unlock", map=map_name))

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
            asyncio.create_task(self.push_ut("unlock", map=short))
        self.tcp_server_task: asyncio.Task[None] | None = None
        asyncio.get_event_loop().create_task(self.start_tcp_server())

    async def start_tcp_server(self):
        async def handler(reader: asyncio.StreamReader, writer: asyncio.StreamWriter):
            self.tcp_clients.add(writer)
            try:
                while not reader.at_eof():
                    line = await reader.readline()
                    if not line:
                        continue
                    try:
                        msg = json.loads(line.decode())
                    except Exception:
                        logger.warning("Malformed JSON from UT99: %s", line)
                        continue
                    await self.process_ut_json(msg, writer)
            finally:
                self.tcp_clients.discard(writer)
                writer.close()
                await writer.wait_closed()

        self.tcp_server = await asyncio.start_server(
            handler,
            "127.0.0.1",
            PROXY_PORT,
        )
        addr = self.tcp_server.sockets[0].getsockname()
        logger.info(f"ut99 TCP JSON bridge listening on {addr}")

    async def process_ut_json(self, msg: dict, writer: asyncio.StreamWriter):
        action = msg.get("action")
        if action == "beat":
            map_name = msg.get("map")
            if map_name:
                await self.check_location(map_name)
                await self.send_json(writer, {"action": "ok"})
            else:
                await self.send_json(
                    writer, {"action": "error", "msg": "missing map param"}
                )
        elif action == "poll":
            for net_item in self.items_received:
                full_name = self.item_names.lookup_in_slot(net_item.item)
                short = full_name.split(" - ")[0]
                await self.send_json(writer, {"action": "unlock", "map": short})
        elif action == "checked_locations":
            address_to_name = {
                loc.address: name for name, loc in location_table.items()
            }
            checked_maps = [
                address_to_name[loc_id]
                for loc_id in self.checked_locations
                if loc_id in address_to_name
            ]
            await self.send_json(
                writer, {"action": "checked_locations", "maps": checked_maps}
            )
        elif action == "chat":
            msg_text = msg.get("msg", "")
            if msg_text:
                asyncio.create_task(self.send_chat(msg_text))
            await self.send_json(writer, {"action": "ok"})
        else:
            await self.send_json(writer, {"action": "error", "msg": "unknown action"})

    async def send_json(self, writer: asyncio.StreamWriter, obj: dict):
        data = json.dumps(obj) + "\n"
        writer.write(data.encode())
        await writer.drain()

    async def send_chat(self, msg: str):
        await self.send_msgs([{"cmd": "Say", "text": msg}])


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
