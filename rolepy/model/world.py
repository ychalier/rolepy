from rolepy.generate import WorldGenerator
from rolepy.generate.biomes import Biome
from rolepy.generate.biomes import Zone
from rolepy.engine.core.structs import Position
from rolepy.model.player import Player


class World:
    """Model of the world, containing the player, the terrain and the entities."""

    def __init__(self):
        self.terrain = dict()
        self.generator = WorldGenerator(1358336837)  # WorldGenerator(rd.randint(0, 2**32-1))
        self.zones = list()
        self.zones_map = dict()
        self.player = Player()

    def generate(self, x, y):
        """Load the generated terrain at a given position."""
        self.terrain[Position(x, y)] = self.generator[y, x]

    def get_zone(self, x_float, y_float):
        """If known, return the name of the zone at a given position."""
        x = round(x_float)
        y = round(y_float)
        if self.generator.biome_map[y, x] == Biome.PLAIN:
            return Zone(Biome.PLAIN)
        if Position(x, y) in self.zones_map:
            return self.zones_map[Position(x, y)]
        return None

    def to_dict(self):
        return [
            {
                "x": position.x,
                "y": position.y,
                "l": [
                    layer.value for layer in layers
                ],
                "z": self.zones_map.get(position, None)
            }
            for position, layers in self.terrain.items()
        ]
