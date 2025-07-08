#!/bin/bash

export PYTHONPATH=$(pwd):$PYTHONPATH
python3 src/parse_results/extract_rustrepotrans.py
python3 src/parse_results/extract_alphatrans.py
# TODO: add more tools here

# note: there might be a need to manually fix some bad rustrepotrans results. do it before running the next command
for agent in base_agent match_agent; do
    for tool in alphatrans rustrepotrans oxidizer skel; do
        mkdir -p data/agent_results/$agent/$tool
        cp -r data/tool_results/$tool/processed_results/*.json data/agent_results/$agent/$tool
        cp -r data/tool_results/$tool/processed_results/*.json data/agent_results/$agent/$tool
    done
done
