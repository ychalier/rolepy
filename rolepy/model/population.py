from rolepy.engine.core.structs import Position
from rolepy.engine.entities.enums import EntityTexture, MovementStyle
from rolepy.engine.entities import Entity, Behavior
from rolepy.engine.events.enums import Trigger


class Population(dict):
    """Create the instances of world entities."""

    def __init__(self, entity_manager):
        super(Population, self).__init__()
        player = Entity(entity_manager, 1)
        player.attributes.speed = 5
        self["__player__"] = player

        jane = Entity(entity_manager, 2)
        jane.attributes.position = Position(-5, 1)
        jane.attributes.texture = EntityTexture.WOMAN
        jane.intellect.states[0] = Behavior(
            text_line="Bonjour. Je m'appelle Jeanne. J'erre sans but dans cette morne vie.",
            proposed_answers=[
                {"text": "Raconter une blague", "trigger": Trigger.ANSWER_YES},
                {"text": "Ne rien faire", "trigger": Trigger.ANSWER_NO},
            ],
            movement_style=MovementStyle.RANDOM,
            anchor=Position(-5, 1),
        )
        jane.intellect.states[1] = Behavior(
            force_interaction=True,
            text_line="Ah Ah Ah Ah !",
            reset=True,
        )
        jane.intellect.states[2] = Behavior(
            text_line="Fichtre ! Que la vie est agréable !",
            movement_style=MovementStyle.RANDOM,
            anchor=Position(-5, 1),
        )
        jane.intellect.transitions[0] = {
            Trigger.ANSWER_YES: 1,
        }
        jane.intellect.transitions[1] = {
            Trigger.RESET: 2,
        }
        self["Jane"] = jane

        mary = Entity(entity_manager, 3)
        mary.attributes.position = Position(0, 2)
        mary.attributes.texture = EntityTexture.WOMAN
        mary.intellect.states[0] = Behavior(
            text_line="Bonjour. Je suis Marie. Puis-je vous accompagner ?",
            proposed_answers=[
                {"text": "Bien sûr !", "trigger": Trigger.ANSWER_YES},
                {"text": "Pas cette fois...", "trigger": Trigger.ANSWER_NO},
            ]
        )
        mary.intellect.states[1] = Behavior(
            movement_style=MovementStyle.FOLLOW,
            text_line="Hihi je vous suis !",
            proposed_answers=[
                {"text": "Arrêtez-vous !", "trigger": Trigger.ANSWER_HALT},
                {"text": "Vous devriez rentrer chez vous.", "trigger": Trigger.ANSWER_RETURN},
                {"text": "Non, rien...", "trigger": Trigger.ANSWER_CANCEL}
            ]
        )
        mary.intellect.states[2] = Behavior(
            force_interaction=True,
            text_line="Oh, excusez ma maladresse...",
            reset=True,
        )
        mary.intellect.states[3] = Behavior(
            movement_style=MovementStyle.RETURN,
            anchor=Position(0, 2),
        )
        mary.intellect.transitions[0] = {
            Trigger.ANSWER_YES: 1,
            Trigger.ANSWER_NO: 2
        }
        mary.intellect.transitions[1] = {
            Trigger.ANSWER_HALT: 0,
            Trigger.ANSWER_RETURN: 3
        }
        mary.intellect.transitions[2] = {
            Trigger.RESET: 0,
        }
        self["Mary"] = mary

        john = Entity(entity_manager, 4)
        john.attributes.position = Position(4, -2)
        john.intellect.states[0] = Behavior(
            text_line="Ils défendent les Droits de l'Homme, mais quand monsieur Sarkozy a été rencontrer le roi, là-bas, le roi d'Arabie Saoudite au Maroc, il lui a dit : \"Dites monsieur, les Droits de l'Homme ? Vous allez arrêter de le frapper à mort, ce type qui a écrit un blog qui ne vous plaisait pas ?\". Et quand monsieur Hollande a privatisé un bout de la plage pour la donner au roi d'Arabie Saoudite, pour la donner au roi d'Arabie Saoudite, il lui a dit: \"Dis donc, faudra pas y aller en burkini hein ?\". Non, bien sur que non."
        )
        self["John"] = john
