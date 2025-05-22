from __future__ import annotations
import re
import threading
import unittest
import pytest
import io
import os
import unittest
from src.main.org.fusesource.jansi.Ansi import *
from src.main.org.fusesource.jansi.AnsiMain import *


class AnsiTest(unittest.TestCase):

    def testColorDisabled_test1_decomposed(self) -> None:
        Ansi.setEnabled(False)
        try:
            self.assertEqual(
                "test",
                Ansi.ansi0()
                .fg1(32)
                .a1("t")
                .fgRgb0(0)
                .a1("e")
                .bg1(24)
                .a1("s")
                .bgRgb0(100)
                .a1("t")
                .toString(),
            )
        finally:
            Ansi.setEnabled(True)

    def testColorDisabled_test0_decomposed(self) -> None:
        Ansi.setEnabled(False)

    def testCursorUpLine0_test1_decomposed(self) -> None:
        ansi_instance = Ansi.Ansi0()
        self.__assertAnsi("ESC[F", ansi_instance.cursorUpLine0())

    def testCursorUpLine0_test0_decomposed(self) -> None:
        Ansi.Ansi0()

    def testCursorDownLine0_test1_decomposed(self) -> None:
        Ansi.Ansi0()
        self.__assertAnsi("ESC[E", Ansi.Ansi0().cursorDownLine0())

    def testCursorDownLine0_test0_decomposed(self) -> None:
        Ansi.Ansi0()

    def testApply_test2_decomposed(self) -> None:
        Ansi.ansi0()
        Ansi.ansi0().apply(lambda ansi: ansi.a1("test"))
        self.assertEqual(
            "test", Ansi.ansi0().apply(lambda ansi: ansi.a1("test")).toString()
        )

    def testApply_test1_decomposed(self) -> None:
        Ansi.ansi0()
        Ansi.ansi0().apply(lambda ansi: ansi.a1("test"))

    def testApply_test0_decomposed(self) -> None:
        Ansi.ansi0()

    def testClone(self) -> None:
        ansi = Ansi.ansi0().a1("Some text").bg0(Color.BLACK).fg0(Color.WHITE)
        clone = Ansi.Ansi1(ansi)

        self.assertEqual(
            ansi.a1("test").reset().toString(), clone.a1("test").reset().toString()
        )

    def testClone_test6_decomposed(self) -> None:
        Ansi.ansi0()
        Ansi.ansi0().a1("Some text")
        Ansi.ansi0().a1("Some text").bg0(Color.BLACK)
        ansi = Ansi.ansi0().a1("Some text").bg0(Color.BLACK).fg0(Color.WHITE)
        clone = Ansi.Ansi1(ansi)
        ansi.a1("test")
        clone.a1("test")
        ansi.a1("test").reset()
        clone.a1("test").reset()

    def testClone_test5_decomposed(self) -> None:
        Ansi.ansi0()
        Ansi.ansi0().a1("Some text")
        Ansi.ansi0().a1("Some text").bg0(Ansi.Color.BLACK)
        ansi = Ansi.ansi0().a1("Some text").bg0(Ansi.Color.BLACK).fg0(Ansi.Color.WHITE)
        clone = Ansi.Ansi1(ansi)
        ansi.a1("test")
        clone.a1("test")

    def testClone_test4_decomposed(self) -> None:
        Ansi.ansi0()
        Ansi.ansi0().a1("Some text")
        Ansi.ansi0().a1("Some text").bg0(Color.BLACK)
        ansi = Ansi.ansi0().a1("Some text").bg0(Color.BLACK).fg0(Color.WHITE)
        clone = Ansi.Ansi1(ansi)

    def testClone_test3_decomposed(self) -> None:
        Ansi.ansi0()
        Ansi.ansi0().a1("Some text")
        Ansi.ansi0().a1("Some text").bg0(Ansi.Color.BLACK)
        ansi = Ansi.ansi0().a1("Some text").bg0(Ansi.Color.BLACK).fg0(Ansi.Color.WHITE)

    def testClone_test2_decomposed(self) -> None:
        Ansi.ansi0()
        Ansi.ansi0().a1("Some text")
        Ansi.ansi0().a1("Some text").bg0(Ansi.Color.BLACK)

    def testClone_test1_decomposed(self) -> None:
        Ansi.ansi0()
        Ansi.ansi0().a1("Some text")

    def testClone_test0_decomposed(self) -> None:
        Ansi.ansi0()

    def testSetEnabled_test5_decomposed(self) -> None:
        Ansi.setEnabled(False)
        self.assertFalse(Ansi.isEnabled())

        # Run a thread to check the value of Ansi.isEnabled()
        thread1 = threading.Thread(target=lambda: self.assertFalse(Ansi.isEnabled()))
        thread1.start()
        thread1.join()

        Ansi.setEnabled(True)
        self.assertTrue(Ansi.isEnabled())

        # Run another thread to check the value of Ansi.isEnabled()
        thread2 = threading.Thread(target=lambda: self.assertTrue(Ansi.isEnabled()))
        thread2.start()
        thread2.join()

    def testSetEnabled_test4_decomposed(self) -> None:
        Ansi.setEnabled(False)
        self.assertFalse(Ansi.isEnabled())

        # Simulate a new thread by using a lambda function and running it directly
        (lambda: self.assertFalse(Ansi.isEnabled()))()

        Ansi.setEnabled(True)
        self.assertTrue(Ansi.isEnabled())

    def testSetEnabled_test3_decomposed(self) -> None:
        Ansi.setEnabled(False)
        self.assertFalse(Ansi.isEnabled())

        # Simulate the behavior of a thread
        def thread_function():
            self.assertFalse(Ansi.isEnabled())

        thread_function()  # Directly call the function to simulate thread execution

        Ansi.setEnabled(True)

    def testSetEnabled_test2_decomposed(self) -> None:
        Ansi.setEnabled(False)
        self.assertFalse(Ansi.isEnabled())

        def thread_function():
            self.assertFalse(Ansi.isEnabled())

        # Simulate running the thread
        thread_function()

    def testSetEnabled_test1_decomposed(self) -> None:
        Ansi.setEnabled(False)
        self.assertFalse(Ansi.isEnabled())

    def testSetEnabled_test0_decomposed(self) -> None:
        Ansi.setEnabled(False)

    def testAnsiMainWithNoConsole(self) -> None:
        java_home = os.getenv("JAVA_HOME")
        if not java_home:
            self.fail("JAVA_HOME environment variable is not set")

        java = os.path.join(java_home, "bin", "javaw.exe")
        cp = os.getenv("CLASSPATH")
        if not cp:
            self.fail("CLASSPATH environment variable is not set")

        process = subprocess.Popen(
            [java, "-cp", cp, AnsiMain.__name__],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )

        stdout, _ = process.communicate()
        output = stdout.decode("utf-8")

        self.assertTrue("test on System.out" in output, output)

    @pytest.mark.skip(reason="Ignore")
    def testCursorUpLine1(self, n: int, expected: str) -> None:
        self.__assertAnsi(expected, Ansi.Ansi0().cursorUpLine1(n))

    @pytest.mark.skip(reason="Ignore")
    def testCursorDownLine1(self, n: int, expected: str) -> None:
        self.__assertAnsi(expected, Ansi.Ansi0().cursorDownLine1(n))

    @pytest.mark.skip(reason="Ignore")
    def testCursorMove(self, x: int, y: int, expected: str) -> None:
        self.__assertAnsi(expected, Ansi.Ansi0().cursorMove(x, y))

    @pytest.mark.skip(reason="Ignore")
    def testCursorLeft(self, x: int, expected: str) -> None:
        self.__assertAnsi(expected, Ansi.Ansi0().cursorLeft(x))

    @pytest.mark.skip(reason="Ignore")
    def testCursorRight(self, x: int, expected: str) -> None:
        self.__assertAnsi(expected, Ansi.Ansi0().cursorRight(x))

    @pytest.mark.skip(reason="Ignore")
    def testCursorDown(self, y: int, expected: str) -> None:
        self.__assertAnsi(expected, Ansi.Ansi0().cursorDown(y))

    @pytest.mark.skip(reason="Ignore")
    def testCursorUp(self, y: int, expected: str) -> None:
        self.__assertAnsi(expected, Ansi.Ansi0().cursorUp(y))

    @pytest.mark.skip(reason="Ignore")
    def testCursorToColumn(self, x: int, expected: str) -> None:
        self.__assertAnsi(expected, Ansi.Ansi0().cursorToColumn(x))

    @pytest.mark.skip(reason="Ignore")
    def testCursor(self, x: int, y: int, expected: str) -> None:
        self.__assertAnsi(expected, Ansi.Ansi0().cursor(x, y))

    @pytest.mark.skip(reason="Ignore")
    def testScrollDown(self, x: int, expected: str) -> None:
        self.__assertAnsi(expected, Ansi.ansi0().scrollDown(x))

    @pytest.mark.skip(reason="Ignore")
    def testScrollUp(self, x: int, expected: str) -> None:
        self.__assertAnsi(expected, Ansi.ansi0().scrollUp(x))

    @staticmethod
    def __assertAnsi(expected: str, actual: Ansi) -> None:
        assert expected.replace("ESC", "\033") == actual.toString()
