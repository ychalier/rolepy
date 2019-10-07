from rolepy.globals import TextureEntities
from rolepy.globals import TextureTerrain
from rolepy.misc import Position


class World:

    def __init__(self):
        self.terrain = dict()
        self.player = TextureEntities.MAN

    def load(self):
        for i in range(-100, 101):
            for j in range(-100, 101):
                self.terrain[Position(i, j)] = TextureTerrain.GRASS
        for i in range(-100, 101):
            self.terrain[Position(0, i)] = TextureTerrain.PAVED_ROAD
            self.terrain[Position(i, 0)] = TextureTerrain.PAVED_ROAD
