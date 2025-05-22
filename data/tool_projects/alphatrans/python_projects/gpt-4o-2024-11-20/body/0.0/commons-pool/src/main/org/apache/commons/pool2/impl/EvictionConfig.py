from __future__ import annotations
import time
import re
import os
import io
import datetime
from src.main.org.apache.commons.pool2.impl.PoolImplUtils import *


class EvictionConfig:

    __minIdle: int = 0

    __idleSoftEvictDuration: datetime.timedelta = None

    __idleEvictDuration: datetime.timedelta = None

    __MAX_DURATION: datetime.timedelta = datetime.timedelta.max

    def toString(self) -> str:
        builder = []
        builder.append("EvictionConfig [idleEvictDuration=")
        builder.append(str(self.__idleEvictDuration))
        builder.append(", idleSoftEvictDuration=")
        builder.append(str(self.__idleSoftEvictDuration))
        builder.append(", minIdle=")
        builder.append(str(self.__minIdle))
        builder.append("]")
        return "".join(builder)

    def getIdleSoftEvictTimeDuration(self) -> datetime.timedelta:
        return self.__idleSoftEvictDuration

    def getIdleSoftEvictTime(self) -> int:
        return int(self.__idleSoftEvictDuration.total_seconds() * 1000)

    def getIdleEvictTimeDuration(self) -> datetime.timedelta:
        return self.__idleEvictDuration

    def getIdleEvictTime(self) -> int:
        return int(self.__idleEvictDuration.total_seconds() * 1000)

    @staticmethod
    def EvictionConfig0(
        poolIdleEvictMillis: int, poolIdleSoftEvictMillis: int, minIdle: int
    ) -> EvictionConfig:
        return EvictionConfig(
            datetime.timedelta(milliseconds=poolIdleEvictMillis),
            datetime.timedelta(milliseconds=poolIdleSoftEvictMillis),
            minIdle,
        )

    def getMinIdle(self) -> int:
        return self.__minIdle

    def getIdleSoftEvictDuration(self) -> datetime.timedelta:
        return self.__idleSoftEvictDuration

    def getIdleEvictDuration(self) -> datetime.timedelta:
        return self.__idleEvictDuration

    def __init__(
        self,
        idleEvictDuration: datetime.timedelta,
        idleSoftEvictDuration: datetime.timedelta,
        minIdle: int,
    ) -> None:
        self.__idleEvictDuration = (
            idleEvictDuration
            if PoolImplUtils.isPositive(idleEvictDuration)
            else self.__MAX_DURATION
        )
        self.__idleSoftEvictDuration = (
            idleSoftEvictDuration
            if PoolImplUtils.isPositive(idleSoftEvictDuration)
            else self.__MAX_DURATION
        )
        self.__minIdle = minIdle
