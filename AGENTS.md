# Test Generation and Execution
- It is IMPORTANT to execute your generated tests in both languages to verify correctness. DO NOT give your response until you have executed the tests in both languages and captured the output.
- When generating tests, YOU MUST only create standalone files in <target_fragment_path> as provided in the initial prompt. DO NOT create global tests in other modules/packages/directories.
- For Rust tests, make sure you execute tests using `cargo test`.
- For Python tests, make sure you execute tests using `python -m unittest` or `pytest`.
- For Java tests, make sure you execute tests using `mvn clean test -Drat.skip`.
- For JavaScript tests, make sure you execute tests using `node`.
- For Go tests, make sure you execute tests using `go`.
- For C tests, make sure you compile and run tests using `gcc`.
- To fix the <target_fragment_method>, YOU MUST make edits in-place in the file given in <target_fragment_path>.

# MCP Servers

- Use the available function `get_directory_tree(path: str, print_dirs_only: bool) -> str` from DirectoryTreeExplorer server to get more context about files and directory structure. This will help you understand where files are located and where to store your generated test files.
- When calling the `get_directory_tree(path: str, print_dirs_only: bool) -> str` function from DirectoryTreeExplorer, make sure first you call it with `print_dirs_only=True` as sometimes high-level directories (e.g., directories higher in the path) can produce very large tree structures. You can call low-level directories (e.g., directories lower in th path) with `print_dirs_only=False` to see their files as their tree structure is relatively shorter.

# TODO list for Test Generation and Repair Agent

- You must always follow the following TODO when running the test generation and repair agent:
  - Read the source file to understand context. The path is given in the initial prompt.
  - Read the target file to understand context. The path is given in the initial prompt.
  - Call the `get_directory_tree(path: str, print_dirs_only: bool) -> str` with a proper path to understand the directory structure and available files in both source and target projects.
  - After understanding the project structure, generate test files in both source and target projects and determine where to store them.
  - Execute tests in both source and target projects and verify results. Your tests should exercise the same behavior. Your goal is to expose bugs in target fragment, if any.
  - If tests in both source and target projects are passing, provide your final response by calling `export_test_repair_agent_response(is_equivalent: str, explanation: str, source_test_file_implementation: str, source_test_execution_outcome: str, target_test_file_implementation: str, target_test_execution_outcome: str, correct_target_method_implementation: str = "")`. This will format your response like the expected <final_response_format>.
  - If tests in target project are failing, make necessary fixes to target fragment if needed. Execute target tests again to verify your patch is working. Keep going until you fix the target fragment.
  - Provide your response by calling `export_test_repair_agent_response(is_equivalent: str, explanation: str, source_test_file_implementation: str, source_test_execution_outcome: str, target_test_file_implementation: str, target_test_execution_outcome: str, correct_target_method_implementation: str = "")`. This will format your response like the expected <final_response_format>.
  - Terminate as soon as possible.

# TODO list for Verdict Agent

- You must always follow the following TODO when running the verdict agent:
  - Consider all semantic analysis results.
  - Consider test generation and repair analysis results (give more attention to these).
  - To the best of your knowledge, determine the functional equivalency between source and target fragments.
  - Provide your response by calling `export_verdict_agent_response(is_equivalent: str, confidence_level: str, explanation: str) -> str`. This will format your response like the expected <final_response_format>.
  - Terminate as soon as possible.