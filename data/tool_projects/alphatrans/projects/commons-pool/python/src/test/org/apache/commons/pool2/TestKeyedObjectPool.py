from __future__ import annotations
import re
import unittest
import pytest
from abc import ABC
import io
import typing
from typing import *
import os
import unittest
from src.main.org.apache.commons.pool2.KeyedObjectPool import *
from src.main.org.apache.commons.pool2.KeyedPooledObjectFactory import *
from src.test.org.apache.commons.pool2.MethodCall import *
from src.main.org.apache.commons.pool2.PooledObject import *
from src.test.org.apache.commons.pool2.PrivateException import *


class TestKeyedObjectPool(ABC, unittest.TestCase):

    _KEY: str = "key"
    __ONE: int = 1
    __ZERO: int = 0
    __pool: KeyedObjectPool[object, typing.Any] = None

    def testBaseNumActiveNumIdle2_test36_decomposed(self) -> None:
        try:
            self.__pool = self._makeEmptyPool0(6)
        except NotImplementedError:
            return  # skip this test if unsupported

        keya = self._makeKey(0)
        keyb = self._makeKey(1)

        self.assertEqual(0, self.__pool.getNumActive0())
        self.assertEqual(0, self.__pool.getNumIdle0())
        self.assertEqual(0, self.__pool.getNumActive1(keya))
        self.assertEqual(0, self.__pool.getNumIdle1(keya))
        self.assertEqual(0, self.__pool.getNumActive1(keyb))
        self.assertEqual(0, self.__pool.getNumIdle1(keyb))

        objA0 = self.__pool.borrowObject(keya)
        objB0 = self.__pool.borrowObject(keyb)

        self.assertEqual(2, self.__pool.getNumActive0())
        self.assertEqual(0, self.__pool.getNumIdle0())
        self.assertEqual(1, self.__pool.getNumActive1(keya))
        self.assertEqual(0, self.__pool.getNumIdle1(keya))
        self.assertEqual(1, self.__pool.getNumActive1(keyb))
        self.assertEqual(0, self.__pool.getNumIdle1(keyb))

        objA1 = self.__pool.borrowObject(keya)
        objB1 = self.__pool.borrowObject(keyb)

        self.assertEqual(4, self.__pool.getNumActive0())
        self.assertEqual(0, self.__pool.getNumIdle0())
        self.assertEqual(2, self.__pool.getNumActive1(keya))
        self.assertEqual(0, self.__pool.getNumIdle1(keya))
        self.assertEqual(2, self.__pool.getNumActive1(keyb))
        self.assertEqual(0, self.__pool.getNumIdle1(keyb))

        self.__pool.returnObject(keya, objA0)
        self.__pool.returnObject(keyb, objB0)

        self.assertEqual(2, self.__pool.getNumActive0())
        self.assertEqual(2, self.__pool.getNumIdle0())
        self.assertEqual(1, self.__pool.getNumActive1(keya))
        self.assertEqual(1, self.__pool.getNumIdle1(keya))
        self.assertEqual(1, self.__pool.getNumActive1(keyb))
        self.assertEqual(1, self.__pool.getNumIdle1(keyb))

        self.__pool.returnObject(keya, objA1)
        self.__pool.returnObject(keyb, objB1)

        self.assertEqual(0, self.__pool.getNumActive0())
        self.assertEqual(4, self.__pool.getNumIdle0())
        self.assertEqual(0, self.__pool.getNumActive1(keya))
        self.assertEqual(2, self.__pool.getNumIdle1(keya))
        self.assertEqual(0, self.__pool.getNumActive1(keyb))
        self.assertEqual(2, self.__pool.getNumIdle1(keyb))

        self.__pool.close()

    def testBaseNumActiveNumIdle2_test35_decomposed(self) -> None:
        try:
            self.__pool = self._makeEmptyPool0(6)
        except NotImplementedError:
            return  # skip this test if unsupported

        keya = self._makeKey(0)
        keyb = self._makeKey(1)

        self.assertEqual(0, self.__pool.getNumActive0())
        self.assertEqual(0, self.__pool.getNumIdle0())
        self.assertEqual(0, self.__pool.getNumActive1(keya))
        self.assertEqual(0, self.__pool.getNumIdle1(keya))
        self.assertEqual(0, self.__pool.getNumActive1(keyb))
        self.assertEqual(0, self.__pool.getNumIdle1(keyb))

        objA0 = self.__pool.borrowObject(keya)
        objB0 = self.__pool.borrowObject(keyb)

        self.assertEqual(2, self.__pool.getNumActive0())
        self.assertEqual(0, self.__pool.getNumIdle0())
        self.assertEqual(1, self.__pool.getNumActive1(keya))
        self.assertEqual(0, self.__pool.getNumIdle1(keya))
        self.assertEqual(1, self.__pool.getNumActive1(keyb))
        self.assertEqual(0, self.__pool.getNumIdle1(keyb))

        objA1 = self.__pool.borrowObject(keya)
        objB1 = self.__pool.borrowObject(keyb)

        self.assertEqual(4, self.__pool.getNumActive0())
        self.assertEqual(0, self.__pool.getNumIdle0())
        self.assertEqual(2, self.__pool.getNumActive1(keya))
        self.assertEqual(0, self.__pool.getNumIdle1(keya))
        self.assertEqual(2, self.__pool.getNumActive1(keyb))
        self.assertEqual(0, self.__pool.getNumIdle1(keyb))

        self.__pool.returnObject(keya, objA0)
        self.__pool.returnObject(keyb, objB0)

        self.assertEqual(2, self.__pool.getNumActive0())
        self.assertEqual(2, self.__pool.getNumIdle0())
        self.assertEqual(1, self.__pool.getNumActive1(keya))
        self.assertEqual(1, self.__pool.getNumIdle1(keya))
        self.assertEqual(1, self.__pool.getNumActive1(keyb))
        self.assertEqual(1, self.__pool.getNumIdle1(keyb))

        self.__pool.returnObject(keya, objA1)
        self.__pool.returnObject(keyb, objB1)

        self.assertEqual(0, self.__pool.getNumActive0())
        self.assertEqual(4, self.__pool.getNumIdle0())
        self.assertEqual(0, self.__pool.getNumActive1(keya))
        self.assertEqual(2, self.__pool.getNumIdle1(keya))
        self.assertEqual(0, self.__pool.getNumActive1(keyb))
        self.assertEqual(2, self.__pool.getNumIdle1(keyb))

    def testBaseNumActiveNumIdle2_test34_decomposed(self) -> None:
        try:
            self.__pool = self._makeEmptyPool0(6)
        except NotImplementedError:
            return  # skip this test if unsupported

        keya = self._makeKey(0)
        keyb = self._makeKey(1)

        self.assertEqual(0, self.__pool.getNumActive0())
        self.assertEqual(0, self.__pool.getNumIdle0())
        self.assertEqual(0, self.__pool.getNumActive1(keya))
        self.assertEqual(0, self.__pool.getNumIdle1(keya))
        self.assertEqual(0, self.__pool.getNumActive1(keyb))
        self.assertEqual(0, self.__pool.getNumIdle1(keyb))

        objA0 = self.__pool.borrowObject(keya)
        objB0 = self.__pool.borrowObject(keyb)

        self.assertEqual(2, self.__pool.getNumActive0())
        self.assertEqual(0, self.__pool.getNumIdle0())
        self.assertEqual(1, self.__pool.getNumActive1(keya))
        self.assertEqual(0, self.__pool.getNumIdle1(keya))
        self.assertEqual(1, self.__pool.getNumActive1(keyb))
        self.assertEqual(0, self.__pool.getNumIdle1(keyb))

        objA1 = self.__pool.borrowObject(keya)
        objB1 = self.__pool.borrowObject(keyb)

        self.assertEqual(4, self.__pool.getNumActive0())
        self.assertEqual(0, self.__pool.getNumIdle0())
        self.assertEqual(2, self.__pool.getNumActive1(keya))
        self.assertEqual(0, self.__pool.getNumIdle1(keya))
        self.assertEqual(2, self.__pool.getNumActive1(keyb))
        self.assertEqual(0, self.__pool.getNumIdle1(keyb))

        self.__pool.returnObject(keya, objA0)
        self.__pool.returnObject(keyb, objB0)

        self.assertEqual(2, self.__pool.getNumActive0())
        self.assertEqual(2, self.__pool.getNumIdle0())
        self.assertEqual(1, self.__pool.getNumActive1(keya))
        self.assertEqual(1, self.__pool.getNumIdle1(keya))
        self.assertEqual(1, self.__pool.getNumActive1(keyb))
        self.assertEqual(1, self.__pool.getNumIdle1(keyb))

        self.__pool.returnObject(keya, objA1)
        self.__pool.returnObject(keyb, objB1)

        self.assertEqual(0, self.__pool.getNumActive0())
        self.assertEqual(4, self.__pool.getNumIdle0())
        self.assertEqual(0, self.__pool.getNumActive1(keya))
        self.assertEqual(2, self.__pool.getNumIdle1(keya))
        self.assertEqual(0, self.__pool.getNumActive1(keyb))

    def testBaseNumActiveNumIdle2_test33_decomposed(self) -> None:
        try:
            self.__pool = self._makeEmptyPool0(6)
        except NotImplementedError:
            return  # skip this test if unsupported

        keya = self._makeKey(0)
        keyb = self._makeKey(1)

        self.assertEqual(0, self.__pool.getNumActive0())
        self.assertEqual(0, self.__pool.getNumIdle0())
        self.assertEqual(0, self.__pool.getNumActive1(keya))
        self.assertEqual(0, self.__pool.getNumIdle1(keya))
        self.assertEqual(0, self.__pool.getNumActive1(keyb))
        self.assertEqual(0, self.__pool.getNumIdle1(keyb))

        objA0 = self.__pool.borrowObject(keya)
        objB0 = self.__pool.borrowObject(keyb)

        self.assertEqual(2, self.__pool.getNumActive0())
        self.assertEqual(0, self.__pool.getNumIdle0())
        self.assertEqual(1, self.__pool.getNumActive1(keya))
        self.assertEqual(0, self.__pool.getNumIdle1(keya))
        self.assertEqual(1, self.__pool.getNumActive1(keyb))
        self.assertEqual(0, self.__pool.getNumIdle1(keyb))

        objA1 = self.__pool.borrowObject(keya)
        objB1 = self.__pool.borrowObject(keyb)

        self.assertEqual(4, self.__pool.getNumActive0())
        self.assertEqual(0, self.__pool.getNumIdle0())
        self.assertEqual(2, self.__pool.getNumActive1(keya))
        self.assertEqual(0, self.__pool.getNumIdle1(keya))
        self.assertEqual(2, self.__pool.getNumActive1(keyb))
        self.assertEqual(0, self.__pool.getNumIdle1(keyb))

        self.__pool.returnObject(keya, objA0)
        self.__pool.returnObject(keyb, objB0)

        self.assertEqual(2, self.__pool.getNumActive0())
        self.assertEqual(2, self.__pool.getNumIdle0())
        self.assertEqual(1, self.__pool.getNumActive1(keya))
        self.assertEqual(1, self.__pool.getNumIdle1(keya))
        self.assertEqual(1, self.__pool.getNumActive1(keyb))
        self.assertEqual(1, self.__pool.getNumIdle1(keyb))

        self.__pool.returnObject(keya, objA1)
        self.__pool.returnObject(keyb, objB1)

        self.assertEqual(0, self.__pool.getNumActive0())
        self.assertEqual(4, self.__pool.getNumIdle0())
        self.assertEqual(0, self.__pool.getNumActive1(keya))
        self.assertEqual(2, self.__pool.getNumIdle1(keya))

    def testBaseNumActiveNumIdle2_test32_decomposed(self) -> None:
        try:
            self.__pool = self._makeEmptyPool0(6)
        except NotImplementedError:
            return  # skip this test if unsupported

        keya = self._makeKey(0)
        keyb = self._makeKey(1)

        self.assertEqual(0, self.__pool.getNumActive0())
        self.assertEqual(0, self.__pool.getNumIdle0())
        self.assertEqual(0, self.__pool.getNumActive1(keya))
        self.assertEqual(0, self.__pool.getNumIdle1(keya))
        self.assertEqual(0, self.__pool.getNumActive1(keyb))
        self.assertEqual(0, self.__pool.getNumIdle1(keyb))

        objA0 = self.__pool.borrowObject(keya)
        objB0 = self.__pool.borrowObject(keyb)

        self.assertEqual(2, self.__pool.getNumActive0())
        self.assertEqual(0, self.__pool.getNumIdle0())
        self.assertEqual(1, self.__pool.getNumActive1(keya))
        self.assertEqual(0, self.__pool.getNumIdle1(keya))
        self.assertEqual(1, self.__pool.getNumActive1(keyb))
        self.assertEqual(0, self.__pool.getNumIdle1(keyb))

        objA1 = self.__pool.borrowObject(keya)
        objB1 = self.__pool.borrowObject(keyb)

        self.assertEqual(4, self.__pool.getNumActive0())
        self.assertEqual(0, self.__pool.getNumIdle0())
        self.assertEqual(2, self.__pool.getNumActive1(keya))
        self.assertEqual(0, self.__pool.getNumIdle1(keya))
        self.assertEqual(2, self.__pool.getNumActive1(keyb))
        self.assertEqual(0, self.__pool.getNumIdle1(keyb))

        self.__pool.returnObject(keya, objA0)
        self.__pool.returnObject(keyb, objB0)

        self.assertEqual(2, self.__pool.getNumActive0())
        self.assertEqual(2, self.__pool.getNumIdle0())
        self.assertEqual(1, self.__pool.getNumActive1(keya))
        self.assertEqual(1, self.__pool.getNumIdle1(keya))
        self.assertEqual(1, self.__pool.getNumActive1(keyb))
        self.assertEqual(1, self.__pool.getNumIdle1(keyb))

        self.__pool.returnObject(keya, objA1)
        self.__pool.returnObject(keyb, objB1)

        self.assertEqual(0, self.__pool.getNumActive0())
        self.assertEqual(4, self.__pool.getNumIdle0())
        self.assertEqual(0, self.__pool.getNumActive1(keya))

    def testBaseNumActiveNumIdle2_test31_decomposed(self) -> None:
        try:
            self.__pool = self._makeEmptyPool0(6)
        except NotImplementedError:
            return  # skip this test if unsupported

        keya = self._makeKey(0)
        keyb = self._makeKey(1)

        self.assertEqual(0, self.__pool.getNumActive0())
        self.assertEqual(0, self.__pool.getNumIdle0())
        self.assertEqual(0, self.__pool.getNumActive1(keya))
        self.assertEqual(0, self.__pool.getNumIdle1(keya))
        self.assertEqual(0, self.__pool.getNumActive1(keyb))
        self.assertEqual(0, self.__pool.getNumIdle1(keyb))

        objA0 = self.__pool.borrowObject(keya)
        objB0 = self.__pool.borrowObject(keyb)

        self.assertEqual(2, self.__pool.getNumActive0())
        self.assertEqual(0, self.__pool.getNumIdle0())
        self.assertEqual(1, self.__pool.getNumActive1(keya))
        self.assertEqual(0, self.__pool.getNumIdle1(keya))
        self.assertEqual(1, self.__pool.getNumActive1(keyb))
        self.assertEqual(0, self.__pool.getNumIdle1(keyb))

        objA1 = self.__pool.borrowObject(keya)
        objB1 = self.__pool.borrowObject(keyb)

        self.assertEqual(4, self.__pool.getNumActive0())
        self.assertEqual(0, self.__pool.getNumIdle0())
        self.assertEqual(2, self.__pool.getNumActive1(keya))
        self.assertEqual(0, self.__pool.getNumIdle1(keya))
        self.assertEqual(2, self.__pool.getNumActive1(keyb))
        self.assertEqual(0, self.__pool.getNumIdle1(keyb))

        self.__pool.returnObject(keya, objA0)
        self.__pool.returnObject(keyb, objB0)

        self.assertEqual(2, self.__pool.getNumActive0())
        self.assertEqual(2, self.__pool.getNumIdle0())
        self.assertEqual(1, self.__pool.getNumActive1(keya))
        self.assertEqual(1, self.__pool.getNumIdle1(keya))
        self.assertEqual(1, self.__pool.getNumActive1(keyb))
        self.assertEqual(1, self.__pool.getNumIdle1(keyb))

        self.__pool.returnObject(keya, objA1)
        self.__pool.returnObject(keyb, objB1)

        self.assertEqual(0, self.__pool.getNumActive0())
        self.assertEqual(4, self.__pool.getNumIdle0())

    def testBaseNumActiveNumIdle2_test30_decomposed(self) -> None:
        try:
            self.__pool = self._makeEmptyPool0(6)
        except NotImplementedError:
            return  # skip this test if unsupported

        keya = self._makeKey(0)
        keyb = self._makeKey(1)

        self.assertEqual(0, self.__pool.getNumActive0())
        self.assertEqual(0, self.__pool.getNumIdle0())
        self.assertEqual(0, self.__pool.getNumActive1(keya))
        self.assertEqual(0, self.__pool.getNumIdle1(keya))
        self.assertEqual(0, self.__pool.getNumActive1(keyb))
        self.assertEqual(0, self.__pool.getNumIdle1(keyb))

        objA0 = self.__pool.borrowObject(keya)
        objB0 = self.__pool.borrowObject(keyb)

        self.assertEqual(2, self.__pool.getNumActive0())
        self.assertEqual(0, self.__pool.getNumIdle0())
        self.assertEqual(1, self.__pool.getNumActive1(keya))
        self.assertEqual(0, self.__pool.getNumIdle1(keya))
        self.assertEqual(1, self.__pool.getNumActive1(keyb))
        self.assertEqual(0, self.__pool.getNumIdle1(keyb))

        objA1 = self.__pool.borrowObject(keya)
        objB1 = self.__pool.borrowObject(keyb)

        self.assertEqual(4, self.__pool.getNumActive0())
        self.assertEqual(0, self.__pool.getNumIdle0())
        self.assertEqual(2, self.__pool.getNumActive1(keya))
        self.assertEqual(0, self.__pool.getNumIdle1(keya))
        self.assertEqual(2, self.__pool.getNumActive1(keyb))
        self.assertEqual(0, self.__pool.getNumIdle1(keyb))

        self.__pool.returnObject(keya, objA0)
        self.__pool.returnObject(keyb, objB0)

        self.assertEqual(2, self.__pool.getNumActive0())
        self.assertEqual(2, self.__pool.getNumIdle0())
        self.assertEqual(1, self.__pool.getNumActive1(keya))
        self.assertEqual(1, self.__pool.getNumIdle1(keya))
        self.assertEqual(1, self.__pool.getNumActive1(keyb))
        self.assertEqual(1, self.__pool.getNumIdle1(keyb))

        self.__pool.returnObject(keya, objA1)
        self.__pool.returnObject(keyb, objB1)

        self.assertEqual(0, self.__pool.getNumActive0())

    def testBaseNumActiveNumIdle2_test29_decomposed(self) -> None:
        try:
            self.__pool = self._makeEmptyPool0(6)
        except NotImplementedError:
            return  # skip this test if unsupported

        keya = self._makeKey(0)
        keyb = self._makeKey(1)

        self.assertEqual(0, self.__pool.getNumActive0())
        self.assertEqual(0, self.__pool.getNumIdle0())
        self.assertEqual(0, self.__pool.getNumActive1(keya))
        self.assertEqual(0, self.__pool.getNumIdle1(keya))
        self.assertEqual(0, self.__pool.getNumActive1(keyb))
        self.assertEqual(0, self.__pool.getNumIdle1(keyb))

        objA0 = self.__pool.borrowObject(keya)
        objB0 = self.__pool.borrowObject(keyb)

        self.assertEqual(2, self.__pool.getNumActive0())
        self.assertEqual(0, self.__pool.getNumIdle0())
        self.assertEqual(1, self.__pool.getNumActive1(keya))
        self.assertEqual(0, self.__pool.getNumIdle1(keya))
        self.assertEqual(1, self.__pool.getNumActive1(keyb))
        self.assertEqual(0, self.__pool.getNumIdle1(keyb))

        objA1 = self.__pool.borrowObject(keya)
        objB1 = self.__pool.borrowObject(keyb)

        self.assertEqual(4, self.__pool.getNumActive0())
        self.assertEqual(0, self.__pool.getNumIdle0())
        self.assertEqual(2, self.__pool.getNumActive1(keya))
        self.assertEqual(0, self.__pool.getNumIdle1(keya))
        self.assertEqual(2, self.__pool.getNumActive1(keyb))
        self.assertEqual(0, self.__pool.getNumIdle1(keyb))

        self.__pool.returnObject(keya, objA0)
        self.__pool.returnObject(keyb, objB0)

        self.assertEqual(2, self.__pool.getNumActive0())
        self.assertEqual(2, self.__pool.getNumIdle0())
        self.assertEqual(1, self.__pool.getNumActive1(keya))
        self.assertEqual(1, self.__pool.getNumIdle1(keya))
        self.assertEqual(1, self.__pool.getNumActive1(keyb))
        self.assertEqual(1, self.__pool.getNumIdle1(keyb))

        self.__pool.returnObject(keya, objA1)
        self.__pool.returnObject(keyb, objB1)

    def testBaseNumActiveNumIdle2_test28_decomposed(self) -> None:
        try:
            self.__pool = self._makeEmptyPool0(6)
        except NotImplementedError:
            return  # skip this test if unsupported

        keya = self._makeKey(0)
        keyb = self._makeKey(1)

        self.assertEqual(0, self.__pool.getNumActive0())
        self.assertEqual(0, self.__pool.getNumIdle0())
        self.assertEqual(0, self.__pool.getNumActive1(keya))
        self.assertEqual(0, self.__pool.getNumIdle1(keya))
        self.assertEqual(0, self.__pool.getNumActive1(keyb))
        self.assertEqual(0, self.__pool.getNumIdle1(keyb))

        objA0 = self.__pool.borrowObject(keya)
        objB0 = self.__pool.borrowObject(keyb)

        self.assertEqual(2, self.__pool.getNumActive0())
        self.assertEqual(0, self.__pool.getNumIdle0())
        self.assertEqual(1, self.__pool.getNumActive1(keya))
        self.assertEqual(0, self.__pool.getNumIdle1(keya))
        self.assertEqual(1, self.__pool.getNumActive1(keyb))
        self.assertEqual(0, self.__pool.getNumIdle1(keyb))

        objA1 = self.__pool.borrowObject(keya)
        objB1 = self.__pool.borrowObject(keyb)

        self.assertEqual(4, self.__pool.getNumActive0())
        self.assertEqual(0, self.__pool.getNumIdle0())
        self.assertEqual(2, self.__pool.getNumActive1(keya))
        self.assertEqual(0, self.__pool.getNumIdle1(keya))
        self.assertEqual(2, self.__pool.getNumActive1(keyb))
        self.assertEqual(0, self.__pool.getNumIdle1(keyb))

        self.__pool.returnObject(keya, objA0)
        self.__pool.returnObject(keyb, objB0)

        self.assertEqual(2, self.__pool.getNumActive0())
        self.assertEqual(2, self.__pool.getNumIdle0())
        self.assertEqual(1, self.__pool.getNumActive1(keya))
        self.assertEqual(1, self.__pool.getNumIdle1(keya))
        self.assertEqual(1, self.__pool.getNumActive1(keyb))
        self.assertEqual(1, self.__pool.getNumIdle1(keyb))

    def testBaseNumActiveNumIdle2_test27_decomposed(self) -> None:
        try:
            self.__pool = self._makeEmptyPool0(6)
        except NotImplementedError:
            return  # skip this test if unsupported

        keya = self._makeKey(0)
        keyb = self._makeKey(1)

        self.assertEqual(0, self.__pool.getNumActive0())
        self.assertEqual(0, self.__pool.getNumIdle0())
        self.assertEqual(0, self.__pool.getNumActive1(keya))
        self.assertEqual(0, self.__pool.getNumIdle1(keya))
        self.assertEqual(0, self.__pool.getNumActive1(keyb))
        self.assertEqual(0, self.__pool.getNumIdle1(keyb))

        objA0 = self.__pool.borrowObject(keya)
        objB0 = self.__pool.borrowObject(keyb)

        self.assertEqual(2, self.__pool.getNumActive0())
        self.assertEqual(0, self.__pool.getNumIdle0())
        self.assertEqual(1, self.__pool.getNumActive1(keya))
        self.assertEqual(0, self.__pool.getNumIdle1(keya))
        self.assertEqual(1, self.__pool.getNumActive1(keyb))
        self.assertEqual(0, self.__pool.getNumIdle1(keyb))

        objA1 = self.__pool.borrowObject(keya)
        objB1 = self.__pool.borrowObject(keyb)

        self.assertEqual(4, self.__pool.getNumActive0())
        self.assertEqual(0, self.__pool.getNumIdle0())
        self.assertEqual(2, self.__pool.getNumActive1(keya))
        self.assertEqual(0, self.__pool.getNumIdle1(keya))
        self.assertEqual(2, self.__pool.getNumActive1(keyb))
        self.assertEqual(0, self.__pool.getNumIdle1(keyb))

        self.__pool.returnObject(keya, objA0)
        self.__pool.returnObject(keyb, objB0)

        self.assertEqual(2, self.__pool.getNumActive0())
        self.assertEqual(2, self.__pool.getNumIdle0())
        self.assertEqual(1, self.__pool.getNumActive1(keya))
        self.assertEqual(1, self.__pool.getNumIdle1(keya))
        self.assertEqual(1, self.__pool.getNumActive1(keyb))

    def testBaseNumActiveNumIdle2_test26_decomposed(self) -> None:
        try:
            self.__pool = self._makeEmptyPool0(6)
        except NotImplementedError:
            return  # skip this test if unsupported

        keya = self._makeKey(0)
        keyb = self._makeKey(1)

        self.assertEqual(0, self.__pool.getNumActive0())
        self.assertEqual(0, self.__pool.getNumIdle0())
        self.assertEqual(0, self.__pool.getNumActive1(keya))
        self.assertEqual(0, self.__pool.getNumIdle1(keya))
        self.assertEqual(0, self.__pool.getNumActive1(keyb))
        self.assertEqual(0, self.__pool.getNumIdle1(keyb))

        objA0 = self.__pool.borrowObject(keya)
        objB0 = self.__pool.borrowObject(keyb)

        self.assertEqual(2, self.__pool.getNumActive0())
        self.assertEqual(0, self.__pool.getNumIdle0())
        self.assertEqual(1, self.__pool.getNumActive1(keya))
        self.assertEqual(0, self.__pool.getNumIdle1(keya))
        self.assertEqual(1, self.__pool.getNumActive1(keyb))
        self.assertEqual(0, self.__pool.getNumIdle1(keyb))

        objA1 = self.__pool.borrowObject(keya)
        objB1 = self.__pool.borrowObject(keyb)

        self.assertEqual(4, self.__pool.getNumActive0())
        self.assertEqual(0, self.__pool.getNumIdle0())
        self.assertEqual(2, self.__pool.getNumActive1(keya))
        self.assertEqual(0, self.__pool.getNumIdle1(keya))
        self.assertEqual(2, self.__pool.getNumActive1(keyb))
        self.assertEqual(0, self.__pool.getNumIdle1(keyb))

        self.__pool.returnObject(keya, objA0)
        self.__pool.returnObject(keyb, objB0)

        self.assertEqual(2, self.__pool.getNumActive0())
        self.assertEqual(2, self.__pool.getNumIdle0())
        self.assertEqual(1, self.__pool.getNumActive1(keya))
        self.assertEqual(1, self.__pool.getNumIdle1(keya))

    def testBaseNumActiveNumIdle2_test25_decomposed(self) -> None:
        try:
            self.__pool = self._makeEmptyPool0(6)
        except NotImplementedError:
            return  # skip this test if unsupported

        keya = self._makeKey(0)
        keyb = self._makeKey(1)

        self.assertEqual(0, self.__pool.getNumActive0())
        self.assertEqual(0, self.__pool.getNumIdle0())
        self.assertEqual(0, self.__pool.getNumActive1(keya))
        self.assertEqual(0, self.__pool.getNumIdle1(keya))
        self.assertEqual(0, self.__pool.getNumActive1(keyb))
        self.assertEqual(0, self.__pool.getNumIdle1(keyb))

        objA0 = self.__pool.borrowObject(keya)
        objB0 = self.__pool.borrowObject(keyb)

        self.assertEqual(2, self.__pool.getNumActive0())
        self.assertEqual(0, self.__pool.getNumIdle0())
        self.assertEqual(1, self.__pool.getNumActive1(keya))
        self.assertEqual(0, self.__pool.getNumIdle1(keya))
        self.assertEqual(1, self.__pool.getNumActive1(keyb))
        self.assertEqual(0, self.__pool.getNumIdle1(keyb))

        objA1 = self.__pool.borrowObject(keya)
        objB1 = self.__pool.borrowObject(keyb)

        self.assertEqual(4, self.__pool.getNumActive0())
        self.assertEqual(0, self.__pool.getNumIdle0())
        self.assertEqual(2, self.__pool.getNumActive1(keya))
        self.assertEqual(0, self.__pool.getNumIdle1(keya))
        self.assertEqual(2, self.__pool.getNumActive1(keyb))
        self.assertEqual(0, self.__pool.getNumIdle1(keyb))

        self.__pool.returnObject(keya, objA0)
        self.__pool.returnObject(keyb, objB0)

        self.assertEqual(2, self.__pool.getNumActive0())
        self.assertEqual(2, self.__pool.getNumIdle0())
        self.assertEqual(1, self.__pool.getNumActive1(keya))

    def testBaseNumActiveNumIdle2_test24_decomposed(self) -> None:
        try:
            self.__pool = self._makeEmptyPool0(6)
        except NotImplementedError:
            return  # skip this test if unsupported

        keya = self._makeKey(0)
        keyb = self._makeKey(1)

        self.assertEqual(0, self.__pool.getNumActive0())
        self.assertEqual(0, self.__pool.getNumIdle0())
        self.assertEqual(0, self.__pool.getNumActive1(keya))
        self.assertEqual(0, self.__pool.getNumIdle1(keya))
        self.assertEqual(0, self.__pool.getNumActive1(keyb))
        self.assertEqual(0, self.__pool.getNumIdle1(keyb))

        objA0 = self.__pool.borrowObject(keya)
        objB0 = self.__pool.borrowObject(keyb)

        self.assertEqual(2, self.__pool.getNumActive0())
        self.assertEqual(0, self.__pool.getNumIdle0())
        self.assertEqual(1, self.__pool.getNumActive1(keya))
        self.assertEqual(0, self.__pool.getNumIdle1(keya))
        self.assertEqual(1, self.__pool.getNumActive1(keyb))
        self.assertEqual(0, self.__pool.getNumIdle1(keyb))

        objA1 = self.__pool.borrowObject(keya)
        objB1 = self.__pool.borrowObject(keyb)

        self.assertEqual(4, self.__pool.getNumActive0())
        self.assertEqual(0, self.__pool.getNumIdle0())
        self.assertEqual(2, self.__pool.getNumActive1(keya))
        self.assertEqual(0, self.__pool.getNumIdle1(keya))
        self.assertEqual(2, self.__pool.getNumActive1(keyb))
        self.assertEqual(0, self.__pool.getNumIdle1(keyb))

        self.__pool.returnObject(keya, objA0)
        self.__pool.returnObject(keyb, objB0)

        self.assertEqual(2, self.__pool.getNumActive0())
        self.assertEqual(2, self.__pool.getNumIdle0())

    def testBaseNumActiveNumIdle2_test23_decomposed(self) -> None:
        try:
            self.__pool = self._makeEmptyPool0(6)
        except NotImplementedError:
            return  # skip this test if unsupported

        keya = self._makeKey(0)
        keyb = self._makeKey(1)

        self.assertEqual(0, self.__pool.getNumActive0())
        self.assertEqual(0, self.__pool.getNumIdle0())
        self.assertEqual(0, self.__pool.getNumActive1(keya))
        self.assertEqual(0, self.__pool.getNumIdle1(keya))
        self.assertEqual(0, self.__pool.getNumActive1(keyb))
        self.assertEqual(0, self.__pool.getNumIdle1(keyb))

        objA0 = self.__pool.borrowObject(keya)
        objB0 = self.__pool.borrowObject(keyb)

        self.assertEqual(2, self.__pool.getNumActive0())
        self.assertEqual(0, self.__pool.getNumIdle0())
        self.assertEqual(1, self.__pool.getNumActive1(keya))
        self.assertEqual(0, self.__pool.getNumIdle1(keya))
        self.assertEqual(1, self.__pool.getNumActive1(keyb))
        self.assertEqual(0, self.__pool.getNumIdle1(keyb))

        objA1 = self.__pool.borrowObject(keya)
        objB1 = self.__pool.borrowObject(keyb)

        self.assertEqual(4, self.__pool.getNumActive0())
        self.assertEqual(0, self.__pool.getNumIdle0())
        self.assertEqual(2, self.__pool.getNumActive1(keya))
        self.assertEqual(0, self.__pool.getNumIdle1(keya))
        self.assertEqual(2, self.__pool.getNumActive1(keyb))
        self.assertEqual(0, self.__pool.getNumIdle1(keyb))

        self.__pool.returnObject(keya, objA0)
        self.__pool.returnObject(keyb, objB0)

        self.assertEqual(2, self.__pool.getNumActive0())

    def testBaseNumActiveNumIdle2_test22_decomposed(self) -> None:
        try:
            self.__pool = self._makeEmptyPool0(6)
        except NotImplementedError:
            return  # skip this test if unsupported

        keya = self._makeKey(0)
        keyb = self._makeKey(1)

        self.assertEqual(0, self.__pool.getNumActive0())
        self.assertEqual(0, self.__pool.getNumIdle0())
        self.assertEqual(0, self.__pool.getNumActive1(keya))
        self.assertEqual(0, self.__pool.getNumIdle1(keya))
        self.assertEqual(0, self.__pool.getNumActive1(keyb))
        self.assertEqual(0, self.__pool.getNumIdle1(keyb))

        objA0 = self.__pool.borrowObject(keya)
        objB0 = self.__pool.borrowObject(keyb)

        self.assertEqual(2, self.__pool.getNumActive0())
        self.assertEqual(0, self.__pool.getNumIdle0())
        self.assertEqual(1, self.__pool.getNumActive1(keya))
        self.assertEqual(0, self.__pool.getNumIdle1(keya))
        self.assertEqual(1, self.__pool.getNumActive1(keyb))
        self.assertEqual(0, self.__pool.getNumIdle1(keyb))

        objA1 = self.__pool.borrowObject(keya)
        objB1 = self.__pool.borrowObject(keyb)

        self.assertEqual(4, self.__pool.getNumActive0())
        self.assertEqual(0, self.__pool.getNumIdle0())
        self.assertEqual(2, self.__pool.getNumActive1(keya))
        self.assertEqual(0, self.__pool.getNumIdle1(keya))
        self.assertEqual(2, self.__pool.getNumActive1(keyb))
        self.assertEqual(0, self.__pool.getNumIdle1(keyb))

        self.__pool.returnObject(keya, objA0)
        self.__pool.returnObject(keyb, objB0)

    def testBaseNumActiveNumIdle2_test21_decomposed(self) -> None:
        try:
            self.__pool = self._makeEmptyPool0(6)
        except NotImplementedError:
            return  # skip this test if unsupported

        keya = self._makeKey(0)
        keyb = self._makeKey(1)

        self.assertEqual(0, self.__pool.getNumActive0())
        self.assertEqual(0, self.__pool.getNumIdle0())
        self.assertEqual(0, self.__pool.getNumActive1(keya))
        self.assertEqual(0, self.__pool.getNumIdle1(keya))
        self.assertEqual(0, self.__pool.getNumActive1(keyb))
        self.assertEqual(0, self.__pool.getNumIdle1(keyb))

        objA0 = self.__pool.borrowObject(keya)
        objB0 = self.__pool.borrowObject(keyb)

        self.assertEqual(2, self.__pool.getNumActive0())
        self.assertEqual(0, self.__pool.getNumIdle0())
        self.assertEqual(1, self.__pool.getNumActive1(keya))
        self.assertEqual(0, self.__pool.getNumIdle1(keya))
        self.assertEqual(1, self.__pool.getNumActive1(keyb))
        self.assertEqual(0, self.__pool.getNumIdle1(keyb))

        objA1 = self.__pool.borrowObject(keya)
        objB1 = self.__pool.borrowObject(keyb)

        self.assertEqual(4, self.__pool.getNumActive0())
        self.assertEqual(0, self.__pool.getNumIdle0())
        self.assertEqual(2, self.__pool.getNumActive1(keya))
        self.assertEqual(0, self.__pool.getNumIdle1(keya))
        self.assertEqual(2, self.__pool.getNumActive1(keyb))
        self.assertEqual(0, self.__pool.getNumIdle1(keyb))

    def testBaseNumActiveNumIdle2_test20_decomposed(self) -> None:
        try:
            self.__pool = self._makeEmptyPool0(6)
        except NotImplementedError:
            return  # skip this test if unsupported

        keya = self._makeKey(0)
        keyb = self._makeKey(1)

        self.assertEqual(0, self.__pool.getNumActive0())
        self.assertEqual(0, self.__pool.getNumIdle0())
        self.assertEqual(0, self.__pool.getNumActive1(keya))
        self.assertEqual(0, self.__pool.getNumIdle1(keya))
        self.assertEqual(0, self.__pool.getNumActive1(keyb))
        self.assertEqual(0, self.__pool.getNumIdle1(keyb))

        objA0 = self.__pool.borrowObject(keya)
        objB0 = self.__pool.borrowObject(keyb)

        self.assertEqual(2, self.__pool.getNumActive0())
        self.assertEqual(0, self.__pool.getNumIdle0())
        self.assertEqual(1, self.__pool.getNumActive1(keya))
        self.assertEqual(0, self.__pool.getNumIdle1(keya))
        self.assertEqual(1, self.__pool.getNumActive1(keyb))
        self.assertEqual(0, self.__pool.getNumIdle1(keyb))

        objA1 = self.__pool.borrowObject(keya)
        objB1 = self.__pool.borrowObject(keyb)

        self.assertEqual(4, self.__pool.getNumActive0())
        self.assertEqual(0, self.__pool.getNumIdle0())
        self.assertEqual(2, self.__pool.getNumActive1(keya))
        self.assertEqual(0, self.__pool.getNumIdle1(keya))
        self.assertEqual(2, self.__pool.getNumActive1(keyb))

    def testBaseNumActiveNumIdle2_test19_decomposed(self) -> None:
        try:
            self.__pool = self._makeEmptyPool0(6)
        except NotImplementedError:
            return  # skip this test if unsupported

        keya = self._makeKey(0)
        keyb = self._makeKey(1)

        self.assertEqual(0, self.__pool.getNumActive0())
        self.assertEqual(0, self.__pool.getNumIdle0())
        self.assertEqual(0, self.__pool.getNumActive1(keya))
        self.assertEqual(0, self.__pool.getNumIdle1(keya))
        self.assertEqual(0, self.__pool.getNumActive1(keyb))
        self.assertEqual(0, self.__pool.getNumIdle1(keyb))

        objA0 = self.__pool.borrowObject(keya)
        objB0 = self.__pool.borrowObject(keyb)

        self.assertEqual(2, self.__pool.getNumActive0())
        self.assertEqual(0, self.__pool.getNumIdle0())
        self.assertEqual(1, self.__pool.getNumActive1(keya))
        self.assertEqual(0, self.__pool.getNumIdle1(keya))
        self.assertEqual(1, self.__pool.getNumActive1(keyb))
        self.assertEqual(0, self.__pool.getNumIdle1(keyb))

        objA1 = self.__pool.borrowObject(keya)
        objB1 = self.__pool.borrowObject(keyb)

        self.assertEqual(4, self.__pool.getNumActive0())
        self.assertEqual(0, self.__pool.getNumIdle0())
        self.assertEqual(2, self.__pool.getNumActive1(keya))
        self.assertEqual(0, self.__pool.getNumIdle1(keya))

    def testBaseNumActiveNumIdle2_test18_decomposed(self) -> None:
        try:
            self.__pool = self._makeEmptyPool0(6)
        except NotImplementedError:
            return  # skip this test if unsupported

        keya = self._makeKey(0)
        keyb = self._makeKey(1)

        self.assertEqual(0, self.__pool.getNumActive0())
        self.assertEqual(0, self.__pool.getNumIdle0())
        self.assertEqual(0, self.__pool.getNumActive1(keya))
        self.assertEqual(0, self.__pool.getNumIdle1(keya))
        self.assertEqual(0, self.__pool.getNumActive1(keyb))
        self.assertEqual(0, self.__pool.getNumIdle1(keyb))

        objA0 = self.__pool.borrowObject(keya)
        objB0 = self.__pool.borrowObject(keyb)

        self.assertEqual(2, self.__pool.getNumActive0())
        self.assertEqual(0, self.__pool.getNumIdle0())
        self.assertEqual(1, self.__pool.getNumActive1(keya))
        self.assertEqual(0, self.__pool.getNumIdle1(keya))
        self.assertEqual(1, self.__pool.getNumActive1(keyb))
        self.assertEqual(0, self.__pool.getNumIdle1(keyb))

        objA1 = self.__pool.borrowObject(keya)
        objB1 = self.__pool.borrowObject(keyb)

        self.assertEqual(4, self.__pool.getNumActive0())
        self.assertEqual(0, self.__pool.getNumIdle0())
        self.assertEqual(2, self.__pool.getNumActive1(keya))

    def testBaseNumActiveNumIdle2_test17_decomposed(self) -> None:
        try:
            self.__pool = self._makeEmptyPool0(6)
        except NotImplementedError:
            return  # skip this test if unsupported

        keya = self._makeKey(0)
        keyb = self._makeKey(1)

        self.assertEqual(0, self.__pool.getNumActive0())
        self.assertEqual(0, self.__pool.getNumIdle0())
        self.assertEqual(0, self.__pool.getNumActive1(keya))
        self.assertEqual(0, self.__pool.getNumIdle1(keya))
        self.assertEqual(0, self.__pool.getNumActive1(keyb))
        self.assertEqual(0, self.__pool.getNumIdle1(keyb))

        objA0 = self.__pool.borrowObject(keya)
        objB0 = self.__pool.borrowObject(keyb)

        self.assertEqual(2, self.__pool.getNumActive0())
        self.assertEqual(0, self.__pool.getNumIdle0())
        self.assertEqual(1, self.__pool.getNumActive1(keya))
        self.assertEqual(0, self.__pool.getNumIdle1(keya))
        self.assertEqual(1, self.__pool.getNumActive1(keyb))
        self.assertEqual(0, self.__pool.getNumIdle1(keyb))

        objA1 = self.__pool.borrowObject(keya)
        objB1 = self.__pool.borrowObject(keyb)

        self.assertEqual(4, self.__pool.getNumActive0())
        self.assertEqual(0, self.__pool.getNumIdle0())

    def testBaseNumActiveNumIdle2_test16_decomposed(self) -> None:
        try:
            self.__pool = self._makeEmptyPool0(6)
        except NotImplementedError:
            return  # skip this test if unsupported

        keya = self._makeKey(0)
        keyb = self._makeKey(1)

        self.assertEqual(0, self.__pool.getNumActive0())
        self.assertEqual(0, self.__pool.getNumIdle0())
        self.assertEqual(0, self.__pool.getNumActive1(keya))
        self.assertEqual(0, self.__pool.getNumIdle1(keya))
        self.assertEqual(0, self.__pool.getNumActive1(keyb))
        self.assertEqual(0, self.__pool.getNumIdle1(keyb))

        objA0 = self.__pool.borrowObject(keya)
        objB0 = self.__pool.borrowObject(keyb)

        self.assertEqual(2, self.__pool.getNumActive0())
        self.assertEqual(0, self.__pool.getNumIdle0())
        self.assertEqual(1, self.__pool.getNumActive1(keya))
        self.assertEqual(0, self.__pool.getNumIdle1(keya))
        self.assertEqual(1, self.__pool.getNumActive1(keyb))
        self.assertEqual(0, self.__pool.getNumIdle1(keyb))

        objA1 = self.__pool.borrowObject(keya)
        objB1 = self.__pool.borrowObject(keyb)

        self.assertEqual(4, self.__pool.getNumActive0())

    def testBaseNumActiveNumIdle2_test15_decomposed(self) -> None:
        try:
            self.__pool = self._makeEmptyPool0(6)
        except NotImplementedError:
            return  # skip this test if unsupported

        keya = self._makeKey(0)
        keyb = self._makeKey(1)

        self.assertEqual(0, self.__pool.getNumActive0())
        self.assertEqual(0, self.__pool.getNumIdle0())
        self.assertEqual(0, self.__pool.getNumActive1(keya))
        self.assertEqual(0, self.__pool.getNumIdle1(keya))
        self.assertEqual(0, self.__pool.getNumActive1(keyb))
        self.assertEqual(0, self.__pool.getNumIdle1(keyb))

        objA0 = self.__pool.borrowObject(keya)
        objB0 = self.__pool.borrowObject(keyb)

        self.assertEqual(2, self.__pool.getNumActive0())
        self.assertEqual(0, self.__pool.getNumIdle0())
        self.assertEqual(1, self.__pool.getNumActive1(keya))
        self.assertEqual(0, self.__pool.getNumIdle1(keya))
        self.assertEqual(1, self.__pool.getNumActive1(keyb))
        self.assertEqual(0, self.__pool.getNumIdle1(keyb))

        objA1 = self.__pool.borrowObject(keya)
        objB1 = self.__pool.borrowObject(keyb)

    def testBaseNumActiveNumIdle2_test14_decomposed(self) -> None:
        try:
            self.__pool = self._makeEmptyPool0(6)
        except NotImplementedError:
            return  # skip this test if unsupported

        keya = self._makeKey(0)
        keyb = self._makeKey(1)

        self.assertEqual(0, self.__pool.getNumActive0())
        self.assertEqual(0, self.__pool.getNumIdle0())
        self.assertEqual(0, self.__pool.getNumActive1(keya))
        self.assertEqual(0, self.__pool.getNumIdle1(keya))
        self.assertEqual(0, self.__pool.getNumActive1(keyb))
        self.assertEqual(0, self.__pool.getNumIdle1(keyb))

        objA0 = self.__pool.borrowObject(keya)
        objB0 = self.__pool.borrowObject(keyb)

        self.assertEqual(2, self.__pool.getNumActive0())
        self.assertEqual(0, self.__pool.getNumIdle0())
        self.assertEqual(1, self.__pool.getNumActive1(keya))
        self.assertEqual(0, self.__pool.getNumIdle1(keya))
        self.assertEqual(1, self.__pool.getNumActive1(keyb))
        self.assertEqual(0, self.__pool.getNumIdle1(keyb))

    def testBaseNumActiveNumIdle2_test13_decomposed(self) -> None:
        try:
            self.__pool = self._makeEmptyPool0(6)
        except NotImplementedError:
            return  # skip this test if unsupported

        keya = self._makeKey(0)
        keyb = self._makeKey(1)

        self.assertEqual(0, self.__pool.getNumActive0())
        self.assertEqual(0, self.__pool.getNumIdle0())
        self.assertEqual(0, self.__pool.getNumActive1(keya))
        self.assertEqual(0, self.__pool.getNumIdle1(keya))
        self.assertEqual(0, self.__pool.getNumActive1(keyb))
        self.assertEqual(0, self.__pool.getNumIdle1(keyb))

        objA0 = self.__pool.borrowObject(keya)
        objB0 = self.__pool.borrowObject(keyb)

        self.assertEqual(2, self.__pool.getNumActive0())
        self.assertEqual(0, self.__pool.getNumIdle0())
        self.assertEqual(1, self.__pool.getNumActive1(keya))
        self.assertEqual(0, self.__pool.getNumIdle1(keya))
        self.assertEqual(1, self.__pool.getNumActive1(keyb))

    def testBaseNumActiveNumIdle2_test12_decomposed(self) -> None:
        try:
            self.__pool = self._makeEmptyPool0(6)
        except NotImplementedError:
            return  # skip this test if unsupported

        keya = self._makeKey(0)
        keyb = self._makeKey(1)

        self.assertEqual(0, self.__pool.getNumActive0())
        self.assertEqual(0, self.__pool.getNumIdle0())
        self.assertEqual(0, self.__pool.getNumActive1(keya))
        self.assertEqual(0, self.__pool.getNumIdle1(keya))
        self.assertEqual(0, self.__pool.getNumActive1(keyb))
        self.assertEqual(0, self.__pool.getNumIdle1(keyb))

        objA0 = self.__pool.borrowObject(keya)
        objB0 = self.__pool.borrowObject(keyb)

        self.assertEqual(2, self.__pool.getNumActive0())
        self.assertEqual(0, self.__pool.getNumIdle0())
        self.assertEqual(1, self.__pool.getNumActive1(keya))
        self.assertEqual(0, self.__pool.getNumIdle1(keya))

    def testBaseNumActiveNumIdle2_test11_decomposed(self) -> None:
        try:
            self.__pool = self._makeEmptyPool0(6)
        except NotImplementedError:
            return  # skip this test if unsupported

        keya = self._makeKey(0)
        keyb = self._makeKey(1)

        self.assertEqual(0, self.__pool.getNumActive0())
        self.assertEqual(0, self.__pool.getNumIdle0())
        self.assertEqual(0, self.__pool.getNumActive1(keya))
        self.assertEqual(0, self.__pool.getNumIdle1(keya))
        self.assertEqual(0, self.__pool.getNumActive1(keyb))
        self.assertEqual(0, self.__pool.getNumIdle1(keyb))

        objA0 = self.__pool.borrowObject(keya)
        objB0 = self.__pool.borrowObject(keyb)

        self.assertEqual(2, self.__pool.getNumActive0())
        self.assertEqual(0, self.__pool.getNumIdle0())
        self.assertEqual(1, self.__pool.getNumActive1(keya))

    def testBaseNumActiveNumIdle2_test10_decomposed(self) -> None:
        try:
            self.__pool = self._makeEmptyPool0(6)
        except NotImplementedError:
            return  # skip this test if unsupported

        keya = self._makeKey(0)
        keyb = self._makeKey(1)

        self.assertEqual(0, self.__pool.getNumActive0())
        self.assertEqual(0, self.__pool.getNumIdle0())
        self.assertEqual(0, self.__pool.getNumActive1(keya))
        self.assertEqual(0, self.__pool.getNumIdle1(keya))
        self.assertEqual(0, self.__pool.getNumActive1(keyb))
        self.assertEqual(0, self.__pool.getNumIdle1(keyb))

        objA0 = self.__pool.borrowObject(keya)
        objB0 = self.__pool.borrowObject(keyb)

        self.assertEqual(2, self.__pool.getNumActive0())
        self.assertEqual(0, self.__pool.getNumIdle0())

    def testBaseNumActiveNumIdle2_test9_decomposed(self) -> None:
        try:
            self.__pool = self._makeEmptyPool0(6)
        except NotImplementedError:
            return  # skip this test if unsupported

        keya = self._makeKey(0)
        keyb = self._makeKey(1)

        self.assertEqual(0, self.__pool.getNumActive0())
        self.assertEqual(0, self.__pool.getNumIdle0())
        self.assertEqual(0, self.__pool.getNumActive1(keya))
        self.assertEqual(0, self.__pool.getNumIdle1(keya))
        self.assertEqual(0, self.__pool.getNumActive1(keyb))
        self.assertEqual(0, self.__pool.getNumIdle1(keyb))

        objA0 = self.__pool.borrowObject(keya)
        objB0 = self.__pool.borrowObject(keyb)

        self.assertEqual(2, self.__pool.getNumActive0())

    def testBaseNumActiveNumIdle2_test8_decomposed(self) -> None:
        try:
            self.__pool = self._makeEmptyPool0(6)
        except NotImplementedError:
            return  # skip this test if unsupported

        keya = self._makeKey(0)
        keyb = self._makeKey(1)

        self.assertEqual(0, self.__pool.getNumActive0())
        self.assertEqual(0, self.__pool.getNumIdle0())
        self.assertEqual(0, self.__pool.getNumActive1(keya))
        self.assertEqual(0, self.__pool.getNumIdle1(keya))
        self.assertEqual(0, self.__pool.getNumActive1(keyb))
        self.assertEqual(0, self.__pool.getNumIdle1(keyb))

        objA0 = self.__pool.borrowObject(keya)
        objB0 = self.__pool.borrowObject(keyb)

    def testBaseNumActiveNumIdle2_test7_decomposed(self) -> None:
        try:
            self.__pool = self._makeEmptyPool0(6)
        except NotImplementedError:
            return  # skip this test if unsupported

        keya = self._makeKey(0)
        keyb = self._makeKey(1)

        self.assertEqual(0, self.__pool.getNumActive0())
        self.assertEqual(0, self.__pool.getNumIdle0())
        self.assertEqual(0, self.__pool.getNumActive1(keya))
        self.assertEqual(0, self.__pool.getNumIdle1(keya))
        self.assertEqual(0, self.__pool.getNumActive1(keyb))
        self.assertEqual(0, self.__pool.getNumIdle1(keyb))

    def testBaseNumActiveNumIdle2_test6_decomposed(self) -> None:
        try:
            self.__pool = self._makeEmptyPool0(6)
        except NotImplementedError:
            return  # skip this test if unsupported

        keya = self._makeKey(0)
        keyb = self._makeKey(1)

        self.assertEqual(0, self.__pool.getNumActive0())
        self.assertEqual(0, self.__pool.getNumIdle0())
        self.assertEqual(0, self.__pool.getNumActive1(keya))
        self.assertEqual(0, self.__pool.getNumIdle1(keya))
        self.assertEqual(0, self.__pool.getNumActive1(keyb))

    def testBaseNumActiveNumIdle2_test5_decomposed(self) -> None:
        try:
            self.__pool = self._makeEmptyPool0(6)
        except NotImplementedError:
            return  # skip this test if unsupported

        keya = self._makeKey(0)
        keyb = self._makeKey(1)

        self.assertEqual(0, self.__pool.getNumActive0())
        self.assertEqual(0, self.__pool.getNumIdle0())
        self.assertEqual(0, self.__pool.getNumActive1(keya))
        self.assertEqual(0, self.__pool.getNumIdle1(keya))

    def testBaseNumActiveNumIdle2_test4_decomposed(self) -> None:
        try:
            self.__pool = self._makeEmptyPool0(6)
        except NotImplementedError:
            return  # skip this test if unsupported

        keya = self._makeKey(0)
        keyb = self._makeKey(1)

        self.assertEqual(0, self.__pool.getNumActive0())
        self.assertEqual(0, self.__pool.getNumIdle0())
        self.assertEqual(0, self.__pool.getNumActive1(keya))

    def testBaseNumActiveNumIdle2_test3_decomposed(self) -> None:
        try:
            self.__pool = self._makeEmptyPool0(6)
        except NotImplementedError:
            return  # skip this test if unsupported

        keya = self._makeKey(0)
        keyb = self._makeKey(1)
        self.assertEqual(0, self.__pool.getNumActive0())
        self.assertEqual(0, self.__pool.getNumIdle0())

    def testBaseNumActiveNumIdle2_test2_decomposed(self) -> None:
        try:
            self.__pool = self._makeEmptyPool0(6)
        except NotImplementedError:
            return  # skip this test if unsupported

        keya = self._makeKey(0)
        keyb = self._makeKey(1)
        self.assertEqual(0, self.__pool.getNumActive0())

    def testBaseNumActiveNumIdle2_test1_decomposed(self) -> None:
        try:
            self.__pool = self._makeEmptyPool0(6)
        except NotImplementedError:
            return  # skip this test if unsupported

        keya = self._makeKey(0)
        keyb = self._makeKey(1)

    def testBaseNumActiveNumIdle2_test0_decomposed(self) -> None:
        try:
            self.__pool = self._makeEmptyPool0(6)
        except NotImplementedError:
            return  # skip this test if unsupported

    def testBaseNumActiveNumIdle_test18_decomposed(self) -> None:
        try:
            self.__pool = self._makeEmptyPool0(3)
        except NotImplementedError:
            return  # skip this test if unsupported

        keya = self._makeKey(0)
        self.assertEqual(0, self.__pool.getNumActive1(keya))
        self.assertEqual(0, self.__pool.getNumIdle1(keya))

        obj0 = self.__pool.borrowObject(keya)
        self.assertEqual(1, self.__pool.getNumActive1(keya))
        self.assertEqual(0, self.__pool.getNumIdle1(keya))

        obj1 = self.__pool.borrowObject(keya)
        self.assertEqual(2, self.__pool.getNumActive1(keya))
        self.assertEqual(0, self.__pool.getNumIdle1(keya))

        self.__pool.returnObject(keya, obj1)
        self.assertEqual(1, self.__pool.getNumActive1(keya))
        self.assertEqual(1, self.__pool.getNumIdle1(keya))

        self.__pool.returnObject(keya, obj0)
        self.assertEqual(0, self.__pool.getNumActive1(keya))
        self.assertEqual(2, self.__pool.getNumIdle1(keya))

        self.assertEqual(0, self.__pool.getNumActive1("xyzzy12345"))
        self.assertEqual(0, self.__pool.getNumIdle1("xyzzy12345"))

        self.__pool.close()

    def testBaseNumActiveNumIdle_test17_decomposed(self) -> None:
        try:
            self.__pool = self._makeEmptyPool0(3)
        except NotImplementedError:
            return  # skip this test if unsupported

        keya = self._makeKey(0)
        self.assertEqual(0, self.__pool.getNumActive1(keya))
        self.assertEqual(0, self.__pool.getNumIdle1(keya))

        obj0 = self.__pool.borrowObject(keya)
        self.assertEqual(1, self.__pool.getNumActive1(keya))
        self.assertEqual(0, self.__pool.getNumIdle1(keya))

        obj1 = self.__pool.borrowObject(keya)
        self.assertEqual(2, self.__pool.getNumActive1(keya))
        self.assertEqual(0, self.__pool.getNumIdle1(keya))

        self.__pool.returnObject(keya, obj1)
        self.assertEqual(1, self.__pool.getNumActive1(keya))
        self.assertEqual(1, self.__pool.getNumIdle1(keya))

        self.__pool.returnObject(keya, obj0)
        self.assertEqual(0, self.__pool.getNumActive1(keya))
        self.assertEqual(2, self.__pool.getNumIdle1(keya))

        self.assertEqual(0, self.__pool.getNumActive1("xyzzy12345"))
        self.assertEqual(0, self.__pool.getNumIdle1("xyzzy12345"))

    def testBaseNumActiveNumIdle_test16_decomposed(self) -> None:
        try:
            self.__pool = self._makeEmptyPool0(3)
        except NotImplementedError:
            return  # skip this test if unsupported

        keya = self._makeKey(0)
        self.assertEqual(0, self.__pool.getNumActive1(keya))
        self.assertEqual(0, self.__pool.getNumIdle1(keya))

        obj0 = self.__pool.borrowObject(keya)
        self.assertEqual(1, self.__pool.getNumActive1(keya))
        self.assertEqual(0, self.__pool.getNumIdle1(keya))

        obj1 = self.__pool.borrowObject(keya)
        self.assertEqual(2, self.__pool.getNumActive1(keya))
        self.assertEqual(0, self.__pool.getNumIdle1(keya))

        self.__pool.returnObject(keya, obj1)
        self.assertEqual(1, self.__pool.getNumActive1(keya))
        self.assertEqual(1, self.__pool.getNumIdle1(keya))

        self.__pool.returnObject(keya, obj0)
        self.assertEqual(0, self.__pool.getNumActive1(keya))
        self.assertEqual(2, self.__pool.getNumIdle1(keya))

        self.assertEqual(0, self.__pool.getNumActive1("xyzzy12345"))

    def testBaseNumActiveNumIdle_test15_decomposed(self) -> None:
        try:
            self.__pool = self._makeEmptyPool0(3)
        except NotImplementedError:
            return  # skip this test if unsupported

        keya = self._makeKey(0)
        self.assertEqual(0, self.__pool.getNumActive1(keya))
        self.assertEqual(0, self.__pool.getNumIdle1(keya))

        obj0 = self.__pool.borrowObject(keya)
        self.assertEqual(1, self.__pool.getNumActive1(keya))
        self.assertEqual(0, self.__pool.getNumIdle1(keya))

        obj1 = self.__pool.borrowObject(keya)
        self.assertEqual(2, self.__pool.getNumActive1(keya))
        self.assertEqual(0, self.__pool.getNumIdle1(keya))

        self.__pool.returnObject(keya, obj1)
        self.assertEqual(1, self.__pool.getNumActive1(keya))
        self.assertEqual(1, self.__pool.getNumIdle1(keya))

        self.__pool.returnObject(keya, obj0)
        self.assertEqual(0, self.__pool.getNumActive1(keya))
        self.assertEqual(2, self.__pool.getNumIdle1(keya))

    def testBaseNumActiveNumIdle_test14_decomposed(self) -> None:
        try:
            self.__pool = self._makeEmptyPool0(3)
        except NotImplementedError:
            return  # skip this test if unsupported

        keya = self._makeKey(0)
        self.assertEqual(0, self.__pool.getNumActive1(keya))
        self.assertEqual(0, self.__pool.getNumIdle1(keya))

        obj0 = self.__pool.borrowObject(keya)
        self.assertEqual(1, self.__pool.getNumActive1(keya))
        self.assertEqual(0, self.__pool.getNumIdle1(keya))

        obj1 = self.__pool.borrowObject(keya)
        self.assertEqual(2, self.__pool.getNumActive1(keya))
        self.assertEqual(0, self.__pool.getNumIdle1(keya))

        self.__pool.returnObject(keya, obj1)
        self.assertEqual(1, self.__pool.getNumActive1(keya))
        self.assertEqual(1, self.__pool.getNumIdle1(keya))

        self.__pool.returnObject(keya, obj0)
        self.assertEqual(0, self.__pool.getNumActive1(keya))

    def testBaseNumActiveNumIdle_test13_decomposed(self) -> None:
        try:
            self.__pool = self._makeEmptyPool0(3)
        except NotImplementedError:
            return  # skip this test if unsupported

        keya = self._makeKey(0)
        self.assertEqual(0, self.__pool.getNumActive1(keya))
        self.assertEqual(0, self.__pool.getNumIdle1(keya))

        obj0 = self.__pool.borrowObject(keya)
        self.assertEqual(1, self.__pool.getNumActive1(keya))
        self.assertEqual(0, self.__pool.getNumIdle1(keya))

        obj1 = self.__pool.borrowObject(keya)
        self.assertEqual(2, self.__pool.getNumActive1(keya))
        self.assertEqual(0, self.__pool.getNumIdle1(keya))

        self.__pool.returnObject(keya, obj1)
        self.assertEqual(1, self.__pool.getNumActive1(keya))
        self.assertEqual(1, self.__pool.getNumIdle1(keya))

        self.__pool.returnObject(keya, obj0)

    def testBaseNumActiveNumIdle_test12_decomposed(self) -> None:
        try:
            self.__pool = self._makeEmptyPool0(3)
        except NotImplementedError:
            return  # skip this test if unsupported

        keya = self._makeKey(0)
        self.assertEqual(0, self.__pool.getNumActive1(keya))
        self.assertEqual(0, self.__pool.getNumIdle1(keya))

        obj0 = self.__pool.borrowObject(keya)
        self.assertEqual(1, self.__pool.getNumActive1(keya))
        self.assertEqual(0, self.__pool.getNumIdle1(keya))

        obj1 = self.__pool.borrowObject(keya)
        self.assertEqual(2, self.__pool.getNumActive1(keya))
        self.assertEqual(0, self.__pool.getNumIdle1(keya))

        self.__pool.returnObject(keya, obj1)
        self.assertEqual(1, self.__pool.getNumActive1(keya))
        self.assertEqual(1, self.__pool.getNumIdle1(keya))

    def testBaseNumActiveNumIdle_test11_decomposed(self) -> None:
        try:
            self.__pool = self._makeEmptyPool0(3)
        except NotImplementedError:
            return  # skip this test if unsupported

        keya = self._makeKey(0)
        self.assertEqual(0, self.__pool.getNumActive1(keya))
        self.assertEqual(0, self.__pool.getNumIdle1(keya))

        obj0 = self.__pool.borrowObject(keya)
        self.assertEqual(1, self.__pool.getNumActive1(keya))
        self.assertEqual(0, self.__pool.getNumIdle1(keya))

        obj1 = self.__pool.borrowObject(keya)
        self.assertEqual(2, self.__pool.getNumActive1(keya))
        self.assertEqual(0, self.__pool.getNumIdle1(keya))

        self.__pool.returnObject(keya, obj1)
        self.assertEqual(1, self.__pool.getNumActive1(keya))

    def testBaseNumActiveNumIdle_test10_decomposed(self) -> None:
        try:
            self.__pool = self._makeEmptyPool0(3)
        except NotImplementedError:
            return  # skip this test if unsupported

        keya = self._makeKey(0)
        self.assertEqual(0, self.__pool.getNumActive1(keya))
        self.assertEqual(0, self.__pool.getNumIdle1(keya))

        obj0 = self.__pool.borrowObject(keya)
        self.assertEqual(1, self.__pool.getNumActive1(keya))
        self.assertEqual(0, self.__pool.getNumIdle1(keya))

        obj1 = self.__pool.borrowObject(keya)
        self.assertEqual(2, self.__pool.getNumActive1(keya))
        self.assertEqual(0, self.__pool.getNumIdle1(keya))

        self.__pool.returnObject(keya, obj1)

    def testBaseNumActiveNumIdle_test9_decomposed(self) -> None:
        try:
            self.__pool = self._makeEmptyPool0(3)
        except NotImplementedError:
            return  # skip this test if unsupported

        keya = self._makeKey(0)
        self.assertEqual(0, self.__pool.getNumActive1(keya))
        self.assertEqual(0, self.__pool.getNumIdle1(keya))

        obj0 = self.__pool.borrowObject(keya)
        self.assertEqual(1, self.__pool.getNumActive1(keya))
        self.assertEqual(0, self.__pool.getNumIdle1(keya))

        obj1 = self.__pool.borrowObject(keya)
        self.assertEqual(2, self.__pool.getNumActive1(keya))
        self.assertEqual(0, self.__pool.getNumIdle1(keya))

    def testBaseNumActiveNumIdle_test8_decomposed(self) -> None:
        try:
            self.__pool = self._makeEmptyPool0(3)
        except NotImplementedError:
            return  # skip this test if unsupported

        keya = self._makeKey(0)
        self.assertEqual(0, self.__pool.getNumActive1(keya))
        self.assertEqual(0, self.__pool.getNumIdle1(keya))

        obj0 = self.__pool.borrowObject(keya)
        self.assertEqual(1, self.__pool.getNumActive1(keya))
        self.assertEqual(0, self.__pool.getNumIdle1(keya))

        obj1 = self.__pool.borrowObject(keya)
        self.assertEqual(2, self.__pool.getNumActive1(keya))

    def testBaseNumActiveNumIdle_test7_decomposed(self) -> None:
        try:
            self.__pool = self._makeEmptyPool0(3)
        except NotImplementedError:
            return  # skip this test if unsupported

        keya = self._makeKey(0)
        self.assertEqual(0, self.__pool.getNumActive1(keya))
        self.assertEqual(0, self.__pool.getNumIdle1(keya))

        obj0 = self.__pool.borrowObject(keya)
        self.assertEqual(1, self.__pool.getNumActive1(keya))
        self.assertEqual(0, self.__pool.getNumIdle1(keya))

        obj1 = self.__pool.borrowObject(keya)

    def testBaseNumActiveNumIdle_test6_decomposed(self) -> None:
        try:
            self.__pool = self._makeEmptyPool0(3)
        except NotImplementedError:
            return  # skip this test if unsupported

        keya = self._makeKey(0)
        self.assertEqual(0, self.__pool.getNumActive1(keya))
        self.assertEqual(0, self.__pool.getNumIdle1(keya))

        obj0 = self.__pool.borrowObject(keya)
        self.assertEqual(1, self.__pool.getNumActive1(keya))
        self.assertEqual(0, self.__pool.getNumIdle1(keya))

    def testBaseNumActiveNumIdle_test5_decomposed(self) -> None:
        try:
            self.__pool = self._makeEmptyPool0(3)
        except NotImplementedError:
            return  # skip this test if unsupported

        keya = self._makeKey(0)
        self.assertEqual(0, self.__pool.getNumActive1(keya))
        self.assertEqual(0, self.__pool.getNumIdle1(keya))
        obj0 = self.__pool.borrowObject(keya)
        self.assertEqual(1, self.__pool.getNumActive1(keya))

    def testBaseNumActiveNumIdle_test4_decomposed(self) -> None:
        try:
            self.__pool = self._makeEmptyPool0(3)
        except NotImplementedError:
            return  # skip this test if unsupported

        keya = self._makeKey(0)
        self.assertEqual(0, self.__pool.getNumActive1(keya))
        self.assertEqual(0, self.__pool.getNumIdle1(keya))
        obj0 = self.__pool.borrowObject(keya)

    def testBaseNumActiveNumIdle_test3_decomposed(self) -> None:
        try:
            self.__pool = self._makeEmptyPool0(3)
        except NotImplementedError:
            return  # skip this test if unsupported

        keya = self._makeKey(0)
        self.assertEqual(0, self.__pool.getNumActive1(keya))
        self.assertEqual(0, self.__pool.getNumIdle1(keya))

    def testBaseNumActiveNumIdle_test2_decomposed(self) -> None:
        try:
            self.__pool = self._makeEmptyPool0(3)
        except NotImplementedError:
            return  # skip this test if unsupported

        keya = self._makeKey(0)
        self.assertEqual(0, self.__pool.getNumActive1(keya))

    def testBaseNumActiveNumIdle_test1_decomposed(self) -> None:
        try:
            self.__pool = self._makeEmptyPool0(3)
        except NotImplementedError:
            return  # skip this test if unsupported
        keya = self._makeKey(0)

    def testBaseNumActiveNumIdle_test0_decomposed(self) -> None:
        try:
            self.__pool = self._makeEmptyPool0(3)
        except NotImplementedError:
            return  # skip this test if unsupported

    def testBaseInvalidateObject_test13_decomposed(self) -> None:
        try:
            self.__pool = self._makeEmptyPool0(3)
        except NotImplementedError:
            return  # skip this test if unsupported

        keya = self._makeKey(0)
        self.assertEqual(0, self.__pool.getNumActive1(keya))
        self.assertEqual(0, self.__pool.getNumIdle1(keya))

        obj0 = self.__pool.borrowObject(keya)
        obj1 = self.__pool.borrowObject(keya)
        self.assertEqual(2, self.__pool.getNumActive1(keya))
        self.assertEqual(0, self.__pool.getNumIdle1(keya))

        self.__pool.invalidateObject0(keya, obj0)
        self.assertEqual(1, self.__pool.getNumActive1(keya))
        self.assertEqual(0, self.__pool.getNumIdle1(keya))

        self.__pool.invalidateObject0(keya, obj1)
        self.assertEqual(0, self.__pool.getNumActive1(keya))
        self.assertEqual(0, self.__pool.getNumIdle1(keya))

        self.__pool.close()

    def testBaseInvalidateObject_test12_decomposed(self) -> None:
        try:
            self.__pool = self._makeEmptyPool0(3)
        except NotImplementedError:
            return  # skip this test if unsupported

        keya = self._makeKey(0)
        self.assertEqual(0, self.__pool.getNumActive1(keya))
        self.assertEqual(0, self.__pool.getNumIdle1(keya))

        obj0 = self.__pool.borrowObject(keya)
        obj1 = self.__pool.borrowObject(keya)
        self.assertEqual(2, self.__pool.getNumActive1(keya))
        self.assertEqual(0, self.__pool.getNumIdle1(keya))

        self.__pool.invalidateObject0(keya, obj0)
        self.assertEqual(1, self.__pool.getNumActive1(keya))
        self.assertEqual(0, self.__pool.getNumIdle1(keya))

        self.__pool.invalidateObject0(keya, obj1)
        self.assertEqual(0, self.__pool.getNumActive1(keya))
        self.assertEqual(0, self.__pool.getNumIdle1(keya))

    def testBaseInvalidateObject_test11_decomposed(self) -> None:
        try:
            self.__pool = self._makeEmptyPool0(3)
        except NotImplementedError:
            return  # skip this test if unsupported

        keya = self._makeKey(0)
        self.assertEqual(0, self.__pool.getNumActive1(keya))
        self.assertEqual(0, self.__pool.getNumIdle1(keya))

        obj0 = self.__pool.borrowObject(keya)
        obj1 = self.__pool.borrowObject(keya)
        self.assertEqual(2, self.__pool.getNumActive1(keya))
        self.assertEqual(0, self.__pool.getNumIdle1(keya))

        self.__pool.invalidateObject0(keya, obj0)
        self.assertEqual(1, self.__pool.getNumActive1(keya))
        self.assertEqual(0, self.__pool.getNumIdle1(keya))

        self.__pool.invalidateObject0(keya, obj1)
        self.assertEqual(0, self.__pool.getNumActive1(keya))

    def testBaseInvalidateObject_test10_decomposed(self) -> None:
        try:
            self.__pool = self._makeEmptyPool0(3)
        except NotImplementedError:
            return  # skip this test if unsupported

        keya = self._makeKey(0)
        self.assertEqual(0, self.__pool.getNumActive1(keya))
        self.assertEqual(0, self.__pool.getNumIdle1(keya))

        obj0 = self.__pool.borrowObject(keya)
        obj1 = self.__pool.borrowObject(keya)
        self.assertEqual(2, self.__pool.getNumActive1(keya))
        self.assertEqual(0, self.__pool.getNumIdle1(keya))

        self.__pool.invalidateObject0(keya, obj0)
        self.assertEqual(1, self.__pool.getNumActive1(keya))
        self.assertEqual(0, self.__pool.getNumIdle1(keya))

        self.__pool.invalidateObject0(keya, obj1)

    def testBaseInvalidateObject_test9_decomposed(self) -> None:
        try:
            self.__pool = self._makeEmptyPool0(3)
        except NotImplementedError:
            return  # skip this test if unsupported

        keya = self._makeKey(0)
        self.assertEqual(0, self.__pool.getNumActive1(keya))
        self.assertEqual(0, self.__pool.getNumIdle1(keya))

        obj0 = self.__pool.borrowObject(keya)
        obj1 = self.__pool.borrowObject(keya)
        self.assertEqual(2, self.__pool.getNumActive1(keya))
        self.assertEqual(0, self.__pool.getNumIdle1(keya))

        self.__pool.invalidateObject0(keya, obj0)
        self.assertEqual(1, self.__pool.getNumActive1(keya))
        self.assertEqual(0, self.__pool.getNumIdle1(keya))

    def testBaseInvalidateObject_test8_decomposed(self) -> None:
        try:
            self.__pool = self._makeEmptyPool0(3)
        except NotImplementedError:
            return  # skip this test if unsupported

        keya = self._makeKey(0)
        self.assertEqual(0, self.__pool.getNumActive1(keya))
        self.assertEqual(0, self.__pool.getNumIdle1(keya))

        obj0 = self.__pool.borrowObject(keya)
        obj1 = self.__pool.borrowObject(keya)
        self.assertEqual(2, self.__pool.getNumActive1(keya))
        self.assertEqual(0, self.__pool.getNumIdle1(keya))

        self.__pool.invalidateObject0(keya, obj0)
        self.assertEqual(1, self.__pool.getNumActive1(keya))

    def testBaseInvalidateObject_test7_decomposed(self) -> None:
        try:
            self.__pool = self._makeEmptyPool0(3)
        except NotImplementedError:
            return  # skip this test if unsupported

        keya = self._makeKey(0)
        self.assertEqual(0, self.__pool.getNumActive1(keya))
        self.assertEqual(0, self.__pool.getNumIdle1(keya))

        obj0 = self.__pool.borrowObject(keya)
        obj1 = self.__pool.borrowObject(keya)

        self.assertEqual(2, self.__pool.getNumActive1(keya))
        self.assertEqual(0, self.__pool.getNumIdle1(keya))

        self.__pool.invalidateObject0(keya, obj0)

    def testBaseInvalidateObject_test6_decomposed(self) -> None:
        try:
            self.__pool = self._makeEmptyPool0(3)
        except NotImplementedError:
            return  # skip this test if unsupported

        keya = self._makeKey(0)
        self.assertEqual(0, self.__pool.getNumActive1(keya))
        self.assertEqual(0, self.__pool.getNumIdle1(keya))

        obj0 = self.__pool.borrowObject(keya)
        obj1 = self.__pool.borrowObject(keya)

        self.assertEqual(2, self.__pool.getNumActive1(keya))
        self.assertEqual(0, self.__pool.getNumIdle1(keya))

    def testBaseInvalidateObject_test5_decomposed(self) -> None:
        try:
            self.__pool = self._makeEmptyPool0(3)
        except NotImplementedError:
            return  # skip this test if unsupported

        keya = self._makeKey(0)
        self.assertEqual(0, self.__pool.getNumActive1(keya))
        self.assertEqual(0, self.__pool.getNumIdle1(keya))
        obj0 = self.__pool.borrowObject(keya)
        obj1 = self.__pool.borrowObject(keya)
        self.assertEqual(2, self.__pool.getNumActive1(keya))

    def testBaseInvalidateObject_test4_decomposed(self) -> None:
        try:
            self.__pool = self._makeEmptyPool0(3)
        except NotImplementedError:
            return  # skip this test if unsupported

        keya = self._makeKey(0)
        self.assertEqual(0, self.__pool.getNumActive1(keya))
        self.assertEqual(0, self.__pool.getNumIdle1(keya))
        obj0 = self.__pool.borrowObject(keya)
        obj1 = self.__pool.borrowObject(keya)

    def testBaseInvalidateObject_test3_decomposed(self) -> None:
        try:
            self.__pool = self._makeEmptyPool0(3)
        except NotImplementedError:
            return  # skip this test if unsupported

        keya = self._makeKey(0)
        self.assertEqual(0, self.__pool.getNumActive1(keya))
        self.assertEqual(0, self.__pool.getNumIdle1(keya))

    def testBaseInvalidateObject_test2_decomposed(self) -> None:
        try:
            self.__pool = self._makeEmptyPool0(3)
        except NotImplementedError:
            return  # skip this test if unsupported

        keya = self._makeKey(0)
        self.assertEqual(0, self.__pool.getNumActive1(keya))

    def testBaseInvalidateObject_test1_decomposed(self) -> None:
        try:
            self.__pool = self._makeEmptyPool0(3)
        except NotImplementedError:
            return  # skip this test if unsupported
        keya = self._makeKey(0)

    def testBaseInvalidateObject_test0_decomposed(self) -> None:
        try:
            self.__pool = self._makeEmptyPool0(3)
        except NotImplementedError:
            return  # skip this test if unsupported

    def testBaseClear_test15_decomposed(self) -> None:
        try:
            self.__pool = self._makeEmptyPool0(3)
        except NotImplementedError:
            return  # skip this test if unsupported

        keya = self._makeKey(0)
        self.assertEqual(0, self.__pool.getNumActive1(keya))
        self.assertEqual(0, self.__pool.getNumIdle1(keya))

        obj0 = self.__pool.borrowObject(keya)
        obj1 = self.__pool.borrowObject(keya)
        self.assertEqual(2, self.__pool.getNumActive1(keya))
        self.assertEqual(0, self.__pool.getNumIdle1(keya))

        self.__pool.returnObject(keya, obj1)
        self.__pool.returnObject(keya, obj0)
        self.assertEqual(0, self.__pool.getNumActive1(keya))
        self.assertEqual(2, self.__pool.getNumIdle1(keya))

        self.__pool.clear1(keya)
        self.assertEqual(0, self.__pool.getNumActive1(keya))
        self.assertEqual(0, self.__pool.getNumIdle1(keya))

        obj2 = self.__pool.borrowObject(keya)
        self.assertEqual(self._getNthObject(keya, 2), obj2)

        self.__pool.close()

    def testBaseClear_test14_decomposed(self) -> None:
        try:
            self.__pool = self._makeEmptyPool0(3)
        except NotImplementedError:
            return  # skip this test if unsupported

        keya = self._makeKey(0)
        self.assertEqual(0, self.__pool.getNumActive1(keya))
        self.assertEqual(0, self.__pool.getNumIdle1(keya))

        obj0 = self.__pool.borrowObject(keya)
        obj1 = self.__pool.borrowObject(keya)
        self.assertEqual(2, self.__pool.getNumActive1(keya))
        self.assertEqual(0, self.__pool.getNumIdle1(keya))

        self.__pool.returnObject(keya, obj1)
        self.__pool.returnObject(keya, obj0)
        self.assertEqual(0, self.__pool.getNumActive1(keya))
        self.assertEqual(2, self.__pool.getNumIdle1(keya))

        self.__pool.clear1(keya)
        self.assertEqual(0, self.__pool.getNumActive1(keya))
        self.assertEqual(0, self.__pool.getNumIdle1(keya))

        obj2 = self.__pool.borrowObject(keya)
        self.assertEqual(self._getNthObject(keya, 2), obj2)

    def testBaseClear_test13_decomposed(self) -> None:
        try:
            self.__pool = self._makeEmptyPool0(3)
        except NotImplementedError:
            return  # skip this test if unsupported

        keya = self._makeKey(0)
        self.assertEqual(0, self.__pool.getNumActive1(keya))
        self.assertEqual(0, self.__pool.getNumIdle1(keya))

        obj0 = self.__pool.borrowObject(keya)
        obj1 = self.__pool.borrowObject(keya)
        self.assertEqual(2, self.__pool.getNumActive1(keya))
        self.assertEqual(0, self.__pool.getNumIdle1(keya))

        self.__pool.returnObject(keya, obj1)
        self.__pool.returnObject(keya, obj0)
        self.assertEqual(0, self.__pool.getNumActive1(keya))
        self.assertEqual(2, self.__pool.getNumIdle1(keya))

        self.__pool.clear1(keya)
        self.assertEqual(0, self.__pool.getNumActive1(keya))
        self.assertEqual(0, self.__pool.getNumIdle1(keya))

        obj2 = self.__pool.borrowObject(keya)

    def testBaseClear_test12_decomposed(self) -> None:
        try:
            self.__pool = self._makeEmptyPool0(3)
        except NotImplementedError:
            return  # skip this test if unsupported

        keya = self._makeKey(0)
        self.assertEqual(0, self.__pool.getNumActive1(keya))
        self.assertEqual(0, self.__pool.getNumIdle1(keya))

        obj0 = self.__pool.borrowObject(keya)
        obj1 = self.__pool.borrowObject(keya)
        self.assertEqual(2, self.__pool.getNumActive1(keya))
        self.assertEqual(0, self.__pool.getNumIdle1(keya))

        self.__pool.returnObject(keya, obj1)
        self.__pool.returnObject(keya, obj0)
        self.assertEqual(0, self.__pool.getNumActive1(keya))
        self.assertEqual(2, self.__pool.getNumIdle1(keya))

        self.__pool.clear1(keya)
        self.assertEqual(0, self.__pool.getNumActive1(keya))
        self.assertEqual(0, self.__pool.getNumIdle1(keya))

    def testBaseClear_test11_decomposed(self) -> None:
        try:
            self.__pool = self._makeEmptyPool0(3)
        except NotImplementedError:
            return  # skip this test if unsupported

        keya = self._makeKey(0)
        self.assertEqual(0, self.__pool.getNumActive1(keya))
        self.assertEqual(0, self.__pool.getNumIdle1(keya))

        obj0 = self.__pool.borrowObject(keya)
        obj1 = self.__pool.borrowObject(keya)
        self.assertEqual(2, self.__pool.getNumActive1(keya))
        self.assertEqual(0, self.__pool.getNumIdle1(keya))

        self.__pool.returnObject(keya, obj1)
        self.__pool.returnObject(keya, obj0)
        self.assertEqual(0, self.__pool.getNumActive1(keya))
        self.assertEqual(2, self.__pool.getNumIdle1(keya))

        self.__pool.clear1(keya)
        self.assertEqual(0, self.__pool.getNumActive1(keya))

    def testBaseClear_test10_decomposed(self) -> None:
        try:
            self.__pool = self._makeEmptyPool0(3)
        except NotImplementedError:
            return  # skip this test if unsupported

        keya = self._makeKey(0)
        self.assertEqual(0, self.__pool.getNumActive1(keya))
        self.assertEqual(0, self.__pool.getNumIdle1(keya))

        obj0 = self.__pool.borrowObject(keya)
        obj1 = self.__pool.borrowObject(keya)
        self.assertEqual(2, self.__pool.getNumActive1(keya))
        self.assertEqual(0, self.__pool.getNumIdle1(keya))

        self.__pool.returnObject(keya, obj1)
        self.__pool.returnObject(keya, obj0)
        self.assertEqual(0, self.__pool.getNumActive1(keya))
        self.assertEqual(2, self.__pool.getNumIdle1(keya))

        self.__pool.clear1(keya)

    def testBaseClear_test9_decomposed(self) -> None:
        try:
            self.__pool = self._makeEmptyPool0(3)
        except NotImplementedError:
            return  # skip this test if unsupported

        keya = self._makeKey(0)
        self.assertEqual(0, self.__pool.getNumActive1(keya))
        self.assertEqual(0, self.__pool.getNumIdle1(keya))

        obj0 = self.__pool.borrowObject(keya)
        obj1 = self.__pool.borrowObject(keya)
        self.assertEqual(2, self.__pool.getNumActive1(keya))
        self.assertEqual(0, self.__pool.getNumIdle1(keya))

        self.__pool.returnObject(keya, obj1)
        self.__pool.returnObject(keya, obj0)
        self.assertEqual(0, self.__pool.getNumActive1(keya))
        self.assertEqual(2, self.__pool.getNumIdle1(keya))

    def testBaseClear_test8_decomposed(self) -> None:
        try:
            self.__pool = self._makeEmptyPool0(3)
        except NotImplementedError:
            return  # skip this test if unsupported

        keya = self._makeKey(0)
        self.assertEqual(0, self.__pool.getNumActive1(keya))
        self.assertEqual(0, self.__pool.getNumIdle1(keya))

        obj0 = self.__pool.borrowObject(keya)
        obj1 = self.__pool.borrowObject(keya)
        self.assertEqual(2, self.__pool.getNumActive1(keya))
        self.assertEqual(0, self.__pool.getNumIdle1(keya))

        self.__pool.returnObject(keya, obj1)
        self.__pool.returnObject(keya, obj0)
        self.assertEqual(0, self.__pool.getNumActive1(keya))

    def testBaseClear_test7_decomposed(self) -> None:
        try:
            self.__pool = self._makeEmptyPool0(3)
        except NotImplementedError:
            return  # skip this test if unsupported

        keya = self._makeKey(0)
        self.assertEqual(0, self.__pool.getNumActive1(keya))
        self.assertEqual(0, self.__pool.getNumIdle1(keya))

        obj0 = self.__pool.borrowObject(keya)
        obj1 = self.__pool.borrowObject(keya)
        self.assertEqual(2, self.__pool.getNumActive1(keya))
        self.assertEqual(0, self.__pool.getNumIdle1(keya))

        self.__pool.returnObject(keya, obj1)
        self.__pool.returnObject(keya, obj0)

    def testBaseClear_test6_decomposed(self) -> None:
        try:
            self.__pool = self._makeEmptyPool0(3)
        except NotImplementedError:
            return  # skip this test if unsupported

        keya = self._makeKey(0)
        self.assertEqual(0, self.__pool.getNumActive1(keya))
        self.assertEqual(0, self.__pool.getNumIdle1(keya))

        obj0 = self.__pool.borrowObject(keya)
        obj1 = self.__pool.borrowObject(keya)

        self.assertEqual(2, self.__pool.getNumActive1(keya))
        self.assertEqual(0, self.__pool.getNumIdle1(keya))

    def testBaseClear_test5_decomposed(self) -> None:
        try:
            self.__pool = self._makeEmptyPool0(3)
        except NotImplementedError:
            return  # skip this test if unsupported

        keya = self._makeKey(0)
        self.assertEqual(0, self.__pool.getNumActive1(keya))
        self.assertEqual(0, self.__pool.getNumIdle1(keya))
        obj0 = self.__pool.borrowObject(keya)
        obj1 = self.__pool.borrowObject(keya)
        self.assertEqual(2, self.__pool.getNumActive1(keya))

    def testBaseClear_test4_decomposed(self) -> None:
        try:
            self.__pool = self._makeEmptyPool0(3)
        except NotImplementedError:
            return  # skip this test if unsupported

        keya = self._makeKey(0)
        self.assertEqual(0, self.__pool.getNumActive1(keya))
        self.assertEqual(0, self.__pool.getNumIdle1(keya))
        obj0 = self.__pool.borrowObject(keya)
        obj1 = self.__pool.borrowObject(keya)

    def testBaseClear_test3_decomposed(self) -> None:
        try:
            self.__pool = self._makeEmptyPool0(3)
        except NotImplementedError:
            return  # skip this test if unsupported

        keya = self._makeKey(0)
        self.assertEqual(0, self.__pool.getNumActive1(keya))
        self.assertEqual(0, self.__pool.getNumIdle1(keya))

    def testBaseClear_test2_decomposed(self) -> None:
        try:
            self.__pool = self._makeEmptyPool0(3)
        except NotImplementedError:
            return  # skip this test if unsupported

        keya = self._makeKey(0)
        self.assertEqual(0, self.__pool.getNumActive1(keya))

    def testBaseClear_test1_decomposed(self) -> None:
        try:
            self.__pool = self._makeEmptyPool0(3)
        except NotImplementedError:
            return  # skip this test if unsupported
        keya = self._makeKey(0)

    def testBaseClear_test0_decomposed(self) -> None:
        try:
            self.__pool = self._makeEmptyPool0(3)
        except NotImplementedError:
            return  # skip this test if unsupported

    def testBaseBorrowReturn_test21_decomposed(self) -> None:
        try:
            self.__pool = self._makeEmptyPool0(3)
        except NotImplementedError:
            return  # skip this test if unsupported

        keya = self._makeKey(0)
        obj0 = self.__pool.borrowObject(keya)
        self.assertEqual(self._getNthObject(keya, 0), obj0)

        obj1 = self.__pool.borrowObject(keya)
        self.assertEqual(self._getNthObject(keya, 1), obj1)

        obj2 = self.__pool.borrowObject(keya)
        self.assertEqual(self._getNthObject(keya, 2), obj2)

        self.__pool.returnObject(keya, obj2)
        obj2 = self.__pool.borrowObject(keya)
        self.assertEqual(self._getNthObject(keya, 2), obj2)

        self.__pool.returnObject(keya, obj1)
        obj1 = self.__pool.borrowObject(keya)
        self.assertEqual(self._getNthObject(keya, 1), obj1)

        self.__pool.returnObject(keya, obj0)
        self.__pool.returnObject(keya, obj2)
        obj2 = self.__pool.borrowObject(keya)

        if self._isLifo():
            self.assertEqual(self._getNthObject(keya, 2), obj2)
        if self._isFifo():
            self.assertEqual(self._getNthObject(keya, 0), obj2)

        obj0 = self.__pool.borrowObject(keya)
        if self._isLifo():
            self.assertEqual(self._getNthObject(keya, 0), obj0)
        if self._isFifo():
            self.assertEqual(self._getNthObject(keya, 2), obj0)

        self.__pool.close()

    def testBaseBorrowReturn_test20_decomposed(self) -> None:
        try:
            self.__pool = self._makeEmptyPool0(3)
        except NotImplementedError:
            return  # skip this test if unsupported

        keya = self._makeKey(0)
        obj0 = self.__pool.borrowObject(keya)
        self.assertEqual(self._getNthObject(keya, 0), obj0)

        obj1 = self.__pool.borrowObject(keya)
        self.assertEqual(self._getNthObject(keya, 1), obj1)

        obj2 = self.__pool.borrowObject(keya)
        self.assertEqual(self._getNthObject(keya, 2), obj2)

        self.__pool.returnObject(keya, obj2)
        obj2 = self.__pool.borrowObject(keya)
        self.assertEqual(self._getNthObject(keya, 2), obj2)

        self.__pool.returnObject(keya, obj1)
        obj1 = self.__pool.borrowObject(keya)
        self.assertEqual(self._getNthObject(keya, 1), obj1)

        self.__pool.returnObject(keya, obj0)
        self.__pool.returnObject(keya, obj2)

        obj2 = self.__pool.borrowObject(keya)
        if self._isLifo():
            self.assertEqual(self._getNthObject(keya, 2), obj2)
        if self._isFifo():
            self.assertEqual(self._getNthObject(keya, 0), obj2)

        obj0 = self.__pool.borrowObject(keya)
        if self._isLifo():
            self.assertEqual(self._getNthObject(keya, 0), obj0)
        if self._isFifo():
            self.assertEqual(self._getNthObject(keya, 2), obj0)

    def testBaseBorrowReturn_test19_decomposed(self) -> None:
        try:
            self.__pool = self._makeEmptyPool0(3)
        except NotImplementedError:
            return  # skip this test if unsupported

        keya = self._makeKey(0)
        obj0 = self.__pool.borrowObject(keya)
        self.assertEqual(self._getNthObject(keya, 0), obj0)

        obj1 = self.__pool.borrowObject(keya)
        self.assertEqual(self._getNthObject(keya, 1), obj1)

        obj2 = self.__pool.borrowObject(keya)
        self.assertEqual(self._getNthObject(keya, 2), obj2)

        self.__pool.returnObject(keya, obj2)
        obj2 = self.__pool.borrowObject(keya)
        self.assertEqual(self._getNthObject(keya, 2), obj2)

        self.__pool.returnObject(keya, obj1)
        obj1 = self.__pool.borrowObject(keya)
        self.assertEqual(self._getNthObject(keya, 1), obj1)

        self.__pool.returnObject(keya, obj0)
        self.__pool.returnObject(keya, obj2)
        obj2 = self.__pool.borrowObject(keya)

        if self._isLifo():
            self.assertEqual(self._getNthObject(keya, 2), obj2)

        if self._isFifo():
            self.assertEqual(self._getNthObject(keya, 0), obj2)

        obj0 = self.__pool.borrowObject(keya)
        if self._isLifo():
            self.assertEqual(self._getNthObject(keya, 0), obj0)

    def testBaseBorrowReturn_test18_decomposed(self) -> None:
        try:
            self.__pool = self._makeEmptyPool0(3)
        except NotImplementedError:
            return  # skip this test if unsupported

        keya = self._makeKey(0)
        obj0 = self.__pool.borrowObject(keya)
        self.assertEqual(self._getNthObject(keya, 0), obj0)

        obj1 = self.__pool.borrowObject(keya)
        self.assertEqual(self._getNthObject(keya, 1), obj1)

        obj2 = self.__pool.borrowObject(keya)
        self.assertEqual(self._getNthObject(keya, 2), obj2)

        self.__pool.returnObject(keya, obj2)
        obj2 = self.__pool.borrowObject(keya)
        self.assertEqual(self._getNthObject(keya, 2), obj2)

        self.__pool.returnObject(keya, obj1)
        obj1 = self.__pool.borrowObject(keya)
        self.assertEqual(self._getNthObject(keya, 1), obj1)

        self.__pool.returnObject(keya, obj0)
        self.__pool.returnObject(keya, obj2)
        obj2 = self.__pool.borrowObject(keya)

        if self._isLifo():
            self.assertEqual(self._getNthObject(keya, 2), obj2)

        if self._isFifo():
            self.assertEqual(self._getNthObject(keya, 0), obj2)

        obj0 = self.__pool.borrowObject(keya)

    def testBaseBorrowReturn_test17_decomposed(self) -> None:
        try:
            self.__pool = self._makeEmptyPool0(3)
        except NotImplementedError:
            return  # skip this test if unsupported

        keya = self._makeKey(0)
        obj0 = self.__pool.borrowObject(keya)
        self.assertEqual(self._getNthObject(keya, 0), obj0)

        obj1 = self.__pool.borrowObject(keya)
        self.assertEqual(self._getNthObject(keya, 1), obj1)

        obj2 = self.__pool.borrowObject(keya)
        self.assertEqual(self._getNthObject(keya, 2), obj2)

        self.__pool.returnObject(keya, obj2)
        obj2 = self.__pool.borrowObject(keya)
        self.assertEqual(self._getNthObject(keya, 2), obj2)

        self.__pool.returnObject(keya, obj1)
        obj1 = self.__pool.borrowObject(keya)
        self.assertEqual(self._getNthObject(keya, 1), obj1)

        self.__pool.returnObject(keya, obj0)
        self.__pool.returnObject(keya, obj2)
        obj2 = self.__pool.borrowObject(keya)

        if self._isLifo():
            self.assertEqual(self._getNthObject(keya, 2), obj2)

        if self._isFifo():
            self.assertEqual(self._getNthObject(keya, 0), obj2)

    def testBaseBorrowReturn_test16_decomposed(self) -> None:
        try:
            self.__pool = self._makeEmptyPool0(3)
        except NotImplementedError:
            return  # skip this test if unsupported

        keya = self._makeKey(0)
        obj0 = self.__pool.borrowObject(keya)
        self.assertEqual(self._getNthObject(keya, 0), obj0)

        obj1 = self.__pool.borrowObject(keya)
        self.assertEqual(self._getNthObject(keya, 1), obj1)

        obj2 = self.__pool.borrowObject(keya)
        self.assertEqual(self._getNthObject(keya, 2), obj2)

        self.__pool.returnObject(keya, obj2)
        obj2 = self.__pool.borrowObject(keya)
        self.assertEqual(self._getNthObject(keya, 2), obj2)

        self.__pool.returnObject(keya, obj1)
        obj1 = self.__pool.borrowObject(keya)
        self.assertEqual(self._getNthObject(keya, 1), obj1)

        self.__pool.returnObject(keya, obj0)
        self.__pool.returnObject(keya, obj2)

        obj2 = self.__pool.borrowObject(keya)
        if self._isLifo():
            self.assertEqual(self._getNthObject(keya, 2), obj2)

    def testBaseBorrowReturn_test15_decomposed(self) -> None:
        try:
            self.__pool = self._makeEmptyPool0(3)
        except NotImplementedError:
            return  # skip this test if unsupported

        keya = self._makeKey(0)
        obj0 = self.__pool.borrowObject(keya)
        self.assertEqual(self._getNthObject(keya, 0), obj0)

        obj1 = self.__pool.borrowObject(keya)
        self.assertEqual(self._getNthObject(keya, 1), obj1)

        obj2 = self.__pool.borrowObject(keya)
        self.assertEqual(self._getNthObject(keya, 2), obj2)

        self.__pool.returnObject(keya, obj2)
        obj2 = self.__pool.borrowObject(keya)
        self.assertEqual(self._getNthObject(keya, 2), obj2)

        self.__pool.returnObject(keya, obj1)
        obj1 = self.__pool.borrowObject(keya)
        self.assertEqual(self._getNthObject(keya, 1), obj1)

        self.__pool.returnObject(keya, obj0)
        self.__pool.returnObject(keya, obj2)
        obj2 = self.__pool.borrowObject(keya)

    def testBaseBorrowReturn_test14_decomposed(self) -> None:
        try:
            self.__pool = self._makeEmptyPool0(3)
        except NotImplementedError:
            return  # skip this test if unsupported

        keya = self._makeKey(0)
        obj0 = self.__pool.borrowObject(keya)
        self.assertEqual(self._getNthObject(keya, 0), obj0)

        obj1 = self.__pool.borrowObject(keya)
        self.assertEqual(self._getNthObject(keya, 1), obj1)

        obj2 = self.__pool.borrowObject(keya)
        self.assertEqual(self._getNthObject(keya, 2), obj2)

        self.__pool.returnObject(keya, obj2)
        obj2 = self.__pool.borrowObject(keya)
        self.assertEqual(self._getNthObject(keya, 2), obj2)

        self.__pool.returnObject(keya, obj1)
        obj1 = self.__pool.borrowObject(keya)
        self.assertEqual(self._getNthObject(keya, 1), obj1)

        self.__pool.returnObject(keya, obj0)
        self.__pool.returnObject(keya, obj2)

    def testBaseBorrowReturn_test13_decomposed(self) -> None:
        try:
            self.__pool = self._makeEmptyPool0(3)
        except NotImplementedError:
            return  # skip this test if unsupported

        keya = self._makeKey(0)
        obj0 = self.__pool.borrowObject(keya)
        self.assertEqual(self._getNthObject(keya, 0), obj0)

        obj1 = self.__pool.borrowObject(keya)
        self.assertEqual(self._getNthObject(keya, 1), obj1)

        obj2 = self.__pool.borrowObject(keya)
        self.assertEqual(self._getNthObject(keya, 2), obj2)

        self.__pool.returnObject(keya, obj2)
        obj2 = self.__pool.borrowObject(keya)
        self.assertEqual(self._getNthObject(keya, 2), obj2)

        self.__pool.returnObject(keya, obj1)
        obj1 = self.__pool.borrowObject(keya)
        self.assertEqual(self._getNthObject(keya, 1), obj1)

    def testBaseBorrowReturn_test12_decomposed(self) -> None:
        try:
            self.__pool = self._makeEmptyPool0(3)
        except NotImplementedError:
            return  # skip this test if unsupported

        keya = self._makeKey(0)
        obj0 = self.__pool.borrowObject(keya)
        self.assertEqual(self._getNthObject(keya, 0), obj0)

        obj1 = self.__pool.borrowObject(keya)
        self.assertEqual(self._getNthObject(keya, 1), obj1)

        obj2 = self.__pool.borrowObject(keya)
        self.assertEqual(self._getNthObject(keya, 2), obj2)

        self.__pool.returnObject(keya, obj2)
        obj2 = self.__pool.borrowObject(keya)
        self.assertEqual(self._getNthObject(keya, 2), obj2)

        self.__pool.returnObject(keya, obj1)
        obj1 = self.__pool.borrowObject(keya)

    def testBaseBorrowReturn_test11_decomposed(self) -> None:
        try:
            self.__pool = self._makeEmptyPool0(3)
        except NotImplementedError:
            return  # skip this test if unsupported

        keya = self._makeKey(0)
        obj0 = self.__pool.borrowObject(keya)
        self.assertEqual(self._getNthObject(keya, 0), obj0)

        obj1 = self.__pool.borrowObject(keya)
        self.assertEqual(self._getNthObject(keya, 1), obj1)

        obj2 = self.__pool.borrowObject(keya)
        self.assertEqual(self._getNthObject(keya, 2), obj2)

        self.__pool.returnObject(keya, obj2)
        obj2 = self.__pool.borrowObject(keya)
        self.assertEqual(self._getNthObject(keya, 2), obj2)

        self.__pool.returnObject(keya, obj1)

    def testBaseBorrowReturn_test10_decomposed(self) -> None:
        try:
            self.__pool = self._makeEmptyPool0(3)
        except NotImplementedError:
            return  # skip this test if unsupported

        keya = self._makeKey(0)
        obj0 = self.__pool.borrowObject(keya)
        self.assertEqual(self._getNthObject(keya, 0), obj0)

        obj1 = self.__pool.borrowObject(keya)
        self.assertEqual(self._getNthObject(keya, 1), obj1)

        obj2 = self.__pool.borrowObject(keya)
        self.assertEqual(self._getNthObject(keya, 2), obj2)

        self.__pool.returnObject(keya, obj2)
        obj2 = self.__pool.borrowObject(keya)
        self.assertEqual(self._getNthObject(keya, 2), obj2)

    def testBaseBorrowReturn_test9_decomposed(self) -> None:
        try:
            self.__pool = self._makeEmptyPool0(3)
        except NotImplementedError:
            return  # skip this test if unsupported

        keya = self._makeKey(0)
        obj0 = self.__pool.borrowObject(keya)
        self.assertEqual(self._getNthObject(keya, 0), obj0)

        obj1 = self.__pool.borrowObject(keya)
        self.assertEqual(self._getNthObject(keya, 1), obj1)

        obj2 = self.__pool.borrowObject(keya)
        self.assertEqual(self._getNthObject(keya, 2), obj2)

        self.__pool.returnObject(keya, obj2)
        obj2 = self.__pool.borrowObject(keya)

    def testBaseBorrowReturn_test8_decomposed(self) -> None:
        try:
            self.__pool = self._makeEmptyPool0(3)
        except NotImplementedError:
            return  # skip this test if unsupported

        keya = self._makeKey(0)
        obj0 = self.__pool.borrowObject(keya)
        self.assertEqual(self._getNthObject(keya, 0), obj0)

        obj1 = self.__pool.borrowObject(keya)
        self.assertEqual(self._getNthObject(keya, 1), obj1)

        obj2 = self.__pool.borrowObject(keya)
        self.assertEqual(self._getNthObject(keya, 2), obj2)

        self.__pool.returnObject(keya, obj2)

    def testBaseBorrowReturn_test7_decomposed(self) -> None:
        try:
            self.__pool = self._makeEmptyPool0(3)
        except NotImplementedError:
            return  # skip this test if unsupported

        keya = self._makeKey(0)
        obj0 = self.__pool.borrowObject(keya)
        self.assertEqual(self._getNthObject(keya, 0), obj0)

        obj1 = self.__pool.borrowObject(keya)
        self.assertEqual(self._getNthObject(keya, 1), obj1)

        obj2 = self.__pool.borrowObject(keya)
        self.assertEqual(self._getNthObject(keya, 2), obj2)

    def testBaseBorrowReturn_test6_decomposed(self) -> None:
        try:
            self.__pool = self._makeEmptyPool0(3)
        except NotImplementedError:
            return  # skip this test if unsupported

        keya = self._makeKey(0)
        obj0 = self.__pool.borrowObject(keya)
        self.assertEqual(self._getNthObject(keya, 0), obj0)

        obj1 = self.__pool.borrowObject(keya)
        self.assertEqual(self._getNthObject(keya, 1), obj1)

        obj2 = self.__pool.borrowObject(keya)

    def testBaseBorrowReturn_test5_decomposed(self) -> None:
        try:
            self.__pool = self._makeEmptyPool0(3)
        except NotImplementedError:
            return  # skip this test if unsupported

        keya = self._makeKey(0)
        obj0 = self.__pool.borrowObject(keya)
        self.assertEqual(self._getNthObject(keya, 0), obj0)

        obj1 = self.__pool.borrowObject(keya)
        self.assertEqual(self._getNthObject(keya, 1), obj1)

    def testBaseBorrowReturn_test4_decomposed(self) -> None:
        try:
            self.__pool = self._makeEmptyPool0(3)
        except NotImplementedError:
            return  # skip this test if unsupported

        keya = self._makeKey(0)
        obj0 = self.__pool.borrowObject(keya)
        self.assertEqual(self._getNthObject(keya, 0), obj0)
        obj1 = self.__pool.borrowObject(keya)

    def testBaseBorrowReturn_test3_decomposed(self) -> None:
        try:
            self.__pool = self._makeEmptyPool0(3)
        except NotImplementedError:
            return  # skip this test if unsupported

        keya = self._makeKey(0)
        obj0 = self.__pool.borrowObject(keya)
        self.assertEqual(self._getNthObject(keya, 0), obj0)

    def testBaseBorrowReturn_test2_decomposed(self) -> None:
        try:
            self.__pool = self._makeEmptyPool0(3)
        except NotImplementedError:
            return  # skip this test if unsupported

        keya = self._makeKey(0)
        obj0 = self.__pool.borrowObject(keya)

    def testBaseBorrowReturn_test1_decomposed(self) -> None:
        try:
            self.__pool = self._makeEmptyPool0(3)
        except NotImplementedError:
            return  # skip this test if unsupported
        keya = self._makeKey(0)

    def testBaseBorrowReturn_test0_decomposed(self) -> None:
        try:
            self.__pool = self._makeEmptyPool0(3)
        except NotImplementedError:
            return  # skip this test if unsupported

    def testBaseBorrow_test14_decomposed(self) -> None:
        try:
            self.__pool = self._makeEmptyPool0(3)
        except NotImplementedError:
            return  # skip this test if unsupported

        keya = self._makeKey(0)
        keyb = self._makeKey(1)

        self._getNthObject(keya, 0)
        self.assertEqual(
            self._getNthObject(keya, 0), self.__pool.borrowObject(keya), "1"
        )

        self._getNthObject(keyb, 0)
        self.assertEqual(
            self._getNthObject(keyb, 0), self.__pool.borrowObject(keyb), "2"
        )

        self._getNthObject(keyb, 1)
        self.assertEqual(
            self._getNthObject(keyb, 1), self.__pool.borrowObject(keyb), "3"
        )

        self._getNthObject(keya, 1)
        self.assertEqual(
            self._getNthObject(keya, 1), self.__pool.borrowObject(keya), "4"
        )

        self._getNthObject(keyb, 2)
        self.assertEqual(
            self._getNthObject(keyb, 2), self.__pool.borrowObject(keyb), "5"
        )

        self._getNthObject(keya, 2)
        self.assertEqual(
            self._getNthObject(keya, 2), self.__pool.borrowObject(keya), "6"
        )

        self.__pool.close()

    def testBaseBorrow_test13_decomposed(self) -> None:
        try:
            self.__pool = self._makeEmptyPool0(3)
        except NotImplementedError:
            return  # skip this test if unsupported

        keya = self._makeKey(0)
        keyb = self._makeKey(1)

        self._getNthObject(keya, 0)
        self.assertEqual(
            self._getNthObject(keya, 0), self.__pool.borrowObject(keya), "1"
        )

        self._getNthObject(keyb, 0)
        self.assertEqual(
            self._getNthObject(keyb, 0), self.__pool.borrowObject(keyb), "2"
        )

        self._getNthObject(keyb, 1)
        self.assertEqual(
            self._getNthObject(keyb, 1), self.__pool.borrowObject(keyb), "3"
        )

        self._getNthObject(keya, 1)
        self.assertEqual(
            self._getNthObject(keya, 1), self.__pool.borrowObject(keya), "4"
        )

        self._getNthObject(keyb, 2)
        self.assertEqual(
            self._getNthObject(keyb, 2), self.__pool.borrowObject(keyb), "5"
        )

        self._getNthObject(keya, 2)
        self.assertEqual(
            self._getNthObject(keya, 2), self.__pool.borrowObject(keya), "6"
        )

    def testBaseBorrow_test12_decomposed(self) -> None:
        try:
            self.__pool = self._makeEmptyPool0(3)
        except NotImplementedError:
            return  # skip this test if unsupported

        keya = self._makeKey(0)
        keyb = self._makeKey(1)

        self._getNthObject(keya, 0)
        self.assertEqual(
            self._getNthObject(keya, 0), self.__pool.borrowObject(keya), "1"
        )

        self._getNthObject(keyb, 0)
        self.assertEqual(
            self._getNthObject(keyb, 0), self.__pool.borrowObject(keyb), "2"
        )

        self._getNthObject(keyb, 1)
        self.assertEqual(
            self._getNthObject(keyb, 1), self.__pool.borrowObject(keyb), "3"
        )

        self._getNthObject(keya, 1)
        self.assertEqual(
            self._getNthObject(keya, 1), self.__pool.borrowObject(keya), "4"
        )

        self._getNthObject(keyb, 2)
        self.assertEqual(
            self._getNthObject(keyb, 2), self.__pool.borrowObject(keyb), "5"
        )

        self._getNthObject(keya, 2)

    def testBaseBorrow_test11_decomposed(self) -> None:
        try:
            self.__pool = self._makeEmptyPool0(3)
        except NotImplementedError:
            return  # skip this test if unsupported

        keya = self._makeKey(0)
        keyb = self._makeKey(1)

        self._getNthObject(keya, 0)
        self.assertEqual(
            self._getNthObject(keya, 0), self.__pool.borrowObject(keya), "1"
        )

        self._getNthObject(keyb, 0)
        self.assertEqual(
            self._getNthObject(keyb, 0), self.__pool.borrowObject(keyb), "2"
        )

        self._getNthObject(keyb, 1)
        self.assertEqual(
            self._getNthObject(keyb, 1), self.__pool.borrowObject(keyb), "3"
        )

        self._getNthObject(keya, 1)
        self.assertEqual(
            self._getNthObject(keya, 1), self.__pool.borrowObject(keya), "4"
        )

        self._getNthObject(keyb, 2)
        self.assertEqual(
            self._getNthObject(keyb, 2), self.__pool.borrowObject(keyb), "5"
        )

    def testBaseBorrow_test10_decomposed(self) -> None:
        try:
            self.__pool = self._makeEmptyPool0(3)
        except NotImplementedError:
            return  # skip this test if unsupported

        keya = self._makeKey(0)
        keyb = self._makeKey(1)

        self._getNthObject(keya, 0)
        self.assertEqual(
            self._getNthObject(keya, 0), self.__pool.borrowObject(keya), "1"
        )

        self._getNthObject(keyb, 0)
        self.assertEqual(
            self._getNthObject(keyb, 0), self.__pool.borrowObject(keyb), "2"
        )

        self._getNthObject(keyb, 1)
        self.assertEqual(
            self._getNthObject(keyb, 1), self.__pool.borrowObject(keyb), "3"
        )

        self._getNthObject(keya, 1)
        self.assertEqual(
            self._getNthObject(keya, 1), self.__pool.borrowObject(keya), "4"
        )

        self._getNthObject(keyb, 2)

    def testBaseBorrow_test9_decomposed(self) -> None:
        try:
            self.__pool = self._makeEmptyPool0(3)
        except NotImplementedError:
            return  # skip this test if unsupported

        keya = self._makeKey(0)
        keyb = self._makeKey(1)

        self._getNthObject(keya, 0)
        self.assertEqual(
            self._getNthObject(keya, 0), self.__pool.borrowObject(keya), "1"
        )

        self._getNthObject(keyb, 0)
        self.assertEqual(
            self._getNthObject(keyb, 0), self.__pool.borrowObject(keyb), "2"
        )

        self._getNthObject(keyb, 1)
        self.assertEqual(
            self._getNthObject(keyb, 1), self.__pool.borrowObject(keyb), "3"
        )

        self._getNthObject(keya, 1)
        self.assertEqual(
            self._getNthObject(keya, 1), self.__pool.borrowObject(keya), "4"
        )

    def testBaseBorrow_test8_decomposed(self) -> None:
        try:
            self.__pool = self._makeEmptyPool0(3)
        except NotImplementedError:
            return  # skip this test if unsupported

        keya = self._makeKey(0)
        keyb = self._makeKey(1)

        self._getNthObject(keya, 0)
        self.assertEqual(
            self._getNthObject(keya, 0), self.__pool.borrowObject(keya), "1"
        )

        self._getNthObject(keyb, 0)
        self.assertEqual(
            self._getNthObject(keyb, 0), self.__pool.borrowObject(keyb), "2"
        )

        self._getNthObject(keyb, 1)
        self.assertEqual(
            self._getNthObject(keyb, 1), self.__pool.borrowObject(keyb), "3"
        )

        self._getNthObject(keya, 1)

    def testBaseBorrow_test7_decomposed(self) -> None:
        try:
            self.__pool = self._makeEmptyPool0(3)
        except NotImplementedError:
            return  # skip this test if unsupported

        keya = self._makeKey(0)
        keyb = self._makeKey(1)

        self._getNthObject(keya, 0)
        self.assertEqual(
            self._getNthObject(keya, 0), self.__pool.borrowObject(keya), "1"
        )

        self._getNthObject(keyb, 0)
        self.assertEqual(
            self._getNthObject(keyb, 0), self.__pool.borrowObject(keyb), "2"
        )

        self._getNthObject(keyb, 1)
        self.assertEqual(
            self._getNthObject(keyb, 1), self.__pool.borrowObject(keyb), "3"
        )

    def testBaseBorrow_test6_decomposed(self) -> None:
        try:
            self.__pool = self._makeEmptyPool0(3)
        except NotImplementedError:
            return  # skip this test if unsupported

        keya = self._makeKey(0)
        keyb = self._makeKey(1)

        self._getNthObject(keya, 0)
        self.assertEqual(
            self._getNthObject(keya, 0), self.__pool.borrowObject(keya), "1"
        )

        self._getNthObject(keyb, 0)
        self.assertEqual(
            self._getNthObject(keyb, 0), self.__pool.borrowObject(keyb), "2"
        )

        self._getNthObject(keyb, 1)

    def testBaseBorrow_test5_decomposed(self) -> None:
        try:
            self.__pool = self._makeEmptyPool0(3)
        except NotImplementedError:
            return  # skip this test if unsupported

        keya = self._makeKey(0)
        keyb = self._makeKey(1)

        self._getNthObject(keya, 0)
        self.assertEqual(
            self._getNthObject(keya, 0), self.__pool.borrowObject(keya), "1"
        )

        self._getNthObject(keyb, 0)
        self.assertEqual(
            self._getNthObject(keyb, 0), self.__pool.borrowObject(keyb), "2"
        )

    def testBaseBorrow_test4_decomposed(self) -> None:
        try:
            self.__pool = self._makeEmptyPool0(3)
        except NotImplementedError:
            return  # skip this test if unsupported

        keya = self._makeKey(0)
        keyb = self._makeKey(1)

        self._getNthObject(keya, 0)
        self.assertEqual(
            self._getNthObject(keya, 0), self.__pool.borrowObject(keya), "1"
        )
        self._getNthObject(keyb, 0)

    def testBaseBorrow_test3_decomposed(self) -> None:
        try:
            self.__pool = self._makeEmptyPool0(3)
        except NotImplementedError:
            return  # skip this test if unsupported

        keya = self._makeKey(0)
        keyb = self._makeKey(1)
        self._getNthObject(keya, 0)
        self.assertEqual(
            self._getNthObject(keya, 0), self.__pool.borrowObject(keya), "1"
        )

    def testBaseBorrow_test2_decomposed(self) -> None:
        try:
            self.__pool = self._makeEmptyPool0(3)
        except NotImplementedError:
            return  # skip this test if unsupported

        keya = self._makeKey(0)
        keyb = self._makeKey(1)
        self._getNthObject(keya, 0)

    def testBaseBorrow_test1_decomposed(self) -> None:
        try:
            self.__pool = self._makeEmptyPool0(3)
        except NotImplementedError:
            return  # skip this test if unsupported

        keya = self._makeKey(0)
        keyb = self._makeKey(1)

    def testBaseBorrow_test0_decomposed(self) -> None:
        try:
            self.__pool = self._makeEmptyPool0(3)
        except NotImplementedError:
            return  # skip this test if unsupported

    def testBaseAddObject_test2_decomposed(self) -> None:
        try:
            self.__pool = self._makeEmptyPool0(3)
        except NotImplementedError:
            return  # skip this test if unsupported

        key = self._makeKey(0)
        try:
            self.assertEqual(0, self.__pool.getNumIdle0())
            self.assertEqual(0, self.__pool.getNumActive0())
            self.assertEqual(0, self.__pool.getNumIdle1(key))
            self.assertEqual(0, self.__pool.getNumActive1(key))

            self.__pool.addObject(key)
            self.assertEqual(1, self.__pool.getNumIdle0())
            self.assertEqual(0, self.__pool.getNumActive0())
            self.assertEqual(1, self.__pool.getNumIdle1(key))
            self.assertEqual(0, self.__pool.getNumActive1(key))

            obj = self.__pool.borrowObject(key)
            self.assertEqual(self._getNthObject(key, 0), obj)
            self.assertEqual(0, self.__pool.getNumIdle0())
            self.assertEqual(1, self.__pool.getNumActive0())
            self.assertEqual(0, self.__pool.getNumIdle1(key))
            self.assertEqual(1, self.__pool.getNumActive1(key))

            self.__pool.returnObject(key, obj)
            self.assertEqual(1, self.__pool.getNumIdle0())
            self.assertEqual(0, self.__pool.getNumActive0())
            self.assertEqual(1, self.__pool.getNumIdle1(key))
            self.assertEqual(0, self.__pool.getNumActive1(key))
        except NotImplementedError:
            return  # skip this test if one of those calls is unsupported
        finally:
            self.__pool.close()

    def testBaseAddObject_test1_decomposed(self) -> None:
        try:
            self.__pool = self._makeEmptyPool0(3)
        except NotImplementedError:
            return  # skip this test if unsupported
        key = self._makeKey(0)

    def testBaseAddObject_test0_decomposed(self) -> None:
        try:
            self.__pool = self._makeEmptyPool0(3)
        except NotImplementedError:
            return  # skip this test if unsupported

    def tearDown(self) -> None:
        self.__pool = None

    def __reset(
        self,
        pool: KeyedObjectPool[object, typing.Any],
        factory: FailingKeyedPooledObjectFactory,
        expectedMethods: typing.List[MethodCall],
    ) -> None:
        pool.clear0()
        self.__clear(factory, expectedMethods)
        factory.reset()

    def __clear(
        self,
        factory: FailingKeyedPooledObjectFactory,
        expectedMethods: typing.List[MethodCall],
    ) -> None:

        pass  # LLM could not translate this method

    def _makeKey(self, n: int) -> typing.Any:
        return n

    def _makeEmptyPool1(
        self, factory: KeyedPooledObjectFactory[typing.Any, typing.Any]
    ) -> KeyedObjectPool[object, typing.Any]:
        # This method is abstract in Java, so we leave it as a placeholder in Python.
        # Subclasses should override this method to provide the implementation.
        raise NotImplementedError("Subclasses must implement _makeEmptyPool1")

    def _makeEmptyPool0(self, minCapacity: int) -> KeyedObjectPool[object, typing.Any]:
        raise NotImplementedError("Subclasses must implement this method")

    def _isLifo(self) -> bool:
        raise NotImplementedError("Subclasses must implement this method.")

    def _isFifo(self) -> bool:
        raise NotImplementedError("Subclasses must implement this method.")

    def _getNthObject(self, key: typing.Any, n: int) -> typing.Any:
        # This method is abstract in Java, so it should raise a NotImplementedError in Python
        raise NotImplementedError("Subclasses must implement this method")


