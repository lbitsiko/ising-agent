# ising-agent
This repository contains code to simulate the [Ising model](https://stanford.edu/~jeffjar/statmech/intro4.html) using the [Python Mesa framework](https://mesa.readthedocs.io/en/stable/).


## How to run
To launch the model run:

```
python ising/run.py
```
Make sure to install the requirements first:
```
pip install -r requirements.txt
```
### Batch runs
In order to run a basic parameter evaluation study:
- Run the [run_batches.py](run_batches.py) script that returns a [runs.csv](runs.csv) with collected variables per simulation step
  - the script simulates multiple models for 50 steps for the following combinations of parameters:
    1) `beta = [0, 0.1,...,0.9, 1.0]`
    2) `hot_configuration = [True, False]`
- Code to visualize the collected data is found in [parameter_evaluation.ipynb](parameter_evaluation.ipynb)

## Files

model files:
- [model.py](ising/model.py): the 2-D Ising model
- [agents.py](ising/agents.py): code containing the Ising Spin agent 
- [server.py](ising/server.py): code for interactive visualization
- [run.py](ising/run.py): code to launch the server that visualizes a model run

batch run:
- [run_batches.py](run_batches.py): script that runs multiple batches of simulations
- [runs.csv](runs.csv): the collected data from the batch run
- [plottiparameter_evaluation.ipynb](parameter_evaluation.ipynb): a notebook for visualizing the collected data


