from statemachine import State

states = [{'name': 'Proces sprawdzania spawu', 'value': 'spr_spaw', 'initial': True},
          {'name': 'Powrót do spawania', 'value': 'pow_spaw', 'initial': False},
          {'name': 'Interwencja pracownika', 'value': 'int_prac', 'initial': False},
          {'name': 'Element usunięty', 'value': 'el_us', 'initial': False}]

transitions = [{'name': 'Spaw prawidłowy', 'identifier': 'spaw_ok'},
               {'name': 'Spaw nieprawidłowy', 'identifier': 'spaw_nk'},
               {'name': 'Zatwierdzenie spawu', 'identifier': 'zat_spaw'},
               {'name': 'Usunięcie elementu', 'identifier': 'us_el'}]

scheme = [[0, 1],
          [0, 2],
          [2, 1],
          [2, 3]]

slave_states = [State(**state) for state in states]

slave = {'states': slave_states, 'transitions': transitions, 'scheme': scheme}
