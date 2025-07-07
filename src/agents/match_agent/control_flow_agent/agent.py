import os
import json
import logging
import re
import uuid
import tempfile
from pathlib import Path

from src.utils.agent_utils import Model
from src.utils.agent_utils import Conversation
from src.utils.credential_utils import get_agent_credentials
from src.static_analysis.utils import sim_cfg

from src.static_analysis.python.cfg_builder import CFGBuilder as PythonCFGBuilder
from src.static_analysis.rust.cfg_builder import CFGBuilder as RustCFGBuilder
from src.static_analysis.go.cfg_builder import CFGBuilder as GoCFGBuilder
from src.static_analysis.c.cfg_builder import CFGBuilder as CCFGBuilder
from src.static_analysis.java.cfg_builder import CFGBuilder as JavaCFGBuilder


class ControlFlowAgent:
    """
    Agent that analyzes control flow in source and target code fragments.
    Focuses on conditionals, loops, early returns, and control structures.
    """

    def __init__(self, configs: dict, session_id=None) -> None:
        """
        Initialize the control flow agent.

        Args:
            configs (dict): Configuration for the agent
            session_id (str, optional): Session ID for logging. If None, a new UUID will be generated.
        """
        self.configs = configs
        self.conversation = Conversation()
        self.session_id = session_id or str(uuid.uuid4())

        # Set up logging
        log_dir = Path(f"logs/match_agent")
        log_dir.mkdir(parents=True, exist_ok=True)

        log_file = log_dir / f"control_flow_agent_{self.session_id}.log"

        self.logger = logging.getLogger(f"control_flow_agent.{self.session_id}")
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

        self.logger.info("Control Flow Agent initialized")

    def get_cfg_dot_file(self, code, method_name, language):

        try:
            # Generate CFG based on language
            if language.lower() == "java":
                cfg_builder = JavaCFGBuilder()
                cfg = cfg_builder.build_from_src(method_name, code)
                dot_file_path = f"{method_name}_java_cfg.dot"
                cfg.build_visual(dot_file_path, "pdf", calls=False, show=False)
            elif language.lower() == "python":
                cfg_builder = PythonCFGBuilder()
                cfg = cfg_builder.build_from_src(method_name, code)
                dot_file_path = f"{method_name}_python_cfg.dot"
                cfg.build_visual(dot_file_path, "pdf", calls=False, show=False)
            elif language.lower() == "rust":
                cfg_builder = RustCFGBuilder()
                cfg = cfg_builder.build_from_src(method_name, code)
                dot_file_path = f"{method_name}_rust_cfg.dot"
                cfg.build_visual(dot_file_path, "pdf", calls=False, show=False)
            elif language.lower() == "go":
                cfg_builder = GoCFGBuilder()
                cfg = cfg_builder.build_from_src(method_name, code)
                dot_file_path = f"{method_name}_go_cfg.dot"
                cfg.build_visual(dot_file_path, "pdf", calls=False, show=False)
            elif language.lower() == "c":
                cfg_builder = CCFGBuilder()
                cfg = cfg_builder.build_from_src(method_name, code)
                dot_file_path = f"{method_name}_c_cfg.dot"
                cfg.build_visual(dot_file_path, "pdf", calls=False, show=False)
            else:
                return "Unsupported language for CFG generation"

            return dot_file_path

        except Exception as e:
            self.logger.error(f"Error generating CFG for {language}: {str(e)}")
            return None

    async def analyze(self, prompt_generator, agent_name=None, sub_agent_name=None):
        """
        Analyze the control flow of source and target code fragments.

        Args:
            prompt_generator: The prompt generator to use
            agent_name (str, optional): Name of the parent agent
            sub_agent_name (str, optional): Name of this sub-agent

        Returns:
            dict: Analysis results
        """
        self.logger.info("Analyzing control flow equivalence")

        try:

            source_cfg_dot_file = self.get_cfg_dot_file(
                prompt_generator.source_method_implementation,
                "",
                self.configs["source_language"],
            )

            target_cfg_dot_file = self.get_cfg_dot_file(
                prompt_generator.target_method_implementation,
                "",
                self.configs["target_language"],
            )

            similarity = sim_cfg.compute_cfg_similarity(source_cfg_dot_file, target_cfg_dot_file)

            try:
                os.unlink(source_cfg_dot_file)
                os.unlink(source_cfg_dot_file + ".pdf")
                os.unlink(target_cfg_dot_file)
                os.unlink(target_cfg_dot_file + ".pdf")
            except:
                self.logger.warning(f"Failed to delete temporary file: {source_cfg_dot_file}")

            # Calculate similarity using sim_cfg.py

            self.logger.info(f"Computed CFG similarity: {similarity:.4f}")

            # If similarity score is over 0.7, return non-LLM response
            if similarity >= 0.7:
                self.logger.info("CFG similarity is over threshold, returning non-LLM response")
                response = {
                    "parsed_final_response": {
                        "is_equivalent": "yes",
                        "explanation": "non-LLM response",
                        "cfg_similarity_score": similarity,
                    },
                    "result": '<final_response_format>{"is_equivalent": "yes", "explanation": "non-LLM response", "cfg_similarity_score": '
                    + str(similarity)
                    + "}</final_response_format>",
                }
                return response

            else:
                self.logger.info("CFG similarity is below threshold, proceeding with LLM-based analysis")

        except Exception as e:
            self.logger.error(f"Error calculating CFG similarity: {str(e)}")
            # Continue with LLM-based approach if similarity calculation fails

        # If similarity is below threshold or calculation failed, continue with LLM approach
        # Generate the prompt using the template for control_flow_agent
        prompt = prompt_generator.generate_prompt("control_flow_agent")

        # Log the full prompt
        self.logger.debug("Generated control flow analysis prompt:")
        self.logger.debug(prompt)

        self.conversation.add_message(role="user", content=prompt)

        try:
            # Use the direct Claude API instead of CLI
            from src.utils.cmd_utils import prompt_claude

            # Use agent_name and sub_agent_name for credential rotation
            status, agent_output = await prompt_claude(
                prompt,
                "",
                self.configs,
                self.logger,
                agent_name=agent_name or "control_flow_agent",
                sub_agent_name=sub_agent_name,
            )

            agent_output = agent_output or {}

            if status:
                self.logger.info("Control flow analysis completed successfully")
                # Extract the final response format
                result = agent_output.get("result", "")
                self.logger.debug("Raw response from model:")
                self.logger.debug(result)

                pattern = r"<final_response_format>(.*?)</final_response_format>"
                match = re.search(pattern, result, re.DOTALL)

                if match:
                    try:
                        control_flow_analysis = json.loads(match.group(1))
                        self.logger.info(
                            f"Control flow equivalence: {control_flow_analysis.get('is_equivalent', 'unknown')}"
                        )
                        # Return the entire agent_output with the parsed result
                        agent_output["parsed_final_response"] = control_flow_analysis
                        return agent_output
                    except json.JSONDecodeError as e:
                        self.logger.error(f"Failed to parse control flow analysis response as JSON: {e}")
                        agent_output["parsed_final_response"] = {
                            "is_equivalent": "error",
                            "explanation": f"Failed to parse model response as JSON: {str(e)}",
                        }
                        return agent_output
                else:
                    self.logger.error("No final response format found in control flow analysis output")
                    agent_output["parsed_final_response"] = {
                        "is_equivalent": "error",
                        "explanation": "No final response format found in control flow analysis output",
                    }
                    return agent_output
            else:
                self.logger.error("Control flow analysis failed")
                agent_output["parsed_final_response"] = {
                    "is_equivalent": "error",
                    "explanation": "Control flow analysis did not complete successfully",
                }
                return agent_output

        except Exception as e:
            self.logger.error(f"Error in control flow analysis: {str(e)}")
            agent_output["parsed_final_response"] = {
                "is_equivalent": "error",
                "explanation": f"An error occurred during control flow analysis: {str(e)}",
            }
            return agent_output
