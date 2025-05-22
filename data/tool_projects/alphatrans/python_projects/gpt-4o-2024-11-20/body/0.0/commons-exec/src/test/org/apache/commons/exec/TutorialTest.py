from __future__ import annotations
import time
import re
import sys
import unittest
import pytest
import pathlib
import io
import datetime
import os
import unittest
from src.main.org.apache.commons.exec.CommandLine import *
from src.main.org.apache.commons.exec.DefaultExecutor import *
from src.main.org.apache.commons.exec.ExecuteResultHandler import *
from src.main.org.apache.commons.exec.ExecuteWatchdog import *
from src.main.org.apache.commons.exec.Executor import *
from src.test.org.apache.commons.exec.TestUtil import *
from src.main.org.apache.commons.exec.DefaultExecuteResultHandler import *
from src.main.org.apache.commons.exec.ExecuteException import *


class TutorialTest(unittest.TestCase):

    __testDir: pathlib.Path = pathlib.Path("src/test/scripts")

    __acroRd32Script: pathlib.Path = None  # LLM could not translate this field

    def testTutorialExample_test2_decomposed(self) -> None:
        print_job_timeout = datetime.timedelta(seconds=15)
        print_in_background = False
        pdf_file = pathlib.Path("/Documents and Settings/foo.pdf")
        print_result = None

        try:
            # Printing takes around 10 seconds
            print("[main] Preparing print job ...")
            print_result = self.print_(pdf_file, print_job_timeout, print_in_background)
            print("[main] Successfully sent the print job ...")
        except Exception as e:
            print(e)
            pytest.fail(
                f"[main] Printing of the following document failed: {pdf_file.absolute()}"
            )
            raise e

        print("[main] Test is exiting but waiting for the print job to finish...")
        print_result.waitFor0()
        print("[main] The print job has finished ...")

    def testTutorialExample_test1_decomposed(self) -> None:
        print_job_timeout = datetime.timedelta(seconds=15)
        print_in_background = False
        pdf_file = pathlib.Path("/Documents and Settings/foo.pdf")
        try:
            # Printing takes around 10 seconds
            print("[main] Preparing print job ...")
            print_result = self.print_(pdf_file, print_job_timeout, print_in_background)
            print("[main] Successfully sent the print job ...")
        except Exception as e:
            print(e)
            pytest.fail(
                f"[main] Printing of the following document failed: {pdf_file.absolute()}"
            )
            raise e
        print("[main] Test is exiting but waiting for the print job to finish...")
        print_result.waitFor0()

    def testTutorialExample_test0_decomposed(self) -> None:
        print_job_timeout = datetime.timedelta(seconds=15)
        print_in_background = False
        pdf_file = pathlib.Path("/Documents and Settings/foo.pdf")

        try:
            # Printing takes around 10 seconds
            print("[main] Preparing print job ...")
            print_result = self.print_(pdf_file, print_job_timeout, print_in_background)
            print("[main] Successfully sent the print job ...")
        except Exception as e:
            print(e)
            pytest.fail(
                f"[main] Printing of the following document failed: {pdf_file.absolute()}"
            )
            raise

    def print_(
        self,
        file: pathlib.Path,
        printJobTimeout: datetime.timedelta,
        printInBackground: bool,
    ) -> PrintResultHandler:
        exit_value: int
        watchdog: ExecuteWatchdog | None = None
        result_handler: PrintResultHandler

        # Build up the command line using a 'pathlib.Path'
        substitution_map: dict[str, pathlib.Path] = {"file": file}
        command_line = CommandLine(1, executable=self.__acroRd32Script)
        command_line.addArgument0("/p")
        command_line.addArgument0("/h")
        command_line.addArgument0("${file}")
        command_line.setSubstitutionMap(substitution_map)

        # Create the executor and consider the exit value '1' as success
        executor = DefaultExecutor.builder().get()
        executor.setExitValue(1)

        # Create a watchdog if requested
        if printJobTimeout.total_seconds() > 0:
            watchdog = ExecuteWatchdog.builder().setTimeout(printJobTimeout).get()
            executor.setWatchdog(watchdog)

        # Pass an "ExecuteResultHandler" when doing background printing
        if printInBackground:
            print("[print] Executing non-blocking print job  ...")
            result_handler = PrintResultHandler(1, 0, watchdog)
            executor.execute1(command_line, result_handler)
        else:
            print("[print] Executing blocking print job  ...")
            exit_value = executor.execute0(command_line)
            result_handler = PrintResultHandler(0, exit_value, None)

        return result_handler


class PrintResultHandler(DefaultExecuteResultHandler):

    __watchdog: ExecuteWatchdog = None

    def onProcessFailed(self, e: ExecuteException) -> None:
        super().onProcessFailed(e)
        if self.__watchdog is not None and self.__watchdog.killedProcess():
            print("[resultHandler] The print process timed out", file=sys.stderr)
        else:
            print(
                f"[resultHandler] The print process failed to do : {e.getMessage()}",
                file=sys.stderr,
            )

    def onProcessComplete(self, exitValue: int) -> None:
        super().onProcessComplete(exitValue)
        print("[resultHandler] The document was successfully printed ...")

    def __init__(
        self, constructorId: int, exitValue: int, watchdog: ExecuteWatchdog
    ) -> None:
        if constructorId == 1:
            self.__watchdog = watchdog
        else:
            super().onProcessComplete(exitValue)
