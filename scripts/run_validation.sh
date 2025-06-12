#!/bin/bash

PROJECT_NAME=$1
AGENT_NAME=$2

export PYTHONPATH=$(pwd):$PYTHONPATH
python3 src/validator/validate.py --config_file=configs/$AGENT_NAME.yaml --project_name=$PROJECT_NAME --agent_name=$AGENT_NAME
