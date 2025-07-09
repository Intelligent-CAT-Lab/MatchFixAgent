from __future__ import annotations
import re
import io
from src.main.org.fusesource.jansi.internal.Kernel32 import *


class WindowsSupport:

    @staticmethod
    def getErrorMessage(errorCode: int) -> str:
        return Kernel32.getErrorMessage(errorCode)

    @staticmethod
    def getLastErrorMessage() -> str:
        return Kernel32.getLastErrorMessage()
