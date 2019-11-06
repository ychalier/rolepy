import os
from rolepy.engine.resources import Sprite
from rolepy.engine.core.enums import Ordinal
from rolepy.engine.entities.enums import Posture


class EntityTile:
    """Handle several keyframes for an entity tile."""

    def __init__(self, path):
        self.sprites = dict()
        for direction in Ordinal:
            self.sprites[direction] = dict()
            for walk_animation in Posture:
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