class FailingKeyedPooledObjectFactory:

    __destroyObjectFail: bool = False

    __passivateObjectFail: bool = False

    __validateObjectFail: bool = False

    __activateObjectFail: bool = False

    __makeObjectFail: bool = False

    __count: int = 0

    __methodCalls: typing.List[MethodCall] = []

    def validateObject(self, key: typing.Any, obj: PooledObject[typing.Any]) -> bool:
        call = MethodCall.MethodCall0("validateObject", key, obj.getObject())
        self.__methodCalls.append(call)
        if self.__validateObjectFail:
            raise PrivateException("validateObject")
        r = True
        call.returned(r)
        return r

    def setValidateObjectFail(self, validateObjectFail: bool) -> None:
        self.__validateObjectFail = validateObjectFail

    def setPassivateObjectFail(self, passivateObjectFail: bool) -> None:
        self.__passivateObjectFail = passivateObjectFail

    def setMakeObjectFail(self, makeObjectFail: bool) -> None:
        self.__makeObjectFail = makeObjectFail

    def setDestroyObjectFail(self, destroyObjectFail: bool) -> None:
        self.__destroyObjectFail = destroyObjectFail

    def setCurrentCount(self, count: int) -> None:
        self.__count = count

    def setActivateObjectFail(self, activateObjectFail: bool) -> None:
        self.__activateObjectFail = activateObjectFail

    def reset(self) -> None:
        self.__count = 0
        self.getMethodCalls().clear()
        self.setMakeObjectFail(False)
        self.setActivateObjectFail(False)
        self.setValidateObjectFail(False)
        self.setPassivateObjectFail(False)
        self.setDestroyObjectFail(False)

    def passivateObject(self, key: typing.Any, obj: PooledObject[typing.Any]) -> None:
        self.__methodCalls.append(
            MethodCall.MethodCall0("passivateObject", key, obj.getObject())
        )
        if self.__passivateObjectFail:
            raise PrivateException("passivateObject")

    def isValidateObjectFail(self) -> bool:
        return self.__validateObjectFail

    def isPassivateObjectFail(self) -> bool:
        return self.__passivateObjectFail

    def isMakeObjectFail(self) -> bool:
        return self.__makeObjectFail

    def isDestroyObjectFail(self) -> bool:
        return self.__destroyObjectFail

    def isActivateObjectFail(self) -> bool:
        return self.__activateObjectFail

    def getMethodCalls(self) -> typing.List[MethodCall]:
        return self.__methodCalls

    def getCurrentCount(self) -> int:
        return self.__count

    def destroyObject(self, key: typing.Any, obj: PooledObject[typing.Any]) -> None:
        self.__methodCalls.append(
            MethodCall.MethodCall0("destroyObject", key, obj.getObject())
        )
        if self.__destroyObjectFail:
            raise PrivateException("destroyObject")

    def activateObject(self, key: typing.Any, obj: PooledObject[typing.Any]) -> None:
        self.__methodCalls.append(
            MethodCall.MethodCall0("activateObject", key, obj.getObject())
        )
        if self.__activateObjectFail:
            raise PrivateException("activateObject")

    def __init__(self) -> None:
        pass
