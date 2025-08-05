#!/usr/bin/env python3

import os
import re
import argparse
from pathlib import Path
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)


def find_test_sections(content):
    """Find test sections in Rust code."""
    test_sections = []

    # Keep track of section positions to detect overlaps
    positions = []

    # Find all #[cfg(test)] mod patterns in the file, including ones with multiple cfg attributes
    cfg_test_pattern = re.compile(r"#\[cfg\(test\)\]\s*(?:#\[cfg\([^\)]+\)\]\s*)*mod\s+([a-zA-Z0-9_]+)\s*\{", re.DOTALL)
    for match in cfg_test_pattern.finditer(content):
        start_pos = match.start()
        # Now find the closing brace for this module using a proper brace counter
        opening_brace_pos = content.find("{", start_pos)
        if opening_brace_pos != -1:
            brace_count = 1
            pos = opening_brace_pos + 1

            while brace_count > 0 and pos < len(content):
                if content[pos] == "{":
                    brace_count += 1
                elif content[pos] == "}":
                    brace_count -= 1
                pos += 1

            # Even if we didn't find the closing brace (brace_count > 0),
            # we still include what we found up to the end of the content
            end_pos = pos if brace_count == 0 else len(content)
            test_module = content[start_pos:end_pos]
            test_sections.append(test_module)
            positions.append((start_pos, end_pos))

    # If direct approach fails, continue with other strategies:

    # Also handle external test modules with #[cfg(test)] mod module_name;
    external_test_pattern = re.compile(
        r"#\[cfg\(test\)\]\s*(?:#\[cfg\([^\)]+\)\]\s*)*mod\s+([a-zA-Z0-9_]+)\b\s*;", re.DOTALL
    )

    # Handle modules where cfg(test) is the second attribute
    reversed_cfg_pattern = re.compile(r"#\[cfg\([^\)]+\)\]\s*#\[cfg\(test\)\]\s*mod\s+([a-zA-Z0-9_]+)\s*\{", re.DOTALL)

    # Handle the specific case in transport.rs with #[cfg(test)] followed by #[cfg(any(...))]
    specific_test_pattern = re.compile(
        r"#\[cfg\(test\)\]\s*#\[cfg\(any\([^\)]+\)\)\]\s*mod\s+([a-zA-Z0-9_]+)\s*\{", re.DOTALL
    )
    for match in external_test_pattern.finditer(content):
        test_sections.append(content[match.start() : match.end()])
        positions.append((match.start(), match.end()))

    # Process modules where cfg(test) is the second attribute
    for match in reversed_cfg_pattern.finditer(content):
        start_pos = match.start()
        # Now find the closing brace for this module using a proper brace counter
        opening_brace_pos = content.find("{", start_pos)
        if opening_brace_pos != -1:
            brace_count = 1
            pos = opening_brace_pos + 1

            while brace_count > 0 and pos < len(content):
                if content[pos] == "{":
                    brace_count += 1
                elif content[pos] == "}":
                    brace_count -= 1
                pos += 1

            # Even if we didn't find the closing brace (brace_count > 0),
            # we still include what we found up to the end of the content
            end_pos = pos if brace_count == 0 else len(content)
            test_module = content[start_pos:end_pos]
            test_sections.append(test_module)
            positions.append((start_pos, end_pos))

    # Process the specific test pattern
    for match in specific_test_pattern.finditer(content):
        start_pos = match.start()
        # Now find the closing brace for this module using a proper brace counter
        opening_brace_pos = content.find("{", start_pos)
        if opening_brace_pos != -1:
            brace_count = 1
            pos = opening_brace_pos + 1

            while brace_count > 0 and pos < len(content):
                if content[pos] == "{":
                    brace_count += 1
                elif content[pos] == "}":
                    brace_count -= 1
                pos += 1

            # Even if we didn't find the closing brace (brace_count > 0),
            # we still include what we found up to the end of the content
            end_pos = pos if brace_count == 0 else len(content)
            test_module = content[start_pos:end_pos]
            test_sections.append(test_module)
            positions.append((start_pos, end_pos))

    # Handle inner attribute test modules #![cfg(test)] inside mod module_name { ... }
    inner_test_pattern = re.compile(
        r"mod\s+([a-zA-Z0-9_]+)\b\s*\{[\s\n]*#!\[cfg\(test\)\]",
        re.DOTALL,
    )
    for match in inner_test_pattern.finditer(content):
        start_pos = match.start()
        opening_brace_pos = content.find("{", start_pos)
        if opening_brace_pos == -1:
            continue

        # Find the matching closing brace with proper nesting
        brace_count = 1
        pos = opening_brace_pos + 1

        while brace_count > 0 and pos < len(content):
            if content[pos] == "{":
                brace_count += 1
            elif content[pos] == "}":
                brace_count -= 1
            pos += 1

        # Even if we didn't find the closing brace, include what we found
        end_pos = pos if brace_count == 0 else len(content)
        test_sections.append(content[start_pos:end_pos])
        positions.append((start_pos, end_pos))

    # This section was removed as it's a duplicate of the previous section

    # Find all #[test], #[tokio::test] and #[async_std::test] attributes
    i = 0
    while i < len(content):
        # Look for #[test], #[tokio::test] or #[async_std::test] pattern
        match = re.search(r"#\[(test|tokio::test|async_std::test)\]", content[i:])
        if not match:
            break

        start_pos = i + match.start()

        # Find the function that follows the test attribute
        fn_match = re.search(r"fn\s+([a-zA-Z0-9_]+)", content[start_pos:])
        if not fn_match:
            i = start_pos + len(match.group(0))
            continue

        fn_pos = start_pos + fn_match.start()
        fn_name = fn_match.group(1)

        # Find the opening brace of the function
        opening_brace_match = re.search(r"\{", content[fn_pos:])
        if not opening_brace_match:
            i = fn_pos + len(fn_name)
            continue

        opening_brace_pos = fn_pos + opening_brace_match.start()

        # Find the matching closing brace with proper nesting
        brace_count = 1
        pos = opening_brace_pos + 1

        while brace_count > 0 and pos < len(content):
            if content[pos] == "{":
                brace_count += 1
            elif content[pos] == "}":
                brace_count -= 1
            pos += 1

        # Even if we didn't find the closing brace, include what we found
        end_pos = pos if brace_count == 0 else len(content)
        test_fn_section = content[start_pos:end_pos]
        test_sections.append(test_fn_section)
        positions.append((start_pos, end_pos))
        i = end_pos

    # Special case: Handle nested #[cfg(test)] modules
    # These are modules within other modules but with their own #[cfg(test)] attribute
    nested_test_pattern = re.compile(
        r"[^#]mod\s+[a-zA-Z0-9_]+\s*\{[\s\S]*?#\[cfg\(test\)\]\s*(?:#\[cfg\([^\)]+\)\]\s*)*mod\s+([a-zA-Z0-9_]+)\s*\{",
        re.DOTALL,
    )
    for match in nested_test_pattern.finditer(content):
        # Find the position of the nested #[cfg(test)] attribute
        cfg_test_pos = content.rfind("#[cfg(test)]", 0, match.end())
        if cfg_test_pos == -1:
            continue

        start_pos = cfg_test_pos
        # Find the opening brace position for the test module
        opening_brace_pos = content.find("{", start_pos)
        if opening_brace_pos == -1:
            continue

        # Find the matching closing brace with proper nesting
        brace_count = 1
        pos = opening_brace_pos + 1

        while brace_count > 0 and pos < len(content):
            if content[pos] == "{":
                brace_count += 1
            elif content[pos] == "}":
                brace_count -= 1
            pos += 1

        # Even if we didn't find the closing brace, include what we found
        end_pos = pos if brace_count == 0 else len(content)
        test_module = content[start_pos:end_pos]

        # Check if this section overlaps with any existing ones
        overlaps = False
        for s_pos, e_pos in positions:
            # Skip if this is a subsection of an already identified section
            if s_pos <= start_pos and e_pos >= end_pos:
                overlaps = True
                break

        if not overlaps:
            test_sections.append(test_module)
            positions.append((start_pos, end_pos))

    return test_sections, positions


