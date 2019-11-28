import math
import time
from rolepy.engine.core.tasks import AsyncTask
from rolepy.engine.core.structs import Position
from rolepy.engine.core.misc import front_position
from rolepy.engine.entities.enums import Posture
from rolepy.engine.entities.enums import EntityState


class Movement(AsyncTask):
    """Thread dedicated to the movement of an entity."""

    def __init__(self, entity, direction, distance, update=False):
        entity.attributes.set("state", EntityState.MOVING)
        duration = float(distance) / entity.attributes.speed
        source = Position(*entity.attributes.position.pair())
        destination = front_position(source, direction, distance)

        def posture_cycle():
            while True:
                yield Posture.LEFT
                yield Posture.REST
                yield Posture.RIGHT
                yield Posture.REST
        postures = posture_cycle()

        def function():
            entity.attributes.set("direction", direction)
            start = time.time()
            early_stop = 1
            progress = 0
            last = 0
            while progress < early_stop:
                collision = entity.manager.detect_collision(front_position(
                    entity.attributes.position,
                    entity.attributes.direction
                ))
                if entity.attributes.interrupt_movement or collision:
                    early_stop = float(math.ceil(progress * distance)) / distance
                    entity.attributes.set("interrupt_movement", False)
                current = time.time()
                progress = min(1, (current - start) / duration)
                entity.attributes.set(
                    "position",
                    (1 - progress) * source + progress * destination
                )
                if current - last > duration / 4 / distance:
                    entity.attributes.set("posture", next(postures))
                    last = current
                time.sleep(duration / 100)
            entity.attributes.set("state", EntityState.IDLE)
            entity.attributes.set("posture", Posture.REST)
            entity.attributes.set("position", entity.attributes.position.target())
            entity.manager.update_entity_position(entity)
            if update:
                entity.manager.update_registry()
        AsyncTask.__init__(self, function)
