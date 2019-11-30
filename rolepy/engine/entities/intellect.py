from rolepy.engine.entities import Behavior
from rolepy.engine.events.enums import Trigger


class Intellect:
    """Automaton representation of an entity brain"""

    def __init__(self, entity, states, transitions, initial):
        self.entity = entity
        self.states = states
        self.transitions = transitions
        self.current_state = initial

    def get(self):
        """Return the current behavior."""
        return self.states[self.current_state]

    def update(self, trigger):
        """Perform the triggered transition if relevant."""
        next_state = self.transitions \
            .get(self.current_state, dict()) \
            .get(trigger, None)
        if next_state is not None:
            self.current_state = next_state
            if self.get().force_interaction:
                self.entity.open_interaction()
            return next_state
        return None

    def to_dict(self):
        state_list = list()
        for key, state in self.states.items():
            d = state.to_dict()
            d["key"] = key
            state_list.append(d)
        transition_list = list()
        for start in self.transitions:
            for trigger in self.transitions[start]:
                transition_list.append({
                    "start": start,
                    "end": self.transitions[start][trigger],
                    "trigger": trigger.value
                })
        return {
            "current_state": self.current_state,
            "states": state_list,
            "transitions": transition_list
        }

    def from_dict(self, d):
        self.current_state = d["current_state"]
        for state in d["states"]:
            self.states[state["key"]] = Behavior()
            self.states[state["key"]].from_dict(state)
        for transition in d["transitions"]:
            self.transitions.setdefault(transition["start"], dict())
            self.transitions[transition["start"]][Trigger(transition["trigger"])] = transition["end"]
