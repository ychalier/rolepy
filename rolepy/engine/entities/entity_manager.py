import logging
from rolepy.engine.core.globals import SPRITE_SIZE
from rolepy.engine.core.structs import Position
from rolepy.engine.core.misc import front_position
from rolepy.engine.events.implemented import TriggerEvent
from rolepy.engine.events.implemented import InteractionEvent
from rolepy.engine.events.enums import Trigger


def index_entity_position(position):
    """Return the indexing hash of a given position."""
    return position.target()


class EntityManager:
    """Store and handle all entities."""

    def __init__(self, event_manager, resolution):
        super(EntityManager, self).__init__()
        self.event_manager = event_manager
        self.registry = set()
        self.entities = dict()
        self.map = dict()
        width, height = map(lambda x: x // SPRITE_SIZE + 2, resolution)
        self.width = width
        self.height = height
        self.center = None
        self.player = None

    def add(self, entity):
        """Add an entity to the RAM."""
        hashed_position = index_entity_position(entity.attributes.position)
        self.map.setdefault(hashed_position, set())
        self.map[hashed_position].add(entity)
        self.entities[entity] = hashed_position

    def get(self, position, i=None):
        """Return the set of entities at a given position."""
        key = position
        if i is not None:
            key = Position(position, i)
        return self.map.get(key, set())

    def set_player(self, entity):
        """Setter for the entity representing the actual player."""
        self.player = entity

    def set_event_listeners(self, event_manager):
        """Emit event listeners so entities react to interaction and triggers."""
        def interaction_callback(arg):
            arg["listener"].target.interact(arg["keywords"]["direction"])

        def trigger_callback(arg):
            entity = arg["listener"].target
            trigger = arg["listener"].event.trigger
            next_state = entity.intellect.update(trigger)
            if next_state is not None:
                logging.debug("Entity %s switched to state %d",
                              entity, next_state)
        for entity in self.entities:
            event_manager.add_event_listener(
                entity, InteractionEvent(), interaction_callback)
            for trigger_type in Trigger:
                event_manager.add_event_listener(
                    entity, TriggerEvent(trigger_type), trigger_callback)

    def update_entity_position(self, entity):
        """Update the position of one entity."""
        old_position = self.entities[entity].target()
        self.map[old_position].discard(entity)
        if len(self.map[old_position]) == 0:
            del self.map[old_position]
        self.add(entity)

    def update_registry(self):
        """Exhaustive build of entity registry."""
        self.registry.clear()
        for i in range(self.center.y - self.height // 2, self.center.y + self.height // 2 + 1):
            for j in range(self.center.x - self.width // 2, self.center.x + self.width // 2 + 1):
                self.registry |= self.get(j, i)

    def blit(self, tile_manager, surface, transformer):
        """Blit entities within the registry to the screen."""
        for entity in sorted(self.registry, key=lambda e: e.attributes.position.y):
            entity.blit(tile_manager, surface, transformer)

    def detect_interaction(self):
        """Check if the player has an entity to interact with in front of him."""
        attrs = self.player.attributes
        entities = self.get(front_position(attrs.position, attrs.direction))
        if len(entities) > 0:
            entity = list(entities).pop(0)
            self.event_manager.provoke(
                entity, InteractionEvent(), direction=attrs.direction)
