from __future__ import annotations
import re
import unittest
import pytest
import io
import os
import unittest
from src.main.org.apache.commons.codec.net.Utils import *


class UtilsTest(unittest.TestCase):

    def testConstructor_test0_decomposed(self) -> None:
        Utils()
