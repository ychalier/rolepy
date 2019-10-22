import os
from rolepy.graphics.assets import Sprite
from rolepy.globals import Ordinal
from rolepy.globals import WalkAnimation


class EntityTile:
    """Handle several keyframes for an entity tile."""

    def __init__(self, path):
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
        """Load a sprite image."""
        for direction in self.sprites:
            for walk_animation in self.sprites[direction]:
                self.sprites[direction][walk_animation].load()

    def sprite(self, direction, walk_animation):
        """Return the sprite corresponding to the current direction and
           animation keyframe.
        """
        return self.sprites[direction][walk_animation]
