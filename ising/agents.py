from mesa import Agent
import numpy as np

class Spin(Agent):
    """
    Spin in the Ising model
    """

    def __init__(self, pos, model, state):
        """
        Create a new spin agent.

        Args:
            pos: where the agent is
            model: the Ising 2-D model lattice
            state: Indicator for the agent's type (spin_up=1, spin_down=-1)
        """
        super().__init__(pos, model) # allows base class to work with pos + model
        self.pos = pos
        self.state = state
        
    def sum_neighboring_spins(self):
        """ 
            Sum of neighboring spins
        """
        return np.sum(
            [
                neighbor.state 
                for neighbor in self.model.grid.iter_neighbors(
                                                                pos=self.pos, 
                                                                moore=False
                                                              )
            ]
                    )

    def calculate_delta_Energy(self):
        """
            Calculation of energy change
        """
        sum_of_neighboring_spins = self.sum_neighboring_spins()
        return sum_of_neighboring_spins * self.state



    def step(self):
        """
            Implementation following the Metropolis algorithm 
            based on the (Anagnostopoulos, 2016) implementation, see: https://dx.doi.org/10.57713/kallipos-946  
        """
        # Update position, Metropolis algorithm
        dE = self.calculate_delta_Energy()
        if dE <= 0.0: # Spin flips if energy remains the same or is lower
            self.state = -self.state
        elif np.random.random() < self.model.probs[int(abs(dE)/2)]:  # Spin flips based on the Metropolis criterion
            self.state = -self.state
        


