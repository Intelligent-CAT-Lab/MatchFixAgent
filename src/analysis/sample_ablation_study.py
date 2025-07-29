import os
import argparse
import json


def main(args):
    args.agent_name = "match_agent"

    pool = []
    for tool in os.listdir(os.path.join("data", "agent_results", args.agent_name)):
        for project in os.listdir(os.path.join("data", "agent_results", args.agent_name, tool)):

            result_file = os.path.join("data", "agent_results", args.agent_name, tool, project)
            with open(result_file, "r") as file:
                data = json.load(file)

            for item in data:

                if args.agent_name not in item:
                    continue

                if item[args.agent_name]["output"]["test_repair"]["parsed_final_response"]["is_equivalent"] not in ["yes", "no"]:
                    continue

                if item[args.agent_name]["output"]["test_repair"]["parsed_final_response"]["is_equivalent"] == "yes" and item["result"] == "success":                    
                    pool.append([
                        item["id"],
                        item["project"],
                        tool,
                    ])

                if item[args.agent_name]["output"]["test_repair"]["parsed_final_response"]["is_equivalent"] == "no" and item["result"] == "failure":
                    pool.append([
                        item["id"],
                        item["project"],
                        tool,
                    ])

    project_counts = {}
    for item in pool:
        project = item[1]
        if project not in project_counts:
            project_counts[project] = 0
        project_counts[project] += 1
        
    print(f"Total number of items in the pool: {len(pool)}")
    print("Number of items in the pool per project:")
    for project, count in project_counts.items():
        print(f"{project}: {count}")
    
    os.makedirs("data/ablation_study", exist_ok=True)
    with open("data/ablation_study/pool.json", "w") as file:
        json.dump(pool, file, indent=4)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Sample ablation study for MatchFixAgent performance.")
    args = parser.parse_args()
    main(args)
