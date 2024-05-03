import numpy as np
import pandas as pd
from mesa.batchrunner import batch_run
from multiprocessing import freeze_support

import sys
sys.path.append('voter')

from model import VotingModel

# input parameters
params = {
    "L": [30],  
    "prob": np.arange(0.1, 1.0, 0.1).tolist(),
    "activation": ["simultaneous"],
    "seed": [69],
    "algo": ["majority", "stochastic_persuasion"]
}

if __name__ == "__main__":
    # batch run
    freeze_support()  # for multiprocessing support in Windows
    results = batch_run(
        VotingModel,
        parameters=params,
        iterations=1,
        max_steps=1000,
        number_processes=3,  
        data_collection_period=1,
        display_progress=True
    )

    # results to DataFrame
    results_df = pd.DataFrame(results)
    out_fname = "studies/batch_run_voting.csv"
    results_df.to_csv(out_fname, index=False)
    print()
    print(f"Batch run complete. Results in {out_fname}")
    print()