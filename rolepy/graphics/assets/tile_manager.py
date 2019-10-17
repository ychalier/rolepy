import logging
from rolepy.globals import TextureTerrain
from rolepy.globals import TextureEntities
from rolepy.graphics.assets import Sprite
from rolepy.graphics.assets import TerrainTile
from rolepy.graphics.assets import EntityTile


class TileManager:

    def __init__(self):
        self.terrain = dict()
        self.entities = dict()

    def load(self):
        self.terrain[TextureTerrain.EMPTY] = TerrainTile(Sprite(None))
        self.terrain[TextureTerrain.GRASS_0] = TerrainTile(Sprite("assets/terrain/grass_0.png"))
        self.terrain[TextureTerrain.GRASS_1] = TerrainTile(Sprite("assets/terrain/grass_1.png"))
        self.terrain[TextureTerrain.GRASS_2] = TerrainTile(Sprite("assets/terrain/grass_2.png"))
        self.terrain[TextureTerrain.GRASS_3] = TerrainTile(Sprite("assets/terrain/grass_3.png"))
        self.terrain[TextureTerrain.GRASS_4] = TerrainTile(Sprite("assets/terrain/grass_4.png"))
        self.terrain[TextureTerrain.GRASS_5] = TerrainTile(Sprite("assets/terrain/grass_5.png"))
        self.terrain[TextureTerrain.GRASS_6] = TerrainTile(Sprite("assets/terrain/grass_6.png"))
        self.terrain[TextureTerrain.GRASS_MOUNTAIN] = TerrainTile(Sprite("assets/terrain/grass_mountain.png"))
        self.terrain[TextureTerrain.HOUSE_1] = TerrainTile(Sprite("assets/terrain/house_1.png"))
        self.terrain[TextureTerrain.HOUSE_2] = TerrainTile(Sprite("assets/terrain/house_2.png"))
        self.terrain[TextureTerrain.HOUSE_3] = TerrainTile(Sprite("assets/terrain/house_3.png"))
        self.terrain[TextureTerrain.HOUSE_4] = TerrainTile(Sprite("assets/terrain/house_4.png"))
        self.terrain[TextureTerrain.HOUSE_5] = TerrainTile(Sprite("assets/terrain/house_5.png"))
        self.terrain[TextureTerrain.HOUSE_6] = TerrainTile(Sprite("assets/terrain/house_6.png"))
        self.terrain[TextureTerrain.SAND_0] = TerrainTile(Sprite("assets/terrain/sand_0.png"))
        self.terrain[TextureTerrain.SAND_1] = TerrainTile(Sprite("assets/terrain/sand_1.png"))
        self.terrain[TextureTerrain.SAND_2] = TerrainTile(Sprite("assets/terrain/sand_2.png"))
        self.terrain[TextureTerrain.SAND_3] = TerrainTile(Sprite("assets/terrain/sand_3.png"))
        self.terrain[TextureTerrain.SAND_4] = TerrainTile(Sprite("assets/terrain/sand_4.png"))
        self.terrain[TextureTerrain.SAND_5] = TerrainTile(Sprite("assets/terrain/sand_5.png"))
        self.terrain[TextureTerrain.TREE_LARGE] = TerrainTile(Sprite("assets/terrain/tree_large.png"))
        self.terrain[TextureTerrain.TREE_SMALL] = TerrainTile(Sprite("assets/terrain/tree_small.png"))
        self.entities[TextureEntities.MAN] = EntityTile("assets/entities/man")
        self.entities[TextureEntities.WOMAN] = EntityTile("assets/entities/woman")
        for enum, tile in self.terrain.items():
            logging.debug(
                "Loading terrain tile '{name}'".format(name=enum.name))
            tile.load()
        for enum, tile in self.entities.items():
            logging.debug(
                "Loading entity tile '{name}'".format(name=enum.name))
            tile.load()
