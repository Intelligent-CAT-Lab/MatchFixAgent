from __future__ import annotations
import re
import unittest
import pytest
import io
import unittest
from src.main.org.fusesource.jansi.internal.Kernel32 import *


class Kernel32Test(unittest.TestCase):

    def testErrorMessage(self) -> None:
        msg = Kernel32.getErrorMessage(500)
        self.assertEqual(msg, "User profile cannot be loaded.")
