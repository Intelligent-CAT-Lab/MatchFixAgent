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
from src.main.org.apache.commons.validator.routines.DateValidator import *


class DateValidatorTest(AbstractCalendarValidatorTest, unittest.TestCase):

    __dateValidator: DateValidator = None

    def testCompare_test9_decomposed(self) -> None:
        same_time = 124522
        test_date = 20050823
        diff_hour = self._createDate(self._GMT, test_date, 115922)
        value = self._createDate(self._GMT, test_date, same_time)
        date_20050824 = self._createDate(self._GMT, 20050824, same_time)
        date_20050822 = self._createDate(self._GMT, 20050822, same_time)
        date_20050830 = self._createDate(self._GMT, 20050830, same_time)
        date_20050816 = self._createDate(self._GMT, 20050816, same_time)
        date_20050901 = self._createDate(self._GMT, 20050901, same_time)
        date_20050801 = self._createDate(self._GMT, 20050801, same_time)
        date_20050731 = self._createDate(self._GMT, 20050731, same_time)
        date_20051101 = self._createDate(self._GMT, 20051101, same_time)
        date_20051001 = self._createDate(self._GMT, 20051001, same_time)
        date_20050701 = self._createDate(self._GMT, 20050701, same_time)
        date_20050630 = self._createDate(self._GMT, 20050630, same_time)
        date_20050110 = self._createDate(self._GMT, 20050110, same_time)
        date_20060101 = self._createDate(self._GMT, 20060101, same_time)
        date_20050101 = self._createDate(self._GMT, 20050101, same_time)
        date_20041231 = self._createDate(self._GMT, 20041231, same_time)
        same_day_two_am = self._createDate(self._GMT, test_date, 20000)

        self.assertEqual(
            -1,
            self.__dateValidator.compareDates(value, date_20050824, self._GMT),
            "date LT",
        )
        self.assertEqual(
            0, self.__dateValidator.compareDates(value, diff_hour, self._GMT), "date EQ"
        )
        self.assertEqual(
            1,
            self.__dateValidator.compareDates(value, date_20050822, self._GMT),
            "date GT",
        )
        self.assertEqual(
            -1,
            self.__dateValidator.compareWeeks(value, date_20050830, self._GMT),
            "week LT",
        )
        self.assertEqual(
            0,
            self.__dateValidator.compareWeeks(value, date_20050824, self._GMT),
            "week =1",
        )
        self.assertEqual(
            0,
            self.__dateValidator.compareWeeks(value, date_20050822, self._GMT),
            "week =2",
        )
        self.assertEqual(
            0,
            self.__dateValidator.compareWeeks(value, date_20050822, self._GMT),
            "week =3",
        )
        self.assertEqual(
            1,
            self.__dateValidator.compareWeeks(value, date_20050816, self._GMT),
            "week GT",
        )
        self.assertEqual(
            -1,
            self.__dateValidator.compareMonths(value, date_20050901, self._GMT),
            "mnth LT",
        )
        self.assertEqual(
            0,
            self.__dateValidator.compareMonths(value, date_20050830, self._GMT),
            "mnth =1",
        )
        self.assertEqual(
            0,
            self.__dateValidator.compareMonths(value, date_20050801, self._GMT),
            "mnth =2",
        )
        self.assertEqual(
            0,
            self.__dateValidator.compareMonths(value, date_20050816, self._GMT),
            "mnth =3",
        )
        self.assertEqual(
            1,
            self.__dateValidator.compareMonths(value, date_20050731, self._GMT),
            "mnth GT",
        )
        self.assertEqual(
            -1,
            self.__dateValidator.compareQuarters0(value, date_20051101, self._GMT),
            "qtrA <1",
        )
        self.assertEqual(
            -1,
            self.__dateValidator.compareQuarters0(value, date_20051001, self._GMT),
            "qtrA <2",
        )
        self.assertEqual(
            0,
            self.__dateValidator.compareQuarters0(value, date_20050901, self._GMT),
            "qtrA =1",
        )
        self.assertEqual(
            0,
            self.__dateValidator.compareQuarters0(value, date_20050701, self._GMT),
            "qtrA =2",
        )
        self.assertEqual(
            0,
            self.__dateValidator.compareQuarters0(value, date_20050731, self._GMT),
            "qtrA =3",
        )
        self.assertEqual(
            1,
            self.__dateValidator.compareQuarters0(value, date_20050630, self._GMT),
            "qtrA GT",
        )
        self.assertEqual(
            -1,
            self.__dateValidator.compareQuarters1(value, date_20051101, self._GMT, 2),
            "qtrB LT",
        )
        self.assertEqual(
            0,
            self.__dateValidator.compareQuarters1(value, date_20051001, self._GMT, 2),
            "qtrB =1",
        )
        self.assertEqual(
            0,
            self.__dateValidator.compareQuarters1(value, date_20050901, self._GMT, 2),
            "qtrB =2",
        )
        self.assertEqual(
            1,
            self.__dateValidator.compareQuarters1(value, date_20050701, self._GMT, 2),
            "qtrB =3",
        )
        self.assertEqual(
            1,
            self.__dateValidator.compareQuarters1(value, date_20050731, self._GMT, 2),
            "qtrB =4",
        )
        self.assertEqual(
            1,
            self.__dateValidator.compareQuarters1(value, date_20050630, self._GMT, 2),
            "qtrB GT",
        )
        self.assertEqual(
            1,
            self.__dateValidator.compareQuarters1(value, date_20050110, self._GMT, 2),
            "qtrB prev",
        )
        self.assertEqual(
            -1,
            self.__dateValidator.compareYears(value, date_20060101, self._GMT),
            "year LT",
        )
        self.assertEqual(
            0,
            self.__dateValidator.compareYears(value, date_20050101, self._GMT),
            "year EQ",
        )
        self.assertEqual(
            1,
            self.__dateValidator.compareYears(value, date_20041231, self._GMT),
            "year GT",
        )
        self.assertEqual(
            -1,
            self.__dateValidator.compareDates(value, date_20050824, self._EST),
            "date LT",
        )
        self.assertEqual(
            0, self.__dateValidator.compareDates(value, diff_hour, self._EST), "date EQ"
        )
        self.assertEqual(
            1,
            self.__dateValidator.compareDates(value, same_day_two_am, self._EST),
            "date EQ",
        )
        self.assertEqual(
            1,
            self.__dateValidator.compareDates(value, date_20050822, self._EST),
            "date GT",
        )

    def testCompare_test8_decomposed(self) -> None:
        same_time = 124522
        test_date = 20050823
        diff_hour = self._createDate(self._GMT, test_date, 115922)
        value = self._createDate(self._GMT, test_date, same_time)
        date_20050824 = self._createDate(self._GMT, 20050824, same_time)
        date_20050822 = self._createDate(self._GMT, 20050822, same_time)
        date_20050830 = self._createDate(self._GMT, 20050830, same_time)
        date_20050816 = self._createDate(self._GMT, 20050816, same_time)
        date_20050901 = self._createDate(self._GMT, 20050901, same_time)
        date_20050801 = self._createDate(self._GMT, 20050801, same_time)
        date_20050731 = self._createDate(self._GMT, 20050731, same_time)
        date_20051101 = self._createDate(self._GMT, 20051101, same_time)
        date_20051001 = self._createDate(self._GMT, 20051001, same_time)
        date_20050701 = self._createDate(self._GMT, 20050701, same_time)
        date_20050630 = self._createDate(self._GMT, 20050630, same_time)
        date_20050110 = self._createDate(self._GMT, 20050110, same_time)
        date_20060101 = self._createDate(self._GMT, 20060101, same_time)
        date_20050101 = self._createDate(self._GMT, 20050101, same_time)
        date_20041231 = self._createDate(self._GMT, 20041231, same_time)

        self.assertEqual(
            -1,
            self.__dateValidator.compareDates(value, date_20050824, self._GMT),
            "date LT",
        )
        self.assertEqual(
            0, self.__dateValidator.compareDates(value, diff_hour, self._GMT), "date EQ"
        )
        self.assertEqual(
            1,
            self.__dateValidator.compareDates(value, date_20050822, self._GMT),
            "date GT",
        )
        self.assertEqual(
            -1,
            self.__dateValidator.compareWeeks(value, date_20050830, self._GMT),
            "week LT",
        )
        self.assertEqual(
            0,
            self.__dateValidator.compareWeeks(value, date_20050824, self._GMT),
            "week =1",
        )
        self.assertEqual(
            0,
            self.__dateValidator.compareWeeks(value, date_20050822, self._GMT),
            "week =2",
        )
        self.assertEqual(
            0,
            self.__dateValidator.compareWeeks(value, date_20050822, self._GMT),
            "week =3",
        )
        self.assertEqual(
            1,
            self.__dateValidator.compareWeeks(value, date_20050816, self._GMT),
            "week GT",
        )
        self.assertEqual(
            -1,
            self.__dateValidator.compareMonths(value, date_20050901, self._GMT),
            "mnth LT",
        )
        self.assertEqual(
            0,
            self.__dateValidator.compareMonths(value, date_20050830, self._GMT),
            "mnth =1",
        )
        self.assertEqual(
            0,
            self.__dateValidator.compareMonths(value, date_20050801, self._GMT),
            "mnth =2",
        )
        self.assertEqual(
            0,
            self.__dateValidator.compareMonths(value, date_20050816, self._GMT),
            "mnth =3",
        )
        self.assertEqual(
            1,
            self.__dateValidator.compareMonths(value, date_20050731, self._GMT),
            "mnth GT",
        )
        self.assertEqual(
            -1,
            self.__dateValidator.compareQuarters0(value, date_20051101, self._GMT),
            "qtrA <1",
        )
        self.assertEqual(
            -1,
            self.__dateValidator.compareQuarters0(value, date_20051001, self._GMT),
            "qtrA <2",
        )
        self.assertEqual(
            0,
            self.__dateValidator.compareQuarters0(value, date_20050901, self._GMT),
            "qtrA =1",
        )
        self.assertEqual(
            0,
            self.__dateValidator.compareQuarters0(value, date_20050701, self._GMT),
            "qtrA =2",
        )
        self.assertEqual(
            0,
            self.__dateValidator.compareQuarters0(value, date_20050731, self._GMT),
            "qtrA =3",
        )
        self.assertEqual(
            1,
            self.__dateValidator.compareQuarters0(value, date_20050630, self._GMT),
            "qtrA GT",
        )
        self.assertEqual(
            -1,
            self.__dateValidator.compareQuarters1(value, date_20051101, self._GMT, 2),
            "qtrB LT",
        )
        self.assertEqual(
            0,
            self.__dateValidator.compareQuarters1(value, date_20051001, self._GMT, 2),
            "qtrB =1",
        )
        self.assertEqual(
            0,
            self.__dateValidator.compareQuarters1(value, date_20050901, self._GMT, 2),
            "qtrB =2",
        )
        self.assertEqual(
            1,
            self.__dateValidator.compareQuarters1(value, date_20050701, self._GMT, 2),
            "qtrB =3",
        )
        self.assertEqual(
            1,
            self.__dateValidator.compareQuarters1(value, date_20050731, self._GMT, 2),
            "qtrB =4",
        )
        self.assertEqual(
            1,
            self.__dateValidator.compareQuarters1(value, date_20050630, self._GMT, 2),
            "qtrB GT",
        )
        self.assertEqual(
            1,
            self.__dateValidator.compareQuarters1(value, date_20050110, self._GMT, 2),
            "qtrB prev",
        )
        self.assertEqual(
            -1,
            self.__dateValidator.compareYears(value, date_20060101, self._GMT),
            "year LT",
        )
        self.assertEqual(
            0,
            self.__dateValidator.compareYears(value, date_20050101, self._GMT),
            "year EQ",
        )
        self.assertEqual(
            1,
            self.__dateValidator.compareYears(value, date_20041231, self._GMT),
            "year GT",
        )

        same_day_two_am = self._createDate(self._GMT, test_date, 20000)

    def testCompare_test7_decomposed(self) -> None:
        same_time = 124522
        test_date = 20050823
        diff_hour = self._createDate(self._GMT, test_date, 115922)
        value = self._createDate(self._GMT, test_date, same_time)
        date_20050824 = self._createDate(self._GMT, 20050824, same_time)
        date_20050822 = self._createDate(self._GMT, 20050822, same_time)
        date_20050830 = self._createDate(self._GMT, 20050830, same_time)
        date_20050816 = self._createDate(self._GMT, 20050816, same_time)
        date_20050901 = self._createDate(self._GMT, 20050901, same_time)
        date_20050801 = self._createDate(self._GMT, 20050801, same_time)
        date_20050731 = self._createDate(self._GMT, 20050731, same_time)
        date_20051101 = self._createDate(self._GMT, 20051101, same_time)
        date_20051001 = self._createDate(self._GMT, 20051001, same_time)
        date_20050701 = self._createDate(self._GMT, 20050701, same_time)
        date_20050630 = self._createDate(self._GMT, 20050630, same_time)
        date_20050110 = self._createDate(self._GMT, 20050110, same_time)
        date_20060101 = self._createDate(self._GMT, 20060101, same_time)
        date_20050101 = self._createDate(self._GMT, 20050101, same_time)
        date_20041231 = self._createDate(self._GMT, 20041231, same_time)

        self.assertEqual(
            -1,
            self.__dateValidator.compareDates(value, date_20050824, self._GMT),
            "date LT",
        )
        self.assertEqual(
            0, self.__dateValidator.compareDates(value, diff_hour, self._GMT), "date EQ"
        )
        self.assertEqual(
            1,
            self.__dateValidator.compareDates(value, date_20050822, self._GMT),
            "date GT",
        )
        self.assertEqual(
            -1,
            self.__dateValidator.compareWeeks(value, date_20050830, self._GMT),
            "week LT",
        )
        self.assertEqual(
            0,
            self.__dateValidator.compareWeeks(value, date_20050824, self._GMT),
            "week =1",
        )
        self.assertEqual(
            0,
            self.__dateValidator.compareWeeks(value, date_20050822, self._GMT),
            "week =2",
        )
        self.assertEqual(
            0,
            self.__dateValidator.compareWeeks(value, date_20050822, self._GMT),
            "week =3",
        )
        self.assertEqual(
            1,
            self.__dateValidator.compareWeeks(value, date_20050816, self._GMT),
            "week GT",
        )
        self.assertEqual(
            -1,
            self.__dateValidator.compareMonths(value, date_20050901, self._GMT),
            "mnth LT",
        )
        self.assertEqual(
            0,
            self.__dateValidator.compareMonths(value, date_20050830, self._GMT),
            "mnth =1",
        )
        self.assertEqual(
            0,
            self.__dateValidator.compareMonths(value, date_20050801, self._GMT),
            "mnth =2",
        )
        self.assertEqual(
            0,
            self.__dateValidator.compareMonths(value, date_20050816, self._GMT),
            "mnth =3",
        )
        self.assertEqual(
            1,
            self.__dateValidator.compareMonths(value, date_20050731, self._GMT),
            "mnth GT",
        )
        self.assertEqual(
            -1,
            self.__dateValidator.compareQuarters0(value, date_20051101, self._GMT),
            "qtrA <1",
        )
        self.assertEqual(
            -1,
            self.__dateValidator.compareQuarters0(value, date_20051001, self._GMT),
            "qtrA <2",
        )
        self.assertEqual(
            0,
            self.__dateValidator.compareQuarters0(value, date_20050901, self._GMT),
            "qtrA =1",
        )
        self.assertEqual(
            0,
            self.__dateValidator.compareQuarters0(value, date_20050701, self._GMT),
            "qtrA =2",
        )
        self.assertEqual(
            0,
            self.__dateValidator.compareQuarters0(value, date_20050731, self._GMT),
            "qtrA =3",
        )
        self.assertEqual(
            1,
            self.__dateValidator.compareQuarters0(value, date_20050630, self._GMT),
            "qtrA GT",
        )
        self.assertEqual(
            -1,
            self.__dateValidator.compareQuarters1(value, date_20051101, self._GMT, 2),
            "qtrB LT",
        )
        self.assertEqual(
            0,
            self.__dateValidator.compareQuarters1(value, date_20051001, self._GMT, 2),
            "qtrB =1",
        )
        self.assertEqual(
            0,
            self.__dateValidator.compareQuarters1(value, date_20050901, self._GMT, 2),
            "qtrB =2",
        )
        self.assertEqual(
            1,
            self.__dateValidator.compareQuarters1(value, date_20050701, self._GMT, 2),
            "qtrB =3",
        )
        self.assertEqual(
            1,
            self.__dateValidator.compareQuarters1(value, date_20050731, self._GMT, 2),
            "qtrB =4",
        )
        self.assertEqual(
            1,
            self.__dateValidator.compareQuarters1(value, date_20050630, self._GMT, 2),
            "qtrB GT",
        )
        self.assertEqual(
            1,
            self.__dateValidator.compareQuarters1(value, date_20050110, self._GMT, 2),
            "qtrB prev",
        )
        self.assertEqual(
            -1,
            self.__dateValidator.compareYears(value, date_20060101, self._GMT),
            "year LT",
        )
        self.assertEqual(
            0,
            self.__dateValidator.compareYears(value, date_20050101, self._GMT),
            "year EQ",
        )
        self.assertEqual(
            1,
            self.__dateValidator.compareYears(value, date_20041231, self._GMT),
            "year GT",
        )

    def testCompare_test6_decomposed(self) -> None:
        same_time = 124522
        test_date = 20050823
        diff_hour = self._createDate(self._GMT, test_date, 115922)
        value = self._createDate(self._GMT, test_date, same_time)
        date_20050824 = self._createDate(self._GMT, 20050824, same_time)
        date_20050822 = self._createDate(self._GMT, 20050822, same_time)
        date_20050830 = self._createDate(self._GMT, 20050830, same_time)
        date_20050816 = self._createDate(self._GMT, 20050816, same_time)
        date_20050901 = self._createDate(self._GMT, 20050901, same_time)
        date_20050801 = self._createDate(self._GMT, 20050801, same_time)
        date_20050731 = self._createDate(self._GMT, 20050731, same_time)
        date_20051101 = self._createDate(self._GMT, 20051101, same_time)
        date_20051001 = self._createDate(self._GMT, 20051001, same_time)
        date_20050701 = self._createDate(self._GMT, 20050701, same_time)
        date_20050630 = self._createDate(self._GMT, 20050630, same_time)
        date_20050110 = self._createDate(self._GMT, 20050110, same_time)
        date_20060101 = self._createDate(self._GMT, 20060101, same_time)
        date_20050101 = self._createDate(self._GMT, 20050101, same_time)
        date_20041231 = self._createDate(self._GMT, 20041231, same_time)

        self.assertEqual(
            -1,
            self.__dateValidator.compareDates(value, date_20050824, self._GMT),
            "date LT",
        )
        self.assertEqual(
            0, self.__dateValidator.compareDates(value, diff_hour, self._GMT), "date EQ"
        )
        self.assertEqual(
            1,
            self.__dateValidator.compareDates(value, date_20050822, self._GMT),
            "date GT",
        )
        self.assertEqual(
            -1,
            self.__dateValidator.compareWeeks(value, date_20050830, self._GMT),
            "week LT",
        )
        self.assertEqual(
            0,
            self.__dateValidator.compareWeeks(value, date_20050824, self._GMT),
            "week =1",
        )
        self.assertEqual(
            0,
            self.__dateValidator.compareWeeks(value, date_20050822, self._GMT),
            "week =2",
        )
        self.assertEqual(
            0,
            self.__dateValidator.compareWeeks(value, date_20050822, self._GMT),
            "week =3",
        )
        self.assertEqual(
            1,
            self.__dateValidator.compareWeeks(value, date_20050816, self._GMT),
            "week GT",
        )
        self.assertEqual(
            -1,
            self.__dateValidator.compareMonths(value, date_20050901, self._GMT),
            "mnth LT",
        )
        self.assertEqual(
            0,
            self.__dateValidator.compareMonths(value, date_20050830, self._GMT),
            "mnth =1",
        )
        self.assertEqual(
            0,
            self.__dateValidator.compareMonths(value, date_20050801, self._GMT),
            "mnth =2",
        )
        self.assertEqual(
            0,
            self.__dateValidator.compareMonths(value, date_20050816, self._GMT),
            "mnth =3",
        )
        self.assertEqual(
            1,
            self.__dateValidator.compareMonths(value, date_20050731, self._GMT),
            "mnth GT",
        )
        self.assertEqual(
            -1,
            self.__dateValidator.compareQuarters0(value, date_20051101, self._GMT),
            "qtrA <1",
        )
        self.assertEqual(
            -1,
            self.__dateValidator.compareQuarters0(value, date_20051001, self._GMT),
            "qtrA <2",
        )
        self.assertEqual(
            0,
            self.__dateValidator.compareQuarters0(value, date_20050901, self._GMT),
            "qtrA =1",
        )
        self.assertEqual(
            0,
            self.__dateValidator.compareQuarters0(value, date_20050701, self._GMT),
            "qtrA =2",
        )
        self.assertEqual(
            0,
            self.__dateValidator.compareQuarters0(value, date_20050731, self._GMT),
            "qtrA =3",
        )
        self.assertEqual(
            1,
            self.__dateValidator.compareQuarters0(value, date_20050630, self._GMT),
            "qtrA GT",
        )
        self.assertEqual(
            -1,
            self.__dateValidator.compareQuarters1(value, date_20051101, self._GMT, 2),
            "qtrB LT",
        )
        self.assertEqual(
            0,
            self.__dateValidator.compareQuarters1(value, date_20051001, self._GMT, 2),
            "qtrB =1",
        )
        self.assertEqual(
            0,
            self.__dateValidator.compareQuarters1(value, date_20050901, self._GMT, 2),
            "qtrB =2",
        )
        self.assertEqual(
            1,
            self.__dateValidator.compareQuarters1(value, date_20050701, self._GMT, 2),
            "qtrB =3",
        )
        self.assertEqual(
            1,
            self.__dateValidator.compareQuarters1(value, date_20050731, self._GMT, 2),
            "qtrB =4",
        )
        self.assertEqual(
            1,
            self.__dateValidator.compareQuarters1(value, date_20050630, self._GMT, 2),
            "qtrB GT",
        )
        self.assertEqual(
            1,
            self.__dateValidator.compareQuarters1(value, date_20050110, self._GMT, 2),
            "qtrB prev",
        )

    def testCompare_test5_decomposed(self) -> None:
        same_time = 124522
        test_date = 20050823
        diff_hour = self._createDate(self._GMT, test_date, 115922)
        value = self._createDate(self._GMT, test_date, same_time)
        date_20050824 = self._createDate(self._GMT, 20050824, same_time)
        date_20050822 = self._createDate(self._GMT, 20050822, same_time)
        date_20050830 = self._createDate(self._GMT, 20050830, same_time)
        date_20050816 = self._createDate(self._GMT, 20050816, same_time)
        date_20050901 = self._createDate(self._GMT, 20050901, same_time)
        date_20050801 = self._createDate(self._GMT, 20050801, same_time)
        date_20050731 = self._createDate(self._GMT, 20050731, same_time)
        date_20051101 = self._createDate(self._GMT, 20051101, same_time)
        date_20051001 = self._createDate(self._GMT, 20051001, same_time)
        date_20050701 = self._createDate(self._GMT, 20050701, same_time)
        date_20050630 = self._createDate(self._GMT, 20050630, same_time)
        date_20050110 = self._createDate(self._GMT, 20050110, same_time)
        date_20060101 = self._createDate(self._GMT, 20060101, same_time)
        date_20050101 = self._createDate(self._GMT, 20050101, same_time)
        date_20041231 = self._createDate(self._GMT, 20041231, same_time)

        self.assertEqual(
            -1,
            self.__dateValidator.compareDates(value, date_20050824, self._GMT),
            "date LT",
        )
        self.assertEqual(
            0, self.__dateValidator.compareDates(value, diff_hour, self._GMT), "date EQ"
        )
        self.assertEqual(
            1,
            self.__dateValidator.compareDates(value, date_20050822, self._GMT),
            "date GT",
        )
        self.assertEqual(
            -1,
            self.__dateValidator.compareWeeks(value, date_20050830, self._GMT),
            "week LT",
        )
        self.assertEqual(
            0,
            self.__dateValidator.compareWeeks(value, date_20050824, self._GMT),
            "week =1",
        )
        self.assertEqual(
            0,
            self.__dateValidator.compareWeeks(value, date_20050822, self._GMT),
            "week =2",
        )
        self.assertEqual(
            0,
            self.__dateValidator.compareWeeks(value, date_20050822, self._GMT),
            "week =3",
        )
        self.assertEqual(
            1,
            self.__dateValidator.compareWeeks(value, date_20050816, self._GMT),
            "week GT",
        )
        self.assertEqual(
            -1,
            self.__dateValidator.compareMonths(value, date_20050901, self._GMT),
            "mnth LT",
        )
        self.assertEqual(
            0,
            self.__dateValidator.compareMonths(value, date_20050830, self._GMT),
            "mnth =1",
        )
        self.assertEqual(
            0,
            self.__dateValidator.compareMonths(value, date_20050801, self._GMT),
            "mnth =2",
        )
        self.assertEqual(
            0,
            self.__dateValidator.compareMonths(value, date_20050816, self._GMT),
            "mnth =3",
        )
        self.assertEqual(
            1,
            self.__dateValidator.compareMonths(value, date_20050731, self._GMT),
            "mnth GT",
        )
        self.assertEqual(
            -1,
            self.__dateValidator.compareQuarters0(value, date_20051101, self._GMT),
            "qtrA <1",
        )
        self.assertEqual(
            -1,
            self.__dateValidator.compareQuarters0(value, date_20051001, self._GMT),
            "qtrA <2",
        )
        self.assertEqual(
            0,
            self.__dateValidator.compareQuarters0(value, date_20050901, self._GMT),
            "qtrA =1",
        )
        self.assertEqual(
            0,
            self.__dateValidator.compareQuarters0(value, date_20050701, self._GMT),
            "qtrA =2",
        )
        self.assertEqual(
            0,
            self.__dateValidator.compareQuarters0(value, date_20050731, self._GMT),
            "qtrA =3",
        )
        self.assertEqual(
            1,
            self.__dateValidator.compareQuarters0(value, date_20050630, self._GMT),
            "qtrA GT",
        )

    def testCompare_test4_decomposed(self) -> None:
        same_time = 124522
        test_date = 20050823
        diff_hour = self._createDate(self._GMT, test_date, 115922)
        value = self._createDate(self._GMT, test_date, same_time)
        date_20050824 = self._createDate(self._GMT, 20050824, same_time)
        date_20050822 = self._createDate(self._GMT, 20050822, same_time)
        date_20050830 = self._createDate(self._GMT, 20050830, same_time)
        date_20050816 = self._createDate(self._GMT, 20050816, same_time)
        date_20050901 = self._createDate(self._GMT, 20050901, same_time)
        date_20050801 = self._createDate(self._GMT, 20050801, same_time)
        date_20050731 = self._createDate(self._GMT, 20050731, same_time)
        date_20051101 = self._createDate(self._GMT, 20051101, same_time)
        date_20051001 = self._createDate(self._GMT, 20051001, same_time)
        date_20050701 = self._createDate(self._GMT, 20050701, same_time)
        date_20050630 = self._createDate(self._GMT, 20050630, same_time)
        date_20050110 = self._createDate(self._GMT, 20050110, same_time)
        date_20060101 = self._createDate(self._GMT, 20060101, same_time)
        date_20050101 = self._createDate(self._GMT, 20050101, same_time)
        date_20041231 = self._createDate(self._GMT, 20041231, same_time)

        self.assertEqual(
            -1,
            self.__dateValidator.compareDates(value, date_20050824, self._GMT),
            "date LT",
        )
        self.assertEqual(
            0, self.__dateValidator.compareDates(value, diff_hour, self._GMT), "date EQ"
        )
        self.assertEqual(
            1,
            self.__dateValidator.compareDates(value, date_20050822, self._GMT),
            "date GT",
        )
        self.assertEqual(
            -1,
            self.__dateValidator.compareWeeks(value, date_20050830, self._GMT),
            "week LT",
        )
        self.assertEqual(
            0,
            self.__dateValidator.compareWeeks(value, date_20050824, self._GMT),
            "week =1",
        )
        self.assertEqual(
            0,
            self.__dateValidator.compareWeeks(value, date_20050822, self._GMT),
            "week =2",
        )
        self.assertEqual(
            0,
            self.__dateValidator.compareWeeks(value, date_20050822, self._GMT),
            "week =3",
        )
        self.assertEqual(
            1,
            self.__dateValidator.compareWeeks(value, date_20050816, self._GMT),
            "week GT",
        )
        self.assertEqual(
            -1,
            self.__dateValidator.compareMonths(value, date_20050901, self._GMT),
            "mnth LT",
        )
        self.assertEqual(
            0,
            self.__dateValidator.compareMonths(value, date_20050830, self._GMT),
            "mnth =1",
        )
        self.assertEqual(
            0,
            self.__dateValidator.compareMonths(value, date_20050801, self._GMT),
            "mnth =2",
        )
        self.assertEqual(
            0,
            self.__dateValidator.compareMonths(value, date_20050816, self._GMT),
            "mnth =3",
        )
        self.assertEqual(
            1,
            self.__dateValidator.compareMonths(value, date_20050731, self._GMT),
            "mnth GT",
        )

    def testCompare_test3_decomposed(self) -> None:
        same_time = 124522
        test_date = 20050823
        diff_hour = self._createDate(self._GMT, test_date, 115922)
        value = self._createDate(self._GMT, test_date, same_time)
        date_20050824 = self._createDate(self._GMT, 20050824, same_time)
        date_20050822 = self._createDate(self._GMT, 20050822, same_time)
        date_20050830 = self._createDate(self._GMT, 20050830, same_time)
        date_20050816 = self._createDate(self._GMT, 20050816, same_time)
        date_20050901 = self._createDate(self._GMT, 20050901, same_time)
        date_20050801 = self._createDate(self._GMT, 20050801, same_time)
        date_20050731 = self._createDate(self._GMT, 20050731, same_time)
        date_20051101 = self._createDate(self._GMT, 20051101, same_time)
        date_20051001 = self._createDate(self._GMT, 20051001, same_time)
        date_20050701 = self._createDate(self._GMT, 20050701, same_time)
        date_20050630 = self._createDate(self._GMT, 20050630, same_time)
        date_20050110 = self._createDate(self._GMT, 20050110, same_time)
        date_20060101 = self._createDate(self._GMT, 20060101, same_time)
        date_20050101 = self._createDate(self._GMT, 20050101, same_time)
        date_20041231 = self._createDate(self._GMT, 20041231, same_time)

        self.assertEqual(
            -1,
            self.__dateValidator.compareDates(value, date_20050824, self._GMT),
            "date LT",
        )
        self.assertEqual(
            0, self.__dateValidator.compareDates(value, diff_hour, self._GMT), "date EQ"
        )
        self.assertEqual(
            1,
            self.__dateValidator.compareDates(value, date_20050822, self._GMT),
            "date GT",
        )
        self.assertEqual(
            -1,
            self.__dateValidator.compareWeeks(value, date_20050830, self._GMT),
            "week LT",
        )
        self.assertEqual(
            0,
            self.__dateValidator.compareWeeks(value, date_20050824, self._GMT),
            "week =1",
        )
        self.assertEqual(
            0,
            self.__dateValidator.compareWeeks(value, date_20050822, self._GMT),
            "week =2",
        )
        self.assertEqual(
            0,
            self.__dateValidator.compareWeeks(value, date_20050822, self._GMT),
            "week =3",
        )
        self.assertEqual(
            1,
            self.__dateValidator.compareWeeks(value, date_20050816, self._GMT),
            "week GT",
        )

    def testCompare_test2_decomposed(self) -> None:
        same_time = 124522
        test_date = 20050823
        diff_hour = self._createDate(self._GMT, test_date, 115922)
        value = self._createDate(self._GMT, test_date, same_time)
        date_20050824 = self._createDate(self._GMT, 20050824, same_time)
        date_20050822 = self._createDate(self._GMT, 20050822, same_time)
        date_20050830 = self._createDate(self._GMT, 20050830, same_time)
        date_20050816 = self._createDate(self._GMT, 20050816, same_time)
        date_20050901 = self._createDate(self._GMT, 20050901, same_time)
        date_20050801 = self._createDate(self._GMT, 20050801, same_time)
        date_20050731 = self._createDate(self._GMT, 20050731, same_time)
        date_20051101 = self._createDate(self._GMT, 20051101, same_time)
        date_20051001 = self._createDate(self._GMT, 20051001, same_time)
        date_20050701 = self._createDate(self._GMT, 20050701, same_time)
        date_20050630 = self._createDate(self._GMT, 20050630, same_time)
        date_20050110 = self._createDate(self._GMT, 20050110, same_time)
        date_20060101 = self._createDate(self._GMT, 20060101, same_time)
        date_20050101 = self._createDate(self._GMT, 20050101, same_time)
        date_20041231 = self._createDate(self._GMT, 20041231, same_time)

        self.assertEqual(
            -1,
            self.__dateValidator.compareDates(value, date_20050824, self._GMT),
            "date LT",
        )
        self.assertEqual(
            0, self.__dateValidator.compareDates(value, diff_hour, self._GMT), "date EQ"
        )
        self.assertEqual(
            1,
            self.__dateValidator.compareDates(value, date_20050822, self._GMT),
            "date GT",
        )

    def testCompare_test1_decomposed(self) -> None:
        same_time = 124522
        test_date = 20050823
        diff_hour = self._createDate(self._GMT, test_date, 115922)
        value = self._createDate(self._GMT, test_date, same_time)
        date_20050824 = self._createDate(self._GMT, 20050824, same_time)
        date_20050822 = self._createDate(self._GMT, 20050822, same_time)
        date_20050830 = self._createDate(self._GMT, 20050830, same_time)
        date_20050816 = self._createDate(self._GMT, 20050816, same_time)
        date_20050901 = self._createDate(self._GMT, 20050901, same_time)
        date_20050801 = self._createDate(self._GMT, 20050801, same_time)
        date_20050731 = self._createDate(self._GMT, 20050731, same_time)
        date_20051101 = self._createDate(self._GMT, 20051101, same_time)
        date_20051001 = self._createDate(self._GMT, 20051001, same_time)
        date_20050701 = self._createDate(self._GMT, 20050701, same_time)
        date_20050630 = self._createDate(self._GMT, 20050630, same_time)
        date_20050110 = self._createDate(self._GMT, 20050110, same_time)
        date_20060101 = self._createDate(self._GMT, 20060101, same_time)
        date_20050101 = self._createDate(self._GMT, 20050101, same_time)
        date_20041231 = self._createDate(self._GMT, 20041231, same_time)

    def testCompare_test0_decomposed(self) -> None:
        same_time: int = 124522
        test_date: int = 20050823
        diff_hour: datetime.datetime = self._createDate(self._GMT, test_date, 115922)

    def testDateValidatorMethods_test41_decomposed(self) -> None:
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

        validator = DateValidator.getInstance()

        self.assertEqual(
            expected, validator.validate0(default_val), "validate(A) default"
        )
        self.assertEqual(
            expected, validator.validate4(locale_val, locale), "validate(A) locale"
        )
        self.assertEqual(
            expected, validator.validate2(pattern_val, pattern), "validate(A) pattern"
        )
        self.assertEqual(
            expected,
            validator.validate6(german_val, german_pattern, Locale.GERMAN),
            "validate(A) both",
        )
        self.assertTrue(validator.isValid0(default_val), "isValid(A) default")
        self.assertTrue(validator.isValid2(locale_val, locale), "isValid(A) locale")
        self.assertTrue(validator.isValid1(pattern_val, pattern), "isValid(A) pattern")
        self.assertTrue(
            validator.isValid3(german_val, german_pattern, Locale.GERMAN),
            "isValid(A) both",
        )
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

        zone = (
            self._EET
            if TimeZone.getDefault().getRawOffset() == self._EET.getRawOffset()
            else self._EST
        )
        expected_zone = self._createCalendar(zone, 20051231, 0).getTime()

        self.assertFalse(
            expected.getTime() == expected_zone.getTime(),
            f"default/zone same {zone}",
        )
        self.assertEqual(
            expected_zone,
            validator.validate1(default_val, zone),
            "validate(C) default",
        )
        self.assertEqual(
            expected_zone,
            validator.validate5(locale_val, locale, zone),
            "validate(C) locale",
        )
        self.assertEqual(
            expected_zone,
            validator.validate3(pattern_val, pattern, zone),
            "validate(C) pattern",
        )
        self.assertEqual(
            expected_zone,
            validator.validate7(german_val, german_pattern, Locale.GERMAN, zone),
            "validate(C) both",
        )

    def testDateValidatorMethods_test40_decomposed(self) -> None:
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
        DateValidator.getInstance()
        self.assertEqual(
            expected,
            DateValidator.getInstance().validate0(default_val),
            "validate(A) default",
        )
        DateValidator.getInstance()
        self.assertEqual(
            expected,
            DateValidator.getInstance().validate4(locale_val, locale),
            "validate(A) locale",
        )
        DateValidator.getInstance()
        self.assertEqual(
            expected,
            DateValidator.getInstance().validate2(pattern_val, pattern),
            "validate(A) pattern",
        )
        DateValidator.getInstance()
        self.assertEqual(
            expected,
            DateValidator.getInstance().validate6(
                german_val, german_pattern, Locale.GERMAN
            ),
            "validate(A) both",
        )
        DateValidator.getInstance()
        self.assertTrue(
            DateValidator.getInstance().isValid0(default_val), "isValid(A) default"
        )
        DateValidator.getInstance()
        self.assertTrue(
            DateValidator.getInstance().isValid2(locale_val, locale),
            "isValid(A) locale",
        )
        DateValidator.getInstance()
        self.assertTrue(
            DateValidator.getInstance().isValid1(pattern_val, pattern),
            "isValid(A) pattern",
        )
        DateValidator.getInstance()
        self.assertTrue(
            DateValidator.getInstance().isValid3(
                german_val, german_pattern, Locale.GERMAN
            ),
            "isValid(A) both",
        )
        DateValidator.getInstance()
        self.assertIsNone(
            DateValidator.getInstance().validate0(XXXX), "validate(B) default"
        )
        DateValidator.getInstance()
        self.assertIsNone(
            DateValidator.getInstance().validate4(XXXX, locale), "validate(B) locale"
        )
        DateValidator.getInstance()
        self.assertIsNone(
            DateValidator.getInstance().validate2(XXXX, pattern), "validate(B) pattern"
        )
        DateValidator.getInstance()
        self.assertIsNone(
            DateValidator.getInstance().validate6(
                "31 Dec 2005", german_pattern, Locale.GERMAN
            ),
            "validate(B) both",
        )
        DateValidator.getInstance()
        self.assertFalse(
            DateValidator.getInstance().isValid0(XXXX), "isValid(B) default"
        )
        DateValidator.getInstance()
        self.assertFalse(
            DateValidator.getInstance().isValid2(XXXX, locale), "isValid(B) locale"
        )
        DateValidator.getInstance()
        self.assertFalse(
            DateValidator.getInstance().isValid1(XXXX, pattern), "isValid(B) pattern"
        )
        DateValidator.getInstance()
        self.assertFalse(
            DateValidator.getInstance().isValid3(
                "31 Dec 2005", german_pattern, Locale.GERMAN
            ),
            "isValid(B) both",
        )
        zone = (
            self._EET
            if TimeZone.getDefault().getRawOffset() == self._EET.getRawOffset()
            else self._EST
        )
        expected_zone = self._createCalendar(zone, 20051231, 0).getTime()
        self.assertFalse(
            expected.getTime() == expected_zone.getTime(), f"default/zone same {zone}"
        )
        DateValidator.getInstance()
        self.assertEqual(
            expected_zone,
            DateValidator.getInstance().validate1(default_val, zone),
            "validate(C) default",
        )
        DateValidator.getInstance()
        self.assertEqual(
            expected_zone,
            DateValidator.getInstance().validate5(locale_val, locale, zone),
            "validate(C) locale",
        )
        DateValidator.getInstance()
        self.assertEqual(
            expected_zone,
            DateValidator.getInstance().validate3(pattern_val, pattern, zone),
            "validate(C) pattern",
        )

    def testDateValidatorMethods_test39_decomposed(self) -> None:
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

        # Validate using DateValidator
        validator = DateValidator.getInstance()

        self.assertEqual(
            expected, validator.validate0(default_val), "validate(A) default"
        )
        self.assertEqual(
            expected,
            validator.validate4(locale_val, locale_german),
            "validate(A) locale",
        )
        self.assertEqual(
            expected, validator.validate2(pattern_val, pattern), "validate(A) pattern"
        )
        self.assertEqual(
            expected,
            validator.validate6(german_val, german_pattern, locale_german),
            "validate(A) both",
        )

        self.assertTrue(validator.isValid0(default_val), "isValid(A) default")
        self.assertTrue(
            validator.isValid2(locale_val, locale_german), "isValid(A) locale"
        )
        self.assertTrue(validator.isValid1(pattern_val, pattern), "isValid(A) pattern")
        self.assertTrue(
            validator.isValid3(german_val, german_pattern, locale_german),
            "isValid(A) both",
        )

        self.assertIsNone(validator.validate0(XXXX), "validate(B) default")
        self.assertIsNone(
            validator.validate4(XXXX, locale_german), "validate(B) locale"
        )
        self.assertIsNone(validator.validate2(XXXX, pattern), "validate(B) pattern")
        self.assertIsNone(
            validator.validate6("31 Dec 2005", german_pattern, locale_german),
            "validate(B) both",
        )

        self.assertFalse(validator.isValid0(XXXX), "isValid(B) default")
        self.assertFalse(validator.isValid2(XXXX, locale_german), "isValid(B) locale")
        self.assertFalse(validator.isValid1(XXXX, pattern), "isValid(B) pattern")
        self.assertFalse(
            validator.isValid3("31 Dec 2005", german_pattern, locale_german),
            "isValid(B) both",
        )

        # Time zone validation
        zone = (
            self._EET
            if self._EET.utcoffset(None) == self._EST.utcoffset(None)
            else self._EST
        )
        expected_zone = self._createCalendar(zone, 20051231, 0).getTime()

        self.assertFalse(
            expected.timestamp() == expected_zone.timestamp(),
            f"default/zone same {zone}",
        )

        self.assertEqual(
            expected_zone, validator.validate1(default_val, zone), "validate(C) default"
        )
        self.assertEqual(
            expected_zone,
            validator.validate5(locale_val, locale_german, zone),
            "validate(C) locale",
        )
        self.assertEqual(
            expected_zone,
            validator.validate3(pattern_val, pattern, zone),
            "validate(C) pattern",
        )

    def testDateValidatorMethods_test38_decomposed(self) -> None:
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

        validator = DateValidator.getInstance()

        self.assertEqual(
            expected, validator.validate0(default_val), "validate(A) default"
        )
        self.assertEqual(
            expected, validator.validate4(locale_val, locale), "validate(A) locale"
        )
        self.assertEqual(
            expected, validator.validate2(pattern_val, pattern), "validate(A) pattern"
        )
        self.assertEqual(
            expected,
            validator.validate6(german_val, german_pattern, Locale.GERMAN),
            "validate(A) both",
        )
        self.assertTrue(validator.isValid0(default_val), "isValid(A) default")
        self.assertTrue(validator.isValid2(locale_val, locale), "isValid(A) locale")
        self.assertTrue(validator.isValid1(pattern_val, pattern), "isValid(A) pattern")
        self.assertTrue(
            validator.isValid3(german_val, german_pattern, Locale.GERMAN),
            "isValid(A) both",
        )
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

        zone = (
            self._EET
            if TimeZone.getDefault().getRawOffset() == self._EET.getRawOffset()
            else self._EST
        )
        expected_zone = self._createCalendar(zone, 20051231, 0).getTime()

        self.assertFalse(
            expected.getTime() == expected_zone.getTime(), f"default/zone same {zone}"
        )
        self.assertEqual(
            expected_zone, validator.validate1(default_val, zone), "validate(C) default"
        )
        self.assertEqual(
            expected_zone,
            validator.validate5(locale_val, locale, zone),
            "validate(C) locale",
        )

    def testDateValidatorMethods_test37_decomposed(self) -> None:
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

        # Validate using DateValidator
        validator = DateValidator.getInstance()

        self.assertEqual(
            expected, validator.validate0(default_val), "validate(A) default"
        )
        self.assertEqual(
            expected,
            validator.validate4(locale_val, locale_value),
            "validate(A) locale",
        )
        self.assertEqual(
            expected, validator.validate2(pattern_val, pattern), "validate(A) pattern"
        )
        self.assertEqual(
            expected,
            validator.validate6(german_val, german_pattern, locale_value),
            "validate(A) both",
        )

        self.assertTrue(validator.isValid0(default_val), "isValid(A) default")
        self.assertTrue(
            validator.isValid2(locale_val, locale_value), "isValid(A) locale"
        )
        self.assertTrue(validator.isValid1(pattern_val, pattern), "isValid(A) pattern")
        self.assertTrue(
            validator.isValid3(german_val, german_pattern, locale_value),
            "isValid(A) both",
        )

        self.assertIsNone(validator.validate0(XXXX), "validate(B) default")
        self.assertIsNone(validator.validate4(XXXX, locale_value), "validate(B) locale")
        self.assertIsNone(validator.validate2(XXXX, pattern), "validate(B) pattern")
        self.assertIsNone(
            validator.validate6("31 Dec 2005", german_pattern, locale_value),
            "validate(B) both",
        )

        self.assertFalse(validator.isValid0(XXXX), "isValid(B) default")
        self.assertFalse(validator.isValid2(XXXX, locale_value), "isValid(B) locale")
        self.assertFalse(validator.isValid1(XXXX, pattern), "isValid(B) pattern")
        self.assertFalse(
            validator.isValid3("31 Dec 2005", german_pattern, locale_value),
            "isValid(B) both",
        )

        # Time zone validation
        zone = (
            self._EET
            if self._EET.utcoffset(None) == self._EST.utcoffset(None)
            else self._EST
        )
        expected_zone = self._createCalendar(zone, 20051231, 0).getTime()

        self.assertFalse(
            expected.timestamp() == expected_zone.timestamp(),
            f"default/zone same {zone}",
        )

        self.assertEqual(
            expected_zone, validator.validate1(default_val, zone), "validate(C) default"
        )
        self.assertEqual(
            expected_zone,
            validator.validate5(locale_val, locale_value, zone),
            "validate(C) locale",
        )

    def testDateValidatorMethods_test36_decomposed(self) -> None:
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

        # Validate using DateValidator
        validator = DateValidator.getInstance()

        self.assertEqual(
            expected, validator.validate0(default_val), "validate(A) default"
        )
        self.assertEqual(
            expected,
            validator.validate4(locale_val, locale_value),
            "validate(A) locale",
        )
        self.assertEqual(
            expected, validator.validate2(pattern_val, pattern), "validate(A) pattern"
        )
        self.assertEqual(
            expected,
            validator.validate6(german_val, german_pattern, locale_value),
            "validate(A) both",
        )

        self.assertTrue(validator.isValid0(default_val), "isValid(A) default")
        self.assertTrue(
            validator.isValid2(locale_val, locale_value), "isValid(A) locale"
        )
        self.assertTrue(validator.isValid1(pattern_val, pattern), "isValid(A) pattern")
        self.assertTrue(
            validator.isValid3(german_val, german_pattern, locale_value),
            "isValid(A) both",
        )

        self.assertIsNone(validator.validate0(XXXX), "validate(B) default")
        self.assertIsNone(validator.validate4(XXXX, locale_value), "validate(B) locale")
        self.assertIsNone(validator.validate2(XXXX, pattern), "validate(B) pattern")
        self.assertIsNone(
            validator.validate6("31 Dec 2005", german_pattern, locale_value),
            "validate(B) both",
        )

        self.assertFalse(validator.isValid0(XXXX), "isValid(B) default")
        self.assertFalse(validator.isValid2(XXXX, locale_value), "isValid(B) locale")
        self.assertFalse(validator.isValid1(XXXX, pattern), "isValid(B) pattern")
        self.assertFalse(
            validator.isValid3("31 Dec 2005", german_pattern, locale_value),
            "isValid(B) both",
        )

        # Time zone validation
        zone = (
            self._EET
            if self._EET.utcoffset(None) == self._EST.utcoffset(None)
            else self._EST
        )
        expected_zone = self._createCalendar(zone, 20051231, 0).getTime()

        self.assertFalse(
            expected.timestamp() == expected_zone.timestamp(),
            f"default/zone same {zone}",
        )
        self.assertEqual(
            expected_zone, validator.validate1(default_val, zone), "validate(C) default"
        )

    def testDateValidatorMethods_test35_decomposed(self) -> None:
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
        DateValidator.getInstance()
        self.assertEqual(
            expected,
            DateValidator.getInstance().validate0(default_val),
            "validate(A) default",
        )
        DateValidator.getInstance()
        self.assertEqual(
            expected,
            DateValidator.getInstance().validate4(locale_val, locale),
            "validate(A) locale",
        )
        DateValidator.getInstance()
        self.assertEqual(
            expected,
            DateValidator.getInstance().validate2(pattern_val, pattern),
            "validate(A) pattern",
        )
        DateValidator.getInstance()
        self.assertEqual(
            expected,
            DateValidator.getInstance().validate6(
                german_val, german_pattern, Locale.GERMAN
            ),
            "validate(A) both",
        )
        DateValidator.getInstance()
        self.assertTrue(
            DateValidator.getInstance().isValid0(default_val), "isValid(A) default"
        )
        DateValidator.getInstance()
        self.assertTrue(
            DateValidator.getInstance().isValid2(locale_val, locale),
            "isValid(A) locale",
        )
        DateValidator.getInstance()
        self.assertTrue(
            DateValidator.getInstance().isValid1(pattern_val, pattern),
            "isValid(A) pattern",
        )
        DateValidator.getInstance()
        self.assertTrue(
            DateValidator.getInstance().isValid3(
                german_val, german_pattern, Locale.GERMAN
            ),
            "isValid(A) both",
        )
        DateValidator.getInstance()
        self.assertIsNone(
            DateValidator.getInstance().validate0(XXXX), "validate(B) default"
        )
        DateValidator.getInstance()
        self.assertIsNone(
            DateValidator.getInstance().validate4(XXXX, locale), "validate(B) locale"
        )
        DateValidator.getInstance()
        self.assertIsNone(
            DateValidator.getInstance().validate2(XXXX, pattern), "validate(B) pattern"
        )
        DateValidator.getInstance()
        self.assertIsNone(
            DateValidator.getInstance().validate6(
                "31 Dec 2005", german_pattern, Locale.GERMAN
            ),
            "validate(B) both",
        )
        DateValidator.getInstance()
        self.assertFalse(
            DateValidator.getInstance().isValid0(XXXX), "isValid(B) default"
        )
        DateValidator.getInstance()
        self.assertFalse(
            DateValidator.getInstance().isValid2(XXXX, locale), "isValid(B) locale"
        )
        DateValidator.getInstance()
        self.assertFalse(
            DateValidator.getInstance().isValid1(XXXX, pattern), "isValid(B) pattern"
        )
        DateValidator.getInstance()
        self.assertFalse(
            DateValidator.getInstance().isValid3(
                "31 Dec 2005", german_pattern, Locale.GERMAN
            ),
            "isValid(B) both",
        )
        zone = (
            self._EET
            if TimeZone.getDefault().getRawOffset() == self._EET.getRawOffset()
            else self._EST
        )
        expected_zone = self._createCalendar(zone, 20051231, 0).getTime()
        self.assertFalse(
            expected.getTime() == expected_zone.getTime(), f"default/zone same {zone}"
        )
        DateValidator.getInstance()
        self.assertEqual(
            expected_zone,
            DateValidator.getInstance().validate1(default_val, zone),
            "validate(C) default",
        )

    def testDateValidatorMethods_test34_decomposed(self) -> None:
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

        # Validate using DateValidator
        validator = DateValidator.getInstance()

        self.assertEqual(
            expected, validator.validate0(default_val), "validate(A) default"
        )
        self.assertEqual(
            expected,
            validator.validate4(locale_val, locale_value),
            "validate(A) locale",
        )
        self.assertEqual(
            expected, validator.validate2(pattern_val, pattern), "validate(A) pattern"
        )
        self.assertEqual(
            expected,
            validator.validate6(german_val, german_pattern, locale_value),
            "validate(A) both",
        )

        self.assertTrue(validator.isValid0(default_val), "isValid(A) default")
        self.assertTrue(
            validator.isValid2(locale_val, locale_value), "isValid(A) locale"
        )
        self.assertTrue(validator.isValid1(pattern_val, pattern), "isValid(A) pattern")
        self.assertTrue(
            validator.isValid3(german_val, german_pattern, locale_value),
            "isValid(A) both",
        )

        self.assertIsNone(validator.validate0(XXXX), "validate(B) default")
        self.assertIsNone(validator.validate4(XXXX, locale_value), "validate(B) locale")
        self.assertIsNone(validator.validate2(XXXX, pattern), "validate(B) pattern")
        self.assertIsNone(
            validator.validate6("31 Dec 2005", german_pattern, locale_value),
            "validate(B) both",
        )

        self.assertFalse(validator.isValid0(XXXX), "isValid(B) default")
        self.assertFalse(validator.isValid2(XXXX, locale_value), "isValid(B) locale")
        self.assertFalse(validator.isValid1(XXXX, pattern), "isValid(B) pattern")
        self.assertFalse(
            validator.isValid3("31 Dec 2005", german_pattern, locale_value),
            "isValid(B) both",
        )

        # Time zone comparison
        zone = (
            self._EET
            if self._EET.utcoffset(None) == self._EST.utcoffset(None)
            else self._EST
        )
        expected_zone = self._createCalendar(zone, 20051231, 0).getTime()

        self.assertFalse(
            expected.timestamp() == expected_zone.timestamp(),
            f"default/zone same {zone}",
        )

    def testDateValidatorMethods_test33_decomposed(self) -> None:
        import locale
        from datetime import datetime

        # Set default locale
        locale.setlocale(locale.LC_ALL, "en_US")

        # Define variables
        locale_german = "de_DE"
        pattern = "yyyy-MM-dd"
        pattern_val = "2005-12-31"
        german_val = "31 Dez 2005"
        german_pattern = "dd MMM yyyy"
        locale_val = "31.12.2005"
        default_val = "12/31/05"
        XXXX = "XXXX"
        expected = self._createCalendar(None, 20051231, 0).getTime()

        # Get DateValidator instance
        validator = DateValidator.getInstance()

        # Assertions for validate methods
        self.assertEqual(
            expected, validator.validate0(default_val), "validate(A) default"
        )
        self.assertEqual(
            expected,
            validator.validate4(locale_val, locale_german),
            "validate(A) locale",
        )
        self.assertEqual(
            expected, validator.validate2(pattern_val, pattern), "validate(A) pattern"
        )
        self.assertEqual(
            expected,
            validator.validate6(german_val, german_pattern, locale_german),
            "validate(A) both",
        )

        # Assertions for isValid methods
        self.assertTrue(validator.isValid0(default_val), "isValid(A) default")
        self.assertTrue(
            validator.isValid2(locale_val, locale_german), "isValid(A) locale"
        )
        self.assertTrue(validator.isValid1(pattern_val, pattern), "isValid(A) pattern")
        self.assertTrue(
            validator.isValid3(german_val, german_pattern, locale_german),
            "isValid(A) both",
        )

        # Assertions for invalid inputs
        self.assertIsNone(validator.validate0(XXXX), "validate(B) default")
        self.assertIsNone(
            validator.validate4(XXXX, locale_german), "validate(B) locale"
        )
        self.assertIsNone(validator.validate2(XXXX, pattern), "validate(B) pattern")
        self.assertIsNone(
            validator.validate6("31 Dec 2005", german_pattern, locale_german),
            "validate(B) both",
        )

        self.assertFalse(validator.isValid0(XXXX), "isValid(B) default")
        self.assertFalse(validator.isValid2(XXXX, locale_german), "isValid(B) locale")
        self.assertFalse(validator.isValid1(XXXX, pattern), "isValid(B) pattern")
        self.assertFalse(
            validator.isValid3("31 Dec 2005", german_pattern, locale_german),
            "isValid(B) both",
        )

        # Time zone handling
        zone = (
            self._EET
            if self._EET.utcoffset(None) == self._EST.utcoffset(None)
            else self._EST
        )
        expected_zone = self._createCalendar(zone, 20051231, 0).getTime()

    def testDateValidatorMethods_test32_decomposed(self) -> None:
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

        # Validate default
        self.assertEqual(
            expected,
            DateValidator.getInstance().validate0(default_val),
            "validate(A) default",
        )

        # Validate locale
        self.assertEqual(
            expected,
            DateValidator.getInstance().validate4(locale_val, locale_value),
            "validate(A) locale",
        )

        # Validate pattern
        self.assertEqual(
            expected,
            DateValidator.getInstance().validate2(pattern_val, pattern),
            "validate(A) pattern",
        )

        # Validate both
        self.assertEqual(
            expected,
            DateValidator.getInstance().validate6(
                german_val, german_pattern, locale_value
            ),
            "validate(A) both",
        )

        # Check isValid for default
        self.assertTrue(
            DateValidator.getInstance().isValid0(default_val), "isValid(A) default"
        )

        # Check isValid for locale
        self.assertTrue(
            DateValidator.getInstance().isValid2(locale_val, locale_value),
            "isValid(A) locale",
        )

        # Check isValid for pattern
        self.assertTrue(
            DateValidator.getInstance().isValid1(pattern_val, pattern),
            "isValid(A) pattern",
        )

        # Check isValid for both
        self.assertTrue(
            DateValidator.getInstance().isValid3(
                german_val, german_pattern, locale_value
            ),
            "isValid(A) both",
        )

        # Validate default with invalid input
        self.assertIsNone(
            DateValidator.getInstance().validate0(XXXX), "validate(B) default"
        )

        # Validate locale with invalid input
        self.assertIsNone(
            DateValidator.getInstance().validate4(XXXX, locale_value),
            "validate(B) locale",
        )

        # Validate pattern with invalid input
        self.assertIsNone(
            DateValidator.getInstance().validate2(XXXX, pattern), "validate(B) pattern"
        )

        # Validate both with invalid input
        self.assertIsNone(
            DateValidator.getInstance().validate6(
                "31 Dec 2005", german_pattern, locale_value
            ),
            "validate(B) both",
        )

        # Check isValid for default with invalid input
        self.assertFalse(
            DateValidator.getInstance().isValid0(XXXX), "isValid(B) default"
        )

        # Check isValid for locale with invalid input
        self.assertFalse(
            DateValidator.getInstance().isValid2(XXXX, locale_value),
            "isValid(B) locale",
        )

        # Check isValid for pattern with invalid input
        self.assertFalse(
            DateValidator.getInstance().isValid1(XXXX, pattern), "isValid(B) pattern"
        )

        # Check isValid for both with invalid input
        self.assertFalse(
            DateValidator.getInstance().isValid3(
                "31 Dec 2005", german_pattern, locale_value
            ),
            "isValid(B) both",
        )

    def testDateValidatorMethods_test31_decomposed(self) -> None:
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

        # Validate using default
        self.assertEqual(
            expected,
            DateValidator.getInstance().validate0(default_val),
            "validate(A) default",
        )

        # Validate using locale
        self.assertEqual(
            expected,
            DateValidator.getInstance().validate4(locale_val, locale),
            "validate(A) locale",
        )

        # Validate using pattern
        self.assertEqual(
            expected,
            DateValidator.getInstance().validate2(pattern_val, pattern),
            "validate(A) pattern",
        )

        # Validate using both pattern and locale
        self.assertEqual(
            expected,
            DateValidator.getInstance().validate6(
                german_val, german_pattern, Locale.GERMAN
            ),
            "validate(A) both",
        )

        # Check validity using default
        self.assertTrue(
            DateValidator.getInstance().isValid0(default_val), "isValid(A) default"
        )

        # Check validity using locale
        self.assertTrue(
            DateValidator.getInstance().isValid2(locale_val, locale),
            "isValid(A) locale",
        )

        # Check validity using pattern
        self.assertTrue(
            DateValidator.getInstance().isValid1(pattern_val, pattern),
            "isValid(A) pattern",
        )

        # Check validity using both pattern and locale
        self.assertTrue(
            DateValidator.getInstance().isValid3(
                german_val, german_pattern, Locale.GERMAN
            ),
            "isValid(A) both",
        )

        # Validate invalid input using default
        self.assertIsNone(
            DateValidator.getInstance().validate0(XXXX), "validate(B) default"
        )

        # Validate invalid input using locale
        self.assertIsNone(
            DateValidator.getInstance().validate4(XXXX, locale), "validate(B) locale"
        )

        # Validate invalid input using pattern
        self.assertIsNone(
            DateValidator.getInstance().validate2(XXXX, pattern), "validate(B) pattern"
        )

        # Validate invalid input using both pattern and locale
        self.assertIsNone(
            DateValidator.getInstance().validate6(
                "31 Dec 2005", german_pattern, Locale.GERMAN
            ),
            "validate(B) both",
        )

        # Check invalidity using default
        self.assertFalse(
            DateValidator.getInstance().isValid0(XXXX), "isValid(B) default"
        )

        # Check invalidity using locale
        self.assertFalse(
            DateValidator.getInstance().isValid2(XXXX, locale), "isValid(B) locale"
        )

        # Check invalidity using pattern
        self.assertFalse(
            DateValidator.getInstance().isValid1(XXXX, pattern), "isValid(B) pattern"
        )

    def testDateValidatorMethods_test30_decomposed(self) -> None:
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

        validator = DateValidator.getInstance()

        self.assertEqual(
            expected, validator.validate0(default_val), "validate(A) default"
        )
        self.assertEqual(
            expected, validator.validate4(locale_val, locale), "validate(A) locale"
        )
        self.assertEqual(
            expected, validator.validate2(pattern_val, pattern), "validate(A) pattern"
        )
        self.assertEqual(
            expected,
            validator.validate6(german_val, german_pattern, Locale.GERMAN),
            "validate(A) both",
        )
        self.assertTrue(validator.isValid0(default_val), "isValid(A) default")
        self.assertTrue(validator.isValid2(locale_val, locale), "isValid(A) locale")
        self.assertTrue(validator.isValid1(pattern_val, pattern), "isValid(A) pattern")
        self.assertTrue(
            validator.isValid3(german_val, german_pattern, Locale.GERMAN),
            "isValid(A) both",
        )
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

    def testDateValidatorMethods_test29_decomposed(self) -> None:
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

        validator = DateValidator.getInstance()

        self.assertEqual(
            expected, validator.validate0(default_val), "validate(A) default"
        )
        self.assertEqual(
            expected, validator.validate4(locale_val, locale), "validate(A) locale"
        )
        self.assertEqual(
            expected, validator.validate2(pattern_val, pattern), "validate(A) pattern"
        )
        self.assertEqual(
            expected,
            validator.validate6(german_val, german_pattern, Locale.GERMAN),
            "validate(A) both",
        )
        self.assertTrue(validator.isValid0(default_val), "isValid(A) default")
        self.assertTrue(validator.isValid2(locale_val, locale), "isValid(A) locale")
        self.assertTrue(validator.isValid1(pattern_val, pattern), "isValid(A) pattern")
        self.assertTrue(
            validator.isValid3(german_val, german_pattern, Locale.GERMAN),
            "isValid(A) both",
        )
        self.assertIsNone(validator.validate0(XXXX), "validate(B) default")
        self.assertIsNone(validator.validate4(XXXX, locale), "validate(B) locale")
        self.assertIsNone(validator.validate2(XXXX, pattern), "validate(B) pattern")
        self.assertIsNone(
            validator.validate6("31 Dec 2005", german_pattern, Locale.GERMAN),
            "validate(B) both",
        )
        self.assertFalse(validator.isValid0(XXXX), "isValid(B) default")
        self.assertFalse(validator.isValid2(XXXX, locale), "isValid(B) locale")

    def testDateValidatorMethods_test28_decomposed(self) -> None:
        import locale

        locale.setlocale(locale.LC_ALL, "en_US")  # Set default locale to US
        test_locale = "de_DE"  # German locale
        pattern = "yyyy-MM-dd"
        pattern_val = "2005-12-31"
        german_val = "31 Dez 2005"
        german_pattern = "dd MMM yyyy"
        locale_val = "31.12.2005"
        default_val = "12/31/05"
        XXXX = "XXXX"
        expected = self._createCalendar(None, 20051231, 0).getTime()

        validator = DateValidator.getInstance()

        # Validate default
        self.assertEqual(
            expected, validator.validate0(default_val), "validate(A) default"
        )

        # Validate with locale
        self.assertEqual(
            expected, validator.validate4(locale_val, test_locale), "validate(A) locale"
        )

        # Validate with pattern
        self.assertEqual(
            expected, validator.validate2(pattern_val, pattern), "validate(A) pattern"
        )

        # Validate with both pattern and locale
        self.assertEqual(
            expected,
            validator.validate6(german_val, german_pattern, test_locale),
            "validate(A) both",
        )

        # Check isValid for default
        self.assertTrue(validator.isValid0(default_val), "isValid(A) default")

        # Check isValid with locale
        self.assertTrue(
            validator.isValid2(locale_val, test_locale), "isValid(A) locale"
        )

        # Check isValid with pattern
        self.assertTrue(validator.isValid1(pattern_val, pattern), "isValid(A) pattern")

        # Check isValid with both pattern and locale
        self.assertTrue(
            validator.isValid3(german_val, german_pattern, test_locale),
            "isValid(A) both",
        )

        # Validate invalid default
        self.assertIsNone(validator.validate0(XXXX), "validate(B) default")

        # Validate invalid locale
        self.assertIsNone(validator.validate4(XXXX, test_locale), "validate(B) locale")

        # Validate invalid pattern
        self.assertIsNone(validator.validate2(XXXX, pattern), "validate(B) pattern")

        # Validate invalid both pattern and locale
        self.assertIsNone(
            validator.validate6("31 Dec 2005", german_pattern, test_locale),
            "validate(B) both",
        )

        # Check isValid for invalid default
        self.assertFalse(validator.isValid0(XXXX), "isValid(B) default")

        # Check isValid for invalid locale
        self.assertFalse(validator.isValid2(XXXX, test_locale), "isValid(B) locale")

    def testDateValidatorMethods_test27_decomposed(self) -> None:
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

        validator = DateValidator.getInstance()

        self.assertEqual(
            expected, validator.validate0(default_val), "validate(A) default"
        )
        self.assertEqual(
            expected, validator.validate4(locale_val, locale), "validate(A) locale"
        )
        self.assertEqual(
            expected, validator.validate2(pattern_val, pattern), "validate(A) pattern"
        )
        self.assertEqual(
            expected,
            validator.validate6(german_val, german_pattern, Locale.GERMAN),
            "validate(A) both",
        )
        self.assertTrue(validator.isValid0(default_val), "isValid(A) default")
        self.assertTrue(validator.isValid2(locale_val, locale), "isValid(A) locale")
        self.assertTrue(validator.isValid1(pattern_val, pattern), "isValid(A) pattern")
        self.assertTrue(
            validator.isValid3(german_val, german_pattern, Locale.GERMAN),
            "isValid(A) both",
        )
        self.assertIsNone(validator.validate0(XXXX), "validate(B) default")
        self.assertIsNone(validator.validate4(XXXX, locale), "validate(B) locale")
        self.assertIsNone(validator.validate2(XXXX, pattern), "validate(B) pattern")
        self.assertIsNone(
            validator.validate6("31 Dec 2005", german_pattern, Locale.GERMAN),
            "validate(B) both",
        )
        self.assertFalse(validator.isValid0(XXXX), "isValid(B) default")

    def testDateValidatorMethods_test26_decomposed(self) -> None:
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

        validator = DateValidator.getInstance()

        self.assertEqual(
            expected, validator.validate0(default_val), "validate(A) default"
        )
        self.assertEqual(
            expected, validator.validate4(locale_val, locale), "validate(A) locale"
        )
        self.assertEqual(
            expected, validator.validate2(pattern_val, pattern), "validate(A) pattern"
        )
        self.assertEqual(
            expected,
            validator.validate6(german_val, german_pattern, Locale.GERMAN),
            "validate(A) both",
        )
        self.assertTrue(validator.isValid0(default_val), "isValid(A) default")
        self.assertTrue(validator.isValid2(locale_val, locale), "isValid(A) locale")
        self.assertTrue(validator.isValid1(pattern_val, pattern), "isValid(A) pattern")
        self.assertTrue(
            validator.isValid3(german_val, german_pattern, Locale.GERMAN),
            "isValid(A) both",
        )
        self.assertIsNone(validator.validate0(XXXX), "validate(B) default")
        self.assertIsNone(validator.validate4(XXXX, locale), "validate(B) locale")
        self.assertIsNone(validator.validate2(XXXX, pattern), "validate(B) pattern")
        self.assertIsNone(
            validator.validate6("31 Dec 2005", german_pattern, Locale.GERMAN),
            "validate(B) both",
        )
        self.assertFalse(validator.isValid0(XXXX), "isValid(B) default")

    def testDateValidatorMethods_test25_decomposed(self) -> None:
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

        validator = DateValidator.getInstance()

        self.assertEqual(
            expected, validator.validate0(default_val), "validate(A) default"
        )
        self.assertEqual(
            expected, validator.validate4(locale_val, locale), "validate(A) locale"
        )
        self.assertEqual(
            expected, validator.validate2(pattern_val, pattern), "validate(A) pattern"
        )
        self.assertEqual(
            expected,
            validator.validate6(german_val, german_pattern, Locale.GERMAN),
            "validate(A) both",
        )
        self.assertTrue(validator.isValid0(default_val), "isValid(A) default")
        self.assertTrue(validator.isValid2(locale_val, locale), "isValid(A) locale")
        self.assertTrue(validator.isValid1(pattern_val, pattern), "isValid(A) pattern")
        self.assertTrue(
            validator.isValid3(german_val, german_pattern, Locale.GERMAN),
            "isValid(A) both",
        )
        self.assertIsNone(validator.validate0(XXXX), "validate(B) default")
        self.assertIsNone(validator.validate4(XXXX, locale), "validate(B) locale")
        self.assertIsNone(validator.validate2(XXXX, pattern), "validate(B) pattern")
        self.assertIsNone(
            validator.validate6("31 Dec 2005", german_pattern, Locale.GERMAN),
            "validate(B) both",
        )

    def testDateValidatorMethods_test24_decomposed(self) -> None:
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
        self.assertEqual(
            expected,
            DateValidator.getInstance().validate0(default_val),
            "validate(A) default",
        )

        # Validate with locale
        self.assertEqual(
            expected,
            DateValidator.getInstance().validate4(locale_val, locale),
            "validate(A) locale",
        )

        # Validate with pattern
        self.assertEqual(
            expected,
            DateValidator.getInstance().validate2(pattern_val, pattern),
            "validate(A) pattern",
        )

        # Validate with both pattern and locale
        self.assertEqual(
            expected,
            DateValidator.getInstance().validate6(
                german_val, german_pattern, Locale.GERMAN
            ),
            "validate(A) both",
        )

        # Check validity for default
        self.assertTrue(
            DateValidator.getInstance().isValid0(default_val), "isValid(A) default"
        )

        # Check validity with locale
        self.assertTrue(
            DateValidator.getInstance().isValid2(locale_val, locale),
            "isValid(A) locale",
        )

        # Check validity with pattern
        self.assertTrue(
            DateValidator.getInstance().isValid1(pattern_val, pattern),
            "isValid(A) pattern",
        )

        # Check validity with both pattern and locale
        self.assertTrue(
            DateValidator.getInstance().isValid3(
                german_val, german_pattern, Locale.GERMAN
            ),
            "isValid(A) both",
        )

        # Validate invalid default
        self.assertIsNone(
            DateValidator.getInstance().validate0(XXXX), "validate(B) default"
        )

        # Validate invalid locale
        self.assertIsNone(
            DateValidator.getInstance().validate4(XXXX, locale), "validate(B) locale"
        )

        # Validate invalid pattern
        self.assertIsNone(
            DateValidator.getInstance().validate2(XXXX, pattern), "validate(B) pattern"
        )

        # Validate invalid both pattern and locale
        self.assertIsNone(
            DateValidator.getInstance().validate6(
                "31 Dec 2005", german_pattern, Locale.GERMAN
            ),
            "validate(B) both",
        )

    def testDateValidatorMethods_test23_decomposed(self) -> None:
        # Set default locale to US
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

        # Validate using default format
        self.assertEqual(
            expected,
            DateValidator.getInstance().validate0(default_val),
            "validate(A) default",
        )

        # Validate using locale
        self.assertEqual(
            expected,
            DateValidator.getInstance().validate4(locale_val, locale),
            "validate(A) locale",
        )

        # Validate using pattern
        self.assertEqual(
            expected,
            DateValidator.getInstance().validate2(pattern_val, pattern),
            "validate(A) pattern",
        )

        # Validate using both pattern and locale
        self.assertEqual(
            expected,
            DateValidator.getInstance().validate6(
                german_val, german_pattern, Locale.GERMAN
            ),
            "validate(A) both",
        )

        # Check validity using default format
        self.assertTrue(
            DateValidator.getInstance().isValid0(default_val), "isValid(A) default"
        )

        # Check validity using locale
        self.assertTrue(
            DateValidator.getInstance().isValid2(locale_val, locale),
            "isValid(A) locale",
        )

        # Check validity using pattern
        self.assertTrue(
            DateValidator.getInstance().isValid1(pattern_val, pattern),
            "isValid(A) pattern",
        )

        # Check validity using both pattern and locale
        self.assertTrue(
            DateValidator.getInstance().isValid3(
                german_val, german_pattern, Locale.GERMAN
            ),
            "isValid(A) both",
        )

        # Validate invalid input using default format
        self.assertIsNone(
            DateValidator.getInstance().validate0(XXXX), "validate(B) default"
        )

        # Validate invalid input using locale
        self.assertIsNone(
            DateValidator.getInstance().validate4(XXXX, locale), "validate(B) locale"
        )

        # Validate invalid input using pattern
        self.assertIsNone(
            DateValidator.getInstance().validate2(XXXX, pattern), "validate(B) pattern"
        )

    def testDateValidatorMethods_test22_decomposed(self) -> None:
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

        validator = DateValidator.getInstance()

        self.assertEqual(
            expected, validator.validate0(default_val), "validate(A) default"
        )
        self.assertEqual(
            expected, validator.validate4(locale_val, locale), "validate(A) locale"
        )
        self.assertEqual(
            expected, validator.validate2(pattern_val, pattern), "validate(A) pattern"
        )
        self.assertEqual(
            expected,
            validator.validate6(german_val, german_pattern, Locale.GERMAN),
            "validate(A) both",
        )
        self.assertTrue(validator.isValid0(default_val), "isValid(A) default")
        self.assertTrue(validator.isValid2(locale_val, locale), "isValid(A) locale")
        self.assertTrue(validator.isValid1(pattern_val, pattern), "isValid(A) pattern")
        self.assertTrue(
            validator.isValid3(german_val, german_pattern, Locale.GERMAN),
            "isValid(A) both",
        )
        self.assertIsNone(validator.validate0(XXXX), "validate(B) default")
        self.assertIsNone(validator.validate4(XXXX, locale), "validate(B) locale")
        self.assertIsNone(validator.validate2(XXXX, pattern), "validate(B) pattern")

    def testDateValidatorMethods_test21_decomposed(self) -> None:
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

        validator = DateValidator.getInstance()

        self.assertEqual(
            expected, validator.validate0(default_val), "validate(A) default"
        )
        self.assertEqual(
            expected, validator.validate4(locale_val, locale), "validate(A) locale"
        )
        self.assertEqual(
            expected, validator.validate2(pattern_val, pattern), "validate(A) pattern"
        )
        self.assertEqual(
            expected,
            validator.validate6(german_val, german_pattern, Locale.GERMAN),
            "validate(A) both",
        )
        self.assertTrue(validator.isValid0(default_val), "isValid(A) default")
        self.assertTrue(validator.isValid2(locale_val, locale), "isValid(A) locale")
        self.assertTrue(validator.isValid1(pattern_val, pattern), "isValid(A) pattern")
        self.assertTrue(
            validator.isValid3(german_val, german_pattern, Locale.GERMAN),
            "isValid(A) both",
        )
        self.assertIsNone(validator.validate0(XXXX), "validate(B) default")
        self.assertIsNone(validator.validate4(XXXX, locale), "validate(B) locale")

    def testDateValidatorMethods_test20_decomposed(self) -> None:
        # Set default locale to US
        locale.setlocale(locale.LC_TIME, "en_US.UTF-8")

        # Define variables
        locale_value = locale.getlocale(locale.LC_TIME)
        german_locale = "de_DE.UTF-8"
        pattern = "yyyy-MM-dd"
        pattern_val = "2005-12-31"
        german_val = "31 Dez 2005"
        german_pattern = "dd MMM yyyy"
        locale_val = "31.12.2005"
        default_val = "12/31/05"
        XXXX = "XXXX"
        expected = self._createCalendar(None, 20051231, 0).date()

        # Get DateValidator instance
        validator = DateValidator.getInstance()

        # Assertions for validate methods
        self.assertEqual(
            expected, validator.validate0(default_val), "validate(A) default"
        )
        self.assertEqual(
            expected,
            validator.validate4(locale_val, german_locale),
            "validate(A) locale",
        )
        self.assertEqual(
            expected, validator.validate2(pattern_val, pattern), "validate(A) pattern"
        )
        self.assertEqual(
            expected,
            validator.validate6(german_val, german_pattern, german_locale),
            "validate(A) both",
        )

        # Assertions for isValid methods
        self.assertTrue(validator.isValid0(default_val), "isValid(A) default")
        self.assertTrue(
            validator.isValid2(locale_val, german_locale), "isValid(A) locale"
        )
        self.assertTrue(validator.isValid1(pattern_val, pattern), "isValid(A) pattern")
        self.assertTrue(
            validator.isValid3(german_val, german_pattern, german_locale),
            "isValid(A) both",
        )

        # Assertions for invalid cases
        self.assertIsNone(validator.validate0(XXXX), "validate(B) default")
        self.assertIsNone(
            validator.validate4(XXXX, german_locale), "validate(B) locale"
        )

    def testDateValidatorMethods_test19_decomposed(self) -> None:
        import locale
        from datetime import datetime

        # Set default locale to US
        locale.setlocale(locale.LC_ALL, "en_US")

        # Define variables
        locale_german = "de_DE"
        pattern = "yyyy-MM-dd"
        pattern_val = "2005-12-31"
        german_val = "31 Dez 2005"
        german_pattern = "dd MMM yyyy"
        locale_val = "31.12.2005"
        default_val = "12/31/05"
        XXXX = "XXXX"
        expected = self._createCalendar(None, 20051231, 0).getTime()

        # Get DateValidator instance
        validator = DateValidator.getInstance()

        # Assertions
        self.assertEqual(
            expected, validator.validate0(default_val), "validate(A) default"
        )
        self.assertEqual(
            expected,
            validator.validate4(locale_val, locale_german),
            "validate(A) locale",
        )
        self.assertEqual(
            expected, validator.validate2(pattern_val, pattern), "validate(A) pattern"
        )
        self.assertEqual(
            expected,
            validator.validate6(german_val, german_pattern, locale_german),
            "validate(A) both",
        )
        self.assertTrue(validator.isValid0(default_val), "isValid(A) default")
        self.assertTrue(
            validator.isValid2(locale_val, locale_german), "isValid(A) locale"
        )
        self.assertTrue(validator.isValid1(pattern_val, pattern), "isValid(A) pattern")
        self.assertTrue(
            validator.isValid3(german_val, german_pattern, locale_german),
            "isValid(A) both",
        )
        self.assertIsNone(validator.validate0(XXXX), "validate(B) default")

    def testDateValidatorMethods_test18_decomposed(self) -> None:
        # Set default locale to US
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

        # Validate using default format
        self.assertEqual(
            expected,
            DateValidator.getInstance().validate0(default_val),
            "validate(A) default",
        )

        # Validate using locale
        self.assertEqual(
            expected,
            DateValidator.getInstance().validate4(locale_val, locale),
            "validate(A) locale",
        )

        # Validate using pattern
        self.assertEqual(
            expected,
            DateValidator.getInstance().validate2(pattern_val, pattern),
            "validate(A) pattern",
        )

        # Validate using both pattern and locale
        self.assertEqual(
            expected,
            DateValidator.getInstance().validate6(
                german_val, german_pattern, Locale.GERMAN
            ),
            "validate(A) both",
        )

        # Check validity using default format
        self.assertTrue(
            DateValidator.getInstance().isValid0(default_val), "isValid(A) default"
        )

        # Check validity using locale
        self.assertTrue(
            DateValidator.getInstance().isValid2(locale_val, locale),
            "isValid(A) locale",
        )

        # Check validity using pattern
        self.assertTrue(
            DateValidator.getInstance().isValid1(pattern_val, pattern),
            "isValid(A) pattern",
        )

        # Check validity using both pattern and locale
        self.assertTrue(
            DateValidator.getInstance().isValid3(
                german_val, german_pattern, Locale.GERMAN
            ),
            "isValid(A) both",
        )

        # Validate an invalid value
        self.assertIsNone(
            DateValidator.getInstance().validate0(XXXX), "validate(B) default"
        )

    def testDateValidatorMethods_test17_decomposed(self) -> None:
        # Set the default locale to US
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

        # Validate using default format
        self.assertEqual(
            expected,
            DateValidator.getInstance().validate0(default_val),
            "validate(A) default",
        )

        # Validate using locale
        self.assertEqual(
            expected,
            DateValidator.getInstance().validate4(locale_val, locale),
            "validate(A) locale",
        )

        # Validate using pattern
        self.assertEqual(
            expected,
            DateValidator.getInstance().validate2(pattern_val, pattern),
            "validate(A) pattern",
        )

        # Validate using both pattern and locale
        self.assertEqual(
            expected,
            DateValidator.getInstance().validate6(
                german_val, german_pattern, Locale.GERMAN
            ),
            "validate(A) both",
        )

        # Check validity using default format
        self.assertTrue(
            DateValidator.getInstance().isValid0(default_val), "isValid(A) default"
        )

        # Check validity using locale
        self.assertTrue(
            DateValidator.getInstance().isValid2(locale_val, locale),
            "isValid(A) locale",
        )

        # Check validity using pattern
        self.assertTrue(
            DateValidator.getInstance().isValid1(pattern_val, pattern),
            "isValid(A) pattern",
        )

        # Check validity using both pattern and locale
        self.assertTrue(
            DateValidator.getInstance().isValid3(
                german_val, german_pattern, Locale.GERMAN
            ),
            "isValid(A) both",
        )

    def testDateValidatorMethods_test16_decomposed(self) -> None:
        import locale
        from datetime import datetime

        # Set default locale to US
        locale.setlocale(locale.LC_ALL, "en_US")

        # Define variables
        locale_german = "de_DE"
        pattern = "yyyy-MM-dd"
        pattern_val = "2005-12-31"
        german_val = "31 Dez 2005"
        german_pattern = "dd MMM yyyy"
        locale_val = "31.12.2005"
        default_val = "12/31/05"
        XXXX = "XXXX"
        expected = self._createCalendar(None, 20051231, 0).getTime()

        # Get DateValidator instance
        validator = DateValidator.getInstance()

        # Assertions
        self.assertEqual(
            expected, validator.validate0(default_val), "validate(A) default"
        )
        self.assertEqual(
            expected,
            validator.validate4(locale_val, locale_german),
            "validate(A) locale",
        )
        self.assertEqual(
            expected, validator.validate2(pattern_val, pattern), "validate(A) pattern"
        )
        self.assertEqual(
            expected,
            validator.validate6(german_val, german_pattern, locale_german),
            "validate(A) both",
        )
        self.assertTrue(validator.isValid0(default_val), "isValid(A) default")
        self.assertTrue(
            validator.isValid2(locale_val, locale_german), "isValid(A) locale"
        )
        self.assertTrue(validator.isValid1(pattern_val, pattern), "isValid(A) pattern")
        self.assertTrue(
            validator.isValid3(german_val, german_pattern, locale_german),
            "isValid(A) both",
        )

    def testDateValidatorMethods_test15_decomposed(self) -> None:
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
        self.assertEqual(
            expected,
            DateValidator.getInstance().validate0(default_val),
            "validate(A) default",
        )

        # Validate using locale
        self.assertEqual(
            expected,
            DateValidator.getInstance().validate4(locale_val, locale),
            "validate(A) locale",
        )

        # Validate using pattern
        self.assertEqual(
            expected,
            DateValidator.getInstance().validate2(pattern_val, pattern),
            "validate(A) pattern",
        )

        # Validate using both pattern and locale
        self.assertEqual(
            expected,
            DateValidator.getInstance().validate6(
                german_val, german_pattern, Locale.GERMAN
            ),
            "validate(A) both",
        )

        # Check validity using default format
        self.assertTrue(
            DateValidator.getInstance().isValid0(default_val), "isValid(A) default"
        )

        # Check validity using locale
        self.assertTrue(
            DateValidator.getInstance().isValid2(locale_val, locale),
            "isValid(A) locale",
        )

        # Check validity using pattern
        self.assertTrue(
            DateValidator.getInstance().isValid1(pattern_val, pattern),
            "isValid(A) pattern",
        )

    def testDateValidatorMethods_test14_decomposed(self) -> None:
        import locale
        from datetime import datetime

        # Set default locale to US
        locale.setlocale(locale.LC_ALL, "en_US")

        # Define variables
        locale_german = "de_DE"
        pattern = "yyyy-MM-dd"
        pattern_val = "2005-12-31"
        german_val = "31 Dez 2005"
        german_pattern = "dd MMM yyyy"
        locale_val = "31.12.2005"
        default_val = "12/31/05"
        XXXX = "XXXX"

        # Expected date
        expected = self._createCalendar(None, 20051231, 0).date()

        # Validate using default format
        self.assertEqual(
            expected,
            DateValidator.getInstance().validate0(default_val),
            "validate(A) default",
        )

        # Validate using locale
        self.assertEqual(
            expected,
            DateValidator.getInstance().validate4(locale_val, locale_german),
            "validate(A) locale",
        )

        # Validate using pattern
        self.assertEqual(
            expected,
            DateValidator.getInstance().validate2(pattern_val, pattern),
            "validate(A) pattern",
        )

        # Validate using both pattern and locale
        self.assertEqual(
            expected,
            DateValidator.getInstance().validate6(
                german_val, german_pattern, locale_german
            ),
            "validate(A) both",
        )

        # Check validity using default format
        self.assertTrue(
            DateValidator.getInstance().isValid0(default_val), "isValid(A) default"
        )

        # Check validity using locale
        self.assertTrue(
            DateValidator.getInstance().isValid2(locale_val, locale_german),
            "isValid(A) locale",
        )

        # Check validity using pattern
        self.assertTrue(
            DateValidator.getInstance().isValid1(pattern_val, pattern),
            "isValid(A) pattern",
        )

    def testDateValidatorMethods_test13_decomposed(self) -> None:
        # Set the default locale to US
        locale.setlocale(locale.LC_ALL, "en_US")

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
        validator = DateValidator.getInstance()
        self.assertEqual(
            expected, validator.validate0(default_val), "validate(A) default"
        )

        # Validate using locale
        self.assertEqual(
            expected,
            validator.validate4(locale_val, locale_value),
            "validate(A) locale",
        )

        # Validate using pattern
        self.assertEqual(
            expected, validator.validate2(pattern_val, pattern), "validate(A) pattern"
        )

        # Validate using both pattern and locale
        self.assertEqual(
            expected,
            validator.validate6(german_val, german_pattern, locale.GERMAN),
            "validate(A) both",
        )

        # Check validity using default pattern
        self.assertTrue(validator.isValid0(default_val), "isValid(A) default")

        # Check validity using locale
        self.assertTrue(
            validator.isValid2(locale_val, locale_value), "isValid(A) locale"
        )

    def testDateValidatorMethods_test12_decomposed(self) -> None:
        # Set the default locale to US
        locale.setlocale(locale.LC_TIME, "en_US.UTF-8")

        # Define variables
        locale_value = locale.localeconv()
        locale_german = "de_DE.UTF-8"
        pattern = "yyyy-MM-dd"
        pattern_val = "2005-12-31"
        german_val = "31 Dez 2005"
        german_pattern = "dd MMM yyyy"
        locale_val = "31.12.2005"
        default_val = "12/31/05"
        XXXX = "XXXX"

        # Expected date
        expected = self._createCalendar(None, 20051231, 0).getTime()

        # Validate using default pattern
        self.assertEqual(
            expected,
            DateValidator.getInstance().validate0(default_val),
            "validate(A) default",
        )

        # Validate using locale
        self.assertEqual(
            expected,
            DateValidator.getInstance().validate4(locale_val, locale_german),
            "validate(A) locale",
        )

        # Validate using pattern
        self.assertEqual(
            expected,
            DateValidator.getInstance().validate2(pattern_val, pattern),
            "validate(A) pattern",
        )

        # Validate using both pattern and locale
        self.assertEqual(
            expected,
            DateValidator.getInstance().validate6(
                german_val, german_pattern, locale_german
            ),
            "validate(A) both",
        )

        # Check validity using default pattern
        self.assertTrue(
            DateValidator.getInstance().isValid0(default_val), "isValid(A) default"
        )

        # Check validity using locale
        self.assertTrue(
            DateValidator.getInstance().isValid2(locale_val, locale_german),
            "isValid(A) locale",
        )

    def testDateValidatorMethods_test11_decomposed(self) -> None:
        # Set the default locale to US
        locale.setlocale(locale.LC_TIME, "en_US.UTF-8")

        # Define variables
        locale_value = locale.Locale("de_DE")  # German locale
        pattern = "yyyy-MM-dd"
        pattern_val = "2005-12-31"
        german_val = "31 Dez 2005"
        german_pattern = "dd MMM yyyy"
        locale_val = "31.12.2005"
        default_val = "12/31/05"
        XXXX = "XXXX"

        # Create the expected date
        expected = self._createCalendar(None, 20051231, 0).getTime()

        # Validate using different methods and assert results
        validator = DateValidator.getInstance()

        # Validate with default format
        self.assertEqual(
            expected, validator.validate0(default_val), "validate(A) default"
        )

        # Validate with locale
        self.assertEqual(
            expected,
            validator.validate4(locale_val, locale_value),
            "validate(A) locale",
        )

        # Validate with pattern
        self.assertEqual(
            expected, validator.validate2(pattern_val, pattern), "validate(A) pattern"
        )

        # Validate with both pattern and locale
        self.assertEqual(
            expected,
            validator.validate6(german_val, german_pattern, locale_value),
            "validate(A) both",
        )

        # Check if the default value is valid
        self.assertTrue(validator.isValid0(default_val), "isValid(A) default")

    def testDateValidatorMethods_test10_decomposed(self) -> None:
        # Set the default locale to US
        locale.setlocale(locale.LC_TIME, "en_US.UTF-8")

        # Define variables
        locale_value = locale.Locale("de_DE")  # GERMAN locale
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
        self.assertEqual(
            expected,
            DateValidator.getInstance().validate0(default_val),
            "validate(A) default",
        )

        # Validate using locale
        self.assertEqual(
            expected,
            DateValidator.getInstance().validate4(locale_val, locale_value),
            "validate(A) locale",
        )

        # Validate using pattern
        self.assertEqual(
            expected,
            DateValidator.getInstance().validate2(pattern_val, pattern),
            "validate(A) pattern",
        )

        # Validate using both pattern and locale
        self.assertEqual(
            expected,
            DateValidator.getInstance().validate6(
                german_val, german_pattern, locale_value
            ),
            "validate(A) both",
        )

        # Check if the default value is valid
        self.assertTrue(
            DateValidator.getInstance().isValid0(default_val), "isValid(A) default"
        )

    def testDateValidatorMethods_test9_decomposed(self) -> None:
        # Set the default locale to US
        locale.setlocale(locale.LC_ALL, "en_US")

        # Define variables
        locale_value = locale.Locale("de")  # Locale.GERMAN
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
        self.assertEqual(
            expected,
            DateValidator.getInstance().validate0(default_val),
            "validate(A) default",
        )

        # Validate using locale
        self.assertEqual(
            expected,
            DateValidator.getInstance().validate4(locale_val, locale_value),
            "validate(A) locale",
        )

        # Validate using pattern
        self.assertEqual(
            expected,
            DateValidator.getInstance().validate2(pattern_val, pattern),
            "validate(A) pattern",
        )

        # Validate using both pattern and locale
        self.assertEqual(
            expected,
            DateValidator.getInstance().validate6(
                german_val, german_pattern, locale_value
            ),
            "validate(A) both",
        )

    def testDateValidatorMethods_test8_decomposed(self) -> None:
        import locale
        from datetime import datetime

        # Set default locale to US
        locale.setlocale(locale.LC_ALL, "en_US")

        # Define variables
        locale_german = "de_DE"
        pattern = "yyyy-MM-dd"
        pattern_val = "2005-12-31"
        german_val = "31 Dez 2005"
        german_pattern = "dd MMM yyyy"
        locale_val = "31.12.2005"
        default_val = "12/31/05"
        XXXX = "XXXX"

        # Expected date
        expected = self._createCalendar(None, 20051231, 0).getTime()

        # Validate using default pattern
        self.assertEqual(
            expected,
            DateValidator.getInstance().validate0(default_val),
            "validate(A) default",
        )

        # Validate using locale
        self.assertEqual(
            expected,
            DateValidator.getInstance().validate4(locale_val, locale_german),
            "validate(A) locale",
        )

        # Validate using pattern
        self.assertEqual(
            expected,
            DateValidator.getInstance().validate2(pattern_val, pattern),
            "validate(A) pattern",
        )

        # Validate using both pattern and locale
        self.assertEqual(
            expected,
            DateValidator.getInstance().validate6(
                german_val, german_pattern, locale_german
            ),
            "validate(A) both",
        )

    def testDateValidatorMethods_test7_decomposed(self) -> None:
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
        validator = DateValidator.getInstance()
        self.assertEqual(
            expected, validator.validate0(default_val), "validate(A) default"
        )

        # Validate using locale
        self.assertEqual(
            expected,
            validator.validate4(locale_val, locale_value),
            "validate(A) locale",
        )

        # Validate using custom pattern
        self.assertEqual(
            expected, validator.validate2(pattern_val, pattern), "validate(A) pattern"
        )

    def testDateValidatorMethods_test6_decomposed(self) -> None:
        # Set the default locale to US
        locale.setlocale(locale.LC_TIME, "en_US")

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
        self.assertEqual(
            expected,
            DateValidator.getInstance().validate0(default_val),
            "validate(A) default",
        )

        # Validate using locale
        self.assertEqual(
            expected,
            DateValidator.getInstance().validate4(locale_val, locale_value),
            "validate(A) locale",
        )

        # Validate using custom pattern
        self.assertEqual(
            expected,
            DateValidator.getInstance().validate2(pattern_val, pattern),
            "validate(A) pattern",
        )

    def testDateValidatorMethods_test5_decomposed(self) -> None:
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

        # Validate using default pattern
        validator = DateValidator.getInstance()
        self.assertEqual(
            expected, validator.validate0(default_val), "validate(A) default"
        )

        # Validate using locale
        self.assertEqual(
            expected,
            validator.validate4(locale_val, locale_value),
            "validate(A) locale",
        )

    def testDateValidatorMethods_test4_decomposed(self) -> None:
        # Set the default locale to US
        locale.setlocale(locale.LC_ALL, "en_US")

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
        validator = DateValidator.getInstance()
        self.assertEqual(
            expected, validator.validate0(default_val), "validate(A) default"
        )

        # Validate using a specific locale
        self.assertEqual(
            expected,
            validator.validate4(locale_val, locale_value),
            "validate(A) locale",
        )

    def testDateValidatorMethods_test3_decomposed(self) -> None:
        # Set the default locale to US
        locale.setlocale(locale.LC_ALL, "en_US")

        # Define variables
        locale_value = "de_DE"  # GERMAN locale
        pattern = "yyyy-MM-dd"
        pattern_val = "2005-12-31"
        german_val = "31 Dez 2005"
        german_pattern = "dd MMM yyyy"
        locale_val = "31.12.2005"
        default_val = "12/31/05"
        XXXX = "XXXX"

        # Create the expected date
        expected = self._createCalendar(None, 20051231, 0).getTime()

        # Validate using DateValidator
        validator = DateValidator.getInstance()
        self.assertEqual(
            expected, validator.validate0(default_val), "validate(A) default"
        )

    def testDateValidatorMethods_test2_decomposed(self) -> None:
        # Set the default locale to US
        locale.setlocale(locale.LC_ALL, "en_US")

        # Define variables
        locale_value = "de_DE"  # German locale
        pattern = "yyyy-MM-dd"
        pattern_val = "2005-12-31"
        german_val = "31 Dez 2005"
        german_pattern = "dd MMM yyyy"
        locale_val = "31.12.2005"
        default_val = "12/31/05"
        XXXX = "XXXX"

        # Create the expected date
        expected = self._createCalendar(None, 20051231, 0).getTime()

        # Get the DateValidator instance
        validator = DateValidator.getInstance()

        # Assert the validation
        self.assertEqual(
            expected, validator.validate0(default_val), "validate(A) default"
        )

    def testDateValidatorMethods_test1_decomposed(self) -> None:
        import locale
        from datetime import datetime

        # Set default locale to US
        locale.setlocale(locale.LC_ALL, "en_US")

        # Define variables
        locale_lang = "de_DE"  # German locale
        pattern = "yyyy-MM-dd"
        pattern_val = "2005-12-31"
        german_val = "31 Dez 2005"
        german_pattern = "dd MMM yyyy"
        locale_val = "31.12.2005"
        default_val = "12/31/05"
        XXXX = "XXXX"

        # Expected date
        expected = self._createCalendar(None, 20051231, 0).getTime()

        # Get DateValidator instance
        DateValidator.getInstance()

    def testDateValidatorMethods_test0_decomposed(self) -> None:
        import locale
        from datetime import datetime

        # Set default locale to US
        locale.setlocale(locale.LC_ALL, "en_US")

        # Define variables
        locale_lang = "de_DE"  # German locale
        pattern = "yyyy-MM-dd"
        pattern_val = "2005-12-31"
        german_val = "31 Dez 2005"
        german_pattern = "dd MMM yyyy"
        locale_val = "31.12.2005"
        default_val = "12/31/05"
        XXXX = "XXXX"

        # Expected date
        expected = self._createCalendar(None, 20051231, 0).getTime()

    def testLocaleProviders_test2_decomposed(self) -> None:
        locale_providers = os.getenv("java.locale.providers")
        if locale_providers is not None:  # may be None before Java 9
            self.assertTrue(
                locale_providers.startswith("COMPAT"),
                "java.locale.providers must start with COMPAT",
            )

        txt = "3/20/15 10:59:00 PM"
        date_format = datetime.datetime.strptime(txt, "%m/%d/%y %I:%M:%S %p")
        date_format = date_format.replace(tzinfo=self._GMT)
        self.assertIsNotNone(date_format)

    def testLocaleProviders_test1_decomposed(self) -> None:
        locale_providers = os.getenv("java.locale.providers")
        if locale_providers is not None:  # may be None before Java 9
            self.assertTrue(
                locale_providers.startswith("COMPAT"),
                "java.locale.providers must start with COMPAT",
            )

        txt = "3/20/15 10:59:00 PM"
        date_format = DateFormat.getDateTimeInstance(3, DateFormat.MEDIUM, Locale.US)
        date_format.setTimeZone(self._GMT)
        date = date_format.parse(txt)

    def testLocaleProviders_test0_decomposed(self) -> None:
        locale_providers = os.getenv("JAVA_LOCALE_PROVIDERS")

    def setUp(self) -> None:
        super().setUp()
        self.__dateValidator = DateValidator.DateValidator1()
        self._validator = self.__dateValidator
