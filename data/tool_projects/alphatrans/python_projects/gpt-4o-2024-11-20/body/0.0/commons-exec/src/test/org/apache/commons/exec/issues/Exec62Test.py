from __future__ import annotations
import time
import re
import tempfile
import os
import unittest
import pytest
import pathlib
import io
import unittest
from src.main.org.apache.commons.exec.CommandLine import *
from src.main.org.apache.commons.exec.DefaultExecutor import *
from src.main.org.apache.commons.exec.ExecuteStreamHandler import *
from src.main.org.apache.commons.exec.ExecuteWatchdog import *
from src.main.org.apache.commons.exec.OS import *
from src.main.org.apache.commons.exec.PumpStreamHandler import *
from src.test.org.apache.commons.exec.TestUtil import *


class Exec62Test(unittest.TestCase):

    __outputFile: Path = None

    def testMe(self) -> None:
        if OS.isFamilyUnix():
            self.__execute("exec-62")

    def tearDown(self) -> None:
        self.__outputFile.unlink()

    def setUp(self) -> None:
        self.__outputFile = pathlib.Path(
            tempfile.mkstemp(suffix=".log", prefix="foo")[1]
        )

    def __execute(self, scriptName: str) -> None:
        watchdog = ExecuteWatchdog.ExecuteWatchdog0(4000)
        commandLine = CommandLine(2, None, None, "/bin/sh")
        testScript = TestUtil.resolveScriptForOS(
            f"./src/test/scripts/issues/{scriptName}"
        )

        commandLine.addArgument0(testScript.absolute())

        executor = DefaultExecutor.builder().get()
        executor.setExitValues(None)  # ignore exit values
        executor.setWatchdog(watchdog)

        with self.__outputFile.open(
            "wb"
        ) as fos:  # Open the output file in binary write mode
            streamHandler = PumpStreamHandler.PumpStreamHandler1(fos)
            executor.setStreamHandler(streamHandler)
            executor.execute0(commandLine)

            if watchdog.killedProcess():
                raise TimeoutError(
                    f"Transcode process was killed on timeout 4000 ms, command line {commandLine.toString()}"
                )
