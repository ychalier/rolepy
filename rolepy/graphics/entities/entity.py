from rolepy.globals import WalkAnimation
from rolepy.globals import Ordinal
from rolepy.misc import Position
from rolepy.graphics.entities import EntityMovement


class Entity:
    """Represent a graphic entity (such as NPCs)."""

    def __init__(self, manager, identifier, tile, **kwargs):
        self.manager = manager
        self.identifier = identifier
        self.tile = tile
        self.position = Position(0, 0)
        self.speed = 3
        self.brain = None
        self.direction = Ordinal.SOUTH
        self.walk_animation = WalkAnimation.REST
        for arg_name, arg_value in kwargs.items():
            setattr(self, arg_name, arg_value)
        self.thinking = True

    def __eq__(self, other):
        return self.identifier == other.identifier

    def __hash__(self):
        return hash(self.identifier)

    def __repr__(self):
        return "<Entity {}>".format(self.identifier)

    def think(self):
        """Perform one step of entity own AI."""
        if self.brain is not None:
            self.brain.iterate(self)

    def blit(self, surface, transformer):
        """Blit the entity onto a surface, and transforming its logical position
           into the rendering position through the transformer.
        """
        surface.blit(
            self.tile.sprite(self.direction, self.walk_animation),
            transformer(self.position).pair()
        )

    def move(self, direction, distance):
        """Start a thread that will move the entity of a given number of tiles
           in a given direction.
        """
        return EntityMovement(self, direction, distance)
