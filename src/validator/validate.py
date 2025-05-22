"""
Validate existing code translations using the ValidatorAgent.

This module provides functionality to validate method translations between
Java and Python using LLM-based semantic analysis through the ValidatorAgent.
"""

import os
import argparse
import yaml
import json
import asyncio

from src.agents.validator_agent.agent import ValidatorAgent
from src.utils.agent_utils import MCPConfig
from src.utils.agent_utils import Model


def validate_by_agent(
    configs: dict,
    schema_name: str,
    class_name: str,
    method_name: str,
    method_pair: dict,
) -> tuple[bool, dict]:
    """
    Validate a single method translation using the ValidatorAgent.

    Args:
        configs (dict): Configuration settings from the YAML config file
        schema_name (str): Name of the schema containing the method
        class_name (str): Name of the class containing the method
        method_name (str): Name of the method to validate
        method_pair (dict): Dictionary containing source and target code

    Returns:
        tuple[bool, dict]: A tuple containing:
            - status (bool): True if validation was successful
            - agent_output (dict): The validation results from the agent
    """
    source_schema_name = schema_name.replace("_python_partial", "").replace("src.main.", "src.main.java.")
    target_schema_name = schema_name.replace("_python_partial", "")

    model = Model(configs["agents"]["validator_agent"]["model"])
    mcp_config = MCPConfig(configs["agents"]["validator_agent"]["mcp_config_file"])

    validator_agent = ValidatorAgent(
        model=model,
        mcp_config=mcp_config,
    )

    status, agent_output = asyncio.run(
        validator_agent.run(configs, source_schema_name, target_schema_name, class_name, method_name, method_pair)
    )

    return status, agent_output


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

    results_path = configs["agents"]["validator_agent"]["tool_results_path"]
    with open(os.path.join(results_path, f"{args.project_name}.json"), "r") as f:
        results = json.load(f)

    for schema_name in results:
        for class_name in results[schema_name]:
            for method_name in results[schema_name][class_name]:

                if "validator_agent" in results[schema_name][class_name][method_name]:
                    if results[schema_name][class_name][method_name]["validator_agent"]["status"] == "success":
                        continue

                status, agent_output = validate_by_agent(
                    configs=configs,
                    schema_name=schema_name,
                    class_name=class_name,
                    method_name=method_name,
                    method_pair=results[schema_name][class_name][method_name],
                )

                results[schema_name][class_name][method_name]["validator_agent"] = {
                    "status": status,
                    "output": agent_output,
                }

                with open(os.path.join(results_path, f"{args.project_name}.json"), "w") as f:
                    json.dump(results, f, indent=4)


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
