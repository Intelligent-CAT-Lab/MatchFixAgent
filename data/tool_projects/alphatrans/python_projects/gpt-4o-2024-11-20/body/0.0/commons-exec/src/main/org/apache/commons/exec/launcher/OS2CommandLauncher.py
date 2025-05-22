from __future__ import annotations
import re
import pathlib
import io
import typing
from typing import *
from src.main.org.apache.commons.exec.CommandLine import *
from src.main.org.apache.commons.exec.launcher.CommandLauncher import *
from src.main.org.apache.commons.exec.launcher.CommandLauncherProxy import *


class OS2CommandLauncher(CommandLauncherProxy):

    def exec1(
        self, cmd: CommandLine, env: typing.Dict[str, str], workingDir: pathlib.Path
    ) -> subprocess.Popen:
        if workingDir is None:
            return self.exec0(cmd, env)
        return self.exec0(
            CommandLine(2, None, None, "cmd")
            .addArgument0("/c")
            .addArguments2(cmd.toStrings()),
            env,
        )

    def __init__(self, launcher: CommandLauncher) -> None:
        super().__init__(launcher)
