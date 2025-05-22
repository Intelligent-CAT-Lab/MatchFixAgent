from __future__ import annotations
import re
import io
from src.main.org.apache.commons.exec.OS import *
from src.main.org.apache.commons.exec.launcher.CommandLauncher import *
from src.main.org.apache.commons.exec.launcher.Java13CommandLauncher import *
from src.main.org.apache.commons.exec.launcher.VmsCommandLauncher import *


class CommandLauncherFactory:

    @staticmethod
    def createVMLauncher() -> CommandLauncher:
        # Try using a JDK 1.3 launcher
        return VmsCommandLauncher() if OS.isFamilyOpenVms() else Java13CommandLauncher()

    def __init__(self) -> None:
        raise NotImplementedError("This class cannot be instantiated.")
