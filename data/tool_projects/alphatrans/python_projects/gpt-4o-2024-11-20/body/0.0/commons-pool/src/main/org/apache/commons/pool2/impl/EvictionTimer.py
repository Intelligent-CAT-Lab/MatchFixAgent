from __future__ import annotations
import time
import re
import threading
import io
import typing
from typing import *
import datetime
from src.main.org.apache.commons.pool2.impl.BaseGenericObjectPool import *


class EvictionTimer:

    __taskMap: typing.Dict[weakref.ref, weakRunner] = {}

    __executor: typing.Union[
        concurrent.futures.ThreadPoolExecutor, concurrent.futures.Future
    ] = None

    def toString(self) -> str:
        builder = []
        builder.append("EvictionTimer []")
        return "".join(builder)

    @staticmethod
    def getNumTasks() -> int:
        return len(EvictionTimer.__taskMap)

    @staticmethod
    def cancel(
        evictor: Evictor[typing.Any], timeout: datetime.timedelta, restarting: bool
    ) -> None:
        if evictor is not None:
            evictor.cancel()
            EvictionTimer.__remove(evictor)

        if (
            not restarting
            and EvictionTimer.__executor is not None
            and not EvictionTimer.__taskMap
        ):
            EvictionTimer.__executor.shutdown(wait=True)
            try:
                EvictionTimer.__executor.awaitTermination(timeout.total_seconds())
            except InterruptedError:
                pass
            EvictionTimer.__executor._max_workers = (
                0  # Equivalent to setting core pool size to 0
            )
            EvictionTimer.__executor = None

    def __init__(self) -> None:
        pass

    @staticmethod
    def __remove(evictor: Evictor[typing.Any]) -> None:
        for key, value in list(EvictionTimer.__taskMap.items()):
            if key() == evictor:  # key() dereferences the weak reference
                EvictionTimer.__executor.remove(value)
                del EvictionTimer.__taskMap[key]
                break


class Reaper:

    def run(self) -> None:
        with threading.Lock():  # Synchronized block equivalent in Python
            for key, value in list(EvictionTimer.__taskMap.items()):
                if key() is None:  # Check if the weak reference is None
                    EvictionTimer.__executor.remove(value)
                    del EvictionTimer.__taskMap[key]

            if not EvictionTimer.__taskMap and EvictionTimer.__executor is not None:
                EvictionTimer.__executor.shutdown()
                EvictionTimer.__executor._max_workers = (
                    0  # Equivalent to setCorePoolSize(0)
                )
                EvictionTimer.__executor = None


class WeakRunner:

    __ref: weakref.ref = None

    def run(self) -> None:
        task = self.__ref()  # Retrieve the object referenced by the weak reference
        if task is not None:
            task.run()
        else:
            EvictionTimer.__executor.remove(self)
            EvictionTimer.__taskMap.pop(self.__ref, None)

    def __init__(self, ref: weakref.ref) -> None:
        self.__ref = ref
