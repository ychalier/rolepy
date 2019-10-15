import random as rd
from rolepy.globals import TextureEntities
from rolepy.globals import TextureTerrain
from rolepy.generate import WorldGenerator
from rolepy.misc import Position


class World:

    def __init__(self):
        self.terrain = dict()
        self.player = TextureEntities.MAN
        self.generator = WorldGenerator(1358336837)  # WorldGenerator(rd.randint(0, 2**32-1))

    def load(self):
        for i in range(-100, 101):
            for j in range(-100, 101):
                self.terrain[Position(i, j)] = self.generator[i, j]
