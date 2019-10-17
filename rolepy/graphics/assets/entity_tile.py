import os
from rolepy.graphics.assets import Tile
from rolepy.graphics.assets import Sprite
from rolepy.globals import Ordinal
from rolepy.globals import WalkAnimation


class EntityTile(Tile):

    def __init__(self, path):
        Tile.__init__(self)
        self.direction = Ordinal.SOUTH
        self.walk_animation = WalkAnimation.REST
        self.sprites = dict()
        for direction in Ordinal:
            self.sprites[direction] = dict()
            for walk_animation in WalkAnimation:
                self.sprites[direction][walk_animation] = Sprite(os.path.join(
                    path,
                    direction.name.lower(),
                    str(walk_animation.value) + ".png"
                ))

    def load(self):
        for direction in self.sprites:
            for walk_animation in self.sprites[direction]:
                self.sprites[direction][walk_animation].load()

    def sprite(self):
        return self.sprites[self.direction][self.walk_animation]
