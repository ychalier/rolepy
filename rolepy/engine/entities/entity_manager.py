import logging
from rolepy.engine.core.globals import SPRITE_SIZE
from rolepy.engine.core.structs import Position
from rolepy.engine.core.misc import front_position
from rolepy.engine.events.implemented import TriggerEvent
from rolepy.engine.events.implemented import InteractionEvent
from rolepy.engine.events.implemented import DialogCloseEvent
from rolepy.engine.events.enums import Trigger


def index_entity_position(position):
    """Return the indexing hash of a given position."""
    return position.target()


class EntityManager:
    """Store and handle all entities."""

    def __init__(self, game):
        super(EntityManager, self).__init__()
        self.game = game
        self.event_manager = game.event_manager
        resolution = game.settings.resolution
        self.registry = set()
        self.entities = dict()
        self.map = dict()
        width, height = map(lambda x: x // SPRITE_SIZE + 2, resolution)
        self.width = width
        self.height = height
        self.center = None
        self.player = None

    def load(self, camera, population, event_manager, loading_screen):
        """Load entities from a population and setup event listeners."""
        loading_screen.next_step("Loading entities", len(population) + 2)
        self.center = camera.target()
        for entity in population.values():
            loading_screen.next_sub_step("Loading %s" % entity)
            self.add(entity)
            loading_screen.done_sub_step()
        self.set_player(population["__player__"])
        loading_screen.next_sub_step("Building registry")
        self.update_registry()
        loading_screen.done_sub_step()
        loading_screen.next_sub_step("Setting up event listeners")
        self.set_event_listeners(event_manager)
        loading_screen.done_sub_step()
        loading_screen.done_step()

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
            arg["listener"].target.open_interaction(arg["keywords"]["direction"])

        def trigger_callback(arg):
            entity = arg["listener"].target
            trigger = arg["listener"].event.trigger
            next_state = entity.intellect.update(trigger)
            if next_state is not None:
                logging.debug("Entity %s switched to state %d",
                              entity, next_state)

        def dialog_close_callback(arg):
            arg["listener"].target.close_interaction()

        for entity in self.entities:
            event_manager.add_event_listener(
                entity, InteractionEvent(), interaction_callback)
            event_manager.add_event_listener(
                entity, DialogCloseEvent(), dialog_close_callback)
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

    def detect_collision(self, position):
        """Check if a registry entity occupies a given position."""
        for entity in self.registry:
            remoteness = (entity.attributes.position - position).norm()
            if remoteness < 1:
                return True
        return False

    def detect_interaction(self):
        """Check if the player has an entity to interact with in front of him."""
        attrs = self.player.attributes
        entities = self.get(front_position(attrs.position, attrs.direction))
        if len(entities) > 0:
            entity = list(entities).pop(0)
            self.event_manager.provoke(
                entity, InteractionEvent(), direction=attrs.direction)
