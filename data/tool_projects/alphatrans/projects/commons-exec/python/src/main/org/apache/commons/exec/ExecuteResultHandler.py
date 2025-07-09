from __future__ import annotations
import re
from abc import ABC
import io
from src.main.org.apache.commons.exec.ExecuteException import *


class ExecuteResultHandler(ABC):

    def onProcessFailed(self, e: ExecuteException) -> None:
        raise e

    def onProcessComplete(self, exitValue: int) -> None:
        pass
