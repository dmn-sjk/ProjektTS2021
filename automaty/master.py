from statemachine import State, Transition

states = [{'name': 'Stanowisko puste', "value": 'stan_pust', 'initial': True},
          {'name': 'Element pochwycony', 'value': 'el_poch', 'initial': False},
          {'name': 'Spawanie zakończone', 'value': 'spaw_end', 'initial': False},
          {'name': 'Proces sprawdzania spawu', 'value': 'spaw_spr', 'initial': False},
          {'name': 'Element odłożony', 'value': 'el_od', 'initial': False}]

transitions = [{'name': 'Pochwycenie elementu', 'identifier': 'poch_el'},
               {'name': 'Spawanie', 'identifier': 'spaw'},
               {'name': 'Przejście do sprawdzenia', 'identifier': 'prz_spr'},
               {'name': 'Usunięcie elementu', 'identifier': 'us_el'},
               {'name': 'Powrót do procesu głównego', 'identifier': 'pow_gl'},
               {'name': 'Odkładanie elementu', 'identifier': 'od_el'},
               {'name': 'Powrót do pozycji', 'identifier': 'pow'}]

scheme = [[0, 1],
          [1, 2],
          [2, 3],
          [3, 0],
          [3, 2],
          [2, 4],
          [4, 0]]

master_states = [State(**state) for state in states]

master = {'states': master_states, 'transitions': transitions, 'scheme': scheme}