import time
import threading
from rolepy.globals import SPRITE_SIZE
from rolepy.globals import WalkAnimation
from rolepy.globals import Ordinal
from rolepy.misc import Position
from rolepy.graphics.entities import EntityMovement


class Entity:

    def __init__(self, manager, identifier, tile, position, speed=3, ai=None):
        self.manager = manager
        self.id = identifier
        self.tile = tile
        self.position = position
        self.ai = ai
        self.last_ai_step = 0
        self.time_since_last_ai_step = 0
        self.speed = speed
        self.direction = Ordinal.SOUTH
        self.walk_animation = WalkAnimation.REST
        self.thinking = True

    def __eq__(self, other):
        return self.id == other.id

    def __hash__(self):
        return hash(self.id)

    def __repr__(self):
        return "<Entity {}>".format(self.id)

    def ai_step(self):
        now = time.time()
        self.time_since_last_ai_step = now - self.last_ai_step
        self.last_ai_step = now
        if self.ai is not None:
            self.ai.iterate(self)

    def blit(self, surface, transformer):
        surface.blit(
            self.tile.sprite(self.direction, self.walk_animation),
            transformer(self.position).pair()
        )

    def move(self, direction, distance):
        return EntityMovement(self, direction, distance)
