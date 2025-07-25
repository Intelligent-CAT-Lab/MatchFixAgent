#!/bin/bash

CONFIG_FILE_PATH=$1

export PYTHONPATH=$(pwd):$PYTHONPATH
python3 src/evaluate/validate.py --config_file=$CONFIG_FILE_PATH
