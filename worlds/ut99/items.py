from __future__ import annotations
from BaseClasses import Item, ItemClassification


class UT99Item(Item):
    __slots__ = ("classification", "code", "location", "name", "player", "placeable")

    def __init__(
        self,
        name: str,
        classification: ItemClassification,
        code: int,
        player: int | None = None,
        placeable: bool = True,
    ):
        super().__init__(
            name=name,
            classification=classification,
            code=code,
            player=player if player else None,
        )
        self.classification = classification
        self.placeable = placeable


BASE_ID = 19991000


item_table: dict[str, UT99Item] = {
    # Deathmatch Maps - Unlocked
    "DM-Oblivion": UT99Item(
        name="DM-Oblivion",
        code=BASE_ID + 16,
        classification=ItemClassification.progression,
    ),
    "DM-Stalwart": UT99Item(
        name="DM-Stalwart",
        code=BASE_ID + 17,
        classification=ItemClassification.progression,
    ),
    "DM-Fractal": UT99Item(
        name="DM-Fractal",
        code=BASE_ID + 18,
        classification=ItemClassification.progression,
    ),
    "DM-Turbine": UT99Item(
        name="DM-Turbine",
        code=BASE_ID + 19,
        classification=ItemClassification.progression,
    ),
    "DM-Codex": UT99Item(
        name="DM-Codex",
        code=BASE_ID + 20,
        classification=ItemClassification.progression,
    ),
    "DM-Pressure": UT99Item(
        name="DM-Pressure",
        code=BASE_ID + 21,
        classification=ItemClassification.progression,
    ),
    "DM-ArcaneTemple": UT99Item(
        name="DM-ArcaneTemple",
        code=BASE_ID + 22,
        classification=ItemClassification.progression,
    ),
    "DM-Grinder": UT99Item(
        name="DM-Grinder",
        code=BASE_ID + 23,
        classification=ItemClassification.progression,
    ),
    "DM-Malevolence": UT99Item(
        name="DM-Malevolence",
        code=BASE_ID + 24,
        classification=ItemClassification.progression,
    ),
    "DM-KGalleon": UT99Item(
        name="DM-KGalleon",
        code=BASE_ID + 25,
        classification=ItemClassification.progression,
    ),
    "DM-Tempest": UT99Item(
        name="DM-Tempest",
        code=BASE_ID + 26,
        classification=ItemClassification.progression,
    ),
    "DM-Shrapnel][": UT99Item(
        name="DM-Shrapnel][",
        code=BASE_ID + 28,
        classification=ItemClassification.progression,
    ),
    "DM-Liandri": UT99Item(
        name="DM-Liandri",
        code=BASE_ID + 29,
        classification=ItemClassification.progression,
    ),
    "DM-Conveyor": UT99Item(
        name="DM-Conveyor",
        code=BASE_ID + 30,
        classification=ItemClassification.progression,
    ),
    "DM-Peak": UT99Item(
        name="DM-Peak",
        code=BASE_ID + 31,
        classification=ItemClassification.progression,
    ),
    # Domination Maps - Unlocked
    "DOM-Condemned": UT99Item(
        name="DOM-Condemned",
        code=BASE_ID + 32,
        classification=ItemClassification.progression,
    ),
    "DOM-Ghardhen": UT99Item(
        name="DOM-Ghardhen",
        code=BASE_ID + 41,
        classification=ItemClassification.progression,
    ),
    "DOM-Cryptic": UT99Item(
        name="DOM-Cryptic",
        code=BASE_ID + 42,
        classification=ItemClassification.progression,
    ),
    "DOM-Cinder": UT99Item(
        name="DOM-Cinder",
        code=BASE_ID + 43,
        classification=ItemClassification.progression,
    ),
    "DOM-Gearbolt": UT99Item(
        name="DOM-Gearbolt",
        code=BASE_ID + 44,
        classification=ItemClassification.progression,
    ),
    "DOM-Leadworks": UT99Item(
        name="DOM-Leadworks",
        code=BASE_ID + 45,
        classification=ItemClassification.progression,
    ),
    "DOM-Olden": UT99Item(
        name="DOM-Olden",
        code=BASE_ID + 46,
        classification=ItemClassification.progression,
    ),
    "DOM-Sesmar": UT99Item(
        name="DOM-Sesmar",
        code=BASE_ID + 47,
        classification=ItemClassification.progression,
    ),
    "DOM-MetalDream": UT99Item(
        name="DOM-MetalDream",
        code=BASE_ID + 48,
        classification=ItemClassification.progression,
    ),
    # Capture the Flag Maps - Unlocked
    "CTF-Niven": UT99Item(
        name="CTF-Niven",
        code=BASE_ID + 49,
        classification=ItemClassification.progression,
    ),
    "CTF-Face": UT99Item(
        name="CTF-Face",
        code=BASE_ID + 60,
        classification=ItemClassification.progression,
    ),
    "CTF-EternalCave": UT99Item(
        name="CTF-EternalCave",
        code=BASE_ID + 61,
        classification=ItemClassification.progression,
    ),
    "CTF-Coret": UT99Item(
        name="CTF-Coret",
        code=BASE_ID + 62,
        classification=ItemClassification.progression,
    ),
    "CTF-Gauntlet": UT99Item(
        name="CTF-Gauntlet",
        code=BASE_ID + 63,
        classification=ItemClassification.progression,
    ),
    "CTF-Dreary": UT99Item(
        name="CTF-Dreary",
        code=BASE_ID + 64,
        classification=ItemClassification.progression,
    ),
    "CTF-Command": UT99Item(
        name="CTF-Command",
        code=BASE_ID + 65,
        classification=ItemClassification.progression,
    ),
    "CTF-LavaGiant": UT99Item(
        name="CTF-LavaGiant",
        code=BASE_ID + 66,
        classification=ItemClassification.progression,
    ),
    "CTF-November": UT99Item(
        name="CTF-November",
        code=BASE_ID + 67,
        classification=ItemClassification.progression,
    ),
    "CTF-Hydro16": UT99Item(
        name="CTF-Hydro16",
        code=BASE_ID + 68,
        classification=ItemClassification.progression,
    ),
    "CTF-Orbital": UT99Item(
        name="CTF-Orbital",
        code=BASE_ID + 69,
        classification=ItemClassification.progression,
    ),
    # Assault Maps - Unlocked
    "AS-Frigate": UT99Item(
        name="AS-Frigate",
        code=BASE_ID + 70,
        classification=ItemClassification.progression,
    ),
    "AS-HiSpeed": UT99Item(
        name="AS-HiSpeed",
        code=BASE_ID + 76,
        classification=ItemClassification.progression,
    ),
    "AS-Rook": UT99Item(
        name="AS-Rook",
        code=BASE_ID + 77,
        classification=ItemClassification.progression,
    ),
    "AS-Mazon": UT99Item(
        name="AS-Mazon",
        code=BASE_ID + 78,
        classification=ItemClassification.progression,
    ),
    "AS-OceanFloor": UT99Item(
        name="AS-OceanFloor",
        code=BASE_ID + 79,
        classification=ItemClassification.progression,
    ),
    "AS-Overlord": UT99Item(
        name="AS-Overlord",
        code=BASE_ID + 80,
        classification=ItemClassification.progression,
    ),
    # Challenge Maps - Unlocked
    "DM-Phobos": UT99Item(
        name="DM-Phobos",
        code=BASE_ID + 81,
        classification=ItemClassification.progression,
    ),
    "DM-Morpheus": UT99Item(
        name="DM-Morpheus",
        code=BASE_ID + 85,
        classification=ItemClassification.progression,
    ),
    "DM-Zeto": UT99Item(
        name="DM-Zeto",
        code=BASE_ID + 86,
        classification=ItemClassification.progression,
    ),
    "DM-HyperBlast": UT99Item(
        name="DM-HyperBlast",
        code=BASE_ID + 87,
        classification=ItemClassification.progression,
    ),
    "Nothing": UT99Item(
        name="Nothing",
        code=BASE_ID + 88,
        classification=ItemClassification.filler,
        placeable=False,
    ),
    "Game Complete": UT99Item(
        name="Game Complete",
        code=BASE_ID + 89,
        classification=ItemClassification.progression,
        placeable=False,
    ),
}
