import os
import json
import asyncio
import logging
import yaml
import random
import boto3
import time
from pathlib import Path
from botocore.exceptions import ClientError


async def run_claude_command(
    prompt: str,
    feedback: str,
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
            agent_name=agent_name, sub_agent_name=sub_agent_name, configs=configs
        )

        if logger:
            logger.info(f"Using credentials for agent: {agent_name}, sub-agent: {sub_agent_name or 'None'}")
            logger.info(f"Using credential: '{credential_name}' in region: {env.get('AWS_REGION', 'unknown')}")
            logger.info(f"Using Claude model: {env.get('ANTHROPIC_MODEL', 'unknown')}")
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


async def prompt_claude(
    prompt: str,
    feedback: str,
    configs: dict,
    logger=None,
    agent_name: str = None,
    sub_agent_name: str = None,
) -> tuple[bool, dict]:
    """
    Execute Claude model via AWS Bedrock API with the given prompt.

    Uses Bedrock API to send the prompt directly to Claude without using CLI.
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
            agent_name=agent_name, sub_agent_name=sub_agent_name, configs=configs
        )

        if logger:
            logger.info(f"Using credentials for agent: {agent_name}, sub-agent: {sub_agent_name or 'None'}")
            logger.info(f"Using credential: '{credential_name}' in region: {env.get('AWS_REGION', 'unknown')}")
            logger.info(f"Using Claude model: {env.get('ANTHROPIC_MODEL', 'unknown')}")
    except Exception as e:
        if logger:
            logger.error(f"Failed to set up credentials: {str(e)}")
        raise

    if feedback != "" and logger:
        logger.info(f"Feedback provided: {feedback}")
        prompt += f"\n\nFeedback: {feedback}"

    try:
        if logger:
            logger.info("Executing Claude via Bedrock API...")

        # Initialize Bedrock client with environment credentials
        bedrock_runtime = boto3.client(
            service_name="bedrock-runtime",
            region_name=env.get("AWS_REGION"),
            aws_access_key_id=env.get("AWS_ACCESS_KEY_ID"),
            aws_secret_access_key=env.get("AWS_SECRET_ACCESS_KEY"),
        )

        # Create system prompt - use empty string if not provided in configs
        system_prompt = "You are a helpful assistant."

        # Prepare message format for Claude
        messages = [{"role": "user", "content": prompt}]

        # Set max tokens - use default if not in configs
        max_tokens = configs.get("max_tokens", 8192)

        # Prepare request body
        body = json.dumps(
            {
                "anthropic_version": "bedrock-2023-05-31",
                "max_tokens": max_tokens,
                "system": system_prompt,
                "messages": messages,
            }
        )

        # Invoke model
        response = bedrock_runtime.invoke_model(body=body, modelId=env["ANTHROPIC_MODEL"])
        response_body = json.loads(response.get("body").read())

        result = response_body.get("content", [{}])[0].get("text", "")
        response_body["result"] = result

        if logger:
            logger.debug("Raw response received from Claude")
            logger.debug(f"Response body: {response_body}")

        return True, response_body

    except ClientError as err:
        if logger:
            message = err.response["Error"]["Message"]
            logger.error(f"A client error occurred: {message}")
        return False, None
