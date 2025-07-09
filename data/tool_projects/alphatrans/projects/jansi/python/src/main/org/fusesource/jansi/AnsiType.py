from __future__ import annotations
import re
import io
import typing
from typing import *


class AnsiType:

    Redirected: AnsiType = None

    Emulation: AnsiType = None

    VirtualTerminal: AnsiType = None

    Unsupported: AnsiType = None

    Native: AnsiType = None

    __description: str = ""

    def __init__(self, description: str) -> None:
        self.__description = description

    def getDescription(self) -> str:
        return self.__description
