import numpy as np
import pandas as pd
import sys
sys.path.append('ising_mod')
from model import IsingModel
from agents import Spin

import time
start_time = time.time()

# constant parameters
num_steps = 1000
grid_size = 30  # L^2 agents
betas = [0.48]
configurations = [True]  # True: hot, False: cold
field_values = [0]  # external field

# variable parameters
activations = ["random","color", "simultaneous"]  # activation function
algos = ["metropolis", "heat_bath"]

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

for beta in betas:
    for configuration in configurations:
        for field_value in field_values:
            for activation in activations:
                for algo in algos:
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
                        print(i, algo, activation, field_value, energy_calc, magnetization_calc, beta, configuration)

# Export simulation data
df = pd.DataFrame(data)
df.to_csv("studies/algo_study.csv", index=False)

end_time = time.time()

print()
print(f"Elapsed time: {(end_time - start_time):.2f} sec")
print(f"Elapsed time: {(end_time - start_time)/60:.2f} min")