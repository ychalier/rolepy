import random
import time
from rolepy.engine.core.enums import Ordinal
from rolepy.engine.core.misc import angle_direction
from rolepy.engine.core.misc import reverse_direction
from rolepy.engine.core.structs import Position
from rolepy.engine.entities.enums import MovementStyle
from rolepy.engine.events.implemented import TriggerEvent
from rolepy.engine.events.enums import Trigger


class Behavior:
    """Represent and handle how an entity behaves while interacting or taking
       autonomous decisions, such as movement.
    """

    def __init__(self, **kwargs):
        self.text_line = ""
        self.proposed_answers = list()
        self.force_interaction = False
        self.movement_style = MovementStyle.STATIC
        self.max_time_between_movements = 10.
        self.min_time_between_movements = 1.
        self.max_distance_to_anchor = 5
        self.anchor = Position(0, 0)
        self.reset = False
        for arg_name, arg_value in kwargs.items():
            setattr(self, arg_name, arg_value)

    def take_action(self, entity):
        """Elementary step of autonomous decision making from the entity."""
        if self.movement_style == MovementStyle.RANDOM:
            now = time.time()
            if entity.attributes.next_movement > 0 and now > entity.attributes.next_movement:
                remoteness = entity.attributes.position - self.anchor
                if remoteness.norm() > self.max_distance_to_anchor:
                    direction = reverse_direction(
                        angle_direction(remoteness.angle()))
                else:
                    direction = random.choice(list(Ordinal))
                distance = random.randint(1, 5)
                entity.move(direction, distance).start()
            if now > entity.attributes.next_movement or entity.attributes.next_movement < 0:
                upcoming = random.random() \
                    * (self.max_time_between_movements - self.min_time_between_movements) \
                    + self.min_time_between_movements + entity.attributes.last_movement
                entity.attributes.set("last_movement", now)
                entity.attributes.set("next_movement", upcoming)
        elif self.movement_style == MovementStyle.FOLLOW:
            remoteness = entity.manager.player.attributes.position - entity.attributes.position
            if remoteness.norm(1) > 1:
                entity.move(angle_direction(remoteness.angle()), 1).start()
        elif self.movement_style == MovementStyle.RETURN:
            remoteness = self.anchor - entity.attributes.position
            if remoteness.norm(1) > 1:
                entity.move(angle_direction(remoteness.angle()), 1).start()

    def open_interaction(self, entity):
        """Callback after an interaction event has been fired."""
        entity.manager.game.interface_manager.dialog_manager.open_dialog(
            entity,
            entity.attributes.position,
            self.text_line,
            self.proposed_answers
        )

    def close_interaction(self, entity):
        """Reset the behavior after the end of the interaction."""
        entity.attributes.set("next_movement", -1)
        entity.attributes.set("last_movement", time.time())
        if self.reset:
            entity.manager.event_manager.provoke(
                entity,
                TriggerEvent(Trigger.RESET),
            )
