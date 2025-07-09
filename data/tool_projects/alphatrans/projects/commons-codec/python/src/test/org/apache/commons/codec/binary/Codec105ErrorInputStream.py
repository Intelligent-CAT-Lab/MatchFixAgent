from __future__ import annotations
import re
import unittest
import pytest
import io
import typing
from typing import *
import os


class Codec105ErrorInputStream:

    __EOF: int = -1
    countdown: int = 3

    def read(self) -> int:
        return self.read0()

    def read1(self, b: typing.List[int], pos: int, len_: int) -> int:
        if self.countdown > 0:
            self.countdown -= 1
            b[pos] = ord("\n")  # Store the ASCII value of '\n' in the list
            return 1
        return self.__EOF

    def read0(self) -> int:
        if self.countdown > 0:
            self.countdown -= 1
            return ord("\n")
        return self.__EOF
