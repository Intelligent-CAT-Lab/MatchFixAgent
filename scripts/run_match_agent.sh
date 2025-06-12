#!/bin/bash

export PYTHONPATH=$(pwd):$PYTHONPATH
python3 src/agents/match_agent/agent.py --config_file configs/match_agent.yaml --log_level DEBUG
