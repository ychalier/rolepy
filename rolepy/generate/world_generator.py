import random as rd
import logging
from rolepy.generate.biomes import Biome
from rolepy.generate.biomes import BiomeMap
from rolepy.generate import Heatmap
from rolepy.engine.terrain import TerrainTexture


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
                TerrainTexture.SAND_0,
                TerrainTexture.SAND_1,
                TerrainTexture.SAND_2,
                TerrainTexture.SAND_3,
                TerrainTexture.SAND_4,
                TerrainTexture.SAND_5
            ]))
        else:
            layers.append(self.choose_version(position, [
                TerrainTexture.GRASS_0,
                TerrainTexture.GRASS_1,
                TerrainTexture.GRASS_2,
                TerrainTexture.GRASS_3,
                TerrainTexture.GRASS_4,
                TerrainTexture.GRASS_5,
                TerrainTexture.GRASS_6
            ]))
        if biome == Biome.FOREST:
            choice = self.choose_version(position, [
                None,
                TerrainTexture.TREE_LARGE,
                TerrainTexture.TREE_SMALL
            ])
            if choice is not None:
                layers.append(choice)
        if biome == Biome.MOUNTAIN:
            choice = self.choose_version(
                position, [None, TerrainTexture.GRASS_MOUNTAIN])
            if choice is not None:
                layers = [choice]
        return layers
