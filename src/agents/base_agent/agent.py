"""
Validator Agent for LLM Translation Equivalence Validation

This module provides a ValidatorAgent class that uses Claude to validate
the equivalence between source and target translations of method pairs.

The agent:
1. Takes source and target code in different languages
2. Generates prompts for the Claude model
3. Executes the model via CLI
4. Parses and validates the model's response
5. Returns the validation result with detailed reasoning
"""

import os
import argparse
import asyncio
import json
import yaml
import re
import logging
import shutil
import uuid
from pathlib import Path
from typing import Dict, List, Any, Optional, Tuple

from src.agents.base_agent.prompt_generator import BaseAgentPromptGenerator
from src.utils.model_utils import ModelUtils


class BaseAgent:
    """
    Agent that validates the functional equivalence between source and target code translations.

    Uses Claude model to perform deep semantic analysis of code pairs and determine
    if they are functionally equivalent, handling different programming languages and styles.

    Attributes:
        model (Model): The LLM model to use for validation
        conversation (Conversation): Tracks the conversation history with the model
        session_id (str): Unique identifier for this validation session
        logger (Logger): Configured logger for this agent instance
    """

    def __init__(self, configs: dict) -> None:
        """
        Initialize the validator agent with a model and configuration.

        Args:
            model (Model): The LLM model to use for validation
            mcp_config (MCPConfig): Configuration for the model control plane
        """
        self.configs = configs
        self.mcp_config = self.configs["mcp_config_file"]
        self.session_id = str(uuid.uuid4())
        self.errors = yaml.safe_load(open("configs/errors.yaml", "r"))

        # Set up logging
        log_dir = Path(f"logs/base_agent")
        log_dir.mkdir(parents=True, exist_ok=True)

        log_file = log_dir / f"{self.session_id}.log"

        self.logger = logging.getLogger(f"base_agent.{self.session_id}")
        self.logger.setLevel(logging.DEBUG)  # Set to DEBUG to allow all messages
        self.logger.propagate = False  # Prevent propagation to parent loggers

        # File handler
        file_handler = logging.FileHandler(log_file)
        file_handler.setLevel(logging.DEBUG)

        # Console handler
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)  # Set console to INFO level

        # Formatter
        formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
        file_handler.setFormatter(formatter)
        console_handler.setFormatter(formatter)

        # Add handlers
        self.logger.addHandler(file_handler)
        self.logger.addHandler(console_handler)

        self.logger.info(f"base_agent initialized with session ID: {self.session_id}")

    async def run(self, fragment_details: Dict[str, Any]) -> Tuple[bool, Dict[str, Any]]:
        """
        Run the validator agent to check equivalence between source and target code.

        This is the main method that orchestrates the entire validation process:
        1. Generates a prompt for the validator
        2. Executes the Claude model
        3. Validates the model's output
        4. Returns validation results with detailed reasoning

        Args:
            fragment_details (dict): Details of the method to validate

        Returns:
            tuple[bool, dict]: (success_status, validation_results)
                - success_status: True if validation was successfully completed
                - validation_results: The validation results including detailed reasoning,
                  or None if validation failed
        """
        self.logger.info(f"Starting base agent for {fragment_details['source_path']}")

        prompt_generator = BaseAgentPromptGenerator(configs=self.configs, fragment_details=fragment_details)
        prompt = prompt_generator.generate_prompt()

        self.logger.debug("Generated prompt:")
        self.logger.debug(prompt)

        try:
            self.logger.info("Executing command")
            model_utils = ModelUtils(configs=self.configs, logger=self.logger)
            status, agent_output = await model_utils.prompt_agent(
                prompt=prompt,
                feedback="",
                agent_name=self.configs["agent_name"],
                timeout=300,
            )

            # Handle timeout case
            if agent_output and agent_output.get("timeout", False):
                self.logger.warning(
                    "Execution timed out after 300 seconds, returning is_equivalent=other with explanation"
                )
                # Create default response for timeout
                agent_output["result"] = (
                    f"<final_response_format>{json.dumps(self.errors['timeout'])}</final_response_format>"
                )

            agent_output = agent_output or {}

            if status:
                self.logger.info("Command execution successful")
                # Extract the final response format - check both last_json and result for backward compatibility
                result = ""
                if "last_json" in agent_output and "result" in agent_output["last_json"]:
                    result = agent_output["last_json"]["result"]
                elif "result" in agent_output:
                    result = agent_output["result"]

                self.logger.debug("Raw response from model:")
                self.logger.debug(result)

                pattern = r"<final_response_format>(.*?)</final_response_format>"
                match = re.search(pattern, result, re.DOTALL)

                if match:
                    try:
                        parsed_response = json.loads(match.group(1), strict=False)
                        self.logger.info("Successfully parsed final response as JSON")

                        # Validate the expected keys are present
                        if (
                            len(parsed_response) != 2
                            or "is_equivalent" not in parsed_response
                            or "explanation" not in parsed_response
                        ):
                            agent_output["parsed_final_response"] = self.errors["invalid_format"]
                            status = False
                            self.logger.error("Parsed response does not match expected response format")
                        else:
                            agent_output["parsed_final_response"] = parsed_response
                            # Determine success based on parsed response
                            is_equivalent = parsed_response.get("is_equivalent")
                            status = is_equivalent is not None and is_equivalent != "error"
                    except json.JSONDecodeError as e:
                        agent_output["parsed_final_response"] = self.errors["json_parsing"]
                        agent_output["parsed_final_response"]["explanation"] += f" - {str(e)}"
                        self.logger.error(agent_output["parsed_final_response"]["explanation"])
                        status = False
                else:
                    self.logger.error(self.errors["no_response_format"]["explanation"])
                    agent_output["parsed_final_response"] = self.errors["no_response_format"]
                    status = False
            else:
                self.logger.error(self.errors["no_response"]["explanation"])
                agent_output["parsed_final_response"] = self.errors["no_response"]
                status = False
        except Exception as e:
            agent_output = {}
            agent_output["parsed_final_response"] = self.errors["unexpected_behavior"]
            agent_output["parsed_final_response"]["explanation"] += f" - {str(e)}"
            self.logger.error(agent_output["parsed_final_response"]["explanation"])
            status = False

        # Log the final status
        if status:
            self.logger.info("Validation successful")
        else:
            self.logger.error("Validation failed or incomplete")

        # Generate the final session ID for log files
        final_session_id = f"{self.configs['tool_name']}.{self.configs['project_name']}.{self.configs['source_language']}.{self.configs['target_language']}.{fragment_details['id']}"

        # Use the helper method to rename the log file
        self._rename_log_file(self.session_id, final_session_id)

        return status, agent_output

    def _rename_log_file(self, old_session_id: str, new_session_id: str) -> None:
        """
        Rename a log file from using old_session_id to new_session_id in the filename.

        Args:
            old_session_id (str): The original session ID in the filename
            new_session_id (str): The new session ID to use in the filename
        """
        # Skip if session IDs are the same
        if old_session_id == new_session_id:
            return

        # Define log file paths
        log_dir = Path(f"logs/base_agent")
        original_log_file = log_dir / f"{old_session_id}.log"
        new_log_file = log_dir / new_session_id / f"{new_session_id}.log"
        logger_name = f"base_agent"

        # Only proceed if the original file exists
        if not original_log_file.exists():
            return

        os.makedirs(new_log_file.parent, exist_ok=True)

        # Close logger handlers first
        logger = logging.getLogger(f"{logger_name}.{old_session_id}")
        for handler in logger.handlers[:]:
            handler.close()
            logger.removeHandler(handler)

        # Use shutil.copy2 and then remove the original instead of rename
        # This avoids issues if the files are on different filesystems
        shutil.copy2(original_log_file, new_log_file)
        original_log_file.unlink(missing_ok=True)

        # Create a new logger with the new session ID
        new_logger = logging.getLogger(f"{logger_name}.{new_session_id}")
        new_logger.setLevel(logging.INFO)
        new_logger.propagate = False

        # Add handlers to the new logger
        file_handler = logging.FileHandler(new_log_file)
        file_handler.setLevel(logging.DEBUG)
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)
        formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
        file_handler.setFormatter(formatter)
        console_handler.setFormatter(formatter)
        new_logger.addHandler(file_handler)
        new_logger.addHandler(console_handler)

        # Log the file rename operation
        new_logger.info(f"Log file renamed from {original_log_file} to {new_log_file}")


