from __future__ import annotations
import re
import unittest
import pytest
import io
import typing
from typing import *


class Waiter:

    __validationCount: int = 0

    __passivationCount: int = 0

    __lastIdleTimeMillis: int = 0

    __lastPassivatedMillis: int = 0

    __latency: int = 0

    __valid: bool = False

    __active: bool = False

    __instanceCount: int = 0
    __id: int = __instanceCount if __instanceCount is not None else 0
    __instanceCount = __id + 1

    def toString(self) -> str:
        buff = []
        buff.append(f"ID = {self.__id}\n")
        buff.append(f"valid = {self.__valid}\n")
        buff.append(f"active = {self.__active}\n")
        buff.append(f"lastPassivated = {self.__lastPassivatedMillis}\n")
        buff.append(f"lastIdleTimeMs = {self.__lastIdleTimeMillis}\n")
        buff.append(f"latency = {self.__latency}\n")
        return "".join(buff)

    def hashCode(self) -> int:
        return self.__id

    def equals(self, obj: typing.Any) -> bool:
        if not isinstance(obj, Waiter):
            return False
        return hash(obj) == self.__id

    @staticmethod
    def sleepQuietly(millis: int) -> None:
        try:
            import time

            time.sleep(millis / 1000)  # Convert milliseconds to seconds
        except Exception:
            pass

    def setValid(self, valid: bool) -> None:
        self.__valid = valid

    def setLatency(self, latency: int) -> None:
        self.__latency = latency

    def setActive(self, active: bool) -> None:
        activeState = self.__active
        if activeState == active:
            return
        self.__active = active
        currentTimeMillis = int(
            time.time() * 1000
        )  # Convert current time to milliseconds
        if active:  # activating
            self.__lastIdleTimeMillis = currentTimeMillis - self.__lastPassivatedMillis
        else:  # passivating
            self.__lastPassivatedMillis = currentTimeMillis
            self.__passivationCount += 1

    def isValid(self) -> bool:
        self.__validationCount += 1
        return self.__valid

    def isActive(self) -> bool:
        return self.__active

    def getValidationCount(self) -> int:
        return self.__validationCount

    def getPassivationCount(self) -> int:
        return self.__passivationCount

    def getLatency(self) -> int:
        return self.__latency

    def getLastPassivatedMillis(self) -> int:
        return self.__lastPassivatedMillis

    def getLastIdleTimeMillis(self) -> int:
        return self.__lastIdleTimeMillis

    def doWait(self) -> None:
        self.sleepQuietly(self.__latency)

    def __init__(self, active: bool, valid: bool, latency: int) -> None:
        self.__active = active
        self.__valid = valid
        self.__latency = latency
        self.__lastPassivatedMillis = int(
            time.time() * 1000
        )  # Equivalent to System.currentTimeMillis() in Java
