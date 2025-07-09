from __future__ import annotations
import time
import re
import io
import typing
from typing import *
from src.main.org.apache.commons.pool2.UsageTracking import *


class BaseProxyHandler:

    __usageTracking: UsageTracking[typing.Any] = None

    __pooledObject: typing.Any = None

    def toString(self) -> str:
        builder = []
        builder.append(self.__class__.__name__)
        builder.append(" [pooledObject=")
        builder.append(str(self.__pooledObject))
        builder.append(", usageTracking=")
        builder.append(str(self.__usageTracking))
        builder.append("]")
        return "".join(builder)

    def validateProxiedObject(self) -> None:
        if self.__pooledObject is None:
            raise RuntimeError(
                "This object may no longer be used as it has been returned to the Object Pool."
            )

    def getPooledObject(self) -> typing.Any:
        return self.__pooledObject

    def doInvoke(
        self, method: typing.Callable, args: typing.List[typing.Any]
    ) -> typing.Any:
        self.validateProxiedObject()
        obj = self.getPooledObject()
        if self.__usageTracking is not None:
            self.__usageTracking.use(obj)
        return method(*args)

    def disableProxy(self) -> typing.Any:
        result = self.__pooledObject
        self.__pooledObject = None
        return result

    def __init__(
        self, pooledObject: typing.Any, usageTracking: UsageTracking[typing.Any]
    ) -> None:
        self.__pooledObject = pooledObject
        self.__usageTracking = usageTracking
