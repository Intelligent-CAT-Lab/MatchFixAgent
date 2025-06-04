import os

from tree_sitter import Language
from pathlib import Path

cwd = Path(__file__).resolve().parent.absolute()

if not (cwd / "vendor/tree-sitter-java/grammar.js").exists():
    os.system(
        f'git clone https://github.com/tree-sitter/tree-sitter-java.git {cwd / "vendor/tree-sitter-java"}'
    )

if not (cwd / "vendor/tree-sitter-python/grammar.js").exists():
    os.system(
        f'git clone https://github.com/tree-sitter/tree-sitter-python.git {cwd / "vendor/tree-sitter-python"}'
    )

Language.build_library(
    # Store the library in the `build` directory
    str(cwd / "build/my-languages.so"),
    
    # Include one or more languages
    [
        str(cwd / "vendor/tree-sitter-java"),
        str(cwd / "vendor/tree-sitter-python"),
    ],
)
