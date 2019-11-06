import logging
from rolepy.engine.terrain import TerrainTexture
from rolepy.engine.entities.enums import EntityTexture
from rolepy.engine.resources import Sprite
from rolepy.engine.resources import TerrainTile
from rolepy.engine.resources import EntityTile


class TileManager:
    """Aggregates all tiles."""

    def __init__(self):
        self.terrain = dict()
        self.entities = dict()

    def load(self):
        """Load all sprites."""
        self.terrain[TerrainTexture.EMPTY] = TerrainTile(Sprite(None))
        self.terrain[TerrainTexture.GRASS_0] = \
            TerrainTile(Sprite("assets/terrain/grass_0.png"))
        self.terrain[TerrainTexture.GRASS_1] = \
            TerrainTile(Sprite("assets/terrain/grass_1.png"))
        self.terrain[TerrainTexture.GRASS_2] = \
            TerrainTile(Sprite("assets/terrain/grass_2.png"))
        self.terrain[TerrainTexture.GRASS_3] = \
            TerrainTile(Sprite("assets/terrain/grass_3.png"))
        self.terrain[TerrainTexture.GRASS_4] = \
            TerrainTile(Sprite("assets/terrain/grass_4.png"))
        self.terrain[TerrainTexture.GRASS_5] = \
            TerrainTile(Sprite("assets/terrain/grass_5.png"))
        self.terrain[TerrainTexture.GRASS_6] = \
            TerrainTile(Sprite("assets/terrain/grass_6.png"))
        self.terrain[TerrainTexture.GRASS_MOUNTAIN] = \
            TerrainTile(Sprite("assets/terrain/grass_mountain.png"))
        self.terrain[TerrainTexture.HOUSE_1] = \
            TerrainTile(Sprite("assets/terrain/house_1.png"))
        self.terrain[TerrainTexture.HOUSE_2] = \
            TerrainTile(Sprite("assets/terrain/house_2.png"))
        self.terrain[TerrainTexture.HOUSE_3] = \
            TerrainTile(Sprite("assets/terrain/house_3.png"))
        self.terrain[TerrainTexture.HOUSE_4] = \
            TerrainTile(Sprite("assets/terrain/house_4.png"))
        self.terrain[TerrainTexture.HOUSE_5] = \
            TerrainTile(Sprite("assets/terrain/house_5.png"))
        self.terrain[TerrainTexture.HOUSE_6] = \
            TerrainTile(Sprite("assets/terrain/house_6.png"))
        self.terrain[TerrainTexture.SAND_0] = \
            TerrainTile(Sprite("assets/terrain/sand_0.png"))
        self.terrain[TerrainTexture.SAND_1] = \
            TerrainTile(Sprite("assets/terrain/sand_1.png"))
        self.terrain[TerrainTexture.SAND_2] = \
            TerrainTile(Sprite("assets/terrain/sand_2.png"))
        self.terrain[TerrainTexture.SAND_3] = \
            TerrainTile(Sprite("assets/terrain/sand_3.png"))
        self.terrain[TerrainTexture.SAND_4] = \
            TerrainTile(Sprite("assets/terrain/sand_4.png"))
        self.terrain[TerrainTexture.SAND_5] = \
            TerrainTile(Sprite("assets/terrain/sand_5.png"))
        self.terrain[TerrainTexture.TREE_LARGE] = \
            TerrainTile(Sprite("assets/terrain/tree_large.png"))
        self.terrain[TerrainTexture.TREE_SMALL] = \
            TerrainTile(Sprite("assets/terrain/tree_small.png"))
        self.entities[EntityTexture.MAN] = \
            EntityTile("assets/entities/man")
        self.entities[EntityTexture.WOMAN] = \
            EntityTile("assets/entities/woman")
        for enum, tile in self.terrain.items():
            logging.debug("Loading terrain tile '%s'", enum.name)
            tile.load()
        for enum, tile in self.entities.items():
            logging.debug("Loading entity tile '%s'", enum.name)
            tile.load()
