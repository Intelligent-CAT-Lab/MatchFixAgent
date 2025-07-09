import os
import json
import logging
import re
import uuid
import yaml
from pathlib import Path

from src.utils.agent_utils import Model
from src.utils.agent_utils import Conversation
from src.utils.credential_utils import get_agent_credentials


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
        self.conversation = Conversation()
        self.session_id = session_id or str(uuid.uuid4())
        self.errors = yaml.safe_load(open("configs/errors.yaml", "r"))

        # Set up logging
        log_dir = Path(f"logs/match_agent")
        log_dir.mkdir(parents=True, exist_ok=True)

        # Check if session_id already has the proper format (contains dots)
        if "." in self.session_id and len(self.session_id.split(".")) >= 5:
            # Extract components from session_id
            parts = self.session_id.split(".")
            if len(parts) >= 5:
                # Use the proper naming format: library_equivalence_agent.project_name.source_lang.target_lang.fragment_id
                project_name, source_lang, target_lang, fragment_id = parts[1:5]
                log_file = (
                    log_dir / f"library_equivalence_agent.{project_name}.{source_lang}.{target_lang}.{fragment_id}.log"
                )
            else:
                log_file = log_dir / f"library_equivalence_agent.{'.'.join(self.session_id.split('.')[1:])}.log"
        else:
            # Use the old UUID format
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

    async def analyze(self, prompt_generator, agent_name=None, sub_agent_name=None):
        """
        Analyze the library usage of source and target code fragments.

        Args:
            prompt_generator: The prompt generator to use
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

        try:
            # Use the direct Claude API instead of CLI
            from src.utils.cmd_utils import prompt_claude

            status, agent_output = await prompt_claude(
                prompt,
                "",
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
                        library_analysis = json.loads(match.group(1), strict=False)
                        self.logger.info(
                            f"Library usage equivalence: {library_analysis.get('is_equivalent', 'unknown')}"
                        )
                        # Return the entire agent_output with the parsed result
                        agent_output["parsed_final_response"] = library_analysis
                        return agent_output
                    except json.JSONDecodeError as e:
                        agent_output["parsed_final_response"] = self.errors["json_parsing"]
                        agent_output["parsed_final_response"]["explanation"] += f" - {str(e)}"
                        self.logger.error(agent_output["parsed_final_response"]["explanation"])
                        return agent_output
                else:
                    self.logger.error(self.errors["no_response_format"]["explanation"])
                    agent_output["parsed_final_response"] = self.errors["no_response_format"]
                    return agent_output
            else:
                self.logger.error(self.errors["no_response"]["explanation"])
                agent_output["parsed_final_response"] = self.errors["no_response"]
                return agent_output

        except Exception as e:
            agent_output["parsed_final_response"] = self.errors["unexpected_behavior"]
            agent_output["parsed_final_response"]["explanation"] += f" - {str(e)}"
            self.logger.error(agent_output["parsed_final_response"]["explanation"])
            return agent_output
