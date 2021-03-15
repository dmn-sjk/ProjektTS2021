from statemachine import State

# define states for a master (way of passing args to class)
options = [
    {"name": "Stanowisko puste", "initial": True, "value": "idle"},  # 0
    {"name": "Element pochwycony", "initial": False, "value": "el. chwycony"},  # 1
    {"name": "Spawanie zakonczone", "initial": False, "value": "spawanie koniec"},  # 2
    {"name": "Proces sprawdzania spawu", "initial": False, "value": "sprawdzanie"},  # 3
    {"name": "Element odlozony", "initial": False, "value": "odlozony"}]  # 4

options_sprawdzanie=[
    {"name": "IDLE", "Sprawdzanie": True, "value": "idle"},  # 0
    {"name": "Powrot do spawania", "initial": False, "value": "powrot"},  # 1
    {"name": "Interwencja pracownika", "initial": False, "value": "interwencja"},  # 2
    {"name": "Element usuniety", "initial": False, "value": "usuniety"}]  # 3


# create State objects for a master
# ** -> unpack dict to args
master_states = [State(**opt) for opt in options]
sprawdzanie_states = [State(**opt) for opt in options]