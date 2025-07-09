from __future__ import annotations
import re
import io


class AnsiMode:

    Force: AnsiMode = None

    Default: AnsiMode = None

    Strip: AnsiMode = None

    __description: str = ""

    def __init__(self, description: str) -> None:
        self.__description = description

    def getDescription(self) -> str:
        return self.__description
