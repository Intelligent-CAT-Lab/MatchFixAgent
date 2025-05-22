from __future__ import annotations
import time
import re
import sys
import os
import io


class DebugUtils:

    COMMONS_EXEC_DEBUG: str = "org.apache.commons.exec.debug"
    COMMONS_EXEC_LENIENT: str = "org.apache.commons.exec.lenient"

    @staticmethod
    def isLenientEnabled() -> bool:
        lenient = os.getenv(DebugUtils.COMMONS_EXEC_LENIENT, str(True))
        return str(True).lower() == lenient.lower()

    @staticmethod
    def isDebugEnabled() -> bool:
        debug = os.getenv(DebugUtils.COMMONS_EXEC_DEBUG, str(False))
        return str(True).lower() == debug.lower()

    @staticmethod
    def handleException(msg: str, e: Exception) -> None:
        if DebugUtils.isDebugEnabled():
            print(msg, file=sys.stderr)
            import traceback

            traceback.print_exception(type(e), e, e.__traceback__)

        if not DebugUtils.isLenientEnabled():
            if isinstance(e, RuntimeError):
                raise e
            raise RuntimeError(e)
