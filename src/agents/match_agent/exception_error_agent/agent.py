import os
import json
import logging
import re
import uuid
from pathlib import Path

from src.utils.agent_utils import Model
from src.utils.agent_utils import Conversation
from src.utils.credential_utils import get_agent_credentials


class ExceptionErrorAgent:
    """
    Agent that analyzes exception and error handling in source and target code fragments.
    Focuses on try-catch blocks, error propagation, and recovery mechanisms.
    """

    def __init__(self, configs: dict, session_id=None) -> None:
        """
        Initialize the exception and error agent.

        Args:
            configs (dict): Configuration for the agent
            session_id (str, optional): Session ID for logging. If None, a new UUID will be generated.
        """
        self.configs = configs
        self.conversation = Conversation()
        self.session_id = session_id or str(uuid.uuid4())

        # Set up logging
        log_dir = Path(f"logs/match_agent")
        log_dir.mkdir(parents=True, exist_ok=True)

        log_file = log_dir / f"exception_error_agent_{self.session_id}.log"

        self.logger = logging.getLogger(f"exception_error_agent.{self.session_id}")
        self.logger.setLevel(logging.DEBUG)
        self.logger.propagate = False  # Don't propagate to parent loggers

        # File handler
        file_handler = logging.FileHandler(log_file)
        file_handler.setLevel(logging.DEBUG)

        # Console handler
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)

        # Formatter
        formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
        file_handler.setFormatter(formatter)
        console_handler.setFormatter(formatter)

        # Add handlers
        self.logger.addHandler(file_handler)
        self.logger.addHandler(console_handler)

        self.logger.info("Exception/Error Agent initialized")

    async def analyze(self, prompt_generator, agent_name=None, sub_agent_name=None):
        """
        Analyze the exception and error handling of source and target code fragments.

        Args:
            prompt_generator: The prompt generator to use
            agent_name (str, optional): Name of the parent agent
            sub_agent_name (str, optional): Name of this sub-agent

        Returns:
            dict: Analysis results
        """
        self.logger.info("Analyzing exception handling equivalence")

        # Generate the prompt using the template for exception_error_agent
        prompt = prompt_generator.generate_prompt("exception_error_agent")

        # Log the full prompt
        self.logger.debug("Generated exception handling analysis prompt:")
        self.logger.debug(prompt)

        self.conversation.add_message(role="user", content=prompt)

        try:
            # Use the direct Claude API instead of CLI
            from src.utils.cmd_utils import prompt_claude

            status, agent_output = await prompt_claude(
                prompt,
                "",
                self.configs,
                self.logger,
                agent_name=agent_name or "exception_error_agent",
                sub_agent_name=sub_agent_name,
            )

            agent_output = agent_output or {}

            if status:
                self.logger.info("Exception handling analysis completed successfully")
                # Extract the final response format
                result = agent_output.get("result", "")
                self.logger.debug("Raw response from model:")
                self.logger.debug(result)

                pattern = r"<final_response_format>(.*?)</final_response_format>"
                match = re.search(pattern, result, re.DOTALL)

                if match:
                    try:
                        exception_analysis = json.loads(match.group(1))
                        self.logger.info(
                            f"Exception handling equivalence: {exception_analysis.get('is_equivalent', 'unknown')}"
                        )
                        # Return the entire agent_output with the parsed result
                        agent_output["parsed_final_response"] = exception_analysis
                        return agent_output
                    except json.JSONDecodeError as e:
                        self.logger.error(f"Failed to parse exception handling analysis response as JSON: {e}")
                        agent_output["parsed_final_response"] = {
                            "is_equivalent": "error",
                            "explanation": "Failed to parse response as JSON: " + str(e),
                        }
                        return agent_output
                else:
                    self.logger.error("No final response format found in exception handling analysis output")
                    agent_output["parsed_final_response"] = {
                        "is_equivalent": "error",
                        "explanation": "No final response format found in output",
                    }
                    return agent_output
            else:
                self.logger.error("Exception handling analysis failed")
                agent_output["parsed_final_response"] = {
                    "is_equivalent": "error",
                    "explanation": "Failed to analyze exception handling properly",
                }
                return agent_output

        except Exception as e:
            self.logger.error(f"Error in exception handling analysis: {str(e)}")
            agent_output["parsed_final_response"] = {
                "is_equivalent": "error",
                "explanation": "An error occurred during exception handling analysis: " + str(e),
            }
            return agent_output
