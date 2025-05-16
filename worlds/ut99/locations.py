from BaseClasses import Location


class UT99Location(Location):
    __slots__ = ("name", "id", "ladder")

    def __init__(
        self,
        name: str,
        address: int,
        ladder: str,
        player: int = 1,
    ):
        # Use the base Location constructor
        super().__init__(
            player=player,
            name=name,
            address=address,
        )
        self.ladder = ladder


BASE_ID = 19992000

location_table: dict[str, UT99Location] = {
    # Deathmatch names - Beaten
    "DM-Oblivion": UT99Location(
        name="DM-Oblivion",
        address=BASE_ID + 17,
        ladder="DM",
    ),
    "DM-Stalwart": UT99Location(
        name="DM-Stalwart",
        address=BASE_ID + 18,
        ladder="DM",
    ),
    "DM-Fractal": UT99Location(
        name="DM-Fractal",
        address=BASE_ID + 19,
        ladder="DM",
    ),
    "DM-Turbine": UT99Location(
        name="DM-Turbine",
        address=BASE_ID + 20,
        ladder="DM",
    ),
    "DM-Codex": UT99Location(
        name="DM-Codex",
        address=BASE_ID + 21,
        ladder="DM",
    ),
    "DM-Pressure": UT99Location(
        name="DM-Pressure",
        address=BASE_ID + 22,
        ladder="DM",
    ),
    "DM-ArcaneTemple": UT99Location(
        name="DM-ArcaneTemple",
        address=BASE_ID + 23,
        ladder="DM",
    ),
    "DM-Grinder": UT99Location(
        name="DM-Grinder",
        address=BASE_ID + 24,
        ladder="DM",
    ),
    "DM-Malevolence": UT99Location(
        name="DM-Malevolence",
        address=BASE_ID + 25,
        ladder="DM",
    ),
    "DM-KGalleon": UT99Location(
        name="DM-KGalleon",
        address=BASE_ID + 26,
        ladder="DM",
    ),
    "DM-Tempest": UT99Location(
        name="DM-Tempest",
        address=BASE_ID + 27,
        ladder="DM",
    ),
    "DM-Shrapnel][": UT99Location(
        name="DM-Shrapnel][",
        address=BASE_ID + 29,
        ladder="DM",
    ),
    "DM-Liandri": UT99Location(
        name="DM-Liandri",
        address=BASE_ID + 30,
        ladder="DM",
    ),
    "DM-Conveyor": UT99Location(
        name="DM-Conveyor",
        address=BASE_ID + 31,
        ladder="DM",
    ),
    "DM-Peak": UT99Location(
        name="DM-Peak",
        address=BASE_ID + 32,
        ladder="DM",
    ),
    # Domination names - Beaten
    "DOM-Condemned": UT99Location(
        name="DOM-Condemned",
        address=BASE_ID + 33,
        ladder="DOM",
    ),
    "DOM-Ghardhen": UT99Location(
        name="DOM-Ghardhen",
        address=BASE_ID + 34,
        ladder="DOM",
    ),
    "DOM-Cryptic": UT99Location(
        name="DOM-Cryptic",
        address=BASE_ID + 35,
        ladder="DOM",
    ),
    "DOM-Cinder": UT99Location(
        name="DOM-Cinder",
        address=BASE_ID + 36,
        ladder="DOM",
    ),
    "DOM-Gearbolt": UT99Location(
        name="DOM-Gearbolt",
        address=BASE_ID + 37,
        ladder="DOM",
    ),
    "DOM-Leadworks": UT99Location(
        name="DOM-Leadworks",
        address=BASE_ID + 38,
        ladder="DOM",
    ),
    "DOM-Olden": UT99Location(
        name="DOM-Olden",
        address=BASE_ID + 39,
        ladder="DOM",
    ),
    "DOM-Sesmar": UT99Location(
        name="DOM-Sesmar",
        address=BASE_ID + 40,
        ladder="DOM",
    ),
    "DOM-MetalDream": UT99Location(
        name="DOM-MetalDream",
        address=BASE_ID + 41,
        ladder="DOM",
    ),
    # Capture the Flag names - Beaten
    "CTF-Niven": UT99Location(
        name="CTF-Niven",
        address=BASE_ID + 42,
        ladder="CTF",
    ),
    "CTF-Face": UT99Location(
        name="CTF-Face",
        address=BASE_ID + 43,
        ladder="CTF",
    ),
    "CTF-EternalCave": UT99Location(
        name="CTF-EternalCave",
        address=BASE_ID + 44,
        ladder="CTF",
    ),
    "CTF-Coret": UT99Location(
        name="CTF-Coret",
        address=BASE_ID + 45,
        ladder="CTF",
    ),
    "CTF-Gauntlet": UT99Location(
        name="CTF-Gauntlet",
        address=BASE_ID + 46,
        ladder="CTF",
    ),
    "CTF-Dreary": UT99Location(
        name="CTF-Dreary",
        address=BASE_ID + 47,
        ladder="CTF",
    ),
    "CTF-Command": UT99Location(
        name="CTF-Command",
        address=BASE_ID + 48,
        ladder="CTF",
    ),
    "CTF-LavaGiant": UT99Location(
        name="CTF-LavaGiant",
        address=BASE_ID + 49,
        ladder="CTF",
    ),
    "CTF-November": UT99Location(
        name="CTF-November",
        address=BASE_ID + 50,
        ladder="CTF",
    ),
    "CTF-Hydro16": UT99Location(
        name="CTF-Hydro16",
        address=BASE_ID + 51,
        ladder="CTF",
    ),
    "CTF-Orbital": UT99Location(
        name="CTF-Orbital",
        address=BASE_ID + 52,
        ladder="CTF",
    ),
    # Assault names - Beaten
    "AS-Frigate": UT99Location(
        name="AS-Frigate",
        address=BASE_ID + 53,
        ladder="AS",
    ),
    "AS-HiSpeed": UT99Location(
        name="AS-HiSpeed",
        address=BASE_ID + 54,
        ladder="AS",
    ),
    "AS-Rook": UT99Location(
        name="AS-Rook",
        address=BASE_ID + 55,
        ladder="AS",
    ),
    "AS-Mazon": UT99Location(
        name="AS-Mazon",
        address=BASE_ID + 56,
        ladder="AS",
    ),
    "AS-OceanFloor": UT99Location(
        name="AS-OceanFloor",
        address=BASE_ID + 57,
        ladder="AS",
    ),
    "AS-Overlord": UT99Location(
        name="AS-Overlord",
        address=BASE_ID + 58,
        ladder="AS",
    ),
    # Challenge names - Beaten
    "DM-Phobos": UT99Location(
        name="DM-Phobos",
        address=BASE_ID + 59,
        ladder="Chal",
    ),
    "DM-Morpheus": UT99Location(
        name="DM-Morpheus",
        address=BASE_ID + 60,
        ladder="Chal",
    ),
    "DM-Zeto": UT99Location(
        name="DM-Zeto",
        address=BASE_ID + 61,
        ladder="Chal",
    ),
    "DM-HyperBlast": UT99Location(
        name="DM-HyperBlast",
        address=BASE_ID + 62,
        ladder="Chal",
    ),
}
