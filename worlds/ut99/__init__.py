import random

from BaseClasses import Region
from worlds.AutoWorld import WebWorld, World
from worlds.LauncherComponents import (
    Component,
    Type,
    components,
)
from worlds.LauncherComponents import (
    launch as launch_component,
)

from .items import UT99Item, item_table
from .locations import location_table


def launch_client():
    from .client import launch

    launch_component(launch)


components.append(
    Component(
        "UT99 Client",
        "UT99Client",
        func=launch_client,
        component_type=Type.CLIENT,
    ),
)


class UT99WebWorld(WebWorld):
    pass


class UT99World(World):
    game = "Unreal Tournament 1999"
    topology_present = False
    web = UT99WebWorld()

    item_name_to_id = {name: data.code for name, data in item_table.items()}
    location_name_to_id = {name: data.address for name, data in location_table.items()}

    origin_region_name: str = "Menu"

    # pick random location to be the last map before Game Complete
    last_map: str = random.choice(  # noqa: S311
        list(location_table),
    )

    def create_regions(self):
        menu = Region("Menu", self.player, self.multiworld)
        self.multiworld.regions.append(menu)
        ladders = []
        for ladder in ["DM", "DOM", "CTF", "AS", "Chal"]:
            region_name = ladder
            ladders.append(region_name)
            region = Region(region_name, self.player, self.multiworld)
            region.add_locations(
                {
                    loc.name: loc.address
                    for loc in location_table.values()
                    if loc.ladder == ladder
                },
            )
            self.multiworld.regions.append(region)
            menu.connect(region)
            region.connect(menu)

        regs = {
            r.name: r
            for r in self.multiworld.regions
            if r.player == self.player and r.name != "Menu"
        }
        for a in regs.values():
            for b in regs.values():
                if a is not b:
                    a.connect(b)

    def create_items(self):
        # get random map from item_table
        random_map = random.choice(  # noqa: S311
            [
                item
                for item in item_table.values()
                if item.placeable
                and item.name != self.last_map
                and item.name == "DM-Oblivion"  # for testing
            ],
        )
        self.multiworld.push_precollected(self.create_item(random_map.name))
        for item_name, item in item_table.items():
            if item.placeable and item_name != random_map.name:
                self.multiworld.itempool.append(self.create_item(item_name))

        gc_item = self.create_item("Game Complete")
        gc_location = self.multiworld.get_location(self.last_map, self.player)
        gc_location.place_locked_item(gc_item)

    def set_rules(self):
        player = self.player
        mw = self.multiworld

        for loc_obj in location_table.values():
            map_name = loc_obj.name
            loc = mw.get_location(map_name, player)

            loc.access_rule = lambda state, unlock=map_name, p=player: state.has(
                unlock,
                p,
                1,
            )

        beaten_locations = [
            mw.get_location(loc.name, player) for loc in location_table.values()
        ]

        mw.completion_condition[player] = lambda state, targets=beaten_locations: all(
            loc in state.locations_checked for loc in targets
        )

        all_unlocks = [n for n, d in item_table.items() if d.placeable]
        gc_location = mw.get_location(self.last_map, player)
        old_rule = gc_location.access_rule
        gc_location.access_rule = lambda state, p=player, base=old_rule, reqs=tuple(
            all_unlocks,
        ): (base(state) and state.has_all(reqs, p))

    def get_filler_item_name(self):
        return "Nothing"

    def create_item(self, name: str) -> UT99Item:
        data = item_table.get(name)
        if not data:
            raise KeyError(f"Item '{name}' not found in item_table.")
        return UT99Item(
            name=data.name,
            code=data.code,
            classification=data.classification,
            player=self.player,
        )
