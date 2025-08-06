from fastmcp import FastMCP
import json

mcp = FastMCP(name="ResponseFormatter")


@mcp.tool
def export_test_repair_agent_response(
    is_equivalent: str,
    explanation: str,
    source_test_file_implementation: str,
    source_test_execution_outcome: str,
    target_test_file_implementation: str,
    target_test_execution_outcome: str,
    correct_target_method_implementation: str = "",
) -> str:
    """Format and export the response from the test generation and repair agent.

    This tool takes individual parameters from the test generation and repair agent and formats them
    according to the expected response format by the user.

    The source_test_file_implementation and target_test_file_implementation MUST be syntactically correct
    and test the same functionality in the source and target languages, respectively.

    If the target fragment is equivalent to the source fragment, the target_test_file_implementation
    should pass on the target fragment. If the target fragment is not equivalent, the
    target_test_file_implementation should fail on the target fragment, and the
    correct_target_method_implementation should contain the corrected implementation.

    Args:
        is_equivalent: "yes", "no", or "other"
        explanation: Detailed explanation of the analysis
        source_test_file_implementation: Implementation of the test file in the source language which passes on the source fragment
        source_test_execution_outcome: Output from executing the test in the source language on the source fragment
        target_test_file_implementation: Implementation of the test file in the target language which passes on the target fragment,
                                        if the target fragment is equivalent to the source fragment, otherwise, it fails on the
                                        target fragment.
        target_test_execution_outcome: Output from executing the test in the target language on the target fragment
        correct_target_method_implementation: Corrected implementation if not equivalent (optional)

    Returns:
        str: A formatted string containing the response in the expected format wrapped in
             <final_response_format> tags.

    Example:
        >>> export_test_repair_agent_response(
        ...     is_equivalent="yes",
        ...     explanation="Both implementations provide the same functionality",
        ...     source_test_file_implementation="test code...",
        ...     source_test_execution_outcome="test output...",
        ...     target_test_file_implementation="test code...",
        ...     target_test_execution_outcome="test output..."
        ... )
        Use the following formatted response as your result and terminate:
        <final_response_format>
        {
          "is_equivalent": "yes",
          "explanation": "Both implementations provide the same functionality",
          "source_test_file_implementation": "test code...",
          "source_test_execution_outcome": "test output...",
          "target_test_file_implementation": "test code...",
          "target_test_execution_outcome": "test output...",
          "correct_target_method_implementation": ""
        }
        </final_response_format>
    """

    try:
        # Create a dictionary with the input parameters
        response_data = {
            "is_equivalent": is_equivalent,
            "explanation": explanation,
            "source_test_file_implementation": source_test_file_implementation,
            "source_test_execution_outcome": source_test_execution_outcome,
            "target_test_file_implementation": target_test_file_implementation,
            "target_test_execution_outcome": target_test_execution_outcome,
            "correct_target_method_implementation": correct_target_method_implementation,
        }

        # Format the JSON response with proper indentation
        formatted_response = json.dumps(response_data, indent=2)

        # Wrap the formatted response in the expected tags
        final_response = f"Use the following formatted response as your result and terminate:\n<final_response_format>\n{formatted_response}\n</final_response_format>"

        return final_response

    except Exception as e:
        return f"Error: Unexpected error while formatting test repair agent response: {str(e)}"


@mcp.tool
def export_verdict_agent_response(is_equivalent: str, confidence_level: str, explanation: str) -> str:
    """Format and export the response from the verdict agent.

    This tool takes individual parameters from the verdict agent and formats them
    according to the expected response format by the user. You can provide the
    output of this tool to the user as the final verdict on the equivalence
    of the source and target implementations.

    Args:
        is_equivalent: "yes", "no", or "other"
        confidence_level: "high", "medium", or "low"
        explanation: Detailed explanation synthesizing all agent perspectives

    Returns:
        str: A formatted string containing the response in the expected format wrapped in
             <final_response_format> tags.

    Example:
        >>> export_verdict_agent_response(
        ...     is_equivalent="yes",
        ...     confidence_level="high",
        ...     explanation="All analyses confirm functional equivalence"
        ... )
        Use the following formatted response as your result and terminate:
        <final_response_format>
        {
          "is_equivalent": "yes",
          "confidence_level": "high",
          "explanation": "All analyses confirm functional equivalence"
        }
        </final_response_format>
    """

    try:
        # Create a dictionary with the input parameters
        response_data = {
            "is_equivalent": is_equivalent,
            "confidence_level": confidence_level,
            "explanation": explanation,
        }

        # Format the JSON response with proper indentation
        formatted_response = json.dumps(response_data, indent=2)

        # Wrap the formatted response in the expected tags
        final_response = f"Use the following formatted response as your result and terminate:\n<final_response_format>\n{formatted_response}\n</final_response_format>"

        return final_response

    except Exception as e:
        return f"Error: Unexpected error while formatting verdict agent response: {str(e)}"


if __name__ == "__main__":
    mcp.run(transport="stdio")
