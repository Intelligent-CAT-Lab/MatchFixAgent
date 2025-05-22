from __future__ import annotations
import re
from abc import ABC
import io
import typing
from typing import *
from src.main.org.apache.commons.exec.CommandLine import *
from src.main.org.apache.commons.exec.launcher.CommandLauncher import *
from src.main.org.apache.commons.exec.launcher.CommandLauncherImpl import *


class CommandLauncherProxy(CommandLauncherImpl, ABC):

    __launcher: CommandLauncher = None

    def exec0(self, cmd: CommandLine, env: typing.Dict[str, str]) -> subprocess.Popen:
        return self.__launcher.exec0(cmd, env)

    def __init__(self, launcher: CommandLauncher) -> None:
        self.__launcher = launcher
