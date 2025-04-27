from BaseClasses import ItemClassification


class UT99Item:
    name: str
    id: int
    classification: ItemClassification


BASE_ID = 19991000


item_table: dict[str, UT99Item] = {
    # Deathmatch Maps - Unlocked
    "Stalwart": UT99Item(
        name="DM-Stalwart - Unlock",
        id=BASE_ID + 17,
        classification=ItemClassification.progression,
    ),
    "Fractal": UT99Item(
        name="DM-Fractal - Unlock",
        id=BASE_ID + 18,
        classification=ItemClassification.progression,
    ),
    "Turbine": UT99Item(
        name="DM-Turbine - Unlock",
        id=BASE_ID + 19,
        classification=ItemClassification.progression,
    ),
    "Codex": UT99Item(
        name="DM-Codex - Unlock",
        id=BASE_ID + 20,
        classification=ItemClassification.progression,
    ),
    "Pressure": UT99Item(
        name="DM-Pressure - Unlock",
        id=BASE_ID + 21,
        classification=ItemClassification.progression,
    ),
    "Arcane": UT99Item(
        name="DM-ArcaneTemple - Unlock",
        id=BASE_ID + 22,
        classification=ItemClassification.progression,
    ),
    "Grinder": UT99Item(
        name="DM-Grinder - Unlock",
        id=BASE_ID + 23,
        classification=ItemClassification.progression,
    ),
    "Malevolence": UT99Item(
        name="DM-Malevolence - Unlock",
        id=BASE_ID + 24,
        classification=ItemClassification.progression,
    ),
    "Galleon": UT99Item(
        name="DM-KGalleon - Unlock",
        id=BASE_ID + 25,
        classification=ItemClassification.progression,
    ),
    "Tempest": UT99Item(
        name="DM-Tempest - Unlock",
        id=BASE_ID + 26,
        classification=ItemClassification.progression,
    ),
    "Barricade": UT99Item(
        name="DM-Barricade - Unlock",
        id=BASE_ID + 27,
        classification=ItemClassification.progression,
    ),
    "Shrapnel": UT99Item(
        name="DM-Shrapnel][ - Unlock",
        id=BASE_ID + 28,
        classification=ItemClassification.progression,
    ),
    "Liandri": UT99Item(
        name="DM-Liandri - Unlock",
        id=BASE_ID + 29,
        classification=ItemClassification.progression,
    ),
    "Conveyor": UT99Item(
        name="DM-Conveyor - Unlock",
        id=BASE_ID + 30,
        classification=ItemClassification.progression,
    ),
    "Peak": UT99Item(
        name="DM-Peak - Unlock",
        id=BASE_ID + 31,
        classification=ItemClassification.progression,
    ),
    # Domination Maps - Unlocked
    "Ghardhen": UT99Item(
        name="DOM-Ghardhen - Unlock",
        id=BASE_ID + 41,
        classification=ItemClassification.progression,
    ),
    "Cryptic": UT99Item(
        name="DOM-Cryptic - Unlock",
        id=BASE_ID + 42,
        classification=ItemClassification.progression,
    ),
    "Cinder": UT99Item(
        name="DOM-Cinder - Unlock",
        id=BASE_ID + 43,
        classification=ItemClassification.progression,
    ),
    "Gearbolt": UT99Item(
        name="DOM-Gearbolt - Unlock",
        id=BASE_ID + 44,
        classification=ItemClassification.progression,
    ),
    "Leadworks": UT99Item(
        name="DOM-Leadworks - Unlock",
        id=BASE_ID + 45,
        classification=ItemClassification.progression,
    ),
    "Olden": UT99Item(
        name="DOM-Olden - Unlock",
        id=BASE_ID + 46,
        classification=ItemClassification.progression,
    ),
    "Sesmar": UT99Item(
        name="DOM-Sesmar - Unlock",
        id=BASE_ID + 47,
        classification=ItemClassification.progression,
    ),
    "MetalDream": UT99Item(
        name="DOM-MetalDream - Unlock",
        id=BASE_ID + 48,
        classification=ItemClassification.progression,
    ),
    # Capture the Flag Maps - Unlocked
    "Facing Worlds": UT99Item(
        name="CTF-Face - Unlock",
        id=BASE_ID + 60,
        classification=ItemClassification.progression,
    ),
    "Eternal Cave": UT99Item(
        name="CTF-EternalCave - Unlock",
        id=BASE_ID + 61,
        classification=ItemClassification.progression,
    ),
    "Coret": UT99Item(
        name="CTF-Coret - Unlock",
        id=BASE_ID + 62,
        classification=ItemClassification.progression,
    ),
    "The Gauntlet": UT99Item(
        name="CTF-Gauntlet - Unlock",
        id=BASE_ID + 63,
        classification=ItemClassification.progression,
    ),
    "Dreary": UT99Item(
        name="CTF-Dreary - Unlock",
        id=BASE_ID + 64,
        classification=ItemClassification.progression,
    ),
    "Last Command": UT99Item(
        name="CTF-Command - Unlock",
        id=BASE_ID + 65,
        classification=ItemClassification.progression,
    ),
    "The Lava Giant": UT99Item(
        name="CTF-LavaGiant - Unlock",
        id=BASE_ID + 66,
        classification=ItemClassification.progression,
    ),
    "November Sub Pen": UT99Item(
        name="CTF-November - Unlock",
        id=BASE_ID + 67,
        classification=ItemClassification.progression,
    ),
    "Hydro": UT99Item(
        name="CTF-Hydro16 - Unlock",
        id=BASE_ID + 68,
        classification=ItemClassification.progression,
    ),
    "Orbital": UT99Item(
        name="CTF-Orbital - Unlock",
        id=BASE_ID + 69,
        classification=ItemClassification.progression,
    ),
    # Assault Maps - Unlocked
    "High Speed": UT99Item(
        name="AS-HiSpeed - Unlock",
        id=BASE_ID + 76,
        classification=ItemClassification.progression,
    ),
    "Rook": UT99Item(
        name="AS-Rook - Unlock",
        id=BASE_ID + 77,
        classification=ItemClassification.progression,
    ),
    "Mazon": UT99Item(
        name="AS-Mazon - Unlock",
        id=BASE_ID + 78,
        classification=ItemClassification.progression,
    ),
    "Ocean Floor": UT99Item(
        name="AS-OceanFloor - Unlock",
        id=BASE_ID + 79,
        classification=ItemClassification.progression,
    ),
    "Overlord": UT99Item(
        name="AS-Overlord - Unlock",
        id=BASE_ID + 80,
        classification=ItemClassification.progression,
    ),
    # Challenge Maps - Unlocked
    "Morpheus": UT99Item(
        name="DM-Morpheus - Unlock",
        id=BASE_ID + 85,
        classification=ItemClassification.progression,
    ),
    "Zeto": UT99Item(
        name="DM-Zeto - Unlock",
        id=BASE_ID + 86,
        classification=ItemClassification.progression,
    ),
    "HyperBlast": UT99Item(
        name="DM-HyperBlast - Unlock",
        id=BASE_ID + 87,
        classification=ItemClassification.progression,
    ),
    # Ladders
    "Deathmatch Ladder Receive": UT99Item(
        name="Deathmatch Ladder - Unlock",
        id=BASE_ID + 89,
        classification=ItemClassification.progression,
    ),
    "Domination Ladder Receive": UT99Item(
        name="Domination Ladder - Unlock",
        id=BASE_ID + 91,
        classification=ItemClassification.progression,
    ),
    "CTF Ladder Receive": UT99Item(
        name="CTF Ladder - Unlock",
        id=BASE_ID + 93,
        classification=ItemClassification.progression,
    ),
    "Assault Ladder Receive": UT99Item(
        name="Assault Ladder - Unlock",
        id=BASE_ID + 95,
        classification=ItemClassification.progression,
    ),
    "Challenge Ladder Receive": UT99Item(
        name="Challenge Ladder - Unlock",
        id=BASE_ID + 97,
        classification=ItemClassification.progression,
    ),
}
