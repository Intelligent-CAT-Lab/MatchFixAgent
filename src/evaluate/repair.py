import os
import argparse
import yaml
import json
import subprocess
import tempfile
import shutil
import boto3
from botocore.exceptions import ClientError


def cleanup(configs: dict):
    """
    Cleanup function to remove temporary files created during validation.

    This function deletes the temporary files used by the ValidatorAgent
    to ensure no residual data is left after validation.
    """

    target_dir = os.path.join("data", "tool_projects", configs["tool_name"], "projects", configs["project_name"])

    assert target_dir, f"Target directory {target_dir} does not exist"
    assert os.path.exists(target_dir), f"Target directory {target_dir} does not exist"

    # Run `git status --porcelain data/tool_projects`
    proc = subprocess.run(["git", "status", "--porcelain", target_dir], capture_output=True, text=True, check=True)
    for line in proc.stdout.splitlines():
        if not line.strip():
            continue
        status, path = line[:2], line[3:]
        # Untracked files (“??”) → delete
        if status.strip() == "??":
            if "package-lock.json" in path or "package.json" in path or "node_modules" in path:
                continue
            if os.path.isdir(path):
                shutil.rmtree(path)
            elif os.path.isfile(path):
                os.remove(path)
        # Any other status → restore to HEAD
        else:
            subprocess.run(["git", "restore", path], check=False)


