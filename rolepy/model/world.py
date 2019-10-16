import time
import logging
import random as rd
from rolepy.globals import TextureTerrain
from rolepy.generate import WorldGenerator
from rolepy.generate.biomes import Biome
from rolepy.generate.biomes import Zone
from rolepy.misc import Position
from rolepy.model.player import Player


class World:

    def __init__(self):
        self.terrain = dict()
        self.generator = WorldGenerator(1358336837)  # WorldGenerator(rd.randint(0, 2**32-1))
        self.zones = list()
        self.zones_map = dict()
        self.player = Player()

    def generate(self, x, y):
        self.terrain[Position(x, y)] = self.generator[y, x]

    def load(self):
        for x in range(-100, 101):
            for y in range(-100, 101):
                self.generate(x, y)
