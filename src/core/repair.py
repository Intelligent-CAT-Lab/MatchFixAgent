import os
import argparse
import yaml
import json
import subprocess
import tempfile
import shutil


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


def execute_oxidizer_tests(configs: dict, fragment_details: dict) -> bool:
    """
    Execute tests using the Oxidizer tool.

    This function runs the Oxidizer tool to execute tests on the provided code fragment.
    It returns True if all tests pass, otherwise False.
    """

    cwd = os.path.join(configs["tool_target_projects_path"], "projects", configs["project_name"], "rust")

    print(fragment_details["id"])
    exit()

    # Run Oxidizer tests
    result = subprocess.run(["cargo", "test", fragment_details["test_name"]], capture_output=True, text=True, cwd=cwd)

    if result.returncode != 0:
        print(f"Oxidizer tests failed for {fragment_details['id']}: {result.stdout}")
        return False

    print(f"Oxidizer tests passed for {fragment_details['id']}.")
    return True


def execute_skel_tests(configs: dict, fragment_details: dict) -> bool:
    """
    Execute tests using the Skel tool.

    This function runs the Skel tool to execute tests on the provided code fragment.
    It returns True if all tests pass, otherwise False.
    """

    cwd = os.path.join(configs["tool_target_projects_path"], "projects", configs["project_name"], "javascript")

    # Run Skel tests
    result = subprocess.run(["node", "translated.js"], capture_output=True, text=True, cwd=cwd)

    if result.returncode != 0:
        print(f"Skel tests failed for {fragment_details['id']}: {result.stderr} {result.stdout}")
        return False

    print(f"Skel tests passed for {fragment_details['id']}.")
    return True


def execute_tests(configs: dict, fragment_details: dict) -> bool:

    if configs["tool_name"] == "oxidizer":
        return execute_oxidizer_tests(configs, fragment_details)
    elif configs["tool_name"] == "skel":
        return execute_skel_tests(configs, fragment_details)
    else:
        raise NotImplementedError(f"Tool {configs['tool_name']} is not supported for test execution.")


def validate_patch(fragment_details: dict, configs: dict, target_file: str, target_function: str) -> bool:

    patch = fragment_details[configs["agent_name"]]["output"]["test_repair"]["parsed_final_response"][
        "correct_target_method_implementation"
    ]
    patch = patch.replace('#[cfg(not(feature = "mock"))]', "").lstrip() + "\n"

    target_file = target_file.replace(target_function, patch)

    with open(os.path.join(configs["tool_target_projects_path"], fragment_details["target_path"]), "w") as f:
        f.write(target_file)

    return execute_tests(configs, fragment_details)


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

        # only interested in intersection of failing fragments
        if (
            fragment_details[configs["agent_name"]]["output"]["test_repair"]["parsed_final_response"]["is_equivalent"]
            != "no"
        ) or (fragment_details["result"] != "failure"):
            continue

        if configs["tool_name"] in ["skel", "rustrepotrans"]:
            target_function = "\n".join(fragment_details["ground_truth_target_function"])
        else:
            target_function = "\n".join([x for x in fragment_details["target_function"] if x.strip()])

        if configs["tool_name"] == "oxidizer":
            os.system(f"rustfmt {os.path.join(configs['tool_target_projects_path'], fragment_details['target_path'])}")
            target_function = format_rust_code(target_function)

        target_file = ""
        with open(os.path.join(configs["tool_target_projects_path"], fragment_details["target_path"]), "r") as f:
            target_file = f.read()

        if target_function not in target_file:
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
    args = parser.parse_args()

    main(args)
