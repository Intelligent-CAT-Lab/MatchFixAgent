from __future__ import annotations
import re
import unittest
import pytest
from abc import ABC
import io
from src.test.org.apache.commons.graph.utils.MultiThreadedTestRunner import *


class TestRunner(ABC):

    __runner: MultiThreadedTestRunner = None

    def setTestRunner(self, runner: MultiThreadedTestRunner) -> None:
        self.__runner = runner

    def run(self) -> None:
        try:
            self.runTest()
        except BaseException as e:
            self.__runner.addException(e)

    def runTest(self) -> None:
        pass
