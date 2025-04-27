from worlds.AutoWorld import World, WebWorld
from .items import item_table, UT99Item
from .locations import location_table


class UT99WebWorld(WebWorld):
    pass


class UT99World(World):
    game = "Unreal Tournament 1999"
    web = UT99WebWorld()

    item_name_to_id = {name: data.id for name, data in item_table.items()}
    location_name_to_id = {name: data.id for name, data in location_table.items()}

    def create_item(self, name: str) -> UT99Item:
        item_id: int(self.item_name_to_id[name])
        return None
