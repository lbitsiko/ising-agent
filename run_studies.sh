#!/bin/bash

# Run the voting study
python -u batch_run_voting.py >> logs/batch_run_voting.log

# Run the magnetic field study
python -u batch_run_field.py >> logs/batch_run_field.log
