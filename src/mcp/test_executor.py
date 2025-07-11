from fastmcp import FastMCP
import os
import json
import subprocess
from pathlib import Path

mcp = FastMCP(name="TestExecutor")


def get_oxidizer_test_command(project: str) -> str:
    if not os.path.exists(f"memory/{project}.json"):
        return "cargo test unit_test"

    fragment_id = json.load(open(f"memory/{project}.json"))["id"]

    fragments = []
    with open(f"data/tool_results/oxidizer/processed_results/{project}.json", "r") as f:
        fragments = json.load(f)

    for fragment in fragments:
        if fragment["id"] == fragment_id and fragment["test_name"]:
            return f"cargo test {fragment['test_name']}"

    return "cargo test unit_test"


@mcp.tool
def execute_rust_tests(project: str) -> str:
    """Execute Rust tests for a specified translated project.

    This tool runs test commands for Rust projects that have been translated
    from other languages. Each project may have different test execution
    commands based on their build system and test setup. The tool also supports
    custom test commands for specific projects and allows skipping certain tests
    using predefined skip flags.

    Args:
        project (str): The name of the project to test. Supported projects
                      include "iceberg", "deltachat-core", "incubator-milagro-crypto",
                      "libp2p", "charset-normalizer", "checkdigit", "go-edlib",
                      "gohistogram", "gonameparts", "stats", and "TextRank".

    Returns:
        str: The output from the test execution, including both stdout and stderr.
             Returns error messages if the project directory doesn't exist,
             if the test command fails to execute, or if an unexpected error occurs.

    Raises:
        No exceptions are raised directly. All errors are caught and
        returned as formatted error messages in the output string.

    Example:
        >>> execute_rust_tests("iceberg")
        Running tests for project: iceberg
        Test command: make unit-test

        test result: ok. 15 passed; 0 failed; 0 ignored; 0 measured; 0 filtered out

    Note:
        - Each project has its own directory path and test command configuration.
        - Test execution happens in the project's specific Rust directory.
        - Both successful and failed test results are captured.
        - Some projects have specific tests that are skipped using --skip flags.
        - For projects like "checkdigit", "go-edlib", "gohistogram", "gonameparts",
          "stats", and "TextRank", the test command is dynamically determined
          using the `get_oxidizer_test_command` function.
        - Environment variables such as `RUST_LOG` are set to control logging levels.
        - A timeout of 5 minutes is enforced for test execution to prevent hanging.
    """

    # Define project-specific test commands
    PROJECT_COMMANDS = {
        "iceberg": "make unit-test",
        "deltachat-core": "cargo nextest run",
        "incubator-milagro-crypto": "cargo test --all --all-features --release",
        "libp2p": "cargo test",
        "charset-normalizer": "cargo test",
        "checkdigit": "cargo test unit_test",
        "go-edlib": "cargo test unit_test",
        "gohistogram": "cargo test unit_test",
        "gonameparts": "cargo test unit_test",
        "stats": "cargo test unit_test",
        "TextRank": "cargo test unit_test",
    }

    PROJECTS_PATHS = {
        "iceberg": Path("data/tool_projects/rustrepotrans/projects/iceberg/rust"),
        "deltachat-core": Path("data/tool_projects/rustrepotrans/projects/deltachat-core/rust"),
        "incubator-milagro-crypto": Path("data/tool_projects/rustrepotrans/projects/incubator-milagro-crypto/rust"),
        "libp2p": Path("data/tool_projects/rustrepotrans/projects/libp2p/rust"),
        "charset-normalizer": Path("data/tool_projects/rustrepotrans/projects/charset-normalizer/rust"),
        "checkdigit": Path("data/tool_projects/oxidizer/projects/checkdigit/rust"),
        "go-edlib": Path("data/tool_projects/oxidizer/projects/go-edlib/rust"),
        "gohistogram": Path("data/tool_projects/oxidizer/projects/gohistogram/rust"),
        "gonameparts": Path("data/tool_projects/oxidizer/projects/gonameparts/rust"),
        "stats": Path("data/tool_projects/oxidizer/projects/stats/rust"),
        "TextRank": Path("data/tool_projects/oxidizer/projects/TextRank/rust"),
    }

    SKIP_TESTS = {
        "libp2p": [
            "basic_resolve",  # this test reqires IPv6 support
            "given_periodic_bootstrap_when_routing_table_updated_then_wont_bootstrap_until_next_interval",  # this test is flaky
        ]
    }

    # Validate project
    if project not in PROJECT_COMMANDS:
        available_projects = ", ".join(PROJECT_COMMANDS.keys())
        return f"Error: Unknown project '{project}'. Available projects: {available_projects}"

    # Get project directory path from PROJECTS_PATHS
    project_dir = PROJECTS_PATHS[project]

    # Check if project directory exists
    if not project_dir.exists():
        return f"Error: Project directory '{project_dir}' does not exist"

    if not project_dir.is_dir():
        return f"Error: Path '{project_dir}' is not a directory"

    # Get the test command for this project
    test_command = PROJECT_COMMANDS[project]

    if project in ["checkdigit", "go-edlib", "gohistogram", "gonameparts", "stats", "TextRank"]:
        test_command = get_oxidizer_test_command(project)

    # Add skip flags if there are tests to skip for this project
    if project in SKIP_TESTS:
        skip_flags = " ".join([f"--skip {test}" for test in SKIP_TESTS[project]])
        test_command = f"{test_command} -- {skip_flags}"

    try:
        # Change to project directory and execute the test command
        env = os.environ.copy()
        env["RUST_LOG"] = "error"

        result = subprocess.run(
            test_command,
            shell=True,
            cwd=str(project_dir),
            capture_output=True,
            text=True,
            timeout=300,  # 5 minute timeout
            env=env,
        )

        stdout = result.stdout
        stderr = result.stderr

        if project == "deltachat-core" and stdout.strip() == "" and result.returncode == 0:
            stdout = stderr or "All tests passed"

        # Format the output
        output_lines = [
            f"Running tests for project: {project}",
            f"Test command: {test_command}",
            f"Working directory: {project_dir}",
            f"Exit code: {result.returncode}",
            "",
            "=== STDOUT ===",
            stdout if stdout else "(no stdout output)",
            "",
            "=== STDERR ===",
            stderr if stderr and result.returncode != 0 else "(no stderr output)",
        ]

        return "\n".join(output_lines)

    except subprocess.TimeoutExpired:
        return f"Error: Test execution timed out after 5 minutes for project '{project}'"
    except subprocess.SubprocessError as e:
        return f"Error: Failed to execute test command '{test_command}' for project '{project}': {str(e)}"
    except Exception as e:
        return f"Error: Unexpected error while running tests for project '{project}': {str(e)}"


if __name__ == "__main__":
    mcp.run(transport="sse", port=8001)
