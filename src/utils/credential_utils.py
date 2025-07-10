import os
import yaml
import random
import logging
from pathlib import Path
from typing import Dict, List, Tuple, Optional, Set

# Global registry to track used credentials
_used_credentials: Set[str] = set()


def load_credentials(credential_file: str) -> Dict:
    """
    Load credentials from the credential file.

    Args:
        credential_file (str): Path to the credentials YAML file

    Returns:
        Dict: The loaded credentials dictionary
    """
    try:
        with open(credential_file, "r") as f:
            credentials = yaml.safe_load(f)
        return credentials
    except Exception as e:
        logging.error(f"Error loading credentials: {str(e)}")
        return {}


def get_temporary_credentials():
    """
    Get temporary AWS credentials using the 'ada credentials' command.

    Returns:
        dict: Dictionary containing AWS temporary credentials

    Raises:
        subprocess.CalledProcessError: If the credential retrieval command fails
    """
    import subprocess
    import json

    try:
        result = subprocess.run(
            ["ada", "credentials", "print", "--account", "177107205214", "--role", "Admin"],
            capture_output=True,
            text=True,
            check=True,
        )
        return json.loads(result.stdout)
    except subprocess.CalledProcessError as e:
        logging.error(f"Failed to retrieve temporary credentials: {e}")
        raise


def get_agent_credentials(
    agent_name: str,
    sub_agent_name: Optional[str],
    configs: dict,
) -> Tuple[Dict, str, str, str]:
    """
    Get credentials for a specific agent and sub-agent.
    Uses a deterministic but distributed approach to assign different credentials
    to different agents and sub-agents to prevent hitting quotas.

    Args:
        agent_name (str): The name of the main agent
        sub_agent_name (Optional[str]): The name of the sub-agent, if applicable
        credential_file (str): Path to the credentials YAML file
        configs (dict): Configuration dictionary

    Returns:
        Tuple[Dict, str, str, str]: A tuple containing the credential dictionary, the region, the credential name, and the model

    Raises:
        ValueError: If no valid agent_name is provided or credentials are not available
    """
    if not agent_name:
        raise ValueError("Agent name must be provided to get credentials")

    credentials = load_credentials(configs["credential_file"])

    if not credentials:
        raise ValueError(f"No credentials found in {configs['credential_file']}")

    aws_credentials = credentials.get("aws_credentials", {})

    # If a config file is provided, check available_credentials
    if configs:
        try:
            # Filter credentials based on available_credentials in config
            available_creds = configs.get("available_credentials", [])
            if available_creds:
                aws_credentials = {k: v for k, v in aws_credentials.items() if k in available_creds}

            logging.info(f"Using filtered credentials: {list(aws_credentials.keys())}")
        except Exception as e:
            logging.warning(f"Failed to load agent config from {configs}: {str(e)}")

    if not aws_credentials:
        raise ValueError(f"No valid AWS credentials found for {agent_name}")

    # Get available credential names
    credential_names = list(aws_credentials.keys())
    random.shuffle(credential_names)  # Shuffle credentials to ensure randomness

    # Make sure we have enough credentials
    total_credentials = len(credential_names)
    global _used_credentials

    # If we're running out of credentials, reset the tracking
    if len(_used_credentials) >= total_credentials * 0.8:
        logging.info("Resetting credential tracking due to limited availability")
        _used_credentials.clear()

    # Generate a deterministic but unique identifier for this agent/sub-agent
    if sub_agent_name:
        combined_name = f"{agent_name}_{sub_agent_name}"
    else:
        combined_name = agent_name

    # Try to find an unused credential
    found_unused_credential = False
    attempts = 0
    max_attempts = total_credentials * 2  # Avoid infinite loops

    # First try a deterministic approach based on agent name
    name_hash = sum(ord(c) for c in combined_name)

    while not found_unused_credential and attempts < max_attempts:
        # Select credential based on hash plus attempt number
        cred_index = (name_hash + attempts) % len(credential_names)
        credential_name = credential_names[cred_index]

        if credential_name not in _used_credentials:
            # Found an unused credential
            found_unused_credential = True
            _used_credentials.add(credential_name)
            logging.info(f"Selected unused credential: {credential_name}")
            break

        attempts += 1

        # If we've tried all credentials and none are available, just pick one
        if attempts >= max_attempts:
            credential_name = credential_names[cred_index]
            logging.warning(
                f"Could not find unused credential after {max_attempts} attempts. Reusing: {credential_name}"
            )
            _used_credentials.add(credential_name)

    credential_data = aws_credentials.get(credential_name, {})

    # Extract region and model from the credential data
    region = credential_data.get("region", "us-west-2")  # Default fallback
    model = credential_data.get("model", "us.anthropic.claude-3-7-sonnet-20250219-v1:0")  # Default fallback

    # Create the credential dict with just the AWS keys
    credential = {
        "AWS_ACCESS_KEY_ID": credential_data.get("AWS_ACCESS_KEY_ID"),
        "AWS_SECRET_ACCESS_KEY": credential_data.get("AWS_SECRET_ACCESS_KEY"),
    }

    # For prod1, prod2, or prod3 credentials, try to get temporary session tokens
    if credential_name in ["prod1", "prod2", "prod3"]:
        try:
            logging.info(f"Retrieving temporary session tokens for {credential_name}")
            retrieved_credentials = get_temporary_credentials()
            credential["AWS_ACCESS_KEY_ID"] = retrieved_credentials["AccessKeyId"]
            credential["AWS_SECRET_ACCESS_KEY"] = retrieved_credentials["SecretAccessKey"]
            credential["AWS_SESSION_TOKEN"] = retrieved_credentials["SessionToken"]
        except Exception as e:
            logging.error(f"Failed to retrieve temporary credentials for {credential_name}: {str(e)}")
            # Fall back to credential 'one'
            logging.warning("Falling back to credential 'one'")
            fallback_credential_name = "one"

            # Make sure 'one' exists in aws_credentials
            if fallback_credential_name not in aws_credentials:
                logging.error(f"Fallback credential '{fallback_credential_name}' not found")
                raise ValueError(f"Failed to retrieve credentials and fallback not available")

            # Use credential 'one' instead
            fallback_credential_data = aws_credentials.get(fallback_credential_name, {})
            credential["AWS_ACCESS_KEY_ID"] = fallback_credential_data.get("AWS_ACCESS_KEY_ID")
            credential["AWS_SECRET_ACCESS_KEY"] = fallback_credential_data.get("AWS_SECRET_ACCESS_KEY")

            # Update credential name, region and model for return values
            credential_name = fallback_credential_name
            region = fallback_credential_data.get("region", region)
            model = fallback_credential_data.get("model", model)

    return credential, region, credential_name, model


