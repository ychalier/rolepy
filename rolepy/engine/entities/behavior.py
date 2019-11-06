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
        if self.movement_style == MovementStyle.RANDOM:
            now = time.time()
            if now > entity.attributes.next_movement:
                remoteness = entity.attributes.position - self.anchor
                if remoteness.norm() > self.max_distance_to_anchor:
                    direction = reverse_direction(angle_direction(remoteness.angle()))
                else:
                    direction = random.choice(list(Ordinal))
                distance = random.randint(1, 5)
                entity.move(direction, distance).start()
            if now > entity.attributes.next_movement or entity.attributes.next_movement < 0:
                entity.attributes.set("last_movement", now)
                entity.attributes.set("next_movement", random.random() \
                    * (self.max_time_between_movements - self.min_time_between_movements) \
                    + self.min_time_between_movements + entity.attributes.last_movement
                )
        elif self.movement_style == MovementStyle.FOLLOW:
            remoteness = entity.manager.player.attributes.position - entity.attributes.position
            if remoteness.norm(1) > 1:
                entity.move(angle_direction(remoteness.angle()), 1).start()

    def interact(self, entity):
        print(self.text_line)
        if len(self.proposed_answers) > 0:
            for i, proposed_answer in enumerate(self.proposed_answers):
                print("\t%d. %s" % (i, proposed_answer["text"]))
            choice = None
            try:
                choice = int(input("\t> "))
            except:
                pass
            if choice in range(len(self.proposed_answers)):
                selection = self.proposed_answers[choice]
                entity.manager.event_manager.provoke(
                    entity,
                    TriggerEvent(selection["trigger"]),
                )
        if self.reset:
            entity.manager.event_manager.provoke(
                entity,
                TriggerEvent(Trigger.RESET),
            )
