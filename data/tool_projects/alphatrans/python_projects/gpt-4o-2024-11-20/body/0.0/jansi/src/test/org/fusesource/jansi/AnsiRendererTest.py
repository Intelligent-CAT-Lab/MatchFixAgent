from __future__ import annotations
import re
import unittest
import pytest
import io
import os
import unittest
from src.main.org.fusesource.jansi.Ansi import *
from src.main.org.fusesource.jansi.AnsiRenderer import *


class AnsiRendererTest(unittest.TestCase):

    def testRenderInvalidMissingText_test1_decomposed(self) -> None:
        str_ = AnsiRenderer.render0("@|bold|@")
        self.assertEqual("@|bold|@", str_)

    def testRenderInvalidMissingText_test0_decomposed(self) -> None:
        str_ = AnsiRenderer.render0("@|bold|@")

    def testRenderInvalidEndBeforeStart_test0_decomposed(self) -> None:
        with self.assertRaises(ValueError):
            render0("@|@")

    def testRenderInvalidMissingEnd_test1_decomposed(self) -> None:
        str_ = AnsiRenderer.render0("@|bold foo")
        self.assertEqual("@|bold foo", str_)

    def testRenderInvalidMissingEnd_test0_decomposed(self) -> None:
        str_ = AnsiRenderer.render0("@|bold foo")

    def testRenderNothing_test0_decomposed(self) -> None:
        self.assertEqual("foo", AnsiRenderer.render0("foo"))

    def testRender5_test7_decomposed(self) -> None:
        ansi_instance = Ansi.ansi0()
        ansi_instance.render0("@|bold Hello|@")
        str_value = Ansi.ansi0().render0("@|bold Hello|@").toString()
        print(str_value)
        Ansi.ansi0()
        Ansi.ansi0().a0(Attribute.INTENSITY_BOLD)
        Ansi.ansi0().a0(Attribute.INTENSITY_BOLD).a1("Hello")
        Ansi.ansi0().a0(Attribute.INTENSITY_BOLD).a1("Hello").reset()
        self.assertEqual(
            Ansi.ansi0().a0(Attribute.INTENSITY_BOLD).a1("Hello").reset().toString(),
            str_value,
        )

    def testRender5_test6_decomposed(self) -> None:
        Ansi.ansi0()
        Ansi.ansi0().render0("@|bold Hello|@")
        str_value = Ansi.ansi0().render0("@|bold Hello|@").toString()
        print(str_value)
        Ansi.ansi0()
        Ansi.ansi0().a0(Attribute.INTENSITY_BOLD)
        Ansi.ansi0().a0(Attribute.INTENSITY_BOLD).a1("Hello")
        Ansi.ansi0().a0(Attribute.INTENSITY_BOLD).a1("Hello").reset()

    def testRender5_test5_decomposed(self) -> None:
        Ansi.ansi0()
        Ansi.ansi0().render0("@|bold Hello|@")
        str_value = Ansi.ansi0().render0("@|bold Hello|@").toString()
        print(str_value)
        Ansi.ansi0()
        Ansi.ansi0().a0(Attribute.INTENSITY_BOLD)
        Ansi.ansi0().a0(Attribute.INTENSITY_BOLD).a1("Hello")

    def testRender5_test4_decomposed(self) -> None:
        Ansi.ansi0()
        Ansi.ansi0().render0("@|bold Hello|@")
        str_value = Ansi.ansi0().render0("@|bold Hello|@").toString()
        print(str_value)
        Ansi.ansi0()
        Ansi.ansi0().a0(INTENSITY_BOLD)

    def testRender5_test3_decomposed(self) -> None:
        ansi_instance = Ansi.ansi0()
        ansi_instance.render0("@|bold Hello|@")
        str_value = ansi_instance.render0("@|bold Hello|@").toString()
        print(str_value)
        Ansi.ansi0()

    def testRender5_test2_decomposed(self) -> None:
        ansi_instance = Ansi.ansi0()
        ansi_instance.render0("@|bold Hello|@")
        str_value = ansi_instance.render0("@|bold Hello|@").toString()

    def testRender5_test1_decomposed(self) -> None:
        Ansi.ansi0()
        Ansi.ansi0().render0("@|bold Hello|@")

    def testRender5_test0_decomposed(self) -> None:
        Ansi.ansi0()

    def testRender4_test6_decomposed(self) -> None:
        str_ = AnsiRenderer.render0(
            "@|bold,red foo bar baz|@ ick @|bold,red foo bar baz|@"
        )
        print(str_)
        ansi = Ansi.ansi0()
        ansi.a0(Attribute.INTENSITY_BOLD)
        ansi.a0(Attribute.INTENSITY_BOLD).fg0(Ansi.Color.RED)
        ansi.a0(Attribute.INTENSITY_BOLD).fg0(Ansi.Color.RED).a1("foo bar baz")
        ansi.a0(Attribute.INTENSITY_BOLD).fg0(Ansi.Color.RED).a1("foo bar baz").reset()
        ansi.a0(Attribute.INTENSITY_BOLD).fg0(Ansi.Color.RED).a1(
            "foo bar baz"
        ).reset().a1(" ick ")
        ansi.a0(Attribute.INTENSITY_BOLD).fg0(Ansi.Color.RED).a1(
            "foo bar baz"
        ).reset().a1(" ick ").a0(Attribute.INTENSITY_BOLD)
        ansi.a0(Attribute.INTENSITY_BOLD).fg0(Ansi.Color.RED).a1(
            "foo bar baz"
        ).reset().a1(" ick ").a0(Attribute.INTENSITY_BOLD).fg0(Ansi.Color.RED)
        ansi.a0(Attribute.INTENSITY_BOLD).fg0(Ansi.Color.RED).a1(
            "foo bar baz"
        ).reset().a1(" ick ").a0(Attribute.INTENSITY_BOLD).fg0(Ansi.Color.RED).a1(
            "foo bar baz"
        )
        ansi.a0(Attribute.INTENSITY_BOLD).fg0(Ansi.Color.RED).a1(
            "foo bar baz"
        ).reset().a1(" ick ").a0(Attribute.INTENSITY_BOLD).fg0(Ansi.Color.RED).a1(
            "foo bar baz"
        ).reset()
        self.assertEqual(
            Ansi.ansi0()
            .a0(Attribute.INTENSITY_BOLD)
            .fg0(Ansi.Color.RED)
            .a1("foo bar baz")
            .reset()
            .a1(" ick ")
            .a0(Attribute.INTENSITY_BOLD)
            .fg0(Ansi.Color.RED)
            .a1("foo bar baz")
            .reset()
            .toString(),
            str_,
        )

    def testRender4_test5_decomposed(self) -> None:

        pytest.fail("LLM could not translate this method")

    def testRender4_test4_decomposed(self) -> None:
        str_ = AnsiRenderer.render0(
            "@|bold,red foo bar baz|@ ick @|bold,red foo bar baz|@"
        )
        print(str_)
        Ansi.ansi0()
        Ansi.ansi0().a0(INTENSITY_BOLD)
        Ansi.ansi0().a0(INTENSITY_BOLD).fg0(RED)
        Ansi.ansi0().a0(INTENSITY_BOLD).fg0(RED).a1("foo bar baz")

    def testRender4_test3_decomposed(self) -> None:
        str_ = AnsiRenderer.render0(
            "@|bold,red foo bar baz|@ ick @|bold,red foo bar baz|@"
        )
        print(str_)
        Ansi.ansi0()
        Ansi.ansi0().a0(INTENSITY_BOLD)
        Ansi.ansi0().a0(INTENSITY_BOLD).fg0(RED)

    def testRender4_test2_decomposed(self) -> None:
        str_ = AnsiRenderer.render0(
            "@|bold,red foo bar baz|@ ick @|bold,red foo bar baz|@"
        )
        print(str_)
        Ansi.ansi0()
        Ansi.ansi0().a0(INTENSITY_BOLD)

    def testRender4_test1_decomposed(self) -> None:
        str_ = AnsiRenderer.render0(
            "@|bold,red foo bar baz|@ ick @|bold,red foo bar baz|@"
        )
        print(str_)
        Ansi.ansi0()

    def testRender4_test0_decomposed(self) -> None:
        str_ = AnsiRenderer.render0(
            "@|bold,red foo bar baz|@ ick @|bold,red foo bar baz|@"
        )

    def testRender3_test12_decomposed(self) -> None:
        str_ = AnsiRenderer.render0("@|bold,red foo bar baz|@")
        print(str_)
        Ansi.ansi0()
        Ansi.ansi0().a0(Attribute.INTENSITY_BOLD)
        Ansi.ansi0().a0(Attribute.INTENSITY_BOLD).fg0(Ansi.Color.RED)
        Ansi.ansi0().a0(Attribute.INTENSITY_BOLD).fg0(Ansi.Color.RED).a1("foo bar baz")
        Ansi.ansi0().a0(Attribute.INTENSITY_BOLD).fg0(Ansi.Color.RED).a1(
            "foo bar baz"
        ).reset()
        self.assertEqual(
            Ansi.ansi0()
            .a0(Attribute.INTENSITY_BOLD)
            .fg0(Ansi.Color.RED)
            .a1("foo bar baz")
            .reset()
            .toString(),
            str_,
        )
        Ansi.ansi0()
        Ansi.ansi0().bold()
        Ansi.ansi0().bold().fgRed()
        Ansi.ansi0().bold().fgRed().a1("foo bar baz")
        Ansi.ansi0().bold().fgRed().a1("foo bar baz").reset()
        self.assertEqual(
            Ansi.ansi0().bold().fgRed().a1("foo bar baz").reset().toString(), str_
        )

    def testRender3_test11_decomposed(self) -> None:
        str_ = AnsiRenderer.render0("@|bold,red foo bar baz|@")
        print(str_)
        Ansi.ansi0()
        Ansi.ansi0().a0(Attribute.INTENSITY_BOLD)
        Ansi.ansi0().a0(Attribute.INTENSITY_BOLD).fg0(Ansi.Color.RED)
        Ansi.ansi0().a0(Attribute.INTENSITY_BOLD).fg0(Ansi.Color.RED).a1("foo bar baz")
        Ansi.ansi0().a0(Attribute.INTENSITY_BOLD).fg0(Ansi.Color.RED).a1(
            "foo bar baz"
        ).reset()
        self.assertEqual(
            Ansi.ansi0()
            .a0(Attribute.INTENSITY_BOLD)
            .fg0(Ansi.Color.RED)
            .a1("foo bar baz")
            .reset()
            .toString(),
            str_,
        )
        Ansi.ansi0()
        Ansi.ansi0().bold()
        Ansi.ansi0().bold().fgRed()
        Ansi.ansi0().bold().fgRed().a1("foo bar baz")
        Ansi.ansi0().bold().fgRed().a1("foo bar baz").reset()

    def testRender3_test10_decomposed(self) -> None:
        str_ = AnsiRenderer.render0("@|bold,red foo bar baz|@")
        print(str_)

        # Decomposed ANSI rendering steps
        Ansi.ansi0()
        Ansi.ansi0().a0(Attribute.INTENSITY_BOLD)
        Ansi.ansi0().a0(Attribute.INTENSITY_BOLD).fg0(Ansi.Color.RED)
        Ansi.ansi0().a0(Attribute.INTENSITY_BOLD).fg0(Ansi.Color.RED).a1("foo bar baz")
        Ansi.ansi0().a0(Attribute.INTENSITY_BOLD).fg0(Ansi.Color.RED).a1(
            "foo bar baz"
        ).reset()

        # Assertion
        self.assertEqual(
            Ansi.ansi0()
            .a0(Attribute.INTENSITY_BOLD)
            .fg0(Ansi.Color.RED)
            .a1("foo bar baz")
            .reset()
            .toString(),
            str_,
        )

        # Additional ANSI rendering steps
        Ansi.ansi0()
        Ansi.ansi0().bold()
        Ansi.ansi0().bold().fgRed()
        Ansi.ansi0().bold().fgRed().a1("foo bar baz")

    def testRender3_test9_decomposed(self) -> None:
        str_ = AnsiRenderer.render0("@|bold,red foo bar baz|@")
        print(str_)
        Ansi.ansi0()
        Ansi.ansi0().a0(Attribute.INTENSITY_BOLD)
        Ansi.ansi0().a0(Attribute.INTENSITY_BOLD).fg0(Ansi.Color.RED)
        Ansi.ansi0().a0(Attribute.INTENSITY_BOLD).fg0(Ansi.Color.RED).a1("foo bar baz")
        Ansi.ansi0().a0(Attribute.INTENSITY_BOLD).fg0(Ansi.Color.RED).a1(
            "foo bar baz"
        ).reset()
        self.assertEqual(
            Ansi.ansi0()
            .a0(Attribute.INTENSITY_BOLD)
            .fg0(Ansi.Color.RED)
            .a1("foo bar baz")
            .reset()
            .toString(),
            str_,
        )
        Ansi.ansi0()
        Ansi.ansi0().bold()
        Ansi.ansi0().bold().fgRed()

    def testRender3_test8_decomposed(self) -> None:
        str_ = AnsiRenderer.render0("@|bold,red foo bar baz|@")
        print(str_)
        Ansi.ansi0()
        Ansi.ansi0().a0(Attribute.INTENSITY_BOLD)
        Ansi.ansi0().a0(Attribute.INTENSITY_BOLD).fg0(Ansi.Color.RED)
        Ansi.ansi0().a0(Attribute.INTENSITY_BOLD).fg0(Ansi.Color.RED).a1("foo bar baz")
        Ansi.ansi0().a0(Attribute.INTENSITY_BOLD).fg0(Ansi.Color.RED).a1(
            "foo bar baz"
        ).reset()
        self.assertEqual(
            Ansi.ansi0()
            .a0(Attribute.INTENSITY_BOLD)
            .fg0(Ansi.Color.RED)
            .a1("foo bar baz")
            .reset()
            .toString(),
            str_,
        )
        Ansi.ansi0()
        Ansi.ansi0().bold()

    def testRender3_test7_decomposed(self) -> None:
        str_ = AnsiRenderer.render0("@|bold,red foo bar baz|@")
        print(str_)
        Ansi.ansi0()
        Ansi.ansi0().a0(Attribute.INTENSITY_BOLD)
        Ansi.ansi0().a0(Attribute.INTENSITY_BOLD).fg0(Ansi.Color.RED)
        Ansi.ansi0().a0(Attribute.INTENSITY_BOLD).fg0(Ansi.Color.RED).a1("foo bar baz")
        Ansi.ansi0().a0(Attribute.INTENSITY_BOLD).fg0(Ansi.Color.RED).a1(
            "foo bar baz"
        ).reset()
        self.assertEqual(
            Ansi.ansi0()
            .a0(Attribute.INTENSITY_BOLD)
            .fg0(Ansi.Color.RED)
            .a1("foo bar baz")
            .reset()
            .toString(),
            str_,
        )
        Ansi.ansi0()

    def testRender3_test6_decomposed(self) -> None:
        str_ = AnsiRenderer.render0("@|bold,red foo bar baz|@")
        print(str_)
        ansi_instance = Ansi.ansi0()
        ansi_instance.a0(Attribute.INTENSITY_BOLD)
        ansi_instance.a0(Attribute.INTENSITY_BOLD).fg0(Ansi.Color.RED)
        ansi_instance.a0(Attribute.INTENSITY_BOLD).fg0(Ansi.Color.RED).a1("foo bar baz")
        ansi_instance.a0(Attribute.INTENSITY_BOLD).fg0(Ansi.Color.RED).a1(
            "foo bar baz"
        ).reset()
        self.assertEqual(
            Ansi.ansi0()
            .a0(Attribute.INTENSITY_BOLD)
            .fg0(Ansi.Color.RED)
            .a1("foo bar baz")
            .reset()
            .toString(),
            str_,
        )

    def testRender3_test5_decomposed(self) -> None:
        str_ = AnsiRenderer.render0("@|bold,red foo bar baz|@")
        print(str_)
        Ansi.ansi0()
        Ansi.ansi0().a0(Attribute.INTENSITY_BOLD)
        Ansi.ansi0().a0(Attribute.INTENSITY_BOLD).fg0(Ansi.Color.RED)
        Ansi.ansi0().a0(Attribute.INTENSITY_BOLD).fg0(Ansi.Color.RED).a1("foo bar baz")
        Ansi.ansi0().a0(Attribute.INTENSITY_BOLD).fg0(Ansi.Color.RED).a1(
            "foo bar baz"
        ).reset()

    def testRender3_test4_decomposed(self) -> None:
        str_ = AnsiRenderer.render0("@|bold,red foo bar baz|@")
        print(str_)
        Ansi.ansi0()
        Ansi.ansi0().a0(INTENSITY_BOLD)
        Ansi.ansi0().a0(INTENSITY_BOLD).fg0(RED)
        Ansi.ansi0().a0(INTENSITY_BOLD).fg0(RED).a1("foo bar baz")

    def testRender3_test3_decomposed(self) -> None:
        str_ = AnsiRenderer.render0("@|bold,red foo bar baz|@")
        print(str_)
        Ansi.ansi0()
        Ansi.ansi0().a0(INTENSITY_BOLD)
        Ansi.ansi0().a0(INTENSITY_BOLD).fg0(RED)

    def testRender3_test2_decomposed(self) -> None:
        str_ = AnsiRenderer.render0("@|bold,red foo bar baz|@")
        print(str_)
        Ansi.ansi0()
        Ansi.ansi0().a0(INTENSITY_BOLD)

    def testRender3_test1_decomposed(self) -> None:
        str_ = AnsiRenderer.render0("@|bold,red foo bar baz|@")
        print(str_)
        Ansi.ansi0()

    def testRender3_test0_decomposed(self) -> None:
        str_ = AnsiRenderer.render0("@|bold,red foo bar baz|@")

    def testRender2_test12_decomposed(self) -> None:
        str_ = AnsiRenderer.render0("@|bold,red foo|@")
        print(str_)
        Ansi.ansi0()
        Ansi.ansi0().a0(Attribute.INTENSITY_BOLD)
        Ansi.ansi0().a0(Attribute.INTENSITY_BOLD).fg0(Color.RED)
        Ansi.ansi0().a0(Attribute.INTENSITY_BOLD).fg0(Color.RED).a1("foo")
        Ansi.ansi0().a0(Attribute.INTENSITY_BOLD).fg0(Color.RED).a1("foo").reset()
        self.assertEqual(
            Ansi.ansi0()
            .a0(Attribute.INTENSITY_BOLD)
            .fg0(Color.RED)
            .a1("foo")
            .reset()
            .toString(),
            str_,
        )
        Ansi.ansi0()
        Ansi.ansi0().bold()
        Ansi.ansi0().bold().fgRed()
        Ansi.ansi0().bold().fgRed().a1("foo")
        Ansi.ansi0().bold().fgRed().a1("foo").reset()
        self.assertEqual(Ansi.ansi0().bold().fgRed().a1("foo").reset().toString(), str_)

    def testRender2_test11_decomposed(self) -> None:
        str_ = AnsiRenderer.render0("@|bold,red foo|@")
        print(str_)
        Ansi.ansi0()
        Ansi.ansi0().a0(Attribute.INTENSITY_BOLD)
        Ansi.ansi0().a0(Attribute.INTENSITY_BOLD).fg0(Color.RED)
        Ansi.ansi0().a0(Attribute.INTENSITY_BOLD).fg0(Color.RED).a1("foo")
        Ansi.ansi0().a0(Attribute.INTENSITY_BOLD).fg0(Color.RED).a1("foo").reset()
        self.assertEqual(
            Ansi.ansi0()
            .a0(Attribute.INTENSITY_BOLD)
            .fg0(Color.RED)
            .a1("foo")
            .reset()
            .toString(),
            str_,
        )
        Ansi.ansi0()
        Ansi.ansi0().bold()
        Ansi.ansi0().bold().fgRed()
        Ansi.ansi0().bold().fgRed().a1("foo")
        Ansi.ansi0().bold().fgRed().a1("foo").reset()

    def testRender2_test10_decomposed(self) -> None:
        str_ = AnsiRenderer.render0("@|bold,red foo|@")
        print(str_)
        Ansi.ansi0()
        Ansi.ansi0().a0(Attribute.INTENSITY_BOLD)
        Ansi.ansi0().a0(Attribute.INTENSITY_BOLD).fg0(Color.RED)
        Ansi.ansi0().a0(Attribute.INTENSITY_BOLD).fg0(Color.RED).a1("foo")
        Ansi.ansi0().a0(Attribute.INTENSITY_BOLD).fg0(Color.RED).a1("foo").reset()
        self.assertEqual(
            Ansi.ansi0()
            .a0(Attribute.INTENSITY_BOLD)
            .fg0(Color.RED)
            .a1("foo")
            .reset()
            .toString(),
            str_,
        )
        Ansi.ansi0()
        Ansi.ansi0().bold()
        Ansi.ansi0().bold().fgRed()
        Ansi.ansi0().bold().fgRed().a1("foo")

    def testRender2_test9_decomposed(self) -> None:
        str_ = AnsiRenderer.render0("@|bold,red foo|@")
        print(str_)
        Ansi.ansi0()
        Ansi.ansi0().a0(Attribute.INTENSITY_BOLD)
        Ansi.ansi0().a0(Attribute.INTENSITY_BOLD).fg0(Color.RED)
        Ansi.ansi0().a0(Attribute.INTENSITY_BOLD).fg0(Color.RED).a1("foo")
        Ansi.ansi0().a0(Attribute.INTENSITY_BOLD).fg0(Color.RED).a1("foo").reset()
        self.assertEqual(
            Ansi.ansi0()
            .a0(Attribute.INTENSITY_BOLD)
            .fg0(Color.RED)
            .a1("foo")
            .reset()
            .toString(),
            str_,
        )
        Ansi.ansi0()
        Ansi.ansi0().bold()
        Ansi.ansi0().bold().fgRed()

    def testRender2_test8_decomposed(self) -> None:
        str_ = AnsiRenderer.render0("@|bold,red foo|@")
        print(str_)
        Ansi.ansi0()
        Ansi.ansi0().a0(Attribute.INTENSITY_BOLD)
        Ansi.ansi0().a0(Attribute.INTENSITY_BOLD).fg0(Ansi.Color.RED)
        Ansi.ansi0().a0(Attribute.INTENSITY_BOLD).fg0(Ansi.Color.RED).a1("foo")
        Ansi.ansi0().a0(Attribute.INTENSITY_BOLD).fg0(Ansi.Color.RED).a1("foo").reset()
        self.assertEqual(
            Ansi.ansi0()
            .a0(Attribute.INTENSITY_BOLD)
            .fg0(Ansi.Color.RED)
            .a1("foo")
            .reset()
            .toString(),
            str_,
        )
        Ansi.ansi0()
        Ansi.ansi0().bold()

    def testRender2_test7_decomposed(self) -> None:
        str_ = AnsiRenderer.render0("@|bold,red foo|@")
        print(str_)
        Ansi.ansi0()
        Ansi.ansi0().a0(Attribute.INTENSITY_BOLD)
        Ansi.ansi0().a0(Attribute.INTENSITY_BOLD).fg0(Ansi.Color.RED)
        Ansi.ansi0().a0(Attribute.INTENSITY_BOLD).fg0(Ansi.Color.RED).a1("foo")
        Ansi.ansi0().a0(Attribute.INTENSITY_BOLD).fg0(Ansi.Color.RED).a1("foo").reset()
        self.assertEqual(
            Ansi.ansi0()
            .a0(Attribute.INTENSITY_BOLD)
            .fg0(Ansi.Color.RED)
            .a1("foo")
            .reset()
            .toString(),
            str_,
        )
        Ansi.ansi0()

    def testRender2_test6_decomposed(self) -> None:
        str_ = AnsiRenderer.render0("@|bold,red foo|@")
        print(str_)
        Ansi.ansi0()
        Ansi.ansi0().a0(Attribute.INTENSITY_BOLD)
        Ansi.ansi0().a0(Attribute.INTENSITY_BOLD).fg0(Ansi.Color.RED)
        Ansi.ansi0().a0(Attribute.INTENSITY_BOLD).fg0(Ansi.Color.RED).a1("foo")
        Ansi.ansi0().a0(Attribute.INTENSITY_BOLD).fg0(Ansi.Color.RED).a1("foo").reset()
        self.assertEqual(
            Ansi.ansi0()
            .a0(Attribute.INTENSITY_BOLD)
            .fg0(Ansi.Color.RED)
            .a1("foo")
            .reset()
            .toString(),
            str_,
        )

    def testRender2_test5_decomposed(self) -> None:
        str_ = AnsiRenderer.render0("@|bold,red foo|@")
        print(str_)
        Ansi.ansi0()
        Ansi.ansi0().a0(Attribute.INTENSITY_BOLD)
        Ansi.ansi0().a0(Attribute.INTENSITY_BOLD).fg0(Ansi.Color.RED)
        Ansi.ansi0().a0(Attribute.INTENSITY_BOLD).fg0(Ansi.Color.RED).a1("foo")
        Ansi.ansi0().a0(Attribute.INTENSITY_BOLD).fg0(Ansi.Color.RED).a1("foo").reset()

    def testRender2_test4_decomposed(self) -> None:
        str_ = AnsiRenderer.render0("@|bold,red foo|@")
        print(str_)
        Ansi.ansi0()
        Ansi.ansi0().a0(INTENSITY_BOLD)
        Ansi.ansi0().a0(INTENSITY_BOLD).fg0(RED)
        Ansi.ansi0().a0(INTENSITY_BOLD).fg0(RED).a1("foo")

    def testRender2_test3_decomposed(self) -> None:
        str_ = AnsiRenderer.render0("@|bold,red foo|@")
        print(str_)
        Ansi.ansi0()
        Ansi.ansi0().a0(INTENSITY_BOLD)
        Ansi.ansi0().a0(INTENSITY_BOLD).fg0(RED)

    def testRender2_test2_decomposed(self) -> None:
        str_ = AnsiRenderer.render0("@|bold,red foo|@")
        print(str_)
        Ansi.ansi0()
        Ansi.ansi0().a0(INTENSITY_BOLD)

    def testRender2_test1_decomposed(self) -> None:
        str_ = AnsiRenderer.render0("@|bold,red foo|@")
        print(str_)
        Ansi.ansi0()

    def testRender2_test0_decomposed(self) -> None:
        str_ = AnsiRenderer.render0("@|bold,red foo|@")

    def testRenderCodes_test4_decomposed(self) -> None:
        str_ = AnsiRenderer.renderCodes1("bold red")
        print(str_)
        ansi_instance = Ansi.ansi0()
        ansi_instance.bold()
        ansi_instance.bold().fg0(Ansi.Color.RED)
        self.assertEqual(Ansi.ansi0().bold().fg0(Ansi.Color.RED).toString(), str_)

    def testRenderCodes_test3_decomposed(self) -> None:
        str_ = AnsiRenderer.renderCodes1("bold red")
        print(str_)
        Ansi.ansi0()
        Ansi.ansi0().bold()
        Ansi.ansi0().bold().fg0(Ansi.Color.RED)

    def testRenderCodes_test2_decomposed(self) -> None:
        str_ = AnsiRenderer.renderCodes1("bold red")
        print(str_)
        Ansi.ansi0()
        Ansi.ansi0().bold()

    def testRenderCodes_test1_decomposed(self) -> None:
        str_ = AnsiRenderer.renderCodes1("bold red")
        print(str_)
        Ansi.ansi0()

    def testRenderCodes_test0_decomposed(self) -> None:
        str_ = AnsiRenderer.renderCodes1("bold red")

    def testRender_test10_decomposed(self) -> None:
        str_ = AnsiRenderer.render0("@|bold foo|@")
        print(str_)
        self.assertEqual(
            Ansi.ansi0().a0(Attribute.INTENSITY_BOLD).a1("foo").reset().toString(), str_
        )

        Ansi.ansi0()
        Ansi.ansi0().bold()
        Ansi.ansi0().bold().a1("foo")
        Ansi.ansi0().bold().a1("foo").reset()
        self.assertEqual(Ansi.ansi0().bold().a1("foo").reset().toString(), str_)

    def testRender_test9_decomposed(self) -> None:
        str_ = AnsiRenderer.render0("@|bold foo|@")
        print(str_)
        Ansi.ansi0()
        Ansi.ansi0().a0(Attribute.INTENSITY_BOLD)
        Ansi.ansi0().a0(Attribute.INTENSITY_BOLD).a1("foo")
        Ansi.ansi0().a0(Attribute.INTENSITY_BOLD).a1("foo").reset()
        self.assertEqual(
            Ansi.ansi0().a0(Attribute.INTENSITY_BOLD).a1("foo").reset().toString(), str_
        )
        Ansi.ansi0()
        Ansi.ansi0().bold()
        Ansi.ansi0().bold().a1("foo")
        Ansi.ansi0().bold().a1("foo").reset()

    def testRender_test8_decomposed(self) -> None:
        str_ = AnsiRenderer.render0("@|bold foo|@")
        print(str_)
        Ansi.ansi0()
        Ansi.ansi0().a0(Attribute.INTENSITY_BOLD)
        Ansi.ansi0().a0(Attribute.INTENSITY_BOLD).a1("foo")
        Ansi.ansi0().a0(Attribute.INTENSITY_BOLD).a1("foo").reset()
        self.assertEqual(
            Ansi.ansi0().a0(Attribute.INTENSITY_BOLD).a1("foo").reset().toString(), str_
        )
        Ansi.ansi0()
        Ansi.ansi0().bold()
        Ansi.ansi0().bold().a1("foo")

    def testRender_test7_decomposed(self) -> None:
        str_ = AnsiRenderer.render0("@|bold foo|@")
        print(str_)
        Ansi.ansi0()
        Ansi.ansi0().a0(Attribute.INTENSITY_BOLD)
        Ansi.ansi0().a0(Attribute.INTENSITY_BOLD).a1("foo")
        Ansi.ansi0().a0(Attribute.INTENSITY_BOLD).a1("foo").reset()
        self.assertEqual(
            Ansi.ansi0().a0(Attribute.INTENSITY_BOLD).a1("foo").reset().toString(), str_
        )
        Ansi.ansi0()
        Ansi.ansi0().bold()

    def testRender_test6_decomposed(self) -> None:
        str_ = AnsiRenderer.render0("@|bold foo|@")
        print(str_)
        Ansi.ansi0()
        Ansi.ansi0().a0(Attribute.INTENSITY_BOLD)
        Ansi.ansi0().a0(Attribute.INTENSITY_BOLD).a1("foo")
        Ansi.ansi0().a0(Attribute.INTENSITY_BOLD).a1("foo").reset()
        self.assertEqual(
            Ansi.ansi0().a0(Attribute.INTENSITY_BOLD).a1("foo").reset().toString(), str_
        )
        Ansi.ansi0()

    def testRender_test5_decomposed(self) -> None:
        str_ = AnsiRenderer.render0("@|bold foo|@")
        print(str_)
        ansi_instance = Ansi.ansi0()
        ansi_instance.a0(Attribute.INTENSITY_BOLD)
        ansi_instance.a0(Attribute.INTENSITY_BOLD).a1("foo")
        ansi_instance.a0(Attribute.INTENSITY_BOLD).a1("foo").reset()
        self.assertEqual(
            Ansi.ansi0().a0(Attribute.INTENSITY_BOLD).a1("foo").reset().toString(), str_
        )

    def testRender_test4_decomposed(self) -> None:
        str_ = AnsiRenderer.render0("@|bold foo|@")
        print(str_)
        Ansi.ansi0()
        Ansi.ansi0().a0(Attribute.INTENSITY_BOLD)
        Ansi.ansi0().a0(Attribute.INTENSITY_BOLD).a1("foo")
        Ansi.ansi0().a0(Attribute.INTENSITY_BOLD).a1("foo").reset()

    def testRender_test3_decomposed(self) -> None:
        str_ = AnsiRenderer.render0("@|bold foo|@")
        print(str_)
        Ansi.ansi0()
        Ansi.ansi0().a0(INTENSITY_BOLD)
        Ansi.ansi0().a0(INTENSITY_BOLD).a1("foo")

    def testRender_test2_decomposed(self) -> None:
        str_ = AnsiRenderer.render0("@|bold foo|@")
        print(str_)
        Ansi.ansi0()
        Ansi.ansi0().a0(INTENSITY_BOLD)

    def testRender_test1_decomposed(self) -> None:
        str_ = AnsiRenderer.render0("@|bold foo|@")
        print(str_)
        Ansi.ansi0()

    def testRender_test0_decomposed(self) -> None:
        str_ = AnsiRenderer.render0("@|bold foo|@")

    def testTest_test0_decomposed(self) -> None:
        self.assertFalse(AnsiRenderer.test("foo"))
        self.assertTrue(AnsiRenderer.test("@|foo|"))
        self.assertTrue(AnsiRenderer.test("@|foo"))

    @staticmethod
    def setUp() -> None:
        Ansi.setEnabled(True)
