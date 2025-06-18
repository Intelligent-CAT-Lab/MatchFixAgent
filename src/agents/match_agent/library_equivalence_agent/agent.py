import os
import json
import logging
import re
import uuid
from pathlib import Path

from src.utils.agent_utils import Model
from src.utils.agent_utils import Conversation


class LibraryEquivalenceAgent:
    """
    Agent that analyzes library usage in source and target code fragments.
    Focuses on standard library functions, third-party libraries, and API differences.
    """

    def __init__(self, configs: dict, session_id=None) -> None:
        """
        Initialize the library equivalence agent.

        Args:
            configs (dict): Configuration for the agent
            session_id (str, optional): Session ID for logging. If None, a new UUID will be generated.
        """
        self.configs = configs
        self.model = Model(self.configs["model"])
        self.conversation = Conversation()
        self.session_id = session_id or str(uuid.uuid4())

        # Set up logging
        log_dir = Path(f"logs/match_agent")
        log_dir.mkdir(parents=True, exist_ok=True)

        log_file = log_dir / f"library_equivalence_agent_{self.session_id}.log"

        self.logger = logging.getLogger(f"library_equivalence_agent.{self.session_id}")
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

        self.logger.info("Library Equivalence Agent initialized")

    async def analyze(self, prompt_generator, method_pair, agent_name=None, sub_agent_name=None):
        """
        Analyze the library usage of source and target code fragments.

        Args:
            prompt_generator: The prompt generator to use
            method_pair (dict): The method pair to analyze
            agent_name (str, optional): Name of the parent agent
            sub_agent_name (str, optional): Name of this sub-agent

        Returns:
            dict: Analysis results
        """
        self.logger.info("Analyzing library usage equivalence")

        # Generate the prompt using the template for library_equivalence_agent
        prompt = prompt_generator.generate_prompt("library_equivalence_agent")

        # Log the full prompt
        self.logger.debug("Generated library equivalence analysis prompt:")
        self.logger.debug(prompt)

        self.conversation.add_message(role="user", content=prompt)

        # Execute the model
        env = os.environ.copy()
        env["CLAUDE_CODE_USE_BEDROCK"] = "true"
        env["ANTHROPIC_MODEL"] = self.model.model_name

        try:
            # Use the dedicated utility function for command execution
            from src.utils.cmd_utils import run_claude_command

            status, agent_output = await run_claude_command(
                prompt,
                "",
                self.model.model_name,
                self.configs,
                self.logger,
                agent_name=agent_name or "library_equivalence_agent",
                sub_agent_name=sub_agent_name,
            )

            agent_output = agent_output or {}

            if status:
                self.logger.info("Library equivalence analysis completed successfully")
                # Extract the final response format
                result = agent_output.get("result", "")
                self.logger.debug("Raw response from model:")
                self.logger.debug(result)

                pattern = r"<final_response_format>(.*?)</final_response_format>"
                match = re.search(pattern, result, re.DOTALL)

                if match:
                    try:
                        library_analysis = json.loads(match.group(1))
                        self.logger.info(
                            f"Library usage equivalence: {library_analysis.get('is_equivalent', 'unknown')}"
                        )
                        # Return the entire agent_output with the parsed result
                        agent_output["parsed_final_response"] = library_analysis
                        return agent_output
                    except json.JSONDecodeError as e:
                        self.logger.error(f"Failed to parse library equivalence analysis response as JSON: {e}")
                        agent_output["parsed_final_response"] = {
                            "is_equivalent": "error",
                            "explanation": "Failed to parse response as JSON: " + str(e),
                        }
                        return agent_output
                else:
                    self.logger.error("No final response format found in library equivalence analysis output")
                    agent_output["parsed_final_response"] = {
                        "is_equivalent": "error",
                        "explanation": "No final response format found in the output",
                    }
                    return agent_output
            else:
                self.logger.error("Library equivalence analysis failed")
                agent_output["parsed_final_response"] = {
                    "is_equivalent": "error",
                    "explanation": "Library equivalence analysis failed to execute properly",
                }
                return agent_output

        except Exception as e:
            self.logger.error(f"Error in library equivalence analysis: {str(e)}")
            agent_output["parsed_final_response"] = {
                "is_equivalent": "error",
                "explanation": "An error occurred during library equivalence analysis: " + str(e),
            }
            return agent_output
