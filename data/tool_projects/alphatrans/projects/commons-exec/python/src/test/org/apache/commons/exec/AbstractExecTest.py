from __future__ import annotations
import re
import sys
import os
import unittest
import pytest
from abc import ABC
import pathlib
import io
from src.test.org.apache.commons.exec.TestUtil import *


class AbstractExecTest(ABC):

    WATCHDOG_TIMEOUT: int = 3000
    TEST_TIMEOUT: int = 15000
    __testDir: pathlib.Path = pathlib.Path("src/test/scripts")
    __OS_NAME: str = os.name

    def _testNotSupportedForCurrentOperatingSystem(self) -> str:
        msg = f"The test is not possible for OS : {self.__OS_NAME}"
        print(msg)
        return msg

    def _testIsBrokenForCurrentOperatingSystem(self) -> str:
        msg = f"The test is broken for OS : {self.__OS_NAME}"
        print(msg, file=sys.stderr)
        return msg

    def _resolveTestScript1(self, directoryName: str, baseName: str) -> pathlib.Path:
        result = TestUtil.resolveScriptForOS(
            str(self.__testDir / directoryName / baseName)
        )
        if not result.exists():
            raise ValueError(f"Unable to find the following file: {result.absolute()}")
        return result

    def _resolveTestScript0(self, baseName: str) -> pathlib.Path:
        result = TestUtil.resolveScriptForOS(str(self.__testDir / baseName))
        if not result.exists():
            raise ValueError(f"Unable to find the following file: {result.absolute()}")
        return result
