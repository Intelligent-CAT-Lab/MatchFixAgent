from __future__ import annotations
import re
from io import StringIO
import io
import typing
from typing import *
from src.main.org.apache.commons.pool2.impl.BaseObjectPoolConfig import *


class GenericObjectPoolConfig(BaseObjectPoolConfig):

    DEFAULT_MIN_IDLE: int = 0
    DEFAULT_MAX_IDLE: int = 8
    DEFAULT_MAX_TOTAL: int = 8
    __minIdle: int = DEFAULT_MIN_IDLE
    __maxIdle: int = DEFAULT_MAX_IDLE
    __maxTotal: int = DEFAULT_MAX_TOTAL

    def _toStringAppendFields(
        self, builder: typing.Union[typing.List[str], io.StringIO]
    ) -> None:
        super()._toStringAppendFields(builder)
        if isinstance(builder, list):
            builder.append(", maxTotal=")
            builder.append(str(self.__maxTotal))
            builder.append(", maxIdle=")
            builder.append(str(self.__maxIdle))
            builder.append(", minIdle=")
            builder.append(str(self.__minIdle))
        elif isinstance(builder, io.StringIO):
            builder.write(", maxTotal=")
            builder.write(str(self.__maxTotal))
            builder.write(", maxIdle=")
            builder.write(str(self.__maxIdle))
            builder.write(", minIdle=")
            builder.write(str(self.__minIdle))

    def clone(self) -> GenericObjectPoolConfig:
        try:
            return self.__class__(**self.__dict__)
        except Exception as e:
            raise AssertionError("Clone operation failed") from e

    def setMinIdle(self, minIdle: int) -> None:
        self.__minIdle = minIdle

    def setMaxTotal(self, maxTotal: int) -> None:
        self.__maxTotal = maxTotal

    def setMaxIdle(self, maxIdle: int) -> None:
        self.__maxIdle = maxIdle

    def getMinIdle(self) -> int:
        return self.__minIdle

    def getMaxTotal(self) -> int:
        return self.__maxTotal

    def getMaxIdle(self) -> int:
        return self.__maxIdle
