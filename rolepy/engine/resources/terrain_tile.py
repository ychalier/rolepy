class TerrainTile:
    """Represent a terrain tile."""
    # TODO: Add tile informative features

    def __init__(self, sprite):
        self.sprite_ = sprite

    def load(self):
        """Load the sprite."""
        self.sprite_.load()

    def sprite(self):
        """Return the sprite surface."""
        return self.sprite_
