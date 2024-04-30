from mesa import Agent
import random
import numpy as np

# TODO: implement randomly getting the opinion of a neighbor

class Voter(Agent):
    """ A voting agent that aligns its opinion with the majority opinion of its neighbors. """
    def __init__(self, pos, model, state):
        super().__init__(pos, model)
        self.pos = pos
        self.state = state 
        self.prob = self.model.prob

    def step(self):
        # majority opinion of neighbors
        neighbor_opinions = [neighbor.state
                              for neighbor 
                              in self.model.grid.iter_neighbors(pos=self.pos, 
                                                                moore=False
                                                                )
                            ]
        if neighbor_opinions:
            majority_opinion = 1 if sum(neighbor_opinions) > 0 else -1
            if np.random.random() > self.prob:
                self.state = majority_opinion
            else:  # if np.random.random() > self.prob:
                self.state = - self.state