def setup_environment_for_agent(
    agent_name: str,
    sub_agent_name: Optional[str],
    configs: dict,
) -> Tuple[Dict, str]:
    """
    Set up environment variables for a specific agent with appropriate AWS credentials.

    Args:
        agent_name (str): The name of the main agent
        sub_agent_name (Optional[str]): The name of the sub-agent, if applicable
        model_name (Optional[str]): The model name to use (if None, uses model from credential)
        credential_file (str): Path to the credentials YAML file
        configs (dict): Configuration dictionary

    Returns:
        Tuple[Dict, str]: The environment dictionary with appropriate AWS credentials and settings,
                         and the credential name being used

    Raises:
        ValueError: If agent_name is not provided or if credentials are not available
    """
    if not agent_name:
        raise ValueError("Agent name must be provided to setup environment")

    env = os.environ.copy()

    # Get credentials, region, and model for this agent - this will raise ValueError if credentials not available
    credential, region, credential_name, credential_model = get_agent_credentials(agent_name, sub_agent_name, configs)

    # Set up environment variables
    env["CLAUDE_CODE_USE_BEDROCK"] = "true"
    # Use provided model_name if available, otherwise use model from credential
    env["ANTHROPIC_MODEL"] = credential_model
    env["AWS_REGION"] = region

    # Set AWS credentials - both must be available
    if "AWS_ACCESS_KEY_ID" not in credential or "AWS_SECRET_ACCESS_KEY" not in credential:
        raise ValueError(f"Incomplete AWS credentials for agent {agent_name}")

    env["AWS_ACCESS_KEY_ID"] = credential["AWS_ACCESS_KEY_ID"]
    env["AWS_SECRET_ACCESS_KEY"] = credential["AWS_SECRET_ACCESS_KEY"]
    env["AWS_SESSION_TOKEN"] = credential["AWS_SESSION_TOKEN"] if "AWS_SESSION_TOKEN" in credential else ""

    # Add maven to PATH
    env["PATH"] = f"{os.path.expanduser('~/apache-maven-3.9.9/bin')}:{env['PATH']}"

    # Add cargo to PATH
    env["PATH"] = f"{os.path.expanduser('~/.cargo/bin')}:{env['PATH']}"

    # Add go to PATH
    env["PATH"] = f"{os.path.expanduser('/usr/local/go/bin')}:{env['PATH']}"

    # Add node to PATH
    env["PATH"] = f"{os.path.expanduser('~/.nvm/versions/node/v22.16.0/bin')}:{env['PATH']}"

    return env, credential_name
