from __future__ import annotations
import re
import typing
from typing import *
from io import BytesIO
import unittest
import pytest
import io
import os
import unittest
from src.main.org.fusesource.jansi.AnsiColors import *
from src.main.org.fusesource.jansi.AnsiMode import *
from src.main.org.fusesource.jansi.AnsiType import *
from src.main.org.fusesource.jansi.io.AnsiOutputStream import *
from src.main.org.fusesource.jansi.io.AnsiProcessor import *


class AnsiOutputStreamTest(unittest.TestCase):

    def testcanHandleSgrsWithMultipleOptions_test2_decomposed(self) -> None:
        baos = io.BytesIO()
        ansi_output = AnsiOutputStream(
            baos,
            None,
            AnsiMode.Strip,
            None,
            AnsiType.Emulation,
            AnsiColors.TrueColor,
            "utf-8",
            None,
            None,
            False
        )
        ansi_output.write(
            b"\u001B[33mbanana_1  |\u001B[0m 19:59:14.353\u001B[0;38m [debug] A message\u001B[0m\n"
        )
        self.assertEqual(
            "banana_1  | 19:59:14.353 [debug] A message\n", baos.getvalue().decode("utf-8")
        )
    def testcanHandleSgrsWithMultipleOptions_test1_decomposed(self) -> None:
        baos = io.BytesIO()
        ansi_output = AnsiOutputStream(
            baos,
            None,
            AnsiMode.Strip,
            None,
            AnsiType.Emulation,
            AnsiColors.TrueColor,
            "utf-8",
            None,
            None,
            False
        )
        ansi_output.write(
            b"\x1B[33mbanana_1  |\x1B[0m 19:59:14.353\x1B[0;38m [debug] A message\x1B[0m\n"
        )
    def testcanHandleSgrsWithMultipleOptions_test0_decomposed(self) -> None:
        baos = io.BytesIO()
        ansi_output = AnsiProcessor(
            os=baos,
            width=None,
            mode=AnsiMode.Strip,
            processor=None,
            type_=AnsiType.Emulation,
            colors=AnsiColors.TrueColor,
            cs="utf-8",
            installer=None,
            uninstaller=None,
            resetAtUninstall=False
        )
