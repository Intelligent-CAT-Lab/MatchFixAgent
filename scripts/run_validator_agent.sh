#!/bin/bash

export PYTHONPATH=$(pwd):$PYTHONPATH

python3 src/agents/validator_agent/agent.py --config_file configs/agent_configs.yaml
