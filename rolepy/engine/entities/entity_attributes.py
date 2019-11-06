from rolepy.engine.core.structs import Position
from rolepy.engine.core.enums import Ordinal
from rolepy.engine.entities.enums import Posture
from rolepy.engine.entities.enums import EntityState
from rolepy.engine.entities.enums import EntityTexture
from rolepy.engine.events.implemented import AttributeChangeEvent


class EntityAttributes:

    def __init__(self, entity):
        self.entity = entity
        self.texture = EntityTexture.MAN
        self.position = Position(0, 0)
        self.speed = 3
        self.direction = Ordinal.SOUTH
        self.posture = Posture.REST
        self.state = EntityState.IDLE
        self.last_movement = 0
        self.next_movement = 0
        self.interrupt_movement = False

    def set(self, attribute, value):
        setattr(self, attribute, value)
        self.entity.manager.event_manager.provoke(
            self.entity,
            AttributeChangeEvent(attribute),
            value=value
        )
