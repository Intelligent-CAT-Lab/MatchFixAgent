from __future__ import annotations
import time
import re
import io


class UncompressibleInputException(RuntimeError):

    __serialVersionUID: int = -798583799846489873

    def __init__(self, string: str) -> None:
        super().__init__(string)
