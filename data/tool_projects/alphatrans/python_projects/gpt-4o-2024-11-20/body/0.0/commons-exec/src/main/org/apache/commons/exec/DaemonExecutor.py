from __future__ import annotations
import re
import pathlib
import io
import threading
import typing
from typing import *
from src.main.org.apache.commons.exec.DefaultExecutor import *
from src.main.org.apache.commons.exec.ExecuteStreamHandler import *


class DaemonExecutor(DefaultExecutor):

    def _createThread(self, runnable: typing.Callable, name: str) -> threading.Thread:
        thread = super()._createThread(runnable, name)
        thread.daemon = True
        return thread

    @staticmethod
    def builder() -> Builder:
        return Builder()

    def __init__(
        self,
        threadFactory: threading.Thread,
        executeStreamHandler: ExecuteStreamHandler,
        workingDirectory: pathlib.Path,
    ) -> None:
        super().__init__(threadFactory, executeStreamHandler, workingDirectory)


class Builder:

    def get(self) -> DefaultExecutor:
        return DaemonExecutor(
            self.getThreadFactory(),
            self.getExecuteStreamHandler(),
            self.getWorkingDirectory(),
        )
