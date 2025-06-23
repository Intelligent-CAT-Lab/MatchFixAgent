"""
Validate existing code translations using the ValidatorAgent.

This module provides functionality to validate method translations between
Java and Python using LLM-based semantic analysis through the ValidatorAgent.
"""

import os
import argparse
import yaml
import json
import shutil
import subprocess
import asyncio

from src.agents.base_agent.agent import BaseAgent
from src.agents.match_agent.agent import MatchAgent


def validate_by_agent(configs: dict, fragment_details: dict) -> tuple[bool, dict]:
    """
    Validate a single method translation using the ValidatorAgent.

    Args:
        configs (dict): Configuration settings from the YAML config file
        fragment_details (dict): Details of the method to validate, including:

    Returns:
        tuple[bool, dict]: A tuple containing:
            - status (bool): True if validation was successful
            - agent_output (dict): The validation results from the agent
    """

    validator_agent = None
    if configs["agent_name"] == "base_agent":
        validator_agent = BaseAgent(configs=configs)
    elif configs["agent_name"] == "match_agent":
        validator_agent = MatchAgent(configs=configs)
    else:
        raise ValueError(f"Agent {configs['agent_name']} is not supported")

    status, agent_output = asyncio.run(validator_agent.run(fragment_details))

    return status, agent_output


def cleanup():
    """
    Cleanup function to remove temporary files created during validation.

    This function deletes the temporary files used by the ValidatorAgent
    to ensure no residual data is left after validation.
    """

    # Run `git status --porcelain data/tool_projects`
    proc = subprocess.run(
        ["git", "status", "--porcelain", "data/tool_projects"], capture_output=True, text=True, check=True
    )
    for line in proc.stdout.splitlines():
        if not line.strip():
            continue
        status, path = line[:2], line[3:]
        # Untracked files (“??”) → delete
        if status.strip() == "??":
            if os.path.isdir(path):
                shutil.rmtree(path)
            elif os.path.isfile(path):
                os.remove(path)
        # Any other status → restore to HEAD
        else:
            subprocess.run(["git", "restore", path], check=False)


def main(args):
    """
    Main function to process all methods in a project file and validate translations.

    Iterates through all methods in the project JSON file, validates each method using
    the ValidatorAgent, and updates the results file after each validation.

    Args:
        args (Namespace): Command-line arguments including:
            - config_file: Path to configuration file
            - project_name: Name of the project to validate
    """
    configs = yaml.safe_load(open(args.config_file, "r"))

    results_path = configs["tool_results_path"]
    with open(os.path.join(results_path, f"{args.project_name}.json"), "r") as f:
        results = json.load(f)

    for fragment_details in results:

        if (
            fragment_details["source_language"] != configs["source_language"]
            or fragment_details["target_language"] != configs["target_language"]
        ):
            continue

        if configs["agent_name"] in fragment_details:
            if fragment_details[configs["agent_name"]]["status"]:
                continue

        status, agent_output = validate_by_agent(configs, fragment_details)

        fragment_details[configs["agent_name"]] = {
            "status": status,
            "output": agent_output,
        }

        with open(os.path.join(results_path, f"{args.project_name}.json"), "w") as f:
            json.dump(results, f, indent=4)

        cleanup()


if __name__ == "__main__":
    """
    Command-line entry point for validation script.

    Parses command-line arguments and calls the main function to validate translations.
    """
    parser = argparse.ArgumentParser(description="Validate existing translations using the Validator Agent")
    parser.add_argument("--config_file", type=str, required=True, help="Path to the config file")
    parser.add_argument("--project_name", type=str, required=True, help="Name of the project")
    args = parser.parse_args()

    main(args)
