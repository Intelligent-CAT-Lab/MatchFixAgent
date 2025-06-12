import os
import json
import asyncio
import logging


async def run_claude_command(
    prompt: str, feedback: str, model_name: str, configs: dict, logger=None
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

    Returns:
        tuple[bool, dict]: (success_status, parsed_output)
            - success_status: True if command executed successfully and output was valid JSON
            - parsed_output: The parsed JSON output from Claude, or None if unsuccessful
    """
    env = os.environ.copy()
    env["CLAUDE_CODE_USE_BEDROCK"] = "true"
    env["ANTHROPIC_MODEL"] = model_name
    env["PATH"] = f"{os.path.expanduser('~/apache-maven-3.9.9/bin')}:{env['PATH']}"

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
