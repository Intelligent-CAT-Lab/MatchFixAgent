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

from src.utils.agent_utils import MCPConfig
from src.utils.agent_utils import Model
from src.utils.agent_utils import Conversation

from src.agents.base_agent.prompt_generator import BaseAgentPromptGenerator
from src.utils.cmd_utils import run_claude_command
from src.utils.credential_utils import setup_environment_for_agent, get_agent_credentials


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
        self.mcp_config = MCPConfig(self.configs["mcp_config_file"])
        self.conversation = Conversation()
        self.session_id = str(uuid.uuid4())

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

    async def run_cmd(self, prompt: str, feedback: str) -> tuple[bool, dict]:
        """
        Execute Claude CLI command with the given prompt.

        Runs Claude via CLI subprocess and parses the JSON output.

        Args:
            prompt (str): The prompt to send to Claude
            feedback (str): Optional feedback to append to the prompt for retries

        Returns:
            tuple[bool, dict]: (success_status, parsed_output)
                - success_status: True if command executed successfully and output was valid JSON
                - parsed_output: The parsed JSON output from Claude, or None if unsuccessful
        """
        # Use shared command utility for consistent credential handling
        return await run_claude_command(
            prompt=prompt,
            feedback=feedback,
            configs=self.configs,
            logger=self.logger,
            agent_name=self.configs["agent_name"],
            timeout=300,
        )

    async def validate_agent_output(self, agent_output: dict) -> tuple[bool, dict, str]:
        """
        Validate and parse the agent's output.

        Extracts the final response format from the agent output and parses it as JSON.

        Args:
            agent_output (dict): The raw output from the agent

        Returns:
            tuple[bool, dict, str]: (validation_status, parsed_output, feedback)
                - validation_status: True if the output was successfully validated
                - parsed_output: The original output with the parsed final response added,
                  or None if validation failed
                - feedback: A message indicating the validation result
        """
        # extract the <final_response_format> </final_response_format> from the agent output
        result = agent_output.get("result", None)
        if result is None:
            self.logger.error("No result found in agent output")
            return False, None, "No result found in agent output"

        self.logger.info("Extracting final response format from agent output")
        pattern = r"<final_response_format>(.*?)</final_response_format>"
        match = re.search(pattern, result, re.DOTALL)

        if match:
            final_response = match.group(1)
            try:
                # Attempt to parse the final response as JSON
                parsed_response = json.loads(final_response, strict=False)

                if (
                    len(parsed_response) != 2
                    or "is_equivalent" not in parsed_response
                    or "explanation" not in parsed_response
                ):
                    self.logger.error("Parsed response does not match expected response format")
                    return False, None, "Parsed response does not match expected response format"

                agent_output["parsed_final_response"] = parsed_response
                self.logger.info("Successfully parsed final response as JSON")
                return True, agent_output, "Final response format validated successfully"
            except json.JSONDecodeError as e:
                self.logger.error(f"Final response is not valid JSON: {e}")
                self.logger.debug(f"Invalid JSON: {final_response}")
                return False, None, "Final response is not valid JSON"
        else:
            self.logger.error("No final response format found in agent output")
            return False, None, "Final response format not found in agent output"

    async def run(self, fragment_details: dict) -> tuple[bool, dict]:
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

        self.conversation.add_message(role="user", content=prompt)

        max_retries = self.configs["max_retries"]
        self.logger.info(f"Maximum retries: {max_retries}")

        agent_output = None
        status = False
        feedback = ""

        for attempt in range(max_retries + 1):
            self.logger.info(f"Execution attempt {attempt+1}/{max_retries}")

            status, agent_output = await self.run_cmd(prompt, feedback)

            if status:
                self.logger.info("Command execution successful, validating output...")
                validation_status, agent_output, feedback = await self.validate_agent_output(agent_output)
                if validation_status:
                    self.logger.info("Agent output validation successful")
                    break
                else:
                    self.logger.warning("Agent output validation failed")
                    if attempt == max_retries:
                        self.logger.error("Max retries reached. Exiting.")
                        break
                    self.logger.info("Retrying...")
            else:
                self.logger.warning("Command execution failed")
                if attempt == max_retries:
                    self.logger.error("Max retries reached. Exiting.")
                    break
                self.logger.info("Retrying command execution...")

        if status:
            self.logger.info("Agent execution completed successfully")
            self.logger.debug("Agent output:")
            for key, value in agent_output.items():
                self.logger.debug(f"{key}: {value}")
        else:
            self.logger.error("Agent execution failed")

        if status:
            self.logger.info("Validation successful")
            self.logger.debug("Validation result:")
            for key, value in agent_output.items():
                self.logger.debug(f"{key}: {value}")

            # Close the current log handlers to release the file
            for handler in self.logger.handlers[:]:
                handler.close()
                self.logger.removeHandler(handler)

            # Original and new log file paths
            original_log_file = Path(f"logs/base_agent") / f"{self.session_id}.log"
            final_session_id = f"{self.configs['tool_name']}.{self.configs['project_name']}.{self.configs['source_language']}.{self.configs['target_language']}.{fragment_details['id']}"
            new_log_file = Path(f"logs/base_agent") / final_session_id / f"{final_session_id}.log"
            logger_name = f"base_agent.{final_session_id}"

            os.makedirs(new_log_file.parent, exist_ok=True)

            # Only rename if the paths are different
            if original_log_file != new_log_file:
                # Use shutil.copy2 and then remove the original instead of rename
                # This avoids issues if the files are on different filesystems

                shutil.copy2(original_log_file, new_log_file)
                original_log_file.unlink(missing_ok=True)

                # Create a new logger with the new session ID
                new_logger = logging.getLogger(logger_name)
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

                # Log the file rename operation using the new logger
                new_logger.info(f"Log file renamed from {original_log_file} to {new_log_file}")

        else:
            logging.getLogger().error("Validation failed")

        return status, agent_output


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
