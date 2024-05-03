import numpy as np
from mesa import Model
from mesa.space import SingleGrid
from mesa.time import RandomActivation, BaseScheduler, SimultaneousActivation
from mesa.datacollection import DataCollector
from agents import Voter
import pickle


import random

class VotingModel(Model):
    """ A simple voting model """
    def __init__(self, L, seed=69, activation="random", prob=0.5, algo="majority"):
        super().__init__()

        self.L = L
        self.num_agents = self.L**2    

        self.grid = SingleGrid(L, L, torus=True)
        self.magnetic_field = 0

        self.activation = activation
        self.prob = prob
        self.algo = algo 

        if self.activation == "random":
            self.schedule = RandomActivation(self)
        elif self.activation == "simultaneous":
            self.schedule = SimultaneousActivation(self)
        
        self.seed = seed
        np.random.seed(self.seed)

        # initialize grid and spins
        for _, (x, y) in self.grid.coord_iter():
            
            state = np.random.choice([1, -1])  # choose initial state at random

            agent = Voter(pos=(x, y), state=state, model=self)
            self.grid.place_agent(agent, pos=(x, y))
            self.schedule.add(agent)

        # DataCollector
        self.datacollector = DataCollector(
            model_reporters={"energy": self.calculate_energy,
                             "magnetization": self.calculate_magnetization
                             }
                             )    
    

    def step(self):
        self.schedule.step()
        self.datacollector.collect(self)
    
    def run_model(self, steps):
        for i in range(steps):
            self.step()

    def calculate_energy(self):
        """
        Calculate the model energy based on the Ising model calculation
        """
        energy = 0
        for cell_content, (x, y) in self.grid.coord_iter():
            current_spin = cell_content.state
            neighbors = self.grid.get_neighbors((x, y), moore=False)  # von Neumann neighbors
            for neighbor in neighbors:
                energy -= current_spin * neighbor.state
            energy -= self.magnetic_field * current_spin  # magnetic field contribution
        return energy

    def calculate_magnetization(self):
        """
        Calculate the total magnetization based on the Ising model calculation.
        """
        return sum(agent.state for agent in self.schedule.agents)