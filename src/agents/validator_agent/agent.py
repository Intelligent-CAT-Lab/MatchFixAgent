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
import uuid
from pathlib import Path

from src.utils.agent_utils import MCPConfig
from src.utils.agent_utils import Model
from src.utils.agent_utils import Conversation

from src.agents.validator_agent.prompt_generator import ValidatorAgentPromptGenerator


class ValidatorAgent:
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

    def __init__(self, model: Model, mcp_config: MCPConfig) -> None:
        """
        Initialize the validator agent with a model and configuration.

        Args:
            model (Model): The LLM model to use for validation
            mcp_config (MCPConfig): Configuration for the model control plane
        """
        self.model = model
        self.conversation = Conversation()
        self.session_id = str(uuid.uuid4())

        # Set up logging
        log_dir = Path("logs/validator_agent")
        log_dir.mkdir(parents=True, exist_ok=True)

        log_file = log_dir / f"{self.session_id}.log"

        self.logger = logging.getLogger(f"validator_agent.{self.session_id}")
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

        self.logger.info(f"Validator Agent initialized with session ID: {self.session_id}")
        self.logger.info(f"Using model: {model.model_name}")

    async def run_cmd(self, prompt: str) -> tuple[bool, dict]:
        """
        Execute Claude CLI command with the given prompt.

        Runs Claude via CLI subprocess and parses the JSON output.

        Args:
            prompt (str): The prompt to send to Claude

        Returns:
            tuple[bool, dict]: (success_status, parsed_output)
                - success_status: True if command executed successfully and output was valid JSON
                - parsed_output: The parsed JSON output from Claude, or None if unsuccessful
        """
        env = os.environ.copy()
        env["CLAUDE_CODE_USE_BEDROCK"] = "true"
        env["ANTHROPIC_MODEL"] = self.model.model_name
        env["PATH"] = f"{os.path.expanduser('~/apache-maven-3.9.9/bin')}:{env['PATH']}"

        try:
            self.logger.info("Executing Claude CLI command...")
            # Use asyncio.create_subprocess_exec for true async operation
            process = await asyncio.create_subprocess_exec(
                "claude",
                "-p",
                prompt,
                "--output-format",
                "json",
                "--dangerously-skip-permissions",
                stdout=asyncio.subprocess.PIPE,
                stderr=asyncio.subprocess.PIPE,
                env=env,
            )

            stdout, stderr = await process.communicate()

            if process.returncode != 0:
                self.logger.error(f"Claude failed with exit code {process.returncode}")
                self.logger.error(f"Error details: {stderr.decode()}")
                return False, None

            output = stdout.decode("utf-8")
            self.logger.debug("Raw output received from Claude")

            try:
                parsed_output = json.loads(output)
                self.logger.info("Successfully parsed Claude output as JSON")
                return True, parsed_output
            except json.JSONDecodeError as e:
                self.logger.error(f"Failed to parse Claude output as JSON: {e}")
                self.logger.debug(f"Raw output: {output}")
                return False, None

        except Exception as e:
            self.logger.error(f"Error executing Claude: {str(e)}")
            return False, None

    async def validate_agent_output(self, agent_output: dict) -> tuple[bool, dict]:
        """
        Validate and parse the agent's output.

        Extracts the final response format from the agent output and parses it as JSON.

        Args:
            agent_output (dict): The raw output from the agent

        Returns:
            tuple[bool, dict]: (validation_status, parsed_output)
                - validation_status: True if the output was successfully validated
                - parsed_output: The original output with the parsed final response added,
                  or None if validation failed
        """
        # extract the <final_response_format> </final_response_format> from the agent output
        result = agent_output.get("result", None)
        if result is None:
            self.logger.error("No result found in agent output")
            return False, None

        self.logger.info("Extracting final response format from agent output")
        pattern = r"<final_response_format>(.*?)</final_response_format>"
        match = re.search(pattern, result, re.DOTALL)

        if match:
            final_response = match.group(1)
            try:
                # Attempt to parse the final response as JSON
                parsed_response = json.loads(final_response)
                agent_output["parsed_final_response"] = parsed_response
                self.logger.info("Successfully parsed final response as JSON")
                return True, agent_output
            except json.JSONDecodeError as e:
                self.logger.error(f"Final response is not valid JSON: {e}")
                self.logger.debug(f"Invalid JSON: {final_response}")
                return False, None
        else:
            self.logger.error("No final response format found in agent output")
            return False, None

    async def run(
        self,
        configs: dict,
        source_schema_name: str,
        target_schema_name: str,
        class_name: str,
        method_name: str,
        method_pair: dict,
    ) -> tuple[bool, dict]:
        """
        Run the validator agent to check equivalence between source and target code.

        This is the main method that orchestrates the entire validation process:
        1. Generates a prompt for the validator
        2. Executes the Claude model
        3. Validates the model's output
        4. Returns validation results with detailed reasoning

        Args:
            configs (dict): Configuration settings
            source_schema_name (str): Name of the source schema
            target_schema_name (str): Name of the target schema
            class_name (str): Name of the class containing the method
            method_name (str): Name of the method to validate
            method_pair (dict): Dictionary containing source and target code

        Returns:
            tuple[bool, dict]: (success_status, validation_results)
                - success_status: True if validation was successfully completed
                - validation_results: The validation results including detailed reasoning,
                  or None if validation failed
        """
        self.logger.info(f"Running validator for {class_name}.{method_name}")
        self.logger.info(f"Source schema: {source_schema_name}")
        self.logger.info(f"Target schema: {target_schema_name}")

        prompt_generator = ValidatorAgentPromptGenerator(
            configs=configs,
            source_schema_name=source_schema_name,
            target_schema_name=target_schema_name,
            class_name=class_name,
            method_name=method_name,
            method_pair=method_pair,
        )
        prompt = prompt_generator.generate_prompt()

        self.logger.debug("Generated prompt:")
        self.logger.debug(prompt)

        self.conversation.add_message(role="user", content=prompt)

        max_retries = configs["agents"]["validator_agent"]["max_retries"]
        self.logger.info(f"Maximum retries: {max_retries}")

        agent_output = None
        status = False

        while True:
            remaining_retries = max_retries
            max_retries -= 1
            self.logger.info(f"Executing agent (remaining retries: {remaining_retries})...")

            status, agent_output = await self.run_cmd(prompt)
            if status:
                self.logger.info("Command execution successful, validating output...")
                validation_status, agent_output = await self.validate_agent_output(agent_output)
                if validation_status:
                    self.logger.info("Agent output validation successful")
                    break
                else:
                    self.logger.warning("Agent output validation failed")
                    if max_retries == 0:
                        self.logger.error("Max retries reached")
                        break
                    self.logger.info("Retrying...")
            else:
                self.logger.warning("Command execution failed")
                if max_retries == 0:
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
            original_log_file = Path("logs/validator_agent") / f"{self.session_id}.log"
            new_log_file = Path("logs/validator_agent") / f"{agent_output['session_id']}.log"

            # Only rename if the paths are different
            if original_log_file != new_log_file:
                # Use shutil.copy2 and then remove the original instead of rename
                # This avoids issues if the files are on different filesystems
                import shutil

                shutil.copy2(original_log_file, new_log_file)
                original_log_file.unlink(missing_ok=True)

                # Create a new logger with the new session ID
                new_logger = logging.getLogger(f"validator_agent.{agent_output['session_id']}")
                new_logger.setLevel(logging.INFO)
                new_logger.propagate = False

                # Log the file rename operation using the root logger since our logger is closed
                logging.getLogger().info(f"Log file renamed from {original_log_file} to {new_log_file}")

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

    logger = logging.getLogger("validator_agent_main")
    logger.info(f"Starting validator agent with config file: {args.config_file}")

    configs = yaml.safe_load(open(args.config_file, "r"))
    args.model = configs["agents"]["validator_agent"]["model"]
    args.mcp_config_file = configs["agents"]["validator_agent"]["mcp_config_file"]

    model = Model(args.model)
    mcp_config = MCPConfig(args.mcp_config_file)

    validator_agent = ValidatorAgent(model, mcp_config)

    ### sample test case
    logger.info("Running sample test case")

    source_schema_name = "commons-cli.src.main.java.org.apache.commons.cli.PatternOptionBuilder"
    target_schema_name = "commons-cli.src.main.org.apache.commons.cli.PatternOptionBuilder"
    class_name = "PatternOptionBuilder"
    method_name = "135-138:isValueCode"
    method_pair = {
        "graal_validation": "success",
        "source_code": [
            "    public static boolean isValueCode(final char ch) {",
            "        return ch == '@' || ch == ':' || ch == '%' || ch == '+' || ch == '#' || ch == '<'",
            "                || ch == '>' || ch == '*' || ch == '/' || ch == '!';",
            "    }",
            "",
        ],
        "target_code": [
            "    @staticmethod",
            "    def isValueCode(ch: str) -> bool:",
            "        return ch in {'@', ':', '%', '+', '#', '<', '>', '*', '/', '!'}",
        ],
    }

    status, result = asyncio.run(
        validator_agent.run(configs, source_schema_name, target_schema_name, class_name, method_name, method_pair)
    )
