from __future__ import annotations
import time
import re
from io import StringIO
import io
import typing
from typing import *
from src.main.org.apache.commons.pool2.PooledObject import *
from src.main.org.apache.commons.pool2.impl.DefaultPooledObjectInfoMBean import *


class DefaultPooledObjectInfo(DefaultPooledObjectInfoMBean):

    __pooledObject: PooledObject[typing.Any] = None

    __PATTERN: str = "yyyy-MM-dd HH:mm:ss Z"

    def toString(self) -> str:
        builder = []
        builder.append("DefaultPooledObjectInfo [pooledObject=")
        builder.append(str(self.__pooledObject))
        builder.append("]")
        return "".join(builder)

    def getPooledObjectType(self) -> str:
        return self.__pooledObject.getObject().__class__.__name__

    def getPooledObjectToString(self) -> str:
        return self.__pooledObject.getObject().__str__()

    def getLastReturnTimeFormatted(self) -> str:
        return self.__getTimeFormatted(self.getLastReturnTime())

    def getLastReturnTime(self) -> int:
        return self.__pooledObject.getLastReturnInstant().toEpochMilli()

    def getLastBorrowTrace(self) -> str:
        sw = io.StringIO()
        self.__pooledObject.printStackTrace(io.StringIO(sw))
        return sw.getvalue()

    def getLastBorrowTimeFormatted(self) -> str:
        return self.__getTimeFormatted(self.getLastBorrowTime())

    def getLastBorrowTime(self) -> int:
        return self.__pooledObject.getLastBorrowInstant().toEpochMilli()

    def getCreateTimeFormatted(self) -> str:
        return self.__getTimeFormatted(self.getCreateTime())

    def getCreateTime(self) -> int:
        return self.__pooledObject.getCreateInstant().toEpochMilli()

    def getBorrowedCount(self) -> int:
        return self.__pooledObject.getBorrowedCount()

    def __init__(self, pooledObject: PooledObject[typing.Any]) -> None:
        self.__pooledObject = pooledObject

    def __getTimeFormatted(self, millis: int) -> str:
        from datetime import datetime
        from pytz import timezone

        # Convert milliseconds to seconds and create a datetime object
        dt = datetime.fromtimestamp(millis / 1000, tz=timezone("UTC"))

        # Format the datetime object according to the pattern
        return dt.strftime("%Y-%m-%d %H:%M:%S %z")
