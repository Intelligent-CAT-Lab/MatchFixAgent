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
from src.utils.credential_utils import get_agent_credentials

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
    def _organize_logs(self) -> None:
        """
        Move all log files to a directory with the same naming pattern as the log files.
        This should be called after the verdict agent completes its analysis.
        """
        # Define log file paths
        log_dir = Path(f"logs/match_agent")

        # Extract components from session_id
        if "." in self.session_id and len(self.session_id.split(".")) >= 5:
            parts = self.session_id.split(".")
            tool_name, project_name, source_lang, target_lang, fragment_id = parts[:5]

            # Create a directory with the same naming pattern
            target_dir = log_dir / f"{tool_name}.{project_name}.{source_lang}.{target_lang}.{fragment_id}"
            target_dir.mkdir(exist_ok=True)

            # Dictionary to track all agent types and their log files
            agent_logs = {}
            agent_types = ["match_agent"] + self.sub_agents

            # First, handle the main match_agent log file
            for log_file in log_dir.glob("match_agent_*-*-*-*-*.log"):
                # Create the new name for the match_agent log
                new_name = f"match_agent.{project_name}.{source_lang}.{target_lang}.{fragment_id}.log"
                agent_logs["match_agent"] = (log_file, target_dir / new_name)
                self.logger.info(f"Will move main log file {log_file} to {target_dir / new_name}")

            # Now find all subagent log files with UUID pattern
            for agent_type in self.sub_agents:
                # Look for UUID-style log files
                for log_file in log_dir.glob(f"{agent_type}_*-*-*-*-*.log"):
                    new_name = f"{agent_type}.{project_name}.{source_lang}.{target_lang}.{fragment_id}.log"
                    agent_logs[agent_type] = (log_file, target_dir / new_name)
                    self.logger.info(f"Will move subagent log file {log_file} to {target_dir / new_name}")

            # Now perform the actual file operations
            # First close all logger handlers
            for handler in self.logger.handlers[:]:
                handler.close()
                self.logger.removeHandler(handler)

            # Close all subagent logger handlers if they have them
            # This is important to ensure all log data is flushed to disk before moving files
            subagent_map = {
                self.control_flow_agent: "control_flow_agent",
                self.data_flow_agent: "data_flow_agent",
                self.io_agent: "io_agent",
                self.library_equivalence_agent: "library_equivalence_agent",
                self.exception_error_agent: "exception_error_agent",
                self.spec_agent: "spec_agent",
                self.test_gen_repair_agent: "test_gen_repair_agent",
                self.verdict_agent: "verdict_agent",
            }

            for subagent, agent_type in subagent_map.items():
                if hasattr(subagent, "logger") and subagent.logger and subagent.logger.handlers:
                    for handler in subagent.logger.handlers[:]:
                        handler.close()
                        subagent.logger.removeHandler(handler)

            # Now move all log files
            for agent_type, (src_file, dst_file) in agent_logs.items():
                if src_file.exists():
                    # Copy and remove original
                    shutil.copy2(src_file, dst_file)
                    src_file.unlink(missing_ok=True)
                    print(f"Moved log file {src_file} to {dst_file}")

            # Finally, move any already-created log files with the new naming pattern
            for log_file in log_dir.glob(f"*.{project_name}.{source_lang}.{target_lang}.{fragment_id}.log"):
                if log_file.parent != target_dir:
                    target_file = target_dir / log_file.name
                    shutil.copy2(log_file, target_file)
                    log_file.unlink(missing_ok=True)
                    print(f"Moved log file {log_file} to {target_file}")

            print(f"Organized all logs into directory: {target_dir}")
            return target_dir

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
            # For sub-agents, the filename includes the agent name using the format: agent_name.project_name.source_lang.target_lang.fragment_id
            # If the old_session_id is in UUID format, use the old pattern
            if "-" in old_session_id and len(old_session_id) > 30:
                original_log_file = log_dir / f"{agent_name}_{old_session_id}.log"
            else:
                # If we're already using the new naming scheme, parse it
                parts = old_session_id.split(".")
                if len(parts) >= 5:
                    # Use the full old_session_id
                    original_log_file = log_dir / f"{old_session_id}.log"
                else:
                    original_log_file = log_dir / f"{agent_name}_{old_session_id}.log"

            # For the new file name, use the new naming scheme: agent_name.project_name.source_lang.target_lang.fragment_id
            parts = new_session_id.split(".")
            if len(parts) >= 5:
                # Extract components from new_session_id
                tool_name, project_name, source_lang, target_lang, fragment_id = parts[:5]
                # Construct sub-agent session ID using the required format
                sub_agent_session_id = f"{agent_name}.{project_name}.{source_lang}.{target_lang}.{fragment_id}"
                new_log_file = log_dir / f"{sub_agent_session_id}.log"
            else:
                new_log_file = log_dir / f"{agent_name}_{new_session_id}.log"

            logger_name = agent_name

        # Only proceed if the original file exists
        if not original_log_file.exists():
            return

        # Ensure parent directory exists
        os.makedirs(new_log_file.parent, exist_ok=True)

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
            # Get the appropriate logger name based on the naming scheme
            if "." in new_session_id and len(new_session_id.split(".")) >= 5:
                # Use the first part (tool_name) as the logger name
                tool_name = new_session_id.split(".")[0]
                new_logger = logging.getLogger(f"{tool_name}.{new_session_id}")
            else:
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
        self.mcp_config = MCPConfig(self.configs["mcp_config_file"])
        self.conversation = Conversation()

        # Generate a temporary UUID that will be replaced with the proper format
        # of tool_name.project_name.source_lang.target_lang.fragment_id
        # This will happen when run() is called with fragment_details
        self.session_id = str(uuid.uuid4())

        # Set up logging
        log_dir = Path(f"logs/match_agent")
        log_dir.mkdir(parents=True, exist_ok=True)

        # Check if session_id already has the proper format (contains dots)
        if "." in self.session_id and len(self.session_id.split(".")) >= 5:
            # Use the proper naming format
            log_file = log_dir / f"match_agent.{'.'.join(self.session_id.split('.')[1:])}.log"
        else:
            # Use the old UUID format
            log_file = log_dir / f"match_agent_{self.session_id}.log"

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

    async def run(self, fragment_details: dict) -> tuple[bool, dict]:
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

        # Update session_id with the new naming scheme based on fragment details
        # Extract required information from fragment_details
        tool_name = self.configs["tool_name"]
        project_name = self.configs["project_name"]
        source_lang = self.configs["source_language"]
        target_lang = self.configs["target_language"]
        fragment_id = fragment_details["id"]

        # Create the new session ID using the desired format
        new_session_id = f"{tool_name}.{project_name}.{source_lang}.{target_lang}.{fragment_id}"
        # Replace any spaces or special chars with underscores for safety
        new_session_id = new_session_id.replace(" ", "_").replace("/", "_").replace("\\", "_")

        # Rename log files from UUID to new naming scheme
        self._rename_log_file(self.session_id, new_session_id, "match_agent")
        self.session_id = new_session_id
        self.logger.info(f"Updated session ID to: {new_session_id}")

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

        # Don't rename the log files for sub-agents yet to ensure proper logging
        # We will handle this in _organize_logs after all processing is done
        # Store the sub-agents for later use
        self.sub_agents = sub_agents

        # Create prompt generator for all agents
        prompt_generator = MatchAgentPromptGenerator(configs=self.configs, fragment_details=fragment_details)

        # Run the 6 semantic analyzer agents in parallel
        self.logger.info("Starting parallel execution of 6 semantic analyzer agents")

        # Update each subagent's log files and session ID
        # Map of subagent instances to their type names
        subagent_map = {
            self.control_flow_agent: "control_flow_agent",
            self.data_flow_agent: "data_flow_agent",
            self.io_agent: "io_agent",
            self.library_equivalence_agent: "library_equivalence_agent",
            self.exception_error_agent: "exception_error_agent",
            self.spec_agent: "spec_agent",
            self.test_gen_repair_agent: "test_gen_repair_agent",
            self.verdict_agent: "verdict_agent",
        }

        # Update each subagent's session_id and rename their log files
        for subagent, agent_type in subagent_map.items():
            # Rename the log file directly rather than using _rename_log_file
            old_log_file = Path(f"logs/match_agent") / f"{agent_type}_{subagent.session_id}.log"

            # Create the new session ID for this subagent using the format: tool_name.project_name.source_lang.target_lang.fragment_id
            subagent_session_id = f"{agent_type}.{project_name}.{source_lang}.{target_lang}.{fragment_id}"
            new_log_file = Path(f"logs/match_agent") / f"{subagent_session_id}.log"

            # Store log file paths for later but don't rename yet
            # This ensures agents continue logging to their original files during execution
            self.logger.info(f"Will rename {old_log_file} to {new_log_file} after execution completes")

            # Update the subagent's session_id
            subagent.session_id = new_session_id

        analysis_tasks = [
            self.control_flow_agent.analyze(
                prompt_generator, agent_name="match_agent", sub_agent_name="control_flow_agent"
            ),
            self.data_flow_agent.analyze(prompt_generator, agent_name="match_agent", sub_agent_name="data_flow_agent"),
            self.io_agent.analyze(prompt_generator, agent_name="match_agent", sub_agent_name="io_agent"),
            self.library_equivalence_agent.analyze(
                prompt_generator, agent_name="match_agent", sub_agent_name="library_equivalence_agent"
            ),
            self.exception_error_agent.analyze(
                prompt_generator, agent_name="match_agent", sub_agent_name="exception_error_agent"
            ),
            self.spec_agent.analyze(prompt_generator, agent_name="match_agent", sub_agent_name="spec_agent"),
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

        # Organize logs into a directory with the same naming pattern as log files
        self._organize_logs()
        self.logger.info(f"Log files have been organized into a directory")

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
            "",
        ],
        "target_function": [
            "    @staticmethod",
            "    def isValueCode(ch: str) -> bool:",
            "        return ch in {'@', ':', '%', '+', '#', '<', '>', '*', '/', '!'}",
        ],
        "ground_truth_target_function": "",
        "source_language": "java",
        "target_language": "python",
        "result": "success",
    }

    status, result = asyncio.run(match_agent.run(fragment_details=fragment_details))

    print("Status:", status)
    print("Result:", json.dumps(result, indent=2))
