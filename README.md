# ising-agent
This repository contains code to simulate the [Ising model](https://stanford.edu/~jeffjar/statmech/intro4.html) using the [Python Mesa framework](https://mesa.readthedocs.io/en/stable/).
Updating schemes implemented include the Metropolis algorithm and the Heat bath approach (see [here](https://courses.physics.illinois.edu/phys498cmp/sp2022/Ising/IsingModel.html)), while an external magnetic field is also introduced.


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
In order to run some parameter evaluation studies:
- Run the [run_studies.sh](run_studies.sh) script 
- The script calls the following batch runs:
  - [run_algo_study.py](run_algo_study.py): batch study comparing activation methods and updating algorithms (data in [algo_study.csv](studies/algo_study.csv))
    - `num_steps = 1000`
    - `grid_size = 30`
    - `beta = 0.48`
    - `hot_configuration = True`
    - `field_value = 0`
    - `activations = ["random", "simultaneous"]`
    - `algos = ["metropolis", "heat_bath"]`
  - [run_field_study.py](run_field_study.py): batch study for evaluating the effect of an external magnetic field across temperatures (data in [field_study.csv](studies/field_study.csv)) 
    - `num_steps = 1000`
    - `grid_size = 30`
    - `activation = "simultaneous"`
    - `algo = "metropolis"`
    - `hot_configuration = False`
    - `betas = [0.1, 0.2, ...,0.9, 1.0`
    - `magnetic_field = [-1, 0, 1]`
  - [run_critical_temp_study.py](run_critical_temp_study.py): batch study in order to locate the critical temperature for a "hot" initial configuration (data in [critical_temp_study.csv](studies/critical_temp_study.csv))
    - `hot_configurations = True`
    - `num_steps = 1000`
    - `field_value = 0`
    - `grid_size = 30`
    - `activation = "simultaneous"`
    - `algo = "metropolis"`
    - `betas = [0.4, 0.41, ..., 0.49, 0.5]`
- Code to visualize the collected data is found in [parameter_evaluation.ipynb](parameter_evaluation.ipynb)

## Files

model files:
- [model.py](ising_mod/model.py): the 2-D Ising model with an external magnetic field and multiple updating and activation options
- [agents.py](ising_mod/agents.py): code containing the Ising Spin agent 
- [server.py](ising_mod/server.py): code for interactive visualization
- [run.py](ising_mod/run.py): code to launch the server that visualizes a model run

batch run:
- [run_studies.sh](run_studies.sh): bash script that runs multiple batches of simulations
- [studies](studies): folder with the collected data from the batch runs
- [parameter_evaluation.ipynb](parameter_evaluation.ipynb): a notebook for visualizing the collected data


