from __future__ import annotations
import re
import sys
import os
import unittest
import pytest
import io
import typing
from typing import *
from src.main.org.fusesource.jansi.AnsiConsole import *


class AnsiConsoleExample:

    @staticmethod
    def main(args: typing.List[str]) -> None:
        file = "src/test/resources/jansi.ans"
        if len(args) > 0:
            file = args[0]

        # Allows us to disable ANSI processing.
        if os.getenv("jansi", "true") == "true":
            AnsiConsole.systemInstall()

        with open(file, "rb") as f:
            while c := f.read(1):
                sys.stdout.buffer.write(c)

    def __init__(self) -> None:
        raise NotImplementedError("This class cannot be instantiated.")
