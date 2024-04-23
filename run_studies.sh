#!/bin/bash

# Run the critical temperature study
python -u run_critical_temp_study.py >> logs/run_critical_temp_study.log

# Run the magnetic field study
python -u run_field_study.py >> logs/run_field_study.log

# Run the algo study
python -u run_algo_study.py >> logs/run_algo_study.log
