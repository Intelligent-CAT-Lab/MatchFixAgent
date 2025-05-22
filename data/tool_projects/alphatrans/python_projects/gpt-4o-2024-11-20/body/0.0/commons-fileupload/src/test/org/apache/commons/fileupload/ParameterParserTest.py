from __future__ import annotations
import re
import unittest
import pytest
import io
import typing
from typing import *
import os
import unittest
from src.main.org.apache.commons.fileupload.ParameterParser import *


class ParameterParserTest(unittest.TestCase):

    def testfileUpload199_test2_decomposed(self) -> None:
        parser = ParameterParser()
        s = (
            'Content-Disposition: form-data; name="file";'
            + ' filename="=?ISO-8859-1?B?SWYgeW91IGNhbiByZWFkIHRoaXMgeW8=?='
            + ' =?ISO-8859-2?B?dSB1bmRlcnN0YW5kIHRoZSBleGFtcGxlLg==?="\r\n'
        )
        params = parser.parse0(s, [",", ";"])
        self.assertEqual(
            "If you can read this you understand the example.", params.get("filename")
        )

    def testfileUpload199_test1_decomposed(self) -> None:
        parser = ParameterParser()
        s = (
            'Content-Disposition: form-data; name="file";'
            + ' filename="=?ISO-8859-1?B?SWYgeW91IGNhbiByZWFkIHRoaXMgeW8=?='
            + ' =?ISO-8859-2?B?dSB1bmRlcnN0YW5kIHRoZSBleGFtcGxlLg==?="\r\n'
        )
        params = parser.parse0(s, [",", ";"])

    def testfileUpload199_test0_decomposed(self) -> None:
        parser = ParameterParser()

    def testFileUpload139_test6_decomposed(self) -> None:
        parser = ParameterParser()

        s = "Content-type: multipart/form-data , boundary=AaB03x"
        params = parser.parse0(s, [",", ";"])
        self.assertEqual("AaB03x", params.get("boundary"))

        s = "Content-type: multipart/form-data, boundary=AaB03x"
        params = parser.parse0(s, [";", ","])
        self.assertEqual("AaB03x", params.get("boundary"))

        s = "Content-type: multipart/mixed, boundary=BbC04y"
        params = parser.parse0(s, [",", ";"])
        self.assertEqual("BbC04y", params.get("boundary"))

    def testFileUpload139_test5_decomposed(self) -> None:
        parser = ParameterParser()

        s = "Content-type: multipart/form-data , boundary=AaB03x"
        params = parser.parse0(s, [",", ";"])
        self.assertEqual("AaB03x", params.get("boundary"))

        s = "Content-type: multipart/form-data, boundary=AaB03x"
        params = parser.parse0(s, [";", ","])
        self.assertEqual("AaB03x", params.get("boundary"))

        s = "Content-type: multipart/mixed, boundary=BbC04y"
        params = parser.parse0(s, [",", ";"])

    def testFileUpload139_test4_decomposed(self) -> None:
        parser = ParameterParser()
        s = "Content-type: multipart/form-data , boundary=AaB03x"
        params = parser.parse0(s, [",", ";"])
        self.assertEqual("AaB03x", params.get("boundary"))

        s = "Content-type: multipart/form-data, boundary=AaB03x"
        params = parser.parse0(s, [";", ","])
        self.assertEqual("AaB03x", params.get("boundary"))

    def testFileUpload139_test3_decomposed(self) -> None:
        parser = ParameterParser()
        s = "Content-type: multipart/form-data , boundary=AaB03x"
        params = parser.parse0(s, [",", ";"])
        self.assertEqual("AaB03x", params.get("boundary"))

        s = "Content-type: multipart/form-data, boundary=AaB03x"
        params = parser.parse0(s, [";", ","])

    def testFileUpload139_test2_decomposed(self) -> None:
        parser = ParameterParser()
        s = "Content-type: multipart/form-data , boundary=AaB03x"
        params = parser.parse0(s, [",", ";"])
        self.assertEqual("AaB03x", params.get("boundary"))

    def testFileUpload139_test1_decomposed(self) -> None:
        parser = ParameterParser()
        s = "Content-type: multipart/form-data , boundary=AaB03x"
        params = parser.parse0(s, [",", ";"])

    def testFileUpload139_test0_decomposed(self) -> None:
        parser = ParameterParser()

    def testParsingEscapedChars_test5_decomposed(self) -> None:
        s = 'param = "stuff\\"; more stuff"'
        parser = ParameterParser()
        params = parser.parse1(s, ";")
        self.assertEqual(1, len(params))
        self.assertEqual('stuff\\"; more stuff', params.get("param"))

        s = 'param = "stuff\\\\"; anotherparam'
        params = parser.parse1(s, ";")
        self.assertEqual(2, len(params))
        self.assertEqual("stuff\\\\", params.get("param"))
        self.assertIsNone(params.get("anotherparam"))

    def testParsingEscapedChars_test4_decomposed(self) -> None:
        s = 'param = "stuff\\"; more stuff"'
        parser = ParameterParser()
        params = parser.parse1(s, ";")
        self.assertEqual(1, len(params))
        self.assertEqual('stuff\\"; more stuff', params.get("param"))

        s = 'param = "stuff\\\\"; anotherparam'
        params = parser.parse1(s, ";")
        self.assertEqual(2, len(params))
        self.assertEqual("stuff\\\\", params.get("param"))

    def testParsingEscapedChars_test3_decomposed(self) -> None:
        s = 'param = "stuff\\"; more stuff"'
        parser = ParameterParser()
        params = parser.parse1(s, ";")
        self.assertEqual(1, len(params))
        self.assertEqual('stuff\\"; more stuff', params.get("param"))

        s = 'param = "stuff\\\\"; anotherparam'
        params = parser.parse1(s, ";")

    def testParsingEscapedChars_test2_decomposed(self) -> None:
        s = 'param = "stuff\\"; more stuff"'
        parser = ParameterParser()
        params = parser.parse1(s, ";")
        self.assertEqual(1, len(params))
        self.assertEqual('stuff\\"; more stuff', params.get("param"))

    def testParsingEscapedChars_test1_decomposed(self) -> None:
        s = 'param = "stuff\\"; more stuff"'
        parser = ParameterParser()
        params = parser.parse1(s, ";")

    def testParsingEscapedChars_test0_decomposed(self) -> None:
        s = 'param = "stuff\\"; more stuff"'
        parser = ParameterParser()

    def testContentTypeParsing_test3_decomposed(self) -> None:
        s = "text/plain; Charset=UTF-8"
        parser = ParameterParser()
        parser.setLowerCaseNames(True)
        params = parser.parse1(s, ";")
        self.assertEqual("UTF-8", params.get("charset"))

    def testContentTypeParsing_test2_decomposed(self) -> None:
        s = "text/plain; Charset=UTF-8"
        parser = ParameterParser()
        parser.setLowerCaseNames(True)
        params = parser.parse1(s, ";")

    def testContentTypeParsing_test1_decomposed(self) -> None:
        s = "text/plain; Charset=UTF-8"
        parser = ParameterParser()
        parser.setLowerCaseNames(True)

    def testContentTypeParsing_test0_decomposed(self) -> None:
        s = "text/plain; Charset=UTF-8"
        parser = ParameterParser()

    def testParsing_test11_decomposed(self) -> None:
        s = 'test; test1 =  stuff   ; test2 =  "stuff; stuff"; test3="stuff'
        parser = ParameterParser()
        params = parser.parse1(s, ";")
        self.assertIsNone(params.get("test"))
        self.assertEqual("stuff", params.get("test1"))
        self.assertEqual("stuff; stuff", params.get("test2"))
        self.assertEqual('"stuff', params.get("test3"))

        params = parser.parse0(s, [",", ";"])
        self.assertIsNone(params.get("test"))
        self.assertEqual("stuff", params.get("test1"))
        self.assertEqual("stuff; stuff", params.get("test2"))
        self.assertEqual('"stuff', params.get("test3"))

        s = "  test  , test1=stuff   ,  , test2=, test3, "
        params = parser.parse1(s, ",")
        self.assertIsNone(params.get("test"))
        self.assertEqual("stuff", params.get("test1"))
        self.assertIsNone(params.get("test2"))
        self.assertIsNone(params.get("test3"))

        s = "  test"
        params = parser.parse1(s, ";")
        self.assertIsNone(params.get("test"))

        s = "  "
        params = parser.parse1(s, ";")
        self.assertEqual(0, len(params))

        s = " = stuff "
        params = parser.parse1(s, ";")
        self.assertEqual(0, len(params))

    def testParsing_test10_decomposed(self) -> None:
        s = 'test; test1 =  stuff   ; test2 =  "stuff; stuff"; test3="stuff'
        parser = ParameterParser()
        params = parser.parse1(s, ";")
        self.assertIsNone(params.get("test"))
        self.assertEqual("stuff", params.get("test1"))
        self.assertEqual("stuff; stuff", params.get("test2"))
        self.assertEqual('"stuff', params.get("test3"))

        params = parser.parse0(s, [",", ";"])
        self.assertIsNone(params.get("test"))
        self.assertEqual("stuff", params.get("test1"))
        self.assertEqual("stuff; stuff", params.get("test2"))
        self.assertEqual('"stuff', params.get("test3"))

        s = "  test  , test1=stuff   ,  , test2=, test3, "
        params = parser.parse1(s, ",")
        self.assertIsNone(params.get("test"))
        self.assertEqual("stuff", params.get("test1"))
        self.assertIsNone(params.get("test2"))
        self.assertIsNone(params.get("test3"))

        s = "  test"
        params = parser.parse1(s, ";")
        self.assertIsNone(params.get("test"))

        s = "  "
        params = parser.parse1(s, ";")
        self.assertEqual(0, len(params))

        s = " = stuff "
        params = parser.parse1(s, ";")

    def testParsing_test9_decomposed(self) -> None:
        s = 'test; test1 =  stuff   ; test2 =  "stuff; stuff"; test3="stuff'
        parser = ParameterParser()

        # Test parse1 with ';' as the separator
        params = parser.parse1(s, ";")
        self.assertIsNone(params.get("test"))
        self.assertEqual("stuff", params.get("test1"))
        self.assertEqual("stuff; stuff", params.get("test2"))
        self.assertEqual('"stuff', params.get("test3"))

        # Test parse0 with [',', ';'] as separators
        params = parser.parse0(s, [",", ";"])
        self.assertIsNone(params.get("test"))
        self.assertEqual("stuff", params.get("test1"))
        self.assertEqual("stuff; stuff", params.get("test2"))
        self.assertEqual('"stuff', params.get("test3"))

        # Test parse1 with ',' as the separator
        s = "  test  , test1=stuff   ,  , test2=, test3, "
        params = parser.parse1(s, ",")
        self.assertIsNone(params.get("test"))
        self.assertEqual("stuff", params.get("test1"))
        self.assertIsNone(params.get("test2"))
        self.assertIsNone(params.get("test3"))

        # Test parse1 with ';' as the separator
        s = "  test"
        params = parser.parse1(s, ";")
        self.assertIsNone(params.get("test"))

        # Test parse1 with an empty string
        s = "  "
        params = parser.parse1(s, ";")

    def testParsing_test8_decomposed(self) -> None:
        s = 'test; test1 =  stuff   ; test2 =  "stuff; stuff"; test3="stuff'
        parser = ParameterParser()

        # Test parse1 with ';' as the separator
        params = parser.parse1(s, ";")
        self.assertIsNone(params.get("test"))
        self.assertEqual("stuff", params.get("test1"))
        self.assertEqual("stuff; stuff", params.get("test2"))
        self.assertEqual('"stuff', params.get("test3"))

        # Test parse0 with [',', ';'] as separators
        params = parser.parse0(s, [",", ";"])
        self.assertIsNone(params.get("test"))
        self.assertEqual("stuff", params.get("test1"))
        self.assertEqual("stuff; stuff", params.get("test2"))
        self.assertEqual('"stuff', params.get("test3"))

        # Test parse1 with ',' as the separator
        s = "  test  , test1=stuff   ,  , test2=, test3, "
        params = parser.parse1(s, ",")
        self.assertIsNone(params.get("test"))
        self.assertEqual("stuff", params.get("test1"))
        self.assertIsNone(params.get("test2"))
        self.assertIsNone(params.get("test3"))

        # Test parse1 with ';' as the separator
        s = "  test"
        params = parser.parse1(s, ";")
        self.assertIsNone(params.get("test"))

    def testParsing_test7_decomposed(self) -> None:
        s = 'test; test1 =  stuff   ; test2 =  "stuff; stuff"; test3="stuff'
        parser = ParameterParser()

        # Test parse1 with ';' as the separator
        params = parser.parse1(s, ";")
        self.assertIsNone(params.get("test"))
        self.assertEqual("stuff", params.get("test1"))
        self.assertEqual("stuff; stuff", params.get("test2"))
        self.assertEqual('"stuff', params.get("test3"))

        # Test parse0 with [',', ';'] as separators
        params = parser.parse0(s, [",", ";"])
        self.assertIsNone(params.get("test"))
        self.assertEqual("stuff", params.get("test1"))
        self.assertEqual("stuff; stuff", params.get("test2"))
        self.assertEqual('"stuff', params.get("test3"))

        # Test parse1 with ',' as the separator
        s = "  test  , test1=stuff   ,  , test2=, test3, "
        params = parser.parse1(s, ",")
        self.assertIsNone(params.get("test"))
        self.assertEqual("stuff", params.get("test1"))
        self.assertIsNone(params.get("test2"))
        self.assertIsNone(params.get("test3"))

        # Test parse1 with ';' as the separator
        s = "  test"
        params = parser.parse1(s, ";")

    def testParsing_test6_decomposed(self) -> None:
        s = 'test; test1 =  stuff   ; test2 =  "stuff; stuff"; test3="stuff'
        parser = ParameterParser()

        # Test parse1 with ';' as the separator
        params = parser.parse1(s, ";")
        self.assertIsNone(params.get("test"))
        self.assertEqual("stuff", params.get("test1"))
        self.assertEqual("stuff; stuff", params.get("test2"))
        self.assertEqual('"stuff', params.get("test3"))

        # Test parse0 with [',', ';'] as the separators
        params = parser.parse0(s, [",", ";"])
        self.assertIsNone(params.get("test"))
        self.assertEqual("stuff", params.get("test1"))
        self.assertEqual("stuff; stuff", params.get("test2"))
        self.assertEqual('"stuff', params.get("test3"))

        # Update the string and test parse1 with ',' as the separator
        s = "  test  , test1=stuff   ,  , test2=, test3, "
        params = parser.parse1(s, ",")
        self.assertIsNone(params.get("test"))
        self.assertEqual("stuff", params.get("test1"))
        self.assertIsNone(params.get("test2"))
        self.assertIsNone(params.get("test3"))

    def testParsing_test5_decomposed(self) -> None:
        s = 'test; test1 =  stuff   ; test2 =  "stuff; stuff"; test3="stuff'
        parser = ParameterParser()

        # Test parse1 with ';' as the separator
        params = parser.parse1(s, ";")
        self.assertIsNone(params.get("test"))
        self.assertEqual("stuff", params.get("test1"))
        self.assertEqual("stuff; stuff", params.get("test2"))
        self.assertEqual('"stuff', params.get("test3"))

        # Test parse0 with ',' and ';' as separators
        params = parser.parse0(s, [",", ";"])
        self.assertIsNone(params.get("test"))
        self.assertEqual("stuff", params.get("test1"))
        self.assertEqual("stuff; stuff", params.get("test2"))
        self.assertEqual('"stuff', params.get("test3"))

        # Test parse1 with ',' as the separator
        s = "  test  , test1=stuff   ,  , test2=, test3, "
        params = parser.parse1(s, ",")

    def testParsing_test4_decomposed(self) -> None:
        s = 'test; test1 =  stuff   ; test2 =  "stuff; stuff"; test3="stuff'
        parser = ParameterParser()

        # Test parse1 method
        params = parser.parse1(s, ";")
        self.assertIsNone(params.get("test"))
        self.assertEqual("stuff", params.get("test1"))
        self.assertEqual("stuff; stuff", params.get("test2"))
        self.assertEqual('"stuff', params.get("test3"))

        # Test parse0 method
        params = parser.parse0(s, [",", ";"])
        self.assertIsNone(params.get("test"))
        self.assertEqual("stuff", params.get("test1"))
        self.assertEqual("stuff; stuff", params.get("test2"))
        self.assertEqual('"stuff', params.get("test3"))

    def testParsing_test3_decomposed(self) -> None:
        s = 'test; test1 =  stuff   ; test2 =  "stuff; stuff"; test3="stuff'
        parser = ParameterParser()

        # Call parse1 and validate results
        params = parser.parse1(s, ";")
        self.assertIsNone(params.get("test"))
        self.assertEqual("stuff", params.get("test1"))
        self.assertEqual("stuff; stuff", params.get("test2"))
        self.assertEqual('"stuff', params.get("test3"))

        # Call parse0 (no assertions provided in the original Java code)
        params = parser.parse0(s, [",", ";"])

    def testParsing_test2_decomposed(self) -> None:
        s = 'test; test1 =  stuff   ; test2 =  "stuff; stuff"; test3="stuff'
        parser = ParameterParser()
        params = parser.parse1(s, ";")
        self.assertIsNone(params.get("test"))
        self.assertEqual("stuff", params.get("test1"))
        self.assertEqual("stuff; stuff", params.get("test2"))
        self.assertEqual('"stuff', params.get("test3"))

    def testParsing_test1_decomposed(self) -> None:
        s = 'test; test1 =  stuff   ; test2 =  "stuff; stuff"; test3="stuff'
        parser = ParameterParser()
        params = parser.parse1(s, ";")

    def testParsing_test0_decomposed(self) -> None:
        s = 'test; test1 =  stuff   ; test2 =  "stuff; stuff"; test3="stuff'
        parser = ParameterParser()
