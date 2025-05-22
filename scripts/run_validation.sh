#!/bin/bash

project_name=$1

export PYTHONPATH=$(pwd):$PYTHONPATH
python3 src/validator/validate.py --config_file=configs/agent_configs.yaml --project_name=$project_name
