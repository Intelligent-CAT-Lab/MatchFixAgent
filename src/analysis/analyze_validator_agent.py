"""
Analyze Validator Agent

This script analyzes the performance of the LLM Translation Validator Agent by:
1. Reading validation results from JSON files
2. Computing statistics on validation outcomes
3. Creating confusion matrices of tool validation vs. LLM predictions
4. Calculating performance metrics

The analysis helps evaluate how well the LLM validator compares to
traditional tool-based validators (e.g., Graal) for code translation validation.
"""

import os
import argparse
import json
import time
import pandas as pd


def find_trajectory_file(session_id):
    trajectory_dir = os.path.expanduser("~/.claude/projects")
    for root, dirs, files in os.walk(trajectory_dir):
        for file in files:
            if file.startswith(session_id) and file.endswith(".jsonl"):
                return os.path.join(root, file)
    raise FileNotFoundError(f"Trajectory file for session {session_id} not found in {trajectory_dir}.")


def copy_trajectory_file(session_id, destination_dir):
    """
    Copy the trajectory file for a given session ID to the specified destination directory.

    Args:
        session_id (str): The session ID to search for.
        destination_dir (str): The directory where the trajectory file should be copied.

    Returns:
        str: The path to the copied trajectory file.
    """
    trajectory_file = find_trajectory_file(session_id)
    os.makedirs(destination_dir, exist_ok=True)
    destination_path = os.path.join(destination_dir, os.path.basename(trajectory_file))
    with open(trajectory_file, "r") as src_file, open(destination_path, "w") as dest_file:
        dest_file.write(src_file.read())
    return destination_path


def get_agent_cost(agent_output):

    cost = {"total_num_turns": 0, "total_cost_usd": 0, "duration_ms": 0, "num_tool_calls": 0}

    if agent_output["parsed_final_response"]["is_equivalent"] in ["error", "other"]:
        return cost

    agent_output = agent_output["last_json"] or agent_output["first_json"]

    cost["total_num_turns"] += agent_output["num_turns"]
    cost["total_cost_usd"] += agent_output["total_cost_usd"]
    cost["duration_ms"] += agent_output["duration_ms"]

    # Load and analyze agent trajectory files
    session_id = agent_output["session_id"]
    trajectory_file = find_trajectory_file(session_id)
    copy_trajectory_file(session_id, "data/agent_trajectories")

    agent_trajectory = []
    with open(trajectory_file, "r") as f:
        agent_trajectory = [json.loads(line) for line in f]

    # Count tool calls in agent trajectories
    for i, item in enumerate(agent_trajectory):
        if "message" not in item:
            continue

        message = item["message"]

        if message["role"] != "assistant":
            continue

        for content in message["content"]:
            if content["type"] == "tool_use":
                cost["num_tool_calls"] += 1

    return cost


def reset_incomplete_responses(test_repair_error, verdict_error, result_file):
    """
    Reset incomplete responses by removing them from the results file.

    This function takes lists of test repair and verdict errors, and removes
    these entries from the results JSON file to ensure that they do not affect
    future analyses.

    Args:
        test_repair_error (list): List of IDs with test repair errors.
        verdict_error (list): List of IDs with verdict errors.
    """
    if not test_repair_error and not verdict_error:
        return

    with open(result_file, "r") as file:
        data = json.load(file)

    for item in data:
        if args.agent_name not in item:
            continue
        if item["id"] in test_repair_error or item["id"] in verdict_error:
            item[args.agent_name]["status"] = False

    with open(result_file, "w") as file:
        json.dump(data, file, indent=4)


