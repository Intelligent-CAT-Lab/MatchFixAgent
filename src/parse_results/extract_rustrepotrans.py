import os
import re
import json


def parse_translation_blocks(text: str, project: str) -> dict:
    target_path = None
    target_func = None
    source_path = None
    source_func = None

    # Find all <path> and <function> pairs
    path_blocks = re.findall(r"<path>\n?(.*?)\s*</path>", text, re.DOTALL)
    func_blocks = re.findall(r"<function>\n?(.*?)\s*</function>", text, re.DOTALL)

    # Determine which path is Rust and which is Python
    for path, func in zip(path_blocks, func_blocks):

        # if first line of func has four spaces, remove the first four space from all func lines
        if func.startswith("    "):
            func = "\n".join(line[4:] for line in func.split("\n"))
        # replace \t with four spaces
        func = func.replace("\t", "    ")

        if path.endswith(".rs"):
            target_path = path
            target_func = func.split("\n")
        else:
            source_path = path
            source_func = func.split("\n")

    return {
        "project": project,
        "source_path": source_path,
        "target_path": target_path,
        "source_function": source_func,
        "ground_truth_target_function": target_func,
    }


def extract_translation(text: str) -> str:
    """
    Extracts the translation from the given text.
    Assumes the translation is enclosed in <translated function> tags.
    """
    match = re.search(r"<translated function>(.*?)</translated function>", text, re.DOTALL)
    if match:
        return match.group(1).strip()
    return None


def extract_code_block(text: str) -> str:
    """
    Extracts the code block from the given text.
    Assumes the code block is enclosed in triple backticks (```).
    """
    text = text.replace("```rust", "```")
    match = re.search(r"```(.*?)```", text, re.DOTALL)
    if match:
        return match.group(1).strip()
    return None


def extract_rust_function(text: str) -> str:
    """
    Extracts the Rust function from the
    """
    match = re.search(r"(pub fn.*?{.*?})", text, re.DOTALL)
    code = match.group(1).strip() if match else None
    return code


def main():
    raw_results_path = "data/tool_results/rustrepotrans/raw_results"
    ground_truth_dir = f"{raw_results_path}/function_pair_with_identical_functionality"
    output_path = "data/tool_results/rustrepotrans/processed_results"
    os.makedirs(output_path, exist_ok=True)

    for project in os.listdir(ground_truth_dir):
        project_results = []
        project_path = os.path.join(ground_truth_dir, project)
        for language_pair in os.listdir(project_path):
            language_pair_path = os.path.join(project_path, language_pair)
            target_language, source_language = language_pair.split("__")
            for function_pair in os.listdir(language_pair_path):
                function_pair_path = os.path.join(language_pair_path, function_pair)

                content = ""
                with open(function_pair_path, "r", encoding="latin1") as f:
                    content = f.read()

                parsed = parse_translation_blocks(content, project)

                parsed["source_language"] = source_language
                parsed["target_language"] = target_language

                translation_file = os.path.join(
                    f"{raw_results_path}/rq1/translate_result/translate_by_claude/{project}/{language_pair}/{function_pair}"
                )
                assert os.path.exists(translation_file), f"Translation file does not exist: {translation_file}"

                result_file = os.path.join(
                    f"{raw_results_path}/rq1/test_result/translate_by_claude/{project}/{language_pair}/{function_pair}"
                )
                assert os.path.exists(result_file), f"Result file does not exist: {result_file}"

                result_file_content = ""
                with open(result_file, "r", encoding="latin1") as f:
                    result_file_content = f.read()

                if result_file_content.strip().startswith("Success"):
                    parsed["result"] = "success"
                else:
                    parsed["result"] = "failure"

                translation_file_content = ""
                with open(translation_file, "r", encoding="latin1") as f:
                    translation_file_content = f.read()

                translation_file_content = extract_translation(translation_file_content)

                assert len(translation_file_content) > 0, f"Translation file is empty: {translation_file}"

                target_function = ""

                if "```" not in translation_file_content:
                    rust_function = extract_rust_function(translation_file_content)
                    if rust_function:
                        target_function = rust_function
                    else:
                        # annotate for manual review
                        target_function = "[FIXTHIS]" + translation_file_content.strip()
                else:
                    translated_function = extract_code_block(translation_file_content)
                    if translated_function:
                        target_function = translated_function
                    else:
                        target_function = None

                if target_function is None:
                    print(f"Warning: No target function found in {translation_file}. Annotate for manual review.")
                    target_function = "[FIXTHIS] No target function found so delete this string manually."
                    parsed["result"] = "pending"

                parsed["target_function"] = target_function.split("\n")
                parsed = {
                    "id": str(len(project_results) + 1),
                    "project": parsed["project"],
                    "source_path": parsed["source_path"],
                    "target_path": parsed["target_path"],
                    "source_function": parsed["source_function"],
                    "target_function": parsed["target_function"],
                    "ground_truth_target_function": parsed["ground_truth_target_function"],
                    "source_language": parsed["source_language"],
                    "target_language": parsed["target_language"],
                    "result": parsed["result"],
                }

                project_results.append(parsed)

        with open(os.path.join(output_path, f"{project}.json"), "w") as f:
            json.dump(project_results, f, indent=4)


if __name__ == "__main__":
    main()
