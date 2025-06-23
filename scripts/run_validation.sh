#!/bin/bash

PROJECT_NAME=$1
CONFIG_FILE_NAME=$2

export PYTHONPATH=$(pwd):$PYTHONPATH
python3 src/validator/validate.py --config_file=configs/$CONFIG_FILE_NAME.yaml --project_name=$PROJECT_NAME
