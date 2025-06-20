import os
import argparse
import asyncio
import json
import yaml
import re
import logging
import shutil
import uuid
from pathlib import Path
from typing import Dict, List, Any, Optional

from src.utils.agent_utils import MCPConfig
from src.utils.agent_utils import Model
from src.utils.agent_utils import Conversation

from src.agents.match_agent.prompt_generator import MatchAgentPromptGenerator
from src.agents.match_agent.control_flow_agent.agent import ControlFlowAgent
from src.agents.match_agent.data_flow_agent.agent import DataFlowAgent
from src.agents.match_agent.io_agent.agent import IOAgent
from src.agents.match_agent.library_equivalence_agent.agent import LibraryEquivalenceAgent
from src.agents.match_agent.exception_error_agent.agent import ExceptionErrorAgent
from src.agents.match_agent.spec_agent.agent import SpecAgent
from src.agents.match_agent.test_gen_repair_agent.agent import TestGenRepairAgent
from src.agents.match_agent.verdict_agent.agent import VerdictAgent


class MatchAgent:
    def _rename_log_file(self, old_session_id: str, new_session_id: str, agent_name: str) -> None:
        """
        Rename a log file from using old_session_id to new_session_id in the filename.

        Args:
            old_session_id (str): The original session ID in the filename
            new_session_id (str): The new session ID to use in the filename
            agent_name (str): Name of the agent (used in filename and logger name)
        """
        # Skip if session IDs are the same
        if old_session_id == new_session_id:
            return

        # Define log file paths
        log_dir = Path(f"logs/match_agent")

        # For match_agent itself, the filename is just the session ID
        if agent_name == "match_agent":
            original_log_file = log_dir / f"{old_session_id}.log"
            new_log_file = log_dir / f"{new_session_id}.log"
            logger_name = f"match_agent"
        else:
            # For sub-agents, the filename includes the agent name
            original_log_file = log_dir / f"{agent_name}_{old_session_id}.log"
            new_log_file = log_dir / f"{agent_name}_{new_session_id}.log"
            logger_name = agent_name

        # Only proceed if the original file exists
        if not original_log_file.exists():
            return

        # For match_agent, close its logger handlers first
        if agent_name == "match_agent":
            logger = logging.getLogger(f"{logger_name}.{old_session_id}")
            for handler in logger.handlers[:]:
                handler.close()
                logger.removeHandler(handler)

        # Use shutil.copy2 and then remove the original instead of rename
        # This avoids issues if the files are on different filesystems
        shutil.copy2(original_log_file, new_log_file)
        original_log_file.unlink(missing_ok=True)

        # Create a new logger with the new session ID for match_agent only
        # We don't need to recreate loggers for sub-agents as they're finished executing
        if agent_name == "match_agent":
            new_logger = logging.getLogger(f"{logger_name}.{new_session_id}")
            new_logger.setLevel(logging.INFO)
            new_logger.propagate = False

            # Add handlers to the new logger
            file_handler = logging.FileHandler(new_log_file)
            file_handler.setLevel(logging.DEBUG)
            console_handler = logging.StreamHandler()
            console_handler.setLevel(logging.INFO)
            formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
            file_handler.setFormatter(formatter)
            console_handler.setFormatter(formatter)
            new_logger.addHandler(file_handler)
            new_logger.addHandler(console_handler)

            # Log the file rename operation
            new_logger.info(f"Log file renamed from {original_log_file} to {new_log_file}")

    """
    Orchestrates multiple semantic analyzer agents to analyze code equivalence.
    Follows the architecture in overview.jpg with 6 parallel semantic analyzer agents,
    followed by test generator & repair agent, and verdict agent.
    """

    def __init__(self, configs: dict) -> None:
        """
        Initialize the match agent with configuration and logging.

        Args:
            configs (dict): Configuration settings
        """
        self.configs = configs
        self.model = Model(self.configs["model"])
        self.mcp_config = MCPConfig(self.configs["mcp_config_file"])
        self.conversation = Conversation()
        self.session_id = str(uuid.uuid4())

        # Set up logging
        log_dir = Path(f"logs/match_agent")
        log_dir.mkdir(parents=True, exist_ok=True)

        log_file = log_dir / f"{self.session_id}.log"

        self.logger = logging.getLogger(f"match_agent.{self.session_id}")
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

        self.logger.info(f"match_agent initialized with session ID: {self.session_id}")
        self.logger.info(f"Using model: {self.model.model_name}")

        # Initialize sub-agents with the same session ID and specialized configurations
        subagent_configs = {}
        for agent_name, agent_config in self.configs.get("sub_agents", {}).items():
            # Create a copy of the base configs
            agent_specific_config = dict(self.configs)
            # Update with sub-agent specific configuration
            agent_specific_config.update(agent_config)
            subagent_configs[agent_name] = agent_specific_config

        # Initialize all sub-agents with their configs
        self.control_flow_agent = ControlFlowAgent(
            subagent_configs.get("control_flow_agent", self.configs), self.session_id
        )
        self.data_flow_agent = DataFlowAgent(subagent_configs.get("data_flow_agent", self.configs), self.session_id)
        self.io_agent = IOAgent(subagent_configs.get("io_agent", self.configs), self.session_id)
        self.library_equivalence_agent = LibraryEquivalenceAgent(
            subagent_configs.get("library_equivalence_agent", self.configs), self.session_id
        )
        self.exception_error_agent = ExceptionErrorAgent(
            subagent_configs.get("exception_error_agent", self.configs), self.session_id
        )
        self.spec_agent = SpecAgent(subagent_configs.get("spec_agent", self.configs), self.session_id)
        self.test_gen_repair_agent = TestGenRepairAgent(
            subagent_configs.get("test_gen_repair_agent", self.configs), self.session_id
        )
        self.verdict_agent = VerdictAgent(subagent_configs.get("verdict_agent", self.configs), self.session_id)

    # MatchAgent is now a pure orchestrator without command execution functionality

    async def run(
        self,
        fragment_details: dict
    ) -> tuple[bool, dict]:
        """
        Run the match agent to analyze code equivalence.

        Orchestrates the execution of multiple semantic analyzer agents to analyze different aspects
        of code equivalence between source and target implementations.

        Args:
            fragment_details (dict): Details of the method to analyze

        Returns:
            tuple[bool, dict]: (success_status, results)
        """
        self.logger.info(f"Starting match agent analysis for {fragment_details}")

        # Create prompt generator for all agents
        prompt_generator = MatchAgentPromptGenerator(
            configs=self.configs,
            fragment_details=fragment_details
        )

        # Run the 6 semantic analyzer agents in parallel
        self.logger.info("Starting parallel execution of 6 semantic analyzer agents")

        analysis_tasks = [
            self.control_flow_agent.analyze(
                prompt_generator, agent_name="match_agent", sub_agent_name="control_flow_agent"
            ),
            self.data_flow_agent.analyze(
                prompt_generator, agent_name="match_agent", sub_agent_name="data_flow_agent"
            ),
            self.io_agent.analyze(prompt_generator, agent_name="match_agent", sub_agent_name="io_agent"),
            self.library_equivalence_agent.analyze(
                prompt_generator, agent_name="match_agent", sub_agent_name="library_equivalence_agent"
            ),
            self.exception_error_agent.analyze(
                prompt_generator, agent_name="match_agent", sub_agent_name="exception_error_agent"
            ),
            self.spec_agent.analyze(
                prompt_generator, agent_name="match_agent", sub_agent_name="spec_agent"
            ),
        ]

        semantic_analyzer_results = await asyncio.gather(*analysis_tasks)

        all_analysis_results = {
            "control_flow": semantic_analyzer_results[0],
            "data_flow": semantic_analyzer_results[1],
            "io": semantic_analyzer_results[2],
            "library_equivalence": semantic_analyzer_results[3],
            "exception_error": semantic_analyzer_results[4],
            "spec": semantic_analyzer_results[5],
        }

        self.logger.info("All semantic analyzer agent analyses completed")

        # Run the test generation and repair agent
        self.logger.info("Starting test generation and repair agent")
        test_repair_results = await self.test_gen_repair_agent.analyze(
            prompt_generator,
            all_analysis_results,
            agent_name="match_agent",
            sub_agent_name="test_gen_repair_agent",
        )

        # Combine all results
        all_results = {"semantic_analyzer_analyses": all_analysis_results, "test_repair": test_repair_results}

        # Run the verdict agent for final decision
        self.logger.info("Starting verdict agent for final decision")
        verdict_results = await self.verdict_agent.analyze(
            prompt_generator, all_results, agent_name="match_agent", sub_agent_name="verdict_agent"
        )

        # Add verdict to final results
        all_results["verdict"] = verdict_results

        # Determine overall success status
        success = False
        try:
            parsed_response = verdict_results.get("parsed_final_response", {})
            is_equivalent = parsed_response.get("is_equivalent")
            success = is_equivalent is not None and is_equivalent != "error"
            self.logger.debug(f"Verdict parsed_final_response: {parsed_response}")
        except Exception as e:
            self.logger.error(f"Error parsing verdict results: {str(e)}")

        self.logger.info(f"Match agent analysis completed with success={success}")

        if success:
            # Get the final session ID from verdict results
            final_session_id = verdict_results.get("session_id", self.session_id)

            # Rename match_agent log file
            self._rename_log_file(self.session_id, final_session_id, "match_agent")

            # List of all sub-agents
            sub_agents = [
                "control_flow_agent",
                "data_flow_agent",
                "io_agent",
                "library_equivalence_agent",
                "exception_error_agent",
                "spec_agent",
                "test_gen_repair_agent",
                "verdict_agent",
            ]

            # Rename log files for all sub-agents
            for sub_agent in sub_agents:
                self._rename_log_file(self.session_id, final_session_id, sub_agent)

        return success, all_results


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="MatchAgent")
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

    logger = logging.getLogger(f"match_agent_main")
    logger.info(f"Starting match agent with config file: {args.config_file}")

    configs = yaml.safe_load(open(args.config_file, "r"))

    match_agent = MatchAgent(configs=configs)

    ### sample test case
    logger.info("Running sample test case")

    fragment_details = {
        "project": "commons-cli",
        "source_path": "commons-cli/src/main/java/org/apache/commons/cli/PatternOptionBuilder.java",
        "target_path": "commons-cli/src/main/org/apache/commons/cli/PatternOptionBuilder.py",
        "source_function": [
            "    public static boolean isValueCode(final char ch) {",
            "        return ch == '@' || ch == ':' || ch == '%' || ch == '+' || ch == '#' || ch == '<'",
            "                || ch == '>' || ch == '*' || ch == '/' || ch == '!';",
            "    }",
            ""
        ],
        "target_function": [
            "    @staticmethod",
            "    def isValueCode(ch: str) -> bool:",
            "        return ch in {'@', ':', '%', '+', '#', '<', '>', '*', '/', '!'}"
        ],
        "ground_truth_target_function": "",
        "source_language": "java",
        "target_language": "python",
        "result": "success"
    }

    status, result = asyncio.run(
        match_agent.run(fragment_details=fragment_details)
    )

    print("Status:", status)
    print("Result:", json.dumps(result, indent=2))
