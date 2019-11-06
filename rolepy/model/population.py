from rolepy.engine.core.structs import Position
from rolepy.engine.entities.enums import EntityTexture, MovementStyle
from rolepy.engine.entities import Entity, Behavior
from rolepy.engine.events.enums import Trigger


class Population(dict):

    def __init__(self, entity_manager):
        super(Population, self).__init__()
        player = Entity(entity_manager, 1)
        player.attributes.speed = 5
        self["__player__"] = player

        jane = Entity(entity_manager, 2)
        jane.attributes.position = Position(-5, 1)
        jane.attributes.texture = EntityTexture.WOMAN
        jane.intellect.states[0] = Behavior(
            text_line="Hello, my name is Jane.",
            movement_style=MovementStyle.RANDOM,
            anchor=Position(-5, 1),
        )
        self["Jane"] = jane

        mary = Entity(entity_manager, 3)
        mary.attributes.position = Position(0, 2)
        mary.attributes.texture = EntityTexture.WOMAN
        mary.intellect.states[0] = Behavior(
            text_line="Hello, I'm Mary. Can I follow you?",
            proposed_answers=[
                {"text": "Sure!", "trigger": Trigger.ANSWER_YES},
                {"text": "Not this time...", "trigger": Trigger.ANSWER_NO},
            ]
        )
        mary.intellect.states[1] = Behavior(
            movement_style=MovementStyle.FOLLOW,
        )
        mary.intellect.states[2] = Behavior(
            force_interaction=True,
            text_line="Oh, I am so sad...",
            reset=True,
        )
        mary.intellect.transitions[0] = {
            Trigger.ANSWER_YES: 1,
            Trigger.ANSWER_NO: 2
        }
        mary.intellect.transitions[2] = {
            Trigger.RESET: 0,
        }
        self["Mary"] = mary

        john = Entity(entity_manager, 4)
        john.attributes.position = Position(4, -2)
        john.intellect.states[0] = Behavior(
            text_line="I'm John and I am here for good.",
        )
        self["John"] = john