def format_rust_code(rust_code: str) -> str:
    with tempfile.NamedTemporaryFile(mode="w+", suffix=".rs", delete=False) as tmp:
        tmp.write(rust_code)
        tmp_filename = tmp.name

    try:
        subprocess.run(["rustfmt", tmp_filename], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        with open(tmp_filename, "r") as formatted_file:
            formatted_code = formatted_file.read()
    finally:
        os.remove(tmp_filename)

    return formatted_code


def prompt_claude(prompt):
    # make sure credential "one" is available in configs/aws_credentials.yaml
    credentials = yaml.safe_load(open("configs/aws_credentials.yaml", "r"))["aws_credentials"]["one"]

    try:
        bedrock_runtime = boto3.client(
            service_name="bedrock-runtime",
            region_name=credentials["region"],
            aws_access_key_id=credentials["AWS_ACCESS_KEY_ID"],
            aws_secret_access_key=credentials["AWS_SECRET_ACCESS_KEY"],
        )

        model_id = credentials["model"]
        system_prompt = "You are a helpful assistant."
        max_tokens = 1024

        # Prompt with user turn only.
        user_message = {"role": "user", "content": prompt}
        messages = [user_message]

        body = json.dumps(
            {
                "anthropic_version": "bedrock-2023-05-31",
                "max_tokens": max_tokens,
                "system": system_prompt,
                "messages": messages,
            }
        )

        response = bedrock_runtime.invoke_model(body=body, modelId=model_id)
        response_body = json.loads(response.get("body").read())
        return response_body["content"][0]["text"]

    except ClientError as err:
        return "A client error occurred: " + format(err)


def sanitize_oxidizer_patch(target_function: str, patch: str) -> str:
    """
    Sanitize the Oxidizer patch by removing unnecessary lines and comments.

    This function processes the patch to ensure it is clean and ready for application.
    It removes lines that are not part of the target function and formats the code.
    """

    prompt = f"""
    Correct template for the target function:
    ```rust
    {target_function}
    ```

    Potential patch:
    ```rust
    {patch}
    ```

    The above patch is a potential fix for the target function. It might need some adjustments, like:
    
    1. adding/removing braces
    2. wrapping the patch with "impl __Synth__" like target function
    
    Please ensure the patch is correctly formatted and similar to the target function. DO NOT change the logic of the patch.

    Put your response in the following format:
    ```rust
    <sanitized_patch>
    ```
    """

    sanitized_patch = prompt_claude(prompt)

    # extract the sanitized patch from the response using regex
    import re

    match = re.search(r"```rust\n(.*?)\n```", sanitized_patch, re.DOTALL)
    if match:
        sanitized_patch = match.group(1).strip()
    else:
        return patch

    return sanitized_patch


def execute_oxidizer_tests(configs: dict, fragment_details: dict, patch: str = "") -> bool:
    """
    Execute tests using the Oxidizer tool.

    This function runs the Oxidizer tool to execute tests on the provided code fragment.
    It returns True if all tests pass, otherwise False.
    """

    cwd = os.path.join(configs["tool_target_projects_path"], "projects", configs["project_name"], "rust")

    if args.run_agent_tests:
        print("### AGENT GENERATED TESTS ###")
        print(
            fragment_details[configs["agent_name"]]["output"]["test_repair"]["parsed_final_response"][
                "target_test_file_implementation"
            ]
        )
        input()  # Wait for user input to proceed
        return True

    # Run Oxidizer tests
    result = subprocess.run(["cargo", "test", fragment_details["test_name"]], capture_output=True, text=True, cwd=cwd)

    if result.returncode != 0:
        print(f"Oxidizer tests failed for {fragment_details['id']}: {result.stderr} {result.stdout}")
        return False

    print(f"Oxidizer tests passed for {fragment_details['id']}.")
    return True


def execute_skel_tests(configs: dict, fragment_details: dict, patch: str = "") -> bool:
    """
    Execute tests using the Skel tool.

    This function runs the Skel tool to execute tests on the provided code fragment.
    It returns True if all tests pass, otherwise False.
    """

    cwd = os.path.join(configs["tool_target_projects_path"], "projects", configs["project_name"], "javascript")

    if args.run_agent_tests:
        print("### AGENT GENERATED TESTS ###")
        print(
            fragment_details[configs["agent_name"]]["output"]["test_repair"]["parsed_final_response"][
                "target_test_file_implementation"
            ]
        )
        input()  # Wait for user input to proceed
        return True

    # Run Skel tests
    result = subprocess.run(["node", "translated.js"], capture_output=True, text=True, cwd=cwd)

    if result.returncode != 0:
        print(f"Skel tests failed for {fragment_details['id']}: {result.stderr} {result.stdout}")
        return False

    print(f"Skel tests passed for {fragment_details['id']}.")
    return True


def execute_rustrepotrans_tests(configs: dict, fragment_details: dict, patch: str = "") -> bool:
    """
    Execute tests using the RustRepotrans tool.

    This function runs the RustRepotrans tool to execute tests on the provided code fragment.
    It returns True if all tests pass, otherwise False.
    """

    cwd = os.path.join(configs["tool_target_projects_path"], "projects", configs["project_name"], "rust")

    if args.run_agent_tests:
        print("### AGENT GENERATED TESTS ###")
        print(
            fragment_details[configs["agent_name"]]["output"]["test_repair"]["parsed_final_response"][
                "target_test_file_implementation"
            ]
        )
        input()  # Wait for user input to proceed
        return True

    PROJECT_COMMANDS = {
        "iceberg": "make unit-test",
        "deltachat-core": "cargo nextest run",
        "incubator-milagro-crypto": "cargo test --all --all-features --release",
        "libp2p": "cargo test",
        "charset-normalizer": "cargo test",
    }

    SKIP_TESTS = {
        "libp2p": [
            "basic_resolve",  # this test reqires IPv6 support
            "given_periodic_bootstrap_when_routing_table_updated_then_wont_bootstrap_until_next_interval",  # this test is flaky
        ]
    }

    project_name = configs["project_name"]

    test_command = PROJECT_COMMANDS.get(project_name, "cargo test")

    if project_name in SKIP_TESTS:
        skip_flags = " ".join([f"--skip {test}" for test in SKIP_TESTS[project_name]])
        test_command = f"{test_command} -- {skip_flags}"

    result = subprocess.run(test_command.split(), capture_output=True, text=True, cwd=cwd)

    if result.returncode != 0:
        print(f"RustRepotrans tests failed for {fragment_details['id']}: {result.stderr} {result.stdout}", flush=True)
        return False

    print(f"RustRepotrans tests passed for {fragment_details['id']}.", flush=True)
    return True


def execute_alphatrans_tests(configs: dict, fragment_details: dict, patch: str = "") -> bool:
    """
    AlphaTrans GraalVM has major issues that cannot reliably validate the patch.
    This function is used by a user to manually verify the correctness of the patch.
    """

    if args.run_agent_tests:
        print("### AGENT GENERATED TESTS ###")
        print(
            fragment_details[configs["agent_name"]]["output"]["test_repair"]["parsed_final_response"][
                "target_test_file_implementation"
            ]
        )
        input()  # Wait for user input to proceed
        return True

    print("---" * 20)
    print("SOURCE CODE:")
    print("\n".join(fragment_details["source_function"]))
    print("---" * 20)
    print("TARGET FUNCTION:")
    print("\n".join(fragment_details["target_function"]))
    print("---" * 20)
    print("PATCH:")
    print(patch)
    print("---" * 20)
    print("Explanation:")
    print(fragment_details[configs["agent_name"]]["output"]["test_repair"]["parsed_final_response"]["explanation"])

    user_decision = input("Is the patch correct? (yes/no): ").strip().lower()
    if user_decision != "yes":
        print(f"User determined patch is not correct for {fragment_details['id']}.")
        return False

    print(f"User determined patch is correct for {fragment_details['id']}.")
    return True


def execute_tests(configs: dict, fragment_details: dict, patch: str) -> bool:

    if configs["tool_name"] == "oxidizer":
        return execute_oxidizer_tests(configs, fragment_details)
    elif configs["tool_name"] == "skel":
        return execute_skel_tests(configs, fragment_details)
    elif configs["tool_name"] == "rustrepotrans":
        return execute_rustrepotrans_tests(configs, fragment_details)
    elif configs["tool_name"] == "alphatrans":
        return execute_alphatrans_tests(configs, fragment_details, patch=patch)
    else:
        raise NotImplementedError(f"Tool {configs['tool_name']} is not supported for test execution.")


def validate_patch(fragment_details: dict, configs: dict, target_file: str, target_function: str) -> bool:

    patch = fragment_details[configs["agent_name"]]["output"]["test_repair"]["parsed_final_response"][
        "correct_target_method_implementation"
    ]
    if configs["tool_name"] == "oxidizer":
        patch = patch.replace('#[cfg(not(feature = "mock"))]', "").lstrip() + "\n"
        patch = sanitize_oxidizer_patch(target_function, patch)

    target_file = target_file.replace(target_function, patch)

    with open(os.path.join(configs["tool_target_projects_path"], fragment_details["target_path"]), "w") as f:
        f.write(target_file)

    return execute_tests(configs, fragment_details, patch)


def main(args):

    configs = yaml.safe_load(open(args.config_file, "r"))

    results_path = configs["tool_results_path"]
    with open(os.path.join(results_path, f"{configs['project_name']}.json"), "r") as f:
        results = json.load(f)

    total_fixed = 0
    total_failed = 0

    for fragment_details in results:

        cleanup(configs)

        if configs["agent_name"] not in fragment_details:
            continue

        if not fragment_details[configs["agent_name"]]["status"]:
            continue

        if fragment_details["source_language"] != configs["source_language"]:
            continue

        # only interested in intersection of failing fragments
        if (
            fragment_details[configs["agent_name"]]["output"]["test_repair"]["parsed_final_response"]["is_equivalent"]
            != "no"
        ) or (fragment_details["result"] != "failure"):
            continue

        if configs["tool_name"] in ["skel", "rustrepotrans"]:
            target_function = "\n".join(fragment_details["ground_truth_target_function"])
        elif configs["tool_name"] == "oxidizer":
            target_function = "\n".join(
                [x for x in fragment_details["target_function"] if x.strip() and not x.strip().startswith("//")]
            )
        elif configs["tool_name"] == "alphatrans":
            target_function = "\n".join(fragment_details["target_function"])
        else:
            raise NotImplementedError(f"Tool {configs['tool_name']} is not supported for target function extraction.")

        if configs["tool_name"] == "oxidizer":
            os.system(f"rustfmt {os.path.join(configs['tool_target_projects_path'], fragment_details['target_path'])}")
            target_function = format_rust_code(target_function)

        target_file = ""
        with open(os.path.join(configs["tool_target_projects_path"], fragment_details["target_path"]), "r") as f:
            target_file = f.read()

        if target_function not in target_file and configs["tool_name"] != "alphatrans":
            print(f'Could not find the target function in the target file for fragment {fragment_details["id"]}')
            continue

        status = validate_patch(fragment_details, configs, target_file, target_function)

        if status:
            total_fixed += 1
        else:
            total_failed += 1

        cleanup(configs)

    print()
    print(f"Total fragments fixed: {total_fixed}")
    print(f"Total fragments failed: {total_failed}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Evaluate and repair code fragments.")
    parser.add_argument("--config_file", type=str, required=True, help="Path to the config file")
    parser.add_argument("--run_agent_tests", action="store_true", help="Run agent tests")
    args = parser.parse_args()

    main(args)