def main(args):
    """
    Analyze validator agent performance across a dataset of method translations.

    This function:
    1. Loads results data for the specified project
    2. Collects statistics on validation outcomes
    3. Creates a confusion matrix of tool validation vs. LLM predictions
    4. Calculates costs, durations, and tool usage metrics
    5. Prints summary statistics and the confusion matrix

    Args:
        args (Namespace): Command line arguments containing:
            - project_name: Name of the project to analyze
            - results_dir: Directory containing results JSON files
            - trajectory_dir: Directory containing agent trajectory files
    """
    report_dir = "reports"

    # Initialize global metrics
    global_total = 0
    global_total_methods = 0
    global_tool_validation_dist = {"error": 0, "failure": 0, "not-exercised": 0, "pending": 0, "success": 0}
    global_equivalency_dist = {"yes": 0, "no": 0, "other": 0}
    global_total_num_turns = 0
    global_total_cost = 0
    global_total_time = 0
    global_total_tool_calls = 0
    global_timeout_count = 0

    # Initialize global error counts
    global_test_repair_errors = 0
    global_verdict_errors = 0

    for tool in ["alphatrans", "oxidizer", "skel", "rustrepotrans"]:
        for project in os.listdir(os.path.join("data", "agent_results", args.agent_name, tool)):

            os.makedirs(os.path.join(report_dir, args.agent_name, tool), exist_ok=True)

            result_file = os.path.join("data", "agent_results", args.agent_name, tool, project)
            with open(result_file, "r") as file:
                data = json.load(file)

            total = 0
            total_methods = 0
            tool_validation_dist = {"error": 0, "failure": 0, "not-exercised": 0, "pending": 0, "success": 0}
            equivalency_dist = {"yes": 0, "no": 0, "other": 0}
            total_num_turns = 0
            total_cost = 0
            total_time = 0
            total_tool_calls = 0

            # incomplete responses
            test_repair_error = []
            verdict_error = []

            disagreements = []

            # Count timeout cases for the project
            project_timeout_count = 0

            # Define possible outcomes
            tool_outcomes = ["error", "failure", "not-exercised", "pending", "success"]
            llm_outcomes = ["yes", "no", "other"]

            # Initialize confusion matrix with zeros
            confusion_df = pd.DataFrame(0, index=tool_outcomes, columns=llm_outcomes)

            for item in data:

                total += 1

                if args.agent_name not in item:
                    continue

                if not item[args.agent_name]["status"]:
                    continue

                verdict = "test_repair"
                if item[args.agent_name]["output"][verdict]["parsed_final_response"]["is_equivalent"] in [
                    "error",
                    "other",
                ]:
                    verdict = "verdict"

                total_methods += 1

                # Get tool validation outcome
                tool_validation = item["result"]

                # Get LLM prediction
                llm_prediction = item[args.agent_name]["output"][verdict]["parsed_final_response"]["is_equivalent"]

                if item[args.agent_name]["output"]["test_repair"]["parsed_final_response"]["is_equivalent"] == "error":
                    test_repair_error.append(item["id"])

                if item[args.agent_name]["output"]["verdict"]["parsed_final_response"]["is_equivalent"] == "error":
                    verdict_error.append(item["id"])

                if tool_validation == "success" and llm_prediction == "no":
                    disagreements.append(f"Tool (YES) vs Agent (NO): ID - {item['id']}")

                if tool_validation == "failure" and llm_prediction == "yes":
                    disagreements.append(f"Tool (NO) vs Agent (YES): ID - {item['id']}")

                # Update confusion matrix
                confusion_df.loc[tool_validation, llm_prediction] += 1

                # Check for timeout cases
                if (
                    item[args.agent_name]["output"]["test_repair"]["parsed_final_response"].get("is_equivalent")
                    == "other"
                    and item[args.agent_name]["output"]["test_repair"]["parsed_final_response"].get("explanation")
                    == "500: timeout"
                ):
                    project_timeout_count += 1

                if (
                    item[args.agent_name]["output"]["verdict"]["parsed_final_response"].get("is_equivalent") == "other"
                    and item[args.agent_name]["output"]["verdict"]["parsed_final_response"].get("explanation")
                    == "500: timeout"
                ):
                    project_timeout_count += 1

                # Continue with your existing stats collection
                tool_validation_dist[tool_validation] += 1
                equivalency_dist[llm_prediction] += 1

                test_repair_agent = item[args.agent_name]["output"]["test_repair"]
                verdict_agent = item[args.agent_name]["output"]["verdict"]

                test_repair_cost = get_agent_cost(test_repair_agent)
                verdict_cost = get_agent_cost(verdict_agent)

                total_num_turns += test_repair_cost["total_num_turns"] + verdict_cost["total_num_turns"]
                total_cost += test_repair_cost["total_cost_usd"] + verdict_cost["total_cost_usd"]
                total_time += test_repair_cost["duration_ms"] + verdict_cost["duration_ms"]
                total_tool_calls += test_repair_cost["num_tool_calls"] + verdict_cost["num_tool_calls"]

            # Verify data consistency
            assert total_methods == sum(
                equivalency_dist.values()
            ), "Total methods do not match the sum of equivalency distribution"

            total_methods = max(total_methods, 1)  # Avoid division by zero

            # Prepare the report content
            report_content = []
            report_content.append(f"Project: {project.split('.')[0]}")
            report_content.append(f"Agent: {args.agent_name}")
            report_content.append(f"Progress: {total_methods}/{total} [{total_methods / total:.2%}]")
            last_modified_time = os.path.getmtime(result_file)
            seconds_ago = time.time() - last_modified_time
            report_content.append(
                f"Results last modified: {seconds_ago // 3600}h, {(seconds_ago % 3600) // 60}m, {seconds_ago % 60:.2f}s ago"
            )
            report_content.append("---" * 50)
            report_content.append("MatchFixAgent: {")
            report_content.append(
                f"    yes:   {{ total: {equivalency_dist['yes']}, %: {equivalency_dist['yes'] / total_methods:.2%} }},"
            )
            report_content.append(
                f"    no:    {{ total: {equivalency_dist['no']}, %: {equivalency_dist['no'] / total_methods:.2%} }},"
            )
            report_content.append(
                f"    other: {{ total: {equivalency_dist['other']}, %: {equivalency_dist['other'] / total_methods:.2%} }}"
            )
            report_content.append("}")
            report_content.append("")
            report_content.append("Tool: {")
            report_content.append(
                f"    success:       {{ total: {tool_validation_dist['success']}, %: {tool_validation_dist['success'] / total_methods:.2%} }},"
            )
            report_content.append(
                f"    failure:       {{ total: {tool_validation_dist['failure']}, %: {tool_validation_dist['failure'] / total_methods:.2%} }},"
            )
            report_content.append(
                f"    not-exercised: {{ total: {tool_validation_dist['not-exercised']}, %: {tool_validation_dist['not-exercised'] / total_methods:.2%} }},"
            )
            report_content.append(
                f"    pending:       {{ total: {tool_validation_dist['pending']}, %: {tool_validation_dist['pending'] / total_methods:.2%} }},"
            )
            report_content.append(
                f"    error:         {{ total: {tool_validation_dist['error']}, %: {tool_validation_dist['error'] / total_methods:.2%} }}"
            )
            report_content.append("}")
            report_content.append("---" * 50)
            report_content.append(f"Total Tool (YES) vs Agent (NO): {confusion_df.loc['success', 'no']}")
            report_content.append(f"Total Tool (NO) vs Agent (YES): {confusion_df.loc['failure', 'yes']}")
            report_content.append("---" * 50)
            report_content.append(f"Total Test Repair Agent Errors: {len(test_repair_error)}")
            report_content.append(f"Total Verdict Agent Errors: {len(verdict_error)}")
            report_content.append(f"Timeout Cases: {project_timeout_count}")
            report_content.append("---" * 50)
            report_content.append(f"Total turns: {total_num_turns} [Average: {total_num_turns / total_methods:.2f}]")
            report_content.append(f"Total cost: ${total_cost:.2f} [Average: ${total_cost / total_methods:.2f}]")
            report_content.append(
                f"Total time: {total_time // 1e3}s [Average: {total_time // 1e3 / total_methods:.2f}s]"
            )
            report_content.append(
                f"Total tool calls: {total_tool_calls} [Average: {total_tool_calls / total_methods:.2f}]"
            )
            report_content.append("---" * 50)
            report_content.append("Confusion Matrix:")
            report_content.append(confusion_df.to_string())
            report_content.append("---" * 50)
            report_content.append("Disagreements:")
            report_content.extend(disagreements)
            report_content.append("---" * 50)

            # Write the report to a .txt file
            report_file_path = os.path.join(report_dir, args.agent_name, tool, f"{project.split('.')[0]}.txt")
            with open(report_file_path, "w") as report_file:
                report_file.write("\n".join(report_content))

            if args.reset_incomplete:
                reset_incomplete_responses(test_repair_error, verdict_error, result_file)

            # Accumulate global metrics
            global_total += total
            global_total_methods += total_methods
            for key in global_tool_validation_dist:
                global_tool_validation_dist[key] += tool_validation_dist[key]
            for key in global_equivalency_dist:
                global_equivalency_dist[key] += equivalency_dist[key]
            global_total_num_turns += total_num_turns
            global_total_cost += total_cost
            global_total_time += total_time
            global_total_tool_calls += total_tool_calls

            # Accumulate global error counts
            global_test_repair_errors += len(test_repair_error)
            global_verdict_errors += len(verdict_error)

            # Accumulate global timeout count
            global_timeout_count += project_timeout_count

    # Calculate global metrics
    global_total_methods = max(global_total_methods, 1)  # Avoid division by zero
    global_error_rate = (global_test_repair_errors + global_verdict_errors) / global_total_methods
    global_timeout_percentage = (global_timeout_count / global_total_methods) * 100

    print("MatchFixAgent: {")
    print(
        f"    yes:   {{ total: {global_equivalency_dist['yes']}, %: {global_equivalency_dist['yes'] / global_total_methods:.2%} }},"
    )
    print(
        f"    no:    {{ total: {global_equivalency_dist['no']}, %: {global_equivalency_dist['no'] / global_total_methods:.2%} }},"
    )
    print(
        f"    other: {{ total: {global_equivalency_dist['other']}, %: {global_equivalency_dist['other'] / global_total_methods:.2%} }}"
    )
    print("}")
    print("Tool: {")
    print(
        f"    success:       {{ total: {global_tool_validation_dist['success']}, %: {global_tool_validation_dist['success'] / global_total_methods:.2%} }},"
    )
    print(
        f"    failure:       {{ total: {global_tool_validation_dist['failure']}, %: {global_tool_validation_dist['failure'] / global_total_methods:.2%} }},"
    )
    print(
        f"    not-exercised: {{ total: {global_tool_validation_dist['not-exercised']}, %: {global_tool_validation_dist['not-exercised'] / global_total_methods:.2%} }},"
    )
    print(
        f"    pending:       {{ total: {global_tool_validation_dist['pending']}, %: {global_tool_validation_dist['pending'] / global_total_methods:.2%} }},"
    )
    print(
        f"    error:         {{ total: {global_tool_validation_dist['error']}, %: {global_tool_validation_dist['error'] / global_total_methods:.2%} }}"
    )
    print("}")
    print()
    print(
        f"Total Methods: {global_equivalency_dist['yes'] + global_equivalency_dist['no'] + global_equivalency_dist['other']} [{global_total_methods / global_total:.2%}]"
    )
    print(f"Total turns: {global_total_num_turns} [Average: {global_total_num_turns / global_total_methods:.2f}]")
    print(f"Total cost: ${global_total_cost:.2f} [Average: ${global_total_cost / global_total_methods:.2f}]")
    print(f"Total time: {global_total_time // 1e3}s [Average: {global_total_time // 1e3 / global_total_methods:.2f}s]")
    print(
        f"Total tool calls: {global_total_tool_calls} [Average: {global_total_tool_calls / global_total_methods:.2f}]"
    )
    print(
        f"API Error Rate: {global_error_rate:.2%} [Test Repair Errors: {global_test_repair_errors}, Verdict Errors: {global_verdict_errors}]"
    )
    print(f"Global Timeout Cases: {global_timeout_count} [{global_timeout_percentage:.2f}%]")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Analyze Agent Results")
    parser.add_argument("--agent_name", type=str, dest="agent_name", help="name of the agent to analyze")
    parser.add_argument(
        "--reset_incomplete", action="store_true", dest="reset_incomplete", help="reset incomplete responses"
    )
    args = parser.parse_args()
    main(args)
