import time
from rolepy.tasks import AsyncTask
from rolepy.globals import WalkAnimation, walk_animation_cycle
from rolepy.globals import Ordinal
from rolepy.misc import Position


class EntityMovement(AsyncTask):
    """Thread dedicated to the movement of an entity."""

    def __init__(self, entity, direction, distance, update=False):
        entity.thinking = False
        duration = float(distance) / entity.speed
        source = Position(*entity.position.pair())
        iterator = walk_animation_cycle()
        if direction == Ordinal.NORTH:
            destination = source + Position(0, -distance)
        elif direction == Ordinal.SOUTH:
            destination = source + Position(0, distance)
        elif direction == Ordinal.WEST:
            destination = source + Position(-distance, 0)
        elif direction == Ordinal.EAST:
            destination = source + Position(distance, 0)

        def function():
            entity.direction = direction
            start = time.time()
            progress = 0
            last = 0
            while progress < 1:
                current = time.time()
                progress = min(1, (current - start) / duration)
                entity.position = (1 - progress) * source + \
                    progress * destination
                if current - last > duration / 4 / distance:
                    entity.walk_animation = next(iterator)
                    last = current
                time.sleep(duration / 100)
            entity.walk_animation = WalkAnimation.REST
            entity.position.round()
            entity.manager.update_entity_position(entity)
            if update:
                entity.manager.update_registry()
        AsyncTask.__init__(self, function)
