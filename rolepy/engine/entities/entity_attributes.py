from rolepy.engine.core.structs import Position
from rolepy.engine.core.enums import Ordinal
from rolepy.engine.entities.enums import Posture
from rolepy.engine.entities.enums import EntityState
from rolepy.engine.entities.enums import EntityTexture
from rolepy.engine.events.implemented import AttributeChangeEvent


class EntityAttributes:
    """Represent all the attributes characterising the entity."""

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
        """Change the value of an attribute and fire an appropriate event."""
        if attribute not in self.__dict__:
            raise NameError("Incorrect attribute '%s'" % attribute)
        setattr(self, attribute, value)
        self.entity.manager.event_manager.provoke(
            self.entity,
            AttributeChangeEvent(attribute),
            value=value
        )

    def to_dict(self):
        return {
            "texture": self.texture.value,
            "position": self.position.to_dict(),
            "speed": self.speed,
            "direction": self.direction.value,
            "posture": self.posture.value,
            "state": self.state.value,
            "last_movement": self.last_movement,
            "next_movement": self.next_movement
        }
