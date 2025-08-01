import os
import argparse
import random
import json


def main(args):
    args.agent_name = "match_agent"

    positive_pool = {}
    negative_pool = {}
    for tool in os.listdir(os.path.join("data", "agent_results", args.agent_name)):
        for project in os.listdir(os.path.join("data", "agent_results", args.agent_name, tool)):

            if tool == "alphatrans" and project.split(".")[0] not in [
                "commons-cli",
                "commons-csv",
                "commons-fileupload",
                "commons-validator",
            ]:
                continue

            result_file = os.path.join("data", "agent_results", args.agent_name, tool, project)
            with open(result_file, "r") as file:
                data = json.load(file)

            for item in data:

                positive_pool.setdefault(item["project"], {})
                negative_pool.setdefault(item["project"], {})

                language_pair = item["source_language"] + "-" + item["target_language"]

                positive_pool[item["project"]].setdefault(language_pair, {"success": [], "failure": []})
                negative_pool[item["project"]].setdefault(language_pair, {"success": [], "failure": []})

                if args.agent_name not in item:
                    continue

                if item[args.agent_name]["output"]["test_repair"]["parsed_final_response"]["is_equivalent"] not in [
                    "yes",
                    "no",
                ]:
                    continue

                if item["result"] == "success":
                    positive_pool[item["project"]][language_pair]["success"].append(
                        [
                            item["id"],
                            item["project"],
                            tool,
                        ]
                    )

                if item["result"] == "failure":
                    negative_pool[item["project"]][language_pair]["failure"].append(
                        [
                            item["id"],
                            item["project"],
                            tool,
                        ]
                    )

    pool = []
    for project in positive_pool:
        for lang_pair in positive_pool[project]:
            pos_items = positive_pool[project][lang_pair]["success"]
            neg_items = negative_pool[project][lang_pair]["failure"]

            sampled = []

            if len(pos_items) >= 2 and len(neg_items) >= 2:
                sampled.extend(random.sample(pos_items, 2))
                sampled.extend(random.sample(neg_items, 2))
            elif len(pos_items) >= 4:
                sampled.extend(random.sample(pos_items, 4))
            elif len(neg_items) >= 4:
                sampled.extend(random.sample(neg_items, 4))
            else:
                # if not enough items in either category to sample full amount, sample as many as possible
                sampled.extend(random.sample(pos_items, min(4, len(pos_items))))
                sampled.extend(random.sample(neg_items, min(4 - len(sampled), len(neg_items))))

            for item in sampled:
                item_id, item_project, item_tool = item
                outcome = "success" if item in pos_items else "failure"
                pool.append([item_id, item_project, item_tool, lang_pair, outcome])

    # truncate to exactly 100 samples if more
    if len(pool) > 100:
        pool = random.sample(pool, 100)
    elif len(pool) < 100:
        raise ValueError(f"Only {len(pool)} samples collected. Need 100.")

    project_counts = {}
    for item in pool:
        project = item[1]
        language_pair = item[3]
        outcome = item[4]
        project_counts.setdefault(project, {})
        project_counts[project].setdefault(language_pair, {"success": 0, "failure": 0})
        project_counts[project][language_pair][outcome] += 1

    print(f"Total number of items in the pool: {len(pool)}")
    print("Number of items in the pool per project:")
    for project, count in project_counts.items():
        print(f"{project}: {count}")

    os.makedirs("data/samples", exist_ok=True)
    with open("data/samples/openai_study.json", "w") as file:
        json.dump(pool, file, indent=4)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Sample instances for experiment with OpenAI.")
    args = parser.parse_args()
    main(args)
