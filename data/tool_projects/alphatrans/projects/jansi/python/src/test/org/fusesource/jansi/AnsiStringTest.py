from __future__ import annotations
import re
import unittest
import pytest
import io
import os
import unittest
from src.main.org.fusesource.jansi.Ansi import *


class AnsiStringTest(unittest.TestCase):

    def testCursorPosition_test3_decomposed(self) -> None:
        Ansi.ansi0()
        Ansi.ansi0().cursor(3, 6)
        ansi = Ansi.ansi0().cursor(3, 6).reset()
        self.assertEqual("\u001b[3;6H\u001b[m", ansi.toString())

    def testCursorPosition_test2_decomposed(self) -> None:
        Ansi.ansi0()
        Ansi.ansi0().cursor(3, 6)
        ansi = Ansi.ansi0().cursor(3, 6).reset()

    def testCursorPosition_test1_decomposed(self) -> None:
        Ansi.ansi0()
        Ansi.ansi0().cursor(3, 6)

    def testCursorPosition_test0_decomposed(self) -> None:
        Ansi.ansi0()
