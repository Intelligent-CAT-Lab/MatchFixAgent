from __future__ import annotations
import re
import sys
import os
import unittest
import pytest
import io
import typing
from typing import *
from src.main.org.fusesource.jansi.Ansi import *
from src.main.org.fusesource.jansi.AnsiConsole import *


class AnsiConsoleExample2:

    @staticmethod
    def main(args: typing.List[str]) -> None:
        file = "src/test/resources/jansi.ans"
        if len(args) > 0:
            file = args[0]

        # Allows us to disable ANSI processing.
        if os.getenv("jansi", "true") == "true":
            AnsiConsole.systemInstall()

        print(Ansi.ansi0().reset().eraseScreen0().cursor(1, 1), end="")
        print("=======================================================================")

        with open(file, "rb") as f:
            while chunk := f.read(1):
                sys.stdout.buffer.write(chunk)

        print("=======================================================================")

    def __init__(self) -> None:
        pass
