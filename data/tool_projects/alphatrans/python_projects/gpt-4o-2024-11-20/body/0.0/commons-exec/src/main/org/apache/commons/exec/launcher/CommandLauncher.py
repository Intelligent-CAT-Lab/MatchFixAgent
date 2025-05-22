from __future__ import annotations
import re
from abc import ABC
import pathlib
import io
import typing
from typing import *
from src.main.org.apache.commons.exec.CommandLine import *


class CommandLauncher(ABC):

    def isFailure(self, exitValue: int) -> bool:
        return exitValue != 0

    def exec1(
        self,
        commandLine: CommandLine,
        env: typing.Dict[str, str],
        workingDirectory: pathlib.Path,
    ) -> subprocess.Popen:
        import subprocess

        # Convert CommandLine to a list of arguments
        command = (
            commandLine.toStrings()
        )  # Assuming CommandLine has a method toStrings() that returns a list of command arguments

        # Convert pathlib.Path to string for subprocess
        working_dir = str(workingDirectory)

        # Launch the process
        process = subprocess.Popen(
            command,
            env=env,
            cwd=working_dir,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )

        return process

    def exec0(
        self, commandLine: CommandLine, env: typing.Dict[str, str]
    ) -> subprocess.Popen:
        import subprocess

        # Convert CommandLine to a list of arguments
        command = (
            commandLine.toStrings()
        )  # Assuming CommandLine has a method toStrings() that returns a list of command arguments

        # Launch the process with the provided environment variables
        process = subprocess.Popen(
            command, env=env, stdout=subprocess.PIPE, stderr=subprocess.PIPE
        )

        return process
