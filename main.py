from automaty.master import master
from automaty.slave import slave
from system_creator import MachineCreator
from random import randint

if __name__ == '__main__':
    machine = MachineCreator(master, slave)
    print(f'Aktualny stan: {machine.curr_state}')
    print(f'Możliwe przejscia: {machine.allowed_trans}\n')
    while True:
        input('Naciśnij Enter, aby kontynuować\n------------------------------')
        action = machine.allowed_trans[randint(0, len(machine.allowed_trans) - 1)]
        print(f'\nWykonanie przejścia: {action}\n')
        state, transitions = machine.run(action.identifier)

        print(f'Aktualny stan: {state}')
        print(f'Możliwe przejscia: {transitions}\n')


