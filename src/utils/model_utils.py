import os
import json
import asyncio
import logging
from typing import Dict, Tuple, Any, Optional

from src.utils.cmd_utils import run_claude_code, prompt_claude, run_codex, prompt_gpt


class ModelUtils:
    """
    A wrapper class to handle model operations for different vendors (Anthropic, OpenAI).

    This class provides unified interfaces for prompting models regardless of the vendor,
    abstracting away the implementation details of each vendor's API.

    Attributes:
        vendor (str): The vendor of the model, either "anthropic" or "openai"
        configs (dict): Configuration settings
        logger (logging.Logger, optional): Logger to use
    """

    def __init__(
        self, vendor: str = None, configs: Dict[str, Any] = None, logger: Optional[logging.Logger] = None
    ) -> None:
        """
        Initialize the ModelUtils with a vendor and configuration.

        Args:
            vendor (str, optional): The vendor of the model, either "anthropic" or "openai".
                                   If None, will try to get from configs["vendor"].
            configs (dict): Configuration settings
            logger (logging.Logger, optional): Logger to use. If None, logs to console only.
        """
        self.configs = configs or {}
        self.logger = logger

        # Get vendor from parameter or configs, default to anthropic
        self.vendor = vendor.lower() if vendor else self.configs.get("vendor", "anthropic").lower()

        if self.vendor not in ["anthropic", "openai"]:
            raise ValueError("Vendor must be either 'anthropic' or 'openai'")

        if self.logger:
            self.logger.info(f"Initialized ModelUtils with vendor: {self.vendor}")

    async def prompt_agent(
        self,
        prompt: str,
        feedback: str = "",
        agent_name: str = None,
        sub_agent_name: str = None,
        timeout: int = None,
    ) -> Tuple[bool, Dict]:
        """
        Execute model command via appropriate API with the given prompt.

        This is a wrapper for run_claude_code (for Anthropic) or equivalent OpenAI function.

        Args:
            prompt (str): The prompt to send to the model
            feedback (str): Optional feedback to append to the prompt for retries
            agent_name (str): The name of the agent running the command
            sub_agent_name (str, optional): The name of the sub-agent running the command
            timeout (int, optional): Maximum time in seconds to wait for model's response.
                               If None, no timeout will be applied.

        Returns:
            tuple[bool, dict]: (success_status, captured_output)
                - success_status: True for both normal completions and timeouts
                - captured_output: Dictionary containing model response details

        Raises:
            ValueError: If agent_name is not provided or credentials are not available
        """
        if self.vendor == "anthropic":
            return await run_claude_code(
                prompt=prompt,
                feedback=feedback,
                configs=self.configs,
                logger=self.logger,
                agent_name=agent_name,
                sub_agent_name=sub_agent_name,
                timeout=timeout,
            )
        elif self.vendor == "openai":
            # Use run_codex which now uses the CLI with JSON output
            return await run_codex(
                prompt=prompt,
                feedback=feedback,
                configs=self.configs,
                logger=self.logger,
                agent_name=agent_name,
                sub_agent_name=sub_agent_name,
                timeout=timeout,
            )
        else:
            raise ValueError(f"Unsupported vendor: {self.vendor}. Supported vendors are 'anthropic' and 'openai'.")

    async def prompt_model(
        self,
        prompt: str,
        feedback: str = "",
        agent_name: str = None,
        sub_agent_name: str = None,
    ) -> Tuple[bool, Dict]:
        """
        Execute model via appropriate API with the given prompt.

        This is a wrapper for prompt_claude (for Anthropic) or equivalent OpenAI function.

        Args:
            prompt (str): The prompt to send to the model
            feedback (str): Optional feedback to append to the prompt for retries
            agent_name (str): The name of the agent running the command
            sub_agent_name (str, optional): The name of the sub-agent running the command

        Returns:
            tuple[bool, dict]: (success_status, parsed_output)
                - success_status: True if command executed successfully and output was valid
                - parsed_output: The parsed output from the model, or None if unsuccessful

        Raises:
            ValueError: If agent_name is not provided or credentials are not available
        """
        if self.vendor == "anthropic":
            return await prompt_claude(
                prompt=prompt,
                feedback=feedback,
                configs=self.configs,
                logger=self.logger,
                agent_name=agent_name,
                sub_agent_name=sub_agent_name,
            )
        elif self.vendor == "openai":
            return await prompt_gpt(
                prompt=prompt,
                feedback=feedback,
                configs=self.configs,
                logger=self.logger,
                agent_name=agent_name,
                sub_agent_name=sub_agent_name,
            )
        else:
            raise ValueError(f"Unsupported vendor: {self.vendor}. Supported vendors are 'anthropic' and 'openai'.")
