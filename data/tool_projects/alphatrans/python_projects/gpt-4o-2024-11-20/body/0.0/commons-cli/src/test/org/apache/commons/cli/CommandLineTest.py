from __future__ import annotations
import re
import typing
from typing import *
import numbers
import unittest
import pytest
import io
import os
import unittest
from src.main.org.apache.commons.cli.CommandLine import *
from src.main.org.apache.commons.cli.CommandLineParser import *
from src.main.org.apache.commons.cli.DefaultParser import *
from src.main.org.apache.commons.cli.GnuParser import *
from src.main.org.apache.commons.cli.Option import *
from src.main.org.apache.commons.cli.OptionBuilder import *
from src.main.org.apache.commons.cli.Options import *
from src.main.org.apache.commons.cli.Parser import *


class CommandLineTest(unittest.TestCase):

    def testNullhOption_test12_decomposed(self) -> None:
        options = Options()

        # Create and configure the "i" option
        builder_i = Builder.builder1("i")
        builder_i.hasArg0()
        builder_i.type_(Number)
        opt_i = builder_i.hasArg0().type_(Number).build()

        # Create and configure the "f" option
        builder_f = Builder.builder1("f")
        builder_f.hasArg0()
        opt_f = builder_f.hasArg0().build()

        # Add options to the options object
        options.addOption0(opt_i)
        options.addOption0(opt_f)

        # Create a parser and parse the command line arguments
        parser = DefaultParser(2, False, None)
        cmd = parser.parse0(options, ["-i", "123", "-f", "foo"])

        # Assertions
        self.assertIsNone(cmd.getOptionValue2(None))
        self.assertIsNone(cmd.getParsedOptionValue1(None))

    def testNullhOption_test11_decomposed(self) -> None:
        options = Options()

        # Create and configure the "i" option
        opt_i = Builder.builder1("i").hasArg0().type_(int).build()

        # Create and configure the "f" option
        opt_f = Builder.builder1("f").hasArg0().build()

        # Add options to the options object
        options.addOption0(opt_i)
        options.addOption0(opt_f)

        # Create a parser and parse the command line arguments
        parser = DefaultParser(2, False, None)
        cmd = parser.parse0(options, ["-i", "123", "-f", "foo"])

        # Assert that the value of a null option is None
        self.assertIsNone(cmd.getOptionValue2(None))

    def testNullhOption_test10_decomposed(self) -> None:
        options = Options()

        # Create the "i" option
        builder_i = Builder.builder1("i")
        builder_i.hasArg0()
        builder_i.type_(int)
        opt_i = builder_i.hasArg0().type_(int).build()

        # Create the "f" option
        builder_f = Builder.builder1("f")
        builder_f.hasArg0()
        opt_f = builder_f.hasArg0().build()

        # Add options to the options object
        options.addOption0(opt_i)
        options.addOption0(opt_f)

        # Create the parser and parse the command line arguments
        parser = DefaultParser(2, False, None)
        cmd = parser.parse0(options, ["-i", "123", "-f", "foo"])

    def testNullhOption_test9_decomposed(self) -> None:
        options = Options()

        # Create Option "i" with various configurations
        Option.builder1("i")
        Option.builder1("i").hasArg0()
        Option.builder1("i").hasArg0().type_(Number)
        opt_i = Option.builder1("i").hasArg0().type_(Number).build()

        # Create Option "f" with various configurations
        Option.builder1("f")
        Option.builder1("f").hasArg0()
        opt_f = Option.builder1("f").hasArg0().build()

        # Add options to the Options object
        options.addOption0(opt_i)
        options.addOption0(opt_f)

        # Create a CommandLineParser instance
        parser = DefaultParser(2, False, None)

    def testNullhOption_test8_decomposed(self) -> None:
        options = Options()
        Builder.builder1("i")
        Builder.builder1("i").hasArg0()
        Builder.builder1("i").hasArg0().type_(Number)
        opt_i = Builder.builder1("i").hasArg0().type_(Number).build()
        Builder.builder1("f")
        Builder.builder1("f").hasArg0()
        opt_f = Builder.builder1("f").hasArg0().build()
        options.addOption0(opt_i)
        options.addOption0(opt_f)

    def testNullhOption_test7_decomposed(self) -> None:
        options = Options()
        Builder.builder1("i")
        Builder.builder1("i").hasArg0()
        Builder.builder1("i").hasArg0().type_(int)
        opt_i = Builder.builder1("i").hasArg0().type_(int).build()
        Builder.builder1("f")
        Builder.builder1("f").hasArg0()
        opt_f = Builder.builder1("f").hasArg0().build()

    def testNullhOption_test6_decomposed(self) -> None:
        options = Options()
        Builder.builder1("i")
        Builder.builder1("i").hasArg0()
        Builder.builder1("i").hasArg0().type_(Number)
        opt_i = Builder.builder1("i").hasArg0().type_(Number).build()
        Builder.builder1("f")
        Builder.builder1("f").hasArg0()

    def testNullhOption_test5_decomposed(self) -> None:
        options = Options()
        Builder.builder1("i")
        Builder.builder1("i").hasArg0()
        Builder.builder1("i").hasArg0().type_(Number)
        opt_i = Builder.builder1("i").hasArg0().type_(Number).build()
        Builder.builder1("f")

    def testNullhOption_test4_decomposed(self) -> None:
        options = Options()
        Builder.builder1("i")
        Builder.builder1("i").hasArg0()
        Builder.builder1("i").hasArg0().type_(int)
        opt_i = Builder.builder1("i").hasArg0().type_(int).build()

    def testNullhOption_test3_decomposed(self) -> None:
        options = Options()
        Parser.builder1("i")
        Parser.builder1("i").hasArg0()
        Parser.builder1("i").hasArg0().type_(Number)

    def testNullhOption_test2_decomposed(self) -> None:
        options = Options()
        Option.builder1("i")
        Option.builder1("i").hasArg0()

    def testNullhOption_test1_decomposed(self) -> None:
        options = Options()
        Option.builder1("i")

    def testNullhOption_test0_decomposed(self) -> None:
        options = Options()

    def testGetParsedOptionValueWithOption_test11_decomposed(self) -> None:
        options = Options()

        # Create the "i" option
        opt_i = Builder.builder1("i").hasArg0().type_(int).build()

        # Create the "f" option
        opt_f = Builder.builder1("f").hasArg0().build()

        # Add options to the options object
        options.addOption0(opt_i)
        options.addOption0(opt_f)

        # Create the parser and parse the command line arguments
        parser = DefaultParser(2, False, None)
        cmd = parser.parse0(options, ["-i", "123", "-f", "foo"])

        # Assertions
        self.assertEqual(123, cmd.getParsedOptionValue1(opt_i))
        self.assertEqual("foo", cmd.getParsedOptionValue1(opt_f))

    def testGetParsedOptionValueWithOption_test10_decomposed(self) -> None:
        options = Options()

        # Create the "i" option
        builder_i = Builder.builder1("i")
        builder_i.hasArg0()
        builder_i.type_(Number)
        opt_i = builder_i.hasArg0().type_(Number).build()

        # Create the "f" option
        builder_f = Builder.builder1("f")
        builder_f.hasArg0()
        opt_f = builder_f.hasArg0().build()

        # Add options to the options object
        options.addOption0(opt_i)
        options.addOption0(opt_f)

        # Create the parser and parse the command line arguments
        parser = DefaultParser(2, False, None)
        cmd = parser.parse0(options, ["-i", "123", "-f", "foo"])

    def testGetParsedOptionValueWithOption_test9_decomposed(self) -> None:
        options = Options()

        # Create the "i" option
        builder_i = Builder.builder1("i")
        builder_i.hasArg0()
        builder_i.type_(Number)
        opt_i = builder_i.hasArg0().type_(Number).build()

        # Create the "f" option
        builder_f = Builder.builder1("f")
        builder_f.hasArg0()
        opt_f = builder_f.hasArg0().build()

        # Add options to the options object
        options.addOption0(opt_i)
        options.addOption0(opt_f)

        # Create the parser
        parser = DefaultParser(2, False, None)

    def testGetParsedOptionValueWithOption_test8_decomposed(self) -> None:
        options = Options()

        # Create the "i" option
        builder_i = Builder.builder1("i")
        builder_i.hasArg0()
        builder_i.type_(Number)
        opt_i = builder_i.hasArg0().type_(Number).build()

        # Create the "f" option
        builder_f = Builder.builder1("f")
        builder_f.hasArg0()
        opt_f = builder_f.hasArg0().build()

        # Add options to the options object
        options.addOption0(opt_i)
        options.addOption0(opt_f)

    def testGetParsedOptionValueWithOption_test7_decomposed(self) -> None:
        options = Options()
        Builder.builder1("i")
        Builder.builder1("i").hasArg0()
        Builder.builder1("i").hasArg0().type_(Number)
        opt_i = Builder.builder1("i").hasArg0().type_(Number).build()
        Builder.builder1("f")
        Builder.builder1("f").hasArg0()
        opt_f = Builder.builder1("f").hasArg0().build()

    def testGetParsedOptionValueWithOption_test6_decomposed(self) -> None:
        options = Options()
        Builder.builder1("i")
        Builder.builder1("i").hasArg0()
        Builder.builder1("i").hasArg0().type_(Number)
        opt_i = Builder.builder1("i").hasArg0().type_(Number).build()
        Builder.builder1("f")
        Builder.builder1("f").hasArg0()

    def testGetParsedOptionValueWithOption_test5_decomposed(self) -> None:
        options = Options()
        Builder.builder1("i")
        Builder.builder1("i").hasArg0()
        Builder.builder1("i").hasArg0().type_(Number)
        opt_i = Builder.builder1("i").hasArg0().type_(Number).build()
        Builder.builder1("f")

    def testGetParsedOptionValueWithOption_test4_decomposed(self) -> None:
        options = Options()
        builder = Builder.builder1("i")
        builder.hasArg0()
        builder.type_(Number)
        opt_i = builder.hasArg0().type_(Number).build()

    def testGetParsedOptionValueWithOption_test3_decomposed(self) -> None:
        options = Options()
        builder = Parser.builder1("i")
        builder.hasArg0()
        builder.type_(Number)

    def testGetParsedOptionValueWithOption_test2_decomposed(self) -> None:
        options = Options()
        Option.builder1("i")
        Option.builder1("i").hasArg0()

    def testGetParsedOptionValueWithOption_test1_decomposed(self) -> None:
        options = Options()
        Option.builder1("i")

    def testGetParsedOptionValueWithOption_test0_decomposed(self) -> None:
        options = Options()

    def testGetParsedOptionValueWithChar_test12_decomposed(self) -> None:
        options = Options()

        # Create and configure the "i" option
        i_option = CommandLineParser.builder1("i").hasArg0().type_(int).build()
        options.addOption0(i_option)

        # Create and configure the "f" option
        f_option = CommandLineParser.builder1("f").hasArg0().build()
        options.addOption0(f_option)

        # Parse the command line arguments
        parser = DefaultParser(2, False, None)
        cmd = parser.parse0(options, ["-i", "123", "-f", "foo"])

        # Assertions
        self.assertEqual(123, cmd.getParsedOptionValue0("i"))
        self.assertEqual("foo", cmd.getParsedOptionValue0("f"))

    def testGetParsedOptionValueWithChar_test11_decomposed(self) -> None:
        options = Options()

        # Create and configure the "i" option
        i_option = CommandLineParser.builder1("i").hasArg0().type_(Number).build()
        options.addOption0(i_option)

        # Create and configure the "f" option
        f_option = CommandLineParser.builder1("f").hasArg0().build()
        options.addOption0(f_option)

        # Create the parser and parse the command line arguments
        parser = DefaultParser(2, False, None)
        cmd = parser.parse0(options, ["-i", "123", "-f", "foo"])

    def testGetParsedOptionValueWithChar_test10_decomposed(self) -> None:
        options = Options()

        # Create and configure the "i" option
        builder_i = Parser.builder1("i")
        builder_i.hasArg0()
        builder_i.type_(Number)
        option_i = builder_i.build()
        options.addOption0(option_i)

        # Create and configure the "f" option
        builder_f = Parser.builder1("f")
        builder_f.hasArg0()
        option_f = builder_f.build()
        options.addOption0(option_f)

        # Create the parser
        parser = DefaultParser(2, False, None)

    def testGetParsedOptionValueWithChar_test9_decomposed(self) -> None:
        options = Options()

        # Create and configure the "i" option
        builder_i = Parser.builder1("i")
        builder_i = builder_i.hasArg0()
        builder_i = builder_i.type_(Number)
        option_i = builder_i.build()
        options.addOption0(option_i)

        # Create and configure the "f" option
        builder_f = Parser.builder1("f")
        builder_f = builder_f.hasArg0()
        option_f = builder_f.build()
        options.addOption0(option_f)

    def testGetParsedOptionValueWithChar_test8_decomposed(self) -> None:
        options = Options()

        # Create and configure the "i" option
        builder_i = Parser.builder1("i")
        builder_i = builder_i.hasArg0()
        builder_i = builder_i.type_(Number)
        option_i = builder_i.build()
        options.addOption0(option_i)

        # Create and configure the "f" option
        builder_f = Parser.builder1("f")
        builder_f = builder_f.hasArg0()
        option_f = builder_f.build()

    def testGetParsedOptionValueWithChar_test7_decomposed(self) -> None:
        options = Options()
        builder = Parser.builder1("i")
        builder.hasArg0()
        builder.type_(Number)
        option_i = builder.hasArg0().type_(Number).build()
        options.addOption0(option_i)
        Parser.builder1("f").hasArg0()

    def testGetParsedOptionValueWithChar_test6_decomposed(self) -> None:
        options = Options()
        builder = Parser.builder1("i")
        builder.hasArg0()
        builder.type_(Number)
        option = builder.hasArg0().type_(Number).build()
        options.addOption0(option)
        Parser.builder1("f")

    def testGetParsedOptionValueWithChar_test5_decomposed(self) -> None:
        options = Options()
        builder = Parser.builder1("i")
        builder = builder.hasArg0()
        builder = builder.type_(Number)
        option = builder.build()
        options.addOption0(option)

    def testGetParsedOptionValueWithChar_test4_decomposed(self) -> None:
        options = Options()
        builder = Parser.builder1("i")
        builder.hasArg0()
        builder.type_(Number)
        option = builder.build()

    def testGetParsedOptionValueWithChar_test3_decomposed(self) -> None:
        options = Options()
        builder = Parser.builder1("i")
        builder.hasArg0()
        builder.type_(Number)

    def testGetParsedOptionValueWithChar_test2_decomposed(self) -> None:
        options = Options()
        Option.builder1("i")
        Option.builder1("i").hasArg0()

    def testGetParsedOptionValueWithChar_test1_decomposed(self) -> None:
        options = Options()
        Option.builder1("i")

    def testGetParsedOptionValueWithChar_test0_decomposed(self) -> None:
        options = Options()

    def testGetParsedOptionValue_test10_decomposed(self) -> None:
        options = Options()

        # Create and add the "i" option
        i_option = OptionBuilder.hasArg0().withType0(int).create2("i")
        options.addOption0(i_option)

        # Create and add the "f" option
        f_option = OptionBuilder.hasArg0().create2("f")
        options.addOption0(f_option)

        # Create the parser and parse the command line arguments
        parser = DefaultParser(2, False, None)
        cmd = parser.parse0(options, ["-i", "123", "-f", "foo"])

        # Assertions
        self.assertEqual(123, cmd.getParsedOptionValue2("i"))
        self.assertEqual("foo", cmd.getParsedOptionValue2("f"))

    def testGetParsedOptionValue_test9_decomposed(self) -> None:
        options = Options()

        # Create and configure the "i" option
        i_option = OptionBuilder.hasArg0().withType0(Number).create2("i")
        options.addOption0(i_option)

        # Create and configure the "f" option
        f_option = OptionBuilder.hasArg0().create2("f")
        options.addOption0(f_option)

        # Create the parser
        parser = DefaultParser(2, False, None)

        # Parse the command line arguments
        cmd = parser.parse0(options, ["-i", "123", "-f", "foo"])

    def testGetParsedOptionValue_test8_decomposed(self) -> None:
        options = Options()
        OptionBuilder.hasArg0()
        OptionBuilder.hasArg0().withType0(Number)
        OptionBuilder.hasArg0().withType0(Number).create2("i")
        options.addOption0(OptionBuilder.hasArg0().withType0(Number).create2("i"))
        OptionBuilder.hasArg0()
        OptionBuilder.hasArg0().create2("f")
        options.addOption0(OptionBuilder.hasArg0().create2("f"))
        parser = DefaultParser(2, False, None)

    def testGetParsedOptionValue_test7_decomposed(self) -> None:
        options = Options()
        OptionBuilder.hasArg0()
        OptionBuilder.hasArg0().withType0(Number)
        OptionBuilder.hasArg0().withType0(Number).create2("i")
        options.addOption0(OptionBuilder.hasArg0().withType0(Number).create2("i"))
        OptionBuilder.hasArg0()
        OptionBuilder.hasArg0().create2("f")
        options.addOption0(OptionBuilder.hasArg0().create2("f"))

    def testGetParsedOptionValue_test6_decomposed(self) -> None:
        options = Options()
        OptionBuilder.hasArg0()
        OptionBuilder.hasArg0().withType0(Number)
        OptionBuilder.hasArg0().withType0(Number).create2("i")
        options.addOption0(OptionBuilder.hasArg0().withType0(Number).create2("i"))
        OptionBuilder.hasArg0()
        OptionBuilder.hasArg0().create2("f")

    def testGetParsedOptionValue_test5_decomposed(self) -> None:
        options = Options()
        OptionBuilder.hasArg0()
        OptionBuilder.hasArg0().withType0(Number)
        OptionBuilder.hasArg0().withType0(Number).create2("i")
        options.addOption0(OptionBuilder.hasArg0().withType0(Number).create2("i"))
        OptionBuilder.hasArg0()

    def testGetParsedOptionValue_test4_decomposed(self) -> None:
        options = Options()
        option = OptionBuilder.hasArg0().withType0(Number).create2("i")
        options.addOption0(option)

    def testGetParsedOptionValue_test3_decomposed(self) -> None:
        options = Options()
        OptionBuilder.hasArg0()
        OptionBuilder.hasArg0().withType0(Number)
        OptionBuilder.hasArg0().withType0(Number).create2("i")

    def testGetParsedOptionValue_test2_decomposed(self) -> None:
        options = Options()
        OptionBuilder.hasArg0()
        OptionBuilder.hasArg0().withType0(Number)

    def testGetParsedOptionValue_test1_decomposed(self) -> None:
        options = Options()
        OptionBuilder.hasArg0()

    def testGetParsedOptionValue_test0_decomposed(self) -> None:
        options = Options()

    def testGetOptions_test8_decomposed(self) -> None:
        cmd = CommandLine()
        self.assertIsNotNone(cmd.getOptions())
        self.assertEqual(0, len(cmd.getOptions()))

        option_a = Option("a", None)
        cmd._addOption(option_a)

        option_b = Option("b", None)
        cmd._addOption(option_b)

        option_c = Option("c", None)
        cmd._addOption(option_c)

        self.assertEqual(3, len(cmd.getOptions()))

    def testGetOptions_test7_decomposed(self) -> None:
        cmd = CommandLine()
        self.assertIsNotNone(cmd.getOptions())
        self.assertEqual(0, len(cmd.getOptions()))

        option_a = Option("a", None)
        cmd._addOption(option_a)

        option_b = Option("b", None)
        cmd._addOption(option_b)

        option_c = Option("c", None)
        cmd._addOption(option_c)

    def testGetOptions_test6_decomposed(self) -> None:
        cmd = CommandLine()
        self.assertIsNotNone(cmd.getOptions())
        self.assertEqual(0, len(cmd.getOptions()))

        option_a = Option("a", None)
        cmd._addOption(option_a)

        option_b = Option("b", None)
        cmd._addOption(option_b)

        option_c = Option("c", None)

    def testGetOptions_test5_decomposed(self) -> None:
        cmd = CommandLine()
        self.assertIsNotNone(cmd.getOptions())
        self.assertEqual(0, len(cmd.getOptions()))
        option_a = Option("a", None)
        cmd._addOption(option_a)
        option_b = Option("b", None)
        cmd._addOption(option_b)

    def testGetOptions_test4_decomposed(self) -> None:
        cmd = CommandLine()  # Create an instance of CommandLine
        self.assertIsNotNone(cmd.getOptions())  # Assert that options are not None
        self.assertEqual(
            0, len(cmd.getOptions())
        )  # Assert that the length of options is 0
        option_a = Option("a", None)  # Create an Option with "a" and None
        cmd._addOption(option_a)  # Add the option to the CommandLine instance
        option_b = Option("b", None)  # Create another Option with "b" and None

    def testGetOptions_test3_decomposed(self) -> None:
        cmd = CommandLine()
        self.assertIsNotNone(cmd.getOptions())
        self.assertEqual(0, len(cmd.getOptions()))
        option = Option("a", None)
        cmd._addOption(option)

    def testGetOptions_test2_decomposed(self) -> None:
        cmd = CommandLine()
        self.assertIsNotNone(cmd.getOptions())
        self.assertEqual(0, len(cmd.getOptions()))
        Option("a", None)

    def testGetOptions_test1_decomposed(self) -> None:
        cmd = CommandLine()
        self.assertIsNotNone(cmd.getOptions())
        self.assertEqual(0, len(cmd.getOptions()))

    def testGetOptions_test0_decomposed(self) -> None:
        cmd = CommandLine()

    def testGetOptionPropertiesWithOption_test15_decomposed(self) -> None:
        args = [
            "-Dparam1=value1",
            "-Dparam2=value2",
            "-Dparam3",
            "-Dparam4=value4",
            "-D",
            "--property",
            "foo=bar",
        ]
        options = Options()

        # Create the '-D' option
        OptionBuilder.withValueSeparator0()
        OptionBuilder.withValueSeparator0().hasOptionalArgs1(2)
        optionD = OptionBuilder.withValueSeparator0().hasOptionalArgs1(2).create1("D")

        # Create the '--property' option
        OptionBuilder.withValueSeparator0()
        OptionBuilder.withValueSeparator0().hasArgs1(2)
        OptionBuilder.withValueSeparator0().hasArgs1(2).withLongOpt("property")
        optionProperty = (
            OptionBuilder.withValueSeparator0()
            .hasArgs1(2)
            .withLongOpt("property")
            .create0()
        )

        # Add options to the options object
        options.addOption0(optionD)
        options.addOption0(optionProperty)

        # Parse the command line arguments
        parser = GnuParser()
        cl = parser.parse0(options, args)

        # Get properties for the '-D' option
        props = cl.getOptionProperties0(optionD)
        self.assertIsNotNone(props, "null properties")
        self.assertEqual(4, len(props), f"number of properties in {props}")
        self.assertEqual("value1", props.get("param1"), "property 1")
        self.assertEqual("value2", props.get("param2"), "property 2")
        self.assertEqual("true", props.get("param3"), "property 3")
        self.assertEqual("value4", props.get("param4"), "property 4")

        # Get properties for the '--property' option
        property_props = cl.getOptionProperties0(optionProperty)
        self.assertEqual("bar", property_props.get("foo"), "property with long format")

    def testGetOptionPropertiesWithOption_test14_decomposed(self) -> None:
        args = [
            "-Dparam1=value1",
            "-Dparam2=value2",
            "-Dparam3",
            "-Dparam4=value4",
            "-D",
            "--property",
            "foo=bar",
        ]
        options = Options()
        OptionBuilder.withValueSeparator0()
        OptionBuilder.withValueSeparator0().hasOptionalArgs1(2)
        optionD = OptionBuilder.withValueSeparator0().hasOptionalArgs1(2).create1("D")
        OptionBuilder.withValueSeparator0()
        OptionBuilder.withValueSeparator0().hasArgs1(2)
        OptionBuilder.withValueSeparator0().hasArgs1(2).withLongOpt("property")
        optionProperty = (
            OptionBuilder.withValueSeparator0()
            .hasArgs1(2)
            .withLongOpt("property")
            .create0()
        )
        options.addOption0(optionD)
        options.addOption0(optionProperty)
        parser = GnuParser()
        cl = parser.parse0(options, args)
        props = cl.getOptionProperties0(optionD)
        self.assertIsNotNone(props, "null properties")
        self.assertEqual(4, len(props), f"number of properties in {props}")
        self.assertEqual("value1", props.get("param1"), "property 1")
        self.assertEqual("value2", props.get("param2"), "property 2")
        self.assertEqual("true", props.get("param3"), "property 3")
        self.assertEqual("value4", props.get("param4"), "property 4")

    def testGetOptionPropertiesWithOption_test13_decomposed(self) -> None:
        args = [
            "-Dparam1=value1",
            "-Dparam2=value2",
            "-Dparam3",
            "-Dparam4=value4",
            "-D",
            "--property",
            "foo=bar",
        ]
        options = Options()
        OptionBuilder.withValueSeparator0()
        OptionBuilder.withValueSeparator0().hasOptionalArgs1(2)
        optionD = OptionBuilder.withValueSeparator0().hasOptionalArgs1(2).create1("D")
        OptionBuilder.withValueSeparator0()
        OptionBuilder.withValueSeparator0().hasArgs1(2)
        OptionBuilder.withValueSeparator0().hasArgs1(2).withLongOpt("property")
        optionProperty = (
            OptionBuilder.withValueSeparator0()
            .hasArgs1(2)
            .withLongOpt("property")
            .create0()
        )
        options.addOption0(optionD)
        options.addOption0(optionProperty)
        parser = GnuParser()
        cl = parser.parse0(options, args)
        props = cl.getOptionProperties0(optionD)
        self.assertIsNotNone(props, "null properties")
        self.assertEqual(4, len(props), f"number of properties in {props}")
        self.assertEqual("value1", props.get("param1"), "property 1")
        self.assertEqual("value2", props.get("param2"), "property 2")

    def testGetOptionPropertiesWithOption_test12_decomposed(self) -> None:
        args = [
            "-Dparam1=value1",
            "-Dparam2=value2",
            "-Dparam3",
            "-Dparam4=value4",
            "-D",
            "--property",
            "foo=bar",
        ]
        options = Options()

        # Create the '-D' option
        OptionBuilder.withValueSeparator0()
        OptionBuilder.withValueSeparator0().hasOptionalArgs1(2)
        optionD = OptionBuilder.withValueSeparator0().hasOptionalArgs1(2).create1("D")

        # Create the '--property' option
        OptionBuilder.withValueSeparator0()
        OptionBuilder.withValueSeparator0().hasArgs1(2)
        OptionBuilder.withValueSeparator0().hasArgs1(2).withLongOpt("property")
        optionProperty = (
            OptionBuilder.withValueSeparator0()
            .hasArgs1(2)
            .withLongOpt("property")
            .create0()
        )

        # Add options to the options object
        options.addOption0(optionD)
        options.addOption0(optionProperty)

        # Parse the command line arguments
        parser = GnuParser()
        cl = parser.parse0(options, args)

        # Get properties for the '-D' option
        props = cl.getOptionProperties0(optionD)

        # Assertions
        self.assertIsNotNone(props, "null properties")
        self.assertEqual(4, len(props), f"number of properties in {props}")

    def testGetOptionPropertiesWithOption_test11_decomposed(self) -> None:
        args = [
            "-Dparam1=value1",
            "-Dparam2=value2",
            "-Dparam3",
            "-Dparam4=value4",
            "-D",
            "--property",
            "foo=bar",
        ]

        options = Options()

        # Create the '-D' option
        OptionBuilder.withValueSeparator0()
        OptionBuilder.withValueSeparator0().hasOptionalArgs1(2)
        optionD = OptionBuilder.withValueSeparator0().hasOptionalArgs1(2).create1("D")

        # Create the '--property' option
        OptionBuilder.withValueSeparator0()
        OptionBuilder.withValueSeparator0().hasArgs1(2)
        OptionBuilder.withValueSeparator0().hasArgs1(2).withLongOpt("property")
        optionProperty = (
            OptionBuilder.withValueSeparator0()
            .hasArgs1(2)
            .withLongOpt("property")
            .create0()
        )

        # Add options to the options object
        options.addOption0(optionD)
        options.addOption0(optionProperty)

        # Parse the command line arguments
        parser = GnuParser()
        cl = parser.parse0(options, args)

        # Get the properties for the '-D' option
        props = cl.getOptionProperties0(optionD)

    def testGetOptionPropertiesWithOption_test10_decomposed(self) -> None:
        args = [
            "-Dparam1=value1",
            "-Dparam2=value2",
            "-Dparam3",
            "-Dparam4=value4",
            "-D",
            "--property",
            "foo=bar",
        ]

        options = Options()

        OptionBuilder.withValueSeparator0()
        OptionBuilder.withValueSeparator0().hasOptionalArgs1(2)
        optionD = OptionBuilder.withValueSeparator0().hasOptionalArgs1(2).create1("D")

        OptionBuilder.withValueSeparator0()
        OptionBuilder.withValueSeparator0().hasArgs1(2)
        OptionBuilder.withValueSeparator0().hasArgs1(2).withLongOpt("property")
        optionProperty = (
            OptionBuilder.withValueSeparator0()
            .hasArgs1(2)
            .withLongOpt("property")
            .create0()
        )

        options.addOption0(optionD)
        options.addOption0(optionProperty)

        parser = GnuParser()
        cl = parser.parse0(options, args)

    def testGetOptionPropertiesWithOption_test9_decomposed(self) -> None:
        args = [
            "-Dparam1=value1",
            "-Dparam2=value2",
            "-Dparam3",
            "-Dparam4=value4",
            "-D",
            "--property",
            "foo=bar",
        ]
        options = Options()

        # Create the '-D' option
        OptionBuilder.withValueSeparator0()
        OptionBuilder.withValueSeparator0().hasOptionalArgs1(2)
        optionD = OptionBuilder.withValueSeparator0().hasOptionalArgs1(2).create1("D")

        # Create the '--property' option
        OptionBuilder.withValueSeparator0()
        OptionBuilder.withValueSeparator0().hasArgs1(2)
        OptionBuilder.withValueSeparator0().hasArgs1(2).withLongOpt("property")
        optionProperty = (
            OptionBuilder.withValueSeparator0()
            .hasArgs1(2)
            .withLongOpt("property")
            .create0()
        )

        # Add options to the options object
        options.addOption0(optionD)
        options.addOption0(optionProperty)

        # Create the parser
        parser = GnuParser()

    def testGetOptionPropertiesWithOption_test8_decomposed(self) -> None:
        args = [
            "-Dparam1=value1",
            "-Dparam2=value2",
            "-Dparam3",
            "-Dparam4=value4",
            "-D",
            "--property",
            "foo=bar",
        ]
        options = Options()

        # Create the '-D' option
        OptionBuilder.withValueSeparator0()
        OptionBuilder.withValueSeparator0().hasOptionalArgs1(2)
        optionD = OptionBuilder.withValueSeparator0().hasOptionalArgs1(2).create1("D")

        # Create the '--property' option
        OptionBuilder.withValueSeparator0()
        OptionBuilder.withValueSeparator0().hasArgs1(2)
        OptionBuilder.withValueSeparator0().hasArgs1(2).withLongOpt("property")
        optionProperty = (
            OptionBuilder.withValueSeparator0()
            .hasArgs1(2)
            .withLongOpt("property")
            .create0()
        )

        # Add options to the options object
        options.addOption0(optionD)
        options.addOption0(optionProperty)

    def testGetOptionPropertiesWithOption_test7_decomposed(self) -> None:
        args = [
            "-Dparam1=value1",
            "-Dparam2=value2",
            "-Dparam3",
            "-Dparam4=value4",
            "-D",
            "--property",
            "foo=bar",
        ]
        options = Options()
        OptionBuilder.withValueSeparator0()
        OptionBuilder.withValueSeparator0().hasOptionalArgs1(2)
        optionD = OptionBuilder.withValueSeparator0().hasOptionalArgs1(2).create1("D")
        OptionBuilder.withValueSeparator0()
        OptionBuilder.withValueSeparator0().hasArgs1(2)
        OptionBuilder.withValueSeparator0().hasArgs1(2).withLongOpt("property")
        optionProperty = (
            OptionBuilder.withValueSeparator0()
            .hasArgs1(2)
            .withLongOpt("property")
            .create0()
        )

    def testGetOptionPropertiesWithOption_test6_decomposed(self) -> None:
        args = [
            "-Dparam1=value1",
            "-Dparam2=value2",
            "-Dparam3",
            "-Dparam4=value4",
            "-D",
            "--property",
            "foo=bar",
        ]
        options = Options()
        OptionBuilder.withValueSeparator0()
        OptionBuilder.withValueSeparator0().hasOptionalArgs1(2)
        optionD = OptionBuilder.withValueSeparator0().hasOptionalArgs1(2).create1("D")
        OptionBuilder.withValueSeparator0()
        OptionBuilder.withValueSeparator0().hasArgs1(2)
        OptionBuilder.withValueSeparator0().hasArgs1(2).withLongOpt("property")

    def testGetOptionPropertiesWithOption_test5_decomposed(self) -> None:
        args = [
            "-Dparam1=value1",
            "-Dparam2=value2",
            "-Dparam3",
            "-Dparam4=value4",
            "-D",
            "--property",
            "foo=bar",
        ]
        options = Options()
        OptionBuilder.withValueSeparator0()
        OptionBuilder.withValueSeparator0().hasOptionalArgs1(2)
        optionD = OptionBuilder.withValueSeparator0().hasOptionalArgs1(2).create1("D")
        OptionBuilder.withValueSeparator0()
        OptionBuilder.withValueSeparator0().hasArgs1(2)

    def testGetOptionPropertiesWithOption_test4_decomposed(self) -> None:
        args = [
            "-Dparam1=value1",
            "-Dparam2=value2",
            "-Dparam3",
            "-Dparam4=value4",
            "-D",
            "--property",
            "foo=bar",
        ]
        options = Options()
        OptionBuilder.withValueSeparator0()
        OptionBuilder.withValueSeparator0().hasOptionalArgs1(2)
        optionD = OptionBuilder.withValueSeparator0().hasOptionalArgs1(2).create1("D")
        OptionBuilder.withValueSeparator0()

    def testGetOptionPropertiesWithOption_test3_decomposed(self) -> None:
        args = [
            "-Dparam1=value1",
            "-Dparam2=value2",
            "-Dparam3",
            "-Dparam4=value4",
            "-D",
            "--property",
            "foo=bar",
        ]
        options = Options()
        OptionBuilder.withValueSeparator0()
        OptionBuilder.withValueSeparator0().hasOptionalArgs1(2)
        optionD = OptionBuilder.withValueSeparator0().hasOptionalArgs1(2).create1("D")

    def testGetOptionPropertiesWithOption_test2_decomposed(self) -> None:
        args = [
            "-Dparam1=value1",
            "-Dparam2=value2",
            "-Dparam3",
            "-Dparam4=value4",
            "-D",
            "--property",
            "foo=bar",
        ]
        options = Options()
        OptionBuilder.withValueSeparator0()
        OptionBuilder.withValueSeparator0().hasOptionalArgs1(2)

    def testGetOptionPropertiesWithOption_test1_decomposed(self) -> None:
        args = [
            "-Dparam1=value1",
            "-Dparam2=value2",
            "-Dparam3",
            "-Dparam4=value4",
            "-D",
            "--property",
            "foo=bar",
        ]
        options = Options()
        OptionBuilder.withValueSeparator0()

    def testGetOptionPropertiesWithOption_test0_decomposed(self) -> None:
        args = [
            "-Dparam1=value1",
            "-Dparam2=value2",
            "-Dparam3",
            "-Dparam4=value4",
            "-D",
            "--property",
            "foo=bar",
        ]
        options = Options()

    def testGetOptionProperties_test16_decomposed(self) -> None:
        args = [
            "-Dparam1=value1",
            "-Dparam2=value2",
            "-Dparam3",
            "-Dparam4=value4",
            "-D",
            "--property",
            "foo=bar",
        ]
        options = Options()
        OptionBuilder.withValueSeparator0()
        OptionBuilder.withValueSeparator0().hasOptionalArgs1(2)
        OptionBuilder.withValueSeparator0().hasOptionalArgs1(2).create1("D")
        options.addOption0(
            OptionBuilder.withValueSeparator0().hasOptionalArgs1(2).create1("D")
        )
        OptionBuilder.withValueSeparator0()
        OptionBuilder.withValueSeparator0().hasArgs1(2)
        OptionBuilder.withValueSeparator0().hasArgs1(2).withLongOpt("property")
        OptionBuilder.withValueSeparator0().hasArgs1(2).withLongOpt(
            "property"
        ).create0()
        options.addOption0(
            OptionBuilder.withValueSeparator0()
            .hasArgs1(2)
            .withLongOpt("property")
            .create0()
        )
        parser = GnuParser()
        cl = parser.parse0(options, args)
        props = cl.getOptionProperties1("D")
        self.assertIsNotNone(props, "null properties")
        self.assertEqual(4, len(props), f"number of properties in {props}")
        self.assertEqual("value1", props.get("param1"), "property 1")
        self.assertEqual("value2", props.get("param2"), "property 2")
        self.assertEqual("true", props.get("param3"), "property 3")
        self.assertEqual("value4", props.get("param4"), "property 4")
        self.assertEqual(
            "bar",
            cl.getOptionProperties1("property").get("foo"),
            "property with long format",
        )

    def testGetOptionProperties_test15_decomposed(self) -> None:
        args = [
            "-Dparam1=value1",
            "-Dparam2=value2",
            "-Dparam3",
            "-Dparam4=value4",
            "-D",
            "--property",
            "foo=bar",
        ]

        options = Options()

        # Configure the 'D' option
        OptionBuilder.withValueSeparator0()
        OptionBuilder.withValueSeparator0().hasOptionalArgs1(2)
        d_option = OptionBuilder.withValueSeparator0().hasOptionalArgs1(2).create1("D")
        options.addOption0(d_option)

        # Configure the '--property' option
        OptionBuilder.withValueSeparator0()
        OptionBuilder.withValueSeparator0().hasArgs1(2)
        property_option = (
            OptionBuilder.withValueSeparator0()
            .hasArgs1(2)
            .withLongOpt("property")
            .create0()
        )
        options.addOption0(property_option)

        # Parse the command line arguments
        parser = GnuParser()
        cl = parser.parse0(options, args)

        # Retrieve properties for the 'D' option
        props = cl.getOptionProperties1("D")

        # Assertions
        self.assertIsNotNone(props, "null properties")
        self.assertEqual(4, len(props), f"number of properties in {props}")
        self.assertEqual("value1", props.get("param1"), "property 1")
        self.assertEqual("value2", props.get("param2"), "property 2")
        self.assertEqual("true", props.get("param3"), "property 3")
        self.assertEqual("value4", props.get("param4"), "property 4")

    def testGetOptionProperties_test14_decomposed(self) -> None:
        args = [
            "-Dparam1=value1",
            "-Dparam2=value2",
            "-Dparam3",
            "-Dparam4=value4",
            "-D",
            "--property",
            "foo=bar",
        ]
        options = Options()
        OptionBuilder.withValueSeparator0()
        OptionBuilder.withValueSeparator0().hasOptionalArgs1(2)
        OptionBuilder.withValueSeparator0().hasOptionalArgs1(2).create1("D")
        options.addOption0(
            OptionBuilder.withValueSeparator0().hasOptionalArgs1(2).create1("D")
        )
        OptionBuilder.withValueSeparator0()
        OptionBuilder.withValueSeparator0().hasArgs1(2)
        OptionBuilder.withValueSeparator0().hasArgs1(2).withLongOpt("property")
        OptionBuilder.withValueSeparator0().hasArgs1(2).withLongOpt(
            "property"
        ).create0()
        options.addOption0(
            OptionBuilder.withValueSeparator0()
            .hasArgs1(2)
            .withLongOpt("property")
            .create0()
        )
        parser = GnuParser()
        cl = parser.parse0(options, args)
        props = cl.getOptionProperties1("D")
        self.assertIsNotNone(props, "null properties")
        self.assertEqual(4, len(props), f"number of properties in {props}")
        self.assertEqual("value1", props.get("param1"), "property 1")
        self.assertEqual("value2", props.get("param2"), "property 2")

    def testGetOptionProperties_test13_decomposed(self) -> None:
        args = [
            "-Dparam1=value1",
            "-Dparam2=value2",
            "-Dparam3",
            "-Dparam4=value4",
            "-D",
            "--property",
            "foo=bar",
        ]

        options = Options()

        # Create and configure the '-D' option
        option_d = OptionBuilder.withValueSeparator0().hasOptionalArgs1(2).create1("D")
        options.addOption0(option_d)

        # Create and configure the '--property' option
        option_property = (
            OptionBuilder.withValueSeparator0()
            .hasArgs1(2)
            .withLongOpt("property")
            .create0()
        )
        options.addOption0(option_property)

        # Parse the command line arguments
        parser = GnuParser()
        cl = parser.parse0(options, args)

        # Retrieve properties for the '-D' option
        props = cl.getOptionProperties1("D")

        # Assertions
        self.assertIsNotNone(props, "null properties")
        self.assertEqual(4, len(props), f"number of properties in {props}")

    def testGetOptionProperties_test12_decomposed(self) -> None:
        args = [
            "-Dparam1=value1",
            "-Dparam2=value2",
            "-Dparam3",
            "-Dparam4=value4",
            "-D",
            "--property",
            "foo=bar",
        ]

        options = Options()

        # Create and add the '-D' option
        option_d = OptionBuilder.withValueSeparator0().hasOptionalArgs1(2).create1("D")
        options.addOption0(option_d)

        # Create and add the '--property' option
        option_property = (
            OptionBuilder.withValueSeparator0()
            .hasArgs1(2)
            .withLongOpt("property")
            .create0()
        )
        options.addOption0(option_property)

        # Parse the command line arguments
        parser = GnuParser()
        cl = parser.parse0(options, args)

        # Retrieve the properties for the '-D' option
        props = cl.getOptionProperties1("D")

        # Assertions or further processing can be added here if needed

    def testGetOptionProperties_test11_decomposed(self) -> None:
        args = [
            "-Dparam1=value1",
            "-Dparam2=value2",
            "-Dparam3",
            "-Dparam4=value4",
            "-D",
            "--property",
            "foo=bar",
        ]

        options = Options()

        # Create and configure the '-D' option
        option_d = OptionBuilder.withValueSeparator0().hasOptionalArgs1(2).create1("D")
        options.addOption0(option_d)

        # Create and configure the '--property' option
        option_property = (
            OptionBuilder.withValueSeparator0()
            .hasArgs1(2)
            .withLongOpt("property")
            .create0()
        )
        options.addOption0(option_property)

        # Parse the command line arguments
        parser = GnuParser()
        cl = parser.parse0(options, args)

    def testGetOptionProperties_test10_decomposed(self) -> None:
        args = [
            "-Dparam1=value1",
            "-Dparam2=value2",
            "-Dparam3",
            "-Dparam4=value4",
            "-D",
            "--property",
            "foo=bar",
        ]

        options = Options()

        # Create and configure the '-D' option
        option_d = OptionBuilder.withValueSeparator0().hasOptionalArgs1(2).create1("D")
        options.addOption0(option_d)

        # Create and configure the '--property' option
        option_property = (
            OptionBuilder.withValueSeparator0()
            .hasArgs1(2)
            .withLongOpt("property")
            .create0()
        )
        options.addOption0(option_property)

        # Instantiate the parser
        parser = GnuParser()

    def testGetOptionProperties_test9_decomposed(self) -> None:
        args = [
            "-Dparam1=value1",
            "-Dparam2=value2",
            "-Dparam3",
            "-Dparam4=value4",
            "-D",
            "--property",
            "foo=bar",
        ]
        options = Options()

        # Create and configure the first option (-D)
        option_d = OptionBuilder.withValueSeparator0().hasOptionalArgs1(2).create1("D")
        options.addOption0(option_d)

        # Create and configure the second option (--property)
        option_property = (
            OptionBuilder.withValueSeparator0()
            .hasArgs1(2)
            .withLongOpt("property")
            .create0()
        )
        options.addOption0(option_property)

    def testGetOptionProperties_test8_decomposed(self) -> None:
        args = [
            "-Dparam1=value1",
            "-Dparam2=value2",
            "-Dparam3",
            "-Dparam4=value4",
            "-D",
            "--property",
            "foo=bar",
        ]
        options = Options()
        OptionBuilder.withValueSeparator0()
        OptionBuilder.withValueSeparator0().hasOptionalArgs1(2)
        option_d = OptionBuilder.withValueSeparator0().hasOptionalArgs1(2).create1("D")
        options.addOption0(option_d)
        OptionBuilder.withValueSeparator0()
        OptionBuilder.withValueSeparator0().hasArgs1(2)
        option_property = (
            OptionBuilder.withValueSeparator0()
            .hasArgs1(2)
            .withLongOpt("property")
            .create0()
        )

    def testGetOptionProperties_test7_decomposed(self) -> None:
        args = [
            "-Dparam1=value1",
            "-Dparam2=value2",
            "-Dparam3",
            "-Dparam4=value4",
            "-D",
            "--property",
            "foo=bar",
        ]
        options = Options()
        OptionBuilder.withValueSeparator0()
        OptionBuilder.withValueSeparator0().hasOptionalArgs1(2)
        OptionBuilder.withValueSeparator0().hasOptionalArgs1(2).create1("D")
        options.addOption0(
            OptionBuilder.withValueSeparator0().hasOptionalArgs1(2).create1("D")
        )
        OptionBuilder.withValueSeparator0()
        OptionBuilder.withValueSeparator0().hasArgs1(2)
        OptionBuilder.withValueSeparator0().hasArgs1(2).withLongOpt("property")

    def testGetOptionProperties_test6_decomposed(self) -> None:
        args = [
            "-Dparam1=value1",
            "-Dparam2=value2",
            "-Dparam3",
            "-Dparam4=value4",
            "-D",
            "--property",
            "foo=bar",
        ]
        options = Options()
        OptionBuilder.withValueSeparator0()
        OptionBuilder.withValueSeparator0().hasOptionalArgs1(2)
        option_d = OptionBuilder.withValueSeparator0().hasOptionalArgs1(2).create1("D")
        options.addOption0(option_d)
        OptionBuilder.withValueSeparator0()
        OptionBuilder.withValueSeparator0().hasArgs1(2)

    def testGetOptionProperties_test5_decomposed(self) -> None:
        args = [
            "-Dparam1=value1",
            "-Dparam2=value2",
            "-Dparam3",
            "-Dparam4=value4",
            "-D",
            "--property",
            "foo=bar",
        ]
        options = Options()
        OptionBuilder.withValueSeparator0()
        OptionBuilder.withValueSeparator0().hasOptionalArgs1(2)
        option = OptionBuilder.withValueSeparator0().hasOptionalArgs1(2).create1("D")
        options.addOption0(option)
        OptionBuilder.withValueSeparator0()

    def testGetOptionProperties_test4_decomposed(self) -> None:
        args = [
            "-Dparam1=value1",
            "-Dparam2=value2",
            "-Dparam3",
            "-Dparam4=value4",
            "-D",
            "--property",
            "foo=bar",
        ]
        options = Options()
        option_builder = OptionBuilder.withValueSeparator0()
        option_builder = option_builder.hasOptionalArgs1(2)
        option = option_builder.create1("D")
        options.addOption0(option)

    def testGetOptionProperties_test3_decomposed(self) -> None:
        args = [
            "-Dparam1=value1",
            "-Dparam2=value2",
            "-Dparam3",
            "-Dparam4=value4",
            "-D",
            "--property",
            "foo=bar",
        ]
        options = Options()
        OptionBuilder.withValueSeparator0()
        OptionBuilder.withValueSeparator0().hasOptionalArgs1(2)
        OptionBuilder.withValueSeparator0().hasOptionalArgs1(2).create1("D")

    def testGetOptionProperties_test2_decomposed(self) -> None:
        args = [
            "-Dparam1=value1",
            "-Dparam2=value2",
            "-Dparam3",
            "-Dparam4=value4",
            "-D",
            "--property",
            "foo=bar",
        ]
        options = Options()
        OptionBuilder.withValueSeparator0()
        OptionBuilder.withValueSeparator0().hasOptionalArgs1(2)

    def testGetOptionProperties_test1_decomposed(self) -> None:
        args = [
            "-Dparam1=value1",
            "-Dparam2=value2",
            "-Dparam3",
            "-Dparam4=value4",
            "-D",
            "--property",
            "foo=bar",
        ]
        options = Options()
        OptionBuilder.withValueSeparator0()

    def testGetOptionProperties_test0_decomposed(self) -> None:
        args = [
            "-Dparam1=value1",
            "-Dparam2=value2",
            "-Dparam3",
            "-Dparam4=value4",
            "-D",
            "--property",
            "foo=bar",
        ]
        options = Options()

    def testBuilder_test9_decomposed(self) -> None:
        builder = Builder()
        builder.addArg("foo").addArg("bar")
        Option.builder1("T")
        Option.builder1("T").build()
        builder.addOption(Option.builder1("T").build())
        cmd = builder.build()
        self.assertEqual("foo", cmd.getArgs()[0])
        self.assertEqual("bar", cmd.getArgList()[1])
        cmd.getOptions()
        self.assertEqual("T", cmd.getOptions()[0].getOpt())

    def testBuilder_test8_decomposed(self) -> None:
        builder = Builder()
        builder.addArg("foo").addArg("bar")
        Option.builder1("T")
        Option.builder1("T").build()
        builder.addOption(Option.builder1("T").build())
        cmd = builder.build()
        self.assertEqual("foo", cmd.getArgs()[0])
        self.assertEqual("bar", cmd.getArgList()[1])
        cmd.getOptions()

    def testBuilder_test7_decomposed(self) -> None:
        builder = Builder()
        builder.addArg("foo").addArg("bar")
        Option.builder1("T")
        Option.builder1("T").build()
        builder.addOption(Option.builder1("T").build())
        cmd = builder.build()
        self.assertEqual("foo", cmd.getArgs()[0])
        self.assertEqual("bar", cmd.getArgList()[1])

    def testBuilder_test6_decomposed(self) -> None:
        builder = Builder()
        builder.addArg("foo").addArg("bar")
        Option.builder1("T")
        Option.builder1("T").build()
        builder.addOption(Option.builder1("T").build())
        cmd = builder.build()
        self.assertEqual("foo", cmd.getArgs()[0])

    def testBuilder_test5_decomposed(self) -> None:
        builder = Builder()
        builder.addArg("foo").addArg("bar")
        Option.builder1("T")
        Option.builder1("T").build()
        builder.addOption(Option.builder1("T").build())
        cmd = builder.build()

    def testBuilder_test4_decomposed(self) -> None:
        builder = Builder()
        builder.addArg("foo").addArg("bar")
        Option.builder1("T")
        Option.builder1("T").build()
        builder.addOption(Option.builder1("T").build())

    def testBuilder_test3_decomposed(self) -> None:
        builder = Builder()
        builder.addArg("foo").addArg("bar")
        Option.builder1("T")
        Option.builder1("T").build()

    def testBuilder_test2_decomposed(self) -> None:
        builder = Builder()
        builder.addArg("foo").addArg("bar")
        Option.builder1("T")

    def testBuilder_test1_decomposed(self) -> None:
        builder = Builder()
        builder.addArg("foo").addArg("bar")

    def testBuilder_test0_decomposed(self) -> None:
        builder = CommandLine.Builder()
