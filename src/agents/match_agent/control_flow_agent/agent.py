import os
import json
import logging
import re
import uuid
from pathlib import Path

from src.utils.agent_utils import Model
from src.utils.agent_utils import Conversation
from src.utils.credential_utils import get_agent_credentials


class ControlFlowAgent:
    """
    Agent that analyzes control flow in source and target code fragments.
    Focuses on conditionals, loops, early returns, and control structures.
    """

    def __init__(self, configs: dict, session_id=None) -> None:
        """
        Initialize the control flow agent.

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

        log_file = log_dir / f"control_flow_agent_{self.session_id}.log"

        self.logger = logging.getLogger(f"control_flow_agent.{self.session_id}")
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

        self.logger.info("Control Flow Agent initialized")

    async def analyze(self, prompt_generator, agent_name=None, sub_agent_name=None):
        """
        Analyze the control flow of source and target code fragments.

        Args:
            prompt_generator: The prompt generator to use
            agent_name (str, optional): Name of the parent agent
            sub_agent_name (str, optional): Name of this sub-agent

        Returns:
            dict: Analysis results
        """
        self.logger.info("Analyzing control flow equivalence")

        # Generate the prompt using the template for control_flow_agent
        prompt = prompt_generator.generate_prompt("control_flow_agent")

        # Log the full prompt
        self.logger.debug("Generated control flow analysis prompt:")
        self.logger.debug(prompt)

        self.conversation.add_message(role="user", content=prompt)

        try:
            # Use the direct Claude API instead of CLI
            from src.utils.cmd_utils import prompt_claude

            # Use agent_name and sub_agent_name for credential rotation
            status, agent_output = await prompt_claude(
                prompt,
                "",
                self.configs,
                self.logger,
                agent_name=agent_name or "control_flow_agent",
                sub_agent_name=sub_agent_name,
            )

            agent_output = agent_output or {}

            if status:
                self.logger.info("Control flow analysis completed successfully")
                # Extract the final response format
                result = agent_output.get("result", "")
                self.logger.debug("Raw response from model:")
                self.logger.debug(result)

                pattern = r"<final_response_format>(.*?)</final_response_format>"
                match = re.search(pattern, result, re.DOTALL)

                if match:
                    try:
                        control_flow_analysis = json.loads(match.group(1))
                        self.logger.info(
                            f"Control flow equivalence: {control_flow_analysis.get('is_equivalent', 'unknown')}"
                        )
                        # Return the entire agent_output with the parsed result
                        agent_output["parsed_final_response"] = control_flow_analysis
                        return agent_output
                    except json.JSONDecodeError as e:
                        self.logger.error(f"Failed to parse control flow analysis response as JSON: {e}")
                        agent_output["parsed_final_response"] = {
                            "is_equivalent": "error",
                            "explanation": f"Failed to parse model response as JSON: {str(e)}",
                        }
                        return agent_output
                else:
                    self.logger.error("No final response format found in control flow analysis output")
                    agent_output["parsed_final_response"] = {
                        "is_equivalent": "error",
                        "explanation": "No final response format found in control flow analysis output",
                    }
                    return agent_output
            else:
                self.logger.error("Control flow analysis failed")
                agent_output["parsed_final_response"] = {
                    "is_equivalent": "error",
                    "explanation": "Control flow analysis did not complete successfully",
                }
                return agent_output

        except Exception as e:
            self.logger.error(f"Error in control flow analysis: {str(e)}")
            agent_output["parsed_final_response"] = {
                "is_equivalent": "error",
                "explanation": f"An error occurred during control flow analysis: {str(e)}",
            }
            return agent_output
