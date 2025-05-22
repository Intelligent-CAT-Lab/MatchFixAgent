from __future__ import annotations
import time
import re
import datetime
import unittest
import pytest
import io
import os
import unittest
from src.main.org.apache.commons.pool2.impl.EvictionConfig import *


class TestEvictionConfig(unittest.TestCase):

    def testConstructorZerosMillis_test7_decomposed(self) -> None:
        config = EvictionConfig.EvictionConfig0(0, 0, 0)
        self.assertEqual(float("inf"), config.getIdleEvictDuration().total_seconds())
        self.assertEqual(float("inf"), config.getIdleEvictTime() / 1000)
        self.assertEqual(
            float("inf"), config.getIdleEvictTimeDuration().total_seconds()
        )
        self.assertEqual(
            float("inf"), config.getIdleSoftEvictDuration().total_seconds()
        )
        self.assertEqual(float("inf"), config.getIdleSoftEvictTime() / 1000)
        self.assertEqual(
            float("inf"), config.getIdleSoftEvictTimeDuration().total_seconds()
        )
        self.assertEqual(0, config.getMinIdle())

    def testConstructorZerosMillis_test6_decomposed(self) -> None:
        config = EvictionConfig.EvictionConfig0(0, 0, 0)
        self.assertEqual(float("inf"), config.getIdleEvictDuration().total_seconds())
        self.assertEqual(float("inf"), config.getIdleEvictTime())
        self.assertEqual(
            float("inf"), config.getIdleEvictTimeDuration().total_seconds()
        )
        self.assertEqual(
            float("inf"), config.getIdleSoftEvictDuration().total_seconds()
        )
        self.assertEqual(float("inf"), config.getIdleSoftEvictTime())
        self.assertEqual(
            float("inf"), config.getIdleSoftEvictTimeDuration().total_seconds()
        )

    def testConstructorZerosMillis_test5_decomposed(self) -> None:
        config = EvictionConfig.EvictionConfig0(0, 0, 0)
        self.assertEqual(float("inf"), config.getIdleEvictDuration().total_seconds())
        self.assertEqual(float("inf"), config.getIdleEvictTime() / 1000)
        self.assertEqual(
            float("inf"), config.getIdleEvictTimeDuration().total_seconds()
        )
        self.assertEqual(
            float("inf"), config.getIdleSoftEvictDuration().total_seconds()
        )
        self.assertEqual(float("inf"), config.getIdleSoftEvictTime() / 1000)

    def testConstructorZerosMillis_test4_decomposed(self) -> None:
        config = EvictionConfig.EvictionConfig0(0, 0, 0)
        self.assertEqual(datetime.timedelta.max, config.getIdleEvictDuration())
        self.assertEqual(float("inf"), config.getIdleEvictTime())
        self.assertEqual(datetime.timedelta.max, config.getIdleEvictTimeDuration())
        self.assertEqual(datetime.timedelta.max, config.getIdleSoftEvictDuration())

    def testConstructorZerosMillis_test3_decomposed(self) -> None:
        config = EvictionConfig.EvictionConfig0(0, 0, 0)
        self.assertEqual(float("inf"), config.getIdleEvictDuration().total_seconds())
        self.assertEqual(float("inf"), config.getIdleEvictTime() / 1000)
        self.assertEqual(
            float("inf"), config.getIdleEvictTimeDuration().total_seconds()
        )

    def testConstructorZerosMillis_test2_decomposed(self) -> None:
        config = EvictionConfig.EvictionConfig0(0, 0, 0)
        self.assertEqual(float("inf"), config.getIdleEvictDuration().total_seconds())
        self.assertEqual(float("inf"), config.getIdleEvictTime() / 1000)

    def testConstructorZerosMillis_test1_decomposed(self) -> None:
        with pytest.deprecated_call():
            config = EvictionConfig.EvictionConfig0(0, 0, 0)
        self.assertEqual(datetime.timedelta.max, config.getIdleEvictDuration())

    def testConstructorZerosMillis_test0_decomposed(self) -> None:
        config = EvictionConfig.EvictionConfig0(0, 0, 0)

    def testConstructorZerosDurations_test7_decomposed(self) -> None:
        config = EvictionConfig(datetime.timedelta(0), datetime.timedelta(0), 0)
        self.assertEqual(
            datetime.timedelta.max.total_seconds() * 1000,
            config.getIdleEvictDuration().total_seconds() * 1000,
        )
        self.assertEqual(
            datetime.timedelta.max.total_seconds() * 1000, config.getIdleEvictTime()
        )
        self.assertEqual(
            datetime.timedelta.max.total_seconds() * 1000,
            config.getIdleEvictTimeDuration().total_seconds() * 1000,
        )
        self.assertEqual(
            datetime.timedelta.max.total_seconds() * 1000,
            config.getIdleSoftEvictDuration().total_seconds() * 1000,
        )
        self.assertEqual(
            datetime.timedelta.max.total_seconds() * 1000, config.getIdleSoftEvictTime()
        )
        self.assertEqual(
            datetime.timedelta.max.total_seconds() * 1000,
            config.getIdleSoftEvictTimeDuration().total_seconds() * 1000,
        )
        self.assertEqual(0, config.getMinIdle())

    def testConstructorZerosDurations_test6_decomposed(self) -> None:
        config = EvictionConfig(datetime.timedelta(0), datetime.timedelta(0), 0)
        self.assertEqual(float("inf"), config.getIdleEvictDuration().total_seconds())
        self.assertEqual(float("inf"), config.getIdleEvictTime())
        self.assertEqual(
            float("inf"), config.getIdleEvictTimeDuration().total_seconds()
        )
        self.assertEqual(
            float("inf"), config.getIdleSoftEvictDuration().total_seconds()
        )
        self.assertEqual(float("inf"), config.getIdleSoftEvictTime())
        self.assertEqual(
            float("inf"), config.getIdleSoftEvictTimeDuration().total_seconds()
        )

    def testConstructorZerosDurations_test5_decomposed(self) -> None:
        config = EvictionConfig(datetime.timedelta(0), datetime.timedelta(0), 0)
        self.assertEqual(
            float("inf"), config.getIdleEvictDuration().total_seconds() * 1000
        )
        self.assertEqual(float("inf"), config.getIdleEvictTime())
        self.assertEqual(
            float("inf"), config.getIdleEvictTimeDuration().total_seconds() * 1000
        )
        self.assertEqual(
            float("inf"), config.getIdleSoftEvictDuration().total_seconds() * 1000
        )
        self.assertEqual(float("inf"), config.getIdleSoftEvictTime())

    def testConstructorZerosDurations_test4_decomposed(self) -> None:
        config = EvictionConfig(datetime.timedelta(0), datetime.timedelta(0), 0)
        self.assertEqual(
            float("inf"), config.getIdleEvictDuration().total_seconds() * 1000
        )
        self.assertEqual(float("inf"), config.getIdleEvictTime())
        self.assertEqual(
            float("inf"), config.getIdleEvictTimeDuration().total_seconds() * 1000
        )
        self.assertEqual(
            float("inf"), config.getIdleSoftEvictDuration().total_seconds() * 1000
        )

    def testConstructorZerosDurations_test3_decomposed(self) -> None:
        config = EvictionConfig(datetime.timedelta(0), datetime.timedelta(0), 0)
        self.assertEqual(
            datetime.timedelta.max.total_seconds() * 1000,
            config.getIdleEvictDuration().total_seconds() * 1000,
        )
        self.assertEqual(
            datetime.timedelta.max.total_seconds() * 1000, config.getIdleEvictTime()
        )
        self.assertEqual(
            datetime.timedelta.max.total_seconds() * 1000,
            config.getIdleEvictTimeDuration().total_seconds() * 1000,
        )

    def testConstructorZerosDurations_test2_decomposed(self) -> None:
        config = EvictionConfig(datetime.timedelta(0), datetime.timedelta(0), 0)
        self.assertEqual(
            datetime.timedelta.max.total_seconds() * 1000,
            config.getIdleEvictDuration().total_seconds() * 1000,
        )
        self.assertEqual(
            int(datetime.timedelta.max.total_seconds() * 1000),
            config.getIdleEvictTime(),
        )

    def testConstructorZerosDurations_test1_decomposed(self) -> None:
        config = EvictionConfig(datetime.timedelta(0), datetime.timedelta(0), 0)
        self.assertEqual(
            datetime.timedelta.max.total_seconds() * 1000,
            config.getIdleEvictDuration().total_seconds() * 1000,
        )

    def testConstructorZerosDurations_test0_decomposed(self) -> None:
        config = EvictionConfig(datetime.timedelta(0), datetime.timedelta(0), 0)

    def testConstructor1s_test7_decomposed(self) -> None:
        config = EvictionConfig(
            datetime.timedelta(milliseconds=1), datetime.timedelta(milliseconds=1), 1
        )
        self.assertEqual(1, config.getIdleEvictDuration().total_seconds() * 1000)
        self.assertEqual(1, config.getIdleEvictTime())
        self.assertEqual(1, config.getIdleEvictTimeDuration().total_seconds() * 1000)
        self.assertEqual(1, config.getIdleSoftEvictDuration().total_seconds() * 1000)
        self.assertEqual(1, config.getIdleSoftEvictTime())
        self.assertEqual(
            1, config.getIdleSoftEvictTimeDuration().total_seconds() * 1000
        )
        self.assertEqual(1, config.getMinIdle())

    def testConstructor1s_test6_decomposed(self) -> None:
        config = EvictionConfig(
            datetime.timedelta(milliseconds=1), datetime.timedelta(milliseconds=1), 1
        )
        self.assertEqual(1, config.getIdleEvictDuration().total_seconds() * 1000)
        self.assertEqual(1, config.getIdleEvictTime())
        self.assertEqual(1, config.getIdleEvictTimeDuration().total_seconds() * 1000)
        self.assertEqual(1, config.getIdleSoftEvictDuration().total_seconds() * 1000)
        self.assertEqual(1, config.getIdleSoftEvictTime())
        self.assertEqual(
            1, config.getIdleSoftEvictTimeDuration().total_seconds() * 1000
        )

    def testConstructor1s_test5_decomposed(self) -> None:
        config = EvictionConfig(
            datetime.timedelta(milliseconds=1), datetime.timedelta(milliseconds=1), 1
        )
        self.assertEqual(1, config.getIdleEvictDuration().total_seconds() * 1000)
        self.assertEqual(1, config.getIdleEvictTime())
        self.assertEqual(1, config.getIdleEvictTimeDuration().total_seconds() * 1000)
        self.assertEqual(1, config.getIdleSoftEvictDuration().total_seconds() * 1000)
        self.assertEqual(1, config.getIdleSoftEvictTime())

    def testConstructor1s_test4_decomposed(self) -> None:
        config = EvictionConfig(
            datetime.timedelta(milliseconds=1), datetime.timedelta(milliseconds=1), 1
        )
        self.assertEqual(1, config.getIdleEvictDuration().total_seconds() * 1000)
        self.assertEqual(1, config.getIdleEvictTime())
        self.assertEqual(1, config.getIdleEvictTimeDuration().total_seconds() * 1000)
        self.assertEqual(1, config.getIdleSoftEvictDuration().total_seconds() * 1000)

    def testConstructor1s_test3_decomposed(self) -> None:
        config = EvictionConfig(
            datetime.timedelta(milliseconds=1), datetime.timedelta(milliseconds=1), 1
        )
        self.assertEqual(1, config.getIdleEvictDuration().total_seconds() * 1000)
        self.assertEqual(1, config.getIdleEvictTime())
        self.assertEqual(1, config.getIdleEvictTimeDuration().total_seconds() * 1000)

    def testConstructor1s_test2_decomposed(self) -> None:
        config = EvictionConfig(
            datetime.timedelta(milliseconds=1), datetime.timedelta(milliseconds=1), 1
        )
        self.assertEqual(1, config.getIdleEvictDuration().total_seconds() * 1000)
        self.assertEqual(1, config.getIdleEvictTime())

    def testConstructor1s_test1_decomposed(self) -> None:
        config = EvictionConfig(
            datetime.timedelta(milliseconds=1), datetime.timedelta(milliseconds=1), 1
        )
        self.assertEqual(1, config.getIdleEvictDuration().total_seconds() * 1000)

    def testConstructor1s_test0_decomposed(self) -> None:
        config = EvictionConfig(
            datetime.timedelta(milliseconds=1), datetime.timedelta(milliseconds=1), 1
        )
