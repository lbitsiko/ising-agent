import numpy as np
from mesa import Model
from mesa.space import SingleGrid
from mesa.time import RandomActivation
from agents import Spin

class IsingModel(Model):
    """
    Model class for the 2-D Ising model.
    Sets up Spin agents advances each time step.
    """
    
    def __init__(self, height, width, beta, seed=69, hot_configuration=True):
        """ 
        Initializes grid with Spin agents occupying each position
        """
        # grid dimensions
        self.height = height
        self.width = width
        
        self.num_agents = width * height  # there are agents in every position of the grid

        self.grid = SingleGrid(width, height, torus = True)  # torroidal boundary conditions
        
        self.schedule = RandomActivation(self) 

        self.beta = beta
        self.probs = [np.exp(-2.0 * self.beta * i) for i in range(2, 9, 2)]

        self.seed = seed
        np.random.seed(self.seed)

        # cold initial configuration: 1, cold
        self.hot_configuration = hot_configuration

        # initialize grid and spins
        if self.hot_configuration:  # cold - random distribution of s(i)
            for _, x, y in self.grid.coord_iter():
                state = np.random.choice([1, -1])
                agent = Spin(pos=(x, y), model=self, state=state)
                self.grid.place_agent(agent, pos=(x, y))
                self.schedule.add(agent)
        else: # cold configuration - all s(i) = 1
            for _, x, y in self.grid.coord_iter():
                state = 1
                agent = Spin(pos=(x, y), model=self, state=state)
                self.grid.place_agent(agent, pos=(x, y))
                self.schedule.add(agent)
    
    def step(self):
        """
        Run one step of the model. 
        """
        self.schedule.step()

    def calculate_energy(self):
        """
        Calculate the Ising model energy
        """
        energy = 0
        for cell_content, x, y in self.grid.coord_iter():
            current_spin = cell_content.state
            neighbors = self.grid.get_neighbors((x, y), moore=False)  # von Neumann neighbors
            for neighbor in neighbors:
                energy -= current_spin * neighbor.state
        return energy  

    def calculate_magnetization(self):
        """
        Calculate the total magnetization.
        """
        return sum(agent.state for agent in self.schedule.agents)