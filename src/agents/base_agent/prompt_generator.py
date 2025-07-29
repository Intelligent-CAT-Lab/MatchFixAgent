import yaml
from jinja2 import Template


class BaseAgentPromptGenerator:

    def __init__(self, configs: dict, fragment_details: dict) -> None:
        self.configs = configs
        self.fragment_details = fragment_details

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
        self.source_file_path = self.fragment_details["source_path"].replace(
            f"projects/{self.configs['project_name']}/", ""
        )
        self.target_file_path = self.fragment_details["target_path"].replace(
            f"projects/{self.configs['project_name']}/", ""
        )

        self.source_method_implementation = "\n".join(self.fragment_details["source_function"]).strip()
        self.target_method_implementation = "\n".join(self.fragment_details["target_function"]).strip()
