import os
import yaml
import random
import logging
from pathlib import Path
from typing import Dict, List, Tuple, Optional, Set

# Global registry to track used credential-region pairs
_used_credential_region_pairs: Set[Tuple[str, str]] = set()


def load_credentials(credential_file: str = "configs/aws_credentials.yaml") -> Dict:
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


def get_agent_credentials(
    agent_name: str,
    sub_agent_name: Optional[str] = None,
    credential_file: str = "configs/aws_credentials.yaml",
    config_file: str = None,
) -> Tuple[Dict, str, str]:
    """
    Get credentials for a specific agent and sub-agent.
    Uses a deterministic but distributed approach to assign different credentials
    to different agents and sub-agents to prevent hitting quotas.

    Args:
        agent_name (str): The name of the main agent
        sub_agent_name (Optional[str]): The name of the sub-agent, if applicable
        credential_file (str): Path to the credentials YAML file

    Returns:
        Tuple[Dict, str, str]: A tuple containing the credential dictionary, the region, and the credential name

    Raises:
        ValueError: If no valid agent_name is provided or credentials are not available
    """
    if not agent_name:
        raise ValueError("Agent name must be provided to get credentials")

    credentials = load_credentials(credential_file)

    if not credentials:
        raise ValueError(f"No credentials found in {credential_file}")

    aws_credentials = credentials.get("aws_credentials", {})
    aws_regions = credentials.get("aws_regions", [])

    # If a config file is provided, check available_credentials and available_regions
    if config_file:
        try:
            with open(config_file, "r") as f:
                agent_config = yaml.safe_load(f)

            # Filter credentials based on available_credentials in config
            available_creds = agent_config.get("available_credentials", [])
            if available_creds:
                aws_credentials = {k: v for k, v in aws_credentials.items() if k in available_creds}

            # Filter regions based on available_regions in config
            available_regions = agent_config.get("available_regions", [])
            if available_regions:
                aws_regions = [r for r in aws_regions if r in available_regions]

            logging.info(f"Using filtered credentials: {list(aws_credentials.keys())} and regions: {aws_regions}")
        except Exception as e:
            logging.warning(f"Failed to load agent config from {config_file}: {str(e)}")

    if not aws_credentials:
        raise ValueError(f"No valid AWS credentials found for {agent_name}")

    if not aws_regions:
        raise ValueError(f"No valid AWS regions found for {agent_name}")

    # Get available credential names and regions
    credential_names = list(aws_credentials.keys())
    available_regions = list(aws_regions)  # Make a copy we can modify

    # Make sure we have enough combinations
    total_combinations = len(credential_names) * len(available_regions)
    global _used_credential_region_pairs

    # If we're running out of combinations, reset the tracking
    if len(_used_credential_region_pairs) >= total_combinations * 0.8:
        logging.info("Resetting credential-region pair tracking due to limited availability")
        _used_credential_region_pairs.clear()

    # Generate a deterministic but unique identifier for this agent/sub-agent
    if sub_agent_name:
        combined_name = f"{agent_name}_{sub_agent_name}"
    else:
        combined_name = agent_name

    # Try to find an unused credential-region pair
    found_unused_pair = False
    attempts = 0
    max_attempts = total_combinations * 2  # Avoid infinite loops

    # First try a deterministic approach based on agent name
    name_hash = sum(ord(c) for c in combined_name)

    while not found_unused_pair and attempts < max_attempts:
        # Select credential based on hash plus attempt number
        cred_index = (name_hash + attempts) % len(credential_names)
        credential_name = credential_names[cred_index]

        # Try each region with this credential until we find an unused pair
        for region_offset in range(len(available_regions)):
            region_index = (cred_index + region_offset) % len(available_regions)
            region = available_regions[region_index]

            if (credential_name, region) not in _used_credential_region_pairs:
                # Found an unused pair
                found_unused_pair = True
                _used_credential_region_pairs.add((credential_name, region))
                logging.info(f"Selected unused credential-region pair: {credential_name} in {region}")
                break

        attempts += 1

        # If we've tried all combinations and none are available, just pick one
        if attempts >= max_attempts:
            credential_name = credential_names[cred_index]
            region = available_regions[0]
            logging.warning(
                f"Could not find unused credential-region pair after {max_attempts} attempts. Reusing: {credential_name} in {region}"
            )
            _used_credential_region_pairs.add((credential_name, region))

    credential = aws_credentials.get(credential_name, {})

    return credential, region, credential_name


def setup_environment_for_agent(
    agent_name: str,
    sub_agent_name: Optional[str] = None,
    model_name: str = "us.anthropic.claude-3-7-sonnet-20250219-v1:0",
    credential_file: str = "configs/aws_credentials.yaml",
    config_file: str = None,
) -> Tuple[Dict, str]:
    """
    Set up environment variables for a specific agent with appropriate AWS credentials.

    Args:
        agent_name (str): The name of the main agent
        sub_agent_name (Optional[str]): The name of the sub-agent, if applicable
        model_name (str): The model name to use
        credential_file (str): Path to the credentials YAML file

    Returns:
        Tuple[Dict, str]: The environment dictionary with appropriate AWS credentials and settings,
                         and the credential name being used

    Raises:
        ValueError: If agent_name is not provided or if credentials are not available
    """
    if not agent_name:
        raise ValueError("Agent name must be provided to setup environment")

    env = os.environ.copy()

    # Set default config file path based on agent_name if not provided
    if not config_file and agent_name:
        default_config_path = f"configs/{agent_name}.yaml"
        if Path(default_config_path).exists():
            config_file = default_config_path
            logging.info(f"Using agent config file: {config_file}")

    # Get credentials and region for this agent - this will raise ValueError if credentials not available
    credential, region, credential_name = get_agent_credentials(
        agent_name, sub_agent_name, credential_file, config_file
    )

    # Set up environment variables
    env["CLAUDE_CODE_USE_BEDROCK"] = "true"
    env["ANTHROPIC_MODEL"] = model_name
    env["AWS_REGION"] = region

    # Set AWS credentials - both must be available
    if "AWS_ACCESS_KEY_ID" not in credential or "AWS_SECRET_ACCESS_KEY" not in credential:
        raise ValueError(f"Incomplete AWS credentials for agent {agent_name}")

    env["AWS_ACCESS_KEY_ID"] = credential["AWS_ACCESS_KEY_ID"]
    env["AWS_SECRET_ACCESS_KEY"] = credential["AWS_SECRET_ACCESS_KEY"]

    # Add maven to PATH
    env["PATH"] = f"{os.path.expanduser('~/apache-maven-3.9.9/bin')}:{env['PATH']}"

    return env, credential_name
