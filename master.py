from statemachine import StateMachine, State, Transition
from states import master_states
from classGenerator import Generator
from paths import paths_master

# valid transitions for a master (indices of states from-to)
form_to = [
    [0, [1]],
    [1, [2]],
    [2, [3, 4]],
    [3, [0, 2]],
    [4, [0]],
]

# create transitions for a master (as a dict)
master_transitions = {}
for indices in form_to:
    from_idx, to_idx_tuple = indices  # unpack list of two elements into separate from_idx and to_idx_tuple
    for to_idx in to_idx_tuple:  # iterate over destinations from a source state
        op_identifier = "m_{}_{}".format(from_idx, to_idx)  # parametrize identifier of a transition

        # create transition object and add it to the master_transitions dict
        transition = Transition(master_states[from_idx], master_states[to_idx], identifier=op_identifier)
        master_transitions[op_identifier] = transition

        # add transition to source state
        master_states[from_idx].transitions.append(transition)

# execute paths
for path in paths:

    # create a supervisor
    supervisor = Generator.create_master(master_states, master_transitions)
    print('\n' + str(supervisor))

    # run supervisor for exemplary path
    print("Executing path: {}".format(path))
    for event in path:

        # launch a transition in our supervisor
        master_transitions[event]._run(supervisor)
        print(supervisor.current_state)

        # add slave
        if supervisor.current_state.value == "a":
            # TODO: automata 1 (for) slave1
            ...

        if supervisor.current_state.value == "b":
            # TODO: automata 2 (for) slave2
            ...

        if supervisor.current_state.value == "c":
            # TODO: automata 3 (for) slave3
            ...

        if supervisor.current_state.value == "f":
            # TODO: automata 3 (for) slave3
            ...
            print("Supervisor done!")
