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
import random
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
    copy_trajectory_file(session_id, "data/agent_trajectories/claude")

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


def reset_incomplete_responses(test_repair_error, verdict_error, project_timeout, result_file):
    """
    Reset incomplete responses by removing them from the results file.

    This function takes lists of test repair and verdict errors, and removes
    these entries from the results JSON file to ensure that they do not affect
    future analyses.

    Args:
        test_repair_error (list): List of IDs with test repair errors.
        verdict_error (list): List of IDs with verdict errors.
    """
    with open(result_file, "r") as file:
        data = json.load(file)

    for item in data:
        if args.agent_name not in item:
            continue
        if item["id"] in test_repair_error or item["id"] in verdict_error or item["id"] in project_timeout:
            if args.agent_name in item:
                del item[args.agent_name]

    with open(result_file, "w") as file:
        json.dump(data, file, indent=4)


def reset_disagreements(disagreement_ids, result_file):
    """
    Reset disagreements by removing entries from the results file.

    This function takes a list of disagreement IDs and removes these entries
    from the results JSON file to ensure that they do not affect future analyses.

    Args:
        disagreement_ids (list): List of IDs with disagreements.
        result_file (str): Path to the results JSON file.
    """
    with open(result_file, "r") as file:
        data = json.load(file)

    for item in data:
        if args.agent_name not in item:
            continue
        if item["id"] in disagreement_ids:
            if args.agent_name in item:
                del item[args.agent_name]

    with open(result_file, "w") as file:
        json.dump(data, file, indent=4)


def reset_timeouts(project_timeout, result_file):
    """
    Reset timeout cases by removing entries from the results file.

    This function takes a list of project timeout IDs and removes these entries
    from the results JSON file to ensure that they do not affect future analyses.

    Args:
        project_timeout (list): List of IDs with timeout cases.
        result_file (str): Path to the results JSON file.
    """
    with open(result_file, "r") as file:
        data = json.load(file)

    for item in data:
        if args.agent_name not in item:
            continue
        if item["id"] in project_timeout:
            if args.agent_name in item:
                del item[args.agent_name]

    with open(result_file, "w") as file:
        json.dump(data, file, indent=4)


