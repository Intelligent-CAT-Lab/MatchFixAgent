from __future__ import annotations
import re
import unittest
import pytest
import io
import os
import unittest
from src.main.org.apache.commons.csv.IOUtils import *


class IOUtilsTest(unittest.TestCase):

    def testRethrow_test0_decomposed(self) -> None:
        with self.assertRaisesExactly(OSError):
            IOUtils.rethrow(OSError())
