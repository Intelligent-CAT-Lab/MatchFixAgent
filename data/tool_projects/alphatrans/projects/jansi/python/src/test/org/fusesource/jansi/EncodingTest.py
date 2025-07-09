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
from src.main.org.fusesource.jansi.AnsiPrintStream import *
from src.main.org.fusesource.jansi.AnsiType import *
from src.main.org.fusesource.jansi.io.AnsiOutputStream import *
from src.main.org.fusesource.jansi.io.AnsiProcessor import *


class EncodingTest(unittest.TestCase):

    def testEncodingUtf8_test2_decomposed(self) -> None:
        baos = io.BytesIO()
        new_label = [None]  # Using a list to simulate AtomicReference

        class CustomAnsiProcessor(AnsiProcessor):
            def __init__(self, os):
                super().__init__(
                    os,
                    None,
                    AnsiMode.Default,
                    None,
                    AnsiType.Emulation,
                    AnsiColors.TrueColor,
                    "UTF-8",
                    None,
                    None,
                    False,
                )

            def processChangeWindowTitle(self, label: str) -> None:
                new_label[0] = label

        ansi = AnsiPrintStream(
            AnsiOutputStream(
                baos,
                None,
                AnsiMode.Default,
                CustomAnsiProcessor(baos),
                AnsiType.Emulation,
                AnsiColors.TrueColor,
                "UTF-8",
                None,
                None,
                False,
            ),
            True,
            "UTF-8",
        )

        ansi.print("\033]0;ひらがな\007")
        ansi.flush()

        self.assertEqual("ひらがな", new_label[0])

    def testEncodingUtf8_test1_decomposed(self) -> None:
        baos = io.BytesIO()
        new_label = None

        class CustomAnsiProcessor(AnsiProcessor):
            def __init__(self, os):
                super().__init__(
                    os,
                    None,
                    AnsiMode.Default,
                    None,
                    AnsiType.Emulation,
                    AnsiColors.TrueColor,
                    "UTF-8",
                    None,
                    None,
                    False,
                )

            def processChangeWindowTitle(self, label: str) -> None:
                nonlocal new_label
                new_label = label

        ansi = AnsiPrintStream(
            AnsiOutputStream(
                baos,
                None,
                AnsiMode.Default,
                CustomAnsiProcessor(baos),
                AnsiType.Emulation,
                AnsiColors.TrueColor,
                "UTF-8",
                None,
                None,
                False,
            ),
            True,
            "UTF-8",
        )
        ansi.print("\033]0;ひらがな\007")
        ansi.flush()

    def testEncodingUtf8_test0_decomposed(self) -> None:
        baos = io.BytesIO()
        new_label = None

        class CustomAnsiProcessor(AnsiProcessor):
            def __init__(self, os: io.BytesIO) -> None:
                super().__init__(
                    os,
                    None,
                    AnsiMode.Default,
                    None,
                    AnsiType.Emulation,
                    AnsiColors.TrueColor,
                    "UTF-8",
                    None,
                    None,
                    False,
                )

            def processChangeWindowTitle(self, label: str) -> None:
                nonlocal new_label
                new_label = label

        ansi = AnsiPrintStream(
            AnsiOutputStream(
                baos,
                None,
                AnsiMode.Default,
                CustomAnsiProcessor(baos),
                AnsiType.Emulation,
                AnsiColors.TrueColor,
                "UTF-8",
                None,
                None,
                False,
            ),
            True,
            "UTF-8",
        )
        ansi.print("\033]0;ひらがな\007")

    def testEncoding8859_test3_decomposed(self) -> None:
        baos = io.BytesIO()
        new_label = None

        class CustomAnsiProcessor(AnsiProcessor):
            def __init__(self, os):
                super().__init__(os)

            def processChangeWindowTitle(self, label: str) -> None:
                nonlocal new_label
                new_label = label

        ansi = AnsiPrintStream(
            AnsiOutputStream(
                baos,
                None,
                AnsiMode.Default,
                CustomAnsiProcessor(baos),
                AnsiType.Emulation,
                AnsiColors.TrueColor,
                "ISO-8859-1",
                None,
                None,
                False,
            ),
            True,
            "ISO-8859-1",
        )

        ansi.print("\033]0;un bon café\007")
        ansi.flush()

        self.assertEqual("un bon café", new_label)

    def testEncoding8859_test2_decomposed(self) -> None:
        baos = io.BytesIO()
        new_label = None

        class CustomAnsiProcessor(AnsiProcessor):
            def __init__(self, os):
                super().__init__(os)

            def processChangeWindowTitle(self, label: str) -> None:
                nonlocal new_label
                new_label = label

        ansi = AnsiPrintStream(
            AnsiOutputStream(
                baos,
                None,
                AnsiMode.Default,
                CustomAnsiProcessor(baos),
                AnsiType.Emulation,
                AnsiColors.TrueColor,
                "ISO-8859-1",
                None,
                None,
                False,
            ),
            True,
            "ISO-8859-1",
        )

        ansi.print("\033]0;un bon café\007")
        ansi.flush()

    def testEncoding8859_test1_decomposed(self) -> None:
        baos = io.BytesIO()
        new_label = None

        class CustomAnsiProcessor(AnsiProcessor):
            def __init__(self, os):
                super().__init__(os)

            def processChangeWindowTitle(self, label: str) -> None:
                nonlocal new_label
                new_label = label

        ansi = AnsiPrintStream(
            AnsiOutputStream(
                baos,
                None,
                AnsiMode.Default,
                CustomAnsiProcessor(baos),
                AnsiType.Emulation,
                AnsiColors.TrueColor,
                "ISO-8859-1",
                None,
                None,
                False,
            ),
            True,
            "ISO-8859-1",
        )
        ansi.print("\033]0;un bon café\007")

    def testEncoding8859_test0_decomposed(self) -> None:
        baos = io.BytesIO()
        new_label = None

        class CustomAnsiProcessor(AnsiProcessor):
            def __init__(self, os):
                super().__init__(os)

            def processChangeWindowTitle(self, label: str) -> None:
                nonlocal new_label
                new_label = label

        ansi = AnsiPrintStream(
            AnsiOutputStream(
                baos,
                None,
                AnsiMode.Default,
                CustomAnsiProcessor(baos),
                AnsiType.Emulation,
                AnsiColors.TrueColor,
                "ISO-8859-1",
                None,
                None,
                False,
            ),
            True,
            "ISO-8859-1",
        )
