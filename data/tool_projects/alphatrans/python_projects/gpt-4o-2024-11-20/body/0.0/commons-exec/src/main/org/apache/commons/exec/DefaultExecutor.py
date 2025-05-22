from __future__ import annotations
import time
import copy
import re
import pathlib
import io
import threading
import typing
from typing import *
import os
from src.main.org.apache.commons.exec.CommandLine import *
from src.main.org.apache.commons.exec.ExecuteException import *
from src.main.org.apache.commons.exec.ExecuteResultHandler import *
from src.main.org.apache.commons.exec.ExecuteStreamHandler import *
from src.main.org.apache.commons.exec.ExecuteWatchdog import *
from src.main.org.apache.commons.exec.Executor import *
from src.main.org.apache.commons.exec.ProcessDestroyer import *
from src.main.org.apache.commons.exec.PumpStreamHandler import *
from src.main.org.apache.commons.exec.ThreadUtil import *
from src.main.org.apache.commons.exec.launcher.CommandLauncher import *
from src.main.org.apache.commons.exec.launcher.CommandLauncherFactory import *


class DefaultExecutor(Executor):

    __threadFactory: threading.Thread = None

    __exceptionCaught: typing.Union[IOError, OSError] = None

    __executorThread: threading.Thread = None

    __processDestroyer: ProcessDestroyer = None

    __launcher: CommandLauncher = None

    __exitValues: typing.List[int] = None

    __watchdog: ExecuteWatchdog = None

    __workingDirectory: pathlib.Path = None

    __executeStreamHandler: ExecuteStreamHandler = None

    def setWorkingDirectory(self, workingDirectory: pathlib.Path) -> None:
        self.__workingDirectory = workingDirectory

    def setWatchdog(self, watchdog: ExecuteWatchdog) -> None:
        self.__watchdog = watchdog

    def setStreamHandler(self, streamHandler: ExecuteStreamHandler) -> None:
        self.__executeStreamHandler = streamHandler

    def setProcessDestroyer(self, processDestroyer: ProcessDestroyer) -> None:
        self.__processDestroyer = processDestroyer

    def setExitValues(self, values: typing.List[int]) -> None:
        self.__exitValues = None if values is None else values.copy()

    def setExitValue(self, value: int) -> None:
        self.setExitValues([value])

    def isFailure(self, exitValue: int) -> bool:
        if self.__exitValues is None:
            return False
        if len(self.__exitValues) == 0:
            return self.__launcher.isFailure(exitValue)
        for exitValue2 in self.__exitValues:
            if exitValue2 == exitValue:
                return False
        return True

    def getWorkingDirectory(self) -> pathlib.Path:
        return self.__workingDirectory

    def getWatchdog(self) -> ExecuteWatchdog:
        return self.__watchdog

    def getStreamHandler(self) -> ExecuteStreamHandler:
        return self.__executeStreamHandler

    def getProcessDestroyer(self) -> ProcessDestroyer:
        return self.__processDestroyer

    def DefaultExecutor0(self) -> DefaultExecutor:
        return DefaultExecutor(
            threading.Thread, PumpStreamHandler.PumpStreamHandler0(), pathlib.Path(".")
        )

    def __setStreams(
        self, streams: ExecuteStreamHandler, process: subprocess.Popen
    ) -> None:
        streams.setProcessInputStream(process.stdout)
        streams.setProcessOutputStream(process.stdin)
        streams.setProcessErrorStream(process.stderr)

    def __closeProcessStreams(self, process: subprocess.Popen) -> None:
        self.__closeCatch(process.stdin)
        self.__closeCatch(process.stdout)
        self.__closeCatch(process.stderr)

    def _launch(
        self,
        command: CommandLine,
        env: typing.Dict[str, str],
        workingDirectory: pathlib.Path,
    ) -> subprocess.Popen:
        if self.__launcher is None:
            raise RuntimeError("CommandLauncher cannot be null")

        self.__checkWorkingDirectory1(workingDirectory)

        return self.__launcher.exec1(command, env, workingDirectory)

    def _getExecutorThread(self) -> threading.Thread:
        return self.__executorThread

    def execute3(
        self,
        command: CommandLine,
        environment: typing.Dict[str, str],
        handler: ExecuteResultHandler,
    ) -> None:
        self.__checkWorkingDirectory0()
        if self.__watchdog is not None:
            self.__watchdog.setProcessNotStarted()

        def runnable():
            exit_value = Executor.INVALID_EXITVALUE
            try:
                exit_value = self._executeInternal(
                    command,
                    environment,
                    self.__workingDirectory,
                    self.__executeStreamHandler,
                )
                handler.onProcessComplete(exit_value)
            except ExecuteException as e:
                handler.onProcessFailed(e)
            except Exception as e:
                handler.onProcessFailed(
                    ExecuteException("Execution failed", exit_value, e)
                )

        self.__executorThread = self._createThread(
            runnable, "CommonsExecDefaultExecutor"
        )
        self._getExecutorThread().start()

    def execute2(self, command: CommandLine, environment: typing.Dict[str, str]) -> int:
        self.__checkWorkingDirectory0()
        return self.__executeInternal(
            command, environment, self.__workingDirectory, self.__executeStreamHandler
        )

    def execute1(self, command: CommandLine, handler: ExecuteResultHandler) -> None:
        self.execute3(command, None, handler)

    def execute0(self, command: CommandLine) -> int:
        return self.execute2(command, None)

    def _createThread(self, runnable: typing.Callable, name: str) -> threading.Thread:
        return ThreadUtil.newThread(self.__threadFactory, runnable, name, False)

    @staticmethod
    def builder() -> Builder:
        return Builder()

    def __setExceptionCaught(self, e: typing.Union[IOError, OSError]) -> None:
        if self.__exceptionCaught is None:
            self.__exceptionCaught = e

    def __getExceptionCaught(self) -> typing.Union[IOError, OSError]:
        return self.__exceptionCaught

    def __executeInternal(
        self,
        command: CommandLine,
        environment: typing.Dict[str, str],
        workingDirectory: pathlib.Path,
        streams: ExecuteStreamHandler,
    ) -> int:
        process = None
        self.__exceptionCaught = None

        try:
            # Launch the process
            process = self._launch(command, environment, workingDirectory)
        except (IOError, OSError) as e:
            if self.__watchdog is not None:
                self.__watchdog.failedToStart(e)
            raise e

        try:
            # Set up the streams
            self.__setStreams(streams, process)
        except (IOError, OSError) as e:
            process.terminate()
            if self.__watchdog is not None:
                self.__watchdog.failedToStart(e)
            raise e

        streams.start()

        try:
            # Add the process to the destroyer list
            if self.getProcessDestroyer() is not None:
                self.getProcessDestroyer().add(process)

            # Start the watchdog
            if self.__watchdog is not None:
                self.__watchdog.start(process)

            exitValue = Executor.INVALID_EXITVALUE

            try:
                # Wait for the process to complete
                exitValue = process.wait()
            except KeyboardInterrupt:
                process.terminate()
            finally:
                # Clear the interrupt status
                threading.current_thread().interrupt()

            # Stop the watchdog
            if self.__watchdog is not None:
                self.__watchdog.stop()

            # Stop the streams
            try:
                streams.stop()
            except (IOError, OSError) as e:
                self.__setExceptionCaught(e)

            # Close process streams
            self.__closeProcessStreams(process)

            # Check for any exceptions caught
            if self.__getExceptionCaught() is not None:
                raise self.__getExceptionCaught()

            # Check for exceptions from the watchdog
            if self.__watchdog is not None:
                try:
                    self.__watchdog.checkException()
                except (IOError, OSError) as e:
                    raise e
                except Exception as e:
                    raise IOError(e)

            # Check if the process exit value indicates failure
            if self.isFailure(exitValue):
                raise ExecuteException(
                    f"Process exited with an error: {exitValue}", exitValue, None
                )

            return exitValue

        finally:
            # Remove the process from the destroyer list
            if self.getProcessDestroyer() is not None:
                self.getProcessDestroyer().remove(process)

    def __closeCatch(self, closeable: Closeable) -> None:
        try:
            closeable.close()
        except (IOError, OSError) as e:
            self.__setExceptionCaught(e)

    def __checkWorkingDirectory1(self, directory: pathlib.Path) -> None:
        if directory is not None and not directory.exists():
            raise IOError(f"{directory} doesn't exist.")

    def __checkWorkingDirectory0(self) -> None:
        self.__checkWorkingDirectory1(self.__workingDirectory)

    def getThreadFactory(self) -> threading.Thread:
        return self.__threadFactory

    def __init__(
        self,
        threadFactory: Optional[threading.Thread],
        executeStreamHandler: Optional[ExecuteStreamHandler],
        workingDirectory: Optional[pathlib.Path],
    ) -> None:
        self.__threadFactory = (
            threadFactory if threadFactory is not None else threading.Thread
        )
        self.__executeStreamHandler = (
            executeStreamHandler
            if executeStreamHandler is not None
            else PumpStreamHandler.PumpStreamHandler0()
        )
        self.__workingDirectory = (
            workingDirectory if workingDirectory is not None else pathlib.Path(".")
        )
        self.__launcher = CommandLauncherFactory.createVMLauncher()
        self.__exitValues = []


class Builder:

    __workingDirectory: pathlib.Path = None

    __executeStreamHandler: ExecuteStreamHandler = None

    __threadFactory: threading.Thread = None

    def get(self) -> DefaultExecutor:
        return DefaultExecutor(
            self.__threadFactory, self.__executeStreamHandler, self.__workingDirectory
        )

    def setWorkingDirectory(self, workingDirectory: pathlib.Path) -> typing.Any:
        self.__workingDirectory = workingDirectory
        return self.asThis()

    def setThreadFactory(self, threadFactory: threading.Thread) -> typing.Any:
        self.__threadFactory = threadFactory
        return self.asThis()

    def setExecuteStreamHandler(
        self, executeStreamHandler: ExecuteStreamHandler
    ) -> typing.Any:
        self.__executeStreamHandler = executeStreamHandler
        return self.asThis()

    def getWorkingDirectory(self) -> pathlib.Path:
        return self.__workingDirectory

    def getThreadFactory(self) -> threading.Thread:
        return self.__threadFactory

    def getExecuteStreamHandler(self) -> ExecuteStreamHandler:
        return self.__executeStreamHandler

    def asThis(self) -> typing.Any:
        return self
