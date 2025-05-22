from __future__ import annotations
import time
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
from src.main.org.apache.commons.exec.ExecuteException import *
from src.main.org.apache.commons.exec.ExecuteStreamHandler import *
from src.main.org.apache.commons.exec.ExecuteWatchdog import *
from src.main.org.apache.commons.exec.OS import *
from src.main.org.apache.commons.exec.PumpStreamHandler import *


class Exec65Test(AbstractExecTest, unittest.TestCase):

    def testExec65WitSleepUsingSleepCommandDirectly_test9_decomposed(self) -> None:
        if not OS.isFamilyUnix():
            raise ExecuteException(
                self._testNotSupportedForCurrentOperatingSystem(), 0, None
            )

        watchdog = ExecuteWatchdog.ExecuteWatchdog0(self.WATCHDOG_TIMEOUT)
        executor_builder = DefaultExecutor.builder()
        executor = executor_builder.get()

        command = CommandLine(2, None, None, "sleep")
        command.addArgument0("60")

        stream_handler = PumpStreamHandler.PumpStreamHandler2(sys.stdout, sys.stderr)
        executor.setStreamHandler(stream_handler)
        executor.setWatchdog(watchdog)

        with pytest.raises(ExecuteException):
            executor.execute0(command)

    def testExec65WitSleepUsingSleepCommandDirectly_test8_decomposed(self) -> None:
        if not OS.isFamilyUnix():
            raise ExecuteException(
                self._testNotSupportedForCurrentOperatingSystem(), 0, None
            )

        watchdog = ExecuteWatchdog.ExecuteWatchdog0(self.WATCHDOG_TIMEOUT)
        executor_builder = DefaultExecutor.builder()
        executor = executor_builder.get()

        command = CommandLine(2, None, None, "sleep")
        command.addArgument0("60")

        stream_handler = PumpStreamHandler.PumpStreamHandler2(sys.stdout, sys.stderr)
        executor.setStreamHandler(stream_handler)
        executor.setWatchdog(watchdog)

    def testExec65WitSleepUsingSleepCommandDirectly_test7_decomposed(self) -> None:
        if not OS.isFamilyUnix():
            raise ExecuteException(
                self._testNotSupportedForCurrentOperatingSystem(), 0, None
            )

        watchdog = ExecuteWatchdog.ExecuteWatchdog0(self.WATCHDOG_TIMEOUT)
        executor = DefaultExecutor.builder().get()
        command = CommandLine(2, None, None, "sleep")
        command.addArgument0("60")
        stream_handler = PumpStreamHandler.PumpStreamHandler2(sys.stdout, sys.stderr)
        executor.setStreamHandler(stream_handler)

    def testExec65WitSleepUsingSleepCommandDirectly_test6_decomposed(self) -> None:
        if not OS.isFamilyUnix():
            raise ExecuteException(
                self._testNotSupportedForCurrentOperatingSystem(), 0, None
            )

        watchdog = ExecuteWatchdog.ExecuteWatchdog0(self.WATCHDOG_TIMEOUT)
        executor_builder = DefaultExecutor.builder()
        executor = executor_builder.get()

        command = CommandLine(2, None, None, "sleep")
        command.addArgument0("60")

        PumpStreamHandler.PumpStreamHandler2(sys.stdout, sys.stderr)

    def testExec65WitSleepUsingSleepCommandDirectly_test5_decomposed(self) -> None:
        if not OS.isFamilyUnix():
            raise ExecuteException(
                self._testNotSupportedForCurrentOperatingSystem(), 0, None
            )

        watchdog = ExecuteWatchdog.ExecuteWatchdog0(self.WATCHDOG_TIMEOUT)
        DefaultExecutor.builder()
        executor = DefaultExecutor.builder().get()
        command = CommandLine(2, None, None, "sleep")
        command.addArgument0("60")

    def testExec65WitSleepUsingSleepCommandDirectly_test4_decomposed(self) -> None:
        if not OS.isFamilyUnix():
            raise ExecuteException(
                self._testNotSupportedForCurrentOperatingSystem(), 0, None
            )

        watchdog = ExecuteWatchdog.ExecuteWatchdog0(self.WATCHDOG_TIMEOUT)
        executor_builder = DefaultExecutor.builder()
        executor = executor_builder.get()
        command = CommandLine(2, None, None, "sleep")

    def testExec65WitSleepUsingSleepCommandDirectly_test3_decomposed(self) -> None:
        if not OS.isFamilyUnix():
            raise ExecuteException(
                self._testNotSupportedForCurrentOperatingSystem(), 0, None
            )

        watchdog = ExecuteWatchdog.ExecuteWatchdog0(self.WATCHDOG_TIMEOUT)
        DefaultExecutor.builder()
        executor = DefaultExecutor.builder().get()

    def testExec65WitSleepUsingSleepCommandDirectly_test2_decomposed(self) -> None:
        if not OS.isFamilyUnix():
            raise ExecuteException(
                self._testNotSupportedForCurrentOperatingSystem(), 0, None
            )

        watchdog = ExecuteWatchdog.ExecuteWatchdog0(self.WATCHDOG_TIMEOUT)
        DefaultExecutor.builder()

    def testExec65WitSleepUsingSleepCommandDirectly_test1_decomposed(self) -> None:
        if not OS.isFamilyUnix():
            raise ExecuteException(
                self._testNotSupportedForCurrentOperatingSystem(), 0, None
            )

        watchdog = ExecuteWatchdog.ExecuteWatchdog0(self.WATCHDOG_TIMEOUT)

    def testExec65WitSleepUsingSleepCommandDirectly_test0_decomposed(self) -> None:
        if not OS.isFamilyUnix():
            raise ExecuteException(
                self._testNotSupportedForCurrentOperatingSystem(), 0, None
            )

    def testExec65WithSudoUsingShellScript_test8_decomposed(self) -> None:
        if "travis" in os.path.abspath("."):
            pytest.skip(
                "Test is skipped on travis, because we have to be a sudoer to make the other tests pass."
            )
        if os.getenv("GITHUB_WORKFLOW") is not None:
            pytest.skip("Test is skipped in GitHub Actions environment.")
        if not OS.isFamilyUnix():
            raise ExecuteException(
                CommandLine._testNotSupportedForCurrentOperatingSystem(), 0, None
            )
        executor = DefaultExecutor.builder().get()
        executor.setStreamHandler(PumpStreamHandler(sys.stdout, sys.stderr, sys.stdin))
        executor.setWatchdog(
            ExecuteWatchdog.ExecuteWatchdog0(AbstractExecTest.WATCHDOG_TIMEOUT)
        )
        command = CommandLine(
            1, None, CommandLine._resolveTestScript1("issues", "exec-65"), None
        )
        with pytest.raises(ExecuteException):
            executor.execute0(command)

    def testExec65WithSudoUsingShellScript_test7_decomposed(self) -> None:
        if "travis" in os.path.abspath("."):
            pytest.skip(
                "Test is skipped on travis, because we have to be a sudoer to make the other tests pass."
            )
        if os.getenv("GITHUB_WORKFLOW") is not None:
            return
        if not OS.isFamilyUnix():
            raise ExecuteException(
                CommandLine._testNotSupportedForCurrentOperatingSystem(), 0, None
            )
        executor = DefaultExecutor.builder().get()
        executor.setStreamHandler(PumpStreamHandler(sys.stdout, sys.stderr, sys.stdin))
        executor.setWatchdog(
            ExecuteWatchdog.ExecuteWatchdog0(AbstractExecTest.WATCHDOG_TIMEOUT)
        )
        command = CommandLine(
            1, None, CommandLine._resolveTestScript1("issues", "exec-65"), None
        )

    def testExec65WithSudoUsingShellScript_test6_decomposed(self) -> None:
        # Skip the test if running on Travis CI
        if "travis" in os.path.abspath("."):
            pytest.skip(
                "Test is skipped on Travis, because we have to be a sudoer to make the other tests pass."
            )

        # Ensure the test is not running in a GitHub Actions workflow
        if os.getenv("GITHUB_WORKFLOW") is not None:
            pytest.skip("Test is skipped in GitHub Actions workflow.")

        # Check if the operating system is not Unix
        if not OS.isFamilyUnix():
            raise ExecuteException(
                self._testNotSupportedForCurrentOperatingSystem(), 0, None
            )

        # Create a DefaultExecutor instance
        executor = DefaultExecutor.builder().get()

        # Set up the stream handler
        stream_handler = PumpStreamHandler(
            outputStream=sys.stdout, errorOutputStream=sys.stderr, inputStream=sys.stdin
        )
        executor.setStreamHandler(stream_handler)

        # Set up the watchdog
        watchdog = ExecuteWatchdog.ExecuteWatchdog0(self.WATCHDOG_TIMEOUT)
        executor.setWatchdog(watchdog)

    def testExec65WithSudoUsingShellScript_test5_decomposed(self) -> None:
        # Skip the test if running on Travis CI
        if "travis" in os.path.abspath("."):
            pytest.skip(
                "Test is skipped on Travis, because we have to be a sudoer to make the other tests pass."
            )

        # Ensure the test is not running in a GitHub Actions workflow
        if os.getenv("GITHUB_WORKFLOW") is not None:
            pytest.skip("Test is skipped in GitHub Actions workflow.")

        # Check if the operating system is Unix-based
        if not OS.isFamilyUnix():
            raise ExecuteException(
                self._testNotSupportedForCurrentOperatingSystem(), 0, None
            )

        # Create a DefaultExecutor instance
        executor = DefaultExecutor.builder().get()

        # Set up the stream handler
        stream_handler = PumpStreamHandler(
            outputStream=sys.stdout, errorOutputStream=sys.stderr, inputStream=sys.stdin
        )
        executor.setStreamHandler(stream_handler)

        # Set up the ExecuteWatchdog with a timeout
        ExecuteWatchdog.ExecuteWatchdog0(self.WATCHDOG_TIMEOUT)

    def testExec65WithSudoUsingShellScript_test4_decomposed(self) -> None:
        # Skip the test if running on Travis CI
        if "travis" in os.path.abspath("."):
            pytest.skip(
                "Test is skipped on Travis CI because we have to be a sudoer to make the other tests pass."
            )

        # Ensure the test is not running in a GitHub Actions workflow
        if os.getenv("GITHUB_WORKFLOW") is not None:
            pytest.skip("Test is skipped in GitHub Actions workflow.")

        # Check if the operating system is not Unix
        if not OS.isFamilyUnix():
            raise ExecuteException(
                self._testNotSupportedForCurrentOperatingSystem(), 0, None
            )

        # Create a DefaultExecutor instance
        executor = DefaultExecutor.builder().get()

        # Set up the PumpStreamHandler
        stream_handler = PumpStreamHandler.PumpStreamHandler3(
            sys.stdout, sys.stderr, sys.stdin
        )
        executor.setStreamHandler(stream_handler)

    def testExec65WithSudoUsingShellScript_test3_decomposed(self) -> None:
        # Skip the test if running in Travis CI
        if "travis" in os.path.abspath("."):
            self.skipTest(
                "Test is skipped on Travis, because we have to be a sudoer to make the other tests pass."
            )

        # Skip the test if running in GitHub Actions
        if os.getenv("GITHUB_WORKFLOW") is not None:
            self.skipTest("Test is skipped in GitHub Actions.")

        # Check if the operating system is not Unix
        if not OS.isFamilyUnix():
            raise ExecuteException(
                self._testNotSupportedForCurrentOperatingSystem(), 0, None
            )

        # Create a DefaultExecutor instance
        DefaultExecutor.builder()
        executor = DefaultExecutor.builder().get()

        # Set up the PumpStreamHandler
        PumpStreamHandler.PumpStreamHandler3(sys.stdout, sys.stderr, sys.stdin)

    def testExec65WithSudoUsingShellScript_test2_decomposed(self) -> None:
        # Skip the test if running on Travis CI
        if ".travis" in os.path.abspath("."):
            pytest.skip(
                "Test is skipped on Travis, because we have to be a sudoer to make the other tests pass."
            )

        # Ensure the test is not running in a GitHub Actions workflow
        if os.getenv("GITHUB_WORKFLOW") is not None:
            pytest.skip("Test is skipped in GitHub Actions workflow.")

        # Check if the operating system is not Unix
        if not OS.isFamilyUnix():
            raise ExecuteException(
                self._testNotSupportedForCurrentOperatingSystem(), 0, None
            )

        # Create a DefaultExecutor instance
        executor = DefaultExecutor.builder().get()

    def testExec65WithSudoUsingShellScript_test1_decomposed(self) -> None:
        # Skip the test if the current directory path contains "travis"
        if "travis" in os.path.abspath("."):
            pytest.skip(
                "Test is skipped on travis, because we have to be a sudoer to make the other tests pass."
            )

        # Skip the test if the GITHUB_WORKFLOW environment variable is set
        if os.getenv("GITHUB_WORKFLOW") is not None:
            pytest.skip("Test is skipped because it is running in a GitHub workflow.")

        # Raise an exception if the operating system is not Unix
        if not OS.isFamilyUnix():
            raise ExecuteException(
                self._testNotSupportedForCurrentOperatingSystem(), 0, None
            )

        # Call the DefaultExecutor builder
        DefaultExecutor.builder()

    def testExec65WithSudoUsingShellScript_test0_decomposed(self) -> None:
        # Skip the test if the current directory path contains "travis"
        if "travis" in os.path.abspath("."):
            pytest.skip(
                "Test is skipped on travis, because we have to be a sudoer to make the other tests pass."
            )

        # Skip the test if the GITHUB_WORKFLOW environment variable is set
        if os.getenv("GITHUB_WORKFLOW") is not None:
            pytest.skip("Test is skipped because it is running in a GitHub workflow.")

        # Raise an exception if the operating system is not Unix
        if not OS.isFamilyUnix():
            raise ExecuteException(
                self._testNotSupportedForCurrentOperatingSystem(), 0, None
            )

    def testExec65WithSleepUsingShellScriptAndJDKOnly_test2_decomposed(self) -> None:
        process = subprocess.Popen([str(self._resolveTestScript0("sleep").absolute())])
        time.sleep(self.WATCHDOG_TIMEOUT / 1000)  # Convert milliseconds to seconds
        process.terminate()
        process.wait()
        self.assertTrue(process.returncode != 0)

    def testExec65WithSleepUsingShellScriptAndJDKOnly_test1_decomposed(self) -> None:
        process = subprocess.Popen(
            [self._resolveTestScript0("sleep").absolute().as_posix()]
        )
        time.sleep(self.WATCHDOG_TIMEOUT / 1000)  # Convert milliseconds to seconds
        process.terminate()
        process.wait()

    def testExec65WithSleepUsingShellScriptAndJDKOnly_test0_decomposed(self) -> None:
        process = subprocess.Popen(
            [str(self._resolveTestScript0("sleep"))],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        process.communicate()

    def testExec65WithSleepUsingShellScript_test8_decomposed(self) -> None:
        # Ensure the test only runs on macOS
        if not OS.isFamilyMac():
            self.skipTest("Test is only applicable for macOS")

        # Create a DefaultExecutor instance
        executor = DefaultExecutor.builder().get()

        # Set up the stream handler
        stream_handler = PumpStreamHandler.PumpStreamHandler2(sys.stdout, sys.stderr)
        executor.setStreamHandler(stream_handler)

        # Set up the watchdog with a timeout
        watchdog = ExecuteWatchdog.ExecuteWatchdog0(self.WATCHDOG_TIMEOUT)
        executor.setWatchdog(watchdog)

        # Resolve the test script for "sleep"
        command = CommandLine(1, None, self._resolveTestScript0("sleep"), None)

        # Assert that executing the command raises an ExecuteException
        with self.assertRaises(ExecuteException):
            executor.execute0(command)

    def testExec65WithSleepUsingShellScript_test7_decomposed(self) -> None:
        pytest.assume(OS.isFamilyMac())
        executor = DefaultExecutor.builder().get()
        stream_handler = PumpStreamHandler.PumpStreamHandler2(sys.stdout, sys.stderr)
        executor.setStreamHandler(stream_handler)
        watchdog = ExecuteWatchdog.ExecuteWatchdog0(self.WATCHDOG_TIMEOUT)
        executor.setWatchdog(watchdog)
        command = CommandLine(1, None, self._resolveTestScript0("sleep"), None)

    def testExec65WithSleepUsingShellScript_test6_decomposed(self) -> None:
        # Ensure the test only runs on macOS
        if not OS.isFamilyMac():
            self.skipTest("Test is only applicable for macOS")

        # Create a DefaultExecutor instance using the builder
        executor = DefaultExecutor.builder().get()

        # Set up the PumpStreamHandler with standard output and error
        stream_handler = PumpStreamHandler.PumpStreamHandler2(sys.stdout, sys.stderr)
        executor.setStreamHandler(stream_handler)

        # Set up the ExecuteWatchdog with the specified timeout
        watchdog = ExecuteWatchdog.ExecuteWatchdog0(self.WATCHDOG_TIMEOUT)
        executor.setWatchdog(watchdog)

    def testExec65WithSleepUsingShellScript_test5_decomposed(self) -> None:
        if not OS.isFamilyMac():
            self.skipTest("Test only runs on Mac OS")

        executor_builder = DefaultExecutor.builder()
        executor = executor_builder.get()
        stream_handler = PumpStreamHandler.PumpStreamHandler2(sys.stdout, sys.stderr)
        executor.setStreamHandler(stream_handler)
        watchdog = ExecuteWatchdog.ExecuteWatchdog0(self.WATCHDOG_TIMEOUT)

    def testExec65WithSleepUsingShellScript_test4_decomposed(self) -> None:
        if not OS.isFamilyMac():
            self.skipTest("Test only runs on Mac OS family")

        executor_builder = DefaultExecutor.builder()
        executor = executor_builder.get()
        stream_handler = PumpStreamHandler.PumpStreamHandler2(sys.stdout, sys.stderr)
        executor.setStreamHandler(stream_handler)

    def testExec65WithSleepUsingShellScript_test3_decomposed(self) -> None:
        if not OS.isFamilyMac():
            self.skipTest("Test only runs on Mac OS")

        builder = DefaultExecutor.builder()
        executor = builder.get()
        PumpStreamHandler.PumpStreamHandler2(sys.stdout, sys.stderr)

    def testExec65WithSleepUsingShellScript_test2_decomposed(self) -> None:
        if not OS.isFamilyMac():
            self.skipTest("Test only runs on Mac OS family")

        builder = DefaultExecutor.builder()
        executor = builder.get()

    def testExec65WithSleepUsingShellScript_test1_decomposed(self) -> None:
        if not OS.isFamilyMac():
            self.skipTest("Test is only applicable for macOS")
        DefaultExecutor.builder()

    def testExec65WithSleepUsingShellScript_test0_decomposed(self) -> None:
        self.assertTrue(OS.isFamilyMac())
