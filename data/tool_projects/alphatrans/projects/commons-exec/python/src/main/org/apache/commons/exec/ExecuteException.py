from __future__ import annotations
import re
import io


class ExecuteException:

    __exitValue: int = 0

    __serialVersionUID: int = 3256443620654331699

    def getExitValue(self) -> int:
        return self.__exitValue

    def __init__(self, message: str, exitValue: int, cause: BaseException) -> None:
        super().__init__(f"{message} (Exit value: {exitValue})")
        self.__exitValue = exitValue
        self.__cause__ = cause
