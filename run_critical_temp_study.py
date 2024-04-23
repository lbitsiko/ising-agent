import numpy as np
import pandas as pd
import sys
sys.path.append('ising_mod')
from model import IsingModel
from agents import Spin

import time
start_time = time.time()

# constant parameters
configurations = [True]  # True: hot, False: cold
num_steps = 1000
field_value = 0
grid_size = 30
activation = "random"
algo = "metropolis"

# variable parameters
betas = np.arange(0.4, 0.5, 0.01)

# data structure to collect data
data = {
    "steps":[],
    "energy":[],
    "magnetization":[],
    "beta":[],
    "configuration":[],
    "activation":[],
    "algo":[],
    "grid_size":[],
    "field":[],
}

steps, Es, Ms, betas_run, configurations_run, models = [], [], [], [], [], []
for beta in betas:
    for configuration in configurations:

        mod = IsingModel(L=grid_size, 
                beta=beta, 
                activation = activation, 
                hot_configuration=configuration, 
                algo=algo,
                magnetic_field = field_value)

        # initial observables
        energy_calc = mod.calculate_energy()
        magnetization_calc = mod.calculate_magnetization()
        data["steps"].append(0)
        data["energy"].append(energy_calc)
        data["magnetization"].append(magnetization_calc)
        data["beta"].append(beta)
        data["configuration"].append(configuration)
        data["activation"].append(activation)
        data["algo"].append(algo)
        data["grid_size"].append(grid_size)
        data["field"].append(field_value)

        for i in range(num_steps):
            mod.step()

            # updated observables
            energy_calc = mod.calculate_energy()
            magnetization_calc = mod.calculate_magnetization()
            data["steps"].append(i+1)
            data["energy"].append(energy_calc)
            data["magnetization"].append(magnetization_calc)
            data["beta"].append(beta)
            data["configuration"].append(configuration)
            data["activation"].append(activation)
            data["algo"].append(algo)
            data["grid_size"].append(grid_size)
            data["field"].append(field_value)
            
            # print for logging
            print(i, mod.calculate_energy(), mod.calculate_magnetization(), beta, configuration)

# Export simulation data
df = pd.DataFrame(data)
df.to_csv("studies/critical_temp_study.csv", index=False)

end_time = time.time()

print()
print(f"Elapsed time: {(end_time - start_time):.2f} sec")
print(f"Elapsed time: {(end_time - start_time)/60:.2f} min")