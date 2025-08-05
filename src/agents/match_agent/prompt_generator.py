import yaml
import os
import tempfile
import subprocess
import uuid
from pathlib import Path
from jinja2 import Template

from src.static_analysis.java.cfg_builder import CFGBuilder as JavaCFGBuilder
from src.static_analysis.python.cfg_builder import CFGBuilder as PythonCFGBuilder
from src.static_analysis.rust.cfg_builder import CFGBuilder as RustCFGBuilder
from src.static_analysis.go.cfg_builder import CFGBuilder as GoCFGBuilder
from src.static_analysis.c.cfg_builder import CFGBuilder as CCFGBuilder
from src.static_analysis.javascript.cfg_builder import CFGBuilder as JavaScriptCFGBuilder


class MatchAgentPromptGenerator:
    """
    Generates prompts for different match agent components based on templates.
    """

    def __init__(self, configs: dict, fragment_details: dict) -> None:
        """
        Initialize the prompt generator.

        Args:
            configs (dict): Configuration settings
            fragment_details (dict): Details of the code fragments to be matched
        """
        self.configs = configs
        self.fragment_details = fragment_details

        self.prompt_templates = yaml.safe_load(open("configs/prompt_templates.yaml", "r"))

        self.format_fragment_details()

    def generate_cfg(self, language: str, code: str, method_name: str) -> str:
        """
        Generate a control flow graph (CFG) visualization for the given code using the external tools.

        Args:
            language (str): The programming language of the code ("java" or "python")
            code (str): The source code to analyze
            method_name (str): The name of the method

        Returns:
            str: A textual representation of the CFG
        """
        # Create a temporary file for the code
        with tempfile.NamedTemporaryFile(mode="w", suffix=f".{language}", delete=False) as temp_file:
            temp_file.write(code)
            code_path = temp_file.name

        try:
            # Generate CFG based on language
            if language.lower() == "java":
                cfg_builder = JavaCFGBuilder()
                cfg = cfg_builder.build_from_file(method_name, code_path)
                unique_id = str(uuid.uuid4().hex[:8])
                dot_file_path = os.path.join(tempfile.gettempdir(), f"{method_name}_java_cfg_{unique_id}")
                cfg.build_visual(dot_file_path, "pdf", calls=False, show=False)
            elif language.lower() == "python":
                cfg_builder = PythonCFGBuilder()
                cfg = cfg_builder.build_from_file(method_name, code_path)
                unique_id = str(uuid.uuid4().hex[:8])
                dot_file_path = os.path.join(tempfile.gettempdir(), f"{method_name}_python_cfg_{unique_id}")
                cfg.build_visual(dot_file_path, "pdf", calls=False, show=False)
            elif language.lower() == "rust":
                cfg_builder = RustCFGBuilder()
                cfg = cfg_builder.build_from_file(method_name, code_path)
                unique_id = str(uuid.uuid4().hex[:8])
                dot_file_path = os.path.join(tempfile.gettempdir(), f"{method_name}_rust_cfg_{unique_id}")
                cfg.build_visual(dot_file_path, "pdf", calls=False, show=False)
            elif language.lower() == "go":
                cfg_builder = GoCFGBuilder()
                cfg = cfg_builder.build_from_file(method_name, code_path)
                unique_id = str(uuid.uuid4().hex[:8])
                dot_file_path = os.path.join(tempfile.gettempdir(), f"{method_name}_go_cfg_{unique_id}")
                cfg.build_visual(dot_file_path, "pdf", calls=False, show=False)
            elif language.lower() == "c":
                cfg_builder = CCFGBuilder()
                cfg = cfg_builder.build_from_file(method_name, code_path)
                unique_id = str(uuid.uuid4().hex[:8])
                dot_file_path = os.path.join(tempfile.gettempdir(), f"{method_name}_c_cfg_{unique_id}")
                cfg.build_visual(dot_file_path, "pdf", calls=False, show=False)
            elif language.lower() == "javascript":
                cfg_builder = JavaScriptCFGBuilder()
                cfg = cfg_builder.build_from_file(method_name, code_path)
                unique_id = str(uuid.uuid4().hex[:8])
                dot_file_path = os.path.join(tempfile.gettempdir(), f"{method_name}_javascript_cfg_{unique_id}")
                cfg.build_visual(dot_file_path, "pdf", calls=False, show=False)
            else:
                return "Unsupported language for CFG generation"

            # Use the print_static_analysis.py script to process the generated graph
            cmd = [
                "python",
                "src/static_analysis/utils/print_static_analysis.py",
                "--dot_file",
                f"{dot_file_path}",
                "--source_file",
                code_path,
                "--language",
                language,
            ]

            # Run the command and capture the stdout
            result = subprocess.run(cmd, capture_output=True, text=True)
            cfg_text = result.stdout

            # Clean up the dot file
            try:
                os.unlink(f"{dot_file_path}")
                os.unlink(f"{dot_file_path}.pdf")
            except:
                pass

            return cfg_text
        finally:
            # Clean up the temporary files
            try:
                os.unlink(code_path)
            except:
                pass

    def generate_dfg(self, language: str, code: str, method_name: str) -> str:
        """
        Generate a data flow graph (DFG) visualization for the given code using the external tools.

        Args:
            language (str): The programming language of the code ("java" or "python")
            code (str): The source code to analyze
            method_name (str): The name of the method

        Returns:
            str: A textual representation of the DFG
        """
        # Create a temporary file for the code
        with tempfile.NamedTemporaryFile(mode="w", suffix=f".{language}", delete=False) as temp_file:
            temp_file.write(code)
            code_path = temp_file.name

        try:
            # Generate CFG based on language
            if language.lower() == "java":
                cfg_builder = JavaCFGBuilder()
                cfg = cfg_builder.build_from_file(method_name, code_path)
                unique_id = str(uuid.uuid4().hex[:8])
                dot_file_path = os.path.join(tempfile.gettempdir(), f"{method_name}_java_dfg_{unique_id}")
                cfg.build_visual(dot_file_path, "pdf", calls=False, show=False)
            elif language.lower() == "python":
                cfg_builder = PythonCFGBuilder()
                cfg = cfg_builder.build_from_file(method_name, code_path)
                unique_id = str(uuid.uuid4().hex[:8])
                dot_file_path = os.path.join(tempfile.gettempdir(), f"{method_name}_python_dfg_{unique_id}")
                cfg.build_visual(dot_file_path, "pdf", calls=False, show=False)
            elif language.lower() == "rust":
                cfg_builder = RustCFGBuilder()
                cfg = cfg_builder.build_from_file(method_name, code_path)
                unique_id = str(uuid.uuid4().hex[:8])
                dot_file_path = os.path.join(tempfile.gettempdir(), f"{method_name}_rust_dfg_{unique_id}")
                cfg.build_visual(dot_file_path, "pdf", calls=False, show=False)
            elif language.lower() == "go":
                cfg_builder = GoCFGBuilder()
                cfg = cfg_builder.build_from_file(method_name, code_path)
                unique_id = str(uuid.uuid4().hex[:8])
                dot_file_path = os.path.join(tempfile.gettempdir(), f"{method_name}_go_dfg_{unique_id}")
                cfg.build_visual(dot_file_path, "pdf", calls=False, show=False)
            elif language.lower() == "c":
                cfg_builder = CCFGBuilder()
                cfg = cfg_builder.build_from_file(method_name, code_path)
                unique_id = str(uuid.uuid4().hex[:8])
                dot_file_path = os.path.join(tempfile.gettempdir(), f"{method_name}_c_dfg_{unique_id}")
                cfg.build_visual(dot_file_path, "pdf", calls=False, show=False)
            elif language.lower() == "javascript":
                cfg_builder = JavaScriptCFGBuilder()
                cfg = cfg_builder.build_from_file(method_name, code_path)
                unique_id = str(uuid.uuid4().hex[:8])
                dot_file_path = os.path.join(tempfile.gettempdir(), f"{method_name}_javascript_dfg_{unique_id}")
                cfg.build_visual(dot_file_path, "pdf", calls=False, show=False)
            else:
                return "Unsupported language for DFG generation"

            # Use the print_static_analysis.py script to process the generated graph and include data flow analysis
            cmd = [
                "python",
                "src/static_analysis/utils/print_static_analysis.py",
                "--dot_file",
                f"{dot_file_path}",
                "--source_file",
                code_path,
                "--language",
                language,
                "--dataflow",  # Enable data flow analysis
            ]

            # Run the command and capture the stdout
            result = subprocess.run(cmd, capture_output=True, text=True)
            dfg_text = result.stdout

            # Clean up the dot file
            try:
                os.unlink(f"{dot_file_path}")
                os.unlink(f"{dot_file_path}.pdf")
            except:
                pass

            return dfg_text
        finally:
            # Clean up the temporary files
            try:
                os.unlink(code_path)
            except:
                pass

    def generate_prompt(self, agent_type: str) -> str:
        """
        Generate a prompt for the specified agent type.

        Args:
            agent_type (str): The type of agent to generate a prompt for

        Returns:
            str: The generated prompt
        """
        prompt = ""

        # Add instruction
        if agent_type in self.prompt_templates["templates"]["match_agent"]:
            template = Template(self.prompt_templates["templates"]["match_agent"][agent_type]["instruction"])

            # Generate CFG for control flow agent
            if agent_type == "control_flow_agent":
                source_cfg = self.generate_cfg(self.configs["source_language"], self.source_method_implementation, "")
                target_cfg = self.generate_cfg(self.configs["target_language"], self.target_method_implementation, "")

                instruction = template.render(
                    {
                        "source_language": self.configs["source_language"].capitalize(),
                        "target_language": self.configs["target_language"].capitalize(),
                        "source_cfg": source_cfg,
                        "target_cfg": target_cfg,
                    }
                )
            # Generate DFG for data flow agent
            elif agent_type == "data_flow_agent":
                source_dfg = self.generate_dfg(self.configs["source_language"], self.source_method_implementation, "")
                target_dfg = self.generate_dfg(self.configs["target_language"], self.target_method_implementation, "")

                instruction = template.render(
                    {
                        "source_language": self.configs["source_language"].capitalize(),
                        "target_language": self.configs["target_language"].capitalize(),
                        "source_dfg": source_dfg,
                        "target_dfg": target_dfg,
                    }
                )
            else:
                instruction = template.render(
                    {
                        "source_language": self.configs["source_language"].capitalize(),
                        "target_language": self.configs["target_language"].capitalize(),
                    }
                )

        # Add fragment details
        template = Template(self.prompt_templates["templates"]["match_agent"]["fragment_details"])
        fragment_details = template.render(
            {
                "source_file_path": self.source_file_path,
                "target_file_path": self.target_file_path,
                "source_method_implementation": self.source_method_implementation,
                "target_method_implementation": self.target_method_implementation,
            }
        )
        prompt += fragment_details
        prompt += "\n\n"

        prompt += instruction
        prompt += "\n\n"

        # Add response format
        if (
            agent_type in self.prompt_templates["templates"]["match_agent"]
            and "response_format" in self.prompt_templates["templates"]["match_agent"][agent_type]
        ):
            prompt += self.prompt_templates["templates"]["match_agent"][agent_type]["response_format"]
        prompt += "\n\n"

        return prompt

    def format_fragment_details(self) -> None:
        """
        Format the details of the source and target code fragments.
        """
        self.source_file_path = self.fragment_details["source_path"].replace(
            f"projects/{self.configs['project_name']}/", ""
        )
        self.target_file_path = self.fragment_details["target_path"].replace(
            f"projects/{self.configs['project_name']}/", ""
        )

        # trim leading indentation from source and target code (e.g., some languages like Python only parse when the indentation is correct)
        source_code = self.fragment_details["source_function"].copy()
        target_code = self.fragment_details["target_function"].copy()

        # if source/target code's first line has leading indentation, remove indentation from all lines
        if source_code and source_code[0].startswith("    "):
            leading_spaces = len(source_code[0]) - len(source_code[0].lstrip())
            source_code = [line[leading_spaces:] for line in source_code]

        if target_code and target_code[0].startswith("    "):
            leading_spaces = len(target_code[0]) - len(target_code[0].lstrip())
            target_code = [line[leading_spaces:] for line in target_code]

        self.source_method_implementation = "\n".join(source_code)
        self.target_method_implementation = "\n".join(target_code)
