from __future__ import annotations
import re
import unittest
import pytest
import pathlib
import io
import typing
from typing import *
from src.main.org.apache.commons.exec.OS import *


class TestUtil:

    @staticmethod
    def resolveScriptForOS(script: str) -> pathlib.Path:
        if OS.isFamilyWindows():
            return pathlib.Path(f"{script}.bat")
        if OS.isFamilyUnix():
            return pathlib.Path(f"{script}.sh")
        if OS.isFamilyOpenVms():
            return pathlib.Path(f"{script}.dcl")
        pytest.fail("Test not supported for this OS")
        return None  # Unreachable

    @staticmethod
    def getTestScriptCodesForOS() -> typing.List[int]:
        if OS.isFamilyWindows():
            return [0, 1]
        if OS.isFamilyUnix():
            return [0, 1]
        if OS.isFamilyOpenVms():
            return [1, 2]
        pytest.fail("Test not supported for this OS")
        return []  # Unreachable, but added for type consistency.

    def __init__(self) -> None:
        raise NotImplementedError("This class cannot be instantiated")
