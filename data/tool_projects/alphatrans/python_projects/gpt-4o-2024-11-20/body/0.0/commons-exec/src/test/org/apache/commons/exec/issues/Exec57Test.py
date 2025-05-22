from __future__ import annotations
import re
import sys
import unittest
import pytest
import io
import os
import unittest
from src.test.org.apache.commons.exec.AbstractExecTest import *
from src.main.org.apache.commons.exec.CommandLine import *
from src.main.org.apache.commons.exec.DefaultExecutor import *
from src.main.org.apache.commons.exec.ExecuteStreamHandler import *
from src.main.org.apache.commons.exec.OS import *
from src.main.org.apache.commons.exec.PumpStreamHandler import *


class Exec57Test(AbstractExecTest, unittest.TestCase):

    def testExecutionOfDetachedProcess_test7_decomposed(self) -> None:
        if not OS.isFamilyUnix():
            self._testNotSupportedForCurrentOperatingSystem()
            return

        cmdLine = (
            CommandLine(2, None, None, "sh")
            .addArgument0("-c")
            .addArgument1("./src/test/scripts/issues/exec-57-detached.sh", False)
        )
        executor = DefaultExecutor.builder().get()
        pumpStreamHandler = PumpStreamHandler.PumpStreamHandler2(sys.stdout, sys.stderr)
        executor.setStreamHandler(pumpStreamHandler)
        executor.execute0(cmdLine)

    def testExecutionOfDetachedProcess_test6_decomposed(self) -> None:
        if not OS.isFamilyUnix():
            self._testNotSupportedForCurrentOperatingSystem()
            return

        cmdLine = CommandLine(2, None, None, "sh").addArgument0("-c")
        cmdLine = cmdLine.addArgument1(
            "./src/test/scripts/issues/exec-57-detached.sh", False
        )

        executor_builder = DefaultExecutor.builder()
        executor = executor_builder.get()

        pumpStreamHandler = PumpStreamHandler.PumpStreamHandler2(sys.stdout, sys.stderr)
        executor.setStreamHandler(pumpStreamHandler)

    def testExecutionOfDetachedProcess_test5_decomposed(self) -> None:
        if not OS.isFamilyUnix():
            self._testNotSupportedForCurrentOperatingSystem()
            return

        cmd_line_1 = CommandLine(2, None, None, "sh").addArgument0("-c")
        cmd_line_2 = (
            CommandLine(2, None, None, "sh")
            .addArgument0("-c")
            .addArgument1("./src/test/scripts/issues/exec-57-detached.sh", False)
        )

        DefaultExecutor.builder()
        executor = DefaultExecutor.builder().get()
        pump_stream_handler = PumpStreamHandler.PumpStreamHandler2(
            sys.stdout, sys.stderr
        )

    def testExecutionOfDetachedProcess_test4_decomposed(self) -> None:
        if not OS.isFamilyUnix():
            self._testNotSupportedForCurrentOperatingSystem()
            return

        CommandLine(2, None, None, "sh").addArgument0("-c")
        cmdLine = (
            CommandLine(2, None, None, "sh")
            .addArgument0("-c")
            .addArgument1("./src/test/scripts/issues/exec-57-detached.sh", False)
        )
        DefaultExecutor.builder()
        executor = DefaultExecutor.builder().get()

    def testExecutionOfDetachedProcess_test3_decomposed(self) -> None:
        if not OS.isFamilyUnix():
            self._testNotSupportedForCurrentOperatingSystem()
            return

        cmd_line_1 = CommandLine(2, None, None, "sh").addArgument0("-c")
        cmd_line_2 = (
            CommandLine(2, None, None, "sh")
            .addArgument0("-c")
            .addArgument1("./src/test/scripts/issues/exec-57-detached.sh", False)
        )
        DefaultExecutor.builder()

    def testExecutionOfDetachedProcess_test2_decomposed(self) -> None:
        if not OS.isFamilyUnix():
            self._testNotSupportedForCurrentOperatingSystem()
            return

        CommandLine(2, None, None, "sh").addArgument0("-c")
        cmdLine = (
            CommandLine(2, None, None, "sh")
            .addArgument0("-c")
            .addArgument1("./src/test/scripts/issues/exec-57-detached.sh", False)
        )

    def testExecutionOfDetachedProcess_test1_decomposed(self) -> None:
        if not OS.isFamilyUnix():
            self._testNotSupportedForCurrentOperatingSystem()
            return
        CommandLine(2, None, None, "sh").addArgument0("-c")

    def testExecutionOfDetachedProcess_test0_decomposed(self) -> None:
        if not OS.isFamilyUnix():
            self._testNotSupportedForCurrentOperatingSystem()
            return

    def testExecutionOfBackgroundProcess(self) -> None:
        cmd_line = (
            CommandLine(2, None, None, "sh")
            .addArgument0("-c")
            .addArgument1("./src/test/scripts/issues/exec-57-nohup.sh", False)
        )
        executor = DefaultExecutor.builder().get()
        pump_stream_handler = PumpStreamHandler.PumpStreamHandler2(
            sys.stdout, sys.stderr
        )

        executor.setStreamHandler(pump_stream_handler)

        executor.execute0(cmd_line)
