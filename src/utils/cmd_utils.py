import os
import json
import asyncio
import logging
import boto3
from botocore.exceptions import ClientError
import openai


async def run_claude_code(
    prompt: str,
    feedback: str,
    configs: dict,
    logger=None,
    agent_name: str = None,
    sub_agent_name: str = None,
    timeout: int = None,
) -> tuple[bool, dict]:
    """
    Execute Claude CLI command with the given prompt and optional timeout.

    Runs Claude via CLI subprocess with stream-json output format, intercepts and parses
    the streamed JSONs. Utility function that can be imported by different agents.

    Args:
        prompt (str): The prompt to send to Claude
        feedback (str): Optional feedback to append to the prompt for retries
        model_name (str): Name of the model to use
        configs (dict): Configuration settings
        logger (logging.Logger, optional): Logger to use. If None, logs to console only.
        agent_name (str): The name of the agent running the command
        sub_agent_name (str, optional): The name of the sub-agent running the command
        timeout (int, optional): Maximum time in seconds to wait for Claude's response.
                               If None, no timeout will be applied.

    Returns:
        tuple[bool, dict]: (success_status, captured_output)
            - success_status: True for both normal completions and timeouts
            - captured_output: A dictionary containing:
                - For normal completions: first and last intercepted JSONs in 'first_json' and 'last_json'
                - For timeouts or errors: only the first intercepted JSON in 'first_json'

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

    process = None
    captured_jsons = []
    try:
        if logger:
            logger.info(f"Executing Claude CLI command{' with timeout: ' + str(timeout) + 's' if timeout else ''}...")
        # Use asyncio.create_subprocess_exec for true async operation
        cmd = (
            ["claude", "-p", prompt]
            + ["--mcp-config", f"{os.getcwd()}/configs/claude_mcp_config.json"]
            + configs["extra_agent_args"]
        )
        working_dir = f"data/tool_projects/{configs['tool_name']}/projects/{configs['project_name']}"
        process = await asyncio.create_subprocess_exec(
            *cmd,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
            env=env,
            cwd=working_dir if working_dir else None,
        )

        # Process the output stream in fixed‐size chunks to avoid 64 KiB readline limit
        async def process_stream():
            buffer = b""
            chunk_size = 32_768  # 32 KiB
            while True:
                chunk = await process.stdout.read(chunk_size)
                if not chunk:
                    break  # End of stream
                buffer += chunk
                while b"\n" in buffer:
                    line, buffer = buffer.split(b"\n", 1)
                    line_str = line.decode("utf-8").strip()
                    if not line_str:
                        continue
                    try:
                        json_obj = json.loads(line_str)
                        captured_jsons.append(json_obj)
                        if logger:
                            logger.debug(f"Captured JSON: {json_obj}")
                            logger.debug(f"Captured JSON stream: {len(captured_jsons)} items so far")
                    except json.JSONDecodeError as e:
                        if logger:
                            logger.warning(f"Failed to parse stream JSON: {e}")
                            logger.debug(f"Raw line: {line_str}")

        # Run with or without timeout
        if timeout is not None:
            try:
                # Create a task for stream processing
                stream_task = asyncio.create_task(process_stream())
                # Wait for the task to complete with timeout
                await asyncio.wait_for(stream_task, timeout=timeout)
                # Wait for process to finish
                await process.wait()  # Don't need to store return code, using process.returncode later
            except asyncio.TimeoutError:
                # Timeout occurred
                if logger:
                    logger.warning(f"Claude command timed out after {timeout} seconds")

                # Cancel the stream processing task
                stream_task.cancel()
                try:
                    await asyncio.wait_for(stream_task, timeout=1.0)
                except (asyncio.TimeoutError, asyncio.CancelledError):
                    pass

                # Try to terminate the process gracefully
                if process and process.returncode is None:
                    try:
                        process.terminate()
                        # Wait a short time for it to terminate
                        await asyncio.sleep(0.5)
                        # Force kill if still running
                        if process.returncode is None:
                            process.kill()
                    except Exception as e:
                        if logger:
                            logger.error(f"Error terminating subprocess during timeout: {str(e)}")

                # Return the first captured JSON if available with timeout flag
                result = {"timeout": True}  # Add explicit timeout flag
                if captured_jsons:
                    result["first_json"] = captured_jsons[0]
                    if logger:
                        logger.info(
                            f"Returning first captured JSON from {len(captured_jsons)} total received before timeout"
                        )

                # Return with success=True as requested
                return True, result
        else:
            # No timeout, process the entire stream
            await process_stream()
            # Wait for process to finish
            await process.wait()  # Don't need to store return code, using process.returncode later

        # Handle process completion
        if process.returncode != 0:
            stderr_content = await process.stderr.read()
            if logger:
                logger.error(f"Claude failed with exit code {process.returncode}")
                logger.error(f"Error details: {stderr_content.decode(errors='ignore')}")

            # Return the first captured JSON if available, with success=True
            result = {"timeout": False}  # Not a timeout, but process error
            if captured_jsons:
                result["first_json"] = captured_jsons[0]
            return True, result

        # Normal completion
        if logger:
            logger.info(f"Claude command completed successfully. Captured {len(captured_jsons)} JSON objects")

        # Return first and last JSON for normal termination
        result = {"timeout": False}  # Explicitly mark as not timeout
        if captured_jsons:
            result["first_json"] = captured_jsons[0]
            result["last_json"] = captured_jsons[-1]

            # Store the result for compatibility with older code
            if "result" in captured_jsons[-1]:
                result["result"] = captured_jsons[-1]["result"]

        return True, result

    except asyncio.CancelledError:
        # Properly handle task cancellation (e.g., due to timeout)
        if process and process.returncode is None:
            try:
                # Try to terminate the process gracefully
                process.terminate()
                # Wait a short time for it to terminate
                await asyncio.sleep(0.5)
                # Force kill if still running
                if process.returncode is None:
                    process.kill()
            except Exception as e:
                if logger:
                    logger.error(f"Error terminating subprocess during cancellation: {str(e)}")

        # Return the first captured JSON if available, with success=True
        result = {"timeout": True}  # Cancellation is usually due to timeout
        if captured_jsons:
            result["first_json"] = captured_jsons[0]
            if logger:
                logger.info(f"Returning first captured JSON from cancellation")
        return True, result  # Return True as requested instead of re-raising

    except Exception as e:
        if logger:
            logger.error(f"Error executing Claude: {str(e)}")
        # Ensure process is cleaned up on any exception
        if process and process.returncode is None:
            try:
                process.terminate()
            except:
                pass

        # Return the first captured JSON if available, with success=True
        result = {"timeout": False}  # Not a timeout, but an exception
        if captured_jsons:
            result["first_json"] = captured_jsons[0]
            if logger:
                logger.info(f"Returning first captured JSON from exception handler")
        return True, result  # Return True as requested


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
            aws_session_token=env.get("AWS_SESSION_TOKEN"),
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


async def run_codex(
    prompt: str,
    feedback: str,
    configs: dict,
    logger=None,
    agent_name: str = None,
    sub_agent_name: str = None,
    timeout: int = None,
) -> tuple[bool, dict]:
    """
    Execute Codex CLI command with the given prompt and optional timeout.

    Runs Codex via CLI subprocess with JSON output format, intercepts and parses
    the JSON output. Utility function that can be imported by different agents.

    Args:
        prompt (str): The prompt to send to Codex
        feedback (str): Optional feedback to append to the prompt for retries
        configs (dict): Configuration settings
        logger (logging.Logger, optional): Logger to use. If None, logs to console only.
        agent_name (str): The name of the agent running the command
        sub_agent_name (str, optional): The name of the sub-agent running the command
        timeout (int, optional): Maximum time in seconds to wait for Codex's response.
                              If None, no timeout will be applied.

    Returns:
        tuple[bool, dict]: (success_status, captured_output)
            - success_status: True for both normal completions and timeouts
            - captured_output: A dictionary containing parsed JSON from Codex

    Raises:
        ValueError: If agent_name is not provided or credentials are not available
    """
    if not agent_name:
        raise ValueError("Agent name must be provided to run Codex command")

    # Import and use credential utility
    from src.utils.credential_utils import setup_environment_for_agent

    # Set up environment with appropriate credentials
    try:
        env, credential_name = setup_environment_for_agent(
            agent_name=agent_name, sub_agent_name=sub_agent_name, configs=configs
        )

        if logger:
            logger.info(f"Using credentials for agent: {agent_name}, sub-agent: {sub_agent_name or 'None'}")
            logger.info(f"Using credential: '{credential_name}'")
            logger.info(f"Using Codex model: {env.get('OPENAI_MODEL', 'unknown')}")
    except Exception as e:
        if logger:
            logger.error(f"Failed to set up credentials: {str(e)}")
        raise

    if feedback != "" and logger:
        logger.info(f"Feedback provided: {feedback}")
        prompt += f"\n\nFeedback: {feedback}"

    process = None
    captured_output = ""
    try:
        if logger:
            logger.info(f"Executing Codex CLI command{' with timeout: ' + str(timeout) + 's' if timeout else ''}...")

        # Build Codex command based on run.sh
        model_name = env.get("OPENAI_MODEL", "o4-mini")
        working_dir = f"data/tool_projects/{configs['tool_name']}/projects/{configs['project_name']}"
        cmd = ["codex", "exec", "--config", f'model="{model_name}"'] + configs["extra_agent_args"] + [prompt]

        logger.debug(f"Running Codex command: {' '.join(cmd)}")

        # Use asyncio.create_subprocess_exec for true async operation
        process = await asyncio.create_subprocess_exec(
            *cmd,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
            env=env,
            cwd=working_dir if working_dir else None,
        )

        # Process the output stream
        async def read_output():
            nonlocal captured_output
            captured_jsons = []
            agent_message_json = None

            while True:
                line = await process.stdout.readline()
                if not line:
                    break

                line_str = line.decode("utf-8").strip()
                captured_output += line_str + "\n"

                if logger:
                    logger.debug(f"Captured JSON: {line_str}")
                    logger.debug(f"Captured JSON stream: {len(captured_jsons)} items so far")

                # Try to parse each line as JSON
                try:
                    json_obj = json.loads(line_str)
                    captured_jsons.append(json_obj)

                    # Check if this is an agent_message type JSON
                    if "msg" in json_obj and json_obj["msg"].get("type") == "agent_message":
                        agent_message_json = json_obj
                        if logger:
                            logger.debug(f"Found agent_message JSON: {json_obj}")
                except json.JSONDecodeError:
                    # Skip lines that aren't valid JSON
                    pass

            return captured_output, captured_jsons, agent_message_json

        # Run with or without timeout
        captured_jsons = []
        agent_message_json = None

        if timeout is not None:
            try:
                # Create a task for output reading
                read_task = asyncio.create_task(read_output())
                # Wait for the task to complete with timeout
                captured_output, captured_jsons, agent_message_json = await asyncio.wait_for(read_task, timeout=timeout)
                # Wait for process to finish
                await process.wait()
            except asyncio.TimeoutError:
                # Timeout occurred
                if logger:
                    logger.warning(f"Codex command timed out after {timeout} seconds")

                # Cancel the read task
                read_task.cancel()

                # Try to terminate the process gracefully
                if process and process.returncode is None:
                    try:
                        process.terminate()
                        await asyncio.sleep(0.5)
                        if process.returncode is None:
                            process.kill()
                    except Exception as e:
                        if logger:
                            logger.error(f"Error terminating subprocess during timeout: {str(e)}")

                # Find the agent_message JSON if available
                result_content = ""
                if agent_message_json and "msg" in agent_message_json and "message" in agent_message_json["msg"]:
                    result_content = agent_message_json["msg"]["message"]
                else:
                    result_content = captured_output or "Response timed out"

                # Return with timeout flag
                return True, {
                    "timeout": True,
                    "result": result_content,
                    "last_json": agent_message_json or {"result": captured_output} if captured_output else None,
                }
        else:
            # No timeout, read all output
            captured_output, captured_jsons, agent_message_json = await read_output()
            # Wait for process to finish
            await process.wait()

        # Handle process completion
        if process.returncode != 0:
            stderr_content = await process.stderr.read()
            if logger:
                logger.error(f"Codex failed with exit code {process.returncode}")
                logger.error(f"Error details: {stderr_content.decode(errors='ignore')}")

            # Find the agent_message JSON if available even on error
            result_content = ""
            if agent_message_json and "msg" in agent_message_json and "message" in agent_message_json["msg"]:
                result_content = agent_message_json["msg"]["message"]
            else:
                result_content = captured_output

            # Return error information
            return True, {
                "timeout": False,
                "error": stderr_content.decode(errors="ignore"),
                "result": result_content,
                "last_json": agent_message_json or {"result": captured_output} if captured_output else None,
            }

        # Prepare the result
        result = {"timeout": False}

        # Extract result from agent message if available
        if agent_message_json and "msg" in agent_message_json and "message" in agent_message_json["msg"]:
            result_content = agent_message_json["msg"]["message"]
            result["result"] = result_content

            # Set up first_json and last_json for compatibility
            if captured_jsons:
                result["first_json"] = captured_jsons[0]
                result["last_json"] = agent_message_json
        else:
            # Fallback if no agent_message found
            if logger:
                logger.warning("No agent_message JSON found in output, using raw output")
            result["result"] = captured_output

            # Try to use any captured JSONs
            if captured_jsons:
                result["first_json"] = captured_jsons[0]
                result["last_json"] = captured_jsons[-1]
            else:
                # No JSONs captured at all, create a basic wrapper
                result["first_json"] = {"result": captured_output}
                result["last_json"] = {"result": captured_output}

        if logger:
            logger.info("Codex command completed successfully")

        return True, result

    except asyncio.CancelledError:
        # Handle task cancellation
        if process and process.returncode is None:
            try:
                process.terminate()
                await asyncio.sleep(0.5)
                if process.returncode is None:
                    process.kill()
            except Exception as e:
                if logger:
                    logger.error(f"Error terminating subprocess during cancellation: {str(e)}")

        # Return with cancellation info
        return True, {
            "timeout": True,
            "cancelled": True,
            "result": captured_output,
            "last_json": {"result": captured_output} if captured_output else None,
        }

    except Exception as e:
        if logger:
            logger.error(f"Error executing Codex: {str(e)}")
        # Clean up process
        if process and process.returncode is None:
            try:
                process.terminate()
            except:
                pass

        # Return error information
        return True, {
            "timeout": False,
            "error": str(e),
            "result": captured_output,
            "last_json": {"result": captured_output} if captured_output else None,
        }


async def prompt_gpt(
    prompt: str,
    feedback: str,
    configs: dict,
    logger=None,
    agent_name: str = None,
    sub_agent_name: str = None,
) -> tuple[bool, dict]:
    """
    Execute OpenAI GPT model via API with the given prompt.

    Uses OpenAI API to send the prompt directly to GPT models.
    Utility function that can be imported by different agents.
    Similar to prompt_claude but for OpenAI models.

    Args:
        prompt (str): The prompt to send to the GPT model
        feedback (str): Optional feedback to append to the prompt for retries
        configs (dict): Configuration settings
        logger (logging.Logger, optional): Logger to use. If None, logs to console only.
        agent_name (str): The name of the agent running the command
        sub_agent_name (str, optional): The name of the sub-agent running the command

    Returns:
        tuple[bool, dict]: (success_status, parsed_output)
            - success_status: True if command executed successfully and output was valid
            - parsed_output: The parsed output from GPT, or None if unsuccessful

    Raises:
        ValueError: If agent_name is not provided or credentials are not available
    """
    if not agent_name:
        raise ValueError("Agent name must be provided to run OpenAI command")

    # Import and use credential utility
    from src.utils.credential_utils import setup_environment_for_agent

    # Set up environment with appropriate credentials
    try:
        env, credential_name = setup_environment_for_agent(
            agent_name=agent_name, sub_agent_name=sub_agent_name, configs=configs
        )

        if logger:
            logger.info(f"Using credentials for agent: {agent_name}, sub-agent: {sub_agent_name or 'None'}")
            logger.info(f"Using credential: '{credential_name}'")
            logger.info(f"Using OpenAI model: {env.get('OPENAI_MODEL', 'o4-mini')}")
    except Exception as e:
        if logger:
            logger.error(f"Failed to set up credentials: {str(e)}")
        raise

    if feedback != "" and logger:
        logger.info(f"Feedback provided: {feedback}")
        prompt += f"\n\nFeedback: {feedback}"

    try:
        if logger:
            logger.info("Executing OpenAI GPT via API...")

        # Set up OpenAI client using API key from environment
        openai.api_key = env.get("OPENAI_API_KEY")

        # Default model if not specified
        model = env.get("OPENAI_MODEL", "o4-mini")

        # Create system prompt - use empty string if not provided in configs
        system_prompt = "You are a helpful assistant."

        # Make the API call
        response = openai.responses.create(
            model=model,
            instructions=system_prompt,
            input=prompt,
        )

        # Extract result text from response
        result_text = response.output_text

        # Create response body similar to Claude's format for compatibility
        response_body = {
            "result": result_text,
            "usage": {
                "input_tokens": response.usage.input_tokens,
                "output_tokens": response.usage.output_tokens,
            },
            "model": model,
        }

        if logger:
            logger.debug("Raw response received from OpenAI")
            logger.debug(f"Response body: {response_body}")

        return True, response_body

    except Exception as e:
        if logger:
            logger.error(f"Error executing OpenAI GPT: {str(e)}")
        return False, None
