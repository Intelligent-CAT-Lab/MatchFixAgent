from __future__ import annotations
import re
from abc import ABC
from io import StringIO
import io
import typing
from typing import *


class CallStack(ABC):

    def printStackTrace(
        self, writer: typing.Union[io.TextIOWrapper, io.StringIO]
    ) -> bool:
        try:
            # Simulate printing the stack trace to the provided writer
            import traceback

            traceback.print_stack(file=writer)
            return True
        except Exception as e:
            # Handle any exceptions that might occur
            return False

    def fillInStackTrace(self) -> None:
        import traceback

        stack_trace = traceback.format_stack()
        print("".join(stack_trace))

    def clear(self) -> None:
        pass
