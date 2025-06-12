import yaml
from jinja2 import Template


class BaseAgentPromptGenerator:

    def __init__(
        self,
        configs: dict,
        source_schema_name: str,
        target_schema_name: str,
        class_name: str,
        method_name: str,
        method_pair: dict,
    ) -> None:
        self.configs = configs
        self.source_schema_name = source_schema_name
        self.target_schema_name = target_schema_name
        self.class_name = class_name.split(":")[1] if ":" in class_name else class_name
        self.method_name = method_name.split(":")[1] if ":" in method_name else method_name
        self.method_pair = method_pair

        self.prompt_templates = yaml.safe_load(open("configs/prompt_templates.yaml", "r"))

        self.format_fragment_details()

        self.prompt = ""

    def generate_prompt(self) -> str:

        ### add instruction
        template = Template(self.prompt_templates["templates"]["base_agent"]["instruction"])
        instruction = template.render(
            {
                "source_language": self.configs["source_language"].capitalize(),
                "target_language": self.configs["target_language"].capitalize(),
                "method_name": self.method_name,
            }
        )
        self.prompt += instruction
        self.prompt += "\n\n"

        ### add fragment details
        template = Template(self.prompt_templates["templates"]["base_agent"]["fragment_details"])
        fragment_details = template.render(
            {
                "source_file_path": self.source_file_path,
                "target_file_path": self.target_file_path,
                "source_class_name": self.class_name,
                "target_class_name": self.class_name,
                "source_method_implementation": self.source_method_implementation,
                "target_method_implementation": self.target_method_implementation,
            }
        )
        self.prompt += fragment_details
        self.prompt += "\n\n"

        ### add response format
        self.prompt += self.prompt_templates["templates"]["base_agent"]["response_format"]
        self.prompt += "\n\n"

        ### add general notes
        self.prompt += self.prompt_templates["templates"]["base_agent"]["general_notes"]

        return self.prompt

    def format_fragment_details(self) -> None:
        tool_source_projects_path = self.configs["tool_source_projects_path"]
        self.source_file_path = f"{tool_source_projects_path}/{self.source_schema_name.replace('.', '/')}.java"

        tool_target_projects_path = self.configs["tool_target_projects_path"]
        self.target_file_path = f"{tool_target_projects_path}/{self.target_schema_name.replace('.', '/')}.py"

        self.source_method_implementation = "\n".join(self.method_pair["source_code"]).strip()
        self.target_method_implementation = "\n".join(self.method_pair["target_code"]).strip()
