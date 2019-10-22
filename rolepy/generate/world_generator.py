import random as rd
import logging
from rolepy.generate.biomes import Biome
from rolepy.generate.biomes import BiomeMap
from rolepy.generate import Heatmap
from rolepy.globals import TextureTerrain


class WorldGenerator:
    """Aggregation of world generation components."""

    def __init__(self, seed):
        logging.info("Initializing world generator with seed %d", seed)
        self.seed = seed
        self.temperature_heatmap = Heatmap(self.seed * 2)
        self.humidity_heatmap = Heatmap(self.seed * 3)
        self.details_heatmap = Heatmap(self.seed * 4)
        self.versions_heatmap = Heatmap(self.seed * 5)
        self.biome_map = BiomeMap(
            self.temperature_heatmap,
            self.humidity_heatmap
        )

    def choose_version(self, position, variants, multiplier=100):
        """Choose a tile variant in a set of possibilites given the variation
           heatmap.
        """
        version = self.versions_heatmap[position]
        rd.seed(int(multiplier * version))
        return rd.choice(variants)

    def __getitem__(self, position):
        self.biome_map.build([position])
        layers = list()
        biome = self.biome_map[position]
        if biome == Biome.DESERT:
            layers.append(self.choose_version(position, [
                TextureTerrain.SAND_0,
                TextureTerrain.SAND_1,
                TextureTerrain.SAND_2,
                TextureTerrain.SAND_3,
                TextureTerrain.SAND_4,
                TextureTerrain.SAND_5
            ]))
        else:
            layers.append(self.choose_version(position, [
                TextureTerrain.GRASS_0,
                TextureTerrain.GRASS_1,
                TextureTerrain.GRASS_2,
                TextureTerrain.GRASS_3,
                TextureTerrain.GRASS_4,
                TextureTerrain.GRASS_5,
                TextureTerrain.GRASS_6
            ]))
        if biome == Biome.FOREST:
            choice = self.choose_version(position, [
                None,
                TextureTerrain.TREE_LARGE,
                TextureTerrain.TREE_SMALL
            ])
            if choice is not None:
                layers.append(choice)
        if biome == Biome.MOUNTAIN:
            choice = self.choose_version(
                position, [None, TextureTerrain.GRASS_MOUNTAIN])
            if choice is not None:
                layers = [choice]
        return layers
