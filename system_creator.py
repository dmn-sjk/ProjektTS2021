from automat_creator import AutomatCreator


# TODO można całość upiększyć
class MachineCreator(AutomatCreator):
    """
    Korzystać z run(), curr_state, allowed_trans, nie z current_state i allowed_transitions
    """

    def __init__(self, master, slave):
        self.master = AutomatCreator(master['states'], master['transitions'], master['scheme'])
        self.slave = AutomatCreator(slave['states'], slave['transitions'], slave['scheme'])

        # stany w których następuje przechodzenie do slave'a lub mastera
        self.state_master_to_slave = self.master.states[3]
        self.states_slave_to_master = [self.slave.states[1], self.slave.states[3]]

        self.curr_state = self.master.states[0]
        self.allowed_trans = self.master.allowed_transitions
        self.weld_checked = False
        self.to_run = self.master

    def what_to_run(self):
        """
        Sprawdzenie który automat jest aktywny i powinien być aktualnym
        """

        if self.to_run.current_state == self.state_master_to_slave:
            if self.to_run == self.master:
                print('Przejście do slave\'a')
            return self.slave
        elif self.to_run.current_state in self.states_slave_to_master:
            if self.to_run == self.slave:
                print('Przejście do mastera')
                self.weld_checked = True
            return self.master
        else:
            return self.to_run

    def reset_slave(self):
        """
        Powrót slava'e do początkowego stanu
        """
        self.slave.current_state = self.slave.states[0]

    def correct_allowed_trans(self):
        """
        Usunięcie z możliwych przejść, przejść które nie powinny być dostępne:
         - przejście po powrocie do mastera w zależności od stanu wyjściowego slave'a
         - przejście do ponownego sprawdzenia spawu po wykonaniu sprawdzenia spawu
         - przejście do odłożenie elementu bez sprawdzenia
        """
        if self.to_run == self.master:
            if self.slave.current_state == self.states_slave_to_master[0]:
                self.allowed_trans.remove(self.master.transitions[3])
                self.reset_slave()
            elif self.slave.current_state == self.states_slave_to_master[1]:
                self.allowed_trans.remove(self.master.transitions[4])
                self.reset_slave()
            elif self.curr_state == self.master.states[2]:
                if self.weld_checked:
                    self.allowed_trans.remove(self.master.transitions[2])
                elif not self.weld_checked:
                    self.allowed_trans.remove(self.master.transitions[5])

    @staticmethod
    def identifier_to_index(to_run, transition):
        """
        Uzyskanie indeksu przejścia w liście przejść na podstawie jego identyfikatora
        """
        for ind, tran in enumerate(to_run.transitions):
            if tran.identifier == transition:
                return ind

    def run(self, transition):
        """
        Wykonanie przejścia
        """
        tran_index = self.identifier_to_index(self.to_run, transition)

        self.to_run.transitions[tran_index]._run(self.to_run)

        self.to_run = self.what_to_run()

        self.curr_state = self.to_run.current_state
        self.allowed_trans = self.to_run.allowed_transitions

        # Spaw nie jest sprawdzony po podniesieniu nowego elementu
        if self.curr_state == self.master.states[0]:
            self.weld_checked = False

        self.correct_allowed_trans()

        return self.curr_state, self.allowed_trans






