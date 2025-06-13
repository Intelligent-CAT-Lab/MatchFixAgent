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
from typing import Dict, List, Any

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
    """
    Orchestrates multiple specialized agents to analyze code equivalence.
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

        # Initialize sub-agents with the same session ID
        self.control_flow_agent = ControlFlowAgent(configs, self.session_id)
        self.data_flow_agent = DataFlowAgent(configs, self.session_id)
        self.io_agent = IOAgent(configs, self.session_id)
        self.library_equivalence_agent = LibraryEquivalenceAgent(configs, self.session_id)
        self.exception_error_agent = ExceptionErrorAgent(configs, self.session_id)
        self.spec_agent = SpecAgent(configs, self.session_id)
        self.test_gen_repair_agent = TestGenRepairAgent(configs, self.session_id)
        self.verdict_agent = VerdictAgent(configs, self.session_id)

    # MatchAgent is now a pure orchestrator without command execution functionality

    async def run(
        self,
        source_schema_name: str,
        target_schema_name: str,
        class_name: str,
        method_name: str,
        method_pair: dict,
    ) -> tuple[bool, dict]:
        """
        Run the match agent to analyze code equivalence.

        Orchestrates the execution of multiple specialized agents to analyze different aspects
        of code equivalence between source and target implementations.

        Args:
            source_schema_name (str): Name of the source schema
            target_schema_name (str): Name of the target schema
            class_name (str): Name of the class containing the method
            method_name (str): Name of the method to validate
            method_pair (dict): Dictionary containing source and target code

        Returns:
            tuple[bool, dict]: (success_status, results)
        """
        self.logger.info(f"Starting match agent analysis for {class_name}.{method_name}")

        # Create prompt generator for all agents
        prompt_generator = MatchAgentPromptGenerator(
            configs=self.configs,
            source_schema_name=source_schema_name,
            target_schema_name=target_schema_name,
            class_name=class_name,
            method_name=method_name,
            method_pair=method_pair,
        )

        # Run the 6 specialized agents in parallel
        self.logger.info("Starting parallel execution of 6 specialized agents")

        analysis_tasks = [
            self.control_flow_agent.analyze(prompt_generator, method_pair),
            self.data_flow_agent.analyze(prompt_generator, method_pair),
            self.io_agent.analyze(prompt_generator, method_pair),
            self.library_equivalence_agent.analyze(prompt_generator, method_pair),
            self.exception_error_agent.analyze(prompt_generator, method_pair),
            self.spec_agent.analyze(prompt_generator, method_pair),
        ]

        specialized_results = await asyncio.gather(*analysis_tasks)

        all_analysis_results = {
            "control_flow": specialized_results[0],
            "data_flow": specialized_results[1],
            "io": specialized_results[2],
            "library_equivalence": specialized_results[3],
            "exception_error": specialized_results[4],
            "spec": specialized_results[5],
        }

        self.logger.info("All specialized agent analyses completed")

        # Run the test generation and repair agent
        # self.logger.info("Starting test generation and repair agent")
        # test_repair_results = await self.test_gen_repair_agent.analyze(
        #     prompt_generator, method_pair, all_analysis_results
        # )

        # Combine all results
        all_results = {
            "specialized_analyses": all_analysis_results,
            # "test_repair": test_repair_results
        }

        # Run the verdict agent for final decision
        self.logger.info("Starting verdict agent for final decision")
        verdict_results = await self.verdict_agent.analyze(prompt_generator, method_pair, all_results)

        # Add verdict to final results
        all_results["verdict"] = verdict_results

        # Determine overall success status
        success = verdict_results["parsed_final_response"]["is_equivalent"] != "error"

        self.logger.info(f"Match agent analysis completed with success={success}")

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

    source_schema_name = "commons-cli.src.main.java.org.apache.commons.cli.PatternOptionBuilder"
    target_schema_name = "commons-cli.src.main.org.apache.commons.cli.PatternOptionBuilder"
    class_name = "PatternOptionBuilder"
    method_name = "135-138:isValueCode"
    method_pair = {
        "graal_validation": "success",
        "source_code": [
            "    public static boolean isValueCode(final char ch) {",
            "        return ch == '@' || ch == ':' || ch == '%' || ch == '+' || ch == '#' || ch == '<'",
            "                || ch == '>' || ch == '*' || ch == '/' || ch == '!';",
            "    }",
            "",
        ],
        "target_code": [
            "    @staticmethod",
            "    def isValueCode(ch: str) -> bool:",
            "        return ch in {'@', ':', '%', '+', '#', '<', '>', '*', '/', '!'}",
        ],
    }

    status, result = asyncio.run(
        match_agent.run(source_schema_name, target_schema_name, class_name, method_name, method_pair)
    )

    print("Status:", status)
    print("Result:", json.dumps(result, indent=2))
