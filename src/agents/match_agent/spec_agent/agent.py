import os
import json
import logging
import re
import uuid
import yaml
from pathlib import Path

from src.utils.credential_utils import get_agent_credentials
from src.utils.model_utils import ModelUtils


class SpecAgent:
    """
    Agent that analyzes specification adherence in source and target code fragments.
    Focuses on function contracts, documented behavior, and implicit contracts.
    """

    def __init__(self, configs: dict, session_id=None) -> None:
        """
        Initialize the specification agent.

        Args:
            configs (dict): Configuration for the agent
            session_id (str, optional): Session ID for logging. If None, a new UUID will be generated.
        """
        self.configs = configs
        self.session_id = session_id or str(uuid.uuid4())
        self.errors = yaml.safe_load(open("configs/errors.yaml", "r"))

        # Set up logging
        log_dir = Path(f"logs/{self.configs['agent_name']}")
        log_dir.mkdir(parents=True, exist_ok=True)

        log_file = log_dir / f"spec_agent_{self.session_id}.log"

        self.logger = logging.getLogger(f"spec_agent.{self.session_id}")
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

        self.logger.info("Specification Agent initialized")

    async def analyze(self, prompt_generator, agent_name=None, sub_agent_name=None):
        """
        Analyze the specification adherence of source and target code fragments.

        Args:
            prompt_generator: The prompt generator to use
            agent_name (str, optional): Name of the parent agent
            sub_agent_name (str, optional): Name of this sub-agent

        Returns:
            dict: Analysis results
        """
        self.logger.info("Analyzing specification adherence")

        # Generate the prompt using the template for spec_agent
        prompt = prompt_generator.generate_prompt("spec_agent")

        # Log the full prompt
        self.logger.debug("Generated specification analysis prompt:")
        self.logger.debug(prompt)

        try:
            # Use the model utility wrapper
            model_utils = ModelUtils(configs=self.configs, logger=self.logger)

            status, agent_output = await model_utils.prompt_model(
                prompt=prompt,
                feedback="",
                agent_name=agent_name or "spec_agent",
                sub_agent_name=sub_agent_name,
            )

            agent_output = agent_output or {}

            if status:
                self.logger.info("Specification analysis completed successfully")
                # Extract the final response format
                result = agent_output.get("result", "")
                self.logger.debug("Raw response from model:")
                self.logger.debug(result)

                pattern = r"<final_response_format>(.*?)</final_response_format>"
                match = re.search(pattern, result, re.DOTALL)

                if match:
                    try:
                        spec_analysis = json.loads(match.group(1), strict=False)
                        self.logger.info(
                            f"Specification adherence equivalence: {spec_analysis.get('is_equivalent', 'unknown')}"
                        )
                        # Return the entire agent_output with the parsed result
                        agent_output["parsed_final_response"] = spec_analysis
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
