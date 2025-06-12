import os
import json
import logging
import re
import uuid
from pathlib import Path

from src.utils.agent_utils import Model
from src.utils.agent_utils import Conversation


class VerdictAgent:
    """
    Final verdict agent that synthesizes analyses from multiple specialized agents.
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
        self.model = Model(self.configs["model"])
        self.conversation = Conversation()
        self.session_id = session_id or str(uuid.uuid4())

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

    async def analyze(self, prompt_generator, method_pair, all_results):
        """
        Synthesize analyses from all agents to provide a final verdict.

        Args:
            prompt_generator: The prompt generator to use
            method_pair (dict): The method pair to analyze
            all_results (dict): Results from all agents including test/repair agent

        Returns:
            dict: Final verdict on functional equivalence
        """
        self.logger.info("Producing final verdict on functional equivalence")

        # Generate the prompt using the template for verdict_agent
        prompt = prompt_generator.generate_prompt("verdict_agent")

        # Add all analysis results to the prompt
        prompt += "\n\n<all_analysis_results>\n"
        prompt += json.dumps(all_results, indent=2)
        prompt += "\n</all_analysis_results>"

        # Log the full prompt
        self.logger.debug("Generated verdict prompt:")
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
                prompt, "", self.model.model_name, self.configs, self.logger
            )

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
                        verdict_analysis = json.loads(match.group(1))
                        self.logger.info(
                            f"Final verdict on functional equivalence: {verdict_analysis.get('is_functionally_equivalent', 'unknown')}"
                        )
                        self.logger.info(f"Confidence level: {verdict_analysis.get('confidence_level', 'unknown')}")
                        # Return the entire agent_output with the parsed result
                        agent_output["parsed_final_response"] = verdict_analysis
                        return agent_output
                    except json.JSONDecodeError as e:
                        self.logger.error(f"Failed to parse verdict analysis response as JSON: {e}")
                        agent_output["error"] = f"Failed to parse response: {e}"
                        agent_output["parsed_final_response"] = {
                            "is_functionally_equivalent": "error",
                            "explanation": f"Failed to parse response: {e}",
                        }
                        return agent_output
                else:
                    self.logger.error("No final response format found in verdict analysis output")
                    agent_output["error"] = "No final response format found"
                    agent_output["parsed_final_response"] = {
                        "is_functionally_equivalent": "error",
                        "explanation": "No response format found",
                    }
                    return agent_output
            else:
                self.logger.error("Verdict analysis failed")
                return {
                    "error": "Verdict analysis failed",
                    "parsed_final_response": {
                        "is_functionally_equivalent": "error",
                        "explanation": "Analysis execution failed",
                    },
                }

        except Exception as e:
            self.logger.error(f"Error in verdict analysis: {str(e)}")
            return {
                "error": f"Exception: {str(e)}",
                "parsed_final_response": {"is_functionally_equivalent": "error", "explanation": f"Exception: {str(e)}"},
            }
