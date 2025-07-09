from __future__ import annotations
import time
import re
import unittest
import pytest
from abc import ABC
from io import StringIO
import io
import typing
from typing import *
import datetime
import os
import unittest
from src.main.org.apache.commons.pool2.ObjectPool import *
from src.main.org.apache.commons.pool2.proxy.ProxySource import *


class BaseTestProxiedObjectPool(ABC, unittest.TestCase):

    __log: io.StringIO = None

    __pool: typing.List[TestObject] = None

    __ABANDONED_TIMEOUT_SECS: datetime.timedelta = datetime.timedelta(seconds=3)
    __DATA1: str = "data1"

    def testUsageTracking_test4_decomposed(self) -> None:
        obj = self.__pool.borrowObject()
        self.assertIsNotNone(obj)
        obj.setData(self.__DATA1)
        time.sleep(
            (
                self.__ABANDONED_TIMEOUT_SECS + datetime.timedelta(seconds=2)
            ).total_seconds()
        )
        self.__pool.borrowObject()
        log_output = self.__log.getvalue()
        self.assertIn("Pooled object created", log_output)
        self.assertIn("The last code to use this object was", log_output)

    def testUsageTracking_test3_decomposed(self) -> None:
        obj = self.__pool.borrowObject()
        self.assertIsNotNone(obj)
        obj.setData(self.__DATA1)
        time.sleep(self.__ABANDONED_TIMEOUT_SECS.total_seconds() + 2)
        self.__pool.borrowObject()
        log_output = self.__log.getvalue()

    def testUsageTracking_test2_decomposed(self) -> None:
        obj = self.__pool.borrowObject()
        self.assertIsNotNone(obj)
        obj.setData(self.__DATA1)
        time.sleep(
            (
                self.__ABANDONED_TIMEOUT_SECS + datetime.timedelta(seconds=2)
            ).total_seconds()
        )
        self.__pool.borrowObject()

    def testUsageTracking_test1_decomposed(self) -> None:
        obj = self.__pool.borrowObject()
        self.assertIsNotNone(obj)
        obj.setData(self.__DATA1)

    def testUsageTracking_test0_decomposed(self) -> None:
        obj: TestObject = self.__pool.borrowObject()

    def testPassThroughMethods02_test1_decomposed(self) -> None:
        self.__pool.close()
        with self.assertRaises(RuntimeError):
            self.__pool.addObject()

    def testPassThroughMethods02_test0_decomposed(self) -> None:
        self.__pool.close()

    def testPassThroughMethods01_test7_decomposed(self) -> None:
        self.assertEqual(0, self.__pool.getNumActive())
        self.assertEqual(0, self.__pool.getNumIdle())
        self.__pool.addObject()
        self.assertEqual(0, self.__pool.getNumActive())
        self.assertEqual(1, self.__pool.getNumIdle())
        self.__pool.clear()
        self.assertEqual(0, self.__pool.getNumActive())
        self.assertEqual(0, self.__pool.getNumIdle())

    def testPassThroughMethods01_test6_decomposed(self) -> None:
        self.assertEqual(0, self.__pool.getNumActive())
        self.assertEqual(0, self.__pool.getNumIdle())
        self.__pool.addObject()
        self.assertEqual(0, self.__pool.getNumActive())
        self.assertEqual(1, self.__pool.getNumIdle())
        self.__pool.clear()
        self.assertEqual(0, self.__pool.getNumActive())

    def testPassThroughMethods01_test5_decomposed(self) -> None:
        self.assertEqual(0, self.__pool.getNumActive())
        self.assertEqual(0, self.__pool.getNumIdle())
        self.__pool.addObject()
        self.assertEqual(0, self.__pool.getNumActive())
        self.assertEqual(1, self.__pool.getNumIdle())
        self.__pool.clear()

    def testPassThroughMethods01_test4_decomposed(self) -> None:
        self.assertEqual(0, self.__pool.getNumActive())
        self.assertEqual(0, self.__pool.getNumIdle())
        self.__pool.addObject()
        self.assertEqual(0, self.__pool.getNumActive())
        self.assertEqual(1, self.__pool.getNumIdle())

    def testPassThroughMethods01_test3_decomposed(self) -> None:
        self.assertEqual(0, self.__pool.getNumActive())
        self.assertEqual(0, self.__pool.getNumIdle())
        self.__pool.addObject()
        self.assertEqual(0, self.__pool.getNumActive())

    def testPassThroughMethods01_test2_decomposed(self) -> None:
        self.assertEqual(0, self.__pool.getNumActive())
        self.assertEqual(0, self.__pool.getNumIdle())
        self.__pool.addObject()

    def testPassThroughMethods01_test1_decomposed(self) -> None:
        self.assertEqual(0, self.__pool.getNumActive())
        self.assertEqual(0, self.__pool.getNumIdle())

    def testPassThroughMethods01_test0_decomposed(self) -> None:
        self.assertEqual(0, self.__pool.getNumActive())

    def testBorrowObject_test3_decomposed(self) -> None:
        obj = self.__pool.borrowObject()
        self.assertIsNotNone(obj)
        obj.setData(self.__DATA1)
        self.assertEqual(self.__DATA1, obj.getData())
        self.__pool.returnObject(obj)

    def testBorrowObject_test2_decomposed(self) -> None:
        obj = self.__pool.borrowObject()
        self.assertIsNotNone(obj)
        obj.setData(self.__DATA1)
        self.assertEqual(self.__DATA1, obj.getData())

    def testBorrowObject_test1_decomposed(self) -> None:
        obj = self.__pool.borrowObject()
        self.assertIsNotNone(obj)
        obj.setData(self.__DATA1)

    def testBorrowObject_test0_decomposed(self) -> None:
        obj: TestObject = self.__pool.borrowObject()

    def testAccessAfterReturn_test4_decomposed(self) -> None:
        obj = self.__pool.borrowObject()
        self.assertIsNotNone(obj)
        obj.setData(self.__DATA1)
        self.assertEqual(self.__DATA1, obj.getData())
        self.__pool.returnObject(obj)
        self.assertIsNotNone(obj)
        with self.assertRaises(RuntimeError):
            obj.getData()

    def testAccessAfterReturn_test3_decomposed(self) -> None:
        obj = self.__pool.borrowObject()
        self.assertIsNotNone(obj)
        obj.setData(self.__DATA1)
        self.assertEqual(self.__DATA1, obj.getData())
        self.__pool.returnObject(obj)

    def testAccessAfterReturn_test2_decomposed(self) -> None:
        obj = self.__pool.borrowObject()
        self.assertIsNotNone(obj)
        obj.setData(self.__DATA1)
        self.assertEqual(self.__DATA1, obj.getData())

    def testAccessAfterReturn_test1_decomposed(self) -> None:
        obj = self.__pool.borrowObject()
        self.assertIsNotNone(obj)
        obj.setData(self.__DATA1)

    def testAccessAfterReturn_test0_decomposed(self) -> None:
        obj = self.__pool.borrowObject()

    def testAccessAfterInvalidate_test4_decomposed(self) -> None:
        obj = self.__pool.borrowObject()
        self.assertIsNotNone(obj)
        obj.setData(self.__DATA1)
        self.assertEqual(self.__DATA1, obj.getData())
        self.__pool.invalidateObject0(obj)
        self.assertIsNotNone(obj)
        with self.assertRaises(RuntimeError):
            obj.getData()

    def testAccessAfterInvalidate_test3_decomposed(self) -> None:
        obj = self.__pool.borrowObject()
        self.assertIsNotNone(obj)
        obj.setData(self.__DATA1)
        self.assertEqual(self.__DATA1, obj.getData())
        self.__pool.invalidateObject0(obj)

    def testAccessAfterInvalidate_test2_decomposed(self) -> None:
        obj = self.__pool.borrowObject()
        self.assertIsNotNone(obj)
        obj.setData(self.__DATA1)
        self.assertEqual(self.__DATA1, obj.getData())

    def testAccessAfterInvalidate_test1_decomposed(self) -> None:
        obj = self.__pool.borrowObject()
        self.assertIsNotNone(obj)
        obj.setData(self.__DATA1)

    def testAccessAfterInvalidate_test0_decomposed(self) -> None:
        obj: TestObject = self.__pool.borrowObject()

    def _getproxySource(self) -> ProxySource[TestObject]:
        raise NotImplementedError("Subclasses must implement this method")


class TestObject(ABC):

    def setData(self, data: str) -> None:
        self.data = data

    def getData(self) -> str:
        return ""


class TestObjectImpl(TestObject):

    __data: str = ""

    def setData(self, data: str) -> None:
        self.__data = data

    def getData(self) -> str:
        return self.__data
