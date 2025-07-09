from __future__ import annotations
import time
import re
import unittest
import pytest
import io
import typing
from typing import *
import os
import unittest
from src.test.org.apache.commons.pool2.MethodCall import *
from src.test.org.apache.commons.pool2.MethodCallPoolableObjectFactory import *
from src.main.org.apache.commons.pool2.ObjectPool import *
from src.main.org.apache.commons.pool2.PooledObjectFactory import *
from src.test.org.apache.commons.pool2.TestObjectPool import *
from src.main.org.apache.commons.pool2.BaseObjectPool import *


class TestObjectPool(BaseObjectPool):

    def returnObject(self, obj: typing.Any) -> None:
        pass

    def invalidateObject0(self, obj: typing.Any) -> None:
        pass

    def borrowObject(self) -> typing.Any:
        return None


class TestBaseObjectPool(TestObjectPool, unittest.TestCase):

    __pool: ObjectPool[str] = None

    def testUnsupportedOperations_test1_decomposed(self) -> None:
        if self.__class__ != TestBaseObjectPool:
            return  # skip redundant tests

        with TestObjectPool() as pool:
            self.assertTrue(pool.getNumIdle() < 0, "Negative expected.")
            self.assertTrue(pool.getNumActive() < 0, "Negative expected.")

            with self.assertRaises(NotImplementedError):
                pool.clear()

            with self.assertRaises(NotImplementedError):
                pool.addObject()

    def testUnsupportedOperations_test0_decomposed(self) -> None:
        if self.__class__ != TestBaseObjectPool:
            return  # skip redundant tests

    def testClose_test1_decomposed(self) -> None:
        pool: ObjectPool[object] = TestObjectPool()
        pool.close()
        pool.close()

    def testClose_test0_decomposed(self) -> None:
        pool: ObjectPool[object] = TestObjectPool()

    def testBaseNumActiveNumIdle_test15_decomposed(self) -> None:
        try:
            self.__pool = self._makeEmptyPool0(3)
        except NotImplementedError:
            return  # skip this test if unsupported

        self.assertEqual(0, self.__pool.getNumActive())
        self.assertEqual(0, self.__pool.getNumIdle())

        obj0 = self.__pool.borrowObject()
        self.assertEqual(1, self.__pool.getNumActive())
        self.assertEqual(0, self.__pool.getNumIdle())

        obj1 = self.__pool.borrowObject()
        self.assertEqual(2, self.__pool.getNumActive())
        self.assertEqual(0, self.__pool.getNumIdle())

        self.__pool.returnObject(obj1)
        self.assertEqual(1, self.__pool.getNumActive())
        self.assertEqual(1, self.__pool.getNumIdle())

        self.__pool.returnObject(obj0)
        self.assertEqual(0, self.__pool.getNumActive())
        self.assertEqual(2, self.__pool.getNumIdle())

        self.__pool.close()

    def testBaseNumActiveNumIdle_test14_decomposed(self) -> None:
        try:
            self.__pool = self._makeEmptyPool0(3)
        except NotImplementedError:
            return  # skip this test if unsupported

        self.assertEqual(0, self.__pool.getNumActive())
        self.assertEqual(0, self.__pool.getNumIdle())

        obj0 = self.__pool.borrowObject()
        self.assertEqual(1, self.__pool.getNumActive())
        self.assertEqual(0, self.__pool.getNumIdle())

        obj1 = self.__pool.borrowObject()
        self.assertEqual(2, self.__pool.getNumActive())
        self.assertEqual(0, self.__pool.getNumIdle())

        self.__pool.returnObject(obj1)
        self.assertEqual(1, self.__pool.getNumActive())
        self.assertEqual(1, self.__pool.getNumIdle())

        self.__pool.returnObject(obj0)
        self.assertEqual(0, self.__pool.getNumActive())
        self.assertEqual(2, self.__pool.getNumIdle())

    def testBaseNumActiveNumIdle_test13_decomposed(self) -> None:
        try:
            self.__pool = self._makeEmptyPool0(3)
        except NotImplementedError:
            return  # skip this test if unsupported

        self.assertEqual(0, self.__pool.getNumActive())
        self.assertEqual(0, self.__pool.getNumIdle())

        obj0 = self.__pool.borrowObject()
        self.assertEqual(1, self.__pool.getNumActive())
        self.assertEqual(0, self.__pool.getNumIdle())

        obj1 = self.__pool.borrowObject()
        self.assertEqual(2, self.__pool.getNumActive())
        self.assertEqual(0, self.__pool.getNumIdle())

        self.__pool.returnObject(obj1)
        self.assertEqual(1, self.__pool.getNumActive())
        self.assertEqual(1, self.__pool.getNumIdle())

        self.__pool.returnObject(obj0)
        self.assertEqual(0, self.__pool.getNumActive())

    def testBaseNumActiveNumIdle_test12_decomposed(self) -> None:
        try:
            self.__pool = self._makeEmptyPool0(3)
        except NotImplementedError:
            return  # skip this test if unsupported

        self.assertEqual(0, self.__pool.getNumActive())
        self.assertEqual(0, self.__pool.getNumIdle())

        obj0 = self.__pool.borrowObject()
        self.assertEqual(1, self.__pool.getNumActive())
        self.assertEqual(0, self.__pool.getNumIdle())

        obj1 = self.__pool.borrowObject()
        self.assertEqual(2, self.__pool.getNumActive())
        self.assertEqual(0, self.__pool.getNumIdle())

        self.__pool.returnObject(obj1)
        self.assertEqual(1, self.__pool.getNumActive())
        self.assertEqual(1, self.__pool.getNumIdle())

        self.__pool.returnObject(obj0)

    def testBaseNumActiveNumIdle_test11_decomposed(self) -> None:
        try:
            self.__pool = self._makeEmptyPool0(3)
        except NotImplementedError:
            return  # skip this test if unsupported

        self.assertEqual(0, self.__pool.getNumActive())
        self.assertEqual(0, self.__pool.getNumIdle())

        obj0 = self.__pool.borrowObject()
        self.assertEqual(1, self.__pool.getNumActive())
        self.assertEqual(0, self.__pool.getNumIdle())

        obj1 = self.__pool.borrowObject()
        self.assertEqual(2, self.__pool.getNumActive())
        self.assertEqual(0, self.__pool.getNumIdle())

        self.__pool.returnObject(obj1)
        self.assertEqual(1, self.__pool.getNumActive())
        self.assertEqual(1, self.__pool.getNumIdle())

    def testBaseNumActiveNumIdle_test10_decomposed(self) -> None:
        try:
            self.__pool = self._makeEmptyPool0(3)
        except NotImplementedError:
            return  # skip this test if unsupported

        self.assertEqual(0, self.__pool.getNumActive())
        self.assertEqual(0, self.__pool.getNumIdle())

        obj0 = self.__pool.borrowObject()
        self.assertEqual(1, self.__pool.getNumActive())
        self.assertEqual(0, self.__pool.getNumIdle())

        obj1 = self.__pool.borrowObject()
        self.assertEqual(2, self.__pool.getNumActive())
        self.assertEqual(0, self.__pool.getNumIdle())

        self.__pool.returnObject(obj1)
        self.assertEqual(1, self.__pool.getNumActive())

    def testBaseNumActiveNumIdle_test9_decomposed(self) -> None:
        try:
            self.__pool = self._makeEmptyPool0(3)
        except NotImplementedError:
            return  # skip this test if unsupported

        self.assertEqual(0, self.__pool.getNumActive())
        self.assertEqual(0, self.__pool.getNumIdle())

        obj0 = self.__pool.borrowObject()
        self.assertEqual(1, self.__pool.getNumActive())
        self.assertEqual(0, self.__pool.getNumIdle())

        obj1 = self.__pool.borrowObject()
        self.assertEqual(2, self.__pool.getNumActive())
        self.assertEqual(0, self.__pool.getNumIdle())

        self.__pool.returnObject(obj1)

    def testBaseNumActiveNumIdle_test8_decomposed(self) -> None:
        try:
            self.__pool = self._makeEmptyPool0(3)
        except NotImplementedError:
            return  # skip this test if unsupported

        self.assertEqual(0, self.__pool.getNumActive())
        self.assertEqual(0, self.__pool.getNumIdle())

        obj0 = self.__pool.borrowObject()
        self.assertEqual(1, self.__pool.getNumActive())
        self.assertEqual(0, self.__pool.getNumIdle())

        obj1 = self.__pool.borrowObject()
        self.assertEqual(2, self.__pool.getNumActive())
        self.assertEqual(0, self.__pool.getNumIdle())

    def testBaseNumActiveNumIdle_test7_decomposed(self) -> None:
        try:
            self.__pool = self._makeEmptyPool0(3)
        except NotImplementedError:
            return  # skip this test if unsupported

        self.assertEqual(0, self.__pool.getNumActive())
        self.assertEqual(0, self.__pool.getNumIdle())

        obj0 = self.__pool.borrowObject()
        self.assertEqual(1, self.__pool.getNumActive())
        self.assertEqual(0, self.__pool.getNumIdle())

        obj1 = self.__pool.borrowObject()
        self.assertEqual(2, self.__pool.getNumActive())

    def testBaseNumActiveNumIdle_test6_decomposed(self) -> None:
        try:
            self.__pool = self._makeEmptyPool0(3)
        except NotImplementedError:
            return  # skip this test if unsupported

        self.assertEqual(0, self.__pool.getNumActive())
        self.assertEqual(0, self.__pool.getNumIdle())

        obj0 = self.__pool.borrowObject()
        self.assertEqual(1, self.__pool.getNumActive())
        self.assertEqual(0, self.__pool.getNumIdle())

        obj1 = self.__pool.borrowObject()

    def testBaseNumActiveNumIdle_test5_decomposed(self) -> None:
        try:
            self.__pool = self._makeEmptyPool0(3)
        except NotImplementedError:
            return  # skip this test if unsupported

        self.assertEqual(0, self.__pool.getNumActive())
        self.assertEqual(0, self.__pool.getNumIdle())

        obj0 = self.__pool.borrowObject()
        self.assertEqual(1, self.__pool.getNumActive())
        self.assertEqual(0, self.__pool.getNumIdle())

    def testBaseNumActiveNumIdle_test4_decomposed(self) -> None:
        try:
            self.__pool = self._makeEmptyPool0(3)
        except NotImplementedError:
            return  # skip this test if unsupported

        self.assertEqual(0, self.__pool.getNumActive())
        self.assertEqual(0, self.__pool.getNumIdle())

        obj0 = self.__pool.borrowObject()
        self.assertEqual(1, self.__pool.getNumActive())

    def testBaseNumActiveNumIdle_test3_decomposed(self) -> None:
        try:
            self.__pool = self._makeEmptyPool0(3)
        except NotImplementedError:
            return  # skip this test if unsupported

        self.assertEqual(0, self.__pool.getNumActive())
        self.assertEqual(0, self.__pool.getNumIdle())
        obj0 = self.__pool.borrowObject()

    def testBaseNumActiveNumIdle_test2_decomposed(self) -> None:
        try:
            self.__pool = self._makeEmptyPool0(3)
        except NotImplementedError:
            return  # skip this test if unsupported

        self.assertEqual(0, self.__pool.getNumActive())
        self.assertEqual(0, self.__pool.getNumIdle())

    def testBaseNumActiveNumIdle_test1_decomposed(self) -> None:
        try:
            self.__pool = self._makeEmptyPool0(3)
        except NotImplementedError:
            return  # skip this test if unsupported
        self.assertEqual(0, self.__pool.getNumActive())

    def testBaseNumActiveNumIdle_test0_decomposed(self) -> None:
        try:
            self.__pool = self._makeEmptyPool0(3)
        except NotImplementedError:
            return  # skip this test if unsupported

    def testBaseInvalidateObject_test12_decomposed(self) -> None:
        try:
            self.__pool = self._makeEmptyPool0(3)
        except NotImplementedError:
            return  # skip this test if unsupported

        self.assertEqual(0, self.__pool.getNumActive())
        self.assertEqual(0, self.__pool.getNumIdle())

        obj0 = self.__pool.borrowObject()
        obj1 = self.__pool.borrowObject()

        self.assertEqual(2, self.__pool.getNumActive())
        self.assertEqual(0, self.__pool.getNumIdle())

        self.__pool.invalidateObject0(obj0)
        self.assertEqual(1, self.__pool.getNumActive())
        self.assertEqual(0, self.__pool.getNumIdle())

        self.__pool.invalidateObject0(obj1)
        self.assertEqual(0, self.__pool.getNumActive())
        self.assertEqual(0, self.__pool.getNumIdle())

        self.__pool.close()

    def testBaseInvalidateObject_test11_decomposed(self) -> None:
        try:
            self.__pool = self._makeEmptyPool0(3)
        except NotImplementedError:
            return  # skip this test if unsupported

        self.assertEqual(0, self.__pool.getNumActive())
        self.assertEqual(0, self.__pool.getNumIdle())

        obj0 = self.__pool.borrowObject()
        obj1 = self.__pool.borrowObject()

        self.assertEqual(2, self.__pool.getNumActive())
        self.assertEqual(0, self.__pool.getNumIdle())

        self.__pool.invalidateObject0(obj0)
        self.assertEqual(1, self.__pool.getNumActive())
        self.assertEqual(0, self.__pool.getNumIdle())

        self.__pool.invalidateObject0(obj1)
        self.assertEqual(0, self.__pool.getNumActive())
        self.assertEqual(0, self.__pool.getNumIdle())

    def testBaseInvalidateObject_test10_decomposed(self) -> None:
        try:
            self.__pool = self._makeEmptyPool0(3)
        except NotImplementedError:
            return  # skip this test if unsupported

        self.assertEqual(0, self.__pool.getNumActive())
        self.assertEqual(0, self.__pool.getNumIdle())

        obj0 = self.__pool.borrowObject()
        obj1 = self.__pool.borrowObject()

        self.assertEqual(2, self.__pool.getNumActive())
        self.assertEqual(0, self.__pool.getNumIdle())

        self.__pool.invalidateObject0(obj0)
        self.assertEqual(1, self.__pool.getNumActive())
        self.assertEqual(0, self.__pool.getNumIdle())

        self.__pool.invalidateObject0(obj1)
        self.assertEqual(0, self.__pool.getNumActive())

    def testBaseInvalidateObject_test9_decomposed(self) -> None:
        try:
            self.__pool = self._makeEmptyPool0(3)
        except NotImplementedError:
            return  # skip this test if unsupported

        self.assertEqual(0, self.__pool.getNumActive())
        self.assertEqual(0, self.__pool.getNumIdle())

        obj0 = self.__pool.borrowObject()
        obj1 = self.__pool.borrowObject()

        self.assertEqual(2, self.__pool.getNumActive())
        self.assertEqual(0, self.__pool.getNumIdle())

        self.__pool.invalidateObject0(obj0)
        self.assertEqual(1, self.__pool.getNumActive())
        self.assertEqual(0, self.__pool.getNumIdle())

        self.__pool.invalidateObject0(obj1)

    def testBaseInvalidateObject_test8_decomposed(self) -> None:
        try:
            self.__pool = self._makeEmptyPool0(3)
        except NotImplementedError:
            return  # skip this test if unsupported

        self.assertEqual(0, self.__pool.getNumActive())
        self.assertEqual(0, self.__pool.getNumIdle())

        obj0 = self.__pool.borrowObject()
        obj1 = self.__pool.borrowObject()

        self.assertEqual(2, self.__pool.getNumActive())
        self.assertEqual(0, self.__pool.getNumIdle())

        self.__pool.invalidateObject0(obj0)

        self.assertEqual(1, self.__pool.getNumActive())
        self.assertEqual(0, self.__pool.getNumIdle())

    def testBaseInvalidateObject_test7_decomposed(self) -> None:
        try:
            self.__pool = self._makeEmptyPool0(3)
        except NotImplementedError:
            return  # skip this test if unsupported

        self.assertEqual(0, self.__pool.getNumActive())
        self.assertEqual(0, self.__pool.getNumIdle())

        obj0 = self.__pool.borrowObject()
        obj1 = self.__pool.borrowObject()

        self.assertEqual(2, self.__pool.getNumActive())
        self.assertEqual(0, self.__pool.getNumIdle())

        self.__pool.invalidateObject0(obj0)

        self.assertEqual(1, self.__pool.getNumActive())

    def testBaseInvalidateObject_test6_decomposed(self) -> None:
        try:
            self.__pool = self._makeEmptyPool0(3)
        except NotImplementedError:
            return  # skip this test if unsupported

        self.assertEqual(0, self.__pool.getNumActive())
        self.assertEqual(0, self.__pool.getNumIdle())

        obj0 = self.__pool.borrowObject()
        obj1 = self.__pool.borrowObject()

        self.assertEqual(2, self.__pool.getNumActive())
        self.assertEqual(0, self.__pool.getNumIdle())

        self.__pool.invalidateObject0(obj0)

    def testBaseInvalidateObject_test5_decomposed(self) -> None:
        try:
            self.__pool = self._makeEmptyPool0(3)
        except NotImplementedError:
            return  # skip this test if unsupported

        self.assertEqual(0, self.__pool.getNumActive())
        self.assertEqual(0, self.__pool.getNumIdle())

        obj0 = self.__pool.borrowObject()
        obj1 = self.__pool.borrowObject()

        self.assertEqual(2, self.__pool.getNumActive())
        self.assertEqual(0, self.__pool.getNumIdle())

    def testBaseInvalidateObject_test4_decomposed(self) -> None:
        try:
            self.__pool = self._makeEmptyPool0(3)
        except NotImplementedError:
            return  # skip this test if unsupported

        self.assertEqual(0, self.__pool.getNumActive())
        self.assertEqual(0, self.__pool.getNumIdle())

        obj0 = self.__pool.borrowObject()
        obj1 = self.__pool.borrowObject()

        self.assertEqual(2, self.__pool.getNumActive())

    def testBaseInvalidateObject_test3_decomposed(self) -> None:
        try:
            self.__pool = self._makeEmptyPool0(3)
        except NotImplementedError:
            return  # skip this test if unsupported

        self.assertEqual(0, self.__pool.getNumActive())
        self.assertEqual(0, self.__pool.getNumIdle())
        obj0 = self.__pool.borrowObject()
        obj1 = self.__pool.borrowObject()

    def testBaseInvalidateObject_test2_decomposed(self) -> None:
        try:
            self.__pool = self._makeEmptyPool0(3)
        except NotImplementedError:
            return  # skip this test if unsupported

        self.assertEqual(0, self.__pool.getNumActive())
        self.assertEqual(0, self.__pool.getNumIdle())

    def testBaseInvalidateObject_test1_decomposed(self) -> None:
        try:
            self.__pool = self._makeEmptyPool0(3)
        except NotImplementedError:
            return  # skip this test if unsupported
        self.assertEqual(0, self.__pool.getNumActive())

    def testBaseInvalidateObject_test0_decomposed(self) -> None:
        try:
            self.__pool = self._makeEmptyPool0(3)
        except NotImplementedError:
            return  # skip this test if unsupported

    def testBaseClosePool_test4_decomposed(self) -> None:
        try:
            self.__pool = self._makeEmptyPool0(3)
        except NotImplementedError:
            return  # skip this test if unsupported

        obj = self.__pool.borrowObject()
        self.__pool.returnObject(obj)
        self.__pool.close()

        with self.assertRaises(RuntimeError):
            self.__pool.borrowObject()

    def testBaseClosePool_test3_decomposed(self) -> None:
        try:
            self.__pool = self._makeEmptyPool0(3)
        except NotImplementedError:
            return  # skip this test if unsupported

        obj = self.__pool.borrowObject()
        self.__pool.returnObject(obj)
        self.__pool.close()

    def testBaseClosePool_test2_decomposed(self) -> None:
        try:
            self.__pool = self._makeEmptyPool0(3)
        except NotImplementedError:
            return  # skip this test if unsupported
        obj = self.__pool.borrowObject()
        self.__pool.returnObject(obj)

    def testBaseClosePool_test1_decomposed(self) -> None:
        try:
            self.__pool = self._makeEmptyPool0(3)
        except NotImplementedError:
            return  # skip this test if unsupported
        obj = self.__pool.borrowObject()

    def testBaseClosePool_test0_decomposed(self) -> None:
        try:
            self.__pool = self._makeEmptyPool0(3)
        except NotImplementedError:
            return  # skip this test if unsupported

    def testBaseClear_test14_decomposed(self) -> None:
        try:
            self.__pool = self._makeEmptyPool0(3)
        except NotImplementedError:
            return  # skip this test if unsupported

        self.assertEqual(0, self.__pool.getNumActive())
        self.assertEqual(0, self.__pool.getNumIdle())

        obj0 = self.__pool.borrowObject()
        obj1 = self.__pool.borrowObject()

        self.assertEqual(2, self.__pool.getNumActive())
        self.assertEqual(0, self.__pool.getNumIdle())

        self.__pool.returnObject(obj1)
        self.__pool.returnObject(obj0)

        self.assertEqual(0, self.__pool.getNumActive())
        self.assertEqual(2, self.__pool.getNumIdle())

        self.__pool.clear()

        self.assertEqual(0, self.__pool.getNumActive())
        self.assertEqual(0, self.__pool.getNumIdle())

        obj2 = self.__pool.borrowObject()
        self.assertEqual(self._getNthObject(2), obj2)

        self.__pool.close()

    def testBaseClear_test13_decomposed(self) -> None:
        try:
            self.__pool = self._makeEmptyPool0(3)
        except NotImplementedError:
            return  # skip this test if unsupported

        self.assertEqual(0, self.__pool.getNumActive())
        self.assertEqual(0, self.__pool.getNumIdle())

        obj0 = self.__pool.borrowObject()
        obj1 = self.__pool.borrowObject()

        self.assertEqual(2, self.__pool.getNumActive())
        self.assertEqual(0, self.__pool.getNumIdle())

        self.__pool.returnObject(obj1)
        self.__pool.returnObject(obj0)

        self.assertEqual(0, self.__pool.getNumActive())
        self.assertEqual(2, self.__pool.getNumIdle())

        self.__pool.clear()

        self.assertEqual(0, self.__pool.getNumActive())
        self.assertEqual(0, self.__pool.getNumIdle())

        obj2 = self.__pool.borrowObject()
        self.assertEqual(self._getNthObject(2), obj2)

    def testBaseClear_test12_decomposed(self) -> None:
        try:
            self.__pool = self._makeEmptyPool0(3)
        except NotImplementedError:
            return  # skip this test if unsupported

        self.assertEqual(0, self.__pool.getNumActive())
        self.assertEqual(0, self.__pool.getNumIdle())

        obj0 = self.__pool.borrowObject()
        obj1 = self.__pool.borrowObject()

        self.assertEqual(2, self.__pool.getNumActive())
        self.assertEqual(0, self.__pool.getNumIdle())

        self.__pool.returnObject(obj1)
        self.__pool.returnObject(obj0)

        self.assertEqual(0, self.__pool.getNumActive())
        self.assertEqual(2, self.__pool.getNumIdle())

        self.__pool.clear()

        self.assertEqual(0, self.__pool.getNumActive())
        self.assertEqual(0, self.__pool.getNumIdle())

        obj2 = self.__pool.borrowObject()

    def testBaseClear_test11_decomposed(self) -> None:
        try:
            self.__pool = self._makeEmptyPool0(3)
        except NotImplementedError:
            return  # skip this test if unsupported

        self.assertEqual(0, self.__pool.getNumActive())
        self.assertEqual(0, self.__pool.getNumIdle())

        obj0 = self.__pool.borrowObject()
        obj1 = self.__pool.borrowObject()

        self.assertEqual(2, self.__pool.getNumActive())
        self.assertEqual(0, self.__pool.getNumIdle())

        self.__pool.returnObject(obj1)
        self.__pool.returnObject(obj0)

        self.assertEqual(0, self.__pool.getNumActive())
        self.assertEqual(2, self.__pool.getNumIdle())

        self.__pool.clear()

        self.assertEqual(0, self.__pool.getNumActive())
        self.assertEqual(0, self.__pool.getNumIdle())

    def testBaseClear_test10_decomposed(self) -> None:
        try:
            self.__pool = self._makeEmptyPool0(3)
        except NotImplementedError:
            return  # skip this test if unsupported

        self.assertEqual(0, self.__pool.getNumActive())
        self.assertEqual(0, self.__pool.getNumIdle())

        obj0 = self.__pool.borrowObject()
        obj1 = self.__pool.borrowObject()

        self.assertEqual(2, self.__pool.getNumActive())
        self.assertEqual(0, self.__pool.getNumIdle())

        self.__pool.returnObject(obj1)
        self.__pool.returnObject(obj0)

        self.assertEqual(0, self.__pool.getNumActive())
        self.assertEqual(2, self.__pool.getNumIdle())

        self.__pool.clear()

        self.assertEqual(0, self.__pool.getNumActive())

    def testBaseClear_test9_decomposed(self) -> None:
        try:
            self.__pool = self._makeEmptyPool0(3)
        except NotImplementedError:
            return  # skip this test if unsupported

        self.assertEqual(0, self.__pool.getNumActive())
        self.assertEqual(0, self.__pool.getNumIdle())

        obj0 = self.__pool.borrowObject()
        obj1 = self.__pool.borrowObject()

        self.assertEqual(2, self.__pool.getNumActive())
        self.assertEqual(0, self.__pool.getNumIdle())

        self.__pool.returnObject(obj1)
        self.__pool.returnObject(obj0)

        self.assertEqual(0, self.__pool.getNumActive())
        self.assertEqual(2, self.__pool.getNumIdle())

        self.__pool.clear()

    def testBaseClear_test8_decomposed(self) -> None:
        try:
            self.__pool = self._makeEmptyPool0(3)
        except NotImplementedError:
            return  # skip this test if unsupported

        self.assertEqual(0, self.__pool.getNumActive())
        self.assertEqual(0, self.__pool.getNumIdle())

        obj0 = self.__pool.borrowObject()
        obj1 = self.__pool.borrowObject()

        self.assertEqual(2, self.__pool.getNumActive())
        self.assertEqual(0, self.__pool.getNumIdle())

        self.__pool.returnObject(obj1)
        self.__pool.returnObject(obj0)

        self.assertEqual(0, self.__pool.getNumActive())
        self.assertEqual(2, self.__pool.getNumIdle())

    def testBaseClear_test7_decomposed(self) -> None:
        try:
            self.__pool = self._makeEmptyPool0(3)
        except NotImplementedError:
            return  # skip this test if unsupported

        self.assertEqual(0, self.__pool.getNumActive())
        self.assertEqual(0, self.__pool.getNumIdle())

        obj0 = self.__pool.borrowObject()
        obj1 = self.__pool.borrowObject()

        self.assertEqual(2, self.__pool.getNumActive())
        self.assertEqual(0, self.__pool.getNumIdle())

        self.__pool.returnObject(obj1)
        self.__pool.returnObject(obj0)

        self.assertEqual(0, self.__pool.getNumActive())

    def testBaseClear_test6_decomposed(self) -> None:
        try:
            self.__pool = self._makeEmptyPool0(3)
        except NotImplementedError:
            return  # skip this test if unsupported

        self.assertEqual(0, self.__pool.getNumActive())
        self.assertEqual(0, self.__pool.getNumIdle())

        obj0 = self.__pool.borrowObject()
        obj1 = self.__pool.borrowObject()

        self.assertEqual(2, self.__pool.getNumActive())
        self.assertEqual(0, self.__pool.getNumIdle())

        self.__pool.returnObject(obj1)
        self.__pool.returnObject(obj0)

    def testBaseClear_test5_decomposed(self) -> None:
        try:
            self.__pool = self._makeEmptyPool0(3)
        except NotImplementedError:
            return  # skip this test if unsupported

        self.assertEqual(0, self.__pool.getNumActive())
        self.assertEqual(0, self.__pool.getNumIdle())

        obj0 = self.__pool.borrowObject()
        obj1 = self.__pool.borrowObject()

        self.assertEqual(2, self.__pool.getNumActive())
        self.assertEqual(0, self.__pool.getNumIdle())

    def testBaseClear_test4_decomposed(self) -> None:
        try:
            self.__pool = self._makeEmptyPool0(3)
        except NotImplementedError:
            return  # skip this test if unsupported

        self.assertEqual(0, self.__pool.getNumActive())
        self.assertEqual(0, self.__pool.getNumIdle())

        obj0 = self.__pool.borrowObject()
        obj1 = self.__pool.borrowObject()

        self.assertEqual(2, self.__pool.getNumActive())

    def testBaseClear_test3_decomposed(self) -> None:
        try:
            self.__pool = self._makeEmptyPool0(3)
        except NotImplementedError:
            return  # skip this test if unsupported

        self.assertEqual(0, self.__pool.getNumActive())
        self.assertEqual(0, self.__pool.getNumIdle())
        obj0 = self.__pool.borrowObject()
        obj1 = self.__pool.borrowObject()

    def testBaseClear_test2_decomposed(self) -> None:
        try:
            self.__pool = self._makeEmptyPool0(3)
        except NotImplementedError:
            return  # skip this test if unsupported

        self.assertEqual(0, self.__pool.getNumActive())
        self.assertEqual(0, self.__pool.getNumIdle())

    def testBaseClear_test1_decomposed(self) -> None:
        try:
            self.__pool = self._makeEmptyPool0(3)
        except NotImplementedError:
            return  # skip this test if unsupported
        self.assertEqual(0, self.__pool.getNumActive())

    def testBaseClear_test0_decomposed(self) -> None:
        try:
            self.__pool = self._makeEmptyPool0(3)
        except NotImplementedError:
            return  # skip this test if unsupported

    def testBaseBorrowReturn_test20_decomposed(self) -> None:
        try:
            self.__pool = self._makeEmptyPool0(3)
        except NotImplementedError:
            return  # skip this test if unsupported

        obj0 = self.__pool.borrowObject()
        self.assertEqual(self._getNthObject(0), obj0)

        obj1 = self.__pool.borrowObject()
        self.assertEqual(self._getNthObject(1), obj1)

        obj2 = self.__pool.borrowObject()
        self.assertEqual(self._getNthObject(2), obj2)

        self.__pool.returnObject(obj2)
        obj2 = self.__pool.borrowObject()
        self.assertEqual(self._getNthObject(2), obj2)

        self.__pool.returnObject(obj1)
        obj1 = self.__pool.borrowObject()
        self.assertEqual(self._getNthObject(1), obj1)

        self.__pool.returnObject(obj0)
        self.__pool.returnObject(obj2)

        obj2 = self.__pool.borrowObject()
        if self._isLifo():
            self.assertEqual(self._getNthObject(2), obj2)
        if self._isFifo():
            self.assertEqual(self._getNthObject(0), obj2)

        obj0 = self.__pool.borrowObject()
        if self._isLifo():
            self.assertEqual(self._getNthObject(0), obj0)
        if self._isFifo():
            self.assertEqual(self._getNthObject(2), obj0)

        self.__pool.close()

    def testBaseBorrowReturn_test19_decomposed(self) -> None:
        try:
            self.__pool = self._makeEmptyPool0(3)
        except NotImplementedError:
            return  # skip this test if unsupported

        obj0 = self.__pool.borrowObject()
        self.assertEqual(self._getNthObject(0), obj0)

        obj1 = self.__pool.borrowObject()
        self.assertEqual(self._getNthObject(1), obj1)

        obj2 = self.__pool.borrowObject()
        self.assertEqual(self._getNthObject(2), obj2)

        self.__pool.returnObject(obj2)
        obj2 = self.__pool.borrowObject()
        self.assertEqual(self._getNthObject(2), obj2)

        self.__pool.returnObject(obj1)
        obj1 = self.__pool.borrowObject()
        self.assertEqual(self._getNthObject(1), obj1)

        self.__pool.returnObject(obj0)
        self.__pool.returnObject(obj2)

        obj2 = self.__pool.borrowObject()
        if self._isLifo():
            self.assertEqual(self._getNthObject(2), obj2)
        if self._isFifo():
            self.assertEqual(self._getNthObject(0), obj2)

        obj0 = self.__pool.borrowObject()
        if self._isLifo():
            self.assertEqual(self._getNthObject(0), obj0)
        if self._isFifo():
            self.assertEqual(self._getNthObject(2), obj0)

    def testBaseBorrowReturn_test18_decomposed(self) -> None:
        try:
            self.__pool = self._makeEmptyPool0(3)
        except NotImplementedError:
            return  # skip this test if unsupported

        obj0 = self.__pool.borrowObject()
        self.assertEqual(self._getNthObject(0), obj0)

        obj1 = self.__pool.borrowObject()
        self.assertEqual(self._getNthObject(1), obj1)

        obj2 = self.__pool.borrowObject()
        self.assertEqual(self._getNthObject(2), obj2)

        self.__pool.returnObject(obj2)
        obj2 = self.__pool.borrowObject()
        self.assertEqual(self._getNthObject(2), obj2)

        self.__pool.returnObject(obj1)
        obj1 = self.__pool.borrowObject()
        self.assertEqual(self._getNthObject(1), obj1)

        self.__pool.returnObject(obj0)
        self.__pool.returnObject(obj2)

        obj2 = self.__pool.borrowObject()
        if self._isLifo():
            self.assertEqual(self._getNthObject(2), obj2)
        if self._isFifo():
            self.assertEqual(self._getNthObject(0), obj2)

        obj0 = self.__pool.borrowObject()
        if self._isLifo():
            self.assertEqual(self._getNthObject(0), obj0)

    def testBaseBorrowReturn_test17_decomposed(self) -> None:
        try:
            self.__pool = self._makeEmptyPool0(3)
        except NotImplementedError:
            return  # skip this test if unsupported

        obj0 = self.__pool.borrowObject()
        self.assertEqual(self._getNthObject(0), obj0)

        obj1 = self.__pool.borrowObject()
        self.assertEqual(self._getNthObject(1), obj1)

        obj2 = self.__pool.borrowObject()
        self.assertEqual(self._getNthObject(2), obj2)

        self.__pool.returnObject(obj2)
        obj2 = self.__pool.borrowObject()
        self.assertEqual(self._getNthObject(2), obj2)

        self.__pool.returnObject(obj1)
        obj1 = self.__pool.borrowObject()
        self.assertEqual(self._getNthObject(1), obj1)

        self.__pool.returnObject(obj0)
        self.__pool.returnObject(obj2)

        obj2 = self.__pool.borrowObject()
        if self._isLifo():
            self.assertEqual(self._getNthObject(2), obj2)
        if self._isFifo():
            self.assertEqual(self._getNthObject(0), obj2)

        obj0 = self.__pool.borrowObject()

    def testBaseBorrowReturn_test16_decomposed(self) -> None:
        try:
            self.__pool = self._makeEmptyPool0(3)
        except NotImplementedError:
            return  # skip this test if unsupported

        obj0 = self.__pool.borrowObject()
        self.assertEqual(self._getNthObject(0), obj0)

        obj1 = self.__pool.borrowObject()
        self.assertEqual(self._getNthObject(1), obj1)

        obj2 = self.__pool.borrowObject()
        self.assertEqual(self._getNthObject(2), obj2)

        self.__pool.returnObject(obj2)
        obj2 = self.__pool.borrowObject()
        self.assertEqual(self._getNthObject(2), obj2)

        self.__pool.returnObject(obj1)
        obj1 = self.__pool.borrowObject()
        self.assertEqual(self._getNthObject(1), obj1)

        self.__pool.returnObject(obj0)
        self.__pool.returnObject(obj2)

        obj2 = self.__pool.borrowObject()
        if self._isLifo():
            self.assertEqual(self._getNthObject(2), obj2)
        if self._isFifo():
            self.assertEqual(self._getNthObject(0), obj2)

    def testBaseBorrowReturn_test15_decomposed(self) -> None:
        try:
            self.__pool = self._makeEmptyPool0(3)
        except NotImplementedError:
            return  # skip this test if unsupported

        obj0 = self.__pool.borrowObject()
        self.assertEqual(self._getNthObject(0), obj0)

        obj1 = self.__pool.borrowObject()
        self.assertEqual(self._getNthObject(1), obj1)

        obj2 = self.__pool.borrowObject()
        self.assertEqual(self._getNthObject(2), obj2)

        self.__pool.returnObject(obj2)
        obj2 = self.__pool.borrowObject()
        self.assertEqual(self._getNthObject(2), obj2)

        self.__pool.returnObject(obj1)
        obj1 = self.__pool.borrowObject()
        self.assertEqual(self._getNthObject(1), obj1)

        self.__pool.returnObject(obj0)
        self.__pool.returnObject(obj2)

        obj2 = self.__pool.borrowObject()
        if self._isLifo():
            self.assertEqual(self._getNthObject(2), obj2)

    def testBaseBorrowReturn_test14_decomposed(self) -> None:
        try:
            self.__pool = self._makeEmptyPool0(3)
        except NotImplementedError:
            return  # skip this test if unsupported

        obj0 = self.__pool.borrowObject()
        self.assertEqual(self._getNthObject(0), obj0)

        obj1 = self.__pool.borrowObject()
        self.assertEqual(self._getNthObject(1), obj1)

        obj2 = self.__pool.borrowObject()
        self.assertEqual(self._getNthObject(2), obj2)

        self.__pool.returnObject(obj2)
        obj2 = self.__pool.borrowObject()
        self.assertEqual(self._getNthObject(2), obj2)

        self.__pool.returnObject(obj1)
        obj1 = self.__pool.borrowObject()
        self.assertEqual(self._getNthObject(1), obj1)

        self.__pool.returnObject(obj0)
        self.__pool.returnObject(obj2)
        obj2 = self.__pool.borrowObject()

    def testBaseBorrowReturn_test13_decomposed(self) -> None:
        try:
            self.__pool = self._makeEmptyPool0(3)
        except NotImplementedError:
            return  # skip this test if unsupported

        obj0 = self.__pool.borrowObject()
        self.assertEqual(self._getNthObject(0), obj0)

        obj1 = self.__pool.borrowObject()
        self.assertEqual(self._getNthObject(1), obj1)

        obj2 = self.__pool.borrowObject()
        self.assertEqual(self._getNthObject(2), obj2)

        self.__pool.returnObject(obj2)
        obj2 = self.__pool.borrowObject()
        self.assertEqual(self._getNthObject(2), obj2)

        self.__pool.returnObject(obj1)
        obj1 = self.__pool.borrowObject()
        self.assertEqual(self._getNthObject(1), obj1)

        self.__pool.returnObject(obj0)
        self.__pool.returnObject(obj2)

    def testBaseBorrowReturn_test12_decomposed(self) -> None:
        try:
            self.__pool = self._makeEmptyPool0(3)
        except NotImplementedError:
            return  # skip this test if unsupported

        obj0 = self.__pool.borrowObject()
        self.assertEqual(self._getNthObject(0), obj0)

        obj1 = self.__pool.borrowObject()
        self.assertEqual(self._getNthObject(1), obj1)

        obj2 = self.__pool.borrowObject()
        self.assertEqual(self._getNthObject(2), obj2)

        self.__pool.returnObject(obj2)
        obj2 = self.__pool.borrowObject()
        self.assertEqual(self._getNthObject(2), obj2)

        self.__pool.returnObject(obj1)
        obj1 = self.__pool.borrowObject()
        self.assertEqual(self._getNthObject(1), obj1)

    def testBaseBorrowReturn_test11_decomposed(self) -> None:
        try:
            self.__pool = self._makeEmptyPool0(3)
        except NotImplementedError:
            return  # skip this test if unsupported

        obj0 = self.__pool.borrowObject()
        self.assertEqual(self._getNthObject(0), obj0)

        obj1 = self.__pool.borrowObject()
        self.assertEqual(self._getNthObject(1), obj1)

        obj2 = self.__pool.borrowObject()
        self.assertEqual(self._getNthObject(2), obj2)

        self.__pool.returnObject(obj2)
        obj2 = self.__pool.borrowObject()
        self.assertEqual(self._getNthObject(2), obj2)

        self.__pool.returnObject(obj1)
        obj1 = self.__pool.borrowObject()

    def testBaseBorrowReturn_test10_decomposed(self) -> None:
        try:
            self.__pool = self._makeEmptyPool0(3)
        except NotImplementedError:
            return  # skip this test if unsupported

        obj0 = self.__pool.borrowObject()
        self.assertEqual(self._getNthObject(0), obj0)

        obj1 = self.__pool.borrowObject()
        self.assertEqual(self._getNthObject(1), obj1)

        obj2 = self.__pool.borrowObject()
        self.assertEqual(self._getNthObject(2), obj2)

        self.__pool.returnObject(obj2)
        obj2 = self.__pool.borrowObject()
        self.assertEqual(self._getNthObject(2), obj2)

        self.__pool.returnObject(obj1)

    def testBaseBorrowReturn_test9_decomposed(self) -> None:
        try:
            self.__pool = self._makeEmptyPool0(3)
        except NotImplementedError:
            return  # skip this test if unsupported

        obj0 = self.__pool.borrowObject()
        self.assertEqual(self._getNthObject(0), obj0)

        obj1 = self.__pool.borrowObject()
        self.assertEqual(self._getNthObject(1), obj1)

        obj2 = self.__pool.borrowObject()
        self.assertEqual(self._getNthObject(2), obj2)

        self.__pool.returnObject(obj2)
        obj2 = self.__pool.borrowObject()
        self.assertEqual(self._getNthObject(2), obj2)

    def testBaseBorrowReturn_test8_decomposed(self) -> None:
        try:
            self.__pool = self._makeEmptyPool0(3)
        except NotImplementedError:
            return  # skip this test if unsupported

        obj0 = self.__pool.borrowObject()
        self.assertEqual(self._getNthObject(0), obj0)

        obj1 = self.__pool.borrowObject()
        self.assertEqual(self._getNthObject(1), obj1)

        obj2 = self.__pool.borrowObject()
        self.assertEqual(self._getNthObject(2), obj2)

        self.__pool.returnObject(obj2)
        obj2 = self.__pool.borrowObject()

    def testBaseBorrowReturn_test7_decomposed(self) -> None:
        try:
            self.__pool = self._makeEmptyPool0(3)
        except NotImplementedError:
            return  # skip this test if unsupported

        obj0 = self.__pool.borrowObject()
        self.assertEqual(self._getNthObject(0), obj0)

        obj1 = self.__pool.borrowObject()
        self.assertEqual(self._getNthObject(1), obj1)

        obj2 = self.__pool.borrowObject()
        self.assertEqual(self._getNthObject(2), obj2)

        self.__pool.returnObject(obj2)

    def testBaseBorrowReturn_test6_decomposed(self) -> None:
        try:
            self.__pool = self._makeEmptyPool0(3)
        except NotImplementedError:
            return  # skip this test if unsupported

        obj0 = self.__pool.borrowObject()
        self.assertEqual(self._getNthObject(0), obj0)

        obj1 = self.__pool.borrowObject()
        self.assertEqual(self._getNthObject(1), obj1)

        obj2 = self.__pool.borrowObject()
        self.assertEqual(self._getNthObject(2), obj2)

    def testBaseBorrowReturn_test5_decomposed(self) -> None:
        try:
            self.__pool = self._makeEmptyPool0(3)
        except NotImplementedError:
            return  # skip this test if unsupported

        obj0 = self.__pool.borrowObject()
        self.assertEqual(self._getNthObject(0), obj0)

        obj1 = self.__pool.borrowObject()
        self.assertEqual(self._getNthObject(1), obj1)

        obj2 = self.__pool.borrowObject()

    def testBaseBorrowReturn_test4_decomposed(self) -> None:
        try:
            self.__pool = self._makeEmptyPool0(3)
        except NotImplementedError:
            return  # skip this test if unsupported

        obj0 = self.__pool.borrowObject()
        self.assertEqual(self._getNthObject(0), obj0)

        obj1 = self.__pool.borrowObject()
        self.assertEqual(self._getNthObject(1), obj1)

    def testBaseBorrowReturn_test3_decomposed(self) -> None:
        try:
            self.__pool = self._makeEmptyPool0(3)
        except NotImplementedError:
            return  # skip this test if unsupported

        obj0 = self.__pool.borrowObject()
        self.assertEqual(self._getNthObject(0), obj0)

        obj1 = self.__pool.borrowObject()

    def testBaseBorrowReturn_test2_decomposed(self) -> None:
        try:
            self.__pool = self._makeEmptyPool0(3)
        except NotImplementedError:
            return  # skip this test if unsupported

        obj0 = self.__pool.borrowObject()
        self.assertEqual(self._getNthObject(0), obj0)

    def testBaseBorrowReturn_test1_decomposed(self) -> None:
        try:
            self.__pool = self._makeEmptyPool0(3)
        except NotImplementedError:
            return  # skip this test if unsupported
        obj0 = self.__pool.borrowObject()

    def testBaseBorrowReturn_test0_decomposed(self) -> None:
        try:
            self.__pool = self._makeEmptyPool0(3)
        except NotImplementedError:
            return  # skip this test if unsupported

    def testBaseBorrow_test7_decomposed(self) -> None:
        try:
            self.__pool = self._makeEmptyPool0(3)
        except NotImplementedError:
            return  # skip this test if unsupported

        self._getNthObject(0)
        self.assertEqual(self._getNthObject(0), self.__pool.borrowObject())
        self._getNthObject(1)
        self.assertEqual(self._getNthObject(1), self.__pool.borrowObject())
        self._getNthObject(2)
        self.assertEqual(self._getNthObject(2), self.__pool.borrowObject())
        self.__pool.close()

    def testBaseBorrow_test6_decomposed(self) -> None:
        try:
            self.__pool = self._makeEmptyPool0(3)
        except NotImplementedError:
            return  # skip this test if unsupported

        self._getNthObject(0)
        self.assertEqual(self._getNthObject(0), self.__pool.borrowObject())
        self._getNthObject(1)
        self.assertEqual(self._getNthObject(1), self.__pool.borrowObject())
        self._getNthObject(2)
        self.assertEqual(self._getNthObject(2), self.__pool.borrowObject())

    def testBaseBorrow_test5_decomposed(self) -> None:
        try:
            self.__pool = self._makeEmptyPool0(3)
        except NotImplementedError:
            return  # skip this test if unsupported

        self._getNthObject(0)
        self.assertEqual(self._getNthObject(0), self.__pool.borrowObject())
        self._getNthObject(1)
        self.assertEqual(self._getNthObject(1), self.__pool.borrowObject())
        self._getNthObject(2)

    def testBaseBorrow_test4_decomposed(self) -> None:
        try:
            self.__pool = self._makeEmptyPool0(3)
        except NotImplementedError:
            return  # skip this test if unsupported

        self._getNthObject(0)
        self.assertEqual(self._getNthObject(0), self.__pool.borrowObject())
        self._getNthObject(1)
        self.assertEqual(self._getNthObject(1), self.__pool.borrowObject())

    def testBaseBorrow_test3_decomposed(self) -> None:
        try:
            self.__pool = self._makeEmptyPool0(3)
        except NotImplementedError:
            return  # skip this test if unsupported

        self._getNthObject(0)
        self.assertEqual(self._getNthObject(0), self.__pool.borrowObject())
        self._getNthObject(1)

    def testBaseBorrow_test2_decomposed(self) -> None:
        try:
            self.__pool = self._makeEmptyPool0(3)
        except NotImplementedError:
            return  # skip this test if unsupported

        self._getNthObject(0)
        self.assertEqual(self._getNthObject(0), self.__pool.borrowObject())

    def testBaseBorrow_test1_decomposed(self) -> None:
        try:
            self.__pool = self._makeEmptyPool0(3)
        except NotImplementedError:
            return  # skip this test if unsupported
        self._getNthObject(0)

    def testBaseBorrow_test0_decomposed(self) -> None:
        try:
            self.__pool = self._makeEmptyPool0(3)
        except NotImplementedError:
            return  # skip this test if unsupported

    def testBaseAddObject_test1_decomposed(self) -> None:
        try:
            try:
                self.__pool = self._makeEmptyPool0(3)
            except NotImplementedError:
                return  # skip this test if unsupported

            try:
                self.assertEqual(0, self.__pool.getNumIdle())
                self.assertEqual(0, self.__pool.getNumActive())
                self.__pool.addObject()
                self.assertEqual(1, self.__pool.getNumIdle())
                self.assertEqual(0, self.__pool.getNumActive())
                obj = self.__pool.borrowObject()
                self.assertEqual(self._getNthObject(0), obj)
                self.assertEqual(0, self.__pool.getNumIdle())
                self.assertEqual(1, self.__pool.getNumActive())
                self.__pool.returnObject(obj)
                self.assertEqual(1, self.__pool.getNumIdle())
                self.assertEqual(0, self.__pool.getNumActive())
            except NotImplementedError:
                return  # skip this test if one of those calls is unsupported
        finally:
            self.__pool.close()

    def testBaseAddObject_test0_decomposed(self) -> None:
        try:
            self.__pool = self._makeEmptyPool0(3)
        except NotImplementedError:
            return  # skip this test if unsupported

    def _makeEmptyPool(
        self, factory: PooledObjectFactory[typing.Any]
    ) -> ObjectPool[object]:
        return self._makeEmptyPool1(factory)

    def _makeEmptyPool1(
        self, factory: PooledObjectFactory[typing.Any]
    ) -> ObjectPool[object]:
        if type(self) is not TestBaseObjectPool:
            pytest.fail(
                "Subclasses of TestBaseObjectPool must reimplement this method."
            )
        raise NotImplementedError("BaseObjectPool isn't a complete implementation.")

    def _makeEmptyPool0(self, minCapacity: int) -> ObjectPool[str]:
        if type(self) is not TestBaseObjectPool:
            pytest.fail(
                "Subclasses of TestBaseObjectPool must reimplement this method."
            )
        raise NotImplementedError("BaseObjectPool isn't a complete implementation.")

    def _isLifo(self) -> bool:
        if self.__class__ != TestBaseObjectPool:
            pytest.fail(
                "Subclasses of TestBaseObjectPool must reimplement this method."
            )
        return False

    def _isFifo(self) -> bool:
        if self.__class__ != TestBaseObjectPool:
            pytest.fail(
                "Subclasses of TestBaseObjectPool must reimplement this method."
            )
        return False

    def _getNthObject(self, n: int) -> typing.Any:
        if self.__class__ != TestBaseObjectPool:
            pytest.fail(
                "Subclasses of TestBaseObjectPool must reimplement this method."
            )
        raise NotImplementedError("BaseObjectPool isn't a complete implementation.")
