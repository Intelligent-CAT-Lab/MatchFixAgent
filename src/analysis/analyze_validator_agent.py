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
    results_file = os.path.join(args.results_dir, f"{args.project_name}.json")

    with open(results_file, "r") as file:
        data = json.load(file)

    total = 0
    total_methods = 0
    tool_validation_dist = {"error": 0, "failure": 0, "not-exercised": 0, "pending": 0, "success": 0}
    equivalency_dist = {"yes": 0, "no": 0, "need_more_context": 0}
    total_num_turns = 0
    total_cost = 0
    total_time = 0
    total_tool_calls = 0

    # Define possible outcomes
    tool_outcomes = ["error", "failure", "not-exercised", "pending", "success"]
    llm_outcomes = ["yes", "no", "need_more_context"]

    # Initialize confusion matrix with zeros
    confusion_df = pd.DataFrame(0, index=tool_outcomes, columns=llm_outcomes)

    for schema_name in data:
        for class_name in data[schema_name]:
            for method_name in data[schema_name][class_name]:

                total += 1

                if args.agent_name not in data[schema_name][class_name][method_name]:
                    continue

                if not data[schema_name][class_name][method_name][args.agent_name]["status"]:
                    continue

                total_methods += 1

                # Get tool validation outcome
                tool_validation = data[schema_name][class_name][method_name]["graal_validation"]

                # Get LLM prediction
                llm_prediction = data[schema_name][class_name][method_name][args.agent_name]["output"][
                    "parsed_final_response"
                ]["is_equivalent"]

                # Update confusion matrix
                confusion_df.loc[tool_validation, llm_prediction] += 1

                # Continue with your existing stats collection
                tool_validation_dist[tool_validation] += 1
                equivalency_dist[llm_prediction] += 1
                total_num_turns += data[schema_name][class_name][method_name][args.agent_name]["output"]["num_turns"]
                total_cost += data[schema_name][class_name][method_name][args.agent_name]["output"]["total_cost"]
                total_time += data[schema_name][class_name][method_name][args.agent_name]["output"]["duration_ms"]

                # Load and analyze agent trajectory files
                session_id = data[schema_name][class_name][method_name][args.agent_name]["output"]["session_id"]
                trajectory_file = os.path.join(args.trajectory_dir, f"{session_id}.jsonl")
                assert os.path.exists(
                    trajectory_file
                ), f"Trajectory file {trajectory_file} does not exist. Please check the session ID."

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
                            total_tool_calls += 1

    # Verify data consistency
    assert total_methods == sum(
        equivalency_dist.values()
    ), "Total methods do not match the sum of equivalency distribution"

    # Print statistics
    print(f"---" * 50)
    print(f"Project: {args.project_name}")
    print(f"Agent: {args.agent_name}")
    print(f"Progress: {total_methods}/{total} [{total_methods / total:.2%}]")
    last_modified_time = os.path.getmtime(results_file)
    seconds_ago = time.time() - last_modified_time
    print(
        f"Results file last modified: {seconds_ago // 3600}h, {(seconds_ago % 3600) // 60}m, {seconds_ago % 60:.2f}s ago"
    )
    print(f"Total methods: {total_methods}")
    print(
        f"Agent Equivalency Dist: [yes: {equivalency_dist['yes']} ({equivalency_dist['yes'] / total_methods:.2%}), "
        f"no: {equivalency_dist['no']} ({equivalency_dist['no'] / total_methods:.2%}), "
        f"need_more_context: {equivalency_dist['need_more_context']} ({equivalency_dist['need_more_context'] / total_methods:.2%})]"
    )
    print(
        f"Tool Success Dist: {tool_validation_dist['success'] / total_methods:.2%} [Improvement: {equivalency_dist['yes'] / total_methods:.2%} - {tool_validation_dist['success'] / total_methods:.2%} = {equivalency_dist['yes'] / total_methods - tool_validation_dist['success'] / total_methods:.2%}]"
    )
    print()
    print(f"Total turns: {total_num_turns} [Average: {total_num_turns / total_methods:.2f}]")
    print(f"Total cost: ${total_cost:.2f} [Average: ${total_cost / total_methods:.2f}]")
    print(f"Total time: {total_time // 1e3}s [Average: {total_time // 1e3 / total_methods:.2f}s]")
    print(f"Total tool calls: {total_tool_calls} [Average: {total_tool_calls / total_methods:.2f}]")

    # Print confusion matrix
    print("\nConfusion Matrix:")
    print(confusion_df)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Analyze Validator Agent")
    parser.add_argument("--project_name", type=str, dest="project_name", help="project name to translate")
    parser.add_argument("--results_dir", type=str, dest="results_dir", help="directory to results")
    parser.add_argument("--trajectory_dir", type=str, dest="trajectory_dir", help="directory to trajectories")
    parser.add_argument("--agent_name", type=str, dest="agent_name", help="name of the agent to analyze")
    args = parser.parse_args()
    main(args)
