from rolepy.graphics import Tile


class TerrainTile(Tile):

    def __init__(self, sprite):
        Tile.__init__(self)
        self.sprite_ = sprite

    def load(self):
        self.sprite_.load()

    def sprite(self):
        return self.sprite_
