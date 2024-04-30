import numpy as np
import pandas as pd
from mesa.batchrunner import batch_run
from multiprocessing import freeze_support

import sys
sys.path.append('ising_mod')

from model import IsingModel

# input parameters
params = {
    "L": [30],  
    "beta": np.arange(0.1, 1.0, 0.01).tolist(),
    "magnetic_field": [-1, 0, 1],
    "hot_configuration": [False],#[True, False],
    "algo": ["heat_bath"],#["metropolis", "heat_bath"], 
    "activation": ["simultaneous"],
    "seed": [69]
}

# batch run
# freeze_support()  # for multiprocessing support in Windows
results = batch_run(
    IsingModel,
    parameters=params,
    iterations=1,
    max_steps=1000,
    number_processes=1,  
    data_collection_period=1,
    display_progress=True
)

# results to DataFrame
results_df = pd.DataFrame(results)
out_fname = "batch_run_field.csv"
results_df.to_csv(out_fname, index=False)
print()
print(f"Batch run complete. Results in {out_fname}")
print()