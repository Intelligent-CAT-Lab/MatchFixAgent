from __future__ import annotations
import re
from abc import ABC
import pathlib
import io
import typing
from typing import *
from src.main.org.apache.commons.exec.CommandLine import *
from src.main.org.apache.commons.exec.environment.EnvironmentUtils import *
from src.main.org.apache.commons.exec.launcher.CommandLauncher import *


class CommandLauncherImpl(CommandLauncher, ABC):

    def isFailure(self, exitValue: int) -> bool:
        # non-zero exit value signals failure
        return exitValue != 0

    def exec0(self, cmd: CommandLine, env: typing.Dict[str, str]) -> subprocess.Popen:
        return subprocess.Popen(cmd.toStrings(), env=dict(env))

    def exec1(
        self, cmd: CommandLine, env: typing.Dict[str, str], workingDir: pathlib.Path
    ) -> subprocess.Popen:
        import subprocess

        # Convert CommandLine to a list of arguments
        command = (
            cmd.toStrings()
        )  # Assuming CommandLine has a method toStrings() that returns a list of command arguments

        # Prepare the environment variables
        environment = {**env}  # Copy the provided environment variables

        # Launch the process
        process = subprocess.Popen(
            command,
            env=environment,
            cwd=str(workingDir),  # Convert pathlib.Path to string for subprocess
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )

        return process
