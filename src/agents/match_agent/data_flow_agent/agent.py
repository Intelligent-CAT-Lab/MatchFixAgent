import os
import json
import logging
import re
import uuid
from pathlib import Path

from src.utils.agent_utils import Model
from src.utils.agent_utils import Conversation


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
        self.model = Model(self.configs["model"])
        self.conversation = Conversation()
        self.session_id = session_id or str(uuid.uuid4())

        # Set up logging
        log_dir = Path(f"logs/match_agent")
        log_dir.mkdir(parents=True, exist_ok=True)

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

    async def analyze(self, prompt_generator, method_pair):
        """
        Analyze the data flow of source and target code fragments.
        
        Args:
            prompt_generator: The prompt generator to use
            method_pair (dict): The method pair to analyze
            
        Returns:
            dict: Analysis results
        """
        self.logger.info("Analyzing data flow equivalence")

        # Generate the prompt using the template for data_flow_agent
        prompt = prompt_generator.generate_prompt("data_flow_agent")
        
        # Log the full prompt
        self.logger.debug("Generated data flow analysis prompt:")
        self.logger.debug(prompt)
        
        self.conversation.add_message(role="user", content=prompt)

        # Execute the model
        env = os.environ.copy()
        env["CLAUDE_CODE_USE_BEDROCK"] = "true"
        env["ANTHROPIC_MODEL"] = self.model.model_name
        
        try:
            # Use the dedicated utility function for command execution
            from src.utils.cmd_utils import run_claude_command
            status, agent_output = await run_claude_command(
                prompt, "", self.model.model_name, self.configs, self.logger
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
                        data_flow_analysis = json.loads(match.group(1))
                        self.logger.info(f"Data flow equivalence: {data_flow_analysis.get('is_equivalent', 'unknown')}")
                        # Return the entire agent_output with the parsed result
                        agent_output["parsed_final_response"] = data_flow_analysis
                        return agent_output
                    except json.JSONDecodeError as e:
                        self.logger.error(f"Failed to parse data flow analysis response as JSON: {e}")
                        agent_output["parsed_final_response"] = {
                            "is_equivalent": "error", 
                            "explanation": f"Failed to parse model response as JSON: {str(e)}"
                        }
                        return agent_output
                else:
                    self.logger.error("No final response format found in data flow analysis output")
                    agent_output["parsed_final_response"] = {
                        "is_equivalent": "error", 
                        "explanation": "No final response format found in data flow analysis output"
                    }
                    return agent_output
            else:
                self.logger.error("Data flow analysis failed")
                agent_output["parsed_final_response"] = {
                    "is_equivalent": "error", 
                    "explanation": "Data flow analysis did not complete successfully"
                }
                return agent_output
                
        except Exception as e:
            self.logger.error(f"Error in data flow analysis: {str(e)}")
            agent_output["parsed_final_response"] = {
                "is_equivalent": "error", 
                "explanation": f"Error during data flow analysis: {str(e)}"
            }
            return agent_output