import numpy as np
import pandas as pd
import sys
sys.path.append('ising')
from model import IsingModel
from agents import Spin

import time
start_time = time.time()

configurations = [True, False]
betas = np.arange(0, 1.0, 0.1)
num_steps = 50

steps, Es, Ms, betas_run, configurations_run, models = [], [], [], [], [], []
for beta in betas:
    for configuration in configurations:

        mod = IsingModel(100, 100, beta=beta, hot_configuration=configuration)

        # initial observables
        steps.append(0)
        Es.append(mod.calculate_energy())
        Ms.append(mod.calculate_magnetization())
        betas_run.append(beta)
        configurations_run.append(configuration)
        models.append(f"mod_{beta}_{configuration}")

        for i in range(num_steps):
            mod.step()

            # updated observables
            steps.append(i+1)
            Es.append(mod.calculate_energy())
            Ms.append(mod.calculate_magnetization())
            betas_run.append(beta)
            configurations_run.append(configuration)
            models.append(f"mod_{beta}_{configuration}")
            
            print(i, mod.calculate_energy(), mod.calculate_magnetization(), beta, configuration)

# Export simulation data
df = pd.DataFrame({"steps": steps, "energy":Es, "magnetization": Ms, 'beta': betas_run, 'hot': configurations_run, "model": models})
df.to_csv("runs.csv", index=False)

end_time = time.time()

print()
print(f"Elapsed time: {(end_time - start_time):.2f} sec")
print(f"Elapsed time: {(end_time - start_time)/60:.2f} min")