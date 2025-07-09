from __future__ import annotations
import time
import re
import unittest
import pytest
from abc import ABC
import io
import typing
from typing import *
import datetime
import os
import unittest
from src.main.org.apache.commons.pool2.impl.PoolImplUtils import *
from src.main.org.apache.commons.pool2.BasePooledObjectFactory import *
from src.main.org.apache.commons.pool2.PooledObject import *


class TestPoolImplUtils(unittest.TestCase):

    __INSTANT_0: datetime.datetime = datetime.datetime.fromtimestamp(
        0, tz=datetime.timezone.utc
    )
    __INSTANT_1: datetime.datetime = datetime.datetime.fromtimestamp(0.001)

    def testToDuration_test0_decomposed(self) -> None:
        self.assertEqual(
            datetime.timedelta(0),
            PoolImplUtils.toDuration(0, datetime.timedelta(milliseconds=1)),
        )
        self.assertEqual(
            datetime.timedelta(milliseconds=1),
            PoolImplUtils.toDuration(1, datetime.timedelta(milliseconds=1)),
        )
        for time_unit in [
            datetime.timedelta(milliseconds=1),
            datetime.timedelta(seconds=1),
            datetime.timedelta(minutes=1),
            datetime.timedelta(hours=1),
            datetime.timedelta(days=1),
        ]:
            self.assertEqual(
                datetime.timedelta(0), PoolImplUtils.toDuration(0, time_unit)
            )

    def testToChronoUnit_test0_decomposed(self) -> None:
        self.assertEqual(
            datetime.timedelta(microseconds=1) / 1000,
            PoolImplUtils.toChronoUnit("NANOSECONDS"),
        )
        self.assertEqual(
            datetime.timedelta(microseconds=1),
            PoolImplUtils.toChronoUnit("MICROSECONDS"),
        )
        self.assertEqual(
            datetime.timedelta(milliseconds=1),
            PoolImplUtils.toChronoUnit("MILLISECONDS"),
        )
        self.assertEqual(
            datetime.timedelta(seconds=1), PoolImplUtils.toChronoUnit("SECONDS")
        )
        self.assertEqual(
            datetime.timedelta(minutes=1), PoolImplUtils.toChronoUnit("MINUTES")
        )
        self.assertEqual(
            datetime.timedelta(hours=1), PoolImplUtils.toChronoUnit("HOURS")
        )
        self.assertEqual(datetime.timedelta(days=1), PoolImplUtils.toChronoUnit("DAYS"))

    def testMinInstants_test0_decomposed(self) -> None:
        self.assertEqual(
            self.__INSTANT_0, PoolImplUtils.min(self.__INSTANT_0, self.__INSTANT_1)
        )
        self.assertEqual(
            self.__INSTANT_0, PoolImplUtils.min(self.__INSTANT_1, self.__INSTANT_0)
        )
        self.assertEqual(
            self.__INSTANT_1, PoolImplUtils.min(self.__INSTANT_1, self.__INSTANT_1)
        )
        self.assertEqual(
            self.__INSTANT_0, PoolImplUtils.min(self.__INSTANT_0, self.__INSTANT_0)
        )

    def testMaxInstants_test0_decomposed(self) -> None:
        self.assertEqual(
            self.__INSTANT_1, PoolImplUtils.max(self.__INSTANT_0, self.__INSTANT_1)
        )
        self.assertEqual(
            self.__INSTANT_1, PoolImplUtils.max(self.__INSTANT_1, self.__INSTANT_0)
        )
        self.assertEqual(
            self.__INSTANT_1, PoolImplUtils.max(self.__INSTANT_1, self.__INSTANT_1)
        )
        self.assertEqual(
            self.__INSTANT_0, PoolImplUtils.max(self.__INSTANT_0, self.__INSTANT_0)
        )

    def testFactoryTypeSimple_test1_decomposed(self) -> None:
        result = PoolImplUtils.getFactoryType(SimpleFactory)
        self.assertEqual(str, result)

    def testFactoryTypeSimple_test0_decomposed(self) -> None:
        result: Type[Any] = PoolImplUtils.getFactoryType(SimpleFactory)

    def testFactoryTypeNotSimple_test1_decomposed(self) -> None:
        result = PoolImplUtils.getFactoryType(NotSimpleFactory)
        self.assertEqual(Long, result)

    def testFactoryTypeNotSimple_test0_decomposed(self) -> None:
        result: Type[Any] = PoolImplUtils.getFactoryType(NotSimpleFactory)


class FactoryAB(BasePooledObjectFactory, ABC):

    pass


class FactoryBA(FactoryAB, ABC):

    pass


class FactoryC(FactoryBA, ABC):

    pass


class FactoryDE(FactoryC, ABC):

    pass


class FactoryF(FactoryDE, ABC):

    pass


class NotSimpleFactory(FactoryF):

    def wrap(self, obj: int) -> PooledObject[int]:
        return None

    def create(self) -> Optional[int]:
        return None


class SimpleFactory(BasePooledObjectFactory):

    def wrap(self, obj: str) -> PooledObject[str]:
        return None

    def create(self) -> str:
        return None
