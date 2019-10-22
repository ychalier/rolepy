from rolepy.misc import Position


def hash_entity_position(position):
    return position.target()


class EntityManager:

    def __init__(self, width, height):
        super(EntityManager, self).__init__()
        self.registry = set()
        self.entities = dict()
        self.map = dict()
        self.width = width
        self.height = height
        self.center = None

    def ai_step(self):
        for entity in self.registry.copy():
            if entity.thinking:
                entity.ai_step()

    def add(self, entity):
        hashed_position = hash_entity_position(entity.position)
        self.entities[entity] = hashed_position
        self.map.setdefault(hashed_position, set())
        self.map[hashed_position].add(entity)

    def get(self, position, i=None):
        key = position
        if i is not None:
            key = Position(position, i)
        return self.map.get(key, set())

    def update_entity_position(self, entity):
        old_position = self.entities[entity]
        self.map[old_position].discard(entity)
        if len(self.map[old_position]) == 0:
            del self.map[old_position]
        self.add(entity)
        if self.center is not None:
            if self.center.x - self.width // 2 <= entity.position.x < self.center.x + self.width // 2 + 1 and self.center.y - self.height // 2 <= entity.position.y < self.center.y + self.height // 2 + 1:
                self.registry.add(entity)
            else:
                self.registry.discard(entity)

    def update_registry(self, center):
        self.center = center
        self.registry.clear()
        for i in range(center.y - self.height // 2, center.y + self.height // 2 + 1):
            for j in range(center.x - self.width // 2, center.x + self.width // 2 + 1):
                self.registry |= self.get(j, i)

    def blit(self, surface, transformer):
        for entity in sorted(self.registry, key=lambda e: e.position.y):
            entity.blit(surface, transformer)
