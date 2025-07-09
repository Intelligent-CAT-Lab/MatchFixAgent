from __future__ import annotations
import re
import unittest
import pytest
import io
import os
import unittest
from src.main.org.apache.commons.codec.digest.Sha2Crypt import *


class Sha2CryptTest(unittest.TestCase):

    def testCtor_test0_decomposed(self) -> None:
        self.assertIsNotNone(Sha2Crypt())
