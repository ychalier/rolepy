import random as rd
from rolepy.generate.biomes import Biome
from rolepy.generate.biomes import BiomeMap
from rolepy.generate import Heatmap
from rolepy.globals import TextureTerrain


class WorldGenerator:

    def __init__(self, seed):
        self.seed = seed
        self.temperature_heatmap = Heatmap(self.seed * 2)
        self.humidity_heatmap = Heatmap(self.seed * 3)
        self.biome_map = BiomeMap(self.temperature_heatmap, self.humidity_heatmap)

    def __getitem__(self, position):
        self.biome_map.build([position])
        if self.biome_map[position] in [Biome.PLAIN, Biome.FOREST]:
            return [TextureTerrain.GRASS]
        return [TextureTerrain.PAVED_ROAD]
