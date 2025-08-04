#!/bin/bash

export PYTHONPATH=$(pwd):$PYTHONPATH

AGENT_NAME=$1
TOOL_NAME=$2
PROJECT_NAME=$3
TRAJECTORY_DIR="$HOME/.claude/projects"

python3 src/analysis/analyze_validator_agent.py --agent_name=$AGENT_NAME \
                                                --project_name=$PROJECT_NAME \
                                                --tool_name=$TOOL_NAME \
                                                --trajectory_dir=$TRAJECTORY_DIR
