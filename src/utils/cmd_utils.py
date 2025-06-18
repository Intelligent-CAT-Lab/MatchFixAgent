import os
import json
import asyncio
import logging
import yaml
import random
from pathlib import Path


async def run_claude_command(
    prompt: str,
    feedback: str,
    model_name: str,
    configs: dict,
    logger=None,
    agent_name: str = None,
    sub_agent_name: str = None,
) -> tuple[bool, dict]:
    """
    Execute Claude CLI command with the given prompt.

    Runs Claude via CLI subprocess and parses the JSON output.
    Utility function that can be imported by different agents.

    Args:
        prompt (str): The prompt to send to Claude
        feedback (str): Optional feedback to append to the prompt for retries
        model_name (str): Name of the model to use
        configs (dict): Configuration settings
        logger (logging.Logger, optional): Logger to use. If None, logs to console only.
        agent_name (str): The name of the agent running the command
        sub_agent_name (str, optional): The name of the sub-agent running the command

    Returns:
        tuple[bool, dict]: (success_status, parsed_output)
            - success_status: True if command executed successfully and output was valid JSON
            - parsed_output: The parsed JSON output from Claude, or None if unsuccessful

    Raises:
        ValueError: If agent_name is not provided or credentials are not available
    """
    if not agent_name:
        raise ValueError("Agent name must be provided to run Claude command")

    # Import and use credential utility
    from src.utils.credential_utils import setup_environment_for_agent

    # Set up environment with appropriate credentials
    try:
        env, credential_name = setup_environment_for_agent(
            agent_name=agent_name, sub_agent_name=sub_agent_name, model_name=model_name
        )

        if logger:
            logger.info(f"Using credentials for agent: {agent_name}, sub-agent: {sub_agent_name or 'None'}")
            logger.info(f"Using credential: '{credential_name}' in region: {env.get('AWS_REGION', 'unknown')}")
    except Exception as e:
        if logger:
            logger.error(f"Failed to set up credentials: {str(e)}")
        raise

    if feedback != "" and logger:
        logger.info(f"Feedback provided: {feedback}")
        prompt += f"\n\nFeedback: {feedback}"

    try:
        if logger:
            logger.info("Executing Claude CLI command...")
        # Use asyncio.create_subprocess_exec for true async operation
        cmd = ["claude", "-p", prompt] + configs["extra_agent_args"]
        process = await asyncio.create_subprocess_exec(
            *cmd,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
            env=env,
        )

        stdout, stderr = await process.communicate()

        if process.returncode != 0:
            if logger:
                logger.error(f"Claude failed with exit code {process.returncode}")
                logger.error(f"Error details: {stderr.decode()}")
            return False, None

        output = stdout.decode("utf-8")
        if logger:
            logger.debug("Raw output received from Claude")

        try:
            parsed_output = json.loads(output)
            if logger:
                logger.info("Successfully parsed Claude output as JSON")
            return True, parsed_output
        except json.JSONDecodeError as e:
            if logger:
                logger.error(f"Failed to parse Claude output as JSON: {e}")
                logger.debug(f"Raw output: {output}")
            return False, None

    except Exception as e:
        if logger:
            logger.error(f"Error executing Claude: {str(e)}")
        return False, None
