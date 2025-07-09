from __future__ import annotations
import time
import re
import datetime
import unittest
import pytest
import pathlib
import io
import unittest
from src.test.org.apache.commons.exec.AbstractExecTest import *
from src.main.org.apache.commons.exec.CommandLine import *
from src.main.org.apache.commons.exec.DefaultExecutor import *
from src.main.org.apache.commons.exec.ExecuteException import *
from src.main.org.apache.commons.exec.ExecuteWatchdog import *
from src.main.org.apache.commons.exec.Executor import *


class Exec60Test(AbstractExecTest, unittest.TestCase):

    __pingScript: pathlib.Path = None  # LLM could not translate this field

    __exec: Executor = None  # LLM could not translate this field

    def testExec_60(self) -> None:
        start = 0
        seconds = 1
        offset_multiplier = 1
        max_retries = 180
        process_terminated_counter = 0
        watchdog_killed_process_counter = 0

        cmd_line = CommandLine(1, executable=self.__pingScript)
        cmd_line.addArgument0(
            str(seconds + 1)
        )  # need to add "1" to wait the requested number of seconds

        start_time = int(datetime.datetime.now().timestamp() * 1000)
        for offset in range(start, max_retries + 1):
            # wait progressively longer for process to complete
            # tricky to get this test right. We want to try and catch the process while it is terminating,
            # so we increase the timeout gradually until the test terminates normally.
            # However if the increase is too gradual, we never wait long enough for any test to exit normally
            watchdog = CommandLine.ExecuteWatchdog0(
                seconds * 1000 + offset * offset_multiplier
            )
            self.__exec.setWatchdog(watchdog)
            try:
                self.__exec.execute0(cmd_line)
                process_terminated_counter += 1
                # print(f"{offset}: process has terminated: {watchdog.killedProcess()}")
                if process_terminated_counter > 5:
                    break
            except ExecuteException as ex:
                # print(f"{offset}: process was killed: {watchdog.killedProcess()}")
                self.assertTrue(watchdog.killedProcess(), "Watchdog killed the process")
                watchdog_killed_process_counter += 1

        elapsed_time = int(datetime.datetime.now().timestamp() * 1000) - start_time
        avg = elapsed_time // (
            watchdog_killed_process_counter + process_terminated_counter
        )
        print(
            f"Processes terminated: {process_terminated_counter} killed: {watchdog_killed_process_counter} "
            f"Multiplier: {offset_multiplier} MaxRetries: {max_retries} Elapsed (avg ms): {avg}"
        )
        self.assertTrue(
            process_terminated_counter > 0, "Not a single process terminated on its own"
        )
        self.assertTrue(
            watchdog_killed_process_counter > 0,
            "Not a single process was killed by the watchdog",
        )
