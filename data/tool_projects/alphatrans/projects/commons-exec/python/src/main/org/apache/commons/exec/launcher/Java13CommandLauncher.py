from __future__ import annotations
import re
import pathlib
import io
import typing
from typing import *
from src.main.org.apache.commons.exec.CommandLine import *
from src.main.org.apache.commons.exec.environment.EnvironmentUtils import *
from src.main.org.apache.commons.exec.launcher.CommandLauncherImpl import *


class Java13CommandLauncher(CommandLauncherImpl):

    def exec1(
        self, cmd: CommandLine, env: typing.Dict[str, str], workingDir: pathlib.Path
    ) -> subprocess.Popen:
        return subprocess.Popen(
            cmd.toStrings(), env=EnvironmentUtils.toStrings(env), cwd=str(workingDir)
        )

    def __init__(self) -> None:
        super().__init__()