def plot_confusion_matrix(semantic_analyzer_alignment):
    """Generate publication-quality confusion matrix visualization for semantic analyzer alignment."""
    import matplotlib.pyplot as plt
    import seaborn as sns
    from sklearn.metrics import confusion_matrix
    import numpy as np

    # Set publication-quality styling
    plt.style.use("default")  # Reset to clean default style
    plt.rcParams.update(
        {
            "font.family": "serif",
            "font.serif": ["Times New Roman", "Times", "Liberation Serif", "DejaVu Serif", "serif"],
            "font.size": 12,
            "axes.linewidth": 1.2,
            "axes.spines.top": False,
            "axes.spines.right": False,
            "xtick.direction": "out",
            "ytick.direction": "out",
            "xtick.major.size": 6,
            "ytick.major.size": 6,
            "xtick.minor.size": 3,
            "ytick.minor.size": 3,
            "legend.frameon": False,
            "figure.dpi": 300,
            "savefig.dpi": 300,
            "savefig.bbox": "tight",
            "savefig.pad_inches": 0.1,
        }
    )

    # Create figure with optimal size for publication
    fig, axes = plt.subplots(2, 3, figsize=(14, 8))
    fig.patch.set_facecolor("white")

    # Define tools and improved titles
    tools = ["cfg", "dfg", "io", "api", "error", "spec"]
    subfigure_titles = [
        "Control Flow",
        "Data Flow Path",
        "Input/Output Mapping",
        "Library API Equivalence",
        "Exception/Error Handling",
        "Specifications",
    ]

    # Custom colormap for better contrast and readability
    custom_cmap = sns.light_palette("seagreen", as_cmap=True)

    for i, tool in enumerate(tools):
        ax = axes[i // 3, i % 3]

        if not semantic_analyzer_alignment[tool]:
            # Handle empty data gracefully
            ax.text(
                0.5,
                0.5,
                "No Data Available",
                horizontalalignment="center",
                verticalalignment="center",
                transform=ax.transAxes,
                fontsize=14,
                style="italic",
                bbox=dict(boxstyle="round,pad=0.3", facecolor="lightgray", alpha=0.5),
            )
            ax.set_xticks([])
            ax.set_yticks([])
            ax.set_title(f"{subfigure_titles[i]}", fontsize=16, fontweight="bold", pad=20)
            continue

        y_true = [x[0] for x in semantic_analyzer_alignment[tool]]
        y_pred = [x[1] for x in semantic_analyzer_alignment[tool]]
        cm = confusion_matrix(y_true, y_pred, labels=["yes", "no", "other"])

        # Calculate percentages for better interpretation
        cm_percent = cm.astype("float") / cm.sum(axis=1)[:, np.newaxis] * 100

        # Create annotations with both counts and percentages
        annot_text = np.empty_like(cm, dtype=object)
        for row in range(cm.shape[0]):
            for col in range(cm.shape[1]):
                count = cm[row, col]
                percent = cm_percent[row, col] if not np.isnan(cm_percent[row, col]) else 0
                annot_text[row, col] = f"{count}\n({percent:.1f}%)"

        # Create heatmap with enhanced styling
        sns.heatmap(
            cm,
            annot=annot_text,
            fmt="",
            cmap=custom_cmap,
            ax=ax,
            cbar=True,
            square=True,
            linewidths=0.5,
            linecolor="white",
            xticklabels=["Yes", "No", "Other"],
            yticklabels=["Yes", "No", "Other"],
            annot_kws={"size": 12, "fontweight": "bold", "color": "black", "fontfamily": "monospace"},
            cbar_kws={"shrink": 0.8, "aspect": 20},
            vmin=0,
            vmax=1500,
        )

        # Enhanced title with better positioning
        ax.set_title(f"{subfigure_titles[i]}", fontsize=16, fontweight="bold", pad=10)

        # Improved axis labels
        ax.set_xlabel("MatchFixAgent", fontsize=14, fontweight="medium", labelpad=2)
        ax.set_ylabel("Semantic Analyzer", fontsize=14, fontweight="medium", labelpad=2)

        # Rotate tick labels for better readability
        ax.tick_params(axis="x", rotation=0, labelsize=12)
        ax.tick_params(axis="y", rotation=0, labelsize=12)

        # Add subtle grid for better readability
        ax.grid(False)  # Remove default grid

        # Ensure tick labels use proper font
        for label in ax.get_xticklabels():
            label.set_fontfamily("serif")
            label.set_fontweight("medium")
        for label in ax.get_yticklabels():
            label.set_fontfamily("serif")
            label.set_fontweight("medium")

    # Optimize layout with professional spacing
    plt.tight_layout(rect=[0, 0.03, 1, 0.94])
    plt.subplots_adjust(hspace=0.35, wspace=0.35)

    plt.savefig("interpretability.pdf", dpi=300, bbox_inches="tight", facecolor="white", edgecolor="none")


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
    global_equivalency_dist = {"yes": 0, "no": 0, "other": 0, "error": 0}
    global_total_num_turns = 0
    global_total_cost = 0
    global_total_time = 0
    global_total_tool_calls = 0
    global_timeout_count = 0

    # Initialize global error counts
    global_test_repair_errors = 0
    global_verdict_errors = 0
    global_disagreements = {}

    # ablation study
    semantic_analyzer_alignment = {"cfg": [], "dfg": [], "io": [], "spec": [], "error": [], "api": []}

    project_language_map = {}
    for tool in ["alphatrans", "oxidizer", "skel", "rustrepotrans"]:
        for project in os.listdir(os.path.join("data", "agent_results", args.agent_name, tool)):
            project_name = project.split(".")[0]
            project_language_map.setdefault(project_name, [])

            result_file = os.path.join("data", "agent_results", args.agent_name, tool, project)
            with open(result_file, "r") as file:
                data = json.load(file)

            for item in data:
                source_language = item.get("source_language", "unknown")
                target_language = item.get("target_language", "unknown")
                if [source_language, target_language] not in project_language_map[project_name]:
                    project_language_map[project_name].append([source_language, target_language])

    for tool in ["alphatrans", "oxidizer", "skel", "rustrepotrans"]:
        if args.tool_name and tool != args.tool_name:
            continue
        for project in os.listdir(os.path.join("data", "agent_results", args.agent_name, tool)):

            # skipped for now
            if tool == "alphatrans" and project.split(".")[0] in [
                "jansi",
                "JavaFastPFOR",
                "commons-codec",
                "commons-graph",
                "commons-exec",
                "commons-pool",
            ]:
                continue

            if args.project_name and project.split(".")[0] != args.project_name:
                continue

            for source_language, target_language in project_language_map[project.split(".")[0]]:

                os.makedirs(os.path.join(report_dir, args.agent_name, tool), exist_ok=True)

                result_file = os.path.join("data", "agent_results", args.agent_name, tool, project)
                with open(result_file, "r") as file:
                    data = json.load(file)

                total = 0
                total_methods = 0
                tool_validation_dist = {"error": 0, "failure": 0, "not-exercised": 0, "pending": 0, "success": 0}
                equivalency_dist = {"yes": 0, "no": 0, "other": 0, "error": 0}
                total_num_turns = 0
                total_cost = 0
                total_time = 0
                total_tool_calls = 0
                total_newly_covered_fragments = 0

                # incomplete responses
                test_repair_error = []
                verdict_error = []

                disagreements = []
                disagreement_ids = []

                # Count timeout cases for the project
                project_timeout_count = []

                # Define possible outcomes
                tool_outcomes = ["error", "failure", "not-exercised", "pending", "success"]
                llm_outcomes = ["yes", "no", "other", "error"]

                # Initialize confusion matrix with zeros
                confusion_df = pd.DataFrame(0, index=tool_outcomes, columns=llm_outcomes)

                for item in data:

                    if item.get("source_language") != source_language or item.get("target_language") != target_language:
                        continue

                    total += 1

                    if args.agent_name not in item:
                        continue

                    # if not item[args.agent_name]["status"]:
                    #     continue

                    agent_output = item[args.agent_name]["output"]
                    if args.agent_name in ["match_agent", "openai_agent"]:
                        if item[args.agent_name]["output"]["test_repair"]["parsed_final_response"]["is_equivalent"] in [
                            "error",
                            "other",
                        ]:
                            agent_output = item[args.agent_name]["output"]["verdict"]
                        else:
                            agent_output = item[args.agent_name]["output"]["test_repair"]

                    total_methods += 1

                    # Get tool validation outcome
                    tool_validation = item["result"]

                    # Get LLM prediction
                    llm_prediction = agent_output["parsed_final_response"]["is_equivalent"]

                    if args.agent_name in ["match_agent", "openai_agent"]:
                        semantic_analyzer_alignment["cfg"].append(
                            [
                                item[args.agent_name]["output"]["semantic_analyzer_analyses"]["control_flow"][
                                    "parsed_final_response"
                                ]["is_equivalent"],
                                llm_prediction,
                            ]
                        )
                        semantic_analyzer_alignment["dfg"].append(
                            [
                                item[args.agent_name]["output"]["semantic_analyzer_analyses"]["data_flow"][
                                    "parsed_final_response"
                                ]["is_equivalent"],
                                llm_prediction,
                            ]
                        )
                        semantic_analyzer_alignment["io"].append(
                            [
                                item[args.agent_name]["output"]["semantic_analyzer_analyses"]["io"][
                                    "parsed_final_response"
                                ]["is_equivalent"],
                                llm_prediction,
                            ]
                        )
                        semantic_analyzer_alignment["spec"].append(
                            [
                                item[args.agent_name]["output"]["semantic_analyzer_analyses"]["spec"][
                                    "parsed_final_response"
                                ]["is_equivalent"],
                                llm_prediction,
                            ]
                        )
                        semantic_analyzer_alignment["error"].append(
                            [
                                item[args.agent_name]["output"]["semantic_analyzer_analyses"]["exception_error"][
                                    "parsed_final_response"
                                ]["is_equivalent"],
                                llm_prediction,
                            ]
                        )
                        semantic_analyzer_alignment["api"].append(
                            [
                                item[args.agent_name]["output"]["semantic_analyzer_analyses"]["library_equivalence"][
                                    "parsed_final_response"
                                ]["is_equivalent"],
                                llm_prediction,
                            ]
                        )

                        if (
                            item[args.agent_name]["output"]["test_repair"]["parsed_final_response"]["is_equivalent"]
                            == "error"
                        ):
                            test_repair_error.append(item["id"])

                        if (
                            item[args.agent_name]["output"]["verdict"]["parsed_final_response"]["is_equivalent"]
                            == "error"
                        ):
                            verdict_error.append(item["id"])

                        # Check for timeout cases
                        if (
                            item[args.agent_name]["output"]["test_repair"]["parsed_final_response"].get("is_equivalent")
                            == "other"
                            and item[args.agent_name]["output"]["test_repair"]["parsed_final_response"].get(
                                "explanation"
                            )
                            == "500: timeout"
                        ):
                            project_timeout_count.append(item["id"])

                        if (
                            item[args.agent_name]["output"]["verdict"]["parsed_final_response"].get("is_equivalent")
                            == "other"
                            and item[args.agent_name]["output"]["verdict"]["parsed_final_response"].get("explanation")
                            == "500: timeout"
                        ):
                            project_timeout_count.append(item["id"])
                    else:
                        if agent_output["parsed_final_response"]["is_equivalent"] == "error":
                            verdict_error.append(item["id"])

                        if (
                            agent_output["parsed_final_response"].get("is_equivalent") == "other"
                            and agent_output["parsed_final_response"].get("explanation") == "500: timeout"
                        ):
                            project_timeout_count.append(item["id"])

                    global_disagreements.setdefault(tool, {})
                    global_disagreements[tool].setdefault(project.split(".")[0], {})
                    global_disagreements[tool][project.split(".")[0]].setdefault(
                        source_language, {target_language: {"D1": [], "D2": []}}
                    )

                    if tool_validation == "success" and llm_prediction == "no":
                        disagreements.append(f"Tool (YES) vs Agent (NO): ID - {item['id']}")
                        disagreement_ids.append(item["id"])
                        global_disagreements[tool][project.split(".")[0]][source_language][target_language][
                            "D1"
                        ].append(item["id"])

                    if tool_validation == "failure" and llm_prediction == "yes":
                        disagreements.append(f"Tool (NO) vs Agent (YES): ID - {item['id']}")
                        disagreement_ids.append(item["id"])
                        global_disagreements[tool][project.split(".")[0]][source_language][target_language][
                            "D2"
                        ].append(item["id"])

                    if tool_validation in ["not-exercised", "pending"] and item[args.agent_name]["output"][
                        "test_repair"
                    ]["parsed_final_response"]["is_equivalent"] in ["yes", "no"]:
                        total_newly_covered_fragments += 1

                    # Update confusion matrix
                    confusion_df.loc[tool_validation, llm_prediction] += 1

                    # Continue with your existing stats collection
                    tool_validation_dist[tool_validation] += 1
                    equivalency_dist[llm_prediction] += 1

                    if args.agent_name == "match_agent":
                        test_repair_agent = item[args.agent_name]["output"]["test_repair"]
                        verdict_agent = item[args.agent_name]["output"]["verdict"]

                        test_repair_cost = get_agent_cost(test_repair_agent)
                        verdict_cost = get_agent_cost(verdict_agent)

                        total_num_turns += test_repair_cost["total_num_turns"] + verdict_cost["total_num_turns"]
                        total_cost += test_repair_cost["total_cost_usd"] + verdict_cost["total_cost_usd"]
                        total_time += test_repair_cost["duration_ms"] + verdict_cost["duration_ms"]
                        total_tool_calls += test_repair_cost["num_tool_calls"] + verdict_cost["num_tool_calls"]
                    elif args.agent_name == "base_agent":
                        agent_cost = get_agent_cost(agent_output)
                        total_num_turns += agent_cost["total_num_turns"]
                        total_cost += agent_cost["total_cost_usd"]
                        total_time += agent_cost["duration_ms"]
                        total_tool_calls += agent_cost["num_tool_calls"]
                    else:  # skip cost calculation for openai_agent because the returned JSONs have limited information
                        continue

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
                report_content.append(
                    f"    error: {{ total: {equivalency_dist['error']}, %: {equivalency_dist['error'] / total_methods:.2%} }}"
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
                report_content.append(f"Timeout Cases: {len(project_timeout_count)}")
                report_content.append("---" * 50)
                report_content.append(f"Total newly covered fragments: {total_newly_covered_fragments}")
                report_content.append(
                    f"Confusion Matrix Accuracy (Success + Failure): {confusion_df.loc['success', 'yes'] + confusion_df.loc['failure', 'no']}/{total_methods} [{(confusion_df.loc['success', 'yes'] + confusion_df.loc['failure', 'no']) / total_methods:.2%}]"
                )
                report_content.append("---" * 50)
                report_content.append(
                    f"Total turns: {total_num_turns} [Average: {total_num_turns / total_methods:.2f}]"
                )
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
                report_file_path = os.path.join(
                    report_dir,
                    args.agent_name,
                    tool,
                    f"{source_language}_{target_language}_{project.split('.')[0]}.txt",
                )
                with open(report_file_path, "w") as report_file:
                    report_file.write("\n".join(report_content))

                if args.reset_incomplete:
                    reset_incomplete_responses(test_repair_error, verdict_error, project_timeout_count, result_file)

                if args.reset_disagreements:
                    reset_disagreements(disagreement_ids, result_file)

                if args.reset_timeouts:
                    reset_timeouts(project_timeout_count, result_file)

                # Accumulate global metrics
                global_total += total
                global_total_methods += total_methods
                for key in global_tool_validation_dist:
                    global_tool_validation_dist[key] += tool_validation_dist[key]
                for key in global_equivalency_dist:
                    global_equivalency_dist[key] += equivalency_dist[key]
                global_total_num_turns += total_num_turns
                global_total_cost += total_cost
                global_total_time += total_time // 1e3
                global_total_tool_calls += total_tool_calls

                # Accumulate global error counts
                global_test_repair_errors += len(test_repair_error)
                global_verdict_errors += len(verdict_error)

                # Accumulate global timeout count
                global_timeout_count += len(project_timeout_count)

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
    print(
        f"    error: {{ total: {global_equivalency_dist['error']}, %: {global_equivalency_dist['error'] / global_total_methods:.2%} }}"
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
        f"Total Methods: {global_equivalency_dist['yes'] + global_equivalency_dist['no'] + global_equivalency_dist['other'] + global_equivalency_dist['error']} [{global_total_methods / global_total:.2%}]"
    )
    print(f"Total turns: {global_total_num_turns} [Average: {global_total_num_turns / global_total_methods:.2f}]")
    print(f"Total cost: ${global_total_cost:.2f} [Average: ${global_total_cost / global_total_methods:.2f}]")
    print(f"Total time: {global_total_time}s [Average: {global_total_time / global_total_methods:.2f}s]")
    print(
        f"Total tool calls: {global_total_tool_calls} [Average: {global_total_tool_calls / global_total_methods:.2f}]"
    )
    print(
        f"API Error Rate: {global_error_rate:.2%} [Test Repair Errors: {global_test_repair_errors}, Verdict Errors: {global_verdict_errors}]"
    )
    print(f"Global Timeout Cases: {global_timeout_count} [{global_timeout_percentage:.2f}%]")

    sampled = []
    for tool, projects in global_disagreements.items():
        for project, languages in projects.items():
            for source_language, targets in languages.items():
                for target_language, ids in targets.items():
                    # sample 5 IDs from D1 and D2 independently. If there are less than 5, take all
                    ids["D1"] = random.sample(ids["D1"], min(5, len(ids["D1"])))
                    ids["D2"] = random.sample(ids["D2"], min(5, len(ids["D2"])))
                    if not ids["D1"] and not ids["D2"]:
                        continue
                    for id in ids["D1"]:
                        sampled.append(f"{tool},{project},{source_language},{target_language},{id},D1")
                    for id in ids["D2"]:
                        sampled.append(f"{tool},{project},{source_language},{target_language},{id},D2")

    with open(f"reports/{args.agent_name}/disagreements.txt", "w") as f:
        f.writelines("\n".join(sampled))

    plot_confusion_matrix(semantic_analyzer_alignment)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Analyze Agent Results")
    parser.add_argument("--agent_name", type=str, dest="agent_name", help="name of the agent to analyze")
    parser.add_argument(
        "--tool_name",
        type=str,
        dest="tool_name",
        help="name of the tool to analyze (e.g., alphatrans, oxidizer, skel, rustrepotrans)",
    )
    parser.add_argument("--project_name", type=str, dest="project_name", help="name of the project to analyze")
    parser.add_argument(
        "--reset_incomplete", action="store_true", dest="reset_incomplete", help="reset incomplete responses"
    )
    parser.add_argument(
        "--reset_disagreements", action="store_true", dest="reset_disagreements", help="reset disagreements"
    )
    parser.add_argument("--reset_timeouts", action="store_true", dest="reset_timeouts", help="reset timeout cases")
    args = parser.parse_args()
    main(args)
