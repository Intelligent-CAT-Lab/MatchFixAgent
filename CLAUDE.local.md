# Test Generation and Execution
- It is IMPORTANT to execute your generated tests in both languages to verify correctness. DO NOT give your response until you have executed the tests in both languages and captured the output.
- When generating tests, YOU MUST only create standalone files in <target_fragment_path> as provided in the initial prompt. DO NOT create global tests in other modules/packages/directories.
- For Rust tests, make sure you execute tests using `cargo test --all-features`.
- For Python tests, make sure you execute tests using `python -m unittest` or `pytest`.
- To fix the <target_fragment_method>, YOU MUST make edits in-place in the file given in <target_fragment_path>.