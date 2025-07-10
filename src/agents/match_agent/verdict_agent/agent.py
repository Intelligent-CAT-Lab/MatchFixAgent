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


class VerdictAgent:
    """
    Final verdict agent that synthesizes analyses from multiple semantic analyzer agents.
    Provides a holistic assessment of functional equivalence between code fragments.
    """

    def __init__(self, configs: dict, session_id=None) -> None:
        """
        Initialize the verdict agent.

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

        log_file = log_dir / f"verdict_agent_{self.session_id}.log"

        self.logger = logging.getLogger(f"verdict_agent.{self.session_id}")
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

        self.logger.info("Verdict Agent initialized")

    async def analyze(self, prompt_generator, all_results, agent_name=None, sub_agent_name=None):
        """
        Synthesize analyses from all agents to provide a final verdict.

        Args:
            prompt_generator: The prompt generator to use
            all_results (dict): Results from all agents including test/repair agent
            agent_name (str, optional): Name of the parent agent
            sub_agent_name (str, optional): Name of this sub-agent

        Returns:
            dict: Final verdict on functional equivalence
        """
        self.logger.info("Producing final verdict on functional equivalence")

        semantic_analyzer_analyses = {"semantic_analyzer_analyses": {}, "test_repair_analyses": {}}
        for analysis_type, analysis_result in all_results["semantic_analyzer_analyses"].items():
            semantic_analyzer_analyses["semantic_analyzer_analyses"][analysis_type] = analysis_result[
                "parsed_final_response"
            ]

        semantic_analyzer_analyses["test_repair_analyses"] = all_results["test_repair"]["parsed_final_response"]

        # Generate the prompt using the template for verdict_agent
        prompt = prompt_generator.generate_prompt("verdict_agent")

        # Add all analysis results to the prompt
        prompt += "\n\n<all_analysis_results>\n"
        prompt += json.dumps(semantic_analyzer_analyses, indent=2)
        prompt += "\n</all_analysis_results>"

        # Log the full prompt
        self.logger.debug("Generated verdict prompt:")
        self.logger.debug(prompt)

        self.conversation.add_message(role="user", content=prompt)

        try:
            # Use the dedicated utility function for command execution
            from src.utils.cmd_utils import run_claude_command

            # Set 300 seconds timeout
            try:
                # Create a task for the Claude CLI call
                api_task = asyncio.create_task(
                    run_claude_command(
                        prompt,
                        "",
                        self.configs,
                        self.logger,
                        agent_name=agent_name or "verdict_agent",
                        sub_agent_name=sub_agent_name,
                    )
                )

                # Wait for the task to complete with a timeout of 300 seconds
                status, agent_output = await asyncio.wait_for(api_task, timeout=300)

            except asyncio.TimeoutError:
                self.logger.warning(
                    "Verdict agent timed out after 300 seconds, returning is_equivalent=error with explanation"
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
                agent_output = {
                    "result": f'<final_response_format>{json.dumps(self.errors["timeout"])}</final_response_format>'
                }

            agent_output = agent_output or {}

            if status:
                self.logger.info("Verdict analysis completed successfully")
                # Extract the final response format
                result = agent_output.get("result", "")
                self.logger.debug("Raw response from model:")
                self.logger.debug(result)

                pattern = r"<final_response_format>(.*?)</final_response_format>"
                match = re.search(pattern, result, re.DOTALL)

                if match:
                    try:
                        verdict_analysis = json.loads(match.group(1), strict=False)
                        self.logger.info(
                            f"Final verdict on functional equivalence: {verdict_analysis.get('is_equivalent', 'other')}"
                        )
                        self.logger.info(f"Confidence level: {verdict_analysis.get('confidence_level', 'other')}")
                        agent_output["parsed_final_response"] = verdict_analysis
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
