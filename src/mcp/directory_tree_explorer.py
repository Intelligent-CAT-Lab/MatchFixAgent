from fastmcp import FastMCP

mcp = FastMCP(name="DirectoryTreeExplorer")


@mcp.tool
def get_directory_tree(path: str, print_dirs_only: bool) -> str:
    """Generate a visual tree representation of a directory structure.

    This tool recursively traverses the specified directory and creates
    a hierarchical tree view using ASCII characters. The output shows
    files and subdirectories in a visually organized format similar
    to the Unix 'tree' command.

    Args:
        path (str): The file system path to the directory to analyze.
                   Can be relative or absolute path. The path will be
                   converted to absolute path internally.
        print_dirs_only (bool): If True, only directories will be shown
                               in the tree structure, files will be excluded.
                               This parameter is required.

    Returns:
        str: A formatted string containing the directory tree structure
             using ASCII art characters (├──, └──, │). Returns an error
             message if the path doesn't exist, isn't a directory, or
             access is denied.

    Raises:
        No exceptions are raised directly. All errors are caught and
        returned as formatted error messages in the output string.

    Example:
        >>> get_directory_tree("/home/user/project")
        project/
        ├── README.md
        ├── src/
        │   ├── main.py
        │   └── utils/
        │       └── helpers.py
        └── tests/
            └── test_main.py

        >>> get_directory_tree("/home/user/project", print_dirs_only=True)
        project/
        ├── src/
        │   └── utils/
        └── tests/

    Note:
        - Directories are traversed recursively
        - Items are sorted alphabetically for consistent output
        - Permission errors are handled gracefully
        - Hidden files and directories (starting with '.') are excluded from output
        - When print_dirs_only=True, only directories are shown in the tree
    """
    import os

    def generate_tree(directory, prefix="", is_last=True):
        """Recursively generate tree structure."""
        if not os.path.exists(directory):
            return f"Error: Path '{directory}' does not exist"

        if not os.path.isdir(directory):
            return f"Error: Path '{directory}' is not a directory"

        tree_lines = []

        try:
            # Get all items in the directory
            items = sorted(os.listdir(directory))
            # Filter out hidden directories (starting with '.')
            items = [item for item in items if not item.startswith(".")]

            # Filter to only directories if print_dirs_only is True
            if print_dirs_only:
                items = [item for item in items if os.path.isdir(os.path.join(directory, item))]

            for i, item in enumerate(items):
                item_path = os.path.join(directory, item)
                is_last_item = i == len(items) - 1

                # Create the tree symbols
                current_prefix = "└── " if is_last_item else "├── "
                tree_lines.append(f"{prefix}{current_prefix}{item}")

                # If it's a directory, recursively add its contents
                if os.path.isdir(item_path):
                    extension_prefix = "    " if is_last_item else "│   "
                    subtree = generate_tree(item_path, prefix + extension_prefix, is_last_item)
                    if subtree:  # Only add if there's content
                        tree_lines.append(subtree)

        except PermissionError:
            tree_lines.append(f"{prefix}[Permission Denied]")
        except Exception as e:
            tree_lines.append(f"{prefix}[Error: {str(e)}]")

        return "\n".join(tree_lines)

    # Get the absolute path and directory name
    abs_path = os.path.abspath(path)
    dir_name = os.path.basename(abs_path)

    # Start the tree with the root directory
    result = f"{dir_name}/\n"
    tree_content = generate_tree(abs_path)

    if tree_content and not tree_content.startswith("Error:"):
        result += tree_content
    else:
        result = tree_content  # Return error message directly

    return result


if __name__ == "__main__":
    mcp.run(transport="stdio")
