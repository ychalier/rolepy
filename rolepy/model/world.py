import time
import logging
import random as rd
from rolepy.globals import TextureEntities
from rolepy.globals import TextureTerrain
from rolepy.generate import WorldGenerator
from rolepy.generate.biomes import Biome
from rolepy.generate.biomes import Zone
from rolepy.misc import Position


class World:

    def __init__(self):
        self.terrain = dict()
        self.player = TextureEntities.MAN
        self.generator = WorldGenerator(1358336837)  # WorldGenerator(rd.randint(0, 2**32-1))
        self.zones = list()
        self.zones_map = dict()

    def generate(self, x, y):
        self.terrain[Position(x, y)] = self.generator[y, x]

    def load(self):
        for x in range(-100, 101):
            for y in range(-100, 101):
                self.generate(x, y)
