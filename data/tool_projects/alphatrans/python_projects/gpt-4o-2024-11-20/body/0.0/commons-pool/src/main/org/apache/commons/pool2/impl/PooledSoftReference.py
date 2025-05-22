from __future__ import annotations
import re
import io
import typing
from typing import *
from src.main.org.apache.commons.pool2.PooledObjectState import *
from src.main.org.apache.commons.pool2.impl.DefaultPooledObject import *


class PooledSoftReference(DefaultPooledObject):

    __reference: weakref.ref = None

    def toString(self) -> str:
        result = []
        result.append("Referenced Object: ")
        result.append(str(self.getObject()))
        result.append(", State: ")
        with self:  # Using 'with' to mimic synchronized block
            result.append(str(self.getState()))
        return "".join(result)

    def getObject(self) -> typing.Any:
        return self.__reference() if self.__reference is not None else None

    def setReference(self, reference: weakref.ref) -> None:
        self.__reference = reference

    def getReference(self) -> weakref.ref:
        return self.__reference

    def __init__(self, reference: weakref.ref) -> None:
        super().__init__(None)  # Null the hard reference in the parent
        self.__reference = reference
