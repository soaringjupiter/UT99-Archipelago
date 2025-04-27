class UT99Location:
    map: str
    id: int


BASE_ID = 19992000

location_table: dict[str, UT99Location] = {
    # Deathmatch Maps - Beaten
    "Oblivion": UT99Location(
        map="DM-Oblivion - Beaten",
        id=BASE_ID + 17,
    ),
    "Stalwart": UT99Location(
        map="DM-Stalwart - Beaten",
        id=BASE_ID + 18,
    ),
    "Fractal": UT99Location(
        map="DM-Fractal - Beaten",
        id=BASE_ID + 19,
    ),
    "Turbine": UT99Location(
        map="DM-Turbine - Beaten",
        id=BASE_ID + 20,
    ),
    "Codex": UT99Location(
        map="DM-Codex - Beaten",
        id=BASE_ID + 21,
    ),
    "Pressure": UT99Location(
        map="DM-Pressure - Beaten",
        id=BASE_ID + 22,
    ),
    "Arcane": UT99Location(
        map="DM-ArcaneTemple - Beaten",
        id=BASE_ID + 23,
    ),
    "Grinder": UT99Location(
        map="DM-Grinder - Beaten",
        id=BASE_ID + 24,
    ),
    "Malevolence": UT99Location(
        map="DM-Malevolence - Beaten",
        id=BASE_ID + 25,
    ),
    "Galleon": UT99Location(
        map="DM-KGalleon - Beaten",
        id=BASE_ID + 26,
    ),
    "Tempest": UT99Location(
        map="DM-Tempest - Beaten",
        id=BASE_ID + 27,
    ),
    "Barricade": UT99Location(
        map="DM-Barricade - Beaten",
        id=BASE_ID + 28,
    ),
    "Shrapnel": UT99Location(
        map="DM-Shrapnel][ - Beaten",
        id=BASE_ID + 29,
    ),
    "Liandri": UT99Location(
        map="DM-Liandri - Beaten",
        id=BASE_ID + 30,
    ),
    "Conveyor": UT99Location(
        map="DM-Conveyor - Beaten",
        id=BASE_ID + 31,
    ),
    "Peak": UT99Location(
        map="DM-Peak - Beaten",
        id=BASE_ID + 32,
    ),
    # Domination Maps - Beaten
    "Condemned": UT99Location(
        map="DOM-Condemned - Beaten",
        id=BASE_ID + 33,
    ),
    "Ghardhen": UT99Location(
        map="DOM-Ghardhen - Beaten",
        id=BASE_ID + 34,
    ),
    "Cryptic": UT99Location(
        map="DOM-Cryptic - Beaten",
        id=BASE_ID + 35,
    ),
    "Cinder": UT99Location(
        map="DOM-Cinder - Beaten",
        id=BASE_ID + 36,
    ),
    "Gearbolt": UT99Location(
        map="DOM-Gearbolt - Beaten",
        id=BASE_ID + 37,
    ),
    "Leadworks": UT99Location(
        map="DOM-Leadworks - Beaten",
        id=BASE_ID + 38,
    ),
    "Olden": UT99Location(
        map="DOM-Olden - Beaten",
        id=BASE_ID + 39,
    ),
    "Sesmar": UT99Location(
        map="DOM-Sesmar - Beaten",
        id=BASE_ID + 40,
    ),
    "MetalDream": UT99Location(
        map="DOM-MetalDream - Beaten",
        id=BASE_ID + 41,
    ),
    # Capture the Flag Maps - Beaten
    "Niven": UT99Location(
        map="CTF-Niven - Beaten",
        id=BASE_ID + 42,
    ),
    "Facing Worlds": UT99Location(
        map="CTF-Face - Beaten",
        id=BASE_ID + 43,
    ),
    "Eternal Cave": UT99Location(
        map="CTF-EternalCave - Beaten",
        id=BASE_ID + 44,
    ),
    "Coret": UT99Location(
        map="CTF-Coret - Beaten",
        id=BASE_ID + 45,
    ),
    "The Gauntlet": UT99Location(
        map="CTF-Gauntlet - Beaten",
        id=BASE_ID + 46,
    ),
    "Dreary": UT99Location(
        map="CTF-Dreary - Beaten",
        id=BASE_ID + 47,
    ),
    "Last Command": UT99Location(
        map="CTF-Command - Beaten",
        id=BASE_ID + 48,
    ),
    "The Lava Giant": UT99Location(
        map="CTF-LavaGiant - Beaten",
        id=BASE_ID + 49,
    ),
    "November Sub Pen": UT99Location(
        map="CTF-November - Beaten",
        id=BASE_ID + 50,
    ),
    "Hydro": UT99Location(
        map="CTF-Hydro16 - Beaten",
        id=BASE_ID + 51,
    ),
    "Orbital": UT99Location(
        map="CTF-Orbital - Beaten",
        id=BASE_ID + 52,
    ),
    # Assault Maps - Beaten
    "Frigate": UT99Location(
        map="AS-Frigate - Beaten",
        id=BASE_ID + 53,
    ),
    "High Speed": UT99Location(
        map="AS-HiSpeed - Beaten",
        id=BASE_ID + 54,
    ),
    "Rook": UT99Location(
        map="AS-Rook - Beaten",
        id=BASE_ID + 55,
    ),
    "Mazon": UT99Location(
        map="AS-Mazon - Beaten",
        id=BASE_ID + 56,
    ),
    "Ocean Floor": UT99Location(
        map="AS-OceanFloor - Beaten",
        id=BASE_ID + 57,
    ),
    "Overlord": UT99Location(
        map="AS-Overlord - Beaten",
        id=BASE_ID + 58,
    ),
    # Challenge Maps - Beaten
    "Phobos": UT99Location(
        map="DM-Phobos - Beaten",
        id=BASE_ID + 59,
    ),
    "Morpheus": UT99Location(
        map="DM-Morpheus - Beaten",
        id=BASE_ID + 60,
    ),
    "Zeto": UT99Location(
        map="DM-Zeto - Beaten",
        id=BASE_ID + 61,
    ),
    "HyperBlast": UT99Location(
        map="DM-Hyperblast - Beaten",
        id=BASE_ID + 62,
    ),
}
