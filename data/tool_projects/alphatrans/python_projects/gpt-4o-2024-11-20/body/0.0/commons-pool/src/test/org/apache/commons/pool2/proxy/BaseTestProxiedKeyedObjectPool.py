from __future__ import annotations
import time
import re
import unittest
import pytest
from abc import ABC
from io import StringIO
import io
import datetime
import os
import unittest
from src.main.org.apache.commons.pool2.KeyedObjectPool import *
from src.main.org.apache.commons.pool2.proxy.ProxySource import *


class BaseTestProxiedKeyedObjectPool(ABC, unittest.TestCase):

    __log: io.StringIO = None

    __pool: KeyedObjectPool[str, TestObject] = None

    __ABANDONED_TIMEOUT_SECS: datetime.timedelta = datetime.timedelta(seconds=3)
    __DATA1: str = "data1"
    __KEY1: str = "key1"

    def testUsageTracking_test4_decomposed(self) -> None:
        obj = self.__pool.borrowObject(self.__KEY1)
        self.assertIsNotNone(obj)
        obj.setData(self.__DATA1)
        time.sleep(
            (
                self.__ABANDONED_TIMEOUT_SECS + datetime.timedelta(seconds=2)
            ).total_seconds()
        )
        self.__pool.borrowObject(self.__KEY1)
        log_output = self.__log.getvalue()
        self.assertTrue("Pooled object created" in log_output)
        self.assertTrue("The last code to use this object was" in log_output)

    def testUsageTracking_test3_decomposed(self) -> None:
        obj = self.__pool.borrowObject(self.__KEY1)
        self.assertIsNotNone(obj)
        obj.setData(self.__DATA1)
        time.sleep(
            (
                self.__ABANDONED_TIMEOUT_SECS + datetime.timedelta(seconds=2)
            ).total_seconds()
        )
        self.__pool.borrowObject(self.__KEY1)
        log_output = self.__log.getvalue()

    def testUsageTracking_test2_decomposed(self) -> None:
        obj = self.__pool.borrowObject(self.__KEY1)
        self.assertIsNotNone(obj)
        obj.setData(self.__DATA1)
        time.sleep(
            (
                self.__ABANDONED_TIMEOUT_SECS + datetime.timedelta(seconds=2)
            ).total_seconds()
        )
        self.__pool.borrowObject(self.__KEY1)

    def testUsageTracking_test1_decomposed(self) -> None:
        obj = self.__pool.borrowObject(self.__KEY1)
        self.assertIsNotNone(obj)
        obj.setData(self.__DATA1)

    def testUsageTracking_test0_decomposed(self) -> None:
        obj: TestObject = self.__pool.borrowObject(self.__KEY1)

    def testPassThroughMethods02_test1_decomposed(self) -> None:
        self.__pool.close()
        with self.assertRaises(RuntimeError):
            self.__pool.addObject(self.__KEY1)

    def testPassThroughMethods02_test0_decomposed(self) -> None:
        self.__pool.close()

    def testPassThroughMethods01_test7_decomposed(self) -> None:
        self.assertEqual(0, self.__pool.getNumActive0())
        self.assertEqual(0, self.__pool.getNumIdle0())
        self.__pool.addObject(self.__KEY1)
        self.assertEqual(0, self.__pool.getNumActive0())
        self.assertEqual(1, self.__pool.getNumIdle0())
        self.__pool.clear0()
        self.assertEqual(0, self.__pool.getNumActive0())
        self.assertEqual(0, self.__pool.getNumIdle0())

    def testPassThroughMethods01_test6_decomposed(self) -> None:
        self.assertEqual(0, self.__pool.getNumActive0())
        self.assertEqual(0, self.__pool.getNumIdle0())
        self.__pool.addObject(self.__KEY1)
        self.assertEqual(0, self.__pool.getNumActive0())
        self.assertEqual(1, self.__pool.getNumIdle0())
        self.__pool.clear0()
        self.assertEqual(0, self.__pool.getNumActive0())

    def testPassThroughMethods01_test5_decomposed(self) -> None:
        self.assertEqual(0, self.__pool.getNumActive0())
        self.assertEqual(0, self.__pool.getNumIdle0())
        self.__pool.addObject(self.__KEY1)
        self.assertEqual(0, self.__pool.getNumActive0())
        self.assertEqual(1, self.__pool.getNumIdle0())
        self.__pool.clear0()

    def testPassThroughMethods01_test4_decomposed(self) -> None:
        self.assertEqual(0, self.__pool.getNumActive0())
        self.assertEqual(0, self.__pool.getNumIdle0())
        self.__pool.addObject(self.__KEY1)
        self.assertEqual(0, self.__pool.getNumActive0())
        self.assertEqual(1, self.__pool.getNumIdle0())

    def testPassThroughMethods01_test3_decomposed(self) -> None:
        self.assertEqual(0, self.__pool.getNumActive0())
        self.assertEqual(0, self.__pool.getNumIdle0())
        self.__pool.addObject(self.__KEY1)
        self.assertEqual(0, self.__pool.getNumActive0())

    def testPassThroughMethods01_test2_decomposed(self) -> None:
        self.assertEqual(0, self.__pool.getNumActive0())
        self.assertEqual(0, self.__pool.getNumIdle0())
        self.__pool.addObject(self.__KEY1)

    def testPassThroughMethods01_test1_decomposed(self) -> None:
        self.assertEqual(0, self.__pool.getNumActive0())
        self.assertEqual(0, self.__pool.getNumIdle0())

    def testPassThroughMethods01_test0_decomposed(self) -> None:
        self.assertEqual(0, self.__pool.getNumActive0())

    def testBorrowObject_test3_decomposed(self) -> None:
        obj = self.__pool.borrowObject(self.__KEY1)
        self.assertIsNotNone(obj)
        obj.setData(self.__DATA1)
        self.assertEqual(self.__DATA1, obj.getData())
        self.__pool.returnObject(self.__KEY1, obj)

    def testBorrowObject_test2_decomposed(self) -> None:
        obj = self.__pool.borrowObject(self.__KEY1)
        self.assertIsNotNone(obj)
        obj.setData(self.__DATA1)
        self.assertEqual(self.__DATA1, obj.getData())

    def testBorrowObject_test1_decomposed(self) -> None:
        obj = self.__pool.borrowObject(self.__KEY1)
        self.assertIsNotNone(obj)
        obj.setData(self.__DATA1)

    def testBorrowObject_test0_decomposed(self) -> None:
        obj: TestObject = self.__pool.borrowObject(self.__KEY1)

    def testAccessAfterReturn_test4_decomposed(self) -> None:
        obj = self.__pool.borrowObject(self.__KEY1)
        self.assertIsNotNone(obj)
        obj.setData(self.__DATA1)
        self.assertEqual(self.__DATA1, obj.getData())
        self.__pool.returnObject(self.__KEY1, obj)
        self.assertIsNotNone(obj)
        with self.assertRaises(RuntimeError):
            obj.getData()

    def testAccessAfterReturn_test3_decomposed(self) -> None:
        obj = self.__pool.borrowObject(self.__KEY1)
        self.assertIsNotNone(obj)
        obj.setData(self.__DATA1)
        self.assertEqual(self.__DATA1, obj.getData())
        self.__pool.returnObject(self.__KEY1, obj)

    def testAccessAfterReturn_test2_decomposed(self) -> None:
        obj = self.__pool.borrowObject(self.__KEY1)
        self.assertIsNotNone(obj)
        obj.setData(self.__DATA1)
        self.assertEqual(self.__DATA1, obj.getData())

    def testAccessAfterReturn_test1_decomposed(self) -> None:
        obj = self.__pool.borrowObject(self.__KEY1)
        self.assertIsNotNone(obj)
        obj.setData(self.__DATA1)

    def testAccessAfterReturn_test0_decomposed(self) -> None:
        obj: TestObject = self.__pool.borrowObject(self.__KEY1)

    def testAccessAfterInvalidate_test4_decomposed(self) -> None:
        obj = self.__pool.borrowObject(self.__KEY1)
        self.assertIsNotNone(obj)
        obj.setData(self.__DATA1)
        self.assertEqual(self.__DATA1, obj.getData())
        self.__pool.invalidateObject0(self.__KEY1, obj)
        self.assertIsNotNone(obj)
        with self.assertRaises(RuntimeError):
            obj.getData()

    def testAccessAfterInvalidate_test3_decomposed(self) -> None:
        obj = self.__pool.borrowObject(self.__KEY1)
        self.assertIsNotNone(obj)
        obj.setData(self.__DATA1)
        self.assertEqual(self.__DATA1, obj.getData())
        self.__pool.invalidateObject0(self.__KEY1, obj)

    def testAccessAfterInvalidate_test2_decomposed(self) -> None:
        obj = self.__pool.borrowObject(self.__KEY1)
        self.assertIsNotNone(obj)
        obj.setData(self.__DATA1)
        self.assertEqual(self.__DATA1, obj.getData())

    def testAccessAfterInvalidate_test1_decomposed(self) -> None:
        obj = self.__pool.borrowObject(self.__KEY1)
        self.assertIsNotNone(obj)
        obj.setData(self.__DATA1)

    def testAccessAfterInvalidate_test0_decomposed(self) -> None:
        obj: TestObject = self.__pool.borrowObject(self.__KEY1)

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
