from __future__ import annotations
import time
import re
import datetime
import unittest
import pytest
import io
import os
import unittest
from src.main.org.apache.commons.exec.PumpStreamHandler import *


class PumpStreamHandlerTest(unittest.TestCase):

    def testSetStopTimeout_test9_decomposed(self) -> None:
        handler = PumpStreamHandler.PumpStreamHandler0()
        self.assertEqual(datetime.timedelta(0), handler.getStopTimeout())

        handler.setStopTimeout0(datetime.timedelta(minutes=1))
        self.assertEqual(datetime.timedelta(minutes=1), handler.getStopTimeout())

        handler.setStopTimeout1(0)
        self.assertEqual(datetime.timedelta(0), handler.getStopTimeout())

        handler.setStopTimeout1(60_001)
        self.assertEqual(
            datetime.timedelta(milliseconds=60_001), handler.getStopTimeout()
        )

        handler.setStopTimeout0(None)
        self.assertEqual(datetime.timedelta(0), handler.getStopTimeout())

    def testSetStopTimeout_test8_decomposed(self) -> None:
        handler = PumpStreamHandler.PumpStreamHandler0()
        self.assertEqual(datetime.timedelta(0), handler.getStopTimeout())

        handler.setStopTimeout0(datetime.timedelta(minutes=1))
        self.assertEqual(datetime.timedelta(minutes=1), handler.getStopTimeout())

        handler.setStopTimeout1(0)
        self.assertEqual(datetime.timedelta(0), handler.getStopTimeout())

        handler.setStopTimeout1(60_001)
        self.assertEqual(
            datetime.timedelta(milliseconds=60_001), handler.getStopTimeout()
        )

        handler.setStopTimeout0(None)

    def testSetStopTimeout_test7_decomposed(self) -> None:
        handler = PumpStreamHandler.PumpStreamHandler0()
        self.assertEqual(datetime.timedelta(0), handler.getStopTimeout())

        handler.setStopTimeout0(datetime.timedelta(minutes=1))
        self.assertEqual(datetime.timedelta(minutes=1), handler.getStopTimeout())

        handler.setStopTimeout1(0)
        self.assertEqual(datetime.timedelta(0), handler.getStopTimeout())

        handler.setStopTimeout1(60_001)
        self.assertEqual(
            datetime.timedelta(milliseconds=60_001), handler.getStopTimeout()
        )

    def testSetStopTimeout_test6_decomposed(self) -> None:
        handler = PumpStreamHandler.PumpStreamHandler0()
        self.assertEqual(datetime.timedelta(0), handler.getStopTimeout())
        handler.setStopTimeout0(datetime.timedelta(minutes=1))
        self.assertEqual(datetime.timedelta(minutes=1), handler.getStopTimeout())
        handler.setStopTimeout1(0)
        self.assertEqual(datetime.timedelta(0), handler.getStopTimeout())
        handler.setStopTimeout1(60001)

    def testSetStopTimeout_test5_decomposed(self) -> None:
        handler = PumpStreamHandler.PumpStreamHandler0()
        self.assertEqual(datetime.timedelta(0), handler.getStopTimeout())
        handler.setStopTimeout0(datetime.timedelta(minutes=1))
        self.assertEqual(datetime.timedelta(minutes=1), handler.getStopTimeout())
        handler.setStopTimeout1(0)
        self.assertEqual(datetime.timedelta(0), handler.getStopTimeout())

    def testSetStopTimeout_test4_decomposed(self) -> None:
        handler = PumpStreamHandler.PumpStreamHandler0()
        self.assertEqual(datetime.timedelta(0), handler.getStopTimeout())
        handler.setStopTimeout0(datetime.timedelta(minutes=1))
        self.assertEqual(datetime.timedelta(minutes=1), handler.getStopTimeout())
        handler.setStopTimeout1(0)

    def testSetStopTimeout_test3_decomposed(self) -> None:
        handler = PumpStreamHandler.PumpStreamHandler0()
        self.assertEqual(datetime.timedelta(0), handler.getStopTimeout())
        handler.setStopTimeout0(datetime.timedelta(minutes=1))
        self.assertEqual(datetime.timedelta(minutes=1), handler.getStopTimeout())

    def testSetStopTimeout_test2_decomposed(self) -> None:
        handler = PumpStreamHandler.PumpStreamHandler0()
        self.assertEqual(datetime.timedelta(0), handler.getStopTimeout())
        handler.setStopTimeout0(datetime.timedelta(minutes=1))

    def testSetStopTimeout_test1_decomposed(self) -> None:
        handler = PumpStreamHandler.PumpStreamHandler0()
        self.assertEqual(
            datetime.timedelta(0),
            handler.getStopTimeout(),
            "Stop timeout does not match expected value of 0",
        )

    def testSetStopTimeout_test0_decomposed(self) -> None:
        handler = PumpStreamHandler.PumpStreamHandler0()
