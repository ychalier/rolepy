class TerrainTile:

    def __init__(self, sprite):
        self.sprite_ = sprite

    def load(self):
        self.sprite_.load()

    def sprite(self):
        return self.sprite_
