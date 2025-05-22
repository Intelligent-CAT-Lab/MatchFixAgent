from __future__ import annotations
import time
import re
import io
import typing
from typing import *


class SecurityManagerCallStack:

    __snapshot: Snapshot = None

    def clear(self) -> None:
        self.__snapshot = None


class PrivateSecurityManager:

    def __getCallStack(self) -> typing.List[weakref.ref]:
        call_stack = [weakref.ref(cls) for cls in self.__getClassContext()]
        return call_stack


class Snapshot:

    __stack: typing.List[weakref.ref] = None

    __timestampMillis: int = int(time.time() * 1000)

    def __init__(self, stack: typing.List[weakref.ref]) -> None:
        self.__stack = stack
