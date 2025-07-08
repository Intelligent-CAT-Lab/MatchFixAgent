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


def cleanup(configs: dict):
    """
    Cleanup function to remove temporary files created during validation.

    This function deletes the temporary files used by the ValidatorAgent
    to ensure no residual data is left after validation.
    """

    target_dir = ""
    if configs["tool_name"] == "alphatrans":
        target_dir = os.path.join(
            "data",
            "tool_projects",
            "alphatrans",
            "python_projects",
            "gpt-4o-2024-11-20",
            "body",
            "0.0",
            configs["project_name"],
        )
    else:
        target_dir = os.path.join("data", "tool_projects", configs["tool_name"], "projects", configs["project_name"])

    assert target_dir, f"Target directory {target_dir} does not exist"
    assert os.path.exists(target_dir), f"Target directory {target_dir} does not exist"

    # Run `git status --porcelain data/tool_projects`
    proc = subprocess.run(["git", "status", "--porcelain", target_dir], capture_output=True, text=True, check=True)
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


def insert_translation(item: dict):
    """
    Insert a translation item into the RustRepoTrans tool results.

    This function adds a translation item to the RustRepoTrans tool results
    by appending it to the existing JSON file.

    Args:
        item (dict): The translation item to insert, containing:
            - source_language: Source language of the method
            - target_language: Target language of the method
            - source_code: Source code in the source language
            - target_code: Target code in the target language
            - tool_name: Name of the tool used for translation
    """
    rust_file_path = os.path.join("data", "tool_projects", "rustrepotrans", item["target_path"])
    assert os.path.exists(rust_file_path), f"File {rust_file_path} does not exist"

    content = ""
    with open(rust_file_path, "r") as f:
        content = f.read()

    source_code = "\n".join(item["ground_truth_target_function"])
    target_code = "\n".join(item["target_function"])

    if source_code not in content:
        raise ValueError(f"Source code not found in {rust_file_path}")

    content = content.replace(source_code, "\n" + target_code + "\n")

    with open(rust_file_path, "w") as f:
        f.write(content)


def main(args):
    """
    Main function to process all methods in a project file and validate translations.

    Iterates through all methods in the project JSON file, validates each method using
    the ValidatorAgent, and updates the results file after each validation.

    Args:
        args (Namespace): Command-line arguments including:
            - config_file: Path to configuration file
    """
    configs = yaml.safe_load(open(args.config_file, "r"))

    results_path = configs["tool_results_path"]
    with open(os.path.join(results_path, f"{configs['project_name']}.json"), "r") as f:
        results = json.load(f)

    for fragment_details in results:

        cleanup(configs)

        if (
            fragment_details["source_language"] != configs["source_language"]
            or fragment_details["target_language"] != configs["target_language"]
        ):
            continue

        if configs["agent_name"] in fragment_details:
            if fragment_details[configs["agent_name"]]["status"]:
                continue

        if "rustrepotrans" == configs["tool_name"]:
            try:
                decoded_ground_truth_target_function = [
                    l.encode("latin1").decode("utf-8") for l in fragment_details["ground_truth_target_function"]
                ]
                fragment_details["ground_truth_target_function"] = decoded_ground_truth_target_function
            except UnicodeDecodeError as e:
                print(f"Error decoding ground truth target function: {e}")
                continue

            try:
                insert_translation(fragment_details)
            except ValueError as e:
                print(f"Error inserting translation: {e}")
                raise

        status, agent_output = validate_by_agent(configs, fragment_details)

        fragment_details[configs["agent_name"]] = {
            "status": status,
            "output": agent_output,
        }

        with open(os.path.join(results_path, f"{configs['project_name']}.json"), "w") as f:
            json.dump(results, f, indent=4)

        cleanup(configs)


if __name__ == "__main__":
    """
    Command-line entry point for validation script.

    Parses command-line arguments and calls the main function to validate translations.
    """
    parser = argparse.ArgumentParser(description="Validate existing translations using the Validator Agent")
    parser.add_argument("--config_file", type=str, required=True, help="Path to the config file")
    args = parser.parse_args()

    main(args)
