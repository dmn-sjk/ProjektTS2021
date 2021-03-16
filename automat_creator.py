from statemachine import StateMachine, State, Transition


class AutomatCreator(StateMachine):

    def __init__(self, my_states, my_transitions, scheme):

        self.states = []
        self.transitions = []
        self.states_map = {}

        for state in my_states:
            setattr(self, state.value, state)
            self.states.append(state)
            self.states_map[state.value] = state

        for ind, tran in enumerate(scheme):
            transition = Transition(self.states[tran[0]], self.states[tran[1]],
                                    identifier=my_transitions[ind]['identifier'])
            setattr(self, transition.identifier, transition)
            self.transitions.append(transition)
            self.states[tran[0]].transitions.append(transition)

        super(AutomatCreator, self).__init__()
