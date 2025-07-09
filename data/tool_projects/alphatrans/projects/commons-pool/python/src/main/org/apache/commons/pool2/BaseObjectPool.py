from __future__ import annotations
import time
import re
from abc import ABC
from io import StringIO
import io
import typing
from typing import *
import os
from src.main.org.apache.commons.pool2.BaseObject import *
from src.main.org.apache.commons.pool2.ObjectPool import *


class BaseObjectPool(BaseObject, ObjectPool, ABC):

    __closed: bool = False

    def _toStringAppendFields(
        self, builder: typing.Union[typing.List[str], io.StringIO]
    ) -> None:
        if isinstance(builder, list):
            builder.append(f"closed={self.__closed}")
        elif isinstance(builder, io.StringIO):
            builder.write(f"closed={self.__closed}")

    def getNumIdle(self) -> int:
        return -1

    def getNumActive(self) -> int:
        return -1

    def close(self) -> None:
        self.__closed = True

    def clear(self) -> None:
        raise NotImplementedError("NotImplementedError")

    def addObject(self) -> None:
        raise NotImplementedError()

    def isClosed(self) -> bool:
        return self.__closed

    def _assertOpen(self) -> None:
        if self.isClosed():
            raise RuntimeError("Pool not open")

    def returnObject(self, obj: typing.Any) -> None:
        raise Exception("This method must be implemented by a subclass")

    def invalidateObject0(self, obj: typing.Any) -> None:
        raise Exception("This method must be implemented by a subclass")

    def borrowObject(self) -> typing.Any:
        raise NotImplementedError("Subclasses must implement this method")
