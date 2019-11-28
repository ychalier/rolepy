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
