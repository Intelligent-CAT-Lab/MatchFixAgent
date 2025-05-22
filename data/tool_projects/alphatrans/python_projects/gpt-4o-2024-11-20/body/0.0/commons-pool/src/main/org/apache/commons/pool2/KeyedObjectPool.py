from __future__ import annotations
import re
from abc import ABC
import io
import typing
from typing import *
import os
from src.main.org.apache.commons.pool2.DestroyMode import *


class KeyedObjectPool(ABC):

    def returnObject(self, key: typing.Any, obj: typing.Any) -> None:
        # The method does not return anything, so we simply pass for now.
        pass

    def invalidateObject0(self, key: typing.Any, obj: typing.Any) -> None:
        raise Exception("This method needs to be implemented")

    def getNumIdle1(self, key: typing.Any) -> int:
        # Implementation would go here, but since the Java method is abstract,
        # we leave it as a placeholder (pass) in Python as well.
        pass

    def getNumIdle0(self) -> int:
        return 0

    def getNumActive1(self, key: typing.Any) -> int:
        # Implementation would go here, but since the Java method is abstract,
        # we leave it as a placeholder (pass) in Python as well.
        pass

    def getNumActive0(self) -> int:
        return 0

    def close(self) -> None:
        pass

    def clear1(self, key: typing.Any) -> None:
        raise NotImplementedError("This method should be implemented by subclasses")

    def clear0(self) -> None:
        raise Exception("Operation not supported")

    def borrowObject(self, key: typing.Any) -> typing.Any:
        raise Exception("Method not implemented")

    def addObject(self, key: typing.Any) -> None:
        raise Exception("Method not implemented")

    def invalidateObject1(
        self, key: typing.Any, obj: typing.Any, destroyMode: DestroyMode
    ) -> None:
        self.invalidateObject0(key, obj)

    def addObjects1(self, key: Any, count: int) -> None:
        if key is None:
            raise ValueError(PoolUtils.MSG_NULL_KEY)
        for _ in range(count):
            self.addObject(key)

    def addObjects0(self, keys: Collection[Any], count: int) -> None:
        if keys is None:
            raise ValueError(PoolUtils.MSG_NULL_KEYS)
        for key in keys:
            self.addObjects1(key, count)
