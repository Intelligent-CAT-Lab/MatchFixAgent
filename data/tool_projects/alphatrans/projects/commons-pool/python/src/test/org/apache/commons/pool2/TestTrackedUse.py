from __future__ import annotations
import time
import re
import datetime
import unittest
import pytest
import io
import os
import unittest
from src.main.org.apache.commons.pool2.TrackedUse import *


class TestTrackedUse(unittest.TestCase):

    def testDefaultGetLastUsedInstant_test0_decomposed(self) -> None:
        self.assertEqual(
            datetime.datetime.fromtimestamp(1 / 1000.0),
            DefaultTrackedUse().getLastUsedInstant(),
        )


class DefaultTrackedUse(TrackedUse):

    def getLastUsed(self) -> int:
        return 1
