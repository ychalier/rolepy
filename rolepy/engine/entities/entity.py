import logging
import time
from rolepy.engine.core.misc import reverse_direction
from rolepy.engine.entities.enums import EntityState
from rolepy.engine.entities import EntityAttributes
from rolepy.engine.entities import Intellect
from rolepy.engine.entities import Behavior
from rolepy.engine.entities import Movement


class Entity:
    """Represent an entity (such as an NPC)."""

    def __init__(self, manager, identifier):
        self.manager = manager
        self.identifier = identifier
        self.attributes = EntityAttributes(self)
        self.intellect = Intellect(self, {0: Behavior()}, {}, 0)

    def __eq__(self, other):
        return self.identifier == other.identifier

    def __hash__(self):
        return hash(self.identifier)

    def __repr__(self):
        return "<Entity {}>".format(self.identifier)

    def take_action(self):
        self.intellect.get().take_action(self)

    def interact(self, inbound_direction=None):
        logging.info("Player is interacting with %s", self)
        if self.attributes.state == EntityState.MOVING:
            self.attributes.set("interrupt_movement", True)
            while self.attributes.state == EntityState.MOVING:
                time.sleep(.001)
        self.attributes.set("state", EntityState.INTERACTING)
        if inbound_direction is not None:
            self.attributes.set("direction", reverse_direction(inbound_direction))
        self.intellect.get().interact(self)
        self.attributes.set("next_movement", -1)
        self.attributes.set("state", EntityState.IDLE)

    def move(self, direction, distance, update=False):
        """Start a thread that will move the entity of a given number of tiles
           in a given direction.
        """
        return Movement(self, direction, distance, update)

    def blit(self, tile_manager, surface, transformer):
        """Blit the entity onto a surface, and transforming its logical position
           into the rendering position through the transformer.
        """
        surface.blit(
            tile_manager.entities[self.attributes.texture].sprite(
                self.attributes.direction,
                self.attributes.posture)
            ,
            transformer(self.attributes.position).pair()
        )