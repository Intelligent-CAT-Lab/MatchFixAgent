from __future__ import annotations
import time
import re
import sys
import enum
import unittest
import pytest
import io
import typing
from typing import *
import datetime
import os
import unittest
import zoneinfo
from src.main.org.apache.commons.validator.routines.TimeValidator import *


class TimeValidatorTest(unittest.TestCase):

    _localeInvalid: List[str] = [
        "24:00",  # midnight
        "24:00",  # past midnight
        "25:02",  # invalid hour
        "10:61",  # invalid minute
        "05-02",  # invalid sep
        "0X:01",  # invalid sep
        "05:0X",  # invalid char
        "01-01",  # invalid pattern
        "10:",  # invalid pattern
        "10::1",  # invalid pattern
        "10:1:",  # invalid pattern
    ]
    _patternInvalid: List[str] = [
        "24-00-00",  # midnight
        "24-00-01",  # past midnight
        "25-02-03",  # invalid hour
        "10-61-31",  # invalid minute
        "10-01-61",  # invalid second
        "05:02-29",  # invalid sep
        "0X-01:01",  # invalid sep
        "05-0X-01",  # invalid char
        "10-01-0X",  # invalid char
        "01:01:05",  # invalid pattern
        "10-10",  # invalid pattern
        "10--10",  # invalid pattern
        "10-10-",  # invalid pattern
    ]
    _localeExpect: typing.List[typing.Union[datetime.date, datetime.datetime]] = None
    _localeValid: typing.List[str] = [
        "23:59",
        "00:00",
        "00:01",
        "0:0",
        "1:12",
        "10:49",
        "16:23",
    ]
    _patternExpect: typing.List[typing.Union[datetime.date, datetime.datetime]] = None
    _patternValid: typing.List[str] = [
        "23-59-59",
        "00-00-00",
        "00-00-01",
        "0-0-0",
        "1-12-1",
        "10-49-18",
        "16-23-46",
    ]
    _validator: TimeValidator = None

    _EST: typing.Union[zoneinfo.ZoneInfo, datetime.timezone] = zoneinfo.ZoneInfo("EST")
    _GMT: typing.Union[zoneinfo.ZoneInfo, datetime.timezone] = zoneinfo.ZoneInfo("GMT")
    __defaultZone: typing.Union[zoneinfo.ZoneInfo, datetime.timezone] = None

    __origDefault: typing.Any = None

    @staticmethod
    def initialize_fields() -> None:
        TimeValidatorTest._localeExpect: typing.List[
            typing.Union[datetime.date, datetime.datetime]
        ] = [
            TimeValidatorTest._createDate(None, 235900, 0),
            TimeValidatorTest._createDate(None, 0, 0),
            TimeValidatorTest._createDate(None, 100, 0),
            TimeValidatorTest._createDate(None, 0, 0),
            TimeValidatorTest._createDate(None, 11200, 0),
            TimeValidatorTest._createDate(None, 104900, 0),
            TimeValidatorTest._createDate(None, 162300, 0),
        ]

        TimeValidatorTest._patternExpect: typing.List[
            typing.Union[datetime.date, datetime.datetime]
        ] = [
            TimeValidatorTest._createDate(None, 235959, 0),
            TimeValidatorTest._createDate(None, 0, 0),
            TimeValidatorTest._createDate(None, 1, 0),
            TimeValidatorTest._createDate(None, 0, 0),
            TimeValidatorTest._createDate(None, 11201, 0),
            TimeValidatorTest._createDate(None, 104918, 0),
            TimeValidatorTest._createDate(None, 162346, 0),
        ]

    def testCompare_test5_decomposed(self) -> None:
        test_time = 154523
        min_offset = 100
        hour_offset = 10000

        milli_greater = self._createTime(self._GMT, test_time, 500)
        value = self._createTime(self._GMT, test_time, 400)
        milli_less = self._createTime(self._GMT, test_time, 300)
        sec_greater = self._createTime(self._GMT, test_time + 1, 100)
        sec_less = self._createTime(self._GMT, test_time - 1, 100)
        min_greater = self._createTime(self._GMT, test_time + min_offset, 100)
        min_less = self._createTime(self._GMT, test_time - min_offset, 100)
        hour_greater = self._createTime(self._GMT, test_time + hour_offset, 100)
        hour_less = self._createTime(self._GMT, test_time - hour_offset, 100)

        self.assertEqual(
            -1, self._validator.compareTime(value, milli_greater), "mili LT"
        )
        self.assertEqual(0, self._validator.compareTime(value, value), "mili EQ")
        self.assertEqual(1, self._validator.compareTime(value, milli_less), "mili GT")
        self.assertEqual(
            -1, self._validator.compareSeconds(value, sec_greater), "secs LT"
        )
        self.assertEqual(
            0, self._validator.compareSeconds(value, milli_greater), "secs =1"
        )
        self.assertEqual(0, self._validator.compareSeconds(value, value), "secs =2")
        self.assertEqual(
            0, self._validator.compareSeconds(value, milli_less), "secs =3"
        )
        self.assertEqual(1, self._validator.compareSeconds(value, sec_less), "secs GT")
        self.assertEqual(
            -1, self._validator.compareMinutes(value, min_greater), "mins LT"
        )
        self.assertEqual(
            0, self._validator.compareMinutes(value, sec_greater), "mins =1"
        )
        self.assertEqual(0, self._validator.compareMinutes(value, value), "mins =2")
        self.assertEqual(0, self._validator.compareMinutes(value, sec_less), "mins =3")
        self.assertEqual(1, self._validator.compareMinutes(value, min_less), "mins GT")
        self.assertEqual(
            -1, self._validator.compareHours(value, hour_greater), "hour LT"
        )
        self.assertEqual(0, self._validator.compareHours(value, min_greater), "hour =1")
        self.assertEqual(0, self._validator.compareHours(value, value), "hour =2")
        self.assertEqual(0, self._validator.compareHours(value, min_less), "hour =3")
        self.assertEqual(1, self._validator.compareHours(value, hour_less), "hour GT")

    def testCompare_test4_decomposed(self) -> None:
        test_time = 154523
        min_offset = 100
        hour_offset = 10000

        milli_greater = self._createTime(self._GMT, test_time, 500)
        value = self._createTime(self._GMT, test_time, 400)
        milli_less = self._createTime(self._GMT, test_time, 300)
        sec_greater = self._createTime(self._GMT, test_time + 1, 100)
        sec_less = self._createTime(self._GMT, test_time - 1, 100)
        min_greater = self._createTime(self._GMT, test_time + min_offset, 100)
        min_less = self._createTime(self._GMT, test_time - min_offset, 100)
        hour_greater = self._createTime(self._GMT, test_time + hour_offset, 100)
        hour_less = self._createTime(self._GMT, test_time - hour_offset, 100)

        self.assertEqual(
            -1, self._validator.compareTime(value, milli_greater), "mili LT"
        )
        self.assertEqual(0, self._validator.compareTime(value, value), "mili EQ")
        self.assertEqual(1, self._validator.compareTime(value, milli_less), "mili GT")
        self.assertEqual(
            -1, self._validator.compareSeconds(value, sec_greater), "secs LT"
        )
        self.assertEqual(
            0, self._validator.compareSeconds(value, milli_greater), "secs =1"
        )
        self.assertEqual(0, self._validator.compareSeconds(value, value), "secs =2")
        self.assertEqual(
            0, self._validator.compareSeconds(value, milli_less), "secs =3"
        )
        self.assertEqual(1, self._validator.compareSeconds(value, sec_less), "secs GT")
        self.assertEqual(
            -1, self._validator.compareMinutes(value, min_greater), "mins LT"
        )
        self.assertEqual(
            0, self._validator.compareMinutes(value, sec_greater), "mins =1"
        )
        self.assertEqual(0, self._validator.compareMinutes(value, value), "mins =2")
        self.assertEqual(0, self._validator.compareMinutes(value, sec_less), "mins =3")
        self.assertEqual(1, self._validator.compareMinutes(value, min_less), "mins GT")

    def testCompare_test3_decomposed(self) -> None:
        test_time = 154523
        min_offset = 100
        hour_offset = 10000

        milli_greater = self._createTime(self._GMT, test_time, 500)
        value = self._createTime(self._GMT, test_time, 400)
        milli_less = self._createTime(self._GMT, test_time, 300)
        sec_greater = self._createTime(self._GMT, test_time + 1, 100)
        sec_less = self._createTime(self._GMT, test_time - 1, 100)
        min_greater = self._createTime(self._GMT, test_time + min_offset, 100)
        min_less = self._createTime(self._GMT, test_time - min_offset, 100)
        hour_greater = self._createTime(self._GMT, test_time + hour_offset, 100)
        hour_less = self._createTime(self._GMT, test_time - hour_offset, 100)

        self.assertEqual(
            -1, self._validator.compareTime(value, milli_greater), "mili LT"
        )
        self.assertEqual(0, self._validator.compareTime(value, value), "mili EQ")
        self.assertEqual(1, self._validator.compareTime(value, milli_less), "mili GT")
        self.assertEqual(
            -1, self._validator.compareSeconds(value, sec_greater), "secs LT"
        )
        self.assertEqual(
            0, self._validator.compareSeconds(value, milli_greater), "secs =1"
        )
        self.assertEqual(0, self._validator.compareSeconds(value, value), "secs =2")
        self.assertEqual(
            0, self._validator.compareSeconds(value, milli_less), "secs =3"
        )
        self.assertEqual(1, self._validator.compareSeconds(value, sec_less), "secs GT")

    def testCompare_test2_decomposed(self) -> None:
        test_time = 154523
        min_offset = 100
        hour_offset = 10000

        milli_greater = self._createTime(self._GMT, test_time, 500)
        value = self._createTime(self._GMT, test_time, 400)
        milli_less = self._createTime(self._GMT, test_time, 300)
        sec_greater = self._createTime(self._GMT, test_time + 1, 100)
        sec_less = self._createTime(self._GMT, test_time - 1, 100)
        min_greater = self._createTime(self._GMT, test_time + min_offset, 100)
        min_less = self._createTime(self._GMT, test_time - min_offset, 100)
        hour_greater = self._createTime(self._GMT, test_time + hour_offset, 100)
        hour_less = self._createTime(self._GMT, test_time - hour_offset, 100)

        self.assertEqual(
            -1, self._validator.compareTime(value, milli_greater), "mili LT"
        )
        self.assertEqual(0, self._validator.compareTime(value, value), "mili EQ")
        self.assertEqual(1, self._validator.compareTime(value, milli_less), "mili GT")

    def testCompare_test1_decomposed(self) -> None:
        test_time = 154523
        minute = 100
        hour = 10000
        milli_greater = self._createTime(self._GMT, test_time, 500)
        value = self._createTime(self._GMT, test_time, 400)
        milli_less = self._createTime(self._GMT, test_time, 300)
        sec_greater = self._createTime(self._GMT, test_time + 1, 100)
        sec_less = self._createTime(self._GMT, test_time - 1, 100)
        min_greater = self._createTime(self._GMT, test_time + minute, 100)
        min_less = self._createTime(self._GMT, test_time - minute, 100)
        hour_greater = self._createTime(self._GMT, test_time + hour, 100)
        hour_less = self._createTime(self._GMT, test_time - hour, 100)

    def testCompare_test0_decomposed(self) -> None:
        test_time = 154523
        min = 100
        hour = 10000
        milli_greater = self._createTime(self._GMT, test_time, 500)

    def testFormat_test4_decomposed(self) -> None:
        # Set the default locale to UK
        locale.setlocale(locale.LC_TIME, "en_GB")

        # Get an instance of the TimeValidator
        validator = TimeValidator.getInstance()

        # Validate the time string with the given pattern
        test = validator.validate2("16:49:23", "HH:mm:ss")
        self.assertIsNotNone(test, "Test Date ")

        # Assert the formatted output with the given pattern
        self.assertEqual(
            "16-49-23", validator.format1(test, "HH-mm-ss"), "Format pattern"
        )

        # Assert the formatted output with a specific locale
        self.assertEqual(
            "4:49 PM", validator.format2(test, locale.Locale("en_US")), "Format locale"
        )

        # Assert the default formatted output
        self.assertEqual("16:49", validator.format0(test), "Format default")

    def testFormat_test3_decomposed(self) -> None:
        # Set the default locale to UK
        locale.setlocale(locale.LC_TIME, "en_GB")

        # Get an instance of TimeValidator
        validator = TimeValidator.getInstance()

        # Validate the time string with the given pattern
        test = validator.validate2("16:49:23", "HH:mm:ss")

        # Assert that the validation result is not None
        self.assertIsNotNone(test, "Test Date ")

        # Assert that the formatted time matches the expected pattern
        self.assertEqual(
            "16-49-23", validator.format1(test, "HH-mm-ss"), "Format pattern"
        )

        # Assert that the formatted time matches the expected locale-specific format
        self.assertEqual(
            "4:49 PM", validator.format2(test, locale.Locale("en_US")), "Format locale"
        )

    def testFormat_test2_decomposed(self) -> None:
        # Set the default locale to UK (not directly applicable in Python, but we proceed with the test logic)
        # In Python, locale settings can be managed using the `locale` module if needed.

        # Get an instance of the TimeValidator
        validator = TimeValidator.getInstance()

        # Validate the time string using the specified pattern
        test = validator.validate2("16:49:23", "HH:mm:ss")

        # Assert that the result is not None
        self.assertIsNotNone(test, "Test Date ")

        # Assert that the formatted output matches the expected value
        self.assertEqual(
            "16-49-23", validator.format1(test, "HH-mm-ss"), "Format pattern"
        )

    def testFormat_test1_decomposed(self) -> None:
        import locale

        try:
            locale.setlocale(locale.LC_TIME, "en_GB.UTF-8")  # Corrected locale setting
        except locale.Error:
            self.skipTest("Locale en_GB.UTF-8 is not supported on this system")
        TimeValidator.getInstance()
        test = TimeValidator.getInstance().validate2("16:49:23", "HH:mm:ss")
        self.assertIsNotNone(test, "Validation result should not be None")

    def testFormat_test0_decomposed(self) -> None:
        locale.setlocale(locale.LC_ALL, "en_GB")  # Set locale to UK
        TimeValidator.getInstance()  # Call the getInstance method

    def testTimeZone_test20_decomposed(self) -> None:
        # Set default locale and timezone
        os.environ["TZ"] = "GMT"
        datetime.datetime.now().astimezone()  # Refresh timezone settings

        # Test validate0
        result = self._validator.validate0("18:01")
        self.assertIsNotNone(result, "default result")
        self.assertEqual(result.tzinfo, self._GMT, "default zone")
        self.assertEqual(result.hour, 18, "default hour")
        self.assertEqual(result.minute, 1, "default minute")

        # Test validate1
        result = self._validator.validate1("16:49", self._EST)
        self.assertIsNotNone(result, "zone result")
        self.assertEqual(result.tzinfo, self._EST, "zone zone")
        self.assertEqual(result.hour, 16, "zone hour")
        self.assertEqual(result.minute, 49, "zone minute")

        # Test validate3
        result = self._validator.validate3("14-34", "HH-mm", self._EST)
        self.assertIsNotNone(result, "pattern result")
        self.assertEqual(result.tzinfo, self._EST, "pattern zone")
        self.assertEqual(result.hour, 14, "pattern hour")
        self.assertEqual(result.minute, 34, "pattern minute")

        # Test validate5
        result = self._validator.validate5(
            "7:18 PM", locale="en_US", timeZone=self._EST
        )
        self.assertIsNotNone(result, "locale result")
        self.assertEqual(result.tzinfo, self._EST, "locale zone")
        self.assertEqual(result.hour, 19, "locale hour")
        self.assertEqual(result.minute, 18, "locale minute")

        # Test validate7
        result = self._validator.validate7(
            "31/Dez/05 21-05", "dd/MMM/yy HH-mm", locale="de_DE", timeZone=self._EST
        )
        self.assertIsNotNone(result, "pattern result")
        self.assertEqual(result.tzinfo, self._EST, "pattern zone")
        self.assertEqual(result.year, 2005, "pattern year")
        self.assertEqual(
            result.month, 12, "pattern month"
        )  # Month is 1-based in Python
        self.assertEqual(result.day, 31, "pattern day")
        self.assertEqual(result.hour, 21, "pattern hour")
        self.assertEqual(result.minute, 5, "pattern minute")

        # Test validate6
        result = self._validator.validate6(
            "31/Dez/05 21-05", "dd/MMM/yy HH-mm", locale="de_DE"
        )
        self.assertIsNotNone(result, "pattern result")
        self.assertEqual(result.tzinfo, self._GMT, "pattern zone")
        self.assertEqual(result.year, 2005, "pattern year")
        self.assertEqual(
            result.month, 12, "pattern month"
        )  # Month is 1-based in Python
        self.assertEqual(result.day, 31, "pattern day")
        self.assertEqual(result.hour, 21, "pattern hour")
        self.assertEqual(result.minute, 5, "pattern minute")

    def testTimeZone_test19_decomposed(self) -> None:
        # Set default locale and timezone
        os.environ["LC_ALL"] = "en_GB.UTF-8"
        datetime.timezone.utc = self._GMT

        # Test validate0
        result = self._validator.validate0("18:01")
        self.assertIsNotNone(result, "default result")
        self.assertEqual(result.tzinfo, self._GMT, "default zone")
        self.assertEqual(result.hour, 18, "default hour")
        self.assertEqual(result.minute, 1, "default minute")

        # Test validate1
        result = self._validator.validate1("16:49", self._EST)
        self.assertIsNotNone(result, "zone result")
        self.assertEqual(result.tzinfo, self._EST, "zone zone")
        self.assertEqual(result.hour, 16, "zone hour")
        self.assertEqual(result.minute, 49, "zone minute")

        # Test validate3
        result = self._validator.validate3("14-34", "HH-mm", self._EST)
        self.assertIsNotNone(result, "pattern result")
        self.assertEqual(result.tzinfo, self._EST, "pattern zone")
        self.assertEqual(result.hour, 14, "pattern hour")
        self.assertEqual(result.minute, 34, "pattern minute")

        # Test validate5
        result = self._validator.validate5(
            "7:18 PM", locale="en_US", timeZone=self._EST
        )
        self.assertIsNotNone(result, "locale result")
        self.assertEqual(result.tzinfo, self._EST, "locale zone")
        self.assertEqual(result.hour, 19, "locale hour")
        self.assertEqual(result.minute, 18, "locale minute")

        # Test validate7
        result = self._validator.validate7(
            "31/Dez/05 21-05", "dd/MMM/yy HH-mm", locale="de_DE", timeZone=self._EST
        )
        self.assertIsNotNone(result, "pattern result")
        self.assertEqual(result.tzinfo, self._EST, "pattern zone")
        self.assertEqual(result.year, 2005, "pattern year")
        self.assertEqual(
            result.month, 12, "pattern month"
        )  # Month is 1-based in Python
        self.assertEqual(result.day, 31, "pattern day")
        self.assertEqual(result.hour, 21, "pattern hour")
        self.assertEqual(result.minute, 5, "pattern minute")

        # Test validate6
        result = self._validator.validate6(
            "31/Dez/05 21-05", "dd/MMM/yy HH-mm", locale="de_DE"
        )
        self.assertIsNotNone(result, "pattern result")
        self.assertEqual(result.tzinfo, self._GMT, "pattern zone")
        self.assertEqual(result.year, 2005, "pattern year")
        self.assertEqual(
            result.month, 12, "pattern month"
        )  # Month is 1-based in Python
        self.assertEqual(result.day, 31, "pattern day")
        self.assertEqual(result.hour, 21, "pattern hour")

    def testTimeZone_test18_decomposed(self) -> None:
        # Set default locale and timezone
        locale.setlocale(locale.LC_ALL, "en_GB")  # Locale.UK equivalent
        os.environ["TZ"] = "GMT"  # TimeZone.setDefault(GMT) equivalent
        datetime.tzset()

        result = None

        # Test validate0
        result = self._validator.validate0("18:01")
        self.assertIsNotNone(result, "default result")
        self.assertEqual(self._GMT, result.tzinfo, "default zone")
        self.assertEqual(18, result.hour, "default hour")
        self.assertEqual(1, result.minute, "default minute")

        # Test validate1
        result = None
        result = self._validator.validate1("16:49", self._EST)
        self.assertIsNotNone(result, "zone result")
        self.assertEqual(self._EST, result.tzinfo, "zone zone")
        self.assertEqual(16, result.hour, "zone hour")
        self.assertEqual(49, result.minute, "zone minute")

        # Test validate3
        result = None
        result = self._validator.validate3("14-34", "HH-mm", self._EST)
        self.assertIsNotNone(result, "pattern result")
        self.assertEqual(self._EST, result.tzinfo, "pattern zone")
        self.assertEqual(14, result.hour, "pattern hour")
        self.assertEqual(34, result.minute, "pattern minute")

        # Test validate5
        result = None
        result = self._validator.validate5(
            "7:18 PM", locale.Locale("en", "US"), self._EST
        )
        self.assertIsNotNone(result, "locale result")
        self.assertEqual(self._EST, result.tzinfo, "locale zone")
        self.assertEqual(19, result.hour, "locale hour")
        self.assertEqual(18, result.minute, "locale minute")

        # Test validate7
        result = None
        result = self._validator.validate7(
            "31/Dez/05 21-05", "dd/MMM/yy HH-mm", locale.Locale("de", "DE"), self._EST
        )
        self.assertIsNotNone(result, "pattern result")
        self.assertEqual(self._EST, result.tzinfo, "pattern zone")
        self.assertEqual(2005, result.year, "pattern day")
        self.assertEqual(
            11, result.month - 1, "pattern day"
        )  # Python months are 1-based
        self.assertEqual(31, result.day, "pattern day")
        self.assertEqual(21, result.hour, "pattern hour")
        self.assertEqual(5, result.minute, "pattern minute")

        # Test validate6
        result = None
        result = self._validator.validate6(
            "31/Dez/05 21-05", "dd/MMM/yy HH-mm", locale.Locale("de", "DE")
        )
        self.assertIsNotNone(result, "pattern result")
        self.assertEqual(self._GMT, result.tzinfo, "pattern zone")
        self.assertEqual(2005, result.year, "pattern day")
        self.assertEqual(
            11, result.month - 1, "pattern day"
        )  # Python months are 1-based

    def testTimeZone_test17_decomposed(self) -> None:
        # Set default locale and timezone
        locale.setlocale(locale.LC_ALL, "en_GB")  # Locale.UK equivalent
        os.environ["TZ"] = "GMT"  # TimeZone.setDefault(GMT) equivalent
        datetime.tzset()

        result = None

        # Test validate0
        result = self._validator.validate0("18:01")
        self.assertIsNotNone(result, "default result")
        self.assertEqual(self._GMT, result.tzinfo, "default zone")
        self.assertEqual(18, result.hour, "default hour")
        self.assertEqual(1, result.minute, "default minute")

        # Test validate1
        result = None
        result = self._validator.validate1("16:49", self._EST)
        self.assertIsNotNone(result, "zone result")
        self.assertEqual(self._EST, result.tzinfo, "zone zone")
        self.assertEqual(16, result.hour, "zone hour")
        self.assertEqual(49, result.minute, "zone minute")

        # Test validate3
        result = None
        result = self._validator.validate3("14-34", "HH-mm", self._EST)
        self.assertIsNotNone(result, "pattern result")
        self.assertEqual(self._EST, result.tzinfo, "pattern zone")
        self.assertEqual(14, result.hour, "pattern hour")
        self.assertEqual(34, result.minute, "pattern minute")

        # Test validate5
        result = None
        result = self._validator.validate5("7:18 PM", locale.Locale("en_US"), self._EST)
        self.assertIsNotNone(result, "locale result")
        self.assertEqual(self._EST, result.tzinfo, "locale zone")
        self.assertEqual(19, result.hour, "locale hour")
        self.assertEqual(18, result.minute, "locale minute")

        # Test validate7
        result = None
        result = self._validator.validate7(
            "31/Dez/05 21-05", "dd/MMM/yy HH-mm", locale.Locale("de_DE"), self._EST
        )
        self.assertIsNotNone(result, "pattern result")
        self.assertEqual(self._EST, result.tzinfo, "pattern zone")
        self.assertEqual(2005, result.year, "pattern year")
        self.assertEqual(
            11, result.month - 1, "pattern month"
        )  # Python months are 1-based
        self.assertEqual(31, result.day, "pattern day")
        self.assertEqual(21, result.hour, "pattern hour")
        self.assertEqual(5, result.minute, "pattern minute")

        # Test validate6
        result = None
        result = self._validator.validate6(
            "31/Dez/05 21-05", "dd/MMM/yy HH-mm", locale.Locale("de_DE")
        )
        self.assertIsNotNone(result, "pattern result")
        self.assertEqual(self._GMT, result.tzinfo, "pattern zone")

    def testTimeZone_test16_decomposed(self) -> None:
        # Set default locale and timezone
        os.environ["TZ"] = "GMT"
        datetime.datetime.now().astimezone()  # Refresh timezone settings

        # Test validate0
        result = self._validator.validate0("18:01")
        self.assertIsNotNone(result, "default result")
        self.assertEqual(result.tzinfo, self._GMT, "default zone")
        self.assertEqual(result.hour, 18, "default hour")
        self.assertEqual(result.minute, 1, "default minute")

        # Test validate1
        result = self._validator.validate1("16:49", self._EST)
        self.assertIsNotNone(result, "zone result")
        self.assertEqual(result.tzinfo, self._EST, "zone zone")
        self.assertEqual(result.hour, 16, "zone hour")
        self.assertEqual(result.minute, 49, "zone minute")

        # Test validate3
        result = self._validator.validate3("14-34", "HH-mm", self._EST)
        self.assertIsNotNone(result, "pattern result")
        self.assertEqual(result.tzinfo, self._EST, "pattern zone")
        self.assertEqual(result.hour, 14, "pattern hour")
        self.assertEqual(result.minute, 34, "pattern minute")

        # Test validate5
        result = self._validator.validate5(
            "7:18 PM", locale="en_US", timeZone=self._EST
        )
        self.assertIsNotNone(result, "locale result")
        self.assertEqual(result.tzinfo, self._EST, "locale zone")
        self.assertEqual(result.hour, 19, "locale hour")
        self.assertEqual(result.minute, 18, "locale minute")

        # Test validate7
        result = self._validator.validate7(
            "31/Dez/05 21-05", "dd/MMM/yy HH-mm", locale="de_DE", timeZone=self._EST
        )
        self.assertIsNotNone(result, "pattern result")
        self.assertEqual(result.tzinfo, self._EST, "pattern zone")
        self.assertEqual(result.year, 2005, "pattern year")
        self.assertEqual(result.month, 12, "pattern month")  # December is 12 in Python
        self.assertEqual(result.day, 31, "pattern day")
        self.assertEqual(result.hour, 21, "pattern hour")
        self.assertEqual(result.minute, 5, "pattern minute")

        # Test validate6
        result = self._validator.validate6(
            "31/Dez/05 21-05", "dd/MMM/yy HH-mm", locale="de_DE"
        )
        # No assertions provided in the original Java code for this case

    def testTimeZone_test15_decomposed(self) -> None:
        # Set default locale and timezone
        os.environ["LC_ALL"] = "en_GB.UTF-8"
        datetime.timezone.utc = self._GMT

        # Test validate0
        result = self._validator.validate0("18:01")
        self.assertIsNotNone(result, "default result")
        self.assertEqual(result.tzinfo, self._GMT, "default zone")
        self.assertEqual(result.hour, 18, "default hour")
        self.assertEqual(result.minute, 1, "default minute")

        # Test validate1
        result = self._validator.validate1("16:49", self._EST)
        self.assertIsNotNone(result, "zone result")
        self.assertEqual(result.tzinfo, self._EST, "zone zone")
        self.assertEqual(result.hour, 16, "zone hour")
        self.assertEqual(result.minute, 49, "zone minute")

        # Test validate3
        result = self._validator.validate3("14-34", "HH-mm", self._EST)
        self.assertIsNotNone(result, "pattern result")
        self.assertEqual(result.tzinfo, self._EST, "pattern zone")
        self.assertEqual(result.hour, 14, "pattern hour")
        self.assertEqual(result.minute, 34, "pattern minute")

        # Test validate5
        result = self._validator.validate5(
            "7:18 PM", locale="en_US", timeZone=self._EST
        )
        self.assertIsNotNone(result, "locale result")
        self.assertEqual(result.tzinfo, self._EST, "locale zone")
        self.assertEqual(result.hour, 19, "locale hour")
        self.assertEqual(result.minute, 18, "locale minute")

        # Test validate7
        result = self._validator.validate7(
            "31/Dez/05 21-05", "dd/MMM/yy HH-mm", locale="de_DE", timeZone=self._EST
        )
        self.assertIsNotNone(result, "pattern result")
        self.assertEqual(result.tzinfo, self._EST, "pattern zone")
        self.assertEqual(result.year, 2005, "pattern year")
        self.assertEqual(
            result.month, 12, "pattern month"
        )  # Note: Python months are 1-based
        self.assertEqual(result.day, 31, "pattern day")
        self.assertEqual(result.hour, 21, "pattern hour")

    def testTimeZone_test14_decomposed(self) -> None:
        # Set default locale and timezone
        locale.setlocale(locale.LC_TIME, "en_GB")  # Locale.UK equivalent
        os.environ["TZ"] = "GMT"  # TimeZone.setDefault(GMT) equivalent
        datetime.tzset()

        result = None

        # Test validate0
        result = self._validator.validate0("18:01")
        self.assertIsNotNone(result, "default result")
        self.assertEqual(self._GMT, result.tzinfo, "default zone")
        self.assertEqual(18, result.hour, "default hour")
        self.assertEqual(1, result.minute, "default minute")

        # Test validate1
        result = None
        result = self._validator.validate1("16:49", self._EST)
        self.assertIsNotNone(result, "zone result")
        self.assertEqual(self._EST, result.tzinfo, "zone zone")
        self.assertEqual(16, result.hour, "zone hour")
        self.assertEqual(49, result.minute, "zone minute")

        # Test validate3
        result = None
        result = self._validator.validate3("14-34", "HH-mm", self._EST)
        self.assertIsNotNone(result, "pattern result")
        self.assertEqual(self._EST, result.tzinfo, "pattern zone")
        self.assertEqual(14, result.hour, "pattern hour")
        self.assertEqual(34, result.minute, "pattern minute")

        # Test validate5
        result = None
        result = self._validator.validate5(
            "7:18 PM", locale.Locale("en", "US"), self._EST
        )
        self.assertIsNotNone(result, "locale result")
        self.assertEqual(self._EST, result.tzinfo, "locale zone")
        self.assertEqual(19, result.hour, "locale hour")
        self.assertEqual(18, result.minute, "locale minute")

        # Test validate7
        result = None
        result = self._validator.validate7(
            "31/Dez/05 21-05", "dd/MMM/yy HH-mm", locale.Locale("de", "DE"), self._EST
        )
        self.assertIsNotNone(result, "pattern result")
        self.assertEqual(self._EST, result.tzinfo, "pattern zone")
        self.assertEqual(2005, result.year, "pattern year")
        self.assertEqual(11, result.month, "pattern month")

    def testTimeZone_test13_decomposed(self) -> None:
        # Set default locale and timezone
        os.environ["LC_ALL"] = "en_GB.UTF-8"
        datetime.timezone.utc = self._GMT

        # Test case 1: validate0
        result = self._validator.validate0("18:01")
        self.assertIsNotNone(result, "default result")
        self.assertEqual(result.tzinfo, self._GMT, "default zone")
        self.assertEqual(result.hour, 18, "default hour")
        self.assertEqual(result.minute, 1, "default minute")

        # Test case 2: validate1
        result = self._validator.validate1("16:49", self._EST)
        self.assertIsNotNone(result, "zone result")
        self.assertEqual(result.tzinfo, self._EST, "zone zone")
        self.assertEqual(result.hour, 16, "zone hour")
        self.assertEqual(result.minute, 49, "zone minute")

        # Test case 3: validate3
        result = self._validator.validate3("14-34", "HH-mm", self._EST)
        self.assertIsNotNone(result, "pattern result")
        self.assertEqual(result.tzinfo, self._EST, "pattern zone")
        self.assertEqual(result.hour, 14, "pattern hour")
        self.assertEqual(result.minute, 34, "pattern minute")

        # Test case 4: validate5
        result = self._validator.validate5(
            "7:18 PM", locale="en_US", timeZone=self._EST
        )
        self.assertIsNotNone(result, "locale result")
        self.assertEqual(result.tzinfo, self._EST, "locale zone")
        self.assertEqual(result.hour, 19, "locale hour")
        self.assertEqual(result.minute, 18, "locale minute")

        # Test case 5: validate7
        result = self._validator.validate7(
            "31/Dez/05 21-05", "dd/MMM/yy HH-mm", locale="de_DE", timeZone=self._EST
        )
        self.assertIsNotNone(result, "pattern result")
        self.assertEqual(result.tzinfo, self._EST, "pattern zone")

    def testTimeZone_test12_decomposed(self) -> None:
        # Set default locale and timezone
        os.environ["TZ"] = "GMT"
        datetime.datetime.now().astimezone()  # Refresh timezone settings

        # Test validate0
        result = self._validator.validate0("18:01")
        self.assertIsNotNone(result, "default result")
        self.assertEqual(result.tzinfo, self._GMT, "default zone")
        self.assertEqual(result.hour, 18, "default hour")
        self.assertEqual(result.minute, 1, "default minute")

        # Test validate1
        result = self._validator.validate1("16:49", self._EST)
        self.assertIsNotNone(result, "zone result")
        self.assertEqual(result.tzinfo, self._EST, "zone zone")
        self.assertEqual(result.hour, 16, "zone hour")
        self.assertEqual(result.minute, 49, "zone minute")

        # Test validate3
        result = self._validator.validate3("14-34", "HH-mm", self._EST)
        self.assertIsNotNone(result, "pattern result")
        self.assertEqual(result.tzinfo, self._EST, "pattern zone")
        self.assertEqual(result.hour, 14, "pattern hour")
        self.assertEqual(result.minute, 34, "pattern minute")

        # Test validate5
        result = self._validator.validate5(
            "7:18 PM", locale="en_US", timeZone=self._EST
        )
        self.assertIsNotNone(result, "locale result")
        self.assertEqual(result.tzinfo, self._EST, "locale zone")
        self.assertEqual(result.hour, 19, "locale hour")
        self.assertEqual(result.minute, 18, "locale minute")

        # Test validate7
        result = self._validator.validate7(
            "31/Dez/05 21-05", "dd/MMM/yy HH-mm", locale="de_DE", timeZone=self._EST
        )
        self.assertIsNotNone(result, "pattern and locale result")

    def testTimeZone_test11_decomposed(self) -> None:
        # Set default locale and timezone
        os.environ["TZ"] = "GMT"
        datetime.datetime.now().astimezone()  # Refresh timezone settings

        # Test case 1: Default timezone
        result = self._validator.validate0("18:01")
        self.assertIsNotNone(result, "default result")
        self.assertEqual(result.tzinfo, self._GMT, "default zone")
        self.assertEqual(result.hour, 18, "default hour")
        self.assertEqual(result.minute, 1, "default minute")

        # Test case 2: Specific timezone (EST)
        result = self._validator.validate1("16:49", self._EST)
        self.assertIsNotNone(result, "zone result")
        self.assertEqual(result.tzinfo, self._EST, "zone zone")
        self.assertEqual(result.hour, 16, "zone hour")
        self.assertEqual(result.minute, 49, "zone minute")

        # Test case 3: Specific pattern and timezone (EST)
        result = self._validator.validate3("14-34", "HH-mm", self._EST)
        self.assertIsNotNone(result, "pattern result")
        self.assertEqual(result.tzinfo, self._EST, "pattern zone")
        self.assertEqual(result.hour, 14, "pattern hour")
        self.assertEqual(result.minute, 34, "pattern minute")

        # Test case 4: Locale-specific format and timezone (EST)
        result = self._validator.validate5(
            "7:18 PM", locale="en_US", timeZone=self._EST
        )
        self.assertIsNotNone(result, "locale result")
        self.assertEqual(result.tzinfo, self._EST, "locale zone")
        self.assertEqual(result.hour, 19, "locale hour")
        self.assertEqual(result.minute, 18, "locale minute")

    def testTimeZone_test10_decomposed(self) -> None:
        # Set default locale and timezone
        os.environ["TZ"] = "GMT"
        datetime.datetime.now().astimezone()  # Refresh timezone settings

        # Test validate0
        result = self._validator.validate0("18:01")
        self.assertIsNotNone(result, "default result")
        self.assertEqual(result.tzinfo, self._GMT, "default zone")
        self.assertEqual(result.hour, 18, "default hour")
        self.assertEqual(result.minute, 1, "default minute")

        # Test validate1
        result = self._validator.validate1("16:49", self._EST)
        self.assertIsNotNone(result, "zone result")
        self.assertEqual(result.tzinfo, self._EST, "zone zone")
        self.assertEqual(result.hour, 16, "zone hour")
        self.assertEqual(result.minute, 49, "zone minute")

        # Test validate3
        result = self._validator.validate3("14-34", "HH-mm", self._EST)
        self.assertIsNotNone(result, "pattern result")
        self.assertEqual(result.tzinfo, self._EST, "pattern zone")
        self.assertEqual(result.hour, 14, "pattern hour")
        self.assertEqual(result.minute, 34, "pattern minute")

        # Test validate5
        result = self._validator.validate5(
            "7:18 PM", locale="en_US", timeZone=self._EST
        )
        self.assertIsNotNone(result, "locale result")
        self.assertEqual(result.tzinfo, self._EST, "locale zone")

    def testTimeZone_test9_decomposed(self) -> None:
        # Set default locale and timezone
        os.environ["TZ"] = "GMT"
        datetime.datetime.now().astimezone()  # Refresh timezone settings

        # Test validate0
        result = self._validator.validate0("18:01")
        self.assertIsNotNone(result, "default result")
        self.assertEqual(result.tzinfo, self._GMT, "default zone")
        self.assertEqual(result.hour, 18, "default hour")
        self.assertEqual(result.minute, 1, "default minute")

        # Test validate1
        result = self._validator.validate1("16:49", self._EST)
        self.assertIsNotNone(result, "zone result")
        self.assertEqual(result.tzinfo, self._EST, "zone zone")
        self.assertEqual(result.hour, 16, "zone hour")
        self.assertEqual(result.minute, 49, "zone minute")

        # Test validate3
        result = self._validator.validate3("14-34", "HH-mm", self._EST)
        self.assertIsNotNone(result, "pattern result")
        self.assertEqual(result.tzinfo, self._EST, "pattern zone")
        self.assertEqual(result.hour, 14, "pattern hour")
        self.assertEqual(result.minute, 34, "pattern minute")

        # Test validate5
        result = self._validator.validate5(
            "7:18 PM", locale="en_US", timeZone=self._EST
        )
        # No assertions provided for validate5 in the original Java code

    def testTimeZone_test8_decomposed(self) -> None:
        # Set default locale and timezone
        os.environ["TZ"] = "GMT"
        datetime.datetime.now().astimezone()  # Refresh timezone settings

        # Test case 1: Default timezone
        result = self._validator.validate0("18:01")
        self.assertIsNotNone(result, "default result")
        self.assertEqual(result.tzinfo, self._GMT, "default zone")
        self.assertEqual(result.hour, 18, "default hour")
        self.assertEqual(result.minute, 1, "default minute")

        # Test case 2: Specific timezone (EST)
        result = self._validator.validate1("16:49", self._EST)
        self.assertIsNotNone(result, "zone result")
        self.assertEqual(result.tzinfo, self._EST, "zone zone")
        self.assertEqual(result.hour, 16, "zone hour")
        self.assertEqual(result.minute, 49, "zone minute")

        # Test case 3: Specific pattern and timezone (EST)
        result = self._validator.validate3("14-34", "HH-mm", self._EST)
        self.assertIsNotNone(result, "pattern result")
        self.assertEqual(result.tzinfo, self._EST, "pattern zone")
        self.assertEqual(result.hour, 14, "pattern hour")
        self.assertEqual(result.minute, 34, "pattern minute")

    def testTimeZone_test7_decomposed(self) -> None:
        # Set default locale and timezone
        os.environ["TZ"] = "GMT"
        datetime.datetime.now().astimezone()  # Refresh timezone settings

        # Test validate0 method
        result = self._validator.validate0("18:01")
        self.assertIsNotNone(result, "default result")
        self.assertEqual(result.tzinfo, self._GMT, "default zone")
        self.assertEqual(result.hour, 18, "default hour")
        self.assertEqual(result.minute, 1, "default minute")

        # Test validate1 method
        result = self._validator.validate1("16:49", self._EST)
        self.assertIsNotNone(result, "zone result")
        self.assertEqual(result.tzinfo, self._EST, "zone zone")
        self.assertEqual(result.hour, 16, "zone hour")
        self.assertEqual(result.minute, 49, "zone minute")

        # Test validate3 method
        result = self._validator.validate3("14-34", "HH-mm", self._EST)
        self.assertIsNotNone(result, "pattern result")
        self.assertEqual(result.tzinfo, self._EST, "pattern zone")

    def testTimeZone_test6_decomposed(self) -> None:
        # Set default locale and timezone
        os.environ["TZ"] = "GMT"
        datetime.datetime.now().astimezone()  # Refresh timezone settings

        # Test with default timezone
        result = None
        result = self._validator.validate0("18:01")
        self.assertIsNotNone(result, "default result")
        self.assertEqual(result.tzinfo, self._GMT, "default zone")
        self.assertEqual(result.hour, 18, "default hour")
        self.assertEqual(result.minute, 1, "default minute")

        # Test with specified timezone (EST)
        result = None
        result = self._validator.validate1("16:49", self._EST)
        self.assertIsNotNone(result, "zone result")
        self.assertEqual(result.tzinfo, self._EST, "zone zone")
        self.assertEqual(result.hour, 16, "zone hour")
        self.assertEqual(result.minute, 49, "zone minute")

        # Test with custom pattern and timezone (EST)
        result = None
        result = self._validator.validate3("14-34", "HH-mm", self._EST)
        # No assertions provided in the original Java code for this case

    def testTimeZone_test5_decomposed(self) -> None:
        # Set default locale and timezone
        os.environ["TZ"] = "GMT"
        datetime.datetime.now().astimezone()  # Refresh timezone settings

        # Test with default timezone
        result = None
        result = self._validator.validate0("18:01")
        self.assertIsNotNone(result, "default result")
        self.assertEqual(result.tzinfo, self._GMT, "default zone")
        self.assertEqual(result.hour, 18, "default hour")
        self.assertEqual(result.minute, 1, "default minute")

        # Test with specified timezone (EST)
        result = None
        result = self._validator.validate1("16:49", self._EST)
        self.assertIsNotNone(result, "zone result")
        self.assertEqual(result.tzinfo, self._EST, "zone zone")
        self.assertEqual(result.hour, 16, "zone hour")
        self.assertEqual(result.minute, 49, "zone minute")

    def testTimeZone_test4_decomposed(self) -> None:
        # Set default locale and timezone
        locale.setlocale(locale.LC_ALL, "en_GB")  # Equivalent to Locale.UK
        os.environ["TZ"] = "GMT"  # Equivalent to TimeZone.setDefault(GMT)
        time.tzset()

        # Test validate0 method
        result = None
        result = self._validator.validate0("18:01")
        self.assertIsNotNone(result, "default result")
        self.assertEqual(self._GMT, result.tzinfo, "default zone")
        self.assertEqual(18, result.hour, "default hour")
        self.assertEqual(1, result.minute, "default minute")

        # Test validate1 method
        result = None
        result = self._validator.validate1("16:49", self._EST)
        self.assertIsNotNone(result, "zone result")
        self.assertEqual(self._EST, result.tzinfo, "zone zone")

    def testTimeZone_test3_decomposed(self) -> None:
        # Set default locale and timezone
        locale.setlocale(locale.LC_ALL, "en_GB")  # Equivalent to Locale.UK
        os.environ["TZ"] = "GMT"  # Equivalent to TimeZone.setDefault(GMT)
        time.tzset()

        # Test validate0 method
        result = None
        result = self._validator.validate0("18:01")
        self.assertIsNotNone(result, "default result")
        self.assertEqual(self._GMT, result.tzinfo, "default zone")
        self.assertEqual(18, result.hour, "default hour")
        self.assertEqual(1, result.minute, "default minute")

        # Test validate1 method
        result = None
        result = self._validator.validate1("16:49", self._EST)

    def testTimeZone_test2_decomposed(self) -> None:
        # Set the default locale and timezone
        os.environ["TZ"] = "GMT"
        datetime.datetime.now().astimezone()  # Refresh timezone settings

        # Validate the time string
        result = self._validator.validate0("18:01")

        # Assertions
        self.assertIsNotNone(result, "default result")
        self.assertEqual(result.tzinfo, self._GMT, "default zone")
        self.assertEqual(result.hour, 18, "default hour")
        self.assertEqual(result.minute, 1, "default minute")

    def testTimeZone_test1_decomposed(self) -> None:
        # Set the default locale and timezone
        locale.setlocale(locale.LC_ALL, "en_GB")  # Equivalent to Locale.UK
        os.environ["TZ"] = "GMT"  # Equivalent to TimeZone.setDefault(GMT)
        time.tzset()  # Apply the timezone change

        # Initialize result
        result = None

        # Validate the time string
        result = self._validator.validate0("18:01")

        # Assert that the result is not null
        self.assertIsNotNone(result, "default result")

        # Assert that the timezone of the result is GMT
        self.assertEqual(self._GMT, result.tzinfo, "default zone")

    def testTimeZone_test0_decomposed(self) -> None:
        import locale
        import os
        from datetime import datetime
        from zoneinfo import ZoneInfo

        try:
            locale.setlocale(locale.LC_ALL, "en_GB")  # Set locale to UK
        except locale.Error:
            locale.setlocale(
                locale.LC_ALL, ""
            )  # Fallback to default locale if 'en_GB' is unsupported

        os.environ["TZ"] = "GMT"  # Set timezone to GMT
        datetime.now(ZoneInfo("GMT"))  # Ensure timezone is applied

        self._validator = TimeValidator()  # Initialize the validator
        result = None
        result = self._validator.validate0("18:01")

    def testLocaleInvalid_test0_decomposed(self) -> None:
        self._validator = TimeValidator()  # Initialize the validator
        for i, invalid_value in enumerate(self._localeInvalid):
            text = f"{i} value=[{invalid_value}] passed "
            date = self._validator.validate4(invalid_value, locale=Locale.US)
            self.assertIsNone(date, f"validate() {text}{date}")
            self.assertFalse(
                self._validator.isValid2(invalid_value, locale=Locale.UK),
                f"isValid() {text}",
            )

    def testLocaleValid_test0_decomposed(self) -> None:
        for i, valid_value in enumerate(self._localeValid):
            text = f"{i} value=[{valid_value}] failed "
            calendar = self._validator.validate4(
                valid_value, locale=zoneinfo.ZoneInfo("Europe/London")
            )
            self.assertIsNotNone(calendar, f"validate() {text}")

            date = calendar if isinstance(calendar, datetime.datetime) else None
            self.assertTrue(
                self._validator.isValid2(
                    valid_value, locale=zoneinfo.ZoneInfo("Europe/London")
                ),
                f"isValid() {text}",
            )
            self.assertEqual(self._localeExpect[i], date, f"compare {text}")

    def testPatternInvalid_test0_decomposed(self) -> None:
        self._validator = TimeValidator(
            strict=False, timeStyle=None
        )  # Initialize the validator with required arguments
        for i, pattern in enumerate(self._patternInvalid):
            text = f"{i} value=[{pattern}] passed "
            date = self._validator.validate2(pattern, "HH-mm-ss")
            self.assertIsNone(date, f"validate() {text}{date}")
            self.assertFalse(
                self._validator.isValid1(pattern, "HH-mm-ss"), f"isValid() {text}"
            )

    def testPatternValid_test0_decomposed(self) -> None:
        for i, pattern in enumerate(self._patternValid):
            text = f"{i} value=[{pattern}] failed "
            calendar = self._validator.validate2(pattern, "HH-mm-ss")
            self.assertIsNotNone(calendar, f"validateObj() {text}")
            date = calendar.getTime() if hasattr(calendar, "getTime") else calendar
            self.assertTrue(
                self._validator.isValid1(pattern, "HH-mm-ss"), f"isValid() {text}"
            )
            self.assertEqual(self._patternExpect[i], date, f"compare {text}")

    def tearDown(self) -> None:
        super().tearDown()
        self._validator = None
        locale.setlocale(locale.LC_ALL, self.__origDefault)
        zoneinfo.ZoneInfo.clear_cache()
        datetime.timezone = self.__defaultZone

    def setUp(self) -> None:
        super().setUp()
        self._validator = TimeValidator.TimeValidator1()
        self.__defaultZone = zoneinfo.ZoneInfo(os.environ.get("TZ", "UTC"))
        self.__origDefault = locale.getdefaultlocale()

    @staticmethod
    def _createDate(
        zone: typing.Union[zoneinfo.ZoneInfo, datetime.timezone],
        time: int,
        millisecond: int,
    ) -> typing.Union[datetime.datetime, datetime.date]:
        calendar = TimeValidatorTest._createTime(zone, time, millisecond)
        return calendar

    @staticmethod
    def _createTime(
        zone: typing.Union[zoneinfo.ZoneInfo, datetime.timezone, None],
        time: int,
        millisecond: int,
    ) -> datetime.datetime:
        if zone is None:
            zone = datetime.timezone.utc  # Default to UTC if no zone is provided
        hour = (time // 10000) * 10000
        minute = (time // 100) * 100 - hour
        second = time - (hour + minute)
        hour //= 10000
        minute //= 100

        # Create a datetime object with the specified time and millisecond
        dt = datetime.datetime(
            year=1970,
            month=1,
            day=1,
            hour=hour,
            minute=minute,
            second=second,
            microsecond=millisecond * 1000,
            tzinfo=zone,
        )
        return dt


TimeValidatorTest.initialize_fields()
