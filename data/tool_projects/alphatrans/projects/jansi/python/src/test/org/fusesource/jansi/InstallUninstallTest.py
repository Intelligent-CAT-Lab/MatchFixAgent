from __future__ import annotations
import re
import sys
import unittest
import pytest
import io
import typing
from typing import *
from src.main.org.fusesource.jansi.Ansi import *
from src.main.org.fusesource.jansi.AnsiConsole import *
from src.main.org.fusesource.jansi.AnsiMode import *
from src.main.org.fusesource.jansi.AnsiPrintStream import *


class InstallUninstallTest:

    @staticmethod
    def main(args: typing.List[typing.List[str]]) -> None:
        InstallUninstallTest.__print_(sys.stdout, "Lorem ipsum")
        InstallUninstallTest.__print_(sys.stderr, "dolor sit amet")
        AnsiMode.systemInstall()
        InstallUninstallTest.__print_(sys.stdout, "consectetur adipiscing elit")
        InstallUninstallTest.__print_(sys.stderr, "sed do eiusmod")
        AnsiMode.out().setMode(AnsiMode.Strip)
        AnsiMode.err().setMode(AnsiMode.Strip)
        InstallUninstallTest.__print_(sys.stdout, "tempor incididunt ut")
        InstallUninstallTest.__print_(sys.stderr, "labore et dolore")
        AnsiMode.systemUninstall()
        InstallUninstallTest.__print_(sys.stdout, "magna aliqua.")
        InstallUninstallTest.__print_(sys.stderr, "Ut enim ad ")

    @staticmethod
    def __print_(stream: typing.IO, text: str) -> None:
        half = len(text) // 2
        stream.write(text[:half])
        stream.write(
            Ansi.ansi0().fg0(Ansi.Color.GREEN).a1(text[half:]).reset().__str__()
        )
