import os
import json
import logging
import re
import uuid
import asyncio
import yaml
from pathlib import Path

from src.utils.agent_utils import Model
from src.utils.agent_utils import Conversation
from src.utils.credential_utils import get_agent_credentials


class TestGenRepairAgent:
    """
    Agent that generates tests and repairs code based on analysis from other agents.
    Focuses on comprehensive test generation and fixing identified discrepancies.
    """

    def __init__(self, configs: dict, session_id=None) -> None:
        """
        Initialize the test generation and repair agent.

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

        log_file = log_dir / f"test_gen_repair_agent_{self.session_id}.log"

        self.logger = logging.getLogger(f"test_gen_repair_agent.{self.session_id}")
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

        self.logger.info("Test Generation & Repair Agent initialized")

    async def analyze(self, prompt_generator, analysis_results, agent_name=None, sub_agent_name=None):
        """
        Generate tests and repair code based on analysis from other agents.

        Args:
            prompt_generator: The prompt generator to use
            analysis_results (dict): Results from all analysis agents
            agent_name (str, optional): Name of the parent agent
            sub_agent_name (str, optional): Name of this sub-agent

        Returns:
            dict: Test generation and repair results
        """
        self.logger.info("Generating tests and repairs based on analysis results")

        semantic_analyzer_analyses = {}
        for analysis_type, analysis_result in analysis_results.items():
            # # only allow certain analysis types
            # if analysis_type not in ["io"]:
            #     continue
            semantic_analyzer_analyses[analysis_type] = analysis_result["parsed_final_response"]

        # Generate the prompt using the template for test_gen_repair_agent
        prompt = prompt_generator.generate_prompt("test_gen_repair_agent")

        # Add analysis results to the prompt
        prompt += "\n\n<semantic_analysis_results>\n"
        prompt += json.dumps(semantic_analyzer_analyses, indent=2)
        prompt += "\n</semantic_analysis_results>"

        # Log the full prompt
        self.logger.debug("Generated test generation and repair prompt:")
        self.logger.debug(prompt)

        self.conversation.add_message(role="user", content=prompt)

        try:
            # Use the dedicated utility function for command execution with 1000 seconds timeout
            from src.utils.cmd_utils import run_claude_command

            # Set 1000 seconds timeout
            try:
                # Create a task for the Claude CLI call
                api_task = asyncio.create_task(
                    run_claude_command(
                        prompt,
                        "",
                        self.configs,
                        self.logger,
                        agent_name=agent_name or "test_gen_repair_agent",
                        sub_agent_name=sub_agent_name,
                    )
                )

                # Wait for the task to complete with a timeout of 1000 seconds
                status, agent_output = await asyncio.wait_for(api_task, timeout=1000)

            except asyncio.TimeoutError:
                self.logger.warning(
                    "Test generation timed out after 1000 seconds, returning is_equivalent=error with explanation"
                )
                # Cancel the task to ensure proper cleanup
                if not api_task.done():
                    api_task.cancel()
                    try:
                        # Give it a moment to clean up
                        await asyncio.wait_for(api_task, timeout=1.0)
                    except (asyncio.TimeoutError, asyncio.CancelledError):
                        pass

                # Create default success response on timeout
                status = True
                agent_output = {"result": f"<final_response_format>{json.dumps(self.errors['timeout'])}</final_response_format>"}

            agent_output = agent_output or {}

            if status:
                self.logger.info("Test generation and repair completed successfully")
                # Extract the final response format
                result = agent_output.get("result", "")
                self.logger.debug("Raw response from model:")
                self.logger.debug(result)

                pattern = r"<final_response_format>(.*?)</final_response_format>"
                match = re.search(pattern, result, re.DOTALL)

                if match:
                    try:
                        test_repair_results = json.loads(match.group(1), strict=False)
                        self.logger.info(f"Generated test cases and repairs")
                        agent_output["parsed_final_response"] = test_repair_results
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
