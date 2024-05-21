import numpy as np
from mesa import Model
from mesa.space import SingleGrid
from mesa.time import RandomActivation, BaseScheduler, SimultaneousActivation
from mesa.datacollection import DataCollector
from agents import Spin
import pickle


def get_color_based_on_position(L, x, y):
    """
        Color scheme based on https://courses.physics.illinois.edu/phys498cmp/sp2022/Ising/IsingModel.html
    """
    if np.logical_and((x + y) % 2 == 0, np.logical_and(x < L - 1, y < L - 1)):
        return 'red'
    elif np.logical_and((x + y) % 2 == 1, np.logical_and(x < L - 1, y < L - 1)):
        return 'blue'
    elif np.logical_and((x + y) % 2 == 0, np.logical_or(x == L - 1, y == L - 1)):
        return 'green'
        if x == L - 1 and y == L - 1:
            return 'red'  # special case, last cell
    else:
        return 'yellow'

class CustomColorActivation(BaseScheduler):
    """
        Custom color activation 
        order: red, blue, green, yellow agents
    """
    def __init__(self, model):
        super().__init__(model)
        
    def step(self):
        # sort agents into color-based queues
        model_agents = self.agents

        red_agents = [agent for agent in model_agents if agent.color == 'red']
        blue_agents = [agent for agent in model_agents if agent.color == 'blue']
        green_agents = [agent for agent in model_agents if agent.color == 'green']
        yellow_agents = [agent for agent in model_agents if agent.color == 'yellow']
        
        # activate agents in color order
        for agent_list in [red_agents, blue_agents, green_agents, yellow_agents]:
            for agent in agent_list:
                agent.step()
        
        self.steps += 1
        self.time += 1


class IsingModel(Model):
    """
    Model class for the 2-D Ising model.
    Sets up Spin agents advances each time step.
    """
    
    def __init__(self, L, beta, seed=None, hot_configuration=True, activation="random", algo="heat_bath", magnetic_field=0):
        """ 
        Initializes grid with Spin agents occupying each position
        """

        super().__init__()

        # grid dimensions
        self.L = L
        
        self.num_agents = self.L ** 2  # there are agents in every position of the grid

        self.grid = SingleGrid(L, L, torus = True)  # torroidal boundary conditions
        
        self.algo = algo

        self.magnetic_field = magnetic_field  # external field
        self.activation = activation 

        if self.activation == "random":
            self.schedule = RandomActivation(self)
        elif self.activation == "color":
            self.schedule = CustomColorActivation(self) 
        elif self.activation == "simultaneous":
            self.schedule = SimultaneousActivation(self)
        
        self.beta = beta
        self.probs = [np.exp(-2.0 * self.beta * i) for i in range(2, 9, 2)]

        # set random seed if needed
        if seed:
            self.seed = seed
            np.random.seed(self.seed)

        # cold initial configuration: 1, cold
        self.hot_configuration = hot_configuration

        # initialize grid and spins
        for _, (x, y) in self.grid.coord_iter():
            
            color = None
            if activation == "color":
                color = get_color_based_on_position(self.L, x=x, y=y)
                    
            if self.hot_configuration:  # hot - random distribution of s(i)
                state = np.random.choice([1, -1])
            else: # cold configuration - all s(i) = 1
                state = 1

            agent = Spin(pos=(x, y), model=self, state=state, color=color, algo=algo)
            self.grid.place_agent(agent, pos=(x, y))
            self.schedule.add(agent)

        # DataCollector
        self.datacollector = DataCollector(
            model_reporters={"energy": self.calculate_energy,
                             "magnetization": self.calculate_magnetization,
                            #  "field": (lambda x: self.magnetic_field),
                            #  "beta": (lambda x: self.beta),
                            #  "algo": (lambda x: self.algo),
                            #  "seed": (lambda x: self.seed),
                            #  "hot_configuration": (lambda x: self.hot_configuration),
                            #  "grid_size": (lambda x: self.L)
                             }
                             )    
    
    def step(self):
        """
        Run one step of the model. 
        """
        self.schedule.step()
        self.datacollector.collect(self)

    def run_model(self, steps):
        for i in range(steps):
            self.step()

    def calculate_energy(self):
        """
        Calculate the Ising model energy
        """
        energy = 0
        for cell_content, (x, y) in self.grid.coord_iter():
            current_spin = cell_content.state
            neighbors = self.grid.get_neighbors((x, y), moore=False)  # von Neumann neighbors
            for neighbor in neighbors:
                energy -= current_spin * neighbor.state
            energy -= self.magnetic_field * current_spin  # magnetic field contribution
        return energy / (self.L * self.L)

    def calculate_magnetization(self):
        """
        Calculate the total magnetization.
        """
        return sum(agent.state for agent in self.schedule.agents)
    
    def save_grid(self):
        """
            Save grid configuration
        """
        with open(f"configurations/L{self.L}_b{self.beta}.pickle", 'wb') as f:
            pickle.dump(self.grid, f)
        