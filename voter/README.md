# Voter Model

## Summary

This Voter model is an implementation of the voting agents described in [*Phase transition and power-law coarsening in an Ising-doped voter model*](https://journals.aps.org/pre/abstract/10.1103/PhysRevE.96.032145) by Adam Lipowski, Dorota Lipowska, and António Luis Ferreira.

In its 2-D version presented here, the model is composed of agents placed on a square lattice, having either a positive or negative opinion. In each simulation step, agents decide to change their opinion looking at the opinions of their nearest neighbors based on:

1) a **majority** mechanism, in which agents randonly decide to take up the majority opinion of their neighbors
2) a **persuasion** mechanism, in which agents randomly adopt the opinion of one of their neighbors

## How to run

To launch the model install the requirements first:
```
pip install -r requirements.txt
```

and then run:
```
python voter/run.py
```

## Files

- [model.py](model.py): the 2-D Voter model
- [agents.py](agents.py): code containing the voting agent class 
- [server.py](server.py): code for interactive visualization
- [run.py](run.py): code to launch the server that visualizes a model run

# References

- Lipowski, A., Lipowska, D., & Ferreira, A. L. (2017). Phase transition and power-law coarsen-
ing in Ising-doped voter model. *Physical Review E, 96* (3), 032145. [doi](https://doi.org/10.1103/PhysRevE.96.032145)
