from __future__ import annotations
import re
import unittest
import pytest
import io
import os
import unittest
from src.main.org.apache.commons.pool2.impl.PooledSoftReference import *


class TestPooledSoftReference(unittest.TestCase):

    __REFERENT2: str = "test2"
    __REFERENT: str = "test"
    ref: PooledSoftReference[str] = None

    def testToString_test0_decomposed(self) -> None:
        expected = "Referenced Object: test, State: IDLE"
        self.assertEqual(expected, self.ref.__str__())

    def testPooledSoftReference_test6_decomposed(self) -> None:
        self.assertEqual(self.__REFERENT, self.ref.get_object())
        soft_ref = self.ref.get_reference()
        self.assertEqual(self.__REFERENT, soft_ref.get())
        soft_ref.clear()
        soft_ref = SoftReference(self.__REFERENT2)
        self.ref.set_reference(soft_ref)
        self.assertEqual(self.__REFERENT2, self.ref.get_object())
        soft_ref = self.ref.get_reference()
        self.assertEqual(self.__REFERENT2, soft_ref.get())
        soft_ref.clear()

    def testPooledSoftReference_test5_decomposed(self) -> None:
        self.assertEqual(self.__REFERENT, self.ref.getObject())
        soft_ref = self.ref.getReference()
        self.assertEqual(self.__REFERENT, soft_ref.get())
        soft_ref.clear()
        soft_ref = SoftReference(self.__REFERENT2)
        self.ref.setReference(soft_ref)
        self.assertEqual(self.__REFERENT2, self.ref.getObject())
        soft_ref = self.ref.getReference()

    def testPooledSoftReference_test4_decomposed(self) -> None:
        self.assertEqual(self.__REFERENT, self.ref.getObject())
        soft_ref = self.ref.getReference()
        self.assertEqual(self.__REFERENT, soft_ref.get())
        soft_ref.clear()
        soft_ref = SoftReference(self.__REFERENT2)
        self.ref.setReference(soft_ref)
        self.assertEqual(self.__REFERENT2, self.ref.getObject())

    def testPooledSoftReference_test3_decomposed(self) -> None:
        self.assertEqual(self.__REFERENT, self.ref.getObject())
        soft_ref = self.ref.getReference()
        self.assertEqual(self.__REFERENT, soft_ref.get())
        soft_ref.clear()
        soft_ref = SoftReference(self.__REFERENT2)
        self.ref.setReference(soft_ref)

    def testPooledSoftReference_test2_decomposed(self) -> None:
        self.assertEqual(self.__REFERENT, self.ref.getObject())
        soft_ref = self.ref.getReference()
        self.assertEqual(self.__REFERENT, soft_ref.get())
        soft_ref.clear()

    def testPooledSoftReference_test1_decomposed(self) -> None:
        self.assertEqual(self.__REFERENT, self.ref.getObject())
        soft_ref = self.ref.getReference()

    def testPooledSoftReference_test0_decomposed(self) -> None:
        self.assertEqual(self.__REFERENT, self.ref.getObject())

    def setUp(self) -> None:
        soft_ref = SoftReference(self.__REFERENT)
        self.ref = PooledSoftReference(soft_ref)
