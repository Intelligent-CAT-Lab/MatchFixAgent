from __future__ import annotations
import re
import unittest
import pytest
import io
import typing
from typing import *
import os
import unittest
from src.main.org.apache.commons.codec.CharEncoding import *
from src.main.org.apache.commons.codec.DecoderException import *
from src.main.org.apache.commons.codec.net.RFC1522Codec import *


class RFC1522CodecTest(unittest.TestCase):

    def testDecodeInvalid_test0_decomposed(self) -> None:
        self.__assertExpectedDecoderException("whatever")
        self.__assertExpectedDecoderException("=?")
        self.__assertExpectedDecoderException("?=")
        self.__assertExpectedDecoderException("==")
        self.__assertExpectedDecoderException("=??=")
        self.__assertExpectedDecoderException("=?stuff?=")
        self.__assertExpectedDecoderException("=?UTF-8??=")
        self.__assertExpectedDecoderException("=?UTF-8?stuff?=")
        self.__assertExpectedDecoderException("=?UTF-8?T?stuff")
        self.__assertExpectedDecoderException("=??T?stuff?=")
        self.__assertExpectedDecoderException("=?UTF-8??stuff?=")
        self.__assertExpectedDecoderException("=?UTF-8?W?stuff?=")

    def testNullInput_test2_decomposed(self) -> None:
        testcodec = RFC1522Codec()
        self.assertIsNone(testcodec._decodeText(None))
        self.assertIsNone(testcodec._encodeText1(None, CharEncoding.UTF_8))

    def testNullInput_test1_decomposed(self) -> None:
        testcodec = RFC1522TestCodec()
        self.assertIsNone(testcodec._decodeText(None))

    def testNullInput_test0_decomposed(self) -> None:
        testcodec = RFC1522TestCodec()

    def __assertExpectedDecoderException(self, s: str) -> None:
        testcodec = RFC1522TestCodec()
        with self.assertRaises(
            DecoderException, msg="DecoderException should have been thrown"
        ):
            testcodec._decodeText(s)


class RFC1522TestCodec(RFC1522Codec):

    def _getEncoding(self) -> str:
        return "T"

    def _doEncoding(self, bytes_: typing.List[int]) -> typing.List[int]:
        return bytes_

    def _doDecoding(self, bytes_: typing.List[int]) -> typing.List[int]:
        return bytes_
