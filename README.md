# ising-agent
This repository contains code to simulate an [Ising model](https://stanford.edu/~jeffjar/statmech/intro4.html) and a [Voter model](https://journals.aps.org/pre/abstract/10.1103/PhysRevE.96.032145) using the [Python Mesa framework](https://mesa.readthedocs.io/en/stable/).

- **Ising model**: updating schemes implemented include the Metropolis algorithm and the Heat bath approach (see [here](https://courses.physics.illinois.edu/phys498cmp/sp2022/Ising/IsingModel.html)), while an external magnetic field is also introduced.
- **Voter model**: updating schemse include a *majority* vote and a *persuasion* mechanism (see [README](voter/README.md)).


## How to run
To launch the models run make sure to install the requirements first:

```
pip install -r requirements.txt
```

You can run them by executing the following lines on a terminal:
```
python ising/run.py
```

```
python voter/run.py
```

### Batch runs
In order to run some parameter evaluation studies:
- Run the [batch_run_field.py](batch_run_field.py) and [batch_run_voting.py](batch_run_voting.py) scripts 
  - [run_field_study.py](run_field_study.py): batch study for evaluating the effect of an external magnetic field across temperatures (data in [field_study.csv](studies/field_study.csv)) 
      - `num_steps = 1000`
      - `grid_size = 30`
      - `activation = "simultaneous"`
      - `algo = "heat_bath"`
      - `hot_configuration = False`
      - `betas = [0.1, 0.2, ...,0.9, 1.0`
      - `magnetic_field = [-1, 0, 1]`
  - [batch_run_voting.py](batch_run_voting.py)
    - `num_steps = 1000`
    - `grid_size = 30`
    - `activation = "simultaneous"`
    - `algo = ["majority", "stochastic_persuasion"]`
    - `prob = [0.1, 0.2, ...,0.9, 1.0`
- Code to visualize the collected data is found in [parameter_evaluation.ipynb](parameter_evaluation.ipynb)

## Files

Ising model files:
- [model.py](ising_mod/model.py): the 2-D Ising model with an external magnetic field and multiple updating and activation options
- [agents.py](ising_mod/agents.py): code containing the Ising Spin agent 
- [server.py](ising_mod/server.py): code for interactive visualization
- [run.py](ising_mod/run.py): code to launch the server that visualizes a model run

Voter model files:
- [model.py](voter/model.py): the 2-D Voter model
- [agents.py](voter/agents.py): code containing the voting agent class 
- [server.py](voter/server.py): code for interactive visualization
- [run.py](voter/run.py): code to launch the server that visualizes a model run

batch run:
- [batch_run_field.py](batch_run_field.py): batch run script that runs multiple simulations for the Ising model
- [batch_run_voting.py](batch_run_voting.py): batch run script that runs multiple simulations for the Voter model
- [studies](studies): folder with the collected data from the batch runs
- [parameter_evaluation.ipynb](parameter_evaluation.ipynb): a notebook for visualizing the collected data
