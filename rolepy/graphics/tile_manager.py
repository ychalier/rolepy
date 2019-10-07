import logging
from rolepy.graphics import Sprite
from rolepy.globals import TextureTerrain
from rolepy.globals import TextureEntities
from rolepy.graphics import TerrainTile
from rolepy.graphics import EntityTile


class TileManager:

    def __init__(self):
        self.terrain = dict()
        self.entities = dict()

    def load(self):
        self.terrain[TextureTerrain.EMPTY] = TerrainTile(Sprite(None))
        self.terrain[TextureTerrain.GRASS] = TerrainTile(
            Sprite("assets/terrain/grass.png"))
        self.terrain[TextureTerrain.PAVED_ROAD] = TerrainTile(
            Sprite("assets/terrain/paved_road.png"))
        self.entities[TextureEntities.MAN] = EntityTile("assets/entities/man")
        for enum, tile in self.terrain.items():
            logging.debug(
                "Loading terrain tile '{name}'".format(name=enum.name))
            tile.load()
        for enum, tile in self.entities.items():
            logging.debug(
                "Loading entity tile '{name}'".format(name=enum.name))
            tile.load()
