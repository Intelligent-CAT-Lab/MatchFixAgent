from __future__ import annotations
import re
from io import StringIO
import io
import typing
from typing import *
from src.main.org.apache.commons.pool2.impl.BaseObjectPoolConfig import *


class GenericKeyedObjectPoolConfig(BaseObjectPoolConfig):

    DEFAULT_MAX_IDLE_PER_KEY: int = 8
    DEFAULT_MIN_IDLE_PER_KEY: int = 0
    DEFAULT_MAX_TOTAL: int = -1
    DEFAULT_MAX_TOTAL_PER_KEY: int = 8
    __maxTotal: int = None
    __maxTotalPerKey: int = None
    __maxIdlePerKey: int = DEFAULT_MAX_IDLE_PER_KEY
    __minIdlePerKey: int = DEFAULT_MIN_IDLE_PER_KEY

    @staticmethod
    def initialize_fields() -> None:
        GenericKeyedObjectPoolConfig.__maxTotal: int = (
            GenericKeyedObjectPoolConfig.DEFAULT_MAX_TOTAL
        )

        GenericKeyedObjectPoolConfig.__maxTotalPerKey: int = (
            GenericKeyedObjectPoolConfig.DEFAULT_MAX_TOTAL_PER_KEY
        )

    def _toStringAppendFields(
        self, builder: typing.Union[typing.List[str], io.StringIO]
    ) -> None:
        super()._toStringAppendFields(builder)
        if isinstance(builder, list):
            builder.append(", minIdlePerKey=")
            builder.append(str(self.__minIdlePerKey))
            builder.append(", maxIdlePerKey=")
            builder.append(str(self.__maxIdlePerKey))
            builder.append(", maxTotalPerKey=")
            builder.append(str(self.__maxTotalPerKey))
            builder.append(", maxTotal=")
            builder.append(str(self.__maxTotal))
        elif isinstance(builder, io.StringIO):
            builder.write(", minIdlePerKey=")
            builder.write(str(self.__minIdlePerKey))
            builder.write(", maxIdlePerKey=")
            builder.write(str(self.__maxIdlePerKey))
            builder.write(", maxTotalPerKey=")
            builder.write(str(self.__maxTotalPerKey))
            builder.write(", maxTotal=")
            builder.write(str(self.__maxTotal))

    def clone(self) -> GenericKeyedObjectPoolConfig:
        try:
            return self.__class__(**self.__dict__)
        except Exception as e:
            raise AssertionError("Cloning failed") from e

    def setMinIdlePerKey(self, minIdlePerKey: int) -> None:
        self.__minIdlePerKey = minIdlePerKey

    def setMaxTotalPerKey(self, maxTotalPerKey: int) -> None:
        self.__maxTotalPerKey = maxTotalPerKey

    def setMaxTotal(self, maxTotal: int) -> None:
        self.__maxTotal = maxTotal

    def setMaxIdlePerKey(self, maxIdlePerKey: int) -> None:
        self.__maxIdlePerKey = maxIdlePerKey

    def getMinIdlePerKey(self) -> int:
        return self.__minIdlePerKey

    def getMaxTotalPerKey(self) -> int:
        return self.__maxTotalPerKey

    def getMaxTotal(self) -> int:
        return self.__maxTotal

    def getMaxIdlePerKey(self) -> int:
        return self.__maxIdlePerKey

    def __init__(self) -> None:
        super().__init__()


GenericKeyedObjectPoolConfig.initialize_fields()
