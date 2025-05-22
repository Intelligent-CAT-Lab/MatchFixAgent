from __future__ import annotations
import re
import io


class AnsiColors:

    TrueColor: AnsiColors = None

    Colors256: AnsiColors = None

    Colors16: AnsiColors = None

    __description: str = ""

    def __init__(self, description: str) -> None:
        self.__description = description

    def getDescription(self) -> str:
        return self.__description
