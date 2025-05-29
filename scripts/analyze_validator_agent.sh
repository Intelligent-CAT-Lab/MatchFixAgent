#!/bin/bash

export PYTHONPATH=$(pwd):$PYTHONPATH

PROJECT_NAME=$1
RESULTS_DIR=$2
TRAJECTORY_DIR=$3
AGENT_NAME=$4

python3 src/analysis/analyze_validator_agent.py --project_name=$PROJECT_NAME \
                                                --results_dir=$RESULTS_DIR \
                                                --trajectory_dir=$TRAJECTORY_DIR \
                                                --agent_name=$AGENT_NAME \
