import os
import json
import logging
import re
import uuid
import tempfile
import yaml
from pathlib import Path

from src.utils.agent_utils import Model
from src.utils.agent_utils import Conversation
from src.utils.credential_utils import get_agent_credentials
from src.static_analysis.utils import sim_dfg

from src.static_analysis.python.cfg_builder import CFGBuilder as PythonCFGBuilder
from src.static_analysis.rust.cfg_builder import CFGBuilder as RustCFGBuilder
from src.static_analysis.go.cfg_builder import CFGBuilder as GoCFGBuilder
from src.static_analysis.c.cfg_builder import CFGBuilder as CCFGBuilder
from src.static_analysis.java.cfg_builder import CFGBuilder as JavaCFGBuilder
from src.static_analysis.javascript.cfg_builder import CFGBuilder as JavaScriptCFGBuilder


class DataFlowAgent:
    """
    Agent that analyzes data flow in source and target code fragments.
    Focuses on variable definitions, data transformations, and state changes.
    """

    def __init__(self, configs: dict, session_id=None) -> None:
        """
        Initialize the data flow agent.
        
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
                # Use the proper naming format: data_flow_agent.project_name.source_lang.target_lang.fragment_id
                project_name, source_lang, target_lang, fragment_id = parts[1:5]
                log_file = log_dir / f"data_flow_agent.{project_name}.{source_lang}.{target_lang}.{fragment_id}.log"
            else:
                log_file = log_dir / f"data_flow_agent.{'.'.join(self.session_id.split('.')[1:])}.log"
        else:
            # Use the old UUID format
            log_file = log_dir / f"data_flow_agent_{self.session_id}.log"

        self.logger = logging.getLogger(f"data_flow_agent.{self.session_id}")
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

        self.logger.info("Data Flow Agent initialized")

    def get_cfg_dot_file(self, code, method_name, language):
        try:
            # Generate DFG based on language
            if language.lower() == "java":
                cfg_builder = JavaCFGBuilder()
                cfg = cfg_builder.build_from_src(method_name, code)
                unique_id = str(uuid.uuid4().hex[:8])
                dot_file_path = os.path.join(tempfile.gettempdir(), f"{method_name}_java_dfg_{unique_id}_{self.session_id}.dot")
                cfg.build_visual(dot_file_path, "pdf", calls=False, show=False)
            elif language.lower() == "python":
                cfg_builder = PythonCFGBuilder()
                cfg = cfg_builder.build_from_src(method_name, code)
                unique_id = str(uuid.uuid4().hex[:8])
                dot_file_path = os.path.join(tempfile.gettempdir(), f"{method_name}_python_dfg_{unique_id}_{self.session_id}.dot")
                cfg.build_visual(dot_file_path, "pdf", calls=False, show=False)
            elif language.lower() == "rust":
                cfg_builder = RustCFGBuilder()
                cfg = cfg_builder.build_from_src(method_name, code)
                unique_id = str(uuid.uuid4().hex[:8])
                dot_file_path = os.path.join(tempfile.gettempdir(), f"{method_name}_rust_dfg_{unique_id}_{self.session_id}.dot")
                cfg.build_visual(dot_file_path, "pdf", calls=False, show=False)
            elif language.lower() == "go":
                cfg_builder = GoCFGBuilder()
                cfg = cfg_builder.build_from_src(method_name, code)
                unique_id = str(uuid.uuid4().hex[:8])
                dot_file_path = os.path.join(tempfile.gettempdir(), f"{method_name}_go_dfg_{unique_id}_{self.session_id}.dot")
                cfg.build_visual(dot_file_path, "pdf", calls=False, show=False)
            elif language.lower() == "c":
                cfg_builder = CCFGBuilder()
                cfg = cfg_builder.build_from_src(method_name, code)
                unique_id = str(uuid.uuid4().hex[:8])
                dot_file_path = os.path.join(tempfile.gettempdir(), f"{method_name}_c_dfg_{unique_id}_{self.session_id}.dot")
                cfg.build_visual(dot_file_path, "pdf", calls=False, show=False)
            elif language.lower() == "javascript":
                cfg_builder = JavaScriptCFGBuilder()
                cfg = cfg_builder.build_from_src(method_name, code)
                unique_id = str(uuid.uuid4().hex[:8])
                dot_file_path = os.path.join(tempfile.gettempdir(), f"{method_name}_javascript_dfg_{unique_id}_{self.session_id}.dot")
                cfg.build_visual(dot_file_path, "pdf", calls=False, show=False)
            else:
                return "Unsupported language for DFG generation"

            return dot_file_path

        except Exception as e:
            self.logger.error(f"Error generating DFG for {language}: {str(e)}")
            return None
                
    async def analyze(self, prompt_generator, agent_name=None, sub_agent_name=None):
        """
        Analyze the data flow of source and target code fragments.
        
        Args:
            prompt_generator: The prompt generator to use
            agent_name (str, optional): Name of the parent agent
            sub_agent_name (str, optional): Name of this sub-agent
            
        Returns:
            dict: Analysis results
        """
        self.logger.info("Analyzing data flow equivalence")

        try:
            # Generate DFG dot files
            source_code = prompt_generator.source_method_implementation
            target_code = prompt_generator.target_method_implementation
            source_language = self.configs["source_language"]
            target_language = self.configs["target_language"]
            
            # Generate the DFG dot files
            source_cfg_dot_file = self.get_cfg_dot_file(
                source_code,
                "",
                source_language
            )
            
            target_cfg_dot_file = self.get_cfg_dot_file(
                target_code,
                "",
                target_language
            )
                        
            # Create temporary files for the source code to pass to sim_dfg
            with tempfile.NamedTemporaryFile(mode="w", suffix=f".{source_language}", delete=False) as temp_source_file:
                temp_source_file.write(source_code)
                source_code_path = temp_source_file.name
                
            with tempfile.NamedTemporaryFile(mode="w", suffix=f".{target_language}", delete=False) as temp_target_file:
                temp_target_file.write(target_code)
                target_code_path = temp_target_file.name
            
            # Calculate similarity using sim_dfg.py
            similarity = sim_dfg.compute_variable_cfg_similarity_from_files(
                source_cfg_dot_file, source_code_path, source_language,
                target_cfg_dot_file, target_code_path, target_language
            )
            # Clean up the dot files
            try:
                os.unlink(source_cfg_dot_file)
                os.unlink(source_cfg_dot_file + ".pdf")
                os.unlink(target_cfg_dot_file)
                os.unlink(target_cfg_dot_file + ".pdf")
            except Exception as e:
                self.logger.warning(f"Failed to delete temporary DFG files: {str(e)}")
            
            # Clean up the temporary source code files
            try:
                os.unlink(source_code_path)
                os.unlink(target_code_path)
            except Exception as e:
                self.logger.warning(f"Failed to delete temporary code files: {str(e)}")
                
            # Log the similarity score
            self.logger.info(f"Computed DFG similarity: {similarity:.4f}")
            
            # If similarity score is over 0.7, return non-LLM response
            if similarity >= 0.7:
                self.logger.info("DFG similarity is over threshold, returning non-LLM response")
                response = {
                    "parsed_final_response": {
                        "is_equivalent": "yes",
                        "explanation": "non-LLM response",
                        "dfg_similarity_score": similarity
                    },
                    "result": "<final_response_format>{\"is_equivalent\": \"yes\", \"explanation\": \"non-LLM response\", \"dfg_similarity_score\": " + str(similarity) + "}</final_response_format>"
                }
                return response
            
            else:
                self.logger.info("DFG similarity is below threshold, proceeding with LLM-based analysis")
                
        except Exception as e:
            self.logger.error(f"Error calculating DFG similarity: {str(e)}")
            # Continue with LLM-based approach if similarity calculation fails

        # If similarity is below threshold or calculation failed, continue with LLM approach
        # Generate the prompt using the template for data_flow_agent
        prompt = prompt_generator.generate_prompt("data_flow_agent")
        
        # Log the full prompt
        self.logger.debug("Generated data flow analysis prompt:")
        self.logger.debug(prompt)
        
        self.conversation.add_message(role="user", content=prompt)
        
        try:
            # Use the direct Claude API instead of CLI
            from src.utils.cmd_utils import prompt_claude
            status, agent_output = await prompt_claude(
                prompt, "", self.configs, self.logger,
                agent_name=agent_name or "data_flow_agent", 
                sub_agent_name=sub_agent_name
            )

            agent_output = agent_output or {}
            
            if status:
                self.logger.info("Data flow analysis completed successfully")
                # Extract the final response format
                result = agent_output.get("result", "")
                self.logger.debug("Raw response from model:")
                self.logger.debug(result)
                
                pattern = r"<final_response_format>(.*?)</final_response_format>"
                match = re.search(pattern, result, re.DOTALL)
                
                if match:
                    try:
                        data_flow_analysis = json.loads(match.group(1), strict=False)
                        self.logger.info(f"Data flow equivalence: {data_flow_analysis.get('is_equivalent', 'unknown')}")
                        # Return the entire agent_output with the parsed result
                        agent_output["parsed_final_response"] = data_flow_analysis
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