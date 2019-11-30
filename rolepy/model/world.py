from rolepy.generate import WorldGenerator
from rolepy.generate.biomes import Biome
from rolepy.generate.biomes import Zone
from rolepy.engine.core.structs import Position
from rolepy.engine.terrain import TerrainTexture
from rolepy.model.player import Player


class World:
    """Model of the world, containing the player, the terrain and the entities."""

    def __init__(self):
        self.terrain = dict()
        self.generator = WorldGenerator(1358336837)  # WorldGenerator(rd.randint(0, 2**32-1))
        self.zones = list()
        self.zones_map = dict()
        self.player = Player()
        self.modified = list()

    def generate(self, x, y):
        """Load the generated terrain at a given position."""
        self.terrain[Position(x, y)] = self.generator[y, x]

    def get_zone(self, x_float, y_float):
        """If known, return the name of the zone at a given position."""
        x = round(x_float)
        y = round(y_float)
        biome = self.generator.biome_map.get((y, x), None)
        if biome is None:
            self.generator.biome_map.build([(y, x)])
            biome = self.generator.biome_map[y, x]
        if biome == Biome.PLAIN:
            return Zone(Biome.PLAIN)
        if Position(x, y) in self.zones_map:
            return self.zones_map[Position(x, y)]
        return None

    def to_dict(self):
        terrain_list = list()
        for position in self.modified:
            d = {
                "x": position.x,
                "y": position.y,
                "l": [
                    layer.value for layer in self.terrain[position]
                ]
            }
            zone = self.zones_map.get(position, None)
            if zone is not None:
                d["z"] = zone
            terrain_list.append(d)
        return {
            "seed": self.generator.seed,
            "terrain": terrain_list
        }

    def from_dict(self, d):
        self.generator = WorldGenerator(d["seed"])
        for tile in d["terrain"]:
            position = Position(tile["x"], tile["y"])
            layers = [
                TerrainTexture(layer)
                for layer in tile["l"]
            ]
            zone = d.get("z", None)
            self.terrain[position] = layers
            if zone is not None:
                self.zones_map[position] = zone
