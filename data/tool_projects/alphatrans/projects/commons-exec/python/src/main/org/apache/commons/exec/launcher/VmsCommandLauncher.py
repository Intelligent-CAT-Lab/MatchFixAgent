from __future__ import annotations
import re
import random
import os
import pathlib
import io
import typing
from typing import *
from src.main.org.apache.commons.exec.CommandLine import *
from src.main.org.apache.commons.exec.launcher.Java13CommandLauncher import *
from src.main.org.apache.commons.exec.util.StringUtils import *


class VmsCommandLauncher(Java13CommandLauncher):

    def isFailure(self, exitValue: int) -> bool:
        # even exit value signals failure
        return exitValue % 2 == 0

    def exec1(
        self, cmd: CommandLine, env: typing.Dict[str, str], workingDir: pathlib.Path
    ) -> subprocess.Popen:
        command_file = self.__createCommandFile(cmd, env)
        new_cmd = CommandLine(2, None, None, command_file.as_posix())
        return super().exec1(new_cmd, env, workingDir)

    def exec0(self, cmd: CommandLine, env: typing.Dict[str, str]) -> subprocess.Popen:
        command_file = self.__createCommandFile(cmd, env)
        new_cmd = CommandLine(2, None, None, command_file.as_posix())
        return super().exec0(new_cmd, env)

    def __createCommandFile(
        self, cmd: CommandLine, env: typing.Dict[str, str]
    ) -> pathlib.Path:
        path = pathlib.Path(
            pathlib.Path().resolve(), f"EXEC{pathlib.os.urandom(4).hex()}.TMP"
        )
        path.touch()
        path.unlink(missing_ok=True)  # Ensure the file is deleted on exit
        script = path

        with path.open(mode="w", encoding="utf-8") as writer:
            # Add the environment as global symbols for the DCL script
            if env is not None:
                for key, value in env.items():
                    writer.write(f'$ {key} == "')
                    # Any embedded " values need to be doubled
                    if '"' in value:
                        value = value.replace('"', '""')
                    writer.write(value)
                    writer.write('"\n')

            command = cmd.getExecutable()
            if cmd.isFile():  # We assume it is a script file
                writer.write("$ @")
                # This is a bit crude, but seems to work
                parts = StringUtils.split(command, "/")
                writer.write(parts[0])  # device
                writer.write(":[")
                writer.write(parts[1])  # top-level directory
                last_part = len(parts) - 1
                for i in range(2, last_part):
                    writer.write(".")
                    writer.write(parts[i])
                writer.write("]")
                writer.write(parts[last_part])
            else:
                writer.write(f"$ {command}")

            args = cmd.getArguments()
            for arg in args:
                writer.write(" -\n")
                writer.write(arg)
            writer.write("\n")

        return script
