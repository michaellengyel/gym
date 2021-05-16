# gym
Reinforcement Learning Environments

## Foreword
This repository contains a number of private reinforcement learning environments.
The objective is to create environments which are easy to use and easy to change.
This repository is meant to be used as a sub-repository

### Quick Start Guide
From the cloned repository, run the following commands in the terminal:

$ conda env create -f environment.yml  
$ conda activate gym_env

If using pycharm, set the interpreter to the python version in the created conda env e.g:

.../anaconda3/envs/gym_env/bin/python

There are two ways to test the environment. Run the "suite_manual.py" file to test manually or run "suite_random.py" to test random behaviour.

When adding or removing a dependency from the environment.yml list, run:  
$ conda env update --file environment.yml


### System Dependencies
TBD

### TODO:
(Solve the loading of models by adding h5py to environment.yml)
pip install tensorflow h5py==2.10.0