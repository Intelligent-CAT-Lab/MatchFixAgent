from __future__ import annotations
import time
import re
import unittest
import pytest
import io
import os
import unittest
from src.main.org.apache.commons.validator.routines.AbstractCalendarValidator import *
from src.test.org.apache.commons.validator.routines.AbstractCalendarValidatorTest import *
from src.main.org.apache.commons.validator.routines.CalendarValidator import *


class CalendarValidatorTest(AbstractCalendarValidatorTest, unittest.TestCase):

    __calValidator: CalendarValidator = None

    __TIME_12_03_45: int = 120345
    __DATE_2005_11_23: int = 20051123

    def testAdjustToTimeZone_test18_decomposed(self) -> None:
        calEST = self._createCalendar(
            self._EST, self.__DATE_2005_11_23, self.__TIME_12_03_45
        )
        dateEST = calEST
        calGMT = self._createCalendar(
            self._GMT, self.__DATE_2005_11_23, self.__TIME_12_03_45
        )
        dateGMT = calGMT
        calCET = self._createCalendar(
            self._EET, self.__DATE_2005_11_23, self.__TIME_12_03_45
        )
        dateCET = calCET

        self.assertFalse(dateGMT.timestamp() == dateCET.timestamp(), "Check GMT != CET")
        self.assertFalse(dateGMT.timestamp() == dateEST.timestamp(), "Check GMT != EST")
        self.assertFalse(dateCET.timestamp() == dateEST.timestamp(), "Check CET != EST")

        CalendarValidator.adjustToTimeZone(calEST, self._GMT)
        self.assertEqual(dateGMT, calEST, "EST to GMT")
        self.assertFalse(dateEST == calEST, "Check EST = GMT")

        CalendarValidator.adjustToTimeZone(calEST, self._EST)
        self.assertEqual(dateEST, calEST, "back to EST")
        self.assertFalse(dateGMT == calEST, "Check EST != GMT")

        CalendarValidator.adjustToTimeZone(calCET, self._GMT)
        self.assertEqual(dateGMT, calCET, "CET to GMT")
        self.assertFalse(dateCET == calCET, "Check CET = GMT")

        CalendarValidator.adjustToTimeZone(calCET, self._EET)
        self.assertEqual(dateCET, calCET, "back to CET")
        self.assertFalse(dateGMT == calCET, "Check CET != GMT")

        calUTC = self._createCalendar(
            self._UTC, self.__DATE_2005_11_23, self.__TIME_12_03_45
        )
        self.assertTrue(self._UTC.key == self._GMT.key, "SAME: UTC = GMT")
        self.assertEqual(calUTC, calGMT, "SAME: Check time (A)")
        self.assertFalse(self._GMT == calUTC.tzinfo, "SAME: Check GMT(A)")
        self.assertTrue(self._UTC == calUTC.tzinfo, "SAME: Check UTC(A)")

        CalendarValidator.adjustToTimeZone(calUTC, self._GMT)
        self.assertEqual(calUTC, calGMT, "SAME: Check time (B)")
        self.assertTrue(self._GMT == calUTC.tzinfo, "SAME: Check GMT(B)")
        self.assertFalse(self._UTC == calUTC.tzinfo, "SAME: Check UTC(B)")

    def testAdjustToTimeZone_test17_decomposed(self) -> None:
        calEST = self._createCalendar(
            self._EST, self.__DATE_2005_11_23, self.__TIME_12_03_45
        )
        dateEST = calEST
        calGMT = self._createCalendar(
            self._GMT, self.__DATE_2005_11_23, self.__TIME_12_03_45
        )
        dateGMT = calGMT
        calCET = self._createCalendar(
            self._EET, self.__DATE_2005_11_23, self.__TIME_12_03_45
        )
        dateCET = calCET

        self.assertFalse(dateGMT.timestamp() == dateCET.timestamp(), "Check GMT != CET")
        self.assertFalse(dateGMT.timestamp() == dateEST.timestamp(), "Check GMT != EST")
        self.assertFalse(dateCET.timestamp() == dateEST.timestamp(), "Check CET != EST")

        CalendarValidator.adjustToTimeZone(calEST, self._GMT)
        self.assertEqual(dateGMT, calEST, "EST to GMT")
        self.assertFalse(dateEST == calEST, "Check EST = GMT")

        CalendarValidator.adjustToTimeZone(calEST, self._EST)
        self.assertEqual(dateEST, calEST, "back to EST")
        self.assertFalse(dateGMT == calEST, "Check EST != GMT")

        CalendarValidator.adjustToTimeZone(calCET, self._GMT)
        self.assertEqual(dateGMT, calCET, "CET to GMT")
        self.assertFalse(dateCET == calCET, "Check CET = GMT")

        CalendarValidator.adjustToTimeZone(calCET, self._EET)
        self.assertEqual(dateCET, calCET, "back to CET")
        self.assertFalse(dateGMT == calCET, "Check CET != GMT")

        calUTC = self._createCalendar(
            self._UTC, self.__DATE_2005_11_23, self.__TIME_12_03_45
        )
        self.assertTrue(self._UTC.key == self._GMT.key, "SAME: UTC = GMT")
        self.assertEqual(calUTC, calGMT, "SAME: Check time (A)")
        self.assertFalse(self._GMT == calUTC.tzinfo, "SAME: Check GMT(A)")
        self.assertTrue(self._UTC == calUTC.tzinfo, "SAME: Check UTC(A)")

        CalendarValidator.adjustToTimeZone(calUTC, self._GMT)
        self.assertEqual(calUTC, calGMT, "SAME: Check time (B)")
        self.assertTrue(self._GMT == calUTC.tzinfo, "SAME: Check GMT(B)")

    def testAdjustToTimeZone_test16_decomposed(self) -> None:
        calEST = self._createCalendar(
            self._EST, self.__DATE_2005_11_23, self.__TIME_12_03_45
        )
        dateEST = calEST
        calGMT = self._createCalendar(
            self._GMT, self.__DATE_2005_11_23, self.__TIME_12_03_45
        )
        dateGMT = calGMT
        calCET = self._createCalendar(
            self._EET, self.__DATE_2005_11_23, self.__TIME_12_03_45
        )
        dateCET = calCET

        self.assertFalse(dateGMT.timestamp() == dateCET.timestamp(), "Check GMT != CET")
        self.assertFalse(dateGMT.timestamp() == dateEST.timestamp(), "Check GMT != EST")
        self.assertFalse(dateCET.timestamp() == dateEST.timestamp(), "Check CET != EST")

        CalendarValidator.adjustToTimeZone(calEST, self._GMT)
        self.assertEqual(dateGMT, calEST, "EST to GMT")
        self.assertFalse(dateEST == calEST, "Check EST = GMT")

        CalendarValidator.adjustToTimeZone(calEST, self._EST)
        self.assertEqual(dateEST, calEST, "back to EST")
        self.assertFalse(dateGMT == calEST, "Check EST != GMT")

        CalendarValidator.adjustToTimeZone(calCET, self._GMT)
        self.assertEqual(dateGMT, calCET, "CET to GMT")
        self.assertFalse(dateCET == calCET, "Check CET = GMT")

        CalendarValidator.adjustToTimeZone(calCET, self._EET)
        self.assertEqual(dateCET, calCET, "back to CET")
        self.assertFalse(dateGMT == calCET, "Check CET != GMT")

        calUTC = self._createCalendar(
            self._UTC, self.__DATE_2005_11_23, self.__TIME_12_03_45
        )
        self.assertTrue(self._UTC.key == self._GMT.key, "SAME: UTC = GMT")
        self.assertEqual(calUTC, calGMT, "SAME: Check time (A)")
        self.assertFalse(self._GMT == calUTC.tzinfo, "SAME: Check GMT(A)")
        self.assertTrue(self._UTC == calUTC.tzinfo, "SAME: Check UTC(A)")

        CalendarValidator.adjustToTimeZone(calUTC, self._GMT)

    def testAdjustToTimeZone_test15_decomposed(self) -> None:
        calEST = self._createCalendar(
            self._EST, self.__DATE_2005_11_23, self.__TIME_12_03_45
        )
        dateEST = calEST
        calGMT = self._createCalendar(
            self._GMT, self.__DATE_2005_11_23, self.__TIME_12_03_45
        )
        dateGMT = calGMT
        calCET = self._createCalendar(
            self._EET, self.__DATE_2005_11_23, self.__TIME_12_03_45
        )
        dateCET = calCET

        self.assertFalse(dateGMT.timestamp() == dateCET.timestamp(), "Check GMT != CET")
        self.assertFalse(dateGMT.timestamp() == dateEST.timestamp(), "Check GMT != EST")
        self.assertFalse(dateCET.timestamp() == dateEST.timestamp(), "Check CET != EST")

        CalendarValidator.adjustToTimeZone(calEST, self._GMT)
        self.assertEqual(dateGMT, calEST, "EST to GMT")
        self.assertFalse(dateEST == calEST, "Check EST = GMT")

        CalendarValidator.adjustToTimeZone(calEST, self._EST)
        self.assertEqual(dateEST, calEST, "back to EST")
        self.assertFalse(dateGMT == calEST, "Check EST != GMT")

        CalendarValidator.adjustToTimeZone(calCET, self._GMT)
        self.assertEqual(dateGMT, calCET, "CET to GMT")
        self.assertFalse(dateCET == calCET, "Check CET = GMT")

        CalendarValidator.adjustToTimeZone(calCET, self._EET)
        self.assertEqual(dateCET, calCET, "back to CET")
        self.assertFalse(dateGMT == calCET, "Check CET != GMT")

        calUTC = self._createCalendar(
            self._UTC, self.__DATE_2005_11_23, self.__TIME_12_03_45
        )
        self.assertTrue(self._UTC.key == self._GMT.key, "SAME: UTC = GMT")
        self.assertEqual(calUTC, calGMT, "SAME: Check time (A)")
        self.assertFalse(self._GMT == calUTC.tzinfo, "SAME: Check GMT(A)")
        self.assertTrue(self._UTC == calUTC.tzinfo, "SAME: Check UTC(A)")

    def testAdjustToTimeZone_test14_decomposed(self) -> None:
        calEST = self._createCalendar(
            self._EST, self.__DATE_2005_11_23, self.__TIME_12_03_45
        )
        dateEST = calEST
        calGMT = self._createCalendar(
            self._GMT, self.__DATE_2005_11_23, self.__TIME_12_03_45
        )
        dateGMT = calGMT
        calCET = self._createCalendar(
            self._EET, self.__DATE_2005_11_23, self.__TIME_12_03_45
        )
        dateCET = calCET

        self.assertFalse(dateGMT.timestamp() == dateCET.timestamp(), "Check GMT != CET")
        self.assertFalse(dateGMT.timestamp() == dateEST.timestamp(), "Check GMT != EST")
        self.assertFalse(dateCET.timestamp() == dateEST.timestamp(), "Check CET != EST")

        CalendarValidator.adjustToTimeZone(calEST, self._GMT)
        self.assertEqual(dateGMT, calEST, "EST to GMT")
        self.assertFalse(dateEST == calEST, "Check EST = GMT")

        CalendarValidator.adjustToTimeZone(calEST, self._EST)
        self.assertEqual(dateEST, calEST, "back to EST")
        self.assertFalse(dateGMT == calEST, "Check EST != GMT")

        CalendarValidator.adjustToTimeZone(calCET, self._GMT)
        self.assertEqual(dateGMT, calCET, "CET to GMT")
        self.assertFalse(dateCET == calCET, "Check CET = GMT")

        CalendarValidator.adjustToTimeZone(calCET, self._EET)
        self.assertEqual(dateCET, calCET, "back to CET")
        self.assertFalse(dateGMT == calCET, "Check CET != GMT")

        calUTC = self._createCalendar(
            self._UTC, self.__DATE_2005_11_23, self.__TIME_12_03_45
        )
        self.assertTrue(self._UTC.key == self._GMT.key, "SAME: UTC = GMT")
        self.assertEqual(calUTC, calGMT, "SAME: Check time (A)")

    def testAdjustToTimeZone_test13_decomposed(self) -> None:
        calEST = self._createCalendar(
            self._EST, self.__DATE_2005_11_23, self.__TIME_12_03_45
        )
        dateEST = calEST
        calGMT = self._createCalendar(
            self._GMT, self.__DATE_2005_11_23, self.__TIME_12_03_45
        )
        dateGMT = calGMT
        calCET = self._createCalendar(
            self._EET, self.__DATE_2005_11_23, self.__TIME_12_03_45
        )
        dateCET = calCET

        self.assertFalse(dateGMT.timestamp() == dateCET.timestamp(), "Check GMT != CET")
        self.assertFalse(dateGMT.timestamp() == dateEST.timestamp(), "Check GMT != EST")
        self.assertFalse(dateCET.timestamp() == dateEST.timestamp(), "Check CET != EST")

        CalendarValidator.adjustToTimeZone(calEST, self._GMT)
        self.assertEqual(dateGMT, calEST, "EST to GMT")
        self.assertFalse(dateEST == calEST, "Check EST = GMT")

        CalendarValidator.adjustToTimeZone(calEST, self._EST)
        self.assertEqual(dateEST, calEST, "back to EST")
        self.assertFalse(dateGMT == calEST, "Check EST != GMT")

        CalendarValidator.adjustToTimeZone(calCET, self._GMT)
        self.assertEqual(dateGMT, calCET, "CET to GMT")
        self.assertFalse(dateCET == calCET, "Check CET = GMT")

        CalendarValidator.adjustToTimeZone(calCET, self._EET)
        self.assertEqual(dateCET, calCET, "back to CET")
        self.assertFalse(dateGMT == calCET, "Check CET != GMT")

        calUTC = self._createCalendar(
            self._UTC, self.__DATE_2005_11_23, self.__TIME_12_03_45
        )

    def testAdjustToTimeZone_test12_decomposed(self) -> None:
        calEST = self._createCalendar(
            self._EST, self.__DATE_2005_11_23, self.__TIME_12_03_45
        )
        dateEST = calEST
        calGMT = self._createCalendar(
            self._GMT, self.__DATE_2005_11_23, self.__TIME_12_03_45
        )
        dateGMT = calGMT
        calCET = self._createCalendar(
            self._EET, self.__DATE_2005_11_23, self.__TIME_12_03_45
        )
        dateCET = calCET

        self.assertFalse(dateGMT.timestamp() == dateCET.timestamp(), "Check GMT != CET")
        self.assertFalse(dateGMT.timestamp() == dateEST.timestamp(), "Check GMT != EST")
        self.assertFalse(dateCET.timestamp() == dateEST.timestamp(), "Check CET != EST")

        CalendarValidator.adjustToTimeZone(calEST, self._GMT)
        self.assertEqual(dateGMT, calEST, "EST to GMT")
        self.assertFalse(dateEST == calEST, "Check EST = GMT")

        CalendarValidator.adjustToTimeZone(calEST, self._EST)
        self.assertEqual(dateEST, calEST, "back to EST")
        self.assertFalse(dateGMT == calEST, "Check EST != GMT")

        CalendarValidator.adjustToTimeZone(calCET, self._GMT)
        self.assertEqual(dateGMT, calCET, "CET to GMT")
        self.assertFalse(dateCET == calCET, "Check CET = GMT")

        CalendarValidator.adjustToTimeZone(calCET, self._EET)
        self.assertEqual(dateCET, calCET, "back to CET")
        self.assertFalse(dateGMT == calCET, "Check CET != GMT")

    def testAdjustToTimeZone_test11_decomposed(self) -> None:
        calEST = self._createCalendar(
            self._EST, self.__DATE_2005_11_23, self.__TIME_12_03_45
        )
        dateEST = calEST
        calGMT = self._createCalendar(
            self._GMT, self.__DATE_2005_11_23, self.__TIME_12_03_45
        )
        dateGMT = calGMT
        calCET = self._createCalendar(
            self._EET, self.__DATE_2005_11_23, self.__TIME_12_03_45
        )
        dateCET = calCET

        self.assertFalse(dateGMT.timestamp() == dateCET.timestamp(), "Check GMT != CET")
        self.assertFalse(dateGMT.timestamp() == dateEST.timestamp(), "Check GMT != EST")
        self.assertFalse(dateCET.timestamp() == dateEST.timestamp(), "Check CET != EST")

        CalendarValidator.adjustToTimeZone(calEST, self._GMT)
        self.assertEqual(dateGMT, calEST, "EST to GMT")
        self.assertFalse(dateEST == calEST, "Check EST = GMT")

        CalendarValidator.adjustToTimeZone(calEST, self._EST)
        self.assertEqual(dateEST, calEST, "back to EST")
        self.assertFalse(dateGMT == calEST, "Check EST != GMT")

        CalendarValidator.adjustToTimeZone(calCET, self._GMT)
        self.assertEqual(dateGMT, calCET, "CET to GMT")
        self.assertFalse(dateCET == calCET, "Check CET = GMT")

        CalendarValidator.adjustToTimeZone(calCET, self._EET)

    def testAdjustToTimeZone_test10_decomposed(self) -> None:
        calEST = self._createCalendar(
            self._EST, self.__DATE_2005_11_23, self.__TIME_12_03_45
        )
        dateEST = calEST
        calGMT = self._createCalendar(
            self._GMT, self.__DATE_2005_11_23, self.__TIME_12_03_45
        )
        dateGMT = calGMT
        calCET = self._createCalendar(
            self._EET, self.__DATE_2005_11_23, self.__TIME_12_03_45
        )
        dateCET = calCET

        self.assertFalse(dateGMT.timestamp() == dateCET.timestamp(), "Check GMT != CET")
        self.assertFalse(dateGMT.timestamp() == dateEST.timestamp(), "Check GMT != EST")
        self.assertFalse(dateCET.timestamp() == dateEST.timestamp(), "Check CET != EST")

        CalendarValidator.adjustToTimeZone(calEST, self._GMT)
        self.assertEqual(dateGMT, calEST, "EST to GMT")
        self.assertFalse(dateEST == calEST, "Check EST = GMT")

        CalendarValidator.adjustToTimeZone(calEST, self._EST)
        self.assertEqual(dateEST, calEST, "back to EST")
        self.assertFalse(dateGMT == calEST, "Check EST != GMT")

        CalendarValidator.adjustToTimeZone(calCET, self._GMT)
        self.assertEqual(dateGMT, calCET, "CET to GMT")
        self.assertFalse(dateCET == calCET, "Check CET = GMT")

    def testAdjustToTimeZone_test9_decomposed(self) -> None:
        calEST = self._createCalendar(
            self._EST, self.__DATE_2005_11_23, self.__TIME_12_03_45
        )
        dateEST = calEST
        calGMT = self._createCalendar(
            self._GMT, self.__DATE_2005_11_23, self.__TIME_12_03_45
        )
        dateGMT = calGMT
        calCET = self._createCalendar(
            self._EET, self.__DATE_2005_11_23, self.__TIME_12_03_45
        )
        dateCET = calCET

        self.assertFalse(dateGMT.timestamp() == dateCET.timestamp(), "Check GMT != CET")
        self.assertFalse(dateGMT.timestamp() == dateEST.timestamp(), "Check GMT != EST")
        self.assertFalse(dateCET.timestamp() == dateEST.timestamp(), "Check CET != EST")

        CalendarValidator.adjustToTimeZone(calEST, self._GMT)
        self.assertEqual(dateGMT, calEST, "EST to GMT")
        self.assertFalse(dateEST == calEST, "Check EST = GMT")

        CalendarValidator.adjustToTimeZone(calEST, self._EST)
        self.assertEqual(dateEST, calEST, "back to EST")
        self.assertFalse(dateGMT == calEST, "Check EST != GMT")

        CalendarValidator.adjustToTimeZone(calCET, self._GMT)

    def testAdjustToTimeZone_test8_decomposed(self) -> None:
        calEST = self._createCalendar(
            self._EST, self.__DATE_2005_11_23, self.__TIME_12_03_45
        )
        dateEST = calEST
        calGMT = self._createCalendar(
            self._GMT, self.__DATE_2005_11_23, self.__TIME_12_03_45
        )
        dateGMT = calGMT
        calCET = self._createCalendar(
            self._EET, self.__DATE_2005_11_23, self.__TIME_12_03_45
        )
        dateCET = calCET

        self.assertFalse(dateGMT.timestamp() == dateCET.timestamp(), "Check GMT != CET")
        self.assertFalse(dateGMT.timestamp() == dateEST.timestamp(), "Check GMT != EST")
        self.assertFalse(dateCET.timestamp() == dateEST.timestamp(), "Check CET != EST")

        CalendarValidator.adjustToTimeZone(calEST, self._GMT)
        self.assertEqual(dateGMT, calEST, "EST to GMT")
        self.assertFalse(dateEST == calEST, "Check EST = GMT")

        CalendarValidator.adjustToTimeZone(calEST, self._EST)
        self.assertEqual(dateEST, calEST, "back to EST")
        self.assertFalse(dateGMT == calEST, "Check EST != GMT")

    def testAdjustToTimeZone_test7_decomposed(self) -> None:
        calEST = self._createCalendar(
            self._EST, self.__DATE_2005_11_23, self.__TIME_12_03_45
        )
        dateEST = calEST
        calGMT = self._createCalendar(
            self._GMT, self.__DATE_2005_11_23, self.__TIME_12_03_45
        )
        dateGMT = calGMT
        calCET = self._createCalendar(
            self._EET, self.__DATE_2005_11_23, self.__TIME_12_03_45
        )
        dateCET = calCET

        self.assertFalse(dateGMT.timestamp() == dateCET.timestamp(), "Check GMT != CET")
        self.assertFalse(dateGMT.timestamp() == dateEST.timestamp(), "Check GMT != EST")
        self.assertFalse(dateCET.timestamp() == dateEST.timestamp(), "Check CET != EST")

        CalendarValidator.adjustToTimeZone(calEST, self._GMT)
        self.assertEqual(dateGMT, calEST, "EST to GMT")
        self.assertFalse(dateEST == calEST, "Check EST = GMT")

        CalendarValidator.adjustToTimeZone(calEST, self._EST)

    def testAdjustToTimeZone_test6_decomposed(self) -> None:
        calEST = self._createCalendar(
            self._EST, self.__DATE_2005_11_23, self.__TIME_12_03_45
        )
        dateEST = calEST
        calGMT = self._createCalendar(
            self._GMT, self.__DATE_2005_11_23, self.__TIME_12_03_45
        )
        dateGMT = calGMT
        calCET = self._createCalendar(
            self._EET, self.__DATE_2005_11_23, self.__TIME_12_03_45
        )
        dateCET = calCET

        self.assertFalse(dateGMT.timestamp() == dateCET.timestamp(), "Check GMT != CET")
        self.assertFalse(dateGMT.timestamp() == dateEST.timestamp(), "Check GMT != EST")
        self.assertFalse(dateCET.timestamp() == dateEST.timestamp(), "Check CET != EST")

        CalendarValidator.adjustToTimeZone(calEST, self._GMT)
        self.assertEqual(dateGMT, calEST, "EST to GMT")
        self.assertFalse(dateEST == calEST, "Check EST = GMT")

    def testAdjustToTimeZone_test5_decomposed(self) -> None:
        calEST = self._createCalendar(
            self._EST, self.__DATE_2005_11_23, self.__TIME_12_03_45
        )
        dateEST = calEST
        calGMT = self._createCalendar(
            self._GMT, self.__DATE_2005_11_23, self.__TIME_12_03_45
        )
        dateGMT = calGMT
        calCET = self._createCalendar(
            self._EET, self.__DATE_2005_11_23, self.__TIME_12_03_45
        )
        dateCET = calCET

        self.assertFalse(dateGMT.timestamp() == dateCET.timestamp(), "Check GMT != CET")
        self.assertFalse(dateGMT.timestamp() == dateEST.timestamp(), "Check GMT != EST")
        self.assertFalse(dateCET.timestamp() == dateEST.timestamp(), "Check CET != EST")

        CalendarValidator.adjustToTimeZone(calEST, self._GMT)

    def testAdjustToTimeZone_test4_decomposed(self) -> None:
        calEST = self._createCalendar(
            self._EST, self.__DATE_2005_11_23, self.__TIME_12_03_45
        )
        dateEST = calEST.timestamp()
        calGMT = self._createCalendar(
            self._GMT, self.__DATE_2005_11_23, self.__TIME_12_03_45
        )
        dateGMT = calGMT.timestamp()
        calCET = self._createCalendar(
            self._EET, self.__DATE_2005_11_23, self.__TIME_12_03_45
        )
        dateCET = calCET.timestamp()

        self.assertFalse(dateGMT == dateCET, "Check GMT != CET")
        self.assertFalse(dateGMT == dateEST, "Check GMT != EST")
        self.assertFalse(dateCET == dateEST, "Check CET != EST")

    def testAdjustToTimeZone_test3_decomposed(self) -> None:
        calEST = self._createCalendar(
            self._EST, self.__DATE_2005_11_23, self.__TIME_12_03_45
        )
        dateEST = calEST
        calGMT = self._createCalendar(
            self._GMT, self.__DATE_2005_11_23, self.__TIME_12_03_45
        )
        dateGMT = calGMT
        calCET = self._createCalendar(
            self._EET, self.__DATE_2005_11_23, self.__TIME_12_03_45
        )
        dateCET = calCET
        self.assertFalse(dateGMT.timestamp() == dateCET.timestamp(), "Check GMT != CET")

    def testAdjustToTimeZone_test2_decomposed(self) -> None:
        calEST = self._createCalendar(
            self._EST, self.__DATE_2005_11_23, self.__TIME_12_03_45
        )
        dateEST = calEST.getTime()
        calGMT = self._createCalendar(
            self._GMT, self.__DATE_2005_11_23, self.__TIME_12_03_45
        )
        dateGMT = calGMT.getTime()
        calCET = self._createCalendar(
            self._EET, self.__DATE_2005_11_23, self.__TIME_12_03_45
        )

    def testAdjustToTimeZone_test1_decomposed(self) -> None:
        calEST = self._createCalendar(
            self._EST, self.__DATE_2005_11_23, self.__TIME_12_03_45
        )
        dateEST = (
            calEST.getTime()
        )  # Assuming getTime() is equivalent to accessing the datetime object in Python
        calGMT = self._createCalendar(
            self._GMT, self.__DATE_2005_11_23, self.__TIME_12_03_45
        )

    def testAdjustToTimeZone_test0_decomposed(self) -> None:
        calEST = self._createCalendar(
            self._EST, self.__DATE_2005_11_23, self.__TIME_12_03_45
        )

    def testDateTimeStyle_test3_decomposed(self) -> None:
        orig_default = Locale.getDefault()
        Locale.setDefault(Locale.UK)

        class CustomCalendarValidator(AbstractCalendarValidator):
            def __init__(self):
                super().__init__(True, 3, 3)

            def processParsedValue(self, value: object, formatter: Format) -> object:
                return value

        date_time_validator = CustomCalendarValidator()

        self.assertTrue(
            date_time_validator.isValid0("31/12/05 14:23"), "validate(A) default"
        )
        self.assertTrue(
            date_time_validator.isValid2("12/31/05 2:23 PM", Locale.US),
            "validate(A) locale",
        )

        Locale.setDefault(orig_default)

    def testDateTimeStyle_test2_decomposed(self) -> None:
        orig_default = Locale.getDefault()
        Locale.setDefault(Locale.UK)

        class CustomCalendarValidator(AbstractCalendarValidator):
            def __init__(self, strict: bool, date_style: int, time_style: int) -> None:
                super().__init__(strict, date_style, time_style)

            def processParsedValue(self, value: object, formatter: Format) -> object:
                return value

        date_time_validator = CustomCalendarValidator(True, 3, 3)

        self.assertTrue(
            date_time_validator.isValid0("31/12/05 14:23"), "validate(A) default"
        )
        self.assertTrue(
            date_time_validator.isValid2("12/31/05 2:23 PM", Locale.US),
            "validate(A) locale",
        )

    def testDateTimeStyle_test1_decomposed(self) -> None:
        orig_default = Locale.getDefault()
        Locale.setDefault(Locale.UK)

        class CustomCalendarValidator(AbstractCalendarValidator):
            def __init__(self, strict: bool, date_style: int, time_style: int) -> None:
                super().__init__(strict, date_style, time_style)

            def processParsedValue(self, value: object, formatter: Format) -> object:
                return value

        date_time_validator = CustomCalendarValidator(True, 3, 3)
        self.assertTrue(
            date_time_validator.isValid0("31/12/05 14:23"), "validate(A) default"
        )

    def testDateTimeStyle_test0_decomposed(self) -> None:
        orig_default = Locale.getDefault()
        Locale.setDefault(Locale.UK)

        class CustomCalendarValidator(AbstractCalendarValidator):
            __serialVersionUID: int = 1

            def __init__(self, strict: bool, date_style: int, time_style: int) -> None:
                super().__init__(strict, date_style, time_style)

            def process_parsed_value(self, value: object, formatter: Format) -> object:
                return value

        date_time_validator = CustomCalendarValidator(True, 3, 3)

    def testCompare_test13_decomposed(self) -> None:
        same_time = 124522
        test_date = 20050823
        diff_hour = self._createCalendar(self._GMT, test_date, 115922)
        diff_min = self._createCalendar(self._GMT, test_date, 124422)
        diff_sec = self._createCalendar(self._GMT, test_date, 124521)
        value = self._createCalendar(self._GMT, test_date, same_time)
        cal_20050824 = self._createCalendar(self._GMT, 20050824, same_time)
        cal_20050822 = self._createCalendar(self._GMT, 20050822, same_time)
        cal_20050830 = self._createCalendar(self._GMT, 20050830, same_time)
        cal_20050816 = self._createCalendar(self._GMT, 20050816, same_time)
        cal_20050901 = self._createCalendar(self._GMT, 20050901, same_time)
        cal_20050801 = self._createCalendar(self._GMT, 20050801, same_time)
        cal_20050731 = self._createCalendar(self._GMT, 20050731, same_time)
        cal_20051101 = self._createCalendar(self._GMT, 20051101, same_time)
        cal_20051001 = self._createCalendar(self._GMT, 20051001, same_time)
        cal_20050701 = self._createCalendar(self._GMT, 20050701, same_time)
        cal_20050630 = self._createCalendar(self._GMT, 20050630, same_time)
        cal_20060101 = self._createCalendar(self._GMT, 20060101, same_time)
        cal_20050101 = self._createCalendar(self._GMT, 20050101, same_time)
        cal_20041231 = self._createCalendar(self._GMT, 20041231, same_time)

        self.assertEqual(1, self.__calValidator.compare(value, diff_hour, "hour"))
        self.assertEqual(0, self.__calValidator.compare(value, diff_min, "hour"))
        self.assertEqual(1, self.__calValidator.compare(value, diff_min, "minute"))
        self.assertEqual(0, self.__calValidator.compare(value, diff_sec, "minute"))
        self.assertEqual(1, self.__calValidator.compare(value, diff_sec, "second"))
        self.assertEqual(-1, self.__calValidator.compareDates(value, cal_20050824))
        self.assertEqual(0, self.__calValidator.compareDates(value, diff_hour))
        self.assertEqual(
            0, self.__calValidator.compare(value, diff_hour, "day_of_year")
        )
        self.assertEqual(1, self.__calValidator.compareDates(value, cal_20050822))
        self.assertEqual(-1, self.__calValidator.compareWeeks(value, cal_20050830))
        self.assertEqual(0, self.__calValidator.compareWeeks(value, cal_20050824))
        self.assertEqual(0, self.__calValidator.compareWeeks(value, cal_20050822))
        self.assertEqual(
            0, self.__calValidator.compare(value, cal_20050822, "week_of_month")
        )
        self.assertEqual(0, self.__calValidator.compareWeeks(value, cal_20050822))
        self.assertEqual(1, self.__calValidator.compareWeeks(value, cal_20050816))
        self.assertEqual(-1, self.__calValidator.compareMonths(value, cal_20050901))
        self.assertEqual(0, self.__calValidator.compareMonths(value, cal_20050830))
        self.assertEqual(0, self.__calValidator.compareMonths(value, cal_20050801))
        self.assertEqual(0, self.__calValidator.compareMonths(value, cal_20050816))
        self.assertEqual(1, self.__calValidator.compareMonths(value, cal_20050731))
        self.assertEqual(-1, self.__calValidator.compareQuarters0(value, cal_20051101))
        self.assertEqual(-1, self.__calValidator.compareQuarters0(value, cal_20051001))
        self.assertEqual(0, self.__calValidator.compareQuarters0(value, cal_20050901))
        self.assertEqual(0, self.__calValidator.compareQuarters0(value, cal_20050701))
        self.assertEqual(0, self.__calValidator.compareQuarters0(value, cal_20050731))
        self.assertEqual(1, self.__calValidator.compareQuarters0(value, cal_20050630))
        self.assertEqual(
            -1, self.__calValidator.compareQuarters1(value, cal_20051101, 2)
        )
        self.assertEqual(
            0, self.__calValidator.compareQuarters1(value, cal_20051001, 2)
        )
        self.assertEqual(
            0, self.__calValidator.compareQuarters1(value, cal_20050901, 2)
        )
        self.assertEqual(
            1, self.__calValidator.compareQuarters1(value, cal_20050701, 2)
        )
        self.assertEqual(
            1, self.__calValidator.compareQuarters1(value, cal_20050731, 2)
        )
        self.assertEqual(
            1, self.__calValidator.compareQuarters1(value, cal_20050630, 2)
        )
        self.assertEqual(-1, self.__calValidator.compareYears(value, cal_20060101))
        self.assertEqual(0, self.__calValidator.compareYears(value, cal_20050101))
        self.assertEqual(1, self.__calValidator.compareYears(value, cal_20041231))

        with pytest.raises(ValueError) as excinfo:
            self.__calValidator.compare(value, value, -1)
        self.assertEqual("Invalid field: -1", str(excinfo.value))

    def testCompare_test12_decomposed(self) -> None:
        same_time = 124522
        test_date = 20050823
        diff_hour = self._createCalendar(self._GMT, test_date, 115922)
        diff_min = self._createCalendar(self._GMT, test_date, 124422)
        diff_sec = self._createCalendar(self._GMT, test_date, 124521)
        value = self._createCalendar(self._GMT, test_date, same_time)
        cal_20050824 = self._createCalendar(self._GMT, 20050824, same_time)
        cal_20050822 = self._createCalendar(self._GMT, 20050822, same_time)
        cal_20050830 = self._createCalendar(self._GMT, 20050830, same_time)
        cal_20050816 = self._createCalendar(self._GMT, 20050816, same_time)
        cal_20050901 = self._createCalendar(self._GMT, 20050901, same_time)
        cal_20050801 = self._createCalendar(self._GMT, 20050801, same_time)
        cal_20050731 = self._createCalendar(self._GMT, 20050731, same_time)
        cal_20051101 = self._createCalendar(self._GMT, 20051101, same_time)
        cal_20051001 = self._createCalendar(self._GMT, 20051001, same_time)
        cal_20050701 = self._createCalendar(self._GMT, 20050701, same_time)
        cal_20050630 = self._createCalendar(self._GMT, 20050630, same_time)
        cal_20060101 = self._createCalendar(self._GMT, 20060101, same_time)
        cal_20050101 = self._createCalendar(self._GMT, 20050101, same_time)
        cal_20041231 = self._createCalendar(self._GMT, 20041231, same_time)

        self.assertEqual(1, self.__calValidator.compare(value, diff_hour, "hour"))
        self.assertEqual(0, self.__calValidator.compare(value, diff_min, "hour"))
        self.assertEqual(1, self.__calValidator.compare(value, diff_min, "minute"))
        self.assertEqual(0, self.__calValidator.compare(value, diff_sec, "minute"))
        self.assertEqual(1, self.__calValidator.compare(value, diff_sec, "second"))
        self.assertEqual(-1, self.__calValidator.compareDates(value, cal_20050824))
        self.assertEqual(0, self.__calValidator.compareDates(value, diff_hour))
        self.assertEqual(
            0, self.__calValidator.compare(value, diff_hour, "day_of_year")
        )
        self.assertEqual(1, self.__calValidator.compareDates(value, cal_20050822))
        self.assertEqual(-1, self.__calValidator.compareWeeks(value, cal_20050830))
        self.assertEqual(0, self.__calValidator.compareWeeks(value, cal_20050824))
        self.assertEqual(0, self.__calValidator.compareWeeks(value, cal_20050822))
        self.assertEqual(
            0, self.__calValidator.compare(value, cal_20050822, "week_of_month")
        )
        self.assertEqual(0, self.__calValidator.compareWeeks(value, cal_20050822))
        self.assertEqual(1, self.__calValidator.compareWeeks(value, cal_20050816))
        self.assertEqual(-1, self.__calValidator.compareMonths(value, cal_20050901))
        self.assertEqual(0, self.__calValidator.compareMonths(value, cal_20050830))
        self.assertEqual(0, self.__calValidator.compareMonths(value, cal_20050801))
        self.assertEqual(0, self.__calValidator.compareMonths(value, cal_20050816))
        self.assertEqual(1, self.__calValidator.compareMonths(value, cal_20050731))
        self.assertEqual(-1, self.__calValidator.compareQuarters0(value, cal_20051101))
        self.assertEqual(-1, self.__calValidator.compareQuarters0(value, cal_20051001))
        self.assertEqual(0, self.__calValidator.compareQuarters0(value, cal_20050901))
        self.assertEqual(0, self.__calValidator.compareQuarters0(value, cal_20050701))
        self.assertEqual(0, self.__calValidator.compareQuarters0(value, cal_20050731))
        self.assertEqual(1, self.__calValidator.compareQuarters0(value, cal_20050630))
        self.assertEqual(
            -1, self.__calValidator.compareQuarters1(value, cal_20051101, 2)
        )
        self.assertEqual(
            0, self.__calValidator.compareQuarters1(value, cal_20051001, 2)
        )
        self.assertEqual(
            0, self.__calValidator.compareQuarters1(value, cal_20050901, 2)
        )
        self.assertEqual(
            1, self.__calValidator.compareQuarters1(value, cal_20050701, 2)
        )
        self.assertEqual(
            1, self.__calValidator.compareQuarters1(value, cal_20050731, 2)
        )
        self.assertEqual(
            1, self.__calValidator.compareQuarters1(value, cal_20050630, 2)
        )
        self.assertEqual(-1, self.__calValidator.compareYears(value, cal_20060101))
        self.assertEqual(0, self.__calValidator.compareYears(value, cal_20050101))
        self.assertEqual(1, self.__calValidator.compareYears(value, cal_20041231))

    def testCompare_test11_decomposed(self) -> None:
        same_time = 124522
        test_date = 20050823
        diff_hour = self._createCalendar(self._GMT, test_date, 115922)
        diff_min = self._createCalendar(self._GMT, test_date, 124422)
        diff_sec = self._createCalendar(self._GMT, test_date, 124521)
        value = self._createCalendar(self._GMT, test_date, same_time)
        cal_20050824 = self._createCalendar(self._GMT, 20050824, same_time)
        cal_20050822 = self._createCalendar(self._GMT, 20050822, same_time)
        cal_20050830 = self._createCalendar(self._GMT, 20050830, same_time)
        cal_20050816 = self._createCalendar(self._GMT, 20050816, same_time)
        cal_20050901 = self._createCalendar(self._GMT, 20050901, same_time)
        cal_20050801 = self._createCalendar(self._GMT, 20050801, same_time)
        cal_20050731 = self._createCalendar(self._GMT, 20050731, same_time)
        cal_20051101 = self._createCalendar(self._GMT, 20051101, same_time)
        cal_20051001 = self._createCalendar(self._GMT, 20051001, same_time)
        cal_20050701 = self._createCalendar(self._GMT, 20050701, same_time)
        cal_20050630 = self._createCalendar(self._GMT, 20050630, same_time)
        cal_20060101 = self._createCalendar(self._GMT, 20060101, same_time)
        cal_20050101 = self._createCalendar(self._GMT, 20050101, same_time)
        cal_20041231 = self._createCalendar(self._GMT, 20041231, same_time)

        self.assertEqual(1, self.__calValidator.compare(value, diff_hour, "hour"))
        self.assertEqual(0, self.__calValidator.compare(value, diff_min, "hour"))
        self.assertEqual(1, self.__calValidator.compare(value, diff_min, "minute"))
        self.assertEqual(0, self.__calValidator.compare(value, diff_sec, "minute"))
        self.assertEqual(1, self.__calValidator.compare(value, diff_sec, "second"))
        self.assertEqual(-1, self.__calValidator.compareDates(value, cal_20050824))
        self.assertEqual(0, self.__calValidator.compareDates(value, diff_hour))
        self.assertEqual(
            0, self.__calValidator.compare(value, diff_hour, "day_of_year")
        )
        self.assertEqual(1, self.__calValidator.compareDates(value, cal_20050822))
        self.assertEqual(-1, self.__calValidator.compareWeeks(value, cal_20050830))
        self.assertEqual(0, self.__calValidator.compareWeeks(value, cal_20050824))
        self.assertEqual(0, self.__calValidator.compareWeeks(value, cal_20050822))
        self.assertEqual(
            0, self.__calValidator.compare(value, cal_20050822, "week_of_month")
        )
        self.assertEqual(0, self.__calValidator.compareWeeks(value, cal_20050822))
        self.assertEqual(1, self.__calValidator.compareWeeks(value, cal_20050816))
        self.assertEqual(-1, self.__calValidator.compareMonths(value, cal_20050901))
        self.assertEqual(0, self.__calValidator.compareMonths(value, cal_20050830))
        self.assertEqual(0, self.__calValidator.compareMonths(value, cal_20050801))
        self.assertEqual(0, self.__calValidator.compareMonths(value, cal_20050816))
        self.assertEqual(1, self.__calValidator.compareMonths(value, cal_20050731))
        self.assertEqual(-1, self.__calValidator.compareQuarters0(value, cal_20051101))
        self.assertEqual(-1, self.__calValidator.compareQuarters0(value, cal_20051001))
        self.assertEqual(0, self.__calValidator.compareQuarters0(value, cal_20050901))
        self.assertEqual(0, self.__calValidator.compareQuarters0(value, cal_20050701))
        self.assertEqual(0, self.__calValidator.compareQuarters0(value, cal_20050731))
        self.assertEqual(1, self.__calValidator.compareQuarters0(value, cal_20050630))
        self.assertEqual(
            -1, self.__calValidator.compareQuarters1(value, cal_20051101, 2)
        )
        self.assertEqual(
            0, self.__calValidator.compareQuarters1(value, cal_20051001, 2)
        )
        self.assertEqual(
            0, self.__calValidator.compareQuarters1(value, cal_20050901, 2)
        )
        self.assertEqual(
            1, self.__calValidator.compareQuarters1(value, cal_20050701, 2)
        )
        self.assertEqual(
            1, self.__calValidator.compareQuarters1(value, cal_20050731, 2)
        )
        self.assertEqual(
            1, self.__calValidator.compareQuarters1(value, cal_20050630, 2)
        )

    def testCompare_test10_decomposed(self) -> None:
        same_time = 124522
        test_date = 20050823
        diff_hour = self._createCalendar(self._GMT, test_date, 115922)
        diff_min = self._createCalendar(self._GMT, test_date, 124422)
        diff_sec = self._createCalendar(self._GMT, test_date, 124521)
        value = self._createCalendar(self._GMT, test_date, same_time)
        cal_20050824 = self._createCalendar(self._GMT, 20050824, same_time)
        cal_20050822 = self._createCalendar(self._GMT, 20050822, same_time)
        cal_20050830 = self._createCalendar(self._GMT, 20050830, same_time)
        cal_20050816 = self._createCalendar(self._GMT, 20050816, same_time)
        cal_20050901 = self._createCalendar(self._GMT, 20050901, same_time)
        cal_20050801 = self._createCalendar(self._GMT, 20050801, same_time)
        cal_20050731 = self._createCalendar(self._GMT, 20050731, same_time)
        cal_20051101 = self._createCalendar(self._GMT, 20051101, same_time)
        cal_20051001 = self._createCalendar(self._GMT, 20051001, same_time)
        cal_20050701 = self._createCalendar(self._GMT, 20050701, same_time)
        cal_20050630 = self._createCalendar(self._GMT, 20050630, same_time)

        self.assertEqual(
            1, self.__calValidator._compare(value, diff_hour, "hour"), "hour GT"
        )
        self.assertEqual(
            0, self.__calValidator._compare(value, diff_min, "hour"), "hour EQ"
        )
        self.assertEqual(
            1, self.__calValidator._compare(value, diff_min, "minute"), "mins GT"
        )
        self.assertEqual(
            0, self.__calValidator._compare(value, diff_sec, "minute"), "mins EQ"
        )
        self.assertEqual(
            1, self.__calValidator._compare(value, diff_sec, "second"), "secs GT"
        )
        self.assertEqual(
            -1, self.__calValidator.compareDates(value, cal_20050824), "date LT"
        )
        self.assertEqual(
            0, self.__calValidator.compareDates(value, diff_hour), "date EQ"
        )
        self.assertEqual(
            0, self.__calValidator._compare(value, diff_hour, "day_of_year"), "date(B)"
        )
        self.assertEqual(
            1, self.__calValidator.compareDates(value, cal_20050822), "date GT"
        )
        self.assertEqual(
            -1, self.__calValidator.compareWeeks(value, cal_20050830), "week LT"
        )
        self.assertEqual(
            0, self.__calValidator.compareWeeks(value, cal_20050824), "week =1"
        )
        self.assertEqual(
            0, self.__calValidator.compareWeeks(value, cal_20050822), "week =2"
        )
        self.assertEqual(
            0,
            self.__calValidator._compare(value, cal_20050822, "week_of_month"),
            "week =3",
        )
        self.assertEqual(
            0, self.__calValidator.compareWeeks(value, cal_20050822), "week =4"
        )
        self.assertEqual(
            1, self.__calValidator.compareWeeks(value, cal_20050816), "week GT"
        )
        self.assertEqual(
            -1, self.__calValidator.compareMonths(value, cal_20050901), "mnth LT"
        )
        self.assertEqual(
            0, self.__calValidator.compareMonths(value, cal_20050830), "mnth =1"
        )
        self.assertEqual(
            0, self.__calValidator.compareMonths(value, cal_20050801), "mnth =2"
        )
        self.assertEqual(
            0, self.__calValidator.compareMonths(value, cal_20050816), "mnth =3"
        )
        self.assertEqual(
            1, self.__calValidator.compareMonths(value, cal_20050731), "mnth GT"
        )
        self.assertEqual(
            -1, self.__calValidator.compareQuarters0(value, cal_20051101), "qtrA <1"
        )
        self.assertEqual(
            -1, self.__calValidator.compareQuarters0(value, cal_20051001), "qtrA <2"
        )
        self.assertEqual(
            0, self.__calValidator.compareQuarters0(value, cal_20050901), "qtrA =1"
        )
        self.assertEqual(
            0, self.__calValidator.compareQuarters0(value, cal_20050701), "qtrA =2"
        )
        self.assertEqual(
            0, self.__calValidator.compareQuarters0(value, cal_20050731), "qtrA =3"
        )
        self.assertEqual(
            1, self.__calValidator.compareQuarters0(value, cal_20050630), "qtrA GT"
        )

    def testCompare_test9_decomposed(self) -> None:
        same_time = 124522
        test_date = 20050823
        diff_hour = self._createCalendar(self._GMT, test_date, 115922)
        diff_min = self._createCalendar(self._GMT, test_date, 124422)
        diff_sec = self._createCalendar(self._GMT, test_date, 124521)
        value = self._createCalendar(self._GMT, test_date, same_time)
        cal_20050824 = self._createCalendar(self._GMT, 20050824, same_time)
        cal_20050822 = self._createCalendar(self._GMT, 20050822, same_time)
        cal_20050830 = self._createCalendar(self._GMT, 20050830, same_time)
        cal_20050816 = self._createCalendar(self._GMT, 20050816, same_time)
        cal_20050901 = self._createCalendar(self._GMT, 20050901, same_time)
        cal_20050801 = self._createCalendar(self._GMT, 20050801, same_time)
        cal_20050731 = self._createCalendar(self._GMT, 20050731, same_time)
        cal_20051101 = self._createCalendar(self._GMT, 20051101, same_time)
        cal_20051001 = self._createCalendar(self._GMT, 20051001, same_time)
        cal_20050701 = self._createCalendar(self._GMT, 20050701, same_time)
        cal_20050630 = self._createCalendar(self._GMT, 20050630, same_time)
        cal_20060101 = self._createCalendar(self._GMT, 20060101, same_time)
        cal_20050101 = self._createCalendar(self._GMT, 20050101, same_time)
        cal_20041231 = self._createCalendar(self._GMT, 20041231, same_time)

        self.assertEqual(
            1, self.__calValidator.compare(value, diff_hour, "hour"), "hour GT"
        )
        self.assertEqual(
            0, self.__calValidator.compare(value, diff_min, "hour"), "hour EQ"
        )
        self.assertEqual(
            1, self.__calValidator.compare(value, diff_min, "minute"), "mins GT"
        )
        self.assertEqual(
            0, self.__calValidator.compare(value, diff_sec, "minute"), "mins EQ"
        )
        self.assertEqual(
            1, self.__calValidator.compare(value, diff_sec, "second"), "secs GT"
        )
        self.assertEqual(
            -1, self.__calValidator.compareDates(value, cal_20050824), "date LT"
        )
        self.assertEqual(
            0, self.__calValidator.compareDates(value, diff_hour), "date EQ"
        )
        self.assertEqual(
            0, self.__calValidator.compare(value, diff_hour, "day_of_year"), "date(B)"
        )
        self.assertEqual(
            1, self.__calValidator.compareDates(value, cal_20050822), "date GT"
        )
        self.assertEqual(
            -1, self.__calValidator.compareWeeks(value, cal_20050830), "week LT"
        )
        self.assertEqual(
            0, self.__calValidator.compareWeeks(value, cal_20050824), "week =1"
        )
        self.assertEqual(
            0, self.__calValidator.compareWeeks(value, cal_20050822), "week =2"
        )
        self.assertEqual(
            0,
            self.__calValidator.compare(value, cal_20050822, "week_of_month"),
            "week =3",
        )
        self.assertEqual(
            0, self.__calValidator.compareWeeks(value, cal_20050822), "week =4"
        )
        self.assertEqual(
            1, self.__calValidator.compareWeeks(value, cal_20050816), "week GT"
        )
        self.assertEqual(
            -1, self.__calValidator.compareMonths(value, cal_20050901), "mnth LT"
        )
        self.assertEqual(
            0, self.__calValidator.compareMonths(value, cal_20050830), "mnth =1"
        )
        self.assertEqual(
            0, self.__calValidator.compareMonths(value, cal_20050801), "mnth =2"
        )
        self.assertEqual(
            0, self.__calValidator.compareMonths(value, cal_20050816), "mnth =3"
        )
        self.assertEqual(
            1, self.__calValidator.compareMonths(value, cal_20050731), "mnth GT"
        )

    def testCompare_test8_decomposed(self) -> None:
        same_time = 124522
        test_date = 20050823
        diff_hour = self._createCalendar(self._GMT, test_date, 115922)
        diff_min = self._createCalendar(self._GMT, test_date, 124422)
        diff_sec = self._createCalendar(self._GMT, test_date, 124521)
        value = self._createCalendar(self._GMT, test_date, same_time)
        cal_20050824 = self._createCalendar(self._GMT, 20050824, same_time)
        cal_20050822 = self._createCalendar(self._GMT, 20050822, same_time)
        cal_20050830 = self._createCalendar(self._GMT, 20050830, same_time)
        cal_20050816 = self._createCalendar(self._GMT, 20050816, same_time)
        cal_20050901 = self._createCalendar(self._GMT, 20050901, same_time)
        cal_20050801 = self._createCalendar(self._GMT, 20050801, same_time)
        cal_20050731 = self._createCalendar(self._GMT, 20050731, same_time)
        cal_20051101 = self._createCalendar(self._GMT, 20051101, same_time)
        cal_20051001 = self._createCalendar(self._GMT, 20051001, same_time)
        cal_20050701 = self._createCalendar(self._GMT, 20050701, same_time)
        cal_20050630 = self._createCalendar(self._GMT, 20050630, same_time)
        cal_20060101 = self._createCalendar(self._GMT, 20060101, same_time)
        cal_20050101 = self._createCalendar(self._GMT, 20050101, same_time)
        cal_20041231 = self._createCalendar(self._GMT, 20041231, same_time)

        self.assertEqual(
            1, self.__calValidator._compare(value, diff_hour, "hour"), "hour GT"
        )
        self.assertEqual(
            0, self.__calValidator._compare(value, diff_min, "hour"), "hour EQ"
        )
        self.assertEqual(
            1, self.__calValidator._compare(value, diff_min, "minute"), "mins GT"
        )
        self.assertEqual(
            0, self.__calValidator._compare(value, diff_sec, "minute"), "mins EQ"
        )
        self.assertEqual(
            1, self.__calValidator._compare(value, diff_sec, "second"), "secs GT"
        )
        self.assertEqual(
            -1, self.__calValidator.compareDates(value, cal_20050824), "date LT"
        )
        self.assertEqual(
            0, self.__calValidator.compareDates(value, diff_hour), "date EQ"
        )
        self.assertEqual(
            0, self.__calValidator._compare(value, diff_hour, "day_of_year"), "date(B)"
        )
        self.assertEqual(
            1, self.__calValidator.compareDates(value, cal_20050822), "date GT"
        )
        self.assertEqual(
            -1, self.__calValidator.compareWeeks(value, cal_20050830), "week LT"
        )
        self.assertEqual(
            0, self.__calValidator.compareWeeks(value, cal_20050824), "week =1"
        )
        self.assertEqual(
            0, self.__calValidator.compareWeeks(value, cal_20050822), "week =2"
        )
        self.assertEqual(
            0,
            self.__calValidator._compare(value, cal_20050822, "week_of_month"),
            "week =3",
        )
        self.assertEqual(
            0, self.__calValidator.compareWeeks(value, cal_20050822), "week =4"
        )
        self.assertEqual(
            1, self.__calValidator.compareWeeks(value, cal_20050816), "week GT"
        )

    def testCompare_test7_decomposed(self) -> None:
        same_time = 124522
        test_date = 20050823
        diff_hour = self._createCalendar(self._GMT, test_date, 115922)
        diff_min = self._createCalendar(self._GMT, test_date, 124422)
        diff_sec = self._createCalendar(self._GMT, test_date, 124521)
        value = self._createCalendar(self._GMT, test_date, same_time)
        cal_20050824 = self._createCalendar(self._GMT, 20050824, same_time)
        cal_20050822 = self._createCalendar(self._GMT, 20050822, same_time)
        cal_20050830 = self._createCalendar(self._GMT, 20050830, same_time)
        cal_20050816 = self._createCalendar(self._GMT, 20050816, same_time)
        cal_20050901 = self._createCalendar(self._GMT, 20050901, same_time)
        cal_20050801 = self._createCalendar(self._GMT, 20050801, same_time)
        cal_20050731 = self._createCalendar(self._GMT, 20050731, same_time)
        cal_20051101 = self._createCalendar(self._GMT, 20051101, same_time)
        cal_20051001 = self._createCalendar(self._GMT, 20051001, same_time)
        cal_20050701 = self._createCalendar(self._GMT, 20050701, same_time)
        cal_20050630 = self._createCalendar(self._GMT, 20050630, same_time)
        cal_20060101 = self._createCalendar(self._GMT, 20060101, same_time)
        cal_20050101 = self._createCalendar(self._GMT, 20050101, same_time)
        cal_20041231 = self._createCalendar(self._GMT, 20041231, same_time)

        self.assertEqual(
            1, self.__calValidator._compare(value, diff_hour, "hour"), "hour GT"
        )
        self.assertEqual(
            0, self.__calValidator._compare(value, diff_min, "hour"), "hour EQ"
        )
        self.assertEqual(
            1, self.__calValidator._compare(value, diff_min, "minute"), "mins GT"
        )
        self.assertEqual(
            0, self.__calValidator._compare(value, diff_sec, "minute"), "mins EQ"
        )
        self.assertEqual(
            1, self.__calValidator._compare(value, diff_sec, "second"), "secs GT"
        )
        self.assertEqual(
            -1, self.__calValidator.compareDates(value, cal_20050824), "date LT"
        )
        self.assertEqual(
            0, self.__calValidator.compareDates(value, diff_hour), "date EQ"
        )
        self.assertEqual(
            0, self.__calValidator._compare(value, diff_hour, "day_of_year"), "date(B)"
        )
        self.assertEqual(
            1, self.__calValidator.compareDates(value, cal_20050822), "date GT"
        )
        self.assertEqual(
            -1, self.__calValidator.compareWeeks(value, cal_20050830), "week LT"
        )
        self.assertEqual(
            0, self.__calValidator.compareWeeks(value, cal_20050824), "week =1"
        )
        self.assertEqual(
            0, self.__calValidator.compareWeeks(value, cal_20050822), "week =2"
        )
        self.assertEqual(
            0,
            self.__calValidator._compare(value, cal_20050822, "week_of_month"),
            "week =3",
        )

    def testCompare_test6_decomposed(self) -> None:
        same_time = 124522
        test_date = 20050823
        diff_hour = self._createCalendar(self._GMT, test_date, 115922)
        diff_min = self._createCalendar(self._GMT, test_date, 124422)
        diff_sec = self._createCalendar(self._GMT, test_date, 124521)
        value = self._createCalendar(self._GMT, test_date, same_time)
        cal_20050824 = self._createCalendar(self._GMT, 20050824, same_time)
        cal_20050822 = self._createCalendar(self._GMT, 20050822, same_time)
        cal_20050830 = self._createCalendar(self._GMT, 20050830, same_time)
        cal_20050816 = self._createCalendar(self._GMT, 20050816, same_time)
        cal_20050901 = self._createCalendar(self._GMT, 20050901, same_time)
        cal_20050801 = self._createCalendar(self._GMT, 20050801, same_time)
        cal_20050731 = self._createCalendar(self._GMT, 20050731, same_time)
        cal_20051101 = self._createCalendar(self._GMT, 20051101, same_time)
        cal_20051001 = self._createCalendar(self._GMT, 20051001, same_time)
        cal_20050701 = self._createCalendar(self._GMT, 20050701, same_time)
        cal_20050630 = self._createCalendar(self._GMT, 20050630, same_time)
        cal_20060101 = self._createCalendar(self._GMT, 20060101, same_time)
        cal_20050101 = self._createCalendar(self._GMT, 20050101, same_time)
        cal_20041231 = self._createCalendar(self._GMT, 20041231, same_time)

        self.assertEqual(
            1, self.__calValidator._compare(value, diff_hour, "hour"), "hour GT"
        )
        self.assertEqual(
            0, self.__calValidator._compare(value, diff_min, "hour"), "hour EQ"
        )
        self.assertEqual(
            1, self.__calValidator._compare(value, diff_min, "minute"), "mins GT"
        )
        self.assertEqual(
            0, self.__calValidator._compare(value, diff_sec, "minute"), "mins EQ"
        )
        self.assertEqual(
            1, self.__calValidator._compare(value, diff_sec, "second"), "secs GT"
        )
        self.assertEqual(
            -1, self.__calValidator.compareDates(value, cal_20050824), "date LT"
        )
        self.assertEqual(
            0, self.__calValidator.compareDates(value, diff_hour), "date EQ"
        )
        self.assertEqual(
            0, self.__calValidator._compare(value, diff_hour, "day_of_year"), "date(B)"
        )
        self.assertEqual(
            1, self.__calValidator.compareDates(value, cal_20050822), "date GT"
        )
        self.assertEqual(
            -1, self.__calValidator.compareWeeks(value, cal_20050830), "week LT"
        )
        self.assertEqual(
            0, self.__calValidator.compareWeeks(value, cal_20050824), "week =1"
        )
        self.assertEqual(
            0, self.__calValidator.compareWeeks(value, cal_20050822), "week =2"
        )

    def testCompare_test5_decomposed(self) -> None:
        same_time = 124522
        test_date = 20050823
        diff_hour = self._createCalendar(self._GMT, test_date, 115922)
        diff_min = self._createCalendar(self._GMT, test_date, 124422)
        diff_sec = self._createCalendar(self._GMT, test_date, 124521)
        value = self._createCalendar(self._GMT, test_date, same_time)
        cal_20050824 = self._createCalendar(self._GMT, 20050824, same_time)
        cal_20050822 = self._createCalendar(self._GMT, 20050822, same_time)
        cal_20050830 = self._createCalendar(self._GMT, 20050830, same_time)
        cal_20050816 = self._createCalendar(self._GMT, 20050816, same_time)
        cal_20050901 = self._createCalendar(self._GMT, 20050901, same_time)
        cal_20050801 = self._createCalendar(self._GMT, 20050801, same_time)
        cal_20050731 = self._createCalendar(self._GMT, 20050731, same_time)
        cal_20051101 = self._createCalendar(self._GMT, 20051101, same_time)
        cal_20051001 = self._createCalendar(self._GMT, 20051001, same_time)
        cal_20050701 = self._createCalendar(self._GMT, 20050701, same_time)
        cal_20050630 = self._createCalendar(self._GMT, 20050630, same_time)
        cal_20060101 = self._createCalendar(self._GMT, 20060101, same_time)
        cal_20050101 = self._createCalendar(self._GMT, 20050101, same_time)
        cal_20041231 = self._createCalendar(self._GMT, 20041231, same_time)

        self.assertEqual(
            1, self.__calValidator._compare(value, diff_hour, "hour"), "hour GT"
        )
        self.assertEqual(
            0, self.__calValidator._compare(value, diff_min, "hour"), "hour EQ"
        )
        self.assertEqual(
            1, self.__calValidator._compare(value, diff_min, "minute"), "mins GT"
        )
        self.assertEqual(
            0, self.__calValidator._compare(value, diff_sec, "minute"), "mins EQ"
        )
        self.assertEqual(
            1, self.__calValidator._compare(value, diff_sec, "second"), "secs GT"
        )
        self.assertEqual(
            -1, self.__calValidator.compareDates(value, cal_20050824), "date LT"
        )
        self.assertEqual(
            0, self.__calValidator.compareDates(value, diff_hour), "date EQ"
        )
        self.assertEqual(
            0, self.__calValidator._compare(value, diff_hour, "day_of_year"), "date(B)"
        )
        self.assertEqual(
            1, self.__calValidator.compareDates(value, cal_20050822), "date GT"
        )

    def testCompare_test4_decomposed(self) -> None:
        same_time = 124522
        test_date = 20050823
        diff_hour = self._createCalendar(self._GMT, test_date, 115922)
        diff_min = self._createCalendar(self._GMT, test_date, 124422)
        diff_sec = self._createCalendar(self._GMT, test_date, 124521)
        value = self._createCalendar(self._GMT, test_date, same_time)
        cal_20050824 = self._createCalendar(self._GMT, 20050824, same_time)
        cal_20050822 = self._createCalendar(self._GMT, 20050822, same_time)
        cal_20050830 = self._createCalendar(self._GMT, 20050830, same_time)
        cal_20050816 = self._createCalendar(self._GMT, 20050816, same_time)
        cal_20050901 = self._createCalendar(self._GMT, 20050901, same_time)
        cal_20050801 = self._createCalendar(self._GMT, 20050801, same_time)
        cal_20050731 = self._createCalendar(self._GMT, 20050731, same_time)
        cal_20051101 = self._createCalendar(self._GMT, 20051101, same_time)
        cal_20051001 = self._createCalendar(self._GMT, 20051001, same_time)
        cal_20050701 = self._createCalendar(self._GMT, 20050701, same_time)
        cal_20050630 = self._createCalendar(self._GMT, 20050630, same_time)
        cal_20060101 = self._createCalendar(self._GMT, 20060101, same_time)
        cal_20050101 = self._createCalendar(self._GMT, 20050101, same_time)
        cal_20041231 = self._createCalendar(self._GMT, 20041231, same_time)

        self.assertEqual(
            1, self.__calValidator._compare(value, diff_hour, "hour"), "hour GT"
        )
        self.assertEqual(
            0, self.__calValidator._compare(value, diff_min, "hour"), "hour EQ"
        )
        self.assertEqual(
            1, self.__calValidator._compare(value, diff_min, "minute"), "mins GT"
        )
        self.assertEqual(
            0, self.__calValidator._compare(value, diff_sec, "minute"), "mins EQ"
        )
        self.assertEqual(
            1, self.__calValidator._compare(value, diff_sec, "second"), "secs GT"
        )
        self.assertEqual(
            -1, self.__calValidator.compareDates(value, cal_20050824), "date LT"
        )
        self.assertEqual(
            0, self.__calValidator.compareDates(value, diff_hour), "date EQ"
        )
        self.assertEqual(
            0, self.__calValidator._compare(value, diff_hour, "day_of_year"), "date(B)"
        )

    def testCompare_test3_decomposed(self) -> None:
        same_time = 124522
        test_date = 20050823
        diff_hour = self._createCalendar(self._GMT, test_date, 115922)
        diff_min = self._createCalendar(self._GMT, test_date, 124422)
        diff_sec = self._createCalendar(self._GMT, test_date, 124521)
        value = self._createCalendar(self._GMT, test_date, same_time)
        cal_20050824 = self._createCalendar(self._GMT, 20050824, same_time)
        cal_20050822 = self._createCalendar(self._GMT, 20050822, same_time)
        cal_20050830 = self._createCalendar(self._GMT, 20050830, same_time)
        cal_20050816 = self._createCalendar(self._GMT, 20050816, same_time)
        cal_20050901 = self._createCalendar(self._GMT, 20050901, same_time)
        cal_20050801 = self._createCalendar(self._GMT, 20050801, same_time)
        cal_20050731 = self._createCalendar(self._GMT, 20050731, same_time)
        cal_20051101 = self._createCalendar(self._GMT, 20051101, same_time)
        cal_20051001 = self._createCalendar(self._GMT, 20051001, same_time)
        cal_20050701 = self._createCalendar(self._GMT, 20050701, same_time)
        cal_20050630 = self._createCalendar(self._GMT, 20050630, same_time)
        cal_20060101 = self._createCalendar(self._GMT, 20060101, same_time)
        cal_20050101 = self._createCalendar(self._GMT, 20050101, same_time)
        cal_20041231 = self._createCalendar(self._GMT, 20041231, same_time)

        self.assertEqual(
            1, self.__calValidator._compare(value, diff_hour, "hour"), "hour GT"
        )
        self.assertEqual(
            0, self.__calValidator._compare(value, diff_min, "hour"), "hour EQ"
        )
        self.assertEqual(
            1, self.__calValidator._compare(value, diff_min, "minute"), "mins GT"
        )
        self.assertEqual(
            0, self.__calValidator._compare(value, diff_sec, "minute"), "mins EQ"
        )
        self.assertEqual(
            1, self.__calValidator._compare(value, diff_sec, "second"), "secs GT"
        )
        self.assertEqual(
            -1, self.__calValidator.compareDates(value, cal_20050824), "date LT"
        )
        self.assertEqual(
            0, self.__calValidator.compareDates(value, diff_hour), "date EQ"
        )

    def testCompare_test2_decomposed(self) -> None:
        same_time = 124522
        test_date = 20050823
        diff_hour = self._createCalendar(self._GMT, test_date, 115922)
        diff_min = self._createCalendar(self._GMT, test_date, 124422)
        diff_sec = self._createCalendar(self._GMT, test_date, 124521)
        value = self._createCalendar(self._GMT, test_date, same_time)
        cal_20050824 = self._createCalendar(self._GMT, 20050824, same_time)
        cal_20050822 = self._createCalendar(self._GMT, 20050822, same_time)
        cal_20050830 = self._createCalendar(self._GMT, 20050830, same_time)
        cal_20050816 = self._createCalendar(self._GMT, 20050816, same_time)
        cal_20050901 = self._createCalendar(self._GMT, 20050901, same_time)
        cal_20050801 = self._createCalendar(self._GMT, 20050801, same_time)
        cal_20050731 = self._createCalendar(self._GMT, 20050731, same_time)
        cal_20051101 = self._createCalendar(self._GMT, 20051101, same_time)
        cal_20051001 = self._createCalendar(self._GMT, 20051001, same_time)
        cal_20050701 = self._createCalendar(self._GMT, 20050701, same_time)
        cal_20050630 = self._createCalendar(self._GMT, 20050630, same_time)
        cal_20060101 = self._createCalendar(self._GMT, 20060101, same_time)
        cal_20050101 = self._createCalendar(self._GMT, 20050101, same_time)
        cal_20041231 = self._createCalendar(self._GMT, 20041231, same_time)

        self.assertEqual(
            1, self.__calValidator._compare(value, diff_hour, "hour"), "hour GT"
        )
        self.assertEqual(
            0, self.__calValidator._compare(value, diff_min, "hour"), "hour EQ"
        )
        self.assertEqual(
            1, self.__calValidator._compare(value, diff_min, "minute"), "mins GT"
        )
        self.assertEqual(
            0, self.__calValidator._compare(value, diff_sec, "minute"), "mins EQ"
        )
        self.assertEqual(
            1, self.__calValidator._compare(value, diff_sec, "second"), "secs GT"
        )

    def testCompare_test1_decomposed(self) -> None:
        same_time = 124522
        test_date = 20050823
        diff_hour = self._createCalendar(self._GMT, test_date, 115922)
        diff_min = self._createCalendar(self._GMT, test_date, 124422)
        diff_sec = self._createCalendar(self._GMT, test_date, 124521)
        value = self._createCalendar(self._GMT, test_date, same_time)
        cal_20050824 = self._createCalendar(self._GMT, 20050824, same_time)
        cal_20050822 = self._createCalendar(self._GMT, 20050822, same_time)
        cal_20050830 = self._createCalendar(self._GMT, 20050830, same_time)
        cal_20050816 = self._createCalendar(self._GMT, 20050816, same_time)
        cal_20050901 = self._createCalendar(self._GMT, 20050901, same_time)
        cal_20050801 = self._createCalendar(self._GMT, 20050801, same_time)
        cal_20050731 = self._createCalendar(self._GMT, 20050731, same_time)
        cal_20051101 = self._createCalendar(self._GMT, 20051101, same_time)
        cal_20051001 = self._createCalendar(self._GMT, 20051001, same_time)
        cal_20050701 = self._createCalendar(self._GMT, 20050701, same_time)
        cal_20050630 = self._createCalendar(self._GMT, 20050630, same_time)
        cal_20060101 = self._createCalendar(self._GMT, 20060101, same_time)
        cal_20050101 = self._createCalendar(self._GMT, 20050101, same_time)
        cal_20041231 = self._createCalendar(self._GMT, 20041231, same_time)

    def testCompare_test0_decomposed(self) -> None:
        same_time = 124522
        test_date = 20050823
        diff_hour = self._createCalendar(self._GMT, test_date, 115922)

    def testCalendarValidatorMethods_test41_decomposed(self) -> None:
        import locale
        from datetime import datetime

        # Set default locale
        locale.setlocale(locale.LC_ALL, "en_US")

        # Initialize variables
        locale_value = "de_DE"
        pattern = "yyyy-MM-dd"
        pattern_val = "2005-12-31"
        german_val = "31 Dez 2005"
        german_pattern = "dd MMM yyyy"
        locale_val = "31.12.2005"
        default_val = "12/31/05"
        XXXX = "XXXX"
        expected = self._createCalendar(None, 20051231, 0).getTime()

        # Validate default
        validator = CalendarValidator.getInstance()
        self.assertEqual(
            expected, validator.validate0(default_val).getTime(), "validate(A) default"
        )

        # Validate locale
        self.assertEqual(
            expected,
            validator.validate4(locale_val, locale_value).getTime(),
            "validate(A) locale",
        )

        # Validate pattern
        self.assertEqual(
            expected,
            validator.validate2(pattern_val, pattern).getTime(),
            "validate(A) pattern",
        )

        # Validate both pattern and locale
        self.assertEqual(
            expected,
            validator.validate6(german_val, german_pattern, locale_value).getTime(),
            "validate(A) both",
        )

        # Check isValid for default
        self.assertTrue(validator.isValid0(default_val), "isValid(A) default")

        # Check isValid for locale
        self.assertTrue(
            validator.isValid2(locale_val, locale_value), "isValid(A) locale"
        )

        # Check isValid for pattern
        self.assertTrue(validator.isValid1(pattern_val, pattern), "isValid(A) pattern")

        # Check isValid for both pattern and locale
        self.assertTrue(
            validator.isValid3(german_val, german_pattern, locale_value),
            "isValid(A) both",
        )

        # Validate invalid default
        self.assertIsNone(validator.validate0(XXXX), "validate(B) default")

        # Validate invalid locale
        self.assertIsNone(validator.validate4(XXXX, locale_value), "validate(B) locale")

        # Validate invalid pattern
        self.assertIsNone(validator.validate2(XXXX, pattern), "validate(B) pattern")

        # Validate invalid both pattern and locale
        self.assertIsNone(
            validator.validate6("31 Dec 2005", german_pattern, locale_value),
            "validate(B) both",
        )

        # Check isValid for invalid default
        self.assertFalse(validator.isValid0(XXXX), "isValid(B) default")

        # Check isValid for invalid locale
        self.assertFalse(validator.isValid2(XXXX, locale_value), "isValid(B) locale")

        # Check isValid for invalid pattern
        self.assertFalse(validator.isValid1(XXXX, pattern), "isValid(B) pattern")

        # Check isValid for invalid both pattern and locale
        self.assertFalse(
            validator.isValid3("31 Dec 2005", german_pattern, locale_value),
            "isValid(B) both",
        )

        # Time zone tests
        zone = (
            self._EET
            if self._EET.utcoffset(None) == self._EST.utcoffset(None)
            else self._EST
        )
        expected_zone = self._createCalendar(zone, 20051231, 0).getTime()

        self.assertNotEqual(
            expected.getTime(), expected_zone.getTime(), "default/EET same"
        )

        # Validate with time zone
        self.assertEqual(
            expected_zone,
            validator.validate1(default_val, zone).getTime(),
            "validate(C) default",
        )

        # Validate locale with time zone
        self.assertEqual(
            expected_zone,
            validator.validate5(locale_val, locale_value, zone).getTime(),
            "validate(C) locale",
        )

        # Validate pattern with time zone
        self.assertEqual(
            expected_zone,
            validator.validate3(pattern_val, pattern, zone).getTime(),
            "validate(C) pattern",
        )

        # Validate both pattern and locale with time zone
        self.assertEqual(
            expected_zone,
            validator.validate7(
                german_val, german_pattern, locale_value, zone
            ).getTime(),
            "validate(C) both",
        )

    def testCalendarValidatorMethods_test40_decomposed(self) -> None:
        Locale.setDefault(Locale.US)
        locale = Locale.GERMAN
        pattern = "yyyy-MM-dd"
        pattern_val = "2005-12-31"
        german_val = "31 Dez 2005"
        german_pattern = "dd MMM yyyy"
        locale_val = "31.12.2005"
        default_val = "12/31/05"
        XXXX = "XXXX"
        expected = self._createCalendar(None, 20051231, 0).getTime()

        validator = CalendarValidator.getInstance()

        # Validate default
        self.assertEqual(
            expected, validator.validate0(default_val).getTime(), "validate(A) default"
        )

        # Validate locale
        self.assertEqual(
            expected,
            validator.validate4(locale_val, locale).getTime(),
            "validate(A) locale",
        )

        # Validate pattern
        self.assertEqual(
            expected,
            validator.validate2(pattern_val, pattern).getTime(),
            "validate(A) pattern",
        )

        # Validate both (pattern and locale)
        self.assertEqual(
            expected,
            validator.validate6(german_val, german_pattern, Locale.GERMAN).getTime(),
            "validate(A) both",
        )

        # isValid checks
        self.assertTrue(validator.isValid0(default_val), "isValid(A) default")
        self.assertTrue(validator.isValid2(locale_val, locale), "isValid(A) locale")
        self.assertTrue(validator.isValid1(pattern_val, pattern), "isValid(A) pattern")
        self.assertTrue(
            validator.isValid3(german_val, german_pattern, Locale.GERMAN),
            "isValid(A) both",
        )

        # Invalid cases
        self.assertIsNone(validator.validate0(XXXX), "validate(B) default")
        self.assertIsNone(validator.validate4(XXXX, locale), "validate(B) locale")
        self.assertIsNone(validator.validate2(XXXX, pattern), "validate(B) pattern")
        self.assertIsNone(
            validator.validate6("31 Dec 2005", german_pattern, Locale.GERMAN),
            "validate(B) both",
        )

        self.assertFalse(validator.isValid0(XXXX), "isValid(B) default")
        self.assertFalse(validator.isValid2(XXXX, locale), "isValid(B) locale")
        self.assertFalse(validator.isValid1(XXXX, pattern), "isValid(B) pattern")
        self.assertFalse(
            validator.isValid3("31 Dec 2005", german_pattern, Locale.GERMAN),
            "isValid(B) both",
        )

        # Time zone checks
        zone = (
            self._EET
            if TimeZone.getDefault().getRawOffset() == self._EET.getRawOffset()
            else self._EST
        )
        expected_zone = self._createCalendar(zone, 20051231, 0).getTime()

        self.assertNotEqual(
            expected.getTime(), expected_zone.getTime(), "default/EET same"
        )

        # Validate with time zone
        self.assertEqual(
            expected_zone,
            validator.validate1(default_val, zone).getTime(),
            "validate(C) default",
        )
        self.assertEqual(
            expected_zone,
            validator.validate5(locale_val, locale, zone).getTime(),
            "validate(C) locale",
        )
        self.assertEqual(
            expected_zone,
            validator.validate3(pattern_val, pattern, zone).getTime(),
            "validate(C) pattern",
        )

    def testCalendarValidatorMethods_test39_decomposed(self) -> None:
        Locale.setDefault(Locale.US)
        locale = Locale.GERMAN
        pattern = "yyyy-MM-dd"
        pattern_val = "2005-12-31"
        german_val = "31 Dez 2005"
        german_pattern = "dd MMM yyyy"
        locale_val = "31.12.2005"
        default_val = "12/31/05"
        XXXX = "XXXX"
        expected = self._createCalendar(None, 20051231, 0).getTime()

        # validate(A) default
        self.assertEqual(
            expected,
            CalendarValidator.getInstance().validate0(default_val).getTime(),
            "validate(A) default",
        )

        # validate(A) locale
        self.assertEqual(
            expected,
            CalendarValidator.getInstance().validate4(locale_val, locale).getTime(),
            "validate(A) locale",
        )

        # validate(A) pattern
        self.assertEqual(
            expected,
            CalendarValidator.getInstance().validate2(pattern_val, pattern).getTime(),
            "validate(A) pattern",
        )

        # validate(A) both
        self.assertEqual(
            expected,
            CalendarValidator.getInstance()
            .validate6(german_val, german_pattern, Locale.GERMAN)
            .getTime(),
            "validate(A) both",
        )

        # isValid(A) default
        self.assertTrue(
            CalendarValidator.getInstance().isValid0(default_val), "isValid(A) default"
        )

        # isValid(A) locale
        self.assertTrue(
            CalendarValidator.getInstance().isValid2(locale_val, locale),
            "isValid(A) locale",
        )

        # isValid(A) pattern
        self.assertTrue(
            CalendarValidator.getInstance().isValid1(pattern_val, pattern),
            "isValid(A) pattern",
        )

        # isValid(A) both
        self.assertTrue(
            CalendarValidator.getInstance().isValid3(
                german_val, german_pattern, Locale.GERMAN
            ),
            "isValid(A) both",
        )

        # validate(B) default
        self.assertIsNone(
            CalendarValidator.getInstance().validate0(XXXX), "validate(B) default"
        )

        # validate(B) locale
        self.assertIsNone(
            CalendarValidator.getInstance().validate4(XXXX, locale),
            "validate(B) locale",
        )

        # validate(B) pattern
        self.assertIsNone(
            CalendarValidator.getInstance().validate2(XXXX, pattern),
            "validate(B) pattern",
        )

        # validate(B) both
        self.assertIsNone(
            CalendarValidator.getInstance().validate6(
                "31 Dec 2005", german_pattern, Locale.GERMAN
            ),
            "validate(B) both",
        )

        # isValid(B) default
        self.assertFalse(
            CalendarValidator.getInstance().isValid0(XXXX), "isValid(B) default"
        )

        # isValid(B) locale
        self.assertFalse(
            CalendarValidator.getInstance().isValid2(XXXX, locale), "isValid(B) locale"
        )

        # isValid(B) pattern
        self.assertFalse(
            CalendarValidator.getInstance().isValid1(XXXX, pattern),
            "isValid(B) pattern",
        )

        # isValid(B) both
        self.assertFalse(
            CalendarValidator.getInstance().isValid3(
                "31 Dec 2005", german_pattern, Locale.GERMAN
            ),
            "isValid(B) both",
        )

        # TimeZone tests
        zone = (
            self._EET
            if TimeZone.getDefault().getRawOffset() == self._EET.getRawOffset()
            else self._EST
        )
        expected_zone = self._createCalendar(zone, 20051231, 0).getTime()

        self.assertNotEqual(
            expected.getTime(), expected_zone.getTime(), "default/EET same"
        )

        # validate(C) default
        self.assertEqual(
            expected_zone,
            CalendarValidator.getInstance().validate1(default_val, zone).getTime(),
            "validate(C) default",
        )

        # validate(C) locale
        self.assertEqual(
            expected_zone,
            CalendarValidator.getInstance()
            .validate5(locale_val, locale, zone)
            .getTime(),
            "validate(C) locale",
        )

        # validate(C) pattern
        self.assertEqual(
            expected_zone,
            CalendarValidator.getInstance()
            .validate3(pattern_val, pattern, zone)
            .getTime(),
            "validate(C) pattern",
        )

    def testCalendarValidatorMethods_test38_decomposed(self) -> None:
        Locale.setDefault(Locale.US)
        locale = Locale.GERMAN
        pattern = "yyyy-MM-dd"
        pattern_val = "2005-12-31"
        german_val = "31 Dez 2005"
        german_pattern = "dd MMM yyyy"
        locale_val = "31.12.2005"
        default_val = "12/31/05"
        XXXX = "XXXX"
        expected = self._createCalendar(None, 20051231, 0).getTime()

        # validate(A) default
        self.assertEqual(
            "validate(A) default",
            expected,
            CalendarValidator.getInstance().validate0(default_val).getTime(),
        )

        # validate(A) locale
        self.assertEqual(
            "validate(A) locale",
            expected,
            CalendarValidator.getInstance().validate4(locale_val, locale).getTime(),
        )

        # validate(A) pattern
        self.assertEqual(
            "validate(A) pattern",
            expected,
            CalendarValidator.getInstance().validate2(pattern_val, pattern).getTime(),
        )

        # validate(A) both
        self.assertEqual(
            "validate(A) both",
            expected,
            CalendarValidator.getInstance()
            .validate6(german_val, german_pattern, Locale.GERMAN)
            .getTime(),
        )

        # isValid(A) default
        self.assertTrue(
            "isValid(A) default", CalendarValidator.getInstance().isValid0(default_val)
        )

        # isValid(A) locale
        self.assertTrue(
            "isValid(A) locale",
            CalendarValidator.getInstance().isValid2(locale_val, locale),
        )

        # isValid(A) pattern
        self.assertTrue(
            "isValid(A) pattern",
            CalendarValidator.getInstance().isValid1(pattern_val, pattern),
        )

        # isValid(A) both
        self.assertTrue(
            "isValid(A) both",
            CalendarValidator.getInstance().isValid3(
                german_val, german_pattern, Locale.GERMAN
            ),
        )

        # validate(B) default
        self.assertIsNone(
            "validate(B) default", CalendarValidator.getInstance().validate0(XXXX)
        )

        # validate(B) locale
        self.assertIsNone(
            "validate(B) locale",
            CalendarValidator.getInstance().validate4(XXXX, locale),
        )

        # validate(B) pattern
        self.assertIsNone(
            "validate(B) pattern",
            CalendarValidator.getInstance().validate2(XXXX, pattern),
        )

        # validate(B) both
        self.assertIsNone(
            "validate(B) both",
            CalendarValidator.getInstance().validate6(
                "31 Dec 2005", german_pattern, Locale.GERMAN
            ),
        )

        # isValid(B) default
        self.assertFalse(
            "isValid(B) default", CalendarValidator.getInstance().isValid0(XXXX)
        )

        # isValid(B) locale
        self.assertFalse(
            "isValid(B) locale", CalendarValidator.getInstance().isValid2(XXXX, locale)
        )

        # isValid(B) pattern
        self.assertFalse(
            "isValid(B) pattern",
            CalendarValidator.getInstance().isValid1(XXXX, pattern),
        )

        # isValid(B) both
        self.assertFalse(
            "isValid(B) both",
            CalendarValidator.getInstance().isValid3(
                "31 Dec 2005", german_pattern, Locale.GERMAN
            ),
        )

        # TimeZone tests
        zone = (
            self._EET
            if TimeZone.getDefault().getRawOffset() == self._EET.getRawOffset()
            else self._EST
        )
        expected_zone = self._createCalendar(zone, 20051231, 0).getTime()

        self.assertFalse(
            "default/EET same", expected.getTime() == expected_zone.getTime()
        )

        # validate(C) default
        self.assertEqual(
            "validate(C) default",
            expected_zone,
            CalendarValidator.getInstance().validate1(default_val, zone).getTime(),
        )

        # validate(C) locale
        self.assertEqual(
            "validate(C) locale",
            expected_zone,
            CalendarValidator.getInstance()
            .validate5(locale_val, locale, zone)
            .getTime(),
        )

    def testCalendarValidatorMethods_test37_decomposed(self) -> None:
        import locale
        from datetime import datetime

        # Set default locale
        locale.setlocale(locale.LC_ALL, "en_US")

        # Initialize variables
        locale_german = "de_DE"
        pattern = "yyyy-MM-dd"
        pattern_val = "2005-12-31"
        german_val = "31 Dez 2005"
        german_pattern = "dd MMM yyyy"
        locale_val = "31.12.2005"
        default_val = "12/31/05"
        XXXX = "XXXX"
        expected = self._createCalendar(None, 20051231, 0).getTime()

        # CalendarValidator instance
        validator = CalendarValidator.getInstance()

        # Validate default
        self.assertEqual(
            expected, validator.validate0(default_val).getTime(), "validate(A) default"
        )

        # Validate locale
        self.assertEqual(
            expected,
            validator.validate4(locale_val, locale_german).getTime(),
            "validate(A) locale",
        )

        # Validate pattern
        self.assertEqual(
            expected,
            validator.validate2(pattern_val, pattern).getTime(),
            "validate(A) pattern",
        )

        # Validate both
        self.assertEqual(
            expected,
            validator.validate6(german_val, german_pattern, locale_german).getTime(),
            "validate(A) both",
        )

        # isValid checks
        self.assertTrue(validator.isValid0(default_val), "isValid(A) default")
        self.assertTrue(
            validator.isValid2(locale_val, locale_german), "isValid(A) locale"
        )
        self.assertTrue(validator.isValid1(pattern_val, pattern), "isValid(A) pattern")
        self.assertTrue(
            validator.isValid3(german_val, german_pattern, locale_german),
            "isValid(A) both",
        )

        # Validate invalid inputs
        self.assertIsNone(validator.validate0(XXXX), "validate(B) default")
        self.assertIsNone(
            validator.validate4(XXXX, locale_german), "validate(B) locale"
        )
        self.assertIsNone(validator.validate2(XXXX, pattern), "validate(B) pattern")
        self.assertIsNone(
            validator.validate6("31 Dec 2005", german_pattern, locale_german),
            "validate(B) both",
        )

        # isValid checks for invalid inputs
        self.assertFalse(validator.isValid0(XXXX), "isValid(B) default")
        self.assertFalse(validator.isValid2(XXXX, locale_german), "isValid(B) locale")
        self.assertFalse(validator.isValid1(XXXX, pattern), "isValid(B) pattern")
        self.assertFalse(
            validator.isValid3("31 Dec 2005", german_pattern, locale_german),
            "isValid(B) both",
        )

        # TimeZone checks
        zone = (
            self._EET
            if self._EET.utcoffset(None) == self._EST.utcoffset(None)
            else self._EST
        )
        expected_zone = self._createCalendar(zone, 20051231, 0).getTime()

        self.assertNotEqual(
            expected.getTime(), expected_zone.getTime(), "default/EET same"
        )

        # Validate with time zone
        self.assertEqual(
            expected_zone,
            validator.validate1(default_val, zone).getTime(),
            "validate(C) default",
        )
        self.assertEqual(
            expected_zone,
            validator.validate5(locale_val, locale_german, zone).getTime(),
            "validate(C) locale",
        )

    def testCalendarValidatorMethods_test36_decomposed(self) -> None:
        import locale
        from datetime import datetime

        # Set default locale
        locale.setlocale(locale.LC_ALL, "en_US")

        # Test data
        locale_value = "de_DE"
        pattern = "yyyy-MM-dd"
        pattern_val = "2005-12-31"
        german_val = "31 Dez 2005"
        german_pattern = "dd MMM yyyy"
        locale_val = "31.12.2005"
        default_val = "12/31/05"
        XXXX = "XXXX"
        expected = self._createCalendar(None, 20051231, 0).getTime()

        # CalendarValidator instance
        validator = CalendarValidator.getInstance()

        # validate0
        self.assertEqual(
            expected, validator.validate0(default_val).getTime(), "validate(A) default"
        )

        # validate4
        self.assertEqual(
            expected,
            validator.validate4(locale_val, locale_value).getTime(),
            "validate(A) locale",
        )

        # validate2
        self.assertEqual(
            expected,
            validator.validate2(pattern_val, pattern).getTime(),
            "validate(A) pattern",
        )

        # validate6
        self.assertEqual(
            expected,
            validator.validate6(german_val, german_pattern, locale_value).getTime(),
            "validate(A) both",
        )

        # isValid0
        self.assertTrue(validator.isValid0(default_val), "isValid(A) default")

        # isValid2
        self.assertTrue(
            validator.isValid2(locale_val, locale_value), "isValid(A) locale"
        )

        # isValid1
        self.assertTrue(validator.isValid1(pattern_val, pattern), "isValid(A) pattern")

        # isValid3
        self.assertTrue(
            validator.isValid3(german_val, german_pattern, locale_value),
            "isValid(A) both",
        )

        # validate0 with invalid input
        self.assertIsNone(validator.validate0(XXXX), "validate(B) default")

        # validate4 with invalid input
        self.assertIsNone(validator.validate4(XXXX, locale_value), "validate(B) locale")

        # validate2 with invalid input
        self.assertIsNone(validator.validate2(XXXX, pattern), "validate(B) pattern")

        # validate6 with invalid input
        self.assertIsNone(
            validator.validate6("31 Dec 2005", german_pattern, locale_value),
            "validate(B) both",
        )

        # isValid0 with invalid input
        self.assertFalse(validator.isValid0(XXXX), "isValid(B) default")

        # isValid2 with invalid input
        self.assertFalse(validator.isValid2(XXXX, locale_value), "isValid(B) locale")

        # isValid1 with invalid input
        self.assertFalse(validator.isValid1(XXXX, pattern), "isValid(B) pattern")

        # isValid3 with invalid input
        self.assertFalse(
            validator.isValid3("31 Dec 2005", german_pattern, locale_value),
            "isValid(B) both",
        )

        # TimeZone tests
        zone = (
            self._EET
            if self._EET.utcoffset(None) == self._EST.utcoffset(None)
            else self._EST
        )
        expected_zone = self._createCalendar(zone, 20051231, 0).getTime()

        self.assertNotEqual(
            expected.getTime(), expected_zone.getTime(), "default/EET same"
        )

        self.assertEqual(
            expected_zone,
            validator.validate1(default_val, zone).getTime(),
            "validate(C) default",
        )

    def testCalendarValidatorMethods_test35_decomposed(self) -> None:
        import locale
        from datetime import datetime

        # Set default locale
        locale.setlocale(locale.LC_ALL, "en_US")

        # Test data
        locale_value = "de_DE"
        pattern = "yyyy-MM-dd"
        pattern_val = "2005-12-31"
        german_val = "31 Dez 2005"
        german_pattern = "dd MMM yyyy"
        locale_val = "31.12.2005"
        default_val = "12/31/05"
        XXXX = "XXXX"
        expected = self._createCalendar(None, 20051231, 0).getTime()

        # CalendarValidator instance
        validator = CalendarValidator.getInstance()

        # validate0
        self.assertEqual(expected, validator.validate0(default_val).getTime())

        # validate4
        self.assertEqual(
            expected, validator.validate4(locale_val, locale_value).getTime()
        )

        # validate2
        self.assertEqual(expected, validator.validate2(pattern_val, pattern).getTime())

        # validate6
        self.assertEqual(
            expected,
            validator.validate6(german_val, german_pattern, locale_value).getTime(),
        )

        # isValid0
        self.assertTrue(validator.isValid0(default_val))

        # isValid2
        self.assertTrue(validator.isValid2(locale_val, locale_value))

        # isValid1
        self.assertTrue(validator.isValid1(pattern_val, pattern))

        # isValid3
        self.assertTrue(validator.isValid3(german_val, german_pattern, locale_value))

        # validate0 with invalid input
        self.assertIsNone(validator.validate0(XXXX))

        # validate4 with invalid input
        self.assertIsNone(validator.validate4(XXXX, locale_value))

        # validate2 with invalid input
        self.assertIsNone(validator.validate2(XXXX, pattern))

        # validate6 with invalid input
        self.assertIsNone(
            validator.validate6("31 Dec 2005", german_pattern, locale_value)
        )

        # isValid0 with invalid input
        self.assertFalse(validator.isValid0(XXXX))

        # isValid2 with invalid input
        self.assertFalse(validator.isValid2(XXXX, locale_value))

        # isValid1 with invalid input
        self.assertFalse(validator.isValid1(XXXX, pattern))

        # isValid3 with invalid input
        self.assertFalse(
            validator.isValid3("31 Dec 2005", german_pattern, locale_value)
        )

        # TimeZone tests
        zone = (
            self._EET
            if self._EET.utcoffset(None) == self._EST.utcoffset(None)
            else self._EST
        )
        expected_zone = self._createCalendar(zone, 20051231, 0).getTime()

        self.assertNotEqual(expected.getTime(), expected_zone.getTime())

        self.assertEqual(
            expected_zone, validator.validate1(default_val, zone).getTime()
        )

    def testCalendarValidatorMethods_test34_decomposed(self) -> None:
        import locale
        from datetime import datetime

        # Set default locale
        locale.setlocale(locale.LC_ALL, "en_US")

        # Initialize variables
        locale_german = "de_DE"
        pattern = "yyyy-MM-dd"
        pattern_val = "2005-12-31"
        german_val = "31 Dez 2005"
        german_pattern = "dd MMM yyyy"
        locale_val = "31.12.2005"
        default_val = "12/31/05"
        XXXX = "XXXX"
        expected = self._createCalendar(None, 20051231, 0).getTime()

        # CalendarValidator instance
        validator = CalendarValidator.getInstance()

        # Validate default
        self.assertEqual(
            expected, validator.validate0(default_val).getTime(), "validate(A) default"
        )

        # Validate locale
        self.assertEqual(
            expected,
            validator.validate4(locale_val, locale_german).getTime(),
            "validate(A) locale",
        )

        # Validate pattern
        self.assertEqual(
            expected,
            validator.validate2(pattern_val, pattern).getTime(),
            "validate(A) pattern",
        )

        # Validate both
        self.assertEqual(
            expected,
            validator.validate6(german_val, german_pattern, locale_german).getTime(),
            "validate(A) both",
        )

        # isValid checks
        self.assertTrue(validator.isValid0(default_val), "isValid(A) default")
        self.assertTrue(
            validator.isValid2(locale_val, locale_german), "isValid(A) locale"
        )
        self.assertTrue(validator.isValid1(pattern_val, pattern), "isValid(A) pattern")
        self.assertTrue(
            validator.isValid3(german_val, german_pattern, locale_german),
            "isValid(A) both",
        )

        # Validate invalid inputs
        self.assertIsNone(validator.validate0(XXXX), "validate(B) default")
        self.assertIsNone(
            validator.validate4(XXXX, locale_german), "validate(B) locale"
        )
        self.assertIsNone(validator.validate2(XXXX, pattern), "validate(B) pattern")
        self.assertIsNone(
            validator.validate6("31 Dec 2005", german_pattern, locale_german),
            "validate(B) both",
        )

        # isValid checks for invalid inputs
        self.assertFalse(validator.isValid0(XXXX), "isValid(B) default")
        self.assertFalse(validator.isValid2(XXXX, locale_german), "isValid(B) locale")
        self.assertFalse(validator.isValid1(XXXX, pattern), "isValid(B) pattern")
        self.assertFalse(
            validator.isValid3("31 Dec 2005", german_pattern, locale_german),
            "isValid(B) both",
        )

        # Time zone checks
        zone = (
            self._EET
            if self._EET.utcoffset(None) == self._EST.utcoffset(None)
            else self._EST
        )
        expected_zone = self._createCalendar(zone, 20051231, 0).getTime()
        self.assertNotEqual(
            expected.getTime(), expected_zone.getTime(), "default/EET same"
        )

    def testCalendarValidatorMethods_test33_decomposed(self) -> None:
        Locale.setDefault(Locale.US)
        locale = Locale.GERMAN
        pattern = "yyyy-MM-dd"
        pattern_val = "2005-12-31"
        german_val = "31 Dez 2005"
        german_pattern = "dd MMM yyyy"
        locale_val = "31.12.2005"
        default_val = "12/31/05"
        XXXX = "XXXX"
        expected = self._createCalendar(None, 20051231, 0).getTime()

        validator = CalendarValidator.getInstance()

        # validate(A) default
        self.assertEqual(
            expected, validator.validate0(default_val).getTime(), "validate(A) default"
        )

        # validate(A) locale
        self.assertEqual(
            expected,
            validator.validate4(locale_val, locale).getTime(),
            "validate(A) locale",
        )

        # validate(A) pattern
        self.assertEqual(
            expected,
            validator.validate2(pattern_val, pattern).getTime(),
            "validate(A) pattern",
        )

        # validate(A) both
        self.assertEqual(
            expected,
            validator.validate6(german_val, german_pattern, Locale.GERMAN).getTime(),
            "validate(A) both",
        )

        # isValid(A) default
        self.assertTrue(validator.isValid0(default_val), "isValid(A) default")

        # isValid(A) locale
        self.assertTrue(validator.isValid2(locale_val, locale), "isValid(A) locale")

        # isValid(A) pattern
        self.assertTrue(validator.isValid1(pattern_val, pattern), "isValid(A) pattern")

        # isValid(A) both
        self.assertTrue(
            validator.isValid3(german_val, german_pattern, Locale.GERMAN),
            "isValid(A) both",
        )

        # validate(B) default
        self.assertIsNone(validator.validate0(XXXX), "validate(B) default")

        # validate(B) locale
        self.assertIsNone(validator.validate4(XXXX, locale), "validate(B) locale")

        # validate(B) pattern
        self.assertIsNone(validator.validate2(XXXX, pattern), "validate(B) pattern")

        # validate(B) both
        self.assertIsNone(
            validator.validate6("31 Dec 2005", german_pattern, Locale.GERMAN),
            "validate(B) both",
        )

        # isValid(B) default
        self.assertFalse(validator.isValid0(XXXX), "isValid(B) default")

        # isValid(B) locale
        self.assertFalse(validator.isValid2(XXXX, locale), "isValid(B) locale")

        # isValid(B) pattern
        self.assertFalse(validator.isValid1(XXXX, pattern), "isValid(B) pattern")

        # isValid(B) both
        self.assertFalse(
            validator.isValid3("31 Dec 2005", german_pattern, Locale.GERMAN),
            "isValid(B) both",
        )

        # TimeZone handling
        zone = (
            self._EET
            if TimeZone.getDefault().getRawOffset() == self._EET.getRawOffset()
            else self._EST
        )
        expected_zone = self._createCalendar(zone, 20051231, 0).getTime()

    def testCalendarValidatorMethods_test32_decomposed(self) -> None:
        Locale.setDefault(Locale.US)
        locale = Locale.GERMAN
        pattern = "yyyy-MM-dd"
        pattern_val = "2005-12-31"
        german_val = "31 Dez 2005"
        german_pattern = "dd MMM yyyy"
        locale_val = "31.12.2005"
        default_val = "12/31/05"
        XXXX = "XXXX"
        expected = self._createCalendar(None, 20051231, 0).getTime()

        # Validate default
        self.assertEqual(
            expected,
            CalendarValidator.getInstance().validate0(default_val).getTime(),
            "validate(A) default",
        )

        # Validate locale
        self.assertEqual(
            expected,
            CalendarValidator.getInstance().validate4(locale_val, locale).getTime(),
            "validate(A) locale",
        )

        # Validate pattern
        self.assertEqual(
            expected,
            CalendarValidator.getInstance().validate2(pattern_val, pattern).getTime(),
            "validate(A) pattern",
        )

        # Validate both pattern and locale
        self.assertEqual(
            expected,
            CalendarValidator.getInstance()
            .validate6(german_val, german_pattern, Locale.GERMAN)
            .getTime(),
            "validate(A) both",
        )

        # Check isValid for default
        self.assertTrue(
            CalendarValidator.getInstance().isValid0(default_val), "isValid(A) default"
        )

        # Check isValid for locale
        self.assertTrue(
            CalendarValidator.getInstance().isValid2(locale_val, locale),
            "isValid(A) locale",
        )

        # Check isValid for pattern
        self.assertTrue(
            CalendarValidator.getInstance().isValid1(pattern_val, pattern),
            "isValid(A) pattern",
        )

        # Check isValid for both pattern and locale
        self.assertTrue(
            CalendarValidator.getInstance().isValid3(
                german_val, german_pattern, Locale.GERMAN
            ),
            "isValid(A) both",
        )

        # Validate invalid default
        self.assertIsNone(
            CalendarValidator.getInstance().validate0(XXXX), "validate(B) default"
        )

        # Validate invalid locale
        self.assertIsNone(
            CalendarValidator.getInstance().validate4(XXXX, locale),
            "validate(B) locale",
        )

        # Validate invalid pattern
        self.assertIsNone(
            CalendarValidator.getInstance().validate2(XXXX, pattern),
            "validate(B) pattern",
        )

        # Validate invalid both pattern and locale
        self.assertIsNone(
            CalendarValidator.getInstance().validate6(
                "31 Dec 2005", german_pattern, Locale.GERMAN
            ),
            "validate(B) both",
        )

        # Check isValid for invalid default
        self.assertFalse(
            CalendarValidator.getInstance().isValid0(XXXX), "isValid(B) default"
        )

        # Check isValid for invalid locale
        self.assertFalse(
            CalendarValidator.getInstance().isValid2(XXXX, locale), "isValid(B) locale"
        )

        # Check isValid for invalid pattern
        self.assertFalse(
            CalendarValidator.getInstance().isValid1(XXXX, pattern),
            "isValid(B) pattern",
        )

        # Check isValid for invalid both pattern and locale
        self.assertFalse(
            CalendarValidator.getInstance().isValid3(
                "31 Dec 2005", german_pattern, Locale.GERMAN
            ),
            "isValid(B) both",
        )

    def testCalendarValidatorMethods_test31_decomposed(self) -> None:
        # Set default locale
        Locale.setDefault(Locale.US)
        locale = Locale.GERMAN
        pattern = "yyyy-MM-dd"
        pattern_val = "2005-12-31"
        german_val = "31 Dez 2005"
        german_pattern = "dd MMM yyyy"
        locale_val = "31.12.2005"
        default_val = "12/31/05"
        XXXX = "XXXX"
        expected = self._createCalendar(None, 20051231, 0).getTime()

        # Validate default
        validator = CalendarValidator.getInstance()
        self.assertEqual(
            expected, validator.validate0(default_val).getTime(), "validate(A) default"
        )

        # Validate locale
        self.assertEqual(
            expected,
            validator.validate4(locale_val, locale).getTime(),
            "validate(A) locale",
        )

        # Validate pattern
        self.assertEqual(
            expected,
            validator.validate2(pattern_val, pattern).getTime(),
            "validate(A) pattern",
        )

        # Validate both pattern and locale
        self.assertEqual(
            expected,
            validator.validate6(german_val, german_pattern, Locale.GERMAN).getTime(),
            "validate(A) both",
        )

        # Check isValid for default
        self.assertTrue(validator.isValid0(default_val), "isValid(A) default")

        # Check isValid for locale
        self.assertTrue(validator.isValid2(locale_val, locale), "isValid(A) locale")

        # Check isValid for pattern
        self.assertTrue(validator.isValid1(pattern_val, pattern), "isValid(A) pattern")

        # Check isValid for both pattern and locale
        self.assertTrue(
            validator.isValid3(german_val, german_pattern, Locale.GERMAN),
            "isValid(A) both",
        )

        # Validate invalid default
        self.assertIsNone(validator.validate0(XXXX), "validate(B) default")

        # Validate invalid locale
        self.assertIsNone(validator.validate4(XXXX, locale), "validate(B) locale")

        # Validate invalid pattern
        self.assertIsNone(validator.validate2(XXXX, pattern), "validate(B) pattern")

        # Validate invalid both pattern and locale
        self.assertIsNone(
            validator.validate6("31 Dec 2005", german_pattern, Locale.GERMAN),
            "validate(B) both",
        )

        # Check isValid for invalid default
        self.assertFalse(validator.isValid0(XXXX), "isValid(B) default")

        # Check isValid for invalid locale
        self.assertFalse(validator.isValid2(XXXX, locale), "isValid(B) locale")

        # Check isValid for invalid pattern
        self.assertFalse(validator.isValid1(XXXX, pattern), "isValid(B) pattern")

    def testCalendarValidatorMethods_test30_decomposed(self) -> None:
        Locale.setDefault(Locale.US)
        locale = Locale.GERMAN
        pattern = "yyyy-MM-dd"
        pattern_val = "2005-12-31"
        german_val = "31 Dez 2005"
        german_pattern = "dd MMM yyyy"
        locale_val = "31.12.2005"
        default_val = "12/31/05"
        XXXX = "XXXX"
        expected = self._createCalendar(None, 20051231, 0).getTime()

        validator = CalendarValidator.getInstance()

        # validate(A) default
        self.assertEqual(
            expected, validator.validate0(default_val).getTime(), "validate(A) default"
        )

        # validate(A) locale
        self.assertEqual(
            expected,
            validator.validate4(locale_val, locale).getTime(),
            "validate(A) locale",
        )

        # validate(A) pattern
        self.assertEqual(
            expected,
            validator.validate2(pattern_val, pattern).getTime(),
            "validate(A) pattern",
        )

        # validate(A) both
        self.assertEqual(
            expected,
            validator.validate6(german_val, german_pattern, Locale.GERMAN).getTime(),
            "validate(A) both",
        )

        # isValid(A) default
        self.assertTrue(validator.isValid0(default_val), "isValid(A) default")

        # isValid(A) locale
        self.assertTrue(validator.isValid2(locale_val, locale), "isValid(A) locale")

        # isValid(A) pattern
        self.assertTrue(validator.isValid1(pattern_val, pattern), "isValid(A) pattern")

        # isValid(A) both
        self.assertTrue(
            validator.isValid3(german_val, german_pattern, Locale.GERMAN),
            "isValid(A) both",
        )

        # validate(B) default
        self.assertIsNone(validator.validate0(XXXX), "validate(B) default")

        # validate(B) locale
        self.assertIsNone(validator.validate4(XXXX, locale), "validate(B) locale")

        # validate(B) pattern
        self.assertIsNone(validator.validate2(XXXX, pattern), "validate(B) pattern")

        # validate(B) both
        self.assertIsNone(
            validator.validate6("31 Dec 2005", german_pattern, Locale.GERMAN),
            "validate(B) both",
        )

        # isValid(B) default
        self.assertFalse(validator.isValid0(XXXX), "isValid(B) default")

        # isValid(B) locale
        self.assertFalse(validator.isValid2(XXXX, locale), "isValid(B) locale")

        # isValid(B) pattern
        self.assertFalse(validator.isValid1(XXXX, pattern), "isValid(B) pattern")

    def testCalendarValidatorMethods_test29_decomposed(self) -> None:
        Locale.setDefault(Locale.US)
        locale = Locale.GERMAN
        pattern = "yyyy-MM-dd"
        pattern_val = "2005-12-31"
        german_val = "31 Dez 2005"
        german_pattern = "dd MMM yyyy"
        locale_val = "31.12.2005"
        default_val = "12/31/05"
        XXXX = "XXXX"
        expected = self._createCalendar(None, 20051231, 0).getTime()

        validator = CalendarValidator.getInstance()

        # validate(A) default
        self.assertEqual(
            expected, validator.validate0(default_val).getTime(), "validate(A) default"
        )

        # validate(A) locale
        self.assertEqual(
            expected,
            validator.validate4(locale_val, locale).getTime(),
            "validate(A) locale",
        )

        # validate(A) pattern
        self.assertEqual(
            expected,
            validator.validate2(pattern_val, pattern).getTime(),
            "validate(A) pattern",
        )

        # validate(A) both
        self.assertEqual(
            expected,
            validator.validate6(german_val, german_pattern, Locale.GERMAN).getTime(),
            "validate(A) both",
        )

        # isValid(A) default
        self.assertTrue(validator.isValid0(default_val), "isValid(A) default")

        # isValid(A) locale
        self.assertTrue(validator.isValid2(locale_val, locale), "isValid(A) locale")

        # isValid(A) pattern
        self.assertTrue(validator.isValid1(pattern_val, pattern), "isValid(A) pattern")

        # isValid(A) both
        self.assertTrue(
            validator.isValid3(german_val, german_pattern, Locale.GERMAN),
            "isValid(A) both",
        )

        # validate(B) default
        self.assertIsNone(validator.validate0(XXXX), "validate(B) default")

        # validate(B) locale
        self.assertIsNone(validator.validate4(XXXX, locale), "validate(B) locale")

        # validate(B) pattern
        self.assertIsNone(validator.validate2(XXXX, pattern), "validate(B) pattern")

        # validate(B) both
        self.assertIsNone(
            validator.validate6("31 Dec 2005", german_pattern, Locale.GERMAN),
            "validate(B) both",
        )

        # isValid(B) default
        self.assertFalse(validator.isValid0(XXXX), "isValid(B) default")

        # isValid(B) locale
        self.assertFalse(validator.isValid2(XXXX, locale), "isValid(B) locale")

    def testCalendarValidatorMethods_test28_decomposed(self) -> None:
        Locale.setDefault(Locale.US)
        locale = Locale.GERMAN
        pattern = "yyyy-MM-dd"
        pattern_val = "2005-12-31"
        german_val = "31 Dez 2005"
        german_pattern = "dd MMM yyyy"
        locale_val = "31.12.2005"
        default_val = "12/31/05"
        XXXX = "XXXX"
        expected = self._createCalendar(None, 20051231, 0).getTime()

        # Validate default
        self.assertEqual(
            expected,
            CalendarValidator.getInstance().validate0(default_val).getTime(),
            "validate(A) default",
        )

        # Validate locale
        self.assertEqual(
            expected,
            CalendarValidator.getInstance().validate4(locale_val, locale).getTime(),
            "validate(A) locale",
        )

        # Validate pattern
        self.assertEqual(
            expected,
            CalendarValidator.getInstance().validate2(pattern_val, pattern).getTime(),
            "validate(A) pattern",
        )

        # Validate both pattern and locale
        self.assertEqual(
            expected,
            CalendarValidator.getInstance()
            .validate6(german_val, german_pattern, Locale.GERMAN)
            .getTime(),
            "validate(A) both",
        )

        # isValid checks
        self.assertTrue(
            CalendarValidator.getInstance().isValid0(default_val), "isValid(A) default"
        )
        self.assertTrue(
            CalendarValidator.getInstance().isValid2(locale_val, locale),
            "isValid(A) locale",
        )
        self.assertTrue(
            CalendarValidator.getInstance().isValid1(pattern_val, pattern),
            "isValid(A) pattern",
        )
        self.assertTrue(
            CalendarValidator.getInstance().isValid3(
                german_val, german_pattern, Locale.GERMAN
            ),
            "isValid(A) both",
        )

        # Invalid validate checks
        self.assertIsNone(
            CalendarValidator.getInstance().validate0(XXXX), "validate(B) default"
        )
        self.assertIsNone(
            CalendarValidator.getInstance().validate4(XXXX, locale),
            "validate(B) locale",
        )
        self.assertIsNone(
            CalendarValidator.getInstance().validate2(XXXX, pattern),
            "validate(B) pattern",
        )
        self.assertIsNone(
            CalendarValidator.getInstance().validate6(
                "31 Dec 2005", german_pattern, Locale.GERMAN
            ),
            "validate(B) both",
        )

        # Invalid isValid checks
        self.assertFalse(
            CalendarValidator.getInstance().isValid0(XXXX), "isValid(B) default"
        )
        self.assertFalse(
            CalendarValidator.getInstance().isValid2(XXXX, locale), "isValid(B) locale"
        )

    def testCalendarValidatorMethods_test27_decomposed(self) -> None:
        Locale.setDefault(Locale.US)
        locale = Locale.GERMAN
        pattern = "yyyy-MM-dd"
        pattern_val = "2005-12-31"
        german_val = "31 Dez 2005"
        german_pattern = "dd MMM yyyy"
        locale_val = "31.12.2005"
        default_val = "12/31/05"
        XXXX = "XXXX"
        expected = self._createCalendar(None, 20051231, 0).getTime()

        validator = CalendarValidator.getInstance()

        # validate0 (default)
        self.assertEqual(
            expected, validator.validate0(default_val).getTime(), "validate(A) default"
        )

        # validate4 (locale)
        self.assertEqual(
            expected,
            validator.validate4(locale_val, locale).getTime(),
            "validate(A) locale",
        )

        # validate2 (pattern)
        self.assertEqual(
            expected,
            validator.validate2(pattern_val, pattern).getTime(),
            "validate(A) pattern",
        )

        # validate6 (both pattern and locale)
        self.assertEqual(
            expected,
            validator.validate6(german_val, german_pattern, Locale.GERMAN).getTime(),
            "validate(A) both",
        )

        # isValid0 (default)
        self.assertTrue(validator.isValid0(default_val), "isValid(A) default")

        # isValid2 (locale)
        self.assertTrue(validator.isValid2(locale_val, locale), "isValid(A) locale")

        # isValid1 (pattern)
        self.assertTrue(validator.isValid1(pattern_val, pattern), "isValid(A) pattern")

        # isValid3 (both pattern and locale)
        self.assertTrue(
            validator.isValid3(german_val, german_pattern, Locale.GERMAN),
            "isValid(A) both",
        )

        # validate0 (default) with invalid input
        self.assertIsNone(validator.validate0(XXXX), "validate(B) default")

        # validate4 (locale) with invalid input
        self.assertIsNone(validator.validate4(XXXX, locale), "validate(B) locale")

        # validate2 (pattern) with invalid input
        self.assertIsNone(validator.validate2(XXXX, pattern), "validate(B) pattern")

        # validate6 (both pattern and locale) with invalid input
        self.assertIsNone(
            validator.validate6("31 Dec 2005", german_pattern, Locale.GERMAN),
            "validate(B) both",
        )

        # isValid0 (default) with invalid input
        self.assertFalse(validator.isValid0(XXXX), "isValid(B) default")

    def testCalendarValidatorMethods_test26_decomposed(self) -> None:
        # Set default locale
        Locale.setDefault(Locale.US)
        locale = Locale.GERMAN
        pattern = "yyyy-MM-dd"
        pattern_val = "2005-12-31"
        german_val = "31 Dez 2005"
        german_pattern = "dd MMM yyyy"
        locale_val = "31.12.2005"
        default_val = "12/31/05"
        XXXX = "XXXX"
        expected = self._createCalendar(None, 20051231, 0).getTime()

        # Validate default
        CalendarValidator.getInstance()
        self.assertEqual(
            expected,
            CalendarValidator.getInstance().validate0(default_val).getTime(),
            "validate(A) default",
        )

        # Validate locale
        CalendarValidator.getInstance()
        self.assertEqual(
            expected,
            CalendarValidator.getInstance().validate4(locale_val, locale).getTime(),
            "validate(A) locale",
        )

        # Validate pattern
        CalendarValidator.getInstance()
        self.assertEqual(
            expected,
            CalendarValidator.getInstance().validate2(pattern_val, pattern).getTime(),
            "validate(A) pattern",
        )

        # Validate both pattern and locale
        CalendarValidator.getInstance()
        self.assertEqual(
            expected,
            CalendarValidator.getInstance()
            .validate6(german_val, german_pattern, Locale.GERMAN)
            .getTime(),
            "validate(A) both",
        )

        # Check isValid for default
        CalendarValidator.getInstance()
        self.assertTrue(
            CalendarValidator.getInstance().isValid0(default_val), "isValid(A) default"
        )

        # Check isValid for locale
        CalendarValidator.getInstance()
        self.assertTrue(
            CalendarValidator.getInstance().isValid2(locale_val, locale),
            "isValid(A) locale",
        )

        # Check isValid for pattern
        CalendarValidator.getInstance()
        self.assertTrue(
            CalendarValidator.getInstance().isValid1(pattern_val, pattern),
            "isValid(A) pattern",
        )

        # Check isValid for both pattern and locale
        CalendarValidator.getInstance()
        self.assertTrue(
            CalendarValidator.getInstance().isValid3(
                german_val, german_pattern, Locale.GERMAN
            ),
            "isValid(A) both",
        )

        # Validate invalid default
        CalendarValidator.getInstance()
        self.assertIsNone(
            CalendarValidator.getInstance().validate0(XXXX), "validate(B) default"
        )

        # Validate invalid locale
        CalendarValidator.getInstance()
        self.assertIsNone(
            CalendarValidator.getInstance().validate4(XXXX, locale),
            "validate(B) locale",
        )

        # Validate invalid pattern
        CalendarValidator.getInstance()
        self.assertIsNone(
            CalendarValidator.getInstance().validate2(XXXX, pattern),
            "validate(B) pattern",
        )

        # Validate invalid both pattern and locale
        CalendarValidator.getInstance()
        self.assertIsNone(
            CalendarValidator.getInstance().validate6(
                "31 Dec 2005", german_pattern, Locale.GERMAN
            ),
            "validate(B) both",
        )

        # Check isValid for invalid default
        CalendarValidator.getInstance()
        self.assertFalse(
            CalendarValidator.getInstance().isValid0(XXXX), "isValid(B) default"
        )

    def testCalendarValidatorMethods_test25_decomposed(self) -> None:
        Locale.setDefault(Locale.US)
        locale = Locale.GERMAN
        pattern = "yyyy-MM-dd"
        pattern_val = "2005-12-31"
        german_val = "31 Dez 2005"
        german_pattern = "dd MMM yyyy"
        locale_val = "31.12.2005"
        default_val = "12/31/05"
        XXXX = "XXXX"
        expected = self._createCalendar(None, 20051231, 0).getTime()

        # Validate default
        self.assertEqual(
            expected,
            CalendarValidator.getInstance().validate0(default_val).getTime(),
            "validate(A) default",
        )

        # Validate locale
        self.assertEqual(
            expected,
            CalendarValidator.getInstance().validate4(locale_val, locale).getTime(),
            "validate(A) locale",
        )

        # Validate pattern
        self.assertEqual(
            expected,
            CalendarValidator.getInstance().validate2(pattern_val, pattern).getTime(),
            "validate(A) pattern",
        )

        # Validate both pattern and locale
        self.assertEqual(
            expected,
            CalendarValidator.getInstance()
            .validate6(german_val, german_pattern, Locale.GERMAN)
            .getTime(),
            "validate(A) both",
        )

        # Check isValid for default
        self.assertTrue(
            CalendarValidator.getInstance().isValid0(default_val), "isValid(A) default"
        )

        # Check isValid for locale
        self.assertTrue(
            CalendarValidator.getInstance().isValid2(locale_val, locale),
            "isValid(A) locale",
        )

        # Check isValid for pattern
        self.assertTrue(
            CalendarValidator.getInstance().isValid1(pattern_val, pattern),
            "isValid(A) pattern",
        )

        # Check isValid for both pattern and locale
        self.assertTrue(
            CalendarValidator.getInstance().isValid3(
                german_val, german_pattern, Locale.GERMAN
            ),
            "isValid(A) both",
        )

        # Validate invalid default
        self.assertIsNone(
            CalendarValidator.getInstance().validate0(XXXX), "validate(B) default"
        )

        # Validate invalid locale
        self.assertIsNone(
            CalendarValidator.getInstance().validate4(XXXX, locale),
            "validate(B) locale",
        )

        # Validate invalid pattern
        self.assertIsNone(
            CalendarValidator.getInstance().validate2(XXXX, pattern),
            "validate(B) pattern",
        )

        # Validate invalid both pattern and locale
        self.assertIsNone(
            CalendarValidator.getInstance().validate6(
                "31 Dec 2005", german_pattern, Locale.GERMAN
            ),
            "validate(B) both",
        )

    def testCalendarValidatorMethods_test24_decomposed(self) -> None:
        Locale.setDefault(Locale.US)
        locale = Locale.GERMAN
        pattern = "yyyy-MM-dd"
        pattern_val = "2005-12-31"
        german_val = "31 Dez 2005"
        german_pattern = "dd MMM yyyy"
        locale_val = "31.12.2005"
        default_val = "12/31/05"
        XXXX = "XXXX"
        expected = self._createCalendar(None, 20051231, 0).getTime()

        validator = CalendarValidator.getInstance()

        # validate0 (default)
        self.assertEqual(
            expected, validator.validate0(default_val).getTime(), "validate(A) default"
        )

        # validate4 (locale)
        self.assertEqual(
            expected,
            validator.validate4(locale_val, locale).getTime(),
            "validate(A) locale",
        )

        # validate2 (pattern)
        self.assertEqual(
            expected,
            validator.validate2(pattern_val, pattern).getTime(),
            "validate(A) pattern",
        )

        # validate6 (both pattern and locale)
        self.assertEqual(
            expected,
            validator.validate6(german_val, german_pattern, Locale.GERMAN).getTime(),
            "validate(A) both",
        )

        # isValid0 (default)
        self.assertTrue(validator.isValid0(default_val), "isValid(A) default")

        # isValid2 (locale)
        self.assertTrue(validator.isValid2(locale_val, locale), "isValid(A) locale")

        # isValid1 (pattern)
        self.assertTrue(validator.isValid1(pattern_val, pattern), "isValid(A) pattern")

        # isValid3 (both pattern and locale)
        self.assertTrue(
            validator.isValid3(german_val, german_pattern, Locale.GERMAN),
            "isValid(A) both",
        )

        # validate0 (default) with invalid input
        self.assertIsNone(validator.validate0(XXXX), "validate(B) default")

        # validate4 (locale) with invalid input
        self.assertIsNone(validator.validate4(XXXX, locale), "validate(B) locale")

        # validate2 (pattern) with invalid input
        self.assertIsNone(validator.validate2(XXXX, pattern), "validate(B) pattern")

        # validate6 (both pattern and locale) with invalid input
        self.assertIsNone(
            validator.validate6("31 Dec 2005", german_pattern, Locale.GERMAN),
            "validate(B) both",
        )

    def testCalendarValidatorMethods_test23_decomposed(self) -> None:
        Locale.setDefault(Locale.US)
        locale = Locale.GERMAN
        pattern = "yyyy-MM-dd"
        pattern_val = "2005-12-31"
        german_val = "31 Dez 2005"
        german_pattern = "dd MMM yyyy"
        locale_val = "31.12.2005"
        default_val = "12/31/05"
        XXXX = "XXXX"
        expected = self._createCalendar(None, 20051231, 0).getTime()

        # Validate default
        CalendarValidator.getInstance()
        self.assertEqual(
            expected,
            CalendarValidator.getInstance().validate0(default_val).getTime(),
            "validate(A) default",
        )

        # Validate locale
        CalendarValidator.getInstance()
        self.assertEqual(
            expected,
            CalendarValidator.getInstance().validate4(locale_val, locale).getTime(),
            "validate(A) locale",
        )

        # Validate pattern
        CalendarValidator.getInstance()
        self.assertEqual(
            expected,
            CalendarValidator.getInstance().validate2(pattern_val, pattern).getTime(),
            "validate(A) pattern",
        )

        # Validate both pattern and locale
        CalendarValidator.getInstance()
        self.assertEqual(
            expected,
            CalendarValidator.getInstance()
            .validate6(german_val, german_pattern, Locale.GERMAN)
            .getTime(),
            "validate(A) both",
        )

        # Check isValid for default
        CalendarValidator.getInstance()
        self.assertTrue(
            CalendarValidator.getInstance().isValid0(default_val), "isValid(A) default"
        )

        # Check isValid for locale
        CalendarValidator.getInstance()
        self.assertTrue(
            CalendarValidator.getInstance().isValid2(locale_val, locale),
            "isValid(A) locale",
        )

        # Check isValid for pattern
        CalendarValidator.getInstance()
        self.assertTrue(
            CalendarValidator.getInstance().isValid1(pattern_val, pattern),
            "isValid(A) pattern",
        )

        # Check isValid for both pattern and locale
        CalendarValidator.getInstance()
        self.assertTrue(
            CalendarValidator.getInstance().isValid3(
                german_val, german_pattern, Locale.GERMAN
            ),
            "isValid(A) both",
        )

        # Validate invalid default
        CalendarValidator.getInstance()
        self.assertIsNone(
            CalendarValidator.getInstance().validate0(XXXX), "validate(B) default"
        )

        # Validate invalid locale
        CalendarValidator.getInstance()
        self.assertIsNone(
            CalendarValidator.getInstance().validate4(XXXX, locale),
            "validate(B) locale",
        )

        # Validate invalid pattern
        CalendarValidator.getInstance()
        self.assertIsNone(
            CalendarValidator.getInstance().validate2(XXXX, pattern),
            "validate(B) pattern",
        )

    def testCalendarValidatorMethods_test22_decomposed(self) -> None:
        # Set default locale
        Locale.setDefault(Locale.US)
        locale = Locale.GERMAN
        pattern = "yyyy-MM-dd"
        pattern_val = "2005-12-31"
        german_val = "31 Dez 2005"
        german_pattern = "dd MMM yyyy"
        locale_val = "31.12.2005"
        default_val = "12/31/05"
        XXXX = "XXXX"
        expected = self._createCalendar(None, 20051231, 0).getTime()

        # Validate default value
        validator = CalendarValidator.getInstance()
        self.assertEqual(
            expected, validator.validate0(default_val).getTime(), "validate(A) default"
        )

        # Validate locale value
        self.assertEqual(
            expected,
            validator.validate4(locale_val, locale).getTime(),
            "validate(A) locale",
        )

        # Validate pattern value
        self.assertEqual(
            expected,
            validator.validate2(pattern_val, pattern).getTime(),
            "validate(A) pattern",
        )

        # Validate both pattern and locale
        self.assertEqual(
            expected,
            validator.validate6(german_val, german_pattern, Locale.GERMAN).getTime(),
            "validate(A) both",
        )

        # Check isValid for default value
        self.assertTrue(validator.isValid0(default_val), "isValid(A) default")

        # Check isValid for locale value
        self.assertTrue(validator.isValid2(locale_val, locale), "isValid(A) locale")

        # Check isValid for pattern value
        self.assertTrue(validator.isValid1(pattern_val, pattern), "isValid(A) pattern")

        # Check isValid for both pattern and locale
        self.assertTrue(
            validator.isValid3(german_val, german_pattern, Locale.GERMAN),
            "isValid(A) both",
        )

        # Validate invalid default value
        self.assertIsNone(validator.validate0(XXXX), "validate(B) default")

        # Validate invalid locale value
        self.assertIsNone(validator.validate4(XXXX, locale), "validate(B) locale")

        # Validate invalid pattern value
        self.assertIsNone(validator.validate2(XXXX, pattern), "validate(B) pattern")

    def testCalendarValidatorMethods_test21_decomposed(self) -> None:
        # Set default locale
        Locale.setDefault(Locale.US)
        locale = Locale.GERMAN
        pattern = "yyyy-MM-dd"
        pattern_val = "2005-12-31"
        german_val = "31 Dez 2005"
        german_pattern = "dd MMM yyyy"
        locale_val = "31.12.2005"
        default_val = "12/31/05"
        XXXX = "XXXX"
        expected = self._createCalendar(None, 20051231, 0).getTime()

        # Validate default value
        CalendarValidator.getInstance()
        self.assertEqual(
            expected,
            CalendarValidator.getInstance().validate0(default_val).getTime(),
            "validate(A) default",
        )

        # Validate locale value
        CalendarValidator.getInstance()
        self.assertEqual(
            expected,
            CalendarValidator.getInstance().validate4(locale_val, locale).getTime(),
            "validate(A) locale",
        )

        # Validate pattern value
        CalendarValidator.getInstance()
        self.assertEqual(
            expected,
            CalendarValidator.getInstance().validate2(pattern_val, pattern).getTime(),
            "validate(A) pattern",
        )

        # Validate both German value and pattern
        CalendarValidator.getInstance()
        self.assertEqual(
            expected,
            CalendarValidator.getInstance()
            .validate6(german_val, german_pattern, Locale.GERMAN)
            .getTime(),
            "validate(A) both",
        )

        # Check isValid for default value
        CalendarValidator.getInstance()
        self.assertTrue(
            CalendarValidator.getInstance().isValid0(default_val), "isValid(A) default"
        )

        # Check isValid for locale value
        CalendarValidator.getInstance()
        self.assertTrue(
            CalendarValidator.getInstance().isValid2(locale_val, locale),
            "isValid(A) locale",
        )

        # Check isValid for pattern value
        CalendarValidator.getInstance()
        self.assertTrue(
            CalendarValidator.getInstance().isValid1(pattern_val, pattern),
            "isValid(A) pattern",
        )

        # Check isValid for both German value and pattern
        CalendarValidator.getInstance()
        self.assertTrue(
            CalendarValidator.getInstance().isValid3(
                german_val, german_pattern, Locale.GERMAN
            ),
            "isValid(A) both",
        )

        # Validate invalid default value
        CalendarValidator.getInstance()
        self.assertIsNone(
            CalendarValidator.getInstance().validate0(XXXX), "validate(B) default"
        )

        # Validate invalid locale value
        CalendarValidator.getInstance()
        self.assertIsNone(
            CalendarValidator.getInstance().validate4(XXXX, locale),
            "validate(B) locale",
        )

    def testCalendarValidatorMethods_test20_decomposed(self) -> None:
        import locale

        locale.setlocale(locale.LC_ALL, "en_US")

        locale_val = "de_DE"
        pattern = "yyyy-MM-dd"
        pattern_val = "2005-12-31"
        german_val = "31 Dez 2005"
        german_pattern = "dd MMM yyyy"
        locale_val_str = "31.12.2005"
        default_val = "12/31/05"
        invalid_val = "XXXX"

        expected = self._createCalendar(None, 20051231, 0).getTime()

        validator = CalendarValidator.getInstance()

        # Validate default
        self.assertEqual(
            expected, validator.validate0(default_val).getTime(), "validate(A) default"
        )

        # Validate locale
        self.assertEqual(
            expected,
            validator.validate4(locale_val_str, locale_val).getTime(),
            "validate(A) locale",
        )

        # Validate pattern
        self.assertEqual(
            expected,
            validator.validate2(pattern_val, pattern).getTime(),
            "validate(A) pattern",
        )

        # Validate both pattern and locale
        self.assertEqual(
            expected,
            validator.validate6(german_val, german_pattern, locale_val).getTime(),
            "validate(A) both",
        )

        # isValid checks
        self.assertTrue(validator.isValid0(default_val), "isValid(A) default")
        self.assertTrue(
            validator.isValid2(locale_val_str, locale_val), "isValid(A) locale"
        )
        self.assertTrue(validator.isValid1(pattern_val, pattern), "isValid(A) pattern")
        self.assertTrue(
            validator.isValid3(german_val, german_pattern, locale_val),
            "isValid(A) both",
        )

        # Invalid value checks
        self.assertIsNone(validator.validate0(invalid_val), "validate(B) default")
        self.assertIsNone(
            validator.validate4(invalid_val, locale_val), "validate(B) locale"
        )

    def testCalendarValidatorMethods_test19_decomposed(self) -> None:
        Locale.setDefault(Locale.US)
        locale = Locale.GERMAN
        pattern = "yyyy-MM-dd"
        pattern_val = "2005-12-31"
        german_val = "31 Dez 2005"
        german_pattern = "dd MMM yyyy"
        locale_val = "31.12.2005"
        default_val = "12/31/05"
        XXXX = "XXXX"
        expected = self._createCalendar(None, 20051231, 0).getTime()

        # Validate default
        CalendarValidator.getInstance()
        self.assertEqual(
            expected,
            CalendarValidator.getInstance().validate0(default_val).getTime(),
            "validate(A) default",
        )

        # Validate locale
        CalendarValidator.getInstance()
        self.assertEqual(
            expected,
            CalendarValidator.getInstance().validate4(locale_val, locale).getTime(),
            "validate(A) locale",
        )

        # Validate pattern
        CalendarValidator.getInstance()
        self.assertEqual(
            expected,
            CalendarValidator.getInstance().validate2(pattern_val, pattern).getTime(),
            "validate(A) pattern",
        )

        # Validate both pattern and locale
        CalendarValidator.getInstance()
        self.assertEqual(
            expected,
            CalendarValidator.getInstance()
            .validate6(german_val, german_pattern, Locale.GERMAN)
            .getTime(),
            "validate(A) both",
        )

        # Check isValid for default
        CalendarValidator.getInstance()
        self.assertTrue(
            CalendarValidator.getInstance().isValid0(default_val), "isValid(A) default"
        )

        # Check isValid for locale
        CalendarValidator.getInstance()
        self.assertTrue(
            CalendarValidator.getInstance().isValid2(locale_val, locale),
            "isValid(A) locale",
        )

        # Check isValid for pattern
        CalendarValidator.getInstance()
        self.assertTrue(
            CalendarValidator.getInstance().isValid1(pattern_val, pattern),
            "isValid(A) pattern",
        )

        # Check isValid for both pattern and locale
        CalendarValidator.getInstance()
        self.assertTrue(
            CalendarValidator.getInstance().isValid3(
                german_val, german_pattern, Locale.GERMAN
            ),
            "isValid(A) both",
        )

        # Validate invalid input
        CalendarValidator.getInstance()
        self.assertIsNone(
            CalendarValidator.getInstance().validate0(XXXX), "validate(B) default"
        )

    def testCalendarValidatorMethods_test18_decomposed(self) -> None:
        # Set default locale
        Locale.setDefault(Locale.US)
        locale = Locale.GERMAN
        pattern = "yyyy-MM-dd"
        pattern_val = "2005-12-31"
        german_val = "31 Dez 2005"
        german_pattern = "dd MMM yyyy"
        locale_val = "31.12.2005"
        default_val = "12/31/05"
        XXXX = "XXXX"
        expected = self._createCalendar(None, 20051231, 0).getTime()

        # Validate default value
        validator = CalendarValidator.getInstance()
        self.assertEqual(
            expected, validator.validate0(default_val).getTime(), "validate(A) default"
        )

        # Validate locale-specific value
        self.assertEqual(
            expected,
            validator.validate4(locale_val, locale).getTime(),
            "validate(A) locale",
        )

        # Validate pattern-specific value
        self.assertEqual(
            expected,
            validator.validate2(pattern_val, pattern).getTime(),
            "validate(A) pattern",
        )

        # Validate both pattern and locale
        self.assertEqual(
            expected,
            validator.validate6(german_val, german_pattern, Locale.GERMAN).getTime(),
            "validate(A) both",
        )

        # Check isValid for default value
        self.assertTrue(validator.isValid0(default_val), "isValid(A) default")

        # Check isValid for locale-specific value
        self.assertTrue(validator.isValid2(locale_val, locale), "isValid(A) locale")

        # Check isValid for pattern-specific value
        self.assertTrue(validator.isValid1(pattern_val, pattern), "isValid(A) pattern")

        # Check isValid for both pattern and locale
        self.assertTrue(
            validator.isValid3(german_val, german_pattern, Locale.GERMAN),
            "isValid(A) both",
        )

        # Validate invalid value
        self.assertIsNone(validator.validate0(XXXX), "validate(B) default")

    def testCalendarValidatorMethods_test17_decomposed(self) -> None:
        Locale.setDefault(Locale.US)
        locale = Locale.GERMAN
        pattern = "yyyy-MM-dd"
        pattern_val = "2005-12-31"
        german_val = "31 Dez 2005"
        german_pattern = "dd MMM yyyy"
        locale_val = "31.12.2005"
        default_val = "12/31/05"
        XXXX = "XXXX"
        expected = self._createCalendar(None, 20051231, 0).getTime()

        # Validate default
        CalendarValidator.getInstance()
        self.assertEqual(
            expected,
            CalendarValidator.getInstance().validate0(default_val).getTime(),
            "validate(A) default",
        )

        # Validate locale
        CalendarValidator.getInstance()
        self.assertEqual(
            expected,
            CalendarValidator.getInstance().validate4(locale_val, locale).getTime(),
            "validate(A) locale",
        )

        # Validate pattern
        CalendarValidator.getInstance()
        self.assertEqual(
            expected,
            CalendarValidator.getInstance().validate2(pattern_val, pattern).getTime(),
            "validate(A) pattern",
        )

        # Validate both pattern and locale
        CalendarValidator.getInstance()
        self.assertEqual(
            expected,
            CalendarValidator.getInstance()
            .validate6(german_val, german_pattern, Locale.GERMAN)
            .getTime(),
            "validate(A) both",
        )

        # Check isValid for default
        CalendarValidator.getInstance()
        self.assertTrue(
            CalendarValidator.getInstance().isValid0(default_val), "isValid(A) default"
        )

        # Check isValid for locale
        CalendarValidator.getInstance()
        self.assertTrue(
            CalendarValidator.getInstance().isValid2(locale_val, locale),
            "isValid(A) locale",
        )

        # Check isValid for pattern
        CalendarValidator.getInstance()
        self.assertTrue(
            CalendarValidator.getInstance().isValid1(pattern_val, pattern),
            "isValid(A) pattern",
        )

        # Check isValid for both pattern and locale
        CalendarValidator.getInstance()
        self.assertTrue(
            CalendarValidator.getInstance().isValid3(
                german_val, german_pattern, Locale.GERMAN
            ),
            "isValid(A) both",
        )

    def testCalendarValidatorMethods_test16_decomposed(self) -> None:
        Locale.setDefault(Locale.US)
        locale = Locale.GERMAN
        pattern = "yyyy-MM-dd"
        patternVal = "2005-12-31"
        germanVal = "31 Dez 2005"
        germanPattern = "dd MMM yyyy"
        localeVal = "31.12.2005"
        defaultVal = "12/31/05"
        XXXX = "XXXX"
        expected = self._createCalendar(None, 20051231, 0).getTime()

        validator = CalendarValidator.getInstance()

        self.assertEqual(
            expected, validator.validate0(defaultVal).getTime(), "validate(A) default"
        )

        self.assertEqual(
            expected,
            validator.validate4(localeVal, locale).getTime(),
            "validate(A) locale",
        )

        self.assertEqual(
            expected,
            validator.validate2(patternVal, pattern).getTime(),
            "validate(A) pattern",
        )

        self.assertEqual(
            expected,
            validator.validate6(germanVal, germanPattern, Locale.GERMAN).getTime(),
            "validate(A) both",
        )

        self.assertTrue(validator.isValid0(defaultVal), "isValid(A) default")

        self.assertTrue(validator.isValid2(localeVal, locale), "isValid(A) locale")

        self.assertTrue(validator.isValid1(patternVal, pattern), "isValid(A) pattern")

        self.assertTrue(
            validator.isValid3(germanVal, germanPattern, Locale.GERMAN),
            "isValid(A) both",
        )

    def testCalendarValidatorMethods_test15_decomposed(self) -> None:
        # Set the default locale to US
        Locale.setDefault(Locale.US)

        # Define variables
        locale = Locale.GERMAN
        pattern = "yyyy-MM-dd"
        pattern_val = "2005-12-31"
        german_val = "31 Dez 2005"
        german_pattern = "dd MMM yyyy"
        locale_val = "31.12.2005"
        default_val = "12/31/05"
        XXXX = "XXXX"

        # Create the expected date
        expected = self._createCalendar(None, 20051231, 0).getTime()

        # Validate using default format
        CalendarValidator.getInstance()
        CalendarValidator.getInstance().validate0(default_val)
        self.assertEqual(
            expected,
            CalendarValidator.getInstance().validate0(default_val).getTime(),
            "validate(A) default",
        )

        # Validate using locale
        CalendarValidator.getInstance()
        CalendarValidator.getInstance().validate4(locale_val, locale)
        self.assertEqual(
            expected,
            CalendarValidator.getInstance().validate4(locale_val, locale).getTime(),
            "validate(A) locale",
        )

        # Validate using pattern
        CalendarValidator.getInstance()
        CalendarValidator.getInstance().validate2(pattern_val, pattern)
        self.assertEqual(
            expected,
            CalendarValidator.getInstance().validate2(pattern_val, pattern).getTime(),
            "validate(A) pattern",
        )

        # Validate using both pattern and locale
        CalendarValidator.getInstance()
        CalendarValidator.getInstance().validate6(
            german_val, german_pattern, Locale.GERMAN
        )
        self.assertEqual(
            expected,
            CalendarValidator.getInstance()
            .validate6(german_val, german_pattern, Locale.GERMAN)
            .getTime(),
            "validate(A) both",
        )

        # Check validity using default format
        CalendarValidator.getInstance()
        self.assertTrue(
            CalendarValidator.getInstance().isValid0(default_val), "isValid(A) default"
        )

        # Check validity using locale
        CalendarValidator.getInstance()
        self.assertTrue(
            CalendarValidator.getInstance().isValid2(locale_val, locale),
            "isValid(A) locale",
        )

        # Check validity using pattern
        CalendarValidator.getInstance()
        self.assertTrue(
            CalendarValidator.getInstance().isValid1(pattern_val, pattern),
            "isValid(A) pattern",
        )

    def testCalendarValidatorMethods_test14_decomposed(self) -> None:
        Locale.setDefault(Locale.US)
        locale = Locale.GERMAN
        pattern = "yyyy-MM-dd"
        pattern_val = "2005-12-31"
        german_val = "31 Dez 2005"
        german_pattern = "dd MMM yyyy"
        locale_val = "31.12.2005"
        default_val = "12/31/05"
        XXXX = "XXXX"
        expected = self._createCalendar(None, 20051231, 0).getTime()

        validator = CalendarValidator.getInstance()

        # Validate default
        self.assertEqual(
            expected, validator.validate0(default_val).getTime(), "validate(A) default"
        )

        # Validate locale
        self.assertEqual(
            expected,
            validator.validate4(locale_val, locale).getTime(),
            "validate(A) locale",
        )

        # Validate pattern
        self.assertEqual(
            expected,
            validator.validate2(pattern_val, pattern).getTime(),
            "validate(A) pattern",
        )

        # Validate both pattern and locale
        self.assertEqual(
            expected,
            validator.validate6(german_val, german_pattern, Locale.GERMAN).getTime(),
            "validate(A) both",
        )

        # Check isValid for default
        self.assertTrue(validator.isValid0(default_val), "isValid(A) default")

        # Check isValid for locale
        self.assertTrue(validator.isValid2(locale_val, locale), "isValid(A) locale")

        # Check isValid for pattern
        self.assertTrue(validator.isValid1(pattern_val, pattern), "isValid(A) pattern")

    def testCalendarValidatorMethods_test13_decomposed(self) -> None:
        # Set the default locale to US
        Locale.setDefault(Locale.US)

        # Define variables
        locale = Locale.GERMAN
        pattern = "yyyy-MM-dd"
        pattern_val = "2005-12-31"
        german_val = "31 Dez 2005"
        german_pattern = "dd MMM yyyy"
        locale_val = "31.12.2005"
        default_val = "12/31/05"
        XXXX = "XXXX"

        # Create the expected date
        expected = self._createCalendar(None, 20051231, 0).getTime()

        # Validate using default format
        CalendarValidator.getInstance()
        CalendarValidator.getInstance().validate0(default_val)
        self.assertEqual(
            expected,
            CalendarValidator.getInstance().validate0(default_val).getTime(),
            "validate(A) default",
        )

        # Validate using locale
        CalendarValidator.getInstance()
        CalendarValidator.getInstance().validate4(locale_val, locale)
        self.assertEqual(
            expected,
            CalendarValidator.getInstance().validate4(locale_val, locale).getTime(),
            "validate(A) locale",
        )

        # Validate using pattern
        CalendarValidator.getInstance()
        CalendarValidator.getInstance().validate2(pattern_val, pattern)
        self.assertEqual(
            expected,
            CalendarValidator.getInstance().validate2(pattern_val, pattern).getTime(),
            "validate(A) pattern",
        )

        # Validate using both pattern and locale
        CalendarValidator.getInstance()
        CalendarValidator.getInstance().validate6(
            german_val, german_pattern, Locale.GERMAN
        )
        self.assertEqual(
            expected,
            CalendarValidator.getInstance()
            .validate6(german_val, german_pattern, Locale.GERMAN)
            .getTime(),
            "validate(A) both",
        )

        # Check validity using default format
        CalendarValidator.getInstance()
        self.assertTrue(
            CalendarValidator.getInstance().isValid0(default_val), "isValid(A) default"
        )

        # Check validity using locale
        CalendarValidator.getInstance()
        self.assertTrue(
            CalendarValidator.getInstance().isValid2(locale_val, locale),
            "isValid(A) locale",
        )

    def testCalendarValidatorMethods_test12_decomposed(self) -> None:
        # Set default locale to US
        Locale.setDefault(Locale.US)

        # Define variables
        locale = Locale.GERMAN
        pattern = "yyyy-MM-dd"
        pattern_val = "2005-12-31"
        german_val = "31 Dez 2005"
        german_pattern = "dd MMM yyyy"
        locale_val = "31.12.2005"
        default_val = "12/31/05"
        XXXX = "XXXX"

        # Create expected date
        expected = self._createCalendar(None, 20051231, 0).getTime()

        # Validate default value
        validator = CalendarValidator.getInstance()
        self.assertEqual(
            expected, validator.validate0(default_val).getTime(), "validate(A) default"
        )

        # Validate locale value
        self.assertEqual(
            expected,
            validator.validate4(locale_val, locale).getTime(),
            "validate(A) locale",
        )

        # Validate pattern value
        self.assertEqual(
            expected,
            validator.validate2(pattern_val, pattern).getTime(),
            "validate(A) pattern",
        )

        # Validate German value with pattern and locale
        self.assertEqual(
            expected,
            validator.validate6(german_val, german_pattern, Locale.GERMAN).getTime(),
            "validate(A) both",
        )

        # Check if default value is valid
        self.assertTrue(validator.isValid0(default_val), "isValid(A) default")

        # Check if locale value is valid
        self.assertTrue(validator.isValid2(locale_val, locale), "isValid(A) locale")

    def testCalendarValidatorMethods_test11_decomposed(self) -> None:
        # Set the default locale to US
        Locale.setDefault(Locale.US)

        # Define variables
        locale = Locale.GERMAN
        pattern = "yyyy-MM-dd"
        pattern_val = "2005-12-31"
        german_val = "31 Dez 2005"
        german_pattern = "dd MMM yyyy"
        locale_val = "31.12.2005"
        default_val = "12/31/05"
        XXXX = "XXXX"

        # Create the expected date
        expected = self._createCalendar(None, 20051231, 0).getTime()

        # Validate using default format
        CalendarValidator.getInstance()
        result_default = CalendarValidator.getInstance().validate0(default_val)
        self.assertEqual(expected, result_default.getTime(), "validate(A) default")

        # Validate using locale
        CalendarValidator.getInstance()
        result_locale = CalendarValidator.getInstance().validate4(locale_val, locale)
        self.assertEqual(expected, result_locale.getTime(), "validate(A) locale")

        # Validate using pattern
        CalendarValidator.getInstance()
        result_pattern = CalendarValidator.getInstance().validate2(pattern_val, pattern)
        self.assertEqual(expected, result_pattern.getTime(), "validate(A) pattern")

        # Validate using both pattern and locale
        CalendarValidator.getInstance()
        result_both = CalendarValidator.getInstance().validate6(
            german_val, german_pattern, Locale.GERMAN
        )
        self.assertEqual(expected, result_both.getTime(), "validate(A) both")

        # Check if the default value is valid
        CalendarValidator.getInstance()
        self.assertTrue(
            CalendarValidator.getInstance().isValid0(default_val), "isValid(A) default"
        )

    def testCalendarValidatorMethods_test10_decomposed(self) -> None:
        Locale.setDefault(Locale.US)
        locale = Locale.GERMAN
        pattern = "yyyy-MM-dd"
        pattern_val = "2005-12-31"
        german_val = "31 Dez 2005"
        german_pattern = "dd MMM yyyy"
        locale_val = "31.12.2005"
        default_val = "12/31/05"
        XXXX = "XXXX"
        expected = self._createCalendar(None, 20051231, 0).getTime()

        # Validate default value
        CalendarValidator.getInstance()
        CalendarValidator.getInstance().validate0(default_val)
        self.assertEqual(
            expected,
            CalendarValidator.getInstance().validate0(default_val).getTime(),
            "validate(A) default",
        )

        # Validate locale value
        CalendarValidator.getInstance()
        CalendarValidator.getInstance().validate4(locale_val, locale)
        self.assertEqual(
            expected,
            CalendarValidator.getInstance().validate4(locale_val, locale).getTime(),
            "validate(A) locale",
        )

        # Validate pattern value
        CalendarValidator.getInstance()
        CalendarValidator.getInstance().validate2(pattern_val, pattern)
        self.assertEqual(
            expected,
            CalendarValidator.getInstance().validate2(pattern_val, pattern).getTime(),
            "validate(A) pattern",
        )

        # Validate German value with pattern and locale
        CalendarValidator.getInstance()
        CalendarValidator.getInstance().validate6(
            german_val, german_pattern, Locale.GERMAN
        )
        self.assertEqual(
            expected,
            CalendarValidator.getInstance()
            .validate6(german_val, german_pattern, Locale.GERMAN)
            .getTime(),
            "validate(A) both",
        )

        # Check if default value is valid
        CalendarValidator.getInstance()
        self.assertTrue(
            CalendarValidator.getInstance().isValid0(default_val), "isValid(A) default"
        )

    def testCalendarValidatorMethods_test9_decomposed(self) -> None:
        # Set default locale to US
        locale.setlocale(locale.LC_TIME, "en_US.UTF-8")

        # Define variables
        locale_value = locale.Locale("de")  # Locale.GERMAN
        pattern = "yyyy-MM-dd"
        pattern_val = "2005-12-31"
        german_val = "31 Dez 2005"
        german_pattern = "dd MMM yyyy"
        locale_val = "31.12.2005"
        default_val = "12/31/05"
        XXXX = "XXXX"

        # Expected date
        expected = self._createCalendar(None, 20051231, 0).getTime()

        # Validate default value
        validator = CalendarValidator.getInstance()
        result_default = validator.validate0(default_val)
        self.assertEqual(expected, result_default.getTime(), "validate(A) default")

        # Validate locale value
        result_locale = validator.validate4(locale_val, locale_value)
        self.assertEqual(expected, result_locale.getTime(), "validate(A) locale")

        # Validate pattern value
        result_pattern = validator.validate2(pattern_val, pattern)
        self.assertEqual(expected, result_pattern.getTime(), "validate(A) pattern")

        # Validate German value with pattern and locale
        result_german = validator.validate6(german_val, german_pattern, locale_value)
        self.assertEqual(expected, result_german.getTime(), "validate(A) both")

    def testCalendarValidatorMethods_test8_decomposed(self) -> None:
        # Set default locale to US
        locale.setlocale(locale.LC_TIME, "en_US.UTF-8")

        # Define variables
        locale_value = locale.Locale("de")  # Locale.GERMAN
        pattern = "yyyy-MM-dd"
        pattern_val = "2005-12-31"
        german_val = "31 Dez 2005"
        german_pattern = "dd MMM yyyy"
        locale_val = "31.12.2005"
        default_val = "12/31/05"
        XXXX = "XXXX"
        expected = self._createCalendar(None, 20051231, 0).getTime()

        # Validate default value
        validator = CalendarValidator.getInstance()
        result = validator.validate0(default_val)
        self.assertEqual(expected, result.getTime(), "validate(A) default")

        # Validate locale value
        result = validator.validate4(locale_val, locale_value)
        self.assertEqual(expected, result.getTime(), "validate(A) locale")

        # Validate pattern value
        result = validator.validate2(pattern_val, pattern)
        self.assertEqual(expected, result.getTime(), "validate(A) pattern")

        # Validate German value with pattern and locale
        result = validator.validate6(german_val, german_pattern, locale_value)
        self.assertEqual(expected, result.getTime(), "validate(A) both")

    def testCalendarValidatorMethods_test7_decomposed(self) -> None:
        # Set the default locale to US
        locale.setlocale(locale.LC_TIME, "en_US.UTF-8")

        # Define variables
        locale_value = locale.GERMAN
        pattern = "yyyy-MM-dd"
        pattern_val = "2005-12-31"
        german_val = "31 Dez 2005"
        german_pattern = "dd MMM yyyy"
        locale_val = "31.12.2005"
        default_val = "12/31/05"
        XXXX = "XXXX"

        # Create the expected date
        expected = self._createCalendar(None, 20051231, 0).getTime()

        # Validate using default locale
        validator = CalendarValidator.getInstance()
        result_default = validator.validate0(default_val)
        self.assertEqual(expected, result_default.getTime(), "validate(A) default")

        # Validate using specific locale
        result_locale = validator.validate4(locale_val, locale_value)
        self.assertEqual(expected, result_locale.getTime(), "validate(A) locale")

        # Validate using specific pattern
        result_pattern = validator.validate2(pattern_val, pattern)
        self.assertEqual(expected, result_pattern.getTime(), "validate(A) pattern")

    def testCalendarValidatorMethods_test6_decomposed(self) -> None:
        # Set the default locale to US
        locale.setlocale(locale.LC_TIME, "en_US.UTF-8")

        # Define variables
        locale_value = locale.GERMAN
        pattern = "yyyy-MM-dd"
        pattern_val = "2005-12-31"
        german_val = "31 Dez 2005"
        german_pattern = "dd MMM yyyy"
        locale_val = "31.12.2005"
        default_val = "12/31/05"
        XXXX = "XXXX"

        # Create the expected date
        expected = self._createCalendar(None, 20051231, 0).getTime()

        # Validate using default pattern
        CalendarValidator.getInstance()
        result_default = CalendarValidator.getInstance().validate0(default_val)
        self.assertEqual(expected, result_default.getTime(), "validate(A) default")

        # Validate using locale
        CalendarValidator.getInstance()
        result_locale = CalendarValidator.getInstance().validate4(
            locale_val, locale_value
        )
        self.assertEqual(expected, result_locale.getTime(), "validate(A) locale")

        # Validate using custom pattern
        CalendarValidator.getInstance()
        result_pattern = CalendarValidator.getInstance().validate2(pattern_val, pattern)
        self.assertEqual(expected, result_pattern.getTime(), "validate(A) pattern")

    def testCalendarValidatorMethods_test5_decomposed(self) -> None:
        # Set the default locale to US
        locale.setlocale(locale.LC_TIME, "en_US.UTF-8")

        # Define variables
        locale_value = locale.Locale("de")  # GERMAN locale
        pattern = "yyyy-MM-dd"
        pattern_val = "2005-12-31"
        german_val = "31 Dez 2005"
        german_pattern = "dd MMM yyyy"
        locale_val = "31.12.2005"
        default_val = "12/31/05"
        XXXX = "XXXX"

        # Create the expected date
        expected = self._createCalendar(None, 20051231, 0).getTime()

        # Validate using default locale
        validator = CalendarValidator.getInstance()
        result_default = validator.validate0(default_val)
        self.assertEqual(expected, result_default.getTime(), "validate(A) default")

        # Validate using German locale
        result_locale = validator.validate4(locale_val, locale_value)
        self.assertEqual(expected, result_locale.getTime(), "validate(A) locale")

    def testCalendarValidatorMethods_test4_decomposed(self) -> None:
        # Set the default locale to US
        locale.setlocale(locale.LC_TIME, "en_US.UTF-8")

        # Define variables
        locale_value = locale.GERMAN
        pattern = "yyyy-MM-dd"
        pattern_val = "2005-12-31"
        german_val = "31 Dez 2005"
        german_pattern = "dd MMM yyyy"
        locale_val = "31.12.2005"
        default_val = "12/31/05"
        XXXX = "XXXX"

        # Create the expected date
        expected = self._createCalendar(None, 20051231, 0).getTime()

        # Validate using default locale
        CalendarValidator.getInstance()
        result_default = CalendarValidator.getInstance().validate0(default_val)
        self.assertEqual(expected, result_default.getTime(), "validate(A) default")

        # Validate using German locale
        CalendarValidator.getInstance()
        result_locale = CalendarValidator.getInstance().validate4(
            locale_val, locale_value
        )
        self.assertEqual(expected, result_locale.getTime(), "validate(A) locale")

    def testCalendarValidatorMethods_test3_decomposed(self) -> None:
        # Set the default locale to US
        locale.setlocale(locale.LC_ALL, "en_US.UTF-8")

        # Define variables
        locale_value = "de_DE.UTF-8"  # Locale.GERMAN equivalent
        pattern = "yyyy-MM-dd"
        pattern_val = "2005-12-31"
        german_val = "31 Dez 2005"
        german_pattern = "dd MMM yyyy"
        locale_val = "31.12.2005"
        default_val = "12/31/05"
        XXXX = "XXXX"

        # Create the expected date
        expected = self._createCalendar(None, 20051231, 0).getTime()

        # Get the CalendarValidator instance
        validator = CalendarValidator.getInstance()

        # Validate the default value
        result = validator.validate0(default_val)

        # Assert the validation result
        self.assertEqual(expected, result.getTime(), "validate(A) default")

    def testCalendarValidatorMethods_test2_decomposed(self) -> None:
        # Set the default locale to US
        locale.setlocale(locale.LC_ALL, "en_US")

        # Define variables
        locale_value = "de_DE"  # Locale.GERMAN equivalent
        pattern = "yyyy-MM-dd"
        pattern_val = "2005-12-31"
        german_val = "31 Dez 2005"
        german_pattern = "dd MMM yyyy"
        locale_val = "31.12.2005"
        default_val = "12/31/05"
        XXXX = "XXXX"

        # Create the expected date
        expected = self._createCalendar(None, 20051231, 0).getTime()

        # Get the CalendarValidator instance
        validator = CalendarValidator.getInstance()

        # Validate the default value
        result = validator.validate0(default_val)

        # Assert the validation result
        self.assertEqual(expected, result.getTime(), "validate(A) default")

    def testCalendarValidatorMethods_test1_decomposed(self) -> None:
        import locale
        from datetime import datetime

        # Set default locale to US
        locale.setlocale(locale.LC_ALL, "en_US")

        # Define variables
        locale_value = "de_DE"  # Locale.GERMAN equivalent
        pattern = "yyyy-MM-dd"
        pattern_val = "2005-12-31"
        german_val = "31 Dez 2005"
        german_pattern = "dd MMM yyyy"
        locale_val = "31.12.2005"
        default_val = "12/31/05"
        XXXX = "XXXX"

        # Expected date
        expected = self._createCalendar(None, 20051231, 0).getTime()

        # Get CalendarValidator instance
        CalendarValidator.getInstance()

    def testCalendarValidatorMethods_test0_decomposed(self) -> None:
        import locale
        from datetime import datetime

        # Set the default locale to US
        locale.setlocale(locale.LC_ALL, "en_US")

        # Define variables
        locale_value = "de_DE"  # Locale.GERMAN equivalent
        pattern = "yyyy-MM-dd"
        pattern_val = "2005-12-31"
        german_val = "31 Dez 2005"
        german_pattern = "dd MMM yyyy"
        locale_val = "31.12.2005"
        default_val = "12/31/05"
        XXXX = "XXXX"

        # Expected date
        expected = self._createCalendar(None, 20051231, 0).getTime()

    def testFormat(self) -> None:
        orig_default = locale.getdefaultlocale()
        locale.setlocale(locale.LC_ALL, "en_GB")  # Set locale to UK

        cal_20050101 = self._createCalendar(self._GMT, 20051231, 11500)
        self.assertIsNone(self.__calValidator.format0(None), "null")
        self.assertEqual(
            "31/12/05", self.__calValidator.format0(cal_20050101), "default"
        )
        self.assertEqual(
            "12/31/05",
            self.__calValidator.format2(cal_20050101, locale="en_US"),
            "locale",
        )
        self.assertEqual(
            "2005-12-31 01:15",
            self.__calValidator.format1(cal_20050101, "yyyy-MM-dd HH:mm"),
            "patternA",
        )
        self.assertEqual(
            "2005-12-31 GMT",
            self.__calValidator.format1(cal_20050101, "yyyy-MM-dd z"),
            "patternB",
        )
        self.assertEqual(
            "31 Dez 2005",
            self.__calValidator.format3(cal_20050101, "dd MMM yyyy", locale="de_DE"),
            "both",
        )

        self.assertEqual(
            "30/12/05",
            self.__calValidator.format0(cal_20050101, self._EST),
            "EST default",
        )
        self.assertEqual(
            "12/30/05",
            self.__calValidator.format2(
                cal_20050101, locale="en_US", timeZone=self._EST
            ),
            "EST locale",
        )
        self.assertEqual(
            "2005-12-30 20:15",
            self.__calValidator.format1(cal_20050101, "yyyy-MM-dd HH:mm", self._EST),
            "EST patternA",
        )
        self.assertEqual(
            "2005-12-30 EST",
            self.__calValidator.format1(cal_20050101, "yyyy-MM-dd z", self._EST),
            "EST patternB",
        )
        self.assertEqual(
            "30 Dez 2005",
            self.__calValidator.format4(
                cal_20050101, "dd MMM yyyy", locale="de_DE", timeZone=self._EST
            ),
            "EST both",
        )

        locale.setlocale(locale.LC_ALL, orig_default)  # Restore original locale

    def setUp(self) -> None:
        super().setUp()
        self.__calValidator = CalendarValidator.CalendarValidator1()
        self._validator = self.__calValidator
