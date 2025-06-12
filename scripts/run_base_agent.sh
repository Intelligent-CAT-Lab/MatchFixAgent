#!/bin/bash

export PYTHONPATH=$(pwd):$PYTHONPATH
python3 src/agents/base_agent/agent.py --config_file configs/base_agent.yaml --log_level DEBUG
