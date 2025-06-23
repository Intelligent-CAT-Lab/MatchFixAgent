import os
import json


def main():

    results_path = "data/tool_results/alphatrans/raw_results/gpt-4o-2024-11-20/body/0.0"
    output_path = "data/tool_results/alphatrans/processed_results"
    os.makedirs(output_path, exist_ok=True)

    for project in os.listdir(results_path):
        project_results = []
        for schema_file in os.listdir(f"{results_path}/{project}"):

            if "src.main" not in schema_file:
                continue

            schema_data = {}
            with open(f"{results_path}/{project}/{schema_file}", "r") as f:
                schema_data = json.load(f)

            formatted_schema_file = schema_file.replace(".json", "")

            for class_ in schema_data["classes"]:

                if "new" in class_ or "{" in class_:  # skip nested and nameless classes
                    continue

                for method_ in schema_data["classes"][class_]["methods"]:

                    if schema_data["classes"][class_]["methods"][method_]["is_overload"]:
                        continue

                    source_code = "".join(schema_data["classes"][class_]["methods"][method_]["body"])
                    target_code = "\n".join(schema_data["classes"][class_]["methods"][method_]["translation"])

                    validation_result = ""
                    if isinstance(schema_data["classes"][class_]["methods"][method_]["graal_validation"], str):
                        validation_result = schema_data["classes"][class_]["methods"][method_]["graal_validation"]
                    elif isinstance(schema_data["classes"][class_]["methods"][method_]["graal_validation"], dict):
                        validation_result = schema_data["classes"][class_]["methods"][method_]["graal_validation"][
                            "outcome"
                        ]
                    else:
                        raise ValueError(
                            f"Unexpected type for graal_validation: {type(schema_data['classes'][class_]['methods'][method_]['graal_validation'])}"
                        )

                    assert validation_result != ""
                    assert isinstance(validation_result, str)

                    file_path = formatted_schema_file.replace(".", "/").replace("_python_partial", "")

                    results = {}
                    results["project"] = project
                    results["source_path"] = file_path.replace("src/main/", "src/main/java/") + ".java"
                    results["target_path"] = file_path + ".py"
                    results["source_function"] = source_code.split("\n")
                    results["target_function"] = target_code.split("\n")
                    results["ground_truth_target_function"] = ""
                    results["source_language"] = "java"
                    results["target_language"] = "python"
                    results["result"] = validation_result

                    project_results.append(results)

        with open(f"{output_path}/{project}.json", "w") as f:
            json.dump(project_results, f, indent=4)


if __name__ == "__main__":
    main()