def remove_test_sections(file_path, dry_run=False):
    """Remove test sections from a Rust file."""
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            content = file.read()
    except UnicodeDecodeError:
        # Try with a different encoding if utf-8 fails
        with open(file_path, "r", encoding="latin-1") as file:
            content = file.read()

    # Find test sections
    test_sections, positions = find_test_sections(content)

    if not test_sections:
        logger.info(f"No test sections found in {file_path}")
        return

    logger.info(f"Found {len(test_sections)} test sections in {file_path}")

    # Handle special case for cfg(test) patterns that might be incomplete
    cfg_test_pattern = re.compile(r"#\[cfg\(test\)\]\s*(?:#\[cfg\([^\)]+\)\]\s*)*mod\s+([a-zA-Z0-9_]+)\b")
    for match in cfg_test_pattern.finditer(content):
        start_pos = match.start()
        # Check if this pattern is already handled in previous sections
        already_handled = False
        for s_pos, e_pos in positions:
            if s_pos <= start_pos < e_pos:
                already_handled = True
                break

        if not already_handled:
            logger.info(f"Found incomplete test module at position {start_pos}")
            # Include everything from the match to the end of file or to the next potential module
            end_pos = len(content)
            # Look for closing brace or next module
            brace_pos = content.find("}", start_pos)
            if brace_pos != -1:
                end_pos = brace_pos + 1
            test_sections.append(content[start_pos:end_pos])
            positions.append((start_pos, end_pos))

    if dry_run:
        for i, section in enumerate(test_sections):
            # Only print a summary for each section to avoid overwhelming output
            preview = section[:100] + "..." if len(section) > 100 else section
            logger.info(f"Would remove section {i+1}: {preview}")
        return

    # Sort sections by length in descending order to handle nested sections properly
    test_sections.sort(key=len, reverse=True)

    # Remove test sections
    modified_content = content

    # First handle the entire test modules (both with single cfg and multiple cfg attributes)
    # Check for any section that has #[cfg(test)] anywhere within the first few lines
    def has_cfg_test(section):
        lines = section.strip().split("\n", 3)  # Check only in the first few lines
        section_start = "\n".join(lines[: min(3, len(lines))])
        return section_start.startswith("#[cfg(test)]") or re.search(r"#\[cfg\(test\)\]", section_start) is not None

    for section in [s for s in test_sections if has_cfg_test(s)]:
        modified_content = modified_content.replace(section, "")
    # Then handle any remaining individual test functions
    for section in [
        s
        for s in test_sections
        if (
            s.strip().startswith("#[test]")
            or s.strip().startswith("#[tokio::test]")
            or s.strip().startswith("#[async_std::test]")
        )
    ]:
        modified_content = modified_content.replace(section, "")

    # Clean up any empty lines caused by removing test sections
    modified_content = re.sub(r"\n\s*\n\s*\n", "\n\n", modified_content)

    # Only remove unnecessary empty blocks, do not touch semicolons
    modified_content = re.sub(r"\{\s*\n\s*\}", "{}", modified_content)

    # Write the modified content back to the file
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(modified_content)

    logger.info(f"Removed {len(test_sections)} test sections from {file_path}")


def process_directory(directory, pattern="**/*.rs", dry_run=False):
    """Process all Rust files in the given directory."""
    path = Path(directory)

    # Check if the path is a file or directory
    if path.is_file():
        try:
            logger.info(f"Processing single file {path}")
            remove_test_sections(path, dry_run)
        except Exception as e:
            logger.error(f"Error processing {path}: {e}")
        return

    # Process directory
    rust_files = list(path.glob(pattern))

    logger.info(f"Found {len(rust_files)} Rust files in {directory}")

    for file_path in rust_files:
        try:
            logger.info(f"Processing {file_path}")
            remove_test_sections(file_path, dry_run)
        except Exception as e:
            logger.error(f"Error processing {file_path}: {e}")


def main():
    parser = argparse.ArgumentParser(description="Remove test sections from Rust files")
    parser.add_argument("directory", help="Directory containing Rust files")
    parser.add_argument("--pattern", default="**/*.rs", help="Glob pattern for finding Rust files")
    parser.add_argument(
        "--dry-run", action="store_true", help="Don't actually modify files, just report what would be removed"
    )

    args = parser.parse_args()

    process_directory(args.directory, args.pattern, args.dry_run)


if __name__ == "__main__":
    main()
