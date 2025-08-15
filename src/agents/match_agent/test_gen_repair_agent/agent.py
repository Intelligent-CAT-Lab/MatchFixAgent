import os
import json
import logging
import re
import uuid
import subprocess
import yaml
from pathlib import Path

from src.utils.model_utils import ModelUtils


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
        self.session_id = session_id or str(uuid.uuid4())
        self.errors = yaml.safe_load(open("configs/errors.yaml", "r"))

        # Set up logging
        log_dir = Path(f"logs/{self.configs['agent_name']}")
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

        if self.configs["tool_name"] == "rustrepotrans":
            target_dir = os.path.join(
                "data", "tool_projects", self.configs["tool_name"], "projects", self.configs["project_name"], "rust"
            )
            has_compile_bug = False
            try:
                if self.configs["project_name"] != "incubator-milagro-crypto":
                    proc = subprocess.run(["cargo", "check", "--all"], cwd=target_dir, capture_output=True, text=True)
                else:
                    proc = subprocess.run(
                        ["cargo", "check", "--all", "--all-features", "--release"],
                        cwd=target_dir,
                        capture_output=True,
                        text=True,
                    )
                if proc.returncode != 0:
                    has_compile_bug = True
            except Exception as e:
                has_compile_bug = True

            if has_compile_bug:
                self.logger.error(
                    "Compilation error detected in the Rust project. Cannot proceed with test generation."
                )
                return {"parsed_final_response": {"is_equivalent": "no", "explanation": "compilation bug"}}

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

        try:
            # Use the model utility wrapper with extended timeout
            model_utils = ModelUtils(configs=self.configs, logger=self.logger)

            # Call prompt_agent with 1000 seconds timeout
            status, agent_output = await model_utils.prompt_agent(
                prompt=prompt,
                feedback="",
                agent_name=agent_name or "test_gen_repair_agent",
                sub_agent_name=sub_agent_name,
                timeout=1000,  # Set 1000 seconds timeout
            )

            # Handle timeout case - check explicit timeout flag
            if agent_output.get("timeout", False):
                self.logger.warning(
                    "Test generation timed out after 1000 seconds, returning is_equivalent=other with explanation"
                )
                # Create default response for timeout
                agent_output["result"] = (
                    f"<final_response_format>{json.dumps(self.errors['timeout'])}</final_response_format>"
                )

            agent_output = agent_output or {}

            if status:
                self.logger.info("Test generation and repair completed successfully")
                # Extract the final response format - check both last_json and result for backward compatibility
                result = ""
                if "last_json" in agent_output and "result" in agent_output["last_json"]:
                    result = agent_output["last_json"]["result"]
                elif "result" in agent_output:
                    result = agent_output["result"]

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
