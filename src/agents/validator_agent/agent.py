import os
import argparse
import asyncio
import json
import sys
import yaml

from src.utils.agent_utils import MCPConfig
from src.utils.agent_utils import Session
from src.utils.agent_utils import Model
from src.utils.agent_utils import Conversation

from src.agents.validator_agent.prompt_generator import ValidatorAgentPromptGenerator


class ValidatorAgent:

    def __init__(self, model: Model, session: Session, mcp_config: MCPConfig) -> None:
        self.model = model
        self.conversation = Conversation()

    async def run_cmd(self, prompt: str) -> tuple[bool, dict]:
        env = os.environ.copy()
        env["CLAUDE_CODE_USE_BEDROCK"] = "true"
        env["ANTHROPIC_MODEL"] = self.model.model_name

        try:
            # Use asyncio.create_subprocess_exec for true async operation
            process = await asyncio.create_subprocess_exec(
                "claude",
                "-p",
                prompt,
                "--output-format",
                "json",
                stdout=asyncio.subprocess.PIPE,
                stderr=asyncio.subprocess.PIPE,
                env=env,
            )

            stdout, stderr = await process.communicate()

            if process.returncode != 0:
                print(
                    f"Error: Claude failed with exit code {process.returncode}",
                    file=sys.stderr,
                )
                print(f"Error details: {stderr.decode()}", file=sys.stderr)
                return False, None

            output = stdout.decode("utf-8")
            parsed_output = json.loads(output)
            return True, parsed_output

        except Exception as e:
            print(f"Error executing Claude: {str(e)}", file=sys.stderr)
            return False, None

    async def run(
        self,
        configs: dict,
        source_schema_name: str,
        target_schema_name: str,
        class_name: str,
        method_name: str,
        method_pair: dict,
    ) -> None:

        prompt_generator = ValidatorAgentPromptGenerator(
            configs=configs,
            source_schema_name=source_schema_name,
            target_schema_name=target_schema_name,
            class_name=class_name,
            method_name=method_name,
            method_pair=method_pair,
        )
        prompt = prompt_generator.generate_prompt()

        self.conversation.add_message(role="user", content=prompt)

        max_retries = configs["agents"]["validator_agent"]["max_retries"]
        while True:
            max_retries -= 1
            status = await self.run_cmd(prompt)
            if status:
                break
            else:
                if max_retries == 0:
                    print("Max retries reached. Exiting.")
                    break
                print("Retrying command execution...")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Validator Agent")
    parser.add_argument("--config_file", type=str, required=True, help="Path to the config file")
    args = parser.parse_args()

    configs = yaml.safe_load(open(args.config_file, "r"))
    args.model = configs["agents"]["validator_agent"]["model"]
    args.session_id = 0
    args.mcp_config_file = configs["agents"]["validator_agent"]["mcp_config_file"]

    model = Model(args.model)
    session = Session(args.session_id)
    mcp_config = MCPConfig(args.mcp_config_file)

    validator_agent = ValidatorAgent(model, session, mcp_config)

    source_schema_name = "commons-cli.src.main.java.org.apache.commons.cli.PatternOptionBuilder_python_partial"
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

    asyncio.run(
        validator_agent.run(configs, source_schema_name, target_schema_name, class_name, method_name, method_pair)
    )
