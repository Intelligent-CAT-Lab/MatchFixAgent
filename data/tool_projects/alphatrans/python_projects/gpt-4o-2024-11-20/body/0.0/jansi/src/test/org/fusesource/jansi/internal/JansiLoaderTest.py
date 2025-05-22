from __future__ import annotations
import re
import unittest
import pytest
import io
import os
import unittest
from src.main.org.fusesource.jansi.internal.JansiLoader import *


class JansiLoaderTest(unittest.TestCase):

    def testLoadJansi_test0_decomposed(self) -> None:
        JansiLoader.initialize()