if __name__ == "__main__":
    """
    Main entry point for running the validator agent from the command line.

    Parses command line arguments, sets up logging, and runs the validator
    on a sample test case.
    """
    parser = argparse.ArgumentParser(description="Validator Agent")
    parser.add_argument("--config_file", type=str, required=True, help="Path to the config file")
    parser.add_argument(
        "--log_level",
        type=str,
        default="INFO",
        choices=["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"],
        help="Set the logging level",
    )
    args = parser.parse_args()

    # Configure root logger
    logging.basicConfig(
        level=getattr(logging, args.log_level), format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )

    logger = logging.getLogger(f"base_agent_main")
    logger.info(f"Starting validator agent with config file: {args.config_file}")

    configs = yaml.safe_load(open(args.config_file, "r"))

    validator_agent = BaseAgent(configs=configs)

    ### sample test case
    logger.info("Running sample test case")

    fragment_details = {
        "project": "commons-cli",
        "source_path": "commons-cli/src/main/java/org/apache/commons/cli/PatternOptionBuilder.java",
        "target_path": "commons-cli/src/main/org/apache/commons/cli/PatternOptionBuilder.py",
        "source_function": [
            "    public static boolean isValueCode(final char ch) {",
            "        return ch == '@' || ch == ':' || ch == '%' || ch == '+' || ch == '#' || ch == '<'",
            "                || ch == '>' || ch == '*' || ch == '/' || ch == '!';",
            "    }",
            "",
        ],
        "target_function": [
            "    @staticmethod",
            "    def isValueCode(ch: str) -> bool:",
            "        return ch in {'@', ':', '%', '+', '#', '<', '>', '*', '/', '!'}",
        ],
        "ground_truth_target_function": "",
        "source_language": "java",
        "target_language": "python",
        "result": "success",
    }

    status, result = asyncio.run(validator_agent.run(fragment_details=fragment_details))

    print("Status:", status)
    print("Result:", json.dumps(result, indent=2))
