from rolepy.misc import Position


def hash_entity_position(position):
    """Return the indexing hash of a given position."""
    return position.target()


class EntityManager:
    """Store and handle all entities."""

    def __init__(self, width, height):
        super(EntityManager, self).__init__()
        self.registry = set()
        self.entities = dict()
        self.map = dict()
        self.width = width
        self.height = height
        self.center = None

    def add(self, entity):
        """Add an entity to the RAM."""
        hashed_position = hash_entity_position(entity.position)
        self.entities[entity] = hashed_position
        self.map.setdefault(hashed_position, set())
        self.map[hashed_position].add(entity)

    def get(self, position, i=None):
        """Return the set of entities at a given position."""
        key = position
        if i is not None:
            key = Position(position, i)
        return self.map.get(key, set())

    def ai_iterate(self):
        """Trigger each entity AI."""
        for entity in self.registry.copy():
            if entity.thinking:
                entity.think()

    def update_entity_position(self, entity):
        """Update the membership of one entity to the registry."""
        old_position = self.entities[entity]
        self.map[old_position].discard(entity)
        if len(self.map[old_position]) == 0:
            del self.map[old_position]
        self.add(entity)
        if self.center is not None:
            if (self.center.x - self.width // 2
                    <= entity.position.x
                    < self.center.x + self.width // 2 + 1) \
                and (self.center.y - self.height // 2
                     <= entity.position.y
                     < self.center.y + self.height // 2 + 1):
                self.registry.add(entity)
            else:
                self.registry.discard(entity)

    def update_registry(self):
        """Exhaustive build of entity registry."""
        self.registry.clear()
        for i in range(self.center.y - self.height // 2, self.center.y + self.height // 2 + 1):
            for j in range(self.center.x - self.width // 2, self.center.x + self.width // 2 + 1):
                self.registry |= self.get(j, i)

    def blit(self, surface, transformer):
        """Blit entities within the registry to the screen."""
        for entity in sorted(self.registry, key=lambda e: e.position.y):
            entity.blit(surface, transformer)
