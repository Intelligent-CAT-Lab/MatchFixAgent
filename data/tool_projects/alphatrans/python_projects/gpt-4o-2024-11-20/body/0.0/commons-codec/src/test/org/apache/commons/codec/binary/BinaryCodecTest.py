from __future__ import annotations
import re
import unittest
import pytest
import io
import typing
from typing import *
import os
import unittest
from src.main.org.apache.commons.codec.DecoderException import *
from src.main.org.apache.commons.codec.EncoderException import *
from src.main.org.apache.commons.codec.binary.BinaryCodec import *


class BinaryCodecTest(unittest.TestCase):

    __BIT_7: int = 0x80
    __BIT_6: int = 0x40
    __BIT_5: int = 0x20
    __BIT_4: int = 0x10
    __BIT_3: int = 0x08
    __BIT_2: int = 0x04
    __BIT_1: int = 0x02
    __BIT_0: int = 0x01
    __CHARSET_UTF8: str = "utf-8"
    instance: BinaryCodec = None

    def testEncodeObject_test26_decomposed(self) -> None:
        bits = bytearray(1)
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("00000000", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("00000001", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("00000011", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("00000111", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("00001111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        )
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("00011111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
        )
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("00111111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
        )
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("01111111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("11111111", l_encoded)

        bits = bytearray(2)
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("0000000000000000", l_encoded)

        bits = bytearray(2)
        bits[0] = self.__BIT_0
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("0000000000000001", l_encoded)

        bits = bytearray(2)
        bits[0] = self.__BIT_0 | self.__BIT_1
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("0000000000000011", l_encoded)

        bits = bytearray(2)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("0000000000000111", l_encoded)

        bits = bytearray(2)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("0000000000001111", l_encoded)

        bits = bytearray(2)
        bits[0] = (
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        )
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("0000000000011111", l_encoded)

        bits = bytearray(2)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
        )
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("0000000000111111", l_encoded)

        bits = bytearray(2)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
        )
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("0000000001111111", l_encoded)

        bits = bytearray(2)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("0000000011111111", l_encoded)

        bits = bytearray(2)
        bits[1] = self.__BIT_0
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("0000000111111111", l_encoded)

        bits = bytearray(2)
        bits[1] = self.__BIT_0 | self.__BIT_1
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("0000001111111111", l_encoded)

        bits = bytearray(2)
        bits[1] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("0000011111111111", l_encoded)

        bits = bytearray(2)
        bits[1] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("0000111111111111", l_encoded)

        bits = bytearray(2)
        bits[1] = (
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        )
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("0001111111111111", l_encoded)

        bits = bytearray(2)
        bits[1] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
        )
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("0011111111111111", l_encoded)

        bits = bytearray(2)
        bits[1] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
        )
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("0111111111111111", l_encoded)

        bits = bytearray(2)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        bits[1] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("1111111111111111", l_encoded)

    def testEncodeObject_test25_decomposed(self) -> None:
        bits = bytearray(1)
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("00000000", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("00000001", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("00000011", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("00000111", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("00001111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        )
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("00011111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
        )
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("00111111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
        )
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("01111111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("11111111", l_encoded)

        bits = bytearray(2)
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("0000000000000000", l_encoded)

        bits = bytearray(2)
        bits[0] = self.__BIT_0
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("0000000000000001", l_encoded)

        bits = bytearray(2)
        bits[0] = self.__BIT_0 | self.__BIT_1
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("0000000000000011", l_encoded)

        bits = bytearray(2)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("0000000000000111", l_encoded)

        bits = bytearray(2)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("0000000000001111", l_encoded)

        bits = bytearray(2)
        bits[0] = (
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        )
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("0000000000011111", l_encoded)

        bits = bytearray(2)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
        )
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("0000000000111111", l_encoded)

        bits = bytearray(2)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
        )
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("0000000001111111", l_encoded)

        bits = bytearray(2)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("0000000011111111", l_encoded)

        bits = bytearray(2)
        bits[1] = self.__BIT_0
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("0000000111111111", l_encoded)

        bits = bytearray(2)
        bits[1] = self.__BIT_0 | self.__BIT_1
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("0000001111111111", l_encoded)

        bits = bytearray(2)
        bits[1] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("0000011111111111", l_encoded)

        bits = bytearray(2)
        bits[1] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("0000111111111111", l_encoded)

        bits = bytearray(2)
        bits[1] = (
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        )
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("0001111111111111", l_encoded)

        bits = bytearray(2)
        bits[1] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
        )
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("0011111111111111", l_encoded)

        bits = bytearray(2)
        bits[1] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
        )
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("0111111111111111", l_encoded)

        bits = bytearray(2)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        bits[1] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("1111111111111111", l_encoded)

    def testEncodeObject_test24_decomposed(self) -> None:
        bits = bytearray(1)
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("00000000", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("00000001", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("00000011", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("00000111", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("00001111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        )
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("00011111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
        )
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("00111111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
        )
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("01111111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("11111111", l_encoded)

        bits = bytearray(2)
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("0000000000000000", l_encoded)

        bits = bytearray(2)
        bits[0] = self.__BIT_0
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("0000000000000001", l_encoded)

        bits = bytearray(2)
        bits[0] = self.__BIT_0 | self.__BIT_1
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("0000000000000011", l_encoded)

        bits = bytearray(2)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("0000000000000111", l_encoded)

        bits = bytearray(2)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("0000000000001111", l_encoded)

        bits = bytearray(2)
        bits[0] = (
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        )
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("0000000000011111", l_encoded)

        bits = bytearray(2)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
        )
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("0000000000111111", l_encoded)

        bits = bytearray(2)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
        )
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("0000000001111111", l_encoded)

        bits = bytearray(2)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("0000000011111111", l_encoded)

        bits = bytearray(2)
        bits[1] = self.__BIT_0
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("0000000111111111", l_encoded)

        bits = bytearray(2)
        bits[1] = self.__BIT_0 | self.__BIT_1
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("0000001111111111", l_encoded)

        bits = bytearray(2)
        bits[1] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("0000011111111111", l_encoded)

        bits = bytearray(2)
        bits[1] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("0000111111111111", l_encoded)

        bits = bytearray(2)
        bits[1] = (
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        )
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("0001111111111111", l_encoded)

        bits = bytearray(2)
        bits[1] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
        )
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("0011111111111111", l_encoded)

        bits = bytearray(2)
        bits[1] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
        )
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("0111111111111111", l_encoded)

    def testEncodeObject_test23_decomposed(self) -> None:
        bits = bytearray(1)
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("00000000", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("00000001", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("00000011", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("00000111", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("00001111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        )
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("00011111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
        )
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("00111111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
        )
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("01111111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("11111111", l_encoded)

        bits = bytearray(2)
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("0000000000000000", l_encoded)

        bits = bytearray(2)
        bits[0] = self.__BIT_0
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("0000000000000001", l_encoded)

        bits = bytearray(2)
        bits[0] = self.__BIT_0 | self.__BIT_1
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("0000000000000011", l_encoded)

        bits = bytearray(2)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("0000000000000111", l_encoded)

        bits = bytearray(2)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("0000000000001111", l_encoded)

        bits = bytearray(2)
        bits[0] = (
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        )
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("0000000000011111", l_encoded)

        bits = bytearray(2)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
        )
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("0000000000111111", l_encoded)

        bits = bytearray(2)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
        )
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("0000000001111111", l_encoded)

        bits = bytearray(2)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("0000000011111111", l_encoded)

        bits = bytearray(2)
        bits[1] = self.__BIT_0
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("0000000111111111", l_encoded)

        bits = bytearray(2)
        bits[1] = self.__BIT_0 | self.__BIT_1
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("0000001111111111", l_encoded)

        bits = bytearray(2)
        bits[1] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("0000011111111111", l_encoded)

        bits = bytearray(2)
        bits[1] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("0000111111111111", l_encoded)

        bits = bytearray(2)
        bits[1] = (
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        )
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("0001111111111111", l_encoded)

        bits = bytearray(2)
        bits[1] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
        )
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("0001111111111111", l_encoded)

    def testEncodeObject_test22_decomposed(self) -> None:
        bits = bytearray(1)
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("00000000", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("00000001", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("00000011", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("00000111", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("00001111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        )
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("00011111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
        )
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("00111111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
        )
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("01111111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("11111111", l_encoded)

        bits = bytearray(2)
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("0000000000000000", l_encoded)

        bits = bytearray(2)
        bits[0] = self.__BIT_0
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("0000000000000001", l_encoded)

        bits = bytearray(2)
        bits[0] = self.__BIT_0 | self.__BIT_1
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("0000000000000011", l_encoded)

        bits = bytearray(2)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("0000000000000111", l_encoded)

        bits = bytearray(2)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("0000000000001111", l_encoded)

        bits = bytearray(2)
        bits[0] = (
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        )
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("0000000000011111", l_encoded)

        bits = bytearray(2)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
        )
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("0000000000111111", l_encoded)

        bits = bytearray(2)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
        )
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("0000000001111111", l_encoded)

        bits = bytearray(2)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("0000000011111111", l_encoded)

        bits = bytearray(2)
        bits[1] = self.__BIT_0
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("0000000111111111", l_encoded)

        bits = bytearray(2)
        bits[1] = self.__BIT_0 | self.__BIT_1
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("0000001111111111", l_encoded)

        bits = bytearray(2)
        bits[1] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("0000011111111111", l_encoded)

        bits = bytearray(2)
        bits[1] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("0000111111111111", l_encoded)

        bits = bytearray(2)
        bits[1] = (
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        )
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("0001111111111111", l_encoded)

    def testEncodeObject_test21_decomposed(self) -> None:
        bits = bytearray(1)
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("00000000", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("00000001", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("00000011", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("00000111", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("00001111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        )
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("00011111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
        )
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("00111111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
        )
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("01111111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("11111111", l_encoded)

        bits = bytearray(2)
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("0000000000000000", l_encoded)

        bits = bytearray(2)
        bits[0] = self.__BIT_0
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("0000000000000001", l_encoded)

        bits = bytearray(2)
        bits[0] = self.__BIT_0 | self.__BIT_1
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("0000000000000011", l_encoded)

        bits = bytearray(2)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("0000000000000111", l_encoded)

        bits = bytearray(2)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("0000000000001111", l_encoded)

        bits = bytearray(2)
        bits[0] = (
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        )
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("0000000000011111", l_encoded)

        bits = bytearray(2)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
        )
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("0000000000111111", l_encoded)

        bits = bytearray(2)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
        )
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("0000000001111111", l_encoded)

        bits = bytearray(2)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("0000000011111111", l_encoded)

        bits = bytearray(2)
        bits[1] = self.__BIT_0
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("0000000111111111", l_encoded)

        bits = bytearray(2)
        bits[1] = self.__BIT_0 | self.__BIT_1
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("0000001111111111", l_encoded)

        bits = bytearray(2)
        bits[1] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("0000011111111111", l_encoded)

        bits = bytearray(2)
        bits[1] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("0000111111111111", l_encoded)

    def testEncodeObject_test20_decomposed(self) -> None:
        bits = bytearray(1)
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("00000000", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("00000001", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("00000011", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("00000111", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("00001111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        )
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("00011111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
        )
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("00111111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
        )
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("01111111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("11111111", l_encoded)

        bits = bytearray(2)
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("0000000000000000", l_encoded)

        bits = bytearray(2)
        bits[0] = self.__BIT_0
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("0000000000000001", l_encoded)

        bits = bytearray(2)
        bits[0] = self.__BIT_0 | self.__BIT_1
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("0000000000000011", l_encoded)

        bits = bytearray(2)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("0000000000000111", l_encoded)

        bits = bytearray(2)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("0000000000001111", l_encoded)

        bits = bytearray(2)
        bits[0] = (
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        )
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("0000000000011111", l_encoded)

        bits = bytearray(2)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
        )
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("0000000000111111", l_encoded)

        bits = bytearray(2)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
        )
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("0000000001111111", l_encoded)

        bits = bytearray(2)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("0000000011111111", l_encoded)

        bits = bytearray(2)
        bits[1] = self.__BIT_0
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("0000000111111111", l_encoded)

        bits = bytearray(2)
        bits[1] = self.__BIT_0 | self.__BIT_1
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("0000001111111111", l_encoded)

        bits = bytearray(2)
        bits[1] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("0000001111111111", l_encoded)

    def testEncodeObject_test19_decomposed(self) -> None:
        bits = bytearray(1)
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("00000000", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("00000001", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("00000011", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("00000111", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("00001111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        )
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("00011111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
        )
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("00111111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
        )
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("01111111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("11111111", l_encoded)

        bits = bytearray(2)
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("0000000000000000", l_encoded)

        bits = bytearray(2)
        bits[0] = self.__BIT_0
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("0000000000000001", l_encoded)

        bits = bytearray(2)
        bits[0] = self.__BIT_0 | self.__BIT_1
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("0000000000000011", l_encoded)

        bits = bytearray(2)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("0000000000000111", l_encoded)

        bits = bytearray(2)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("0000000000001111", l_encoded)

        bits = bytearray(2)
        bits[0] = (
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        )
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("0000000000011111", l_encoded)

        bits = bytearray(2)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
        )
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("0000000000111111", l_encoded)

        bits = bytearray(2)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
        )
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("0000000001111111", l_encoded)

        bits = bytearray(2)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("0000000011111111", l_encoded)

        bits = bytearray(2)
        bits[1] = self.__BIT_0
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("0000000111111111", l_encoded)

        bits = bytearray(2)
        bits[1] = self.__BIT_0 | self.__BIT_1
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("0000001111111111", l_encoded)

    def testEncodeObject_test18_decomposed(self) -> None:
        bits = bytearray(1)
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("00000000", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("00000001", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("00000011", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("00000111", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("00001111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        )
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("00011111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
        )
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("00111111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
        )
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("01111111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("11111111", l_encoded)

        bits = bytearray(2)
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("0000000000000000", l_encoded)

        bits = bytearray(2)
        bits[0] = self.__BIT_0
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("0000000000000001", l_encoded)

        bits = bytearray(2)
        bits[0] = self.__BIT_0 | self.__BIT_1
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("0000000000000011", l_encoded)

        bits = bytearray(2)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("0000000000000111", l_encoded)

        bits = bytearray(2)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("0000000000001111", l_encoded)

        bits = bytearray(2)
        bits[0] = (
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        )
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("0000000000011111", l_encoded)

        bits = bytearray(2)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
        )
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("0000000000111111", l_encoded)

        bits = bytearray(2)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
        )
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("0000000001111111", l_encoded)

        bits = bytearray(2)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("0000000011111111", l_encoded)

        bits = bytearray(2)
        bits[1] = self.__BIT_0
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("1111111100000001", l_encoded)

    def testEncodeObject_test17_decomposed(self) -> None:
        bits = bytearray(1)
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("00000000", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("00000001", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("00000011", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("00000111", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("00001111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        )
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("00011111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
        )
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("00111111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
        )
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("01111111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("11111111", l_encoded)

        bits = bytearray(2)
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("0000000000000000", l_encoded)

        bits = bytearray(2)
        bits[0] = self.__BIT_0
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("0000000000000001", l_encoded)

        bits = bytearray(2)
        bits[0] = self.__BIT_0 | self.__BIT_1
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("0000000000000011", l_encoded)

        bits = bytearray(2)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("0000000000000111", l_encoded)

        bits = bytearray(2)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("0000000000001111", l_encoded)

        bits = bytearray(2)
        bits[0] = (
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        )
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("0000000000011111", l_encoded)

        bits = bytearray(2)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
        )
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("0000000000111111", l_encoded)

        bits = bytearray(2)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
        )
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("0000000001111111", l_encoded)

        bits = bytearray(2)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("1111111111111111", l_encoded)

    def testEncodeObject_test16_decomposed(self) -> None:
        bits = bytearray(1)
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("00000000", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("00000001", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("00000011", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("00000111", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("00001111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        )
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("00011111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
        )
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("00111111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
        )
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("01111111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("11111111", l_encoded)

        bits = bytearray(2)
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("0000000000000000", l_encoded)

        bits = bytearray(2)
        bits[0] = self.__BIT_0
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("0000000000000001", l_encoded)

        bits = bytearray(2)
        bits[0] = self.__BIT_0 | self.__BIT_1
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("0000000000000011", l_encoded)

        bits = bytearray(2)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("0000000000000111", l_encoded)

        bits = bytearray(2)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("0000000000001111", l_encoded)

        bits = bytearray(2)
        bits[0] = (
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        )
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("0000000000011111", l_encoded)

        bits = bytearray(2)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
        )
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("0000000000111111", l_encoded)

        bits = bytearray(2)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
        )
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("0000000001111111", l_encoded)

    def testEncodeObject_test15_decomposed(self) -> None:
        bits = bytearray(1)
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("00000000", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("00000001", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("00000011", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("00000111", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("00001111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        )
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("00011111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
        )
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("00111111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
        )
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("01111111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("11111111", l_encoded)

        bits = bytearray(2)
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("0000000000000000", l_encoded)

        bits = bytearray(2)
        bits[0] = self.__BIT_0
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("0000000000000001", l_encoded)

        bits = bytearray(2)
        bits[0] = self.__BIT_0 | self.__BIT_1
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("0000000000000011", l_encoded)

        bits = bytearray(2)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("0000000000000111", l_encoded)

        bits = bytearray(2)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("0000000000001111", l_encoded)

        bits = bytearray(2)
        bits[0] = (
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        )
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("0000000000011111", l_encoded)

        bits = bytearray(2)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
        )
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("0000000000111111", l_encoded)

    def testEncodeObject_test14_decomposed(self) -> None:
        bits = bytearray(1)
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("00000000", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("00000001", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("00000011", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("00000111", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("00001111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        )
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("00011111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
        )
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("00111111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
        )
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("01111111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("11111111", l_encoded)

        bits = bytearray(2)
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("0000000000000000", l_encoded)

        bits = bytearray(2)
        bits[0] = self.__BIT_0
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("0000000000000001", l_encoded)

        bits = bytearray(2)
        bits[0] = self.__BIT_0 | self.__BIT_1
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("0000000000000011", l_encoded)

        bits = bytearray(2)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("0000000000000111", l_encoded)

        bits = bytearray(2)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("0000000000001111", l_encoded)

        bits = bytearray(2)
        bits[0] = (
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        )
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("0000000000011111", l_encoded)

    def testEncodeObject_test13_decomposed(self) -> None:
        bits = bytearray(1)
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("00000000", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("00000001", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("00000011", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("00000111", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("00001111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        )
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("00011111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
        )
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("00111111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
        )
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("01111111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("11111111", l_encoded)

        bits = bytearray(2)
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("0000000000000000", l_encoded)

        bits = bytearray(2)
        bits[0] = self.__BIT_0
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("0000000000000001", l_encoded)

        bits = bytearray(2)
        bits[0] = self.__BIT_0 | self.__BIT_1
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("0000000000000011", l_encoded)

        bits = bytearray(2)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("0000000000000111", l_encoded)

        bits = bytearray(2)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("0000000000001111", l_encoded)

    def testEncodeObject_test12_decomposed(self) -> None:
        bits = bytearray(1)
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("00000000", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("00000001", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("00000011", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("00000111", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("00001111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        )
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("00011111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
        )
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("00111111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
        )
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("01111111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("11111111", l_encoded)

        bits = bytearray(2)
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("0000000000000000", l_encoded)

        bits = bytearray(2)
        bits[0] = self.__BIT_0
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("0000000000000001", l_encoded)

        bits = bytearray(2)
        bits[0] = self.__BIT_0 | self.__BIT_1
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("0000000000000011", l_encoded)

        bits = bytearray(2)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("0000000000000111", l_encoded)

    def testEncodeObject_test11_decomposed(self) -> None:
        bits = bytearray(1)
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("00000000", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("00000001", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("00000011", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("00000111", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("00001111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        )
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("00011111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
        )
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("00111111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
        )
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("01111111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("11111111", l_encoded)

        bits = bytearray(2)
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("0000000000000000", l_encoded)

        bits = bytearray(2)
        bits[0] = self.__BIT_0
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("0000000000000001", l_encoded)

        bits = bytearray(2)
        bits[0] = self.__BIT_0 | self.__BIT_1
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("0000000000000011", l_encoded)

    def testEncodeObject_test10_decomposed(self) -> None:
        bits = bytearray(1)
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("00000000", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("00000001", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("00000011", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("00000111", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("00001111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        )
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("00011111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
        )
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("00111111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
        )
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("01111111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("11111111", l_encoded)

        bits = bytearray(2)
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("0000000000000000", l_encoded)

        bits = bytearray(2)
        bits[0] = self.__BIT_0
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("0000000100000000", l_encoded)

    def testEncodeObject_test9_decomposed(self) -> None:
        bits = bytearray(1)
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("00000000", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("00000001", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("00000011", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("00000111", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("00001111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        )
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("00011111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
        )
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("00111111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
        )
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("01111111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("11111111", l_encoded)

        bits = bytearray(2)
        l_encoded = "".join(self.instance.encode1(bits))

    def testEncodeObject_test8_decomposed(self) -> None:
        bits = bytearray(1)
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("00000000", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("00000001", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("00000011", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("00000111", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("00001111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        )
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("00011111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
        )
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("00111111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
        )
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("01111111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("11111111", l_encoded)

    def testEncodeObject_test7_decomposed(self) -> None:
        bits = bytearray(1)
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("00000000", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("00000001", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("00000011", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("00000111", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("00001111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        )
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("00011111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
        )
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("00111111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
        )
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("01111111", l_encoded)

    def testEncodeObject_test6_decomposed(self) -> None:
        bits = bytearray(1)
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("00000000", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("00000001", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("00000011", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("00000111", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("00001111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        )
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("00011111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
        )
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("00111111", l_encoded)

    def testEncodeObject_test5_decomposed(self) -> None:
        bits = bytearray(1)
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("00000000", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("00000001", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("00000011", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("00000111", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("00001111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        )
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("00011111", l_encoded)

    def testEncodeObject_test4_decomposed(self) -> None:
        bits = bytearray(1)
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("00000000", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("00000001", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("00000011", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("00000111", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("00001111", l_encoded)

    def testEncodeObject_test3_decomposed(self) -> None:
        bits = bytearray(1)
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("00000000", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("00000001", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("00000011", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        l_encoded = "".join(self.instance.encode1(bits))
        self.assertEqual("00000111", l_encoded)

    def testEncodeObject_test2_decomposed(self) -> None:
        bits = bytearray(1)  # Create a byte array of size 1
        l_encoded = "".join(self.instance.encode1(bits))  # Encode and convert to string
        self.assertEqual("00000000", l_encoded)  # Assert the encoded value matches

        bits = bytearray(1)  # Reset the byte array
        bits[0] = self.__BIT_0  # Set the first bit
        l_encoded = "".join(self.instance.encode1(bits))  # Encode and convert to string
        self.assertEqual("00000001", l_encoded)  # Assert the encoded value matches

        bits = bytearray(1)  # Reset the byte array
        bits[0] = self.__BIT_0 | self.__BIT_1  # Set the first and second bits
        l_encoded = "".join(self.instance.encode1(bits))  # Encode and convert to string
        self.assertEqual("00000011", l_encoded)  # Assert the encoded value matches

    def testEncodeObject_test1_decomposed(self) -> None:
        bits = bytearray(1)  # Create a byte array of size 1
        l_encoded = "".join(
            self.instance.encode1(bits)
        )  # Encode the byte array and join the resulting characters into a string
        self.assertEqual(
            "00000000", l_encoded
        )  # Assert that the encoded string matches the expected value

        bits = bytearray(1)  # Create a new byte array of size 1
        bits[0] = self.__BIT_0  # Set the first byte to BIT_0
        l_encoded = "".join(
            self.instance.encode1(bits)
        )  # Encode the updated byte array and join the resulting characters into a string

    def testEncodeObject_test0_decomposed(self) -> None:
        bits = bytearray(1)  # Equivalent to `new byte[1]` in Java
        l_encoded = str(
            self.instance.encode1(bits)
        )  # Cast the result of encode1 to a string

    def testEncodeObjectException_test1_decomposed(self) -> None:
        with pytest.raises(EncoderException):
            self.instance.encode1("")

    def testEncodeObjectException_test0_decomposed(self) -> None:
        try:
            self.instance.encode1("")
        except EncoderException:
            return

    def testEncodeObjectNull_test0_decomposed(self) -> None:
        obj = bytes()  # Equivalent to new byte[0] in Java
        result = self.instance.encode1(obj)  # Call the encode1 method
        self.assertEqual(0, len(result))  # Assert that the length of the result is 0

    def testToAsciiString_test26_decomposed(self) -> None:
        bits = [0]
        l_encoded = BinaryCodec.toAsciiString(bits)
        self.assertEqual("00000000", l_encoded)

        bits = [self.__BIT_0]
        l_encoded = BinaryCodec.toAsciiString(bits)
        self.assertEqual("00000001", l_encoded)

        bits = [self.__BIT_0 | self.__BIT_1]
        l_encoded = BinaryCodec.toAsciiString(bits)
        self.assertEqual("00000011", l_encoded)

        bits = [self.__BIT_0 | self.__BIT_1 | self.__BIT_2]
        l_encoded = BinaryCodec.toAsciiString(bits)
        self.assertEqual("00000111", l_encoded)

        bits = [self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3]
        l_encoded = BinaryCodec.toAsciiString(bits)
        self.assertEqual("00001111", l_encoded)

        bits = [
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        ]
        l_encoded = BinaryCodec.toAsciiString(bits)
        self.assertEqual("00011111", l_encoded)

        bits = [
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
        ]
        l_encoded = BinaryCodec.toAsciiString(bits)
        self.assertEqual("00111111", l_encoded)

        bits = [
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
        ]
        l_encoded = BinaryCodec.toAsciiString(bits)
        self.assertEqual("01111111", l_encoded)

        bits = [
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        ]
        l_encoded = BinaryCodec.toAsciiString(bits)
        self.assertEqual("11111111", l_encoded)

        bits = [0, 0]
        l_encoded = BinaryCodec.toAsciiString(bits)
        self.assertEqual("0000000000000000", l_encoded)

        bits = [self.__BIT_0, 0]
        l_encoded = BinaryCodec.toAsciiString(bits)
        self.assertEqual("0000000000000001", l_encoded)

        bits = [self.__BIT_0 | self.__BIT_1, 0]
        l_encoded = BinaryCodec.toAsciiString(bits)
        self.assertEqual("0000000000000011", l_encoded)

        bits = [self.__BIT_0 | self.__BIT_1 | self.__BIT_2, 0]
        l_encoded = BinaryCodec.toAsciiString(bits)
        self.assertEqual("0000000000000111", l_encoded)

        bits = [self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3, 0]
        l_encoded = BinaryCodec.toAsciiString(bits)
        self.assertEqual("0000000000001111", l_encoded)

        bits = [
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4,
            0,
        ]
        l_encoded = BinaryCodec.toAsciiString(bits)
        self.assertEqual("0000000000011111", l_encoded)

        bits = [
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5,
            0,
        ]
        l_encoded = BinaryCodec.toAsciiString(bits)
        self.assertEqual("0000000000111111", l_encoded)

        bits = [
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6,
            0,
        ]
        l_encoded = BinaryCodec.toAsciiString(bits)
        self.assertEqual("0000000001111111", l_encoded)

        bits = [
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7,
            0,
        ]
        l_encoded = BinaryCodec.toAsciiString(bits)
        self.assertEqual("0000000011111111", l_encoded)

        bits = [
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7,
            self.__BIT_0,
        ]
        l_encoded = BinaryCodec.toAsciiString(bits)
        self.assertEqual("0000000111111111", l_encoded)

        bits = [
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7,
            self.__BIT_0 | self.__BIT_1,
        ]
        l_encoded = BinaryCodec.toAsciiString(bits)
        self.assertEqual("0000001111111111", l_encoded)

        bits = [
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7,
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2,
        ]
        l_encoded = BinaryCodec.toAsciiString(bits)
        self.assertEqual("0000011111111111", l_encoded)

        bits = [
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7,
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3,
        ]
        l_encoded = BinaryCodec.toAsciiString(bits)
        self.assertEqual("0000111111111111", l_encoded)

        bits = [
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7,
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4,
        ]
        l_encoded = BinaryCodec.toAsciiString(bits)
        self.assertEqual("0001111111111111", l_encoded)

        bits = [
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7,
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5,
        ]
        l_encoded = BinaryCodec.toAsciiString(bits)
        self.assertEqual("0011111111111111", l_encoded)

        bits = [
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7,
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6,
        ]
        l_encoded = BinaryCodec.toAsciiString(bits)
        self.assertEqual("0111111111111111", l_encoded)

        bits = [
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7,
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7,
        ]
        l_encoded = BinaryCodec.toAsciiString(bits)
        self.assertEqual("1111111111111111", l_encoded)

    def testToAsciiString_test25_decomposed(self) -> None:
        bits = [0]
        l_encoded = BinaryCodec.toAsciiString(bits)
        self.assertEqual("00000000", l_encoded)

        bits = [self.__BIT_0]
        l_encoded = BinaryCodec.toAsciiString(bits)
        self.assertEqual("00000001", l_encoded)

        bits = [self.__BIT_0 | self.__BIT_1]
        l_encoded = BinaryCodec.toAsciiString(bits)
        self.assertEqual("00000011", l_encoded)

        bits = [self.__BIT_0 | self.__BIT_1 | self.__BIT_2]
        l_encoded = BinaryCodec.toAsciiString(bits)
        self.assertEqual("00000111", l_encoded)

        bits = [self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3]
        l_encoded = BinaryCodec.toAsciiString(bits)
        self.assertEqual("00001111", l_encoded)

        bits = [
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        ]
        l_encoded = BinaryCodec.toAsciiString(bits)
        self.assertEqual("00011111", l_encoded)

        bits = [
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
        ]
        l_encoded = BinaryCodec.toAsciiString(bits)
        self.assertEqual("00111111", l_encoded)

        bits = [
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
        ]
        l_encoded = BinaryCodec.toAsciiString(bits)
        self.assertEqual("01111111", l_encoded)

        bits = [
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        ]
        l_encoded = BinaryCodec.toAsciiString(bits)
        self.assertEqual("11111111", l_encoded)

        bits = [0, 0]
        l_encoded = BinaryCodec.toAsciiString(bits)
        self.assertEqual("0000000000000000", l_encoded)

        bits = [self.__BIT_0, 0]
        l_encoded = BinaryCodec.toAsciiString(bits)
        self.assertEqual("0000000000000001", l_encoded)

        bits = [self.__BIT_0 | self.__BIT_1, 0]
        l_encoded = BinaryCodec.toAsciiString(bits)
        self.assertEqual("0000000000000011", l_encoded)

        bits = [self.__BIT_0 | self.__BIT_1 | self.__BIT_2, 0]
        l_encoded = BinaryCodec.toAsciiString(bits)
        self.assertEqual("0000000000000111", l_encoded)

        bits = [self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3, 0]
        l_encoded = BinaryCodec.toAsciiString(bits)
        self.assertEqual("0000000000001111", l_encoded)

        bits = [
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4,
            0,
        ]
        l_encoded = BinaryCodec.toAsciiString(bits)
        self.assertEqual("0000000000011111", l_encoded)

        bits = [
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5,
            0,
        ]
        l_encoded = BinaryCodec.toAsciiString(bits)
        self.assertEqual("0000000000111111", l_encoded)

        bits = [
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6,
            0,
        ]
        l_encoded = BinaryCodec.toAsciiString(bits)
        self.assertEqual("0000000001111111", l_encoded)

        bits = [
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7,
            0,
        ]
        l_encoded = BinaryCodec.toAsciiString(bits)
        self.assertEqual("0000000011111111", l_encoded)

        bits = [
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7,
            self.__BIT_0,
        ]
        l_encoded = BinaryCodec.toAsciiString(bits)
        self.assertEqual("0000000111111111", l_encoded)

        bits = [
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7,
            self.__BIT_0 | self.__BIT_1,
        ]
        l_encoded = BinaryCodec.toAsciiString(bits)
        self.assertEqual("0000001111111111", l_encoded)

        bits = [
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7,
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2,
        ]
        l_encoded = BinaryCodec.toAsciiString(bits)
        self.assertEqual("0000011111111111", l_encoded)

        bits = [
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7,
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3,
        ]
        l_encoded = BinaryCodec.toAsciiString(bits)
        self.assertEqual("0000111111111111", l_encoded)

        bits = [
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7,
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4,
        ]
        l_encoded = BinaryCodec.toAsciiString(bits)
        self.assertEqual("0001111111111111", l_encoded)

        bits = [
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7,
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5,
        ]
        l_encoded = BinaryCodec.toAsciiString(bits)
        self.assertEqual("0011111111111111", l_encoded)

        bits = [
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7,
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6,
        ]
        l_encoded = BinaryCodec.toAsciiString(bits)
        self.assertEqual("0111111111111111", l_encoded)

        bits = [
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7,
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7,
        ]
        l_encoded = BinaryCodec.toAsciiString(bits)
        self.assertEqual("1111111111111111", l_encoded)

    def testToAsciiString_test24_decomposed(self) -> None:
        bits = [0]
        l_encoded = BinaryCodec.toAsciiString(bits)
        self.assertEqual("00000000", l_encoded)

        bits = [self.__BIT_0]
        l_encoded = BinaryCodec.toAsciiString(bits)
        self.assertEqual("00000001", l_encoded)

        bits = [self.__BIT_0 | self.__BIT_1]
        l_encoded = BinaryCodec.toAsciiString(bits)
        self.assertEqual("00000011", l_encoded)

        bits = [self.__BIT_0 | self.__BIT_1 | self.__BIT_2]
        l_encoded = BinaryCodec.toAsciiString(bits)
        self.assertEqual("00000111", l_encoded)

        bits = [self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3]
        l_encoded = BinaryCodec.toAsciiString(bits)
        self.assertEqual("00001111", l_encoded)

        bits = [
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        ]
        l_encoded = BinaryCodec.toAsciiString(bits)
        self.assertEqual("00011111", l_encoded)

        bits = [
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
        ]
        l_encoded = BinaryCodec.toAsciiString(bits)
        self.assertEqual("00111111", l_encoded)

        bits = [
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
        ]
        l_encoded = BinaryCodec.toAsciiString(bits)
        self.assertEqual("01111111", l_encoded)

        bits = [
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        ]
        l_encoded = BinaryCodec.toAsciiString(bits)
        self.assertEqual("11111111", l_encoded)

        bits = [0, 0]
        l_encoded = BinaryCodec.toAsciiString(bits)
        self.assertEqual("0000000000000000", l_encoded)

        bits = [self.__BIT_0, 0]
        l_encoded = BinaryCodec.toAsciiString(bits)
        self.assertEqual("0000000000000001", l_encoded)

        bits = [self.__BIT_0 | self.__BIT_1, 0]
        l_encoded = BinaryCodec.toAsciiString(bits)
        self.assertEqual("0000000000000011", l_encoded)

        bits = [self.__BIT_0 | self.__BIT_1 | self.__BIT_2, 0]
        l_encoded = BinaryCodec.toAsciiString(bits)
        self.assertEqual("0000000000000111", l_encoded)

        bits = [self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3, 0]
        l_encoded = BinaryCodec.toAsciiString(bits)
        self.assertEqual("0000000000001111", l_encoded)

        bits = [
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4,
            0,
        ]
        l_encoded = BinaryCodec.toAsciiString(bits)
        self.assertEqual("0000000000011111", l_encoded)

        bits = [
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5,
            0,
        ]
        l_encoded = BinaryCodec.toAsciiString(bits)
        self.assertEqual("0000000000111111", l_encoded)

        bits = [
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6,
            0,
        ]
        l_encoded = BinaryCodec.toAsciiString(bits)
        self.assertEqual("0000000001111111", l_encoded)

        bits = [
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7,
            0,
        ]
        l_encoded = BinaryCodec.toAsciiString(bits)
        self.assertEqual("0000000011111111", l_encoded)

        bits = [
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7,
            self.__BIT_0,
        ]
        l_encoded = BinaryCodec.toAsciiString(bits)
        self.assertEqual("0000000111111111", l_encoded)

        bits = [
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7,
            self.__BIT_0 | self.__BIT_1,
        ]
        l_encoded = BinaryCodec.toAsciiString(bits)
        self.assertEqual("0000001111111111", l_encoded)

        bits = [
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7,
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2,
        ]
        l_encoded = BinaryCodec.toAsciiString(bits)
        self.assertEqual("0000011111111111", l_encoded)

        bits = [
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7,
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3,
        ]
        l_encoded = BinaryCodec.toAsciiString(bits)
        self.assertEqual("0000111111111111", l_encoded)

        bits = [
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7,
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4,
        ]
        l_encoded = BinaryCodec.toAsciiString(bits)
        self.assertEqual("0001111111111111", l_encoded)

        bits = [
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7,
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5,
        ]
        l_encoded = BinaryCodec.toAsciiString(bits)
        self.assertEqual("0011111111111111", l_encoded)

        bits = [
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7,
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6,
        ]
        l_encoded = BinaryCodec.toAsciiString(bits)
        self.assertEqual("0111111111111111", l_encoded)

    def testToAsciiString_test23_decomposed(self) -> None:
        bits = [0]
        l_encoded = BinaryCodec.toAsciiString(bits)
        self.assertEqual("00000000", l_encoded)

        bits = [self.__BIT_0]
        l_encoded = BinaryCodec.toAsciiString(bits)
        self.assertEqual("00000001", l_encoded)

        bits = [self.__BIT_0 | self.__BIT_1]
        l_encoded = BinaryCodec.toAsciiString(bits)
        self.assertEqual("00000011", l_encoded)

        bits = [self.__BIT_0 | self.__BIT_1 | self.__BIT_2]
        l_encoded = BinaryCodec.toAsciiString(bits)
        self.assertEqual("00000111", l_encoded)

        bits = [self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3]
        l_encoded = BinaryCodec.toAsciiString(bits)
        self.assertEqual("00001111", l_encoded)

        bits = [
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        ]
        l_encoded = BinaryCodec.toAsciiString(bits)
        self.assertEqual("00011111", l_encoded)

        bits = [
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
        ]
        l_encoded = BinaryCodec.toAsciiString(bits)
        self.assertEqual("00111111", l_encoded)

        bits = [
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
        ]
        l_encoded = BinaryCodec.toAsciiString(bits)
        self.assertEqual("01111111", l_encoded)

        bits = [
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        ]
        l_encoded = BinaryCodec.toAsciiString(bits)
        self.assertEqual("11111111", l_encoded)

        bits = [0, 0]
        l_encoded = BinaryCodec.toAsciiString(bits)
        self.assertEqual("0000000000000000", l_encoded)

        bits = [self.__BIT_0, 0]
        l_encoded = BinaryCodec.toAsciiString(bits)
        self.assertEqual("0000000000000001", l_encoded)

        bits = [self.__BIT_0 | self.__BIT_1, 0]
        l_encoded = BinaryCodec.toAsciiString(bits)
        self.assertEqual("0000000000000011", l_encoded)

        bits = [self.__BIT_0 | self.__BIT_1 | self.__BIT_2, 0]
        l_encoded = BinaryCodec.toAsciiString(bits)
        self.assertEqual("0000000000000111", l_encoded)

        bits = [self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3, 0]
        l_encoded = BinaryCodec.toAsciiString(bits)
        self.assertEqual("0000000000001111", l_encoded)

        bits = [
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4,
            0,
        ]
        l_encoded = BinaryCodec.toAsciiString(bits)
        self.assertEqual("0000000000011111", l_encoded)

        bits = [
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5,
            0,
        ]
        l_encoded = BinaryCodec.toAsciiString(bits)
        self.assertEqual("0000000000111111", l_encoded)

        bits = [
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6,
            0,
        ]
        l_encoded = BinaryCodec.toAsciiString(bits)
        self.assertEqual("0000000001111111", l_encoded)

        bits = [
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7,
            0,
        ]
        l_encoded = BinaryCodec.toAsciiString(bits)
        self.assertEqual("0000000011111111", l_encoded)

        bits = [
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7,
            self.__BIT_0,
        ]
        l_encoded = BinaryCodec.toAsciiString(bits)
        self.assertEqual("0000000111111111", l_encoded)

        bits = [
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7,
            self.__BIT_0 | self.__BIT_1,
        ]
        l_encoded = BinaryCodec.toAsciiString(bits)
        self.assertEqual("0000001111111111", l_encoded)

        bits = [
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7,
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2,
        ]
        l_encoded = BinaryCodec.toAsciiString(bits)
        self.assertEqual("0000011111111111", l_encoded)

        bits = [
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7,
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3,
        ]
        l_encoded = BinaryCodec.toAsciiString(bits)
        self.assertEqual("0000111111111111", l_encoded)

        bits = [
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7,
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4,
        ]
        l_encoded = BinaryCodec.toAsciiString(bits)
        self.assertEqual("0001111111111111", l_encoded)

        bits = [
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7,
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5,
        ]
        l_encoded = BinaryCodec.toAsciiString(bits)
        self.assertEqual("0011111111111111", l_encoded)

    def testToAsciiString_test22_decomposed(self) -> None:
        bits = [0]
        l_encoded = BinaryCodec.toAsciiString(bits)
        self.assertEqual("00000000", l_encoded)

        bits = [self.__BIT_0]
        l_encoded = BinaryCodec.toAsciiString(bits)
        self.assertEqual("00000001", l_encoded)

        bits = [self.__BIT_0 | self.__BIT_1]
        l_encoded = BinaryCodec.toAsciiString(bits)
        self.assertEqual("00000011", l_encoded)

        bits = [self.__BIT_0 | self.__BIT_1 | self.__BIT_2]
        l_encoded = BinaryCodec.toAsciiString(bits)
        self.assertEqual("00000111", l_encoded)

        bits = [self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3]
        l_encoded = BinaryCodec.toAsciiString(bits)
        self.assertEqual("00001111", l_encoded)

        bits = [
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        ]
        l_encoded = BinaryCodec.toAsciiString(bits)
        self.assertEqual("00011111", l_encoded)

        bits = [
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
        ]
        l_encoded = BinaryCodec.toAsciiString(bits)
        self.assertEqual("00111111", l_encoded)

        bits = [
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
        ]
        l_encoded = BinaryCodec.toAsciiString(bits)
        self.assertEqual("01111111", l_encoded)

        bits = [
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        ]
        l_encoded = BinaryCodec.toAsciiString(bits)
        self.assertEqual("11111111", l_encoded)

        bits = [0, 0]
        l_encoded = BinaryCodec.toAsciiString(bits)
        self.assertEqual("0000000000000000", l_encoded)

        bits = [self.__BIT_0, 0]
        l_encoded = BinaryCodec.toAsciiString(bits)
        self.assertEqual("0000000000000001", l_encoded)

        bits = [self.__BIT_0 | self.__BIT_1, 0]
        l_encoded = BinaryCodec.toAsciiString(bits)
        self.assertEqual("0000000000000011", l_encoded)

        bits = [self.__BIT_0 | self.__BIT_1 | self.__BIT_2, 0]
        l_encoded = BinaryCodec.toAsciiString(bits)
        self.assertEqual("0000000000000111", l_encoded)

        bits = [self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3, 0]
        l_encoded = BinaryCodec.toAsciiString(bits)
        self.assertEqual("0000000000001111", l_encoded)

        bits = [
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4,
            0,
        ]
        l_encoded = BinaryCodec.toAsciiString(bits)
        self.assertEqual("0000000000011111", l_encoded)

        bits = [
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5,
            0,
        ]
        l_encoded = BinaryCodec.toAsciiString(bits)
        self.assertEqual("0000000000111111", l_encoded)

        bits = [
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6,
            0,
        ]
        l_encoded = BinaryCodec.toAsciiString(bits)
        self.assertEqual("0000000001111111", l_encoded)

        bits = [
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7,
            0,
        ]
        l_encoded = BinaryCodec.toAsciiString(bits)
        self.assertEqual("0000000011111111", l_encoded)

        bits = [
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7,
            self.__BIT_0,
        ]
        l_encoded = BinaryCodec.toAsciiString(bits)
        self.assertEqual("0000000111111111", l_encoded)

        bits = [
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7,
            self.__BIT_0 | self.__BIT_1,
        ]
        l_encoded = BinaryCodec.toAsciiString(bits)
        self.assertEqual("0000001111111111", l_encoded)

        bits = [
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7,
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2,
        ]
        l_encoded = BinaryCodec.toAsciiString(bits)
        self.assertEqual("0000011111111111", l_encoded)

        bits = [
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7,
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3,
        ]
        l_encoded = BinaryCodec.toAsciiString(bits)
        self.assertEqual("0000111111111111", l_encoded)

        bits = [
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7,
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4,
        ]
        l_encoded = BinaryCodec.toAsciiString(bits)
        self.assertEqual("0001111111111111", l_encoded)

    def testToAsciiString_test21_decomposed(self) -> None:
        bits = [0]
        l_encoded = BinaryCodec.toAsciiString(bits)
        self.assertEqual("00000000", l_encoded)

        bits = [self.__BIT_0]
        l_encoded = BinaryCodec.toAsciiString(bits)
        self.assertEqual("00000001", l_encoded)

        bits = [self.__BIT_0 | self.__BIT_1]
        l_encoded = BinaryCodec.toAsciiString(bits)
        self.assertEqual("00000011", l_encoded)

        bits = [self.__BIT_0 | self.__BIT_1 | self.__BIT_2]
        l_encoded = BinaryCodec.toAsciiString(bits)
        self.assertEqual("00000111", l_encoded)

        bits = [self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3]
        l_encoded = BinaryCodec.toAsciiString(bits)
        self.assertEqual("00001111", l_encoded)

        bits = [
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        ]
        l_encoded = BinaryCodec.toAsciiString(bits)
        self.assertEqual("00011111", l_encoded)

        bits = [
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
        ]
        l_encoded = BinaryCodec.toAsciiString(bits)
        self.assertEqual("00111111", l_encoded)

        bits = [
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
        ]
        l_encoded = BinaryCodec.toAsciiString(bits)
        self.assertEqual("01111111", l_encoded)

        bits = [
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        ]
        l_encoded = BinaryCodec.toAsciiString(bits)
        self.assertEqual("11111111", l_encoded)

        bits = [0, 0]
        l_encoded = BinaryCodec.toAsciiString(bits)
        self.assertEqual("0000000000000000", l_encoded)

        bits = [self.__BIT_0, 0]
        l_encoded = BinaryCodec.toAsciiString(bits)
        self.assertEqual("0000000000000001", l_encoded)

        bits = [self.__BIT_0 | self.__BIT_1, 0]
        l_encoded = BinaryCodec.toAsciiString(bits)
        self.assertEqual("0000000000000011", l_encoded)

        bits = [self.__BIT_0 | self.__BIT_1 | self.__BIT_2, 0]
        l_encoded = BinaryCodec.toAsciiString(bits)
        self.assertEqual("0000000000000111", l_encoded)

        bits = [self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3, 0]
        l_encoded = BinaryCodec.toAsciiString(bits)
        self.assertEqual("0000000000001111", l_encoded)

        bits = [
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4,
            0,
        ]
        l_encoded = BinaryCodec.toAsciiString(bits)
        self.assertEqual("0000000000011111", l_encoded)

        bits = [
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5,
            0,
        ]
        l_encoded = BinaryCodec.toAsciiString(bits)
        self.assertEqual("0000000000111111", l_encoded)

        bits = [
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6,
            0,
        ]
        l_encoded = BinaryCodec.toAsciiString(bits)
        self.assertEqual("0000000001111111", l_encoded)

        bits = [
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7,
            0,
        ]
        l_encoded = BinaryCodec.toAsciiString(bits)
        self.assertEqual("0000000011111111", l_encoded)

        bits = [
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7,
            self.__BIT_0,
        ]
        l_encoded = BinaryCodec.toAsciiString(bits)
        self.assertEqual("0000000111111111", l_encoded)

        bits = [
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7,
            self.__BIT_0 | self.__BIT_1,
        ]
        l_encoded = BinaryCodec.toAsciiString(bits)
        self.assertEqual("0000001111111111", l_encoded)

        bits = [
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7,
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2,
        ]
        l_encoded = BinaryCodec.toAsciiString(bits)
        self.assertEqual("0000011111111111", l_encoded)

        bits = [
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7,
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3,
        ]
        l_encoded = BinaryCodec.toAsciiString(bits)
        self.assertEqual("0000111111111111", l_encoded)

    def testToAsciiString_test20_decomposed(self) -> None:
        bits = [0]
        l_encoded = self.instance.toAsciiString(bits)
        self.assertEqual("00000000", l_encoded)

        bits = [self.__BIT_0]
        l_encoded = self.instance.toAsciiString(bits)
        self.assertEqual("00000001", l_encoded)

        bits = [self.__BIT_0 | self.__BIT_1]
        l_encoded = self.instance.toAsciiString(bits)
        self.assertEqual("00000011", l_encoded)

        bits = [self.__BIT_0 | self.__BIT_1 | self.__BIT_2]
        l_encoded = self.instance.toAsciiString(bits)
        self.assertEqual("00000111", l_encoded)

        bits = [self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3]
        l_encoded = self.instance.toAsciiString(bits)
        self.assertEqual("00001111", l_encoded)

        bits = [
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        ]
        l_encoded = self.instance.toAsciiString(bits)
        self.assertEqual("00011111", l_encoded)

        bits = [
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
        ]
        l_encoded = self.instance.toAsciiString(bits)
        self.assertEqual("00111111", l_encoded)

        bits = [
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
        ]
        l_encoded = self.instance.toAsciiString(bits)
        self.assertEqual("01111111", l_encoded)

        bits = [
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        ]
        l_encoded = self.instance.toAsciiString(bits)
        self.assertEqual("11111111", l_encoded)

        bits = [0, 0]
        l_encoded = self.instance.toAsciiString(bits)
        self.assertEqual("0000000000000000", l_encoded)

        bits = [self.__BIT_0, 0]
        l_encoded = self.instance.toAsciiString(bits)
        self.assertEqual("0000000000000001", l_encoded)

        bits = [self.__BIT_0 | self.__BIT_1, 0]
        l_encoded = self.instance.toAsciiString(bits)
        self.assertEqual("0000000000000011", l_encoded)

        bits = [self.__BIT_0 | self.__BIT_1 | self.__BIT_2, 0]
        l_encoded = self.instance.toAsciiString(bits)
        self.assertEqual("0000000000000111", l_encoded)

        bits = [self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3, 0]
        l_encoded = self.instance.toAsciiString(bits)
        self.assertEqual("0000000000001111", l_encoded)

        bits = [
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4,
            0,
        ]
        l_encoded = self.instance.toAsciiString(bits)
        self.assertEqual("0000000000011111", l_encoded)

        bits = [
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5,
            0,
        ]
        l_encoded = self.instance.toAsciiString(bits)
        self.assertEqual("0000000000111111", l_encoded)

        bits = [
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6,
            0,
        ]
        l_encoded = self.instance.toAsciiString(bits)
        self.assertEqual("0000000001111111", l_encoded)

        bits = [
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7,
            0,
        ]
        l_encoded = self.instance.toAsciiString(bits)
        self.assertEqual("0000000011111111", l_encoded)

        bits = [
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7,
            self.__BIT_0,
        ]
        l_encoded = self.instance.toAsciiString(bits)
        self.assertEqual("0000000111111111", l_encoded)

        bits = [
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7,
            self.__BIT_0 | self.__BIT_1,
        ]
        l_encoded = self.instance.toAsciiString(bits)
        self.assertEqual("0000001111111111", l_encoded)

        bits = [
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7,
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2,
        ]
        l_encoded = self.instance.toAsciiString(bits)
        self.assertEqual("0000011111111111", l_encoded)

    def testToAsciiString_test19_decomposed(self) -> None:
        bits = [0]
        l_encoded = self.instance.toAsciiString(bits)
        self.assertEqual("00000000", l_encoded)

        bits = [self.__BIT_0]
        l_encoded = self.instance.toAsciiString(bits)
        self.assertEqual("00000001", l_encoded)

        bits = [self.__BIT_0 | self.__BIT_1]
        l_encoded = self.instance.toAsciiString(bits)
        self.assertEqual("00000011", l_encoded)

        bits = [self.__BIT_0 | self.__BIT_1 | self.__BIT_2]
        l_encoded = self.instance.toAsciiString(bits)
        self.assertEqual("00000111", l_encoded)

        bits = [self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3]
        l_encoded = self.instance.toAsciiString(bits)
        self.assertEqual("00001111", l_encoded)

        bits = [
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        ]
        l_encoded = self.instance.toAsciiString(bits)
        self.assertEqual("00011111", l_encoded)

        bits = [
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
        ]
        l_encoded = self.instance.toAsciiString(bits)
        self.assertEqual("00111111", l_encoded)

        bits = [
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
        ]
        l_encoded = self.instance.toAsciiString(bits)
        self.assertEqual("01111111", l_encoded)

        bits = [
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        ]
        l_encoded = self.instance.toAsciiString(bits)
        self.assertEqual("11111111", l_encoded)

        bits = [0, 0]
        l_encoded = self.instance.toAsciiString(bits)
        self.assertEqual("0000000000000000", l_encoded)

        bits = [self.__BIT_0, 0]
        l_encoded = self.instance.toAsciiString(bits)
        self.assertEqual("0000000000000001", l_encoded)

        bits = [self.__BIT_0 | self.__BIT_1, 0]
        l_encoded = self.instance.toAsciiString(bits)
        self.assertEqual("0000000000000011", l_encoded)

        bits = [self.__BIT_0 | self.__BIT_1 | self.__BIT_2, 0]
        l_encoded = self.instance.toAsciiString(bits)
        self.assertEqual("0000000000000111", l_encoded)

        bits = [self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3, 0]
        l_encoded = self.instance.toAsciiString(bits)
        self.assertEqual("0000000000001111", l_encoded)

        bits = [
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4,
            0,
        ]
        l_encoded = self.instance.toAsciiString(bits)
        self.assertEqual("0000000000011111", l_encoded)

        bits = [
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5,
            0,
        ]
        l_encoded = self.instance.toAsciiString(bits)
        self.assertEqual("0000000000111111", l_encoded)

        bits = [
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6,
            0,
        ]
        l_encoded = self.instance.toAsciiString(bits)
        self.assertEqual("0000000001111111", l_encoded)

        bits = [
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7,
            0,
        ]
        l_encoded = self.instance.toAsciiString(bits)
        self.assertEqual("0000000011111111", l_encoded)

        bits = [
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7,
            self.__BIT_0,
        ]
        l_encoded = self.instance.toAsciiString(bits)
        self.assertEqual("0000000111111111", l_encoded)

        bits = [
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7,
            self.__BIT_0 | self.__BIT_1,
        ]
        l_encoded = self.instance.toAsciiString(bits)
        self.assertEqual("0000001111111111", l_encoded)

    def testToAsciiString_test18_decomposed(self) -> None:
        bits = [0]
        l_encoded = BinaryCodec.toAsciiString(bits)
        self.assertEqual("00000000", l_encoded)

        bits = [self.__BIT_0]
        l_encoded = BinaryCodec.toAsciiString(bits)
        self.assertEqual("00000001", l_encoded)

        bits = [self.__BIT_0 | self.__BIT_1]
        l_encoded = BinaryCodec.toAsciiString(bits)
        self.assertEqual("00000011", l_encoded)

        bits = [self.__BIT_0 | self.__BIT_1 | self.__BIT_2]
        l_encoded = BinaryCodec.toAsciiString(bits)
        self.assertEqual("00000111", l_encoded)

        bits = [self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3]
        l_encoded = BinaryCodec.toAsciiString(bits)
        self.assertEqual("00001111", l_encoded)

        bits = [
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        ]
        l_encoded = BinaryCodec.toAsciiString(bits)
        self.assertEqual("00011111", l_encoded)

        bits = [
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
        ]
        l_encoded = BinaryCodec.toAsciiString(bits)
        self.assertEqual("00111111", l_encoded)

        bits = [
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
        ]
        l_encoded = BinaryCodec.toAsciiString(bits)
        self.assertEqual("01111111", l_encoded)

        bits = [
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        ]
        l_encoded = BinaryCodec.toAsciiString(bits)
        self.assertEqual("11111111", l_encoded)

        bits = [0, 0]
        l_encoded = BinaryCodec.toAsciiString(bits)
        self.assertEqual("0000000000000000", l_encoded)

        bits = [self.__BIT_0, 0]
        l_encoded = BinaryCodec.toAsciiString(bits)
        self.assertEqual("0000000000000001", l_encoded)

        bits = [self.__BIT_0 | self.__BIT_1, 0]
        l_encoded = BinaryCodec.toAsciiString(bits)
        self.assertEqual("0000000000000011", l_encoded)

        bits = [self.__BIT_0 | self.__BIT_1 | self.__BIT_2, 0]
        l_encoded = BinaryCodec.toAsciiString(bits)
        self.assertEqual("0000000000000111", l_encoded)

        bits = [self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3, 0]
        l_encoded = BinaryCodec.toAsciiString(bits)
        self.assertEqual("0000000000001111", l_encoded)

        bits = [
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4,
            0,
        ]
        l_encoded = BinaryCodec.toAsciiString(bits)
        self.assertEqual("0000000000011111", l_encoded)

        bits = [
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5,
            0,
        ]
        l_encoded = BinaryCodec.toAsciiString(bits)
        self.assertEqual("0000000000111111", l_encoded)

        bits = [
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6,
            0,
        ]
        l_encoded = BinaryCodec.toAsciiString(bits)
        self.assertEqual("0000000001111111", l_encoded)

        bits = [
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7,
            0,
        ]
        l_encoded = BinaryCodec.toAsciiString(bits)
        self.assertEqual("0000000011111111", l_encoded)

        bits = [
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7,
            self.__BIT_0,
        ]
        l_encoded = BinaryCodec.toAsciiString(bits)
        self.assertEqual("000000001111111100000001", l_encoded)

    def testToAsciiString_test17_decomposed(self) -> None:
        bits = [0]
        l_encoded = self.instance.toAsciiString(bits)
        self.assertEqual("00000000", l_encoded)

        bits = [self.__BIT_0]
        l_encoded = self.instance.toAsciiString(bits)
        self.assertEqual("00000001", l_encoded)

        bits = [self.__BIT_0 | self.__BIT_1]
        l_encoded = self.instance.toAsciiString(bits)
        self.assertEqual("00000011", l_encoded)

        bits = [self.__BIT_0 | self.__BIT_1 | self.__BIT_2]
        l_encoded = self.instance.toAsciiString(bits)
        self.assertEqual("00000111", l_encoded)

        bits = [self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3]
        l_encoded = self.instance.toAsciiString(bits)
        self.assertEqual("00001111", l_encoded)

        bits = [
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        ]
        l_encoded = self.instance.toAsciiString(bits)
        self.assertEqual("00011111", l_encoded)

        bits = [
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
        ]
        l_encoded = self.instance.toAsciiString(bits)
        self.assertEqual("00111111", l_encoded)

        bits = [
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
        ]
        l_encoded = self.instance.toAsciiString(bits)
        self.assertEqual("01111111", l_encoded)

        bits = [
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        ]
        l_encoded = self.instance.toAsciiString(bits)
        self.assertEqual("11111111", l_encoded)

        bits = [0, 0]
        l_encoded = self.instance.toAsciiString(bits)
        self.assertEqual("0000000000000000", l_encoded)

        bits = [self.__BIT_0, 0]
        l_encoded = self.instance.toAsciiString(bits)
        self.assertEqual("0000000000000001", l_encoded)

        bits = [self.__BIT_0 | self.__BIT_1, 0]
        l_encoded = self.instance.toAsciiString(bits)
        self.assertEqual("0000000000000011", l_encoded)

        bits = [self.__BIT_0 | self.__BIT_1 | self.__BIT_2, 0]
        l_encoded = self.instance.toAsciiString(bits)
        self.assertEqual("0000000000000111", l_encoded)

        bits = [self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3, 0]
        l_encoded = self.instance.toAsciiString(bits)
        self.assertEqual("0000000000001111", l_encoded)

        bits = [
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4,
            0,
        ]
        l_encoded = self.instance.toAsciiString(bits)
        self.assertEqual("0000000000011111", l_encoded)

        bits = [
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5,
            0,
        ]
        l_encoded = self.instance.toAsciiString(bits)
        self.assertEqual("0000000000111111", l_encoded)

        bits = [
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6,
            0,
        ]
        l_encoded = self.instance.toAsciiString(bits)
        self.assertEqual("0000000001111111", l_encoded)

        bits = [
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7,
            0,
        ]
        l_encoded = self.instance.toAsciiString(bits)
        self.assertEqual("0000000011111111", l_encoded)

    def testToAsciiString_test16_decomposed(self) -> None:
        bits = [0]
        l_encoded = self.instance.toAsciiString(bits)
        self.assertEqual("00000000", l_encoded)

        bits = [self.__BIT_0]
        l_encoded = self.instance.toAsciiString(bits)
        self.assertEqual("00000001", l_encoded)

        bits = [self.__BIT_0 | self.__BIT_1]
        l_encoded = self.instance.toAsciiString(bits)
        self.assertEqual("00000011", l_encoded)

        bits = [self.__BIT_0 | self.__BIT_1 | self.__BIT_2]
        l_encoded = self.instance.toAsciiString(bits)
        self.assertEqual("00000111", l_encoded)

        bits = [self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3]
        l_encoded = self.instance.toAsciiString(bits)
        self.assertEqual("00001111", l_encoded)

        bits = [
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        ]
        l_encoded = self.instance.toAsciiString(bits)
        self.assertEqual("00011111", l_encoded)

        bits = [
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
        ]
        l_encoded = self.instance.toAsciiString(bits)
        self.assertEqual("00111111", l_encoded)

        bits = [
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
        ]
        l_encoded = self.instance.toAsciiString(bits)
        self.assertEqual("01111111", l_encoded)

        bits = [
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        ]
        l_encoded = self.instance.toAsciiString(bits)
        self.assertEqual("11111111", l_encoded)

        bits = [0, 0]
        l_encoded = self.instance.toAsciiString(bits)
        self.assertEqual("0000000000000000", l_encoded)

        bits = [self.__BIT_0, 0]
        l_encoded = self.instance.toAsciiString(bits)
        self.assertEqual("0000000000000001", l_encoded)

        bits = [self.__BIT_0 | self.__BIT_1, 0]
        l_encoded = self.instance.toAsciiString(bits)
        self.assertEqual("0000000000000011", l_encoded)

        bits = [self.__BIT_0 | self.__BIT_1 | self.__BIT_2, 0]
        l_encoded = self.instance.toAsciiString(bits)
        self.assertEqual("0000000000000111", l_encoded)

        bits = [self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3, 0]
        l_encoded = self.instance.toAsciiString(bits)
        self.assertEqual("0000000000001111", l_encoded)

        bits = [
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4,
            0,
        ]
        l_encoded = self.instance.toAsciiString(bits)
        self.assertEqual("0000000000011111", l_encoded)

        bits = [
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5,
            0,
        ]
        l_encoded = self.instance.toAsciiString(bits)
        self.assertEqual("0000000000111111", l_encoded)

        bits = [
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6,
            0,
        ]
        l_encoded = self.instance.toAsciiString(bits)
        self.assertEqual("0000000001111111", l_encoded)

    def testToAsciiString_test15_decomposed(self) -> None:
        bits = bytearray(1)
        l_encoded = BinaryCodec.toAsciiString(bits)
        self.assertEqual("00000000", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0
        l_encoded = BinaryCodec.toAsciiString(bits)
        self.assertEqual("00000001", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1
        l_encoded = BinaryCodec.toAsciiString(bits)
        self.assertEqual("00000011", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        l_encoded = BinaryCodec.toAsciiString(bits)
        self.assertEqual("00000111", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        l_encoded = BinaryCodec.toAsciiString(bits)
        self.assertEqual("00001111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        )
        l_encoded = BinaryCodec.toAsciiString(bits)
        self.assertEqual("00011111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
        )
        l_encoded = BinaryCodec.toAsciiString(bits)
        self.assertEqual("00111111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
        )
        l_encoded = BinaryCodec.toAsciiString(bits)
        self.assertEqual("01111111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        l_encoded = BinaryCodec.toAsciiString(bits)
        self.assertEqual("11111111", l_encoded)

        bits = bytearray(2)
        l_encoded = BinaryCodec.toAsciiString(bits)
        self.assertEqual("0000000000000000", l_encoded)

        bits = bytearray(2)
        bits[0] = self.__BIT_0
        l_encoded = BinaryCodec.toAsciiString(bits)
        self.assertEqual("0000000000000001", l_encoded)

        bits = bytearray(2)
        bits[0] = self.__BIT_0 | self.__BIT_1
        l_encoded = BinaryCodec.toAsciiString(bits)
        self.assertEqual("0000000000000011", l_encoded)

        bits = bytearray(2)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        l_encoded = BinaryCodec.toAsciiString(bits)
        self.assertEqual("0000000000000111", l_encoded)

        bits = bytearray(2)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        l_encoded = BinaryCodec.toAsciiString(bits)
        self.assertEqual("0000000000001111", l_encoded)

        bits = bytearray(2)
        bits[0] = (
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        )
        l_encoded = BinaryCodec.toAsciiString(bits)
        self.assertEqual("0000000000011111", l_encoded)

        bits = bytearray(2)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
        )
        l_encoded = BinaryCodec.toAsciiString(bits)
        self.assertEqual("0000000000111111", l_encoded)

    def testToAsciiString_test14_decomposed(self) -> None:
        bits = [0]
        l_encoded = BinaryCodec.toAsciiString(bits)
        self.assertEqual("00000000", l_encoded)

        bits = [self.__BIT_0]
        l_encoded = BinaryCodec.toAsciiString(bits)
        self.assertEqual("00000001", l_encoded)

        bits = [self.__BIT_0 | self.__BIT_1]
        l_encoded = BinaryCodec.toAsciiString(bits)
        self.assertEqual("00000011", l_encoded)

        bits = [self.__BIT_0 | self.__BIT_1 | self.__BIT_2]
        l_encoded = BinaryCodec.toAsciiString(bits)
        self.assertEqual("00000111", l_encoded)

        bits = [self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3]
        l_encoded = BinaryCodec.toAsciiString(bits)
        self.assertEqual("00001111", l_encoded)

        bits = [
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        ]
        l_encoded = BinaryCodec.toAsciiString(bits)
        self.assertEqual("00011111", l_encoded)

        bits = [
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
        ]
        l_encoded = BinaryCodec.toAsciiString(bits)
        self.assertEqual("00111111", l_encoded)

        bits = [
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
        ]
        l_encoded = BinaryCodec.toAsciiString(bits)
        self.assertEqual("01111111", l_encoded)

        bits = [
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        ]
        l_encoded = BinaryCodec.toAsciiString(bits)
        self.assertEqual("11111111", l_encoded)

        bits = [0, 0]
        l_encoded = BinaryCodec.toAsciiString(bits)
        self.assertEqual("0000000000000000", l_encoded)

        bits = [self.__BIT_0, 0]
        l_encoded = BinaryCodec.toAsciiString(bits)
        self.assertEqual("0000000000000001", l_encoded)

        bits = [self.__BIT_0 | self.__BIT_1, 0]
        l_encoded = BinaryCodec.toAsciiString(bits)
        self.assertEqual("0000000000000011", l_encoded)

        bits = [self.__BIT_0 | self.__BIT_1 | self.__BIT_2, 0]
        l_encoded = BinaryCodec.toAsciiString(bits)
        self.assertEqual("0000000000000111", l_encoded)

        bits = [self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3, 0]
        l_encoded = BinaryCodec.toAsciiString(bits)
        self.assertEqual("0000000000001111", l_encoded)

        bits = [
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4,
            0,
        ]
        l_encoded = BinaryCodec.toAsciiString(bits)
        self.assertEqual("0000000000011111", l_encoded)

    def testToAsciiString_test13_decomposed(self) -> None:
        bits = [0]
        l_encoded = BinaryCodec.toAsciiString(bits)
        self.assertEqual("00000000", l_encoded)

        bits = [self.__BIT_0]
        l_encoded = BinaryCodec.toAsciiString(bits)
        self.assertEqual("00000001", l_encoded)

        bits = [self.__BIT_0 | self.__BIT_1]
        l_encoded = BinaryCodec.toAsciiString(bits)
        self.assertEqual("00000011", l_encoded)

        bits = [self.__BIT_0 | self.__BIT_1 | self.__BIT_2]
        l_encoded = BinaryCodec.toAsciiString(bits)
        self.assertEqual("00000111", l_encoded)

        bits = [self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3]
        l_encoded = BinaryCodec.toAsciiString(bits)
        self.assertEqual("00001111", l_encoded)

        bits = [
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        ]
        l_encoded = BinaryCodec.toAsciiString(bits)
        self.assertEqual("00011111", l_encoded)

        bits = [
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
        ]
        l_encoded = BinaryCodec.toAsciiString(bits)
        self.assertEqual("00111111", l_encoded)

        bits = [
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
        ]
        l_encoded = BinaryCodec.toAsciiString(bits)
        self.assertEqual("01111111", l_encoded)

        bits = [
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        ]
        l_encoded = BinaryCodec.toAsciiString(bits)
        self.assertEqual("11111111", l_encoded)

        bits = [0, 0]
        l_encoded = BinaryCodec.toAsciiString(bits)
        self.assertEqual("0000000000000000", l_encoded)

        bits = [self.__BIT_0, 0]
        l_encoded = BinaryCodec.toAsciiString(bits)
        self.assertEqual("0000000000000001", l_encoded)

        bits = [self.__BIT_0 | self.__BIT_1, 0]
        l_encoded = BinaryCodec.toAsciiString(bits)
        self.assertEqual("0000000000000011", l_encoded)

        bits = [self.__BIT_0 | self.__BIT_1 | self.__BIT_2, 0]
        l_encoded = BinaryCodec.toAsciiString(bits)
        self.assertEqual("0000000000000111", l_encoded)

        bits = [self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3, 0]
        l_encoded = BinaryCodec.toAsciiString(bits)
        self.assertEqual("0000000000001111", l_encoded)

    def testToAsciiString_test12_decomposed(self) -> None:
        bits = [0]
        l_encoded = self.instance.toAsciiString(bits)
        self.assertEqual("00000000", l_encoded)

        bits = [self.__BIT_0]
        l_encoded = self.instance.toAsciiString(bits)
        self.assertEqual("00000001", l_encoded)

        bits = [self.__BIT_0 | self.__BIT_1]
        l_encoded = self.instance.toAsciiString(bits)
        self.assertEqual("00000011", l_encoded)

        bits = [self.__BIT_0 | self.__BIT_1 | self.__BIT_2]
        l_encoded = self.instance.toAsciiString(bits)
        self.assertEqual("00000111", l_encoded)

        bits = [self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3]
        l_encoded = self.instance.toAsciiString(bits)
        self.assertEqual("00001111", l_encoded)

        bits = [
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        ]
        l_encoded = self.instance.toAsciiString(bits)
        self.assertEqual("00011111", l_encoded)

        bits = [
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
        ]
        l_encoded = self.instance.toAsciiString(bits)
        self.assertEqual("00111111", l_encoded)

        bits = [
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
        ]
        l_encoded = self.instance.toAsciiString(bits)
        self.assertEqual("01111111", l_encoded)

        bits = [
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        ]
        l_encoded = self.instance.toAsciiString(bits)
        self.assertEqual("11111111", l_encoded)

        bits = [0, 0]
        l_encoded = self.instance.toAsciiString(bits)
        self.assertEqual("0000000000000000", l_encoded)

        bits = [self.__BIT_0, 0]
        l_encoded = self.instance.toAsciiString(bits)
        self.assertEqual("0000000000000001", l_encoded)

        bits = [self.__BIT_0 | self.__BIT_1, 0]
        l_encoded = self.instance.toAsciiString(bits)
        self.assertEqual("0000000000000011", l_encoded)

        bits = [self.__BIT_0 | self.__BIT_1 | self.__BIT_2, 0]
        l_encoded = self.instance.toAsciiString(bits)
        self.assertEqual("0000000000000111", l_encoded)

    def testToAsciiString_test11_decomposed(self) -> None:
        bits = [0]
        l_encoded = BinaryCodec.toAsciiString(bits)
        self.assertEqual("00000000", l_encoded)

        bits = [self.__BIT_0]
        l_encoded = BinaryCodec.toAsciiString(bits)
        self.assertEqual("00000001", l_encoded)

        bits = [self.__BIT_0 | self.__BIT_1]
        l_encoded = BinaryCodec.toAsciiString(bits)
        self.assertEqual("00000011", l_encoded)

        bits = [self.__BIT_0 | self.__BIT_1 | self.__BIT_2]
        l_encoded = BinaryCodec.toAsciiString(bits)
        self.assertEqual("00000111", l_encoded)

        bits = [self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3]
        l_encoded = BinaryCodec.toAsciiString(bits)
        self.assertEqual("00001111", l_encoded)

        bits = [
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        ]
        l_encoded = BinaryCodec.toAsciiString(bits)
        self.assertEqual("00011111", l_encoded)

        bits = [
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
        ]
        l_encoded = BinaryCodec.toAsciiString(bits)
        self.assertEqual("00111111", l_encoded)

        bits = [
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
        ]
        l_encoded = BinaryCodec.toAsciiString(bits)
        self.assertEqual("01111111", l_encoded)

        bits = [
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        ]
        l_encoded = BinaryCodec.toAsciiString(bits)
        self.assertEqual("11111111", l_encoded)

        bits = [0, 0]
        l_encoded = BinaryCodec.toAsciiString(bits)
        self.assertEqual("0000000000000000", l_encoded)

        bits = [self.__BIT_0, 0]
        l_encoded = BinaryCodec.toAsciiString(bits)
        self.assertEqual("0000000000000001", l_encoded)

        bits = [self.__BIT_0 | self.__BIT_1, 0]
        l_encoded = BinaryCodec.toAsciiString(bits)
        self.assertEqual("0000000000000011", l_encoded)

    def testToAsciiString_test10_decomposed(self) -> None:
        bits = bytearray(1)
        l_encoded = BinaryCodec.toAsciiString(bits)
        self.assertEqual("00000000", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0
        l_encoded = BinaryCodec.toAsciiString(bits)
        self.assertEqual("00000001", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1
        l_encoded = BinaryCodec.toAsciiString(bits)
        self.assertEqual("00000011", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        l_encoded = BinaryCodec.toAsciiString(bits)
        self.assertEqual("00000111", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        l_encoded = BinaryCodec.toAsciiString(bits)
        self.assertEqual("00001111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        )
        l_encoded = BinaryCodec.toAsciiString(bits)
        self.assertEqual("00011111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
        )
        l_encoded = BinaryCodec.toAsciiString(bits)
        self.assertEqual("00111111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
        )
        l_encoded = BinaryCodec.toAsciiString(bits)
        self.assertEqual("01111111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        l_encoded = BinaryCodec.toAsciiString(bits)
        self.assertEqual("11111111", l_encoded)

        bits = bytearray(2)
        l_encoded = BinaryCodec.toAsciiString(bits)
        self.assertEqual("0000000000000000", l_encoded)

        bits = bytearray(2)
        bits[0] = self.__BIT_0
        l_encoded = BinaryCodec.toAsciiString(bits)
        self.assertEqual("0000000100000000", l_encoded)

    def testToAsciiString_test9_decomposed(self) -> None:
        bits = [0]
        l_encoded = BinaryCodec.toAsciiString(bits)
        self.assertEqual("00000000", l_encoded)

        bits = [self.__BIT_0]
        l_encoded = BinaryCodec.toAsciiString(bits)
        self.assertEqual("00000001", l_encoded)

        bits = [self.__BIT_0 | self.__BIT_1]
        l_encoded = BinaryCodec.toAsciiString(bits)
        self.assertEqual("00000011", l_encoded)

        bits = [self.__BIT_0 | self.__BIT_1 | self.__BIT_2]
        l_encoded = BinaryCodec.toAsciiString(bits)
        self.assertEqual("00000111", l_encoded)

        bits = [self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3]
        l_encoded = BinaryCodec.toAsciiString(bits)
        self.assertEqual("00001111", l_encoded)

        bits = [
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        ]
        l_encoded = BinaryCodec.toAsciiString(bits)
        self.assertEqual("00011111", l_encoded)

        bits = [
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
        ]
        l_encoded = BinaryCodec.toAsciiString(bits)
        self.assertEqual("00111111", l_encoded)

        bits = [
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
        ]
        l_encoded = BinaryCodec.toAsciiString(bits)
        self.assertEqual("01111111", l_encoded)

        bits = [
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        ]
        l_encoded = BinaryCodec.toAsciiString(bits)
        self.assertEqual("11111111", l_encoded)

        bits = [0, 0]
        l_encoded = BinaryCodec.toAsciiString(bits)
        # No assertion provided in the original Java code for this case

    def testToAsciiString_test8_decomposed(self) -> None:
        bits = [0]
        l_encoded = BinaryCodec.toAsciiString(bits)
        self.assertEqual("00000000", l_encoded)

        bits = [self.__BIT_0]
        l_encoded = BinaryCodec.toAsciiString(bits)
        self.assertEqual("00000001", l_encoded)

        bits = [self.__BIT_0 | self.__BIT_1]
        l_encoded = BinaryCodec.toAsciiString(bits)
        self.assertEqual("00000011", l_encoded)

        bits = [self.__BIT_0 | self.__BIT_1 | self.__BIT_2]
        l_encoded = BinaryCodec.toAsciiString(bits)
        self.assertEqual("00000111", l_encoded)

        bits = [self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3]
        l_encoded = BinaryCodec.toAsciiString(bits)
        self.assertEqual("00001111", l_encoded)

        bits = [
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        ]
        l_encoded = BinaryCodec.toAsciiString(bits)
        self.assertEqual("00011111", l_encoded)

        bits = [
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
        ]
        l_encoded = BinaryCodec.toAsciiString(bits)
        self.assertEqual("00111111", l_encoded)

        bits = [
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
        ]
        l_encoded = BinaryCodec.toAsciiString(bits)
        self.assertEqual("01111111", l_encoded)

        bits = [
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        ]
        l_encoded = BinaryCodec.toAsciiString(bits)
        self.assertEqual("11111111", l_encoded)

    def testToAsciiString_test7_decomposed(self) -> None:
        bits = bytearray(1)
        l_encoded = self.instance.toAsciiString(bits)
        self.assertEqual("00000000", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0
        l_encoded = self.instance.toAsciiString(bits)
        self.assertEqual("00000001", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1
        l_encoded = self.instance.toAsciiString(bits)
        self.assertEqual("00000011", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        l_encoded = self.instance.toAsciiString(bits)
        self.assertEqual("00000111", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        l_encoded = self.instance.toAsciiString(bits)
        self.assertEqual("00001111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        )
        l_encoded = self.instance.toAsciiString(bits)
        self.assertEqual("00011111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
        )
        l_encoded = self.instance.toAsciiString(bits)
        self.assertEqual("00111111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
        )
        l_encoded = self.instance.toAsciiString(bits)
        self.assertEqual("01111111", l_encoded)

    def testToAsciiString_test6_decomposed(self) -> None:
        bits = bytearray(1)
        l_encoded = self.instance.toAsciiString(bits)
        self.assertEqual("00000000", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0
        l_encoded = self.instance.toAsciiString(bits)
        self.assertEqual("00000001", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1
        l_encoded = self.instance.toAsciiString(bits)
        self.assertEqual("00000011", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        l_encoded = self.instance.toAsciiString(bits)
        self.assertEqual("00000111", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        l_encoded = self.instance.toAsciiString(bits)
        self.assertEqual("00001111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        )
        l_encoded = self.instance.toAsciiString(bits)
        self.assertEqual("00011111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
        )
        l_encoded = self.instance.toAsciiString(bits)
        self.assertEqual("00111111", l_encoded)

    def testToAsciiString_test5_decomposed(self) -> None:
        bits = [0]
        l_encoded = BinaryCodec.toAsciiString(bits)
        self.assertEqual("00000000", l_encoded)

        bits = [self.__BIT_0]
        l_encoded = BinaryCodec.toAsciiString(bits)
        self.assertEqual("00000001", l_encoded)

        bits = [self.__BIT_0 | self.__BIT_1]
        l_encoded = BinaryCodec.toAsciiString(bits)
        self.assertEqual("00000011", l_encoded)

        bits = [self.__BIT_0 | self.__BIT_1 | self.__BIT_2]
        l_encoded = BinaryCodec.toAsciiString(bits)
        self.assertEqual("00000111", l_encoded)

        bits = [self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3]
        l_encoded = BinaryCodec.toAsciiString(bits)
        self.assertEqual("00001111", l_encoded)

        bits = [
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        ]
        l_encoded = BinaryCodec.toAsciiString(bits)
        self.assertEqual("00011111", l_encoded)

    def testToAsciiString_test4_decomposed(self) -> None:
        bits = [0]
        l_encoded = self.instance.toAsciiString(bits)
        self.assertEqual("00000000", l_encoded)

        bits = [0]
        bits[0] = self.__BIT_0
        l_encoded = self.instance.toAsciiString(bits)
        self.assertEqual("00000001", l_encoded)

        bits = [0]
        bits[0] = self.__BIT_0 | self.__BIT_1
        l_encoded = self.instance.toAsciiString(bits)
        self.assertEqual("00000011", l_encoded)

        bits = [0]
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        l_encoded = self.instance.toAsciiString(bits)
        self.assertEqual("00000111", l_encoded)

        bits = [0]
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        l_encoded = self.instance.toAsciiString(bits)
        self.assertEqual("00001111", l_encoded)

    def testToAsciiString_test3_decomposed(self) -> None:
        bits = [0]  # Equivalent to new byte[1] in Java
        l_encoded = BinaryCodec.toAsciiString(bits)
        self.assertEqual("00000000", l_encoded)

        bits = [0]  # Reset bits
        bits[0] = self.__BIT_0
        l_encoded = BinaryCodec.toAsciiString(bits)
        self.assertEqual("00000001", l_encoded)

        bits = [0]  # Reset bits
        bits[0] = self.__BIT_0 | self.__BIT_1
        l_encoded = BinaryCodec.toAsciiString(bits)
        self.assertEqual("00000011", l_encoded)

        bits = [0]  # Reset bits
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        l_encoded = BinaryCodec.toAsciiString(bits)
        self.assertEqual("00000111", l_encoded)

    def testToAsciiString_test2_decomposed(self) -> None:
        bits = [0]  # Initialize a byte array with one element set to 0
        l_encoded = BinaryCodec.toAsciiString(bits)
        self.assertEqual("00000000", l_encoded)

        bits = [0]  # Reinitialize the byte array
        bits[0] = self.__BIT_0  # Set the first bit to BIT_0
        l_encoded = BinaryCodec.toAsciiString(bits)
        self.assertEqual("00000001", l_encoded)

        bits = [0]  # Reinitialize the byte array
        bits[0] = self.__BIT_0 | self.__BIT_1  # Set the first bit to BIT_0 OR BIT_1
        l_encoded = BinaryCodec.toAsciiString(bits)
        self.assertEqual("00000011", l_encoded)

    def testToAsciiString_test1_decomposed(self) -> None:
        bits = bytearray(1)  # Create a byte array of size 1, initialized to 0
        l_encoded = BinaryCodec.toAsciiString(bits)  # Call the toAsciiString method
        self.assertEqual(
            "00000000", l_encoded
        )  # Assert that the result matches the expected string

        bits = bytearray(1)  # Create a new byte array of size 1
        bits[0] = self.__BIT_0  # Set the first byte to BIT_0 (0x01)
        l_encoded = BinaryCodec.toAsciiString(
            bits
        )  # Call the toAsciiString method again
        # No assertion is provided for the second call in the original Java code

    def testToAsciiString_test0_decomposed(self) -> None:
        bits = bytearray(1)  # Equivalent to `byte[] bits = new byte[1];` in Java
        l_encoded = self.instance.toAsciiString(bits)  # Call the `toAsciiString` method

    def testToAsciiChars_test26_decomposed(self) -> None:
        bits = bytearray(1)
        l_encoded = "".join(BinaryCodec.toAsciiChars(bits))
        self.assertEqual("00000000", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0
        l_encoded = "".join(BinaryCodec.toAsciiChars(bits))
        self.assertEqual("00000001", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1
        l_encoded = "".join(BinaryCodec.toAsciiChars(bits))
        self.assertEqual("00000011", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        l_encoded = "".join(BinaryCodec.toAsciiChars(bits))
        self.assertEqual("00000111", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        l_encoded = "".join(BinaryCodec.toAsciiChars(bits))
        self.assertEqual("00001111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        )
        l_encoded = "".join(BinaryCodec.toAsciiChars(bits))
        self.assertEqual("00011111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
        )
        l_encoded = "".join(BinaryCodec.toAsciiChars(bits))
        self.assertEqual("00111111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
        )
        l_encoded = "".join(BinaryCodec.toAsciiChars(bits))
        self.assertEqual("01111111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        l_encoded = "".join(BinaryCodec.toAsciiChars(bits))
        self.assertEqual("11111111", l_encoded)

        bits = bytearray(2)
        l_encoded = "".join(BinaryCodec.toAsciiChars(bits))
        self.assertEqual("0000000000000000", l_encoded)

        bits = bytearray(2)
        bits[0] = self.__BIT_0
        l_encoded = "".join(BinaryCodec.toAsciiChars(bits))
        self.assertEqual("0000000000000001", l_encoded)

        bits = bytearray(2)
        bits[0] = self.__BIT_0 | self.__BIT_1
        l_encoded = "".join(BinaryCodec.toAsciiChars(bits))
        self.assertEqual("0000000000000011", l_encoded)

        bits = bytearray(2)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        l_encoded = "".join(BinaryCodec.toAsciiChars(bits))
        self.assertEqual("0000000000000111", l_encoded)

        bits = bytearray(2)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        l_encoded = "".join(BinaryCodec.toAsciiChars(bits))
        self.assertEqual("0000000000001111", l_encoded)

        bits = bytearray(2)
        bits[0] = (
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        )
        l_encoded = "".join(BinaryCodec.toAsciiChars(bits))
        self.assertEqual("0000000000011111", l_encoded)

        bits = bytearray(2)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
        )
        l_encoded = "".join(BinaryCodec.toAsciiChars(bits))
        self.assertEqual("0000000000111111", l_encoded)

        bits = bytearray(2)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
        )
        l_encoded = "".join(BinaryCodec.toAsciiChars(bits))
        self.assertEqual("0000000001111111", l_encoded)

        bits = bytearray(2)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        l_encoded = "".join(BinaryCodec.toAsciiChars(bits))
        self.assertEqual("0000000011111111", l_encoded)

        bits = bytearray(2)
        bits[1] = self.__BIT_0
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        l_encoded = "".join(BinaryCodec.toAsciiChars(bits))
        self.assertEqual("0000000111111111", l_encoded)

        bits = bytearray(2)
        bits[1] = self.__BIT_0 | self.__BIT_1
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        l_encoded = "".join(BinaryCodec.toAsciiChars(bits))
        self.assertEqual("0000001111111111", l_encoded)

        bits = bytearray(2)
        bits[1] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        l_encoded = "".join(BinaryCodec.toAsciiChars(bits))
        self.assertEqual("0000011111111111", l_encoded)

        bits = bytearray(2)
        bits[1] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        l_encoded = "".join(BinaryCodec.toAsciiChars(bits))
        self.assertEqual("0000111111111111", l_encoded)

        bits = bytearray(2)
        bits[1] = (
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        )
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        l_encoded = "".join(BinaryCodec.toAsciiChars(bits))
        self.assertEqual("0001111111111111", l_encoded)

        bits = bytearray(2)
        bits[1] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
        )
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        l_encoded = "".join(BinaryCodec.toAsciiChars(bits))
        self.assertEqual("0011111111111111", l_encoded)

        bits = bytearray(2)
        bits[1] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
        )
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        l_encoded = "".join(BinaryCodec.toAsciiChars(bits))
        self.assertEqual("0111111111111111", l_encoded)

        bits = bytearray(2)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        bits[1] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        l_encoded = "".join(BinaryCodec.toAsciiChars(bits))
        self.assertEqual("1111111111111111", l_encoded)

        self.assertEqual(0, len(BinaryCodec.toAsciiChars(None)))

    def testToAsciiChars_test25_decomposed(self) -> None:
        bits = bytearray(1)
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("00000000", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("00000001", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("00000011", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("00000111", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("00001111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        )
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("00011111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
        )
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("00111111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
        )
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("01111111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("11111111", l_encoded)

        bits = bytearray(2)
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("0000000000000000", l_encoded)

        bits = bytearray(2)
        bits[0] = self.__BIT_0
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("0000000000000001", l_encoded)

        bits = bytearray(2)
        bits[0] = self.__BIT_0 | self.__BIT_1
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("0000000000000011", l_encoded)

        bits = bytearray(2)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("0000000000000111", l_encoded)

        bits = bytearray(2)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("0000000000001111", l_encoded)

        bits = bytearray(2)
        bits[0] = (
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        )
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("0000000000011111", l_encoded)

        bits = bytearray(2)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
        )
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("0000000000111111", l_encoded)

        bits = bytearray(2)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
        )
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("0000000001111111", l_encoded)

        bits = bytearray(2)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("0000000011111111", l_encoded)

        bits = bytearray(2)
        bits[1] = self.__BIT_0
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("0000000111111111", l_encoded)

        bits = bytearray(2)
        bits[1] = self.__BIT_0 | self.__BIT_1
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("0000001111111111", l_encoded)

        bits = bytearray(2)
        bits[1] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("0000011111111111", l_encoded)

        bits = bytearray(2)
        bits[1] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("0000111111111111", l_encoded)

        bits = bytearray(2)
        bits[1] = (
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        )
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("0001111111111111", l_encoded)

        bits = bytearray(2)
        bits[1] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
        )
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("0011111111111111", l_encoded)

        bits = bytearray(2)
        bits[1] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
        )
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("0111111111111111", l_encoded)

        bits = bytearray(2)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        bits[1] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("1111111111111111", l_encoded)

    def testToAsciiChars_test24_decomposed(self) -> None:
        bits = bytearray(1)
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("00000000", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("00000001", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("00000011", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("00000111", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("00001111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        )
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("00011111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
        )
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("00111111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
        )
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("01111111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("11111111", l_encoded)

        bits = bytearray(2)
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("0000000000000000", l_encoded)

        bits = bytearray(2)
        bits[0] = self.__BIT_0
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("0000000000000001", l_encoded)

        bits = bytearray(2)
        bits[0] = self.__BIT_0 | self.__BIT_1
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("0000000000000011", l_encoded)

        bits = bytearray(2)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("0000000000000111", l_encoded)

        bits = bytearray(2)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("0000000000001111", l_encoded)

        bits = bytearray(2)
        bits[0] = (
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        )
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("0000000000011111", l_encoded)

        bits = bytearray(2)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
        )
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("0000000000111111", l_encoded)

        bits = bytearray(2)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
        )
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("0000000001111111", l_encoded)

        bits = bytearray(2)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("0000000011111111", l_encoded)

        bits = bytearray(2)
        bits[1] = self.__BIT_0
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("0000000111111111", l_encoded)

        bits = bytearray(2)
        bits[1] = self.__BIT_0 | self.__BIT_1
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("0000001111111111", l_encoded)

        bits = bytearray(2)
        bits[1] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("0000011111111111", l_encoded)

        bits = bytearray(2)
        bits[1] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("0000111111111111", l_encoded)

        bits = bytearray(2)
        bits[1] = (
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        )
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("0001111111111111", l_encoded)

        bits = bytearray(2)
        bits[1] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
        )
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("0011111111111111", l_encoded)

        bits = bytearray(2)
        bits[1] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
        )
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("0111111111111111", l_encoded)

    def testToAsciiChars_test23_decomposed(self) -> None:
        bits = bytearray(1)
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("00000000", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("00000001", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("00000011", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("00000111", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("00001111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        )
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("00011111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
        )
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("00111111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
        )
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("01111111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("11111111", l_encoded)

        bits = bytearray(2)
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("0000000000000000", l_encoded)

        bits = bytearray(2)
        bits[0] = self.__BIT_0
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("0000000000000001", l_encoded)

        bits = bytearray(2)
        bits[0] = self.__BIT_0 | self.__BIT_1
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("0000000000000011", l_encoded)

        bits = bytearray(2)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("0000000000000111", l_encoded)

        bits = bytearray(2)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("0000000000001111", l_encoded)

        bits = bytearray(2)
        bits[0] = (
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        )
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("0000000000011111", l_encoded)

        bits = bytearray(2)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
        )
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("0000000000111111", l_encoded)

        bits = bytearray(2)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
        )
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("0000000001111111", l_encoded)

        bits = bytearray(2)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("0000000011111111", l_encoded)

        bits = bytearray(2)
        bits[1] = self.__BIT_0
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("0000000111111111", l_encoded)

        bits = bytearray(2)
        bits[1] = self.__BIT_0 | self.__BIT_1
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("0000001111111111", l_encoded)

        bits = bytearray(2)
        bits[1] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("0000011111111111", l_encoded)

        bits = bytearray(2)
        bits[1] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("0000111111111111", l_encoded)

        bits = bytearray(2)
        bits[1] = (
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        )
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("0001111111111111", l_encoded)

        bits = bytearray(2)
        bits[1] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
        )
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("0001111111111111", l_encoded)

    def testToAsciiChars_test22_decomposed(self) -> None:
        bits = bytearray(1)
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("00000000", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("00000001", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("00000011", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("00000111", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("00001111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        )
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("00011111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
        )
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("00111111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
        )
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("01111111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("11111111", l_encoded)

        bits = bytearray(2)
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("0000000000000000", l_encoded)

        bits = bytearray(2)
        bits[0] = self.__BIT_0
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("0000000000000001", l_encoded)

        bits = bytearray(2)
        bits[0] = self.__BIT_0 | self.__BIT_1
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("0000000000000011", l_encoded)

        bits = bytearray(2)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("0000000000000111", l_encoded)

        bits = bytearray(2)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("0000000000001111", l_encoded)

        bits = bytearray(2)
        bits[0] = (
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        )
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("0000000000011111", l_encoded)

        bits = bytearray(2)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
        )
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("0000000000111111", l_encoded)

        bits = bytearray(2)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
        )
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("0000000001111111", l_encoded)

        bits = bytearray(2)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("0000000011111111", l_encoded)

        bits = bytearray(2)
        bits[1] = self.__BIT_0
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("0000000111111111", l_encoded)

        bits = bytearray(2)
        bits[1] = self.__BIT_0 | self.__BIT_1
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("0000001111111111", l_encoded)

        bits = bytearray(2)
        bits[1] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("0000011111111111", l_encoded)

        bits = bytearray(2)
        bits[1] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("0000111111111111", l_encoded)

        bits = bytearray(2)
        bits[1] = (
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        )
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("0001111111111111", l_encoded)

    def testToAsciiChars_test21_decomposed(self) -> None:
        bits = bytearray(1)
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("00000000", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("00000001", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("00000011", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("00000111", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("00001111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        )
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("00011111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
        )
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("00111111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
        )
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("01111111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("11111111", l_encoded)

        bits = bytearray(2)
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("0000000000000000", l_encoded)

        bits = bytearray(2)
        bits[0] = self.__BIT_0
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("0000000000000001", l_encoded)

        bits = bytearray(2)
        bits[0] = self.__BIT_0 | self.__BIT_1
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("0000000000000011", l_encoded)

        bits = bytearray(2)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("0000000000000111", l_encoded)

        bits = bytearray(2)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("0000000000001111", l_encoded)

        bits = bytearray(2)
        bits[0] = (
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        )
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("0000000000011111", l_encoded)

        bits = bytearray(2)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
        )
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("0000000000111111", l_encoded)

        bits = bytearray(2)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
        )
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("0000000001111111", l_encoded)

        bits = bytearray(2)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("0000000011111111", l_encoded)

        bits = bytearray(2)
        bits[1] = self.__BIT_0
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("0000000111111111", l_encoded)

        bits = bytearray(2)
        bits[1] = self.__BIT_0 | self.__BIT_1
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("0000001111111111", l_encoded)

        bits = bytearray(2)
        bits[1] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("0000011111111111", l_encoded)

        bits = bytearray(2)
        bits[1] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("0000111111111111", l_encoded)

    def testToAsciiChars_test20_decomposed(self) -> None:
        bits = bytearray(1)
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("00000000", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("00000001", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("00000011", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("00000111", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("00001111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        )
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("00011111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
        )
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("00111111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
        )
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("01111111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("11111111", l_encoded)

        bits = bytearray(2)
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("0000000000000000", l_encoded)

        bits = bytearray(2)
        bits[0] = self.__BIT_0
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("0000000000000001", l_encoded)

        bits = bytearray(2)
        bits[0] = self.__BIT_0 | self.__BIT_1
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("0000000000000011", l_encoded)

        bits = bytearray(2)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("0000000000000111", l_encoded)

        bits = bytearray(2)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("0000000000001111", l_encoded)

        bits = bytearray(2)
        bits[0] = (
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        )
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("0000000000011111", l_encoded)

        bits = bytearray(2)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
        )
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("0000000000111111", l_encoded)

        bits = bytearray(2)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
        )
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("0000000001111111", l_encoded)

        bits = bytearray(2)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("0000000011111111", l_encoded)

        bits = bytearray(2)
        bits[1] = self.__BIT_0
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("0000000111111111", l_encoded)

        bits = bytearray(2)
        bits[1] = self.__BIT_0 | self.__BIT_1
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("0000001111111111", l_encoded)

        bits = bytearray(2)
        bits[1] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("0000011111111111", l_encoded)

    def testToAsciiChars_test19_decomposed(self) -> None:
        bits = bytearray(1)
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("00000000", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("00000001", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("00000011", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("00000111", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("00001111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        )
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("00011111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
        )
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("00111111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
        )
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("01111111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("11111111", l_encoded)

        bits = bytearray(2)
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("0000000000000000", l_encoded)

        bits = bytearray(2)
        bits[0] = self.__BIT_0
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("0000000000000001", l_encoded)

        bits = bytearray(2)
        bits[0] = self.__BIT_0 | self.__BIT_1
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("0000000000000011", l_encoded)

        bits = bytearray(2)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("0000000000000111", l_encoded)

        bits = bytearray(2)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("0000000000001111", l_encoded)

        bits = bytearray(2)
        bits[0] = (
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        )
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("0000000000011111", l_encoded)

        bits = bytearray(2)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
        )
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("0000000000111111", l_encoded)

        bits = bytearray(2)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
        )
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("0000000001111111", l_encoded)

        bits = bytearray(2)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("0000000011111111", l_encoded)

        bits = bytearray(2)
        bits[1] = self.__BIT_0
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("0000000111111111", l_encoded)

        bits = bytearray(2)
        bits[1] = self.__BIT_0 | self.__BIT_1
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("0000001111111111", l_encoded)

    def testToAsciiChars_test18_decomposed(self) -> None:
        bits = bytearray(1)
        l_encoded = "".join(BinaryCodec.toAsciiChars(bits))
        self.assertEqual("00000000", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0
        l_encoded = "".join(BinaryCodec.toAsciiChars(bits))
        self.assertEqual("00000001", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1
        l_encoded = "".join(BinaryCodec.toAsciiChars(bits))
        self.assertEqual("00000011", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        l_encoded = "".join(BinaryCodec.toAsciiChars(bits))
        self.assertEqual("00000111", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        l_encoded = "".join(BinaryCodec.toAsciiChars(bits))
        self.assertEqual("00001111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        )
        l_encoded = "".join(BinaryCodec.toAsciiChars(bits))
        self.assertEqual("00011111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
        )
        l_encoded = "".join(BinaryCodec.toAsciiChars(bits))
        self.assertEqual("00111111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
        )
        l_encoded = "".join(BinaryCodec.toAsciiChars(bits))
        self.assertEqual("01111111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        l_encoded = "".join(BinaryCodec.toAsciiChars(bits))
        self.assertEqual("11111111", l_encoded)

        bits = bytearray(2)
        l_encoded = "".join(BinaryCodec.toAsciiChars(bits))
        self.assertEqual("0000000000000000", l_encoded)

        bits = bytearray(2)
        bits[0] = self.__BIT_0
        l_encoded = "".join(BinaryCodec.toAsciiChars(bits))
        self.assertEqual("0000000000000001", l_encoded)

        bits = bytearray(2)
        bits[0] = self.__BIT_0 | self.__BIT_1
        l_encoded = "".join(BinaryCodec.toAsciiChars(bits))
        self.assertEqual("0000000000000011", l_encoded)

        bits = bytearray(2)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        l_encoded = "".join(BinaryCodec.toAsciiChars(bits))
        self.assertEqual("0000000000000111", l_encoded)

        bits = bytearray(2)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        l_encoded = "".join(BinaryCodec.toAsciiChars(bits))
        self.assertEqual("0000000000001111", l_encoded)

        bits = bytearray(2)
        bits[0] = (
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        )
        l_encoded = "".join(BinaryCodec.toAsciiChars(bits))
        self.assertEqual("0000000000011111", l_encoded)

        bits = bytearray(2)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
        )
        l_encoded = "".join(BinaryCodec.toAsciiChars(bits))
        self.assertEqual("0000000000111111", l_encoded)

        bits = bytearray(2)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
        )
        l_encoded = "".join(BinaryCodec.toAsciiChars(bits))
        self.assertEqual("0000000001111111", l_encoded)

        bits = bytearray(2)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        l_encoded = "".join(BinaryCodec.toAsciiChars(bits))
        self.assertEqual("0000000011111111", l_encoded)

        bits = bytearray(2)
        bits[1] = self.__BIT_0
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        l_encoded = "".join(BinaryCodec.toAsciiChars(bits))
        self.assertEqual("1111111100000001", l_encoded)

    def testToAsciiChars_test17_decomposed(self) -> None:
        bits = bytearray(1)
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("00000000", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("00000001", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("00000011", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("00000111", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("00001111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        )
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("00011111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
        )
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("00111111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
        )
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("01111111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("11111111", l_encoded)

        bits = bytearray(2)
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("0000000000000000", l_encoded)

        bits = bytearray(2)
        bits[0] = self.__BIT_0
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("0000000000000001", l_encoded)

        bits = bytearray(2)
        bits[0] = self.__BIT_0 | self.__BIT_1
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("0000000000000011", l_encoded)

        bits = bytearray(2)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("0000000000000111", l_encoded)

        bits = bytearray(2)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("0000000000001111", l_encoded)

        bits = bytearray(2)
        bits[0] = (
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        )
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("0000000000011111", l_encoded)

        bits = bytearray(2)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
        )
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("0000000000111111", l_encoded)

        bits = bytearray(2)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
        )
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("0000000001111111", l_encoded)

        bits = bytearray(2)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("1111111111111111", l_encoded)

    def testToAsciiChars_test16_decomposed(self) -> None:
        bits = bytearray(1)
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("00000000", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("00000001", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("00000011", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("00000111", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("00001111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        )
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("00011111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
        )
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("00111111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
        )
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("01111111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("11111111", l_encoded)

        bits = bytearray(2)
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("0000000000000000", l_encoded)

        bits = bytearray(2)
        bits[0] = self.__BIT_0
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("0000000000000001", l_encoded)

        bits = bytearray(2)
        bits[0] = self.__BIT_0 | self.__BIT_1
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("0000000000000011", l_encoded)

        bits = bytearray(2)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("0000000000000111", l_encoded)

        bits = bytearray(2)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("0000000000001111", l_encoded)

        bits = bytearray(2)
        bits[0] = (
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        )
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("0000000000011111", l_encoded)

        bits = bytearray(2)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
        )
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("0000000000111111", l_encoded)

        bits = bytearray(2)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
        )
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("0000000001111111", l_encoded)

    def testToAsciiChars_test15_decomposed(self) -> None:
        bits = bytearray(1)
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("00000000", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("00000001", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("00000011", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("00000111", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("00001111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        )
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("00011111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
        )
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("00111111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
        )
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("01111111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("11111111", l_encoded)

        bits = bytearray(2)
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("0000000000000000", l_encoded)

        bits = bytearray(2)
        bits[0] = self.__BIT_0
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("0000000000000001", l_encoded)

        bits = bytearray(2)
        bits[0] = self.__BIT_0 | self.__BIT_1
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("0000000000000011", l_encoded)

        bits = bytearray(2)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("0000000000000111", l_encoded)

        bits = bytearray(2)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("0000000000001111", l_encoded)

        bits = bytearray(2)
        bits[0] = (
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        )
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("0000000000011111", l_encoded)

        bits = bytearray(2)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
        )
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("0000000000111111", l_encoded)

    def testToAsciiChars_test14_decomposed(self) -> None:
        bits = bytearray(1)
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("00000000", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("00000001", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("00000011", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("00000111", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("00001111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        )
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("00011111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
        )
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("00111111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
        )
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("01111111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("11111111", l_encoded)

        bits = bytearray(2)
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("0000000000000000", l_encoded)

        bits = bytearray(2)
        bits[0] = self.__BIT_0
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("0000000000000001", l_encoded)

        bits = bytearray(2)
        bits[0] = self.__BIT_0 | self.__BIT_1
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("0000000000000011", l_encoded)

        bits = bytearray(2)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("0000000000000111", l_encoded)

        bits = bytearray(2)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("0000000000001111", l_encoded)

        bits = bytearray(2)
        bits[0] = (
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        )
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("0000000000011111", l_encoded)

    def testToAsciiChars_test13_decomposed(self) -> None:
        bits = bytearray(1)
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("00000000", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("00000001", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("00000011", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("00000111", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("00001111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        )
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("00011111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
        )
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("00111111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
        )
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("01111111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("11111111", l_encoded)

        bits = bytearray(2)
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("0000000000000000", l_encoded)

        bits = bytearray(2)
        bits[0] = self.__BIT_0
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("0000000000000001", l_encoded)

        bits = bytearray(2)
        bits[0] = self.__BIT_0 | self.__BIT_1
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("0000000000000011", l_encoded)

        bits = bytearray(2)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("0000000000000111", l_encoded)

        bits = bytearray(2)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("0000000000001111", l_encoded)

    def testToAsciiChars_test12_decomposed(self) -> None:
        bits = bytearray(1)
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("00000000", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("00000001", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("00000011", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("00000111", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("00001111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        )
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("00011111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
        )
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("00111111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
        )
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("01111111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("11111111", l_encoded)

        bits = bytearray(2)
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("0000000000000000", l_encoded)

        bits = bytearray(2)
        bits[0] = self.__BIT_0
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("0000000000000001", l_encoded)

        bits = bytearray(2)
        bits[0] = self.__BIT_0 | self.__BIT_1
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("0000000000000011", l_encoded)

        bits = bytearray(2)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("0000000000000111", l_encoded)

    def testToAsciiChars_test11_decomposed(self) -> None:
        bits = bytearray(1)
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("00000000", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("00000001", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("00000011", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("00000111", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("00001111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        )
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("00011111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
        )
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("00111111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
        )
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("01111111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("11111111", l_encoded)

        bits = bytearray(2)
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("0000000000000000", l_encoded)

        bits = bytearray(2)
        bits[0] = self.__BIT_0
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("0000000000000001", l_encoded)

        bits = bytearray(2)
        bits[0] = self.__BIT_0 | self.__BIT_1
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("0000000000000011", l_encoded)

    def testToAsciiChars_test10_decomposed(self) -> None:
        bits = bytearray(1)
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("00000000", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("00000001", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("00000011", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("00000111", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("00001111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        )
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("00011111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
        )
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("00111111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
        )
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("01111111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("11111111", l_encoded)

        bits = bytearray(2)
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("0000000000000000", l_encoded)

        bits = bytearray(2)
        bits[0] = self.__BIT_0
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("0000000100000000", l_encoded)

    def testToAsciiChars_test9_decomposed(self) -> None:
        bits = bytearray(1)
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("00000000", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("00000001", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("00000011", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("00000111", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("00001111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        )
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("00011111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
        )
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("00111111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
        )
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("01111111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("11111111", l_encoded)

        bits = bytearray(2)
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        # Add an assertion here if needed, depending on the expected result

    def testToAsciiChars_test8_decomposed(self) -> None:
        bits = bytearray(1)
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("00000000", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("00000001", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("00000011", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("00000111", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("00001111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        )
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("00011111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
        )
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("00111111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
        )
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("01111111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("11111111", l_encoded)

    def testToAsciiChars_test7_decomposed(self) -> None:
        bits = bytearray(1)
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("00000000", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("00000001", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("00000011", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("00000111", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("00001111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        )
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("00011111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
        )
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("00111111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
        )
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("01111111", l_encoded)

    def testToAsciiChars_test6_decomposed(self) -> None:
        bits = bytearray(1)
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("00000000", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("00000001", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("00000011", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("00000111", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("00001111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        )
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("00011111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
        )
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("00111111", l_encoded)

    def testToAsciiChars_test5_decomposed(self) -> None:
        bits = bytearray(1)
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("00000000", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("00000001", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("00000011", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("00000111", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("00001111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        )
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("00011111", l_encoded)

    def testToAsciiChars_test4_decomposed(self) -> None:
        bits = bytearray(1)
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("00000000", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("00000001", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("00000011", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("00000111", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        l_encoded = "".join(self.instance.toAsciiChars(bits))
        self.assertEqual("00001111", l_encoded)

    def testToAsciiChars_test3_decomposed(self) -> None:
        bits = [0]  # Initialize a byte array with one element set to 0
        l_encoded = "".join(
            self.instance.toAsciiChars(bits)
        )  # Convert to ASCII chars and join into a string
        self.assertEqual(
            "00000000", l_encoded
        )  # Assert the result matches the expected string

        bits = [0]  # Reset the byte array
        bits[0] = self.__BIT_0  # Set the first bit
        l_encoded = "".join(
            self.instance.toAsciiChars(bits)
        )  # Convert to ASCII chars and join into a string
        self.assertEqual(
            "00000001", l_encoded
        )  # Assert the result matches the expected string

        bits = [0]  # Reset the byte array
        bits[0] = self.__BIT_0 | self.__BIT_1  # Set the first and second bits
        l_encoded = "".join(
            self.instance.toAsciiChars(bits)
        )  # Convert to ASCII chars and join into a string
        self.assertEqual(
            "00000011", l_encoded
        )  # Assert the result matches the expected string

        bits = [0]  # Reset the byte array
        bits[0] = (
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        )  # Set the first, second, and third bits
        l_encoded = "".join(
            self.instance.toAsciiChars(bits)
        )  # Convert to ASCII chars and join into a string
        self.assertEqual(
            "00000111", l_encoded
        )  # Assert the result matches the expected string

    def testToAsciiChars_test2_decomposed(self) -> None:
        bits = bytearray(1)  # Create a byte array of size 1
        l_encoded = "".join(
            self.instance.toAsciiChars(bits)
        )  # Convert to ASCII chars and join into a string
        self.assertEqual(
            "00000000", l_encoded
        )  # Assert the result matches the expected value

        bits = bytearray(1)  # Reset the byte array
        bits[0] = self.__BIT_0  # Set the first bit
        l_encoded = "".join(
            self.instance.toAsciiChars(bits)
        )  # Convert to ASCII chars and join into a string
        self.assertEqual(
            "00000001", l_encoded
        )  # Assert the result matches the expected value

        bits = bytearray(1)  # Reset the byte array
        bits[0] = self.__BIT_0 | self.__BIT_1  # Set the first and second bits
        l_encoded = "".join(
            self.instance.toAsciiChars(bits)
        )  # Convert to ASCII chars and join into a string
        self.assertEqual(
            "00000011", l_encoded
        )  # Assert the result matches the expected value

    def testToAsciiChars_test1_decomposed(self) -> None:
        bits = bytearray(1)  # Create a byte array of size 1, initialized to 0
        l_encoded = "".join(
            self.instance.toAsciiChars(bits)
        )  # Convert to ASCII chars and join into a string
        self.assertEqual(
            "00000000", l_encoded
        )  # Assert the result matches the expected string

        bits = bytearray(1)  # Reset the byte array
        bits[0] = self.__BIT_0  # Set the first bit to BIT_0 (0x01)
        l_encoded = "".join(
            self.instance.toAsciiChars(bits)
        )  # Convert to ASCII chars and join into a string
        # You can add further assertions here if needed

    def testToAsciiChars_test0_decomposed(self) -> None:
        bits = bytearray(1)  # Create a byte array of size 1
        l_encoded = "".join(
            self.instance.toAsciiChars(bits)
        )  # Convert the ASCII characters to a string

    def testToAsciiBytes_test26_decomposed(self) -> None:
        bits = bytearray(1)
        l_encoded = "".join(map(chr, BinaryCodec.toAsciiBytes(bits)))
        self.assertEqual("00000000", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0
        l_encoded = "".join(map(chr, BinaryCodec.toAsciiBytes(bits)))
        self.assertEqual("00000001", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1
        l_encoded = "".join(map(chr, BinaryCodec.toAsciiBytes(bits)))
        self.assertEqual("00000011", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        l_encoded = "".join(map(chr, BinaryCodec.toAsciiBytes(bits)))
        self.assertEqual("00000111", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        l_encoded = "".join(map(chr, BinaryCodec.toAsciiBytes(bits)))
        self.assertEqual("00001111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        )
        l_encoded = "".join(map(chr, BinaryCodec.toAsciiBytes(bits)))
        self.assertEqual("00011111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
        )
        l_encoded = "".join(map(chr, BinaryCodec.toAsciiBytes(bits)))
        self.assertEqual("00111111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
        )
        l_encoded = "".join(map(chr, BinaryCodec.toAsciiBytes(bits)))
        self.assertEqual("01111111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        l_encoded = "".join(map(chr, BinaryCodec.toAsciiBytes(bits)))
        self.assertEqual("11111111", l_encoded)

        bits = bytearray(2)
        l_encoded = "".join(map(chr, BinaryCodec.toAsciiBytes(bits)))
        self.assertEqual("0000000000000000", l_encoded)

        bits = bytearray(2)
        bits[0] = self.__BIT_0
        l_encoded = "".join(map(chr, BinaryCodec.toAsciiBytes(bits)))
        self.assertEqual("0000000000000001", l_encoded)

        bits = bytearray(2)
        bits[0] = self.__BIT_0 | self.__BIT_1
        l_encoded = "".join(map(chr, BinaryCodec.toAsciiBytes(bits)))
        self.assertEqual("0000000000000011", l_encoded)

        bits = bytearray(2)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        l_encoded = "".join(map(chr, BinaryCodec.toAsciiBytes(bits)))
        self.assertEqual("0000000000000111", l_encoded)

        bits = bytearray(2)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        l_encoded = "".join(map(chr, BinaryCodec.toAsciiBytes(bits)))
        self.assertEqual("0000000000001111", l_encoded)

        bits = bytearray(2)
        bits[0] = (
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        )
        l_encoded = "".join(map(chr, BinaryCodec.toAsciiBytes(bits)))
        self.assertEqual("0000000000011111", l_encoded)

        bits = bytearray(2)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
        )
        l_encoded = "".join(map(chr, BinaryCodec.toAsciiBytes(bits)))
        self.assertEqual("0000000000111111", l_encoded)

        bits = bytearray(2)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
        )
        l_encoded = "".join(map(chr, BinaryCodec.toAsciiBytes(bits)))
        self.assertEqual("0000000001111111", l_encoded)

        bits = bytearray(2)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        l_encoded = "".join(map(chr, BinaryCodec.toAsciiBytes(bits)))
        self.assertEqual("0000000011111111", l_encoded)

        bits = bytearray(2)
        bits[1] = self.__BIT_0
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        l_encoded = "".join(map(chr, BinaryCodec.toAsciiBytes(bits)))
        self.assertEqual("0000000111111111", l_encoded)

        bits = bytearray(2)
        bits[1] = self.__BIT_0 | self.__BIT_1
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        l_encoded = "".join(map(chr, BinaryCodec.toAsciiBytes(bits)))
        self.assertEqual("0000001111111111", l_encoded)

        bits = bytearray(2)
        bits[1] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        l_encoded = "".join(map(chr, BinaryCodec.toAsciiBytes(bits)))
        self.assertEqual("0000011111111111", l_encoded)

        bits = bytearray(2)
        bits[1] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        l_encoded = "".join(map(chr, BinaryCodec.toAsciiBytes(bits)))
        self.assertEqual("0000111111111111", l_encoded)

        bits = bytearray(2)
        bits[1] = (
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        )
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        l_encoded = "".join(map(chr, BinaryCodec.toAsciiBytes(bits)))
        self.assertEqual("0001111111111111", l_encoded)

        bits = bytearray(2)
        bits[1] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
        )
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        l_encoded = "".join(map(chr, BinaryCodec.toAsciiBytes(bits)))
        self.assertEqual("0011111111111111", l_encoded)

        bits = bytearray(2)
        bits[1] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
        )
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        l_encoded = "".join(map(chr, BinaryCodec.toAsciiBytes(bits)))
        self.assertEqual("0111111111111111", l_encoded)

        bits = bytearray(2)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        bits[1] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        l_encoded = "".join(map(chr, BinaryCodec.toAsciiBytes(bits)))
        self.assertEqual("1111111111111111", l_encoded)

        self.assertEqual(0, len(BinaryCodec.toAsciiBytes(None)))

    def testToAsciiBytes_test25_decomposed(self) -> None:
        bits = bytearray(1)
        l_encoded = "".join(map(chr, self.instance.toAsciiBytes(bits)))
        self.assertEqual("00000000", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0
        l_encoded = "".join(map(chr, self.instance.toAsciiBytes(bits)))
        self.assertEqual("00000001", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1
        l_encoded = "".join(map(chr, self.instance.toAsciiBytes(bits)))
        self.assertEqual("00000011", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        l_encoded = "".join(map(chr, self.instance.toAsciiBytes(bits)))
        self.assertEqual("00000111", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        l_encoded = "".join(map(chr, self.instance.toAsciiBytes(bits)))
        self.assertEqual("00001111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        )
        l_encoded = "".join(map(chr, self.instance.toAsciiBytes(bits)))
        self.assertEqual("00011111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
        )
        l_encoded = "".join(map(chr, self.instance.toAsciiBytes(bits)))
        self.assertEqual("00111111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
        )
        l_encoded = "".join(map(chr, self.instance.toAsciiBytes(bits)))
        self.assertEqual("01111111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        l_encoded = "".join(map(chr, self.instance.toAsciiBytes(bits)))
        self.assertEqual("11111111", l_encoded)

        bits = bytearray(2)
        l_encoded = "".join(map(chr, self.instance.toAsciiBytes(bits)))
        self.assertEqual("0000000000000000", l_encoded)

        bits = bytearray(2)
        bits[0] = self.__BIT_0
        l_encoded = "".join(map(chr, self.instance.toAsciiBytes(bits)))
        self.assertEqual("0000000000000001", l_encoded)

        bits = bytearray(2)
        bits[0] = self.__BIT_0 | self.__BIT_1
        l_encoded = "".join(map(chr, self.instance.toAsciiBytes(bits)))
        self.assertEqual("0000000000000011", l_encoded)

        bits = bytearray(2)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        l_encoded = "".join(map(chr, self.instance.toAsciiBytes(bits)))
        self.assertEqual("0000000000000111", l_encoded)

        bits = bytearray(2)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        l_encoded = "".join(map(chr, self.instance.toAsciiBytes(bits)))
        self.assertEqual("0000000000001111", l_encoded)

        bits = bytearray(2)
        bits[0] = (
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        )
        l_encoded = "".join(map(chr, self.instance.toAsciiBytes(bits)))
        self.assertEqual("0000000000011111", l_encoded)

        bits = bytearray(2)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
        )
        l_encoded = "".join(map(chr, self.instance.toAsciiBytes(bits)))
        self.assertEqual("0000000000111111", l_encoded)

        bits = bytearray(2)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
        )
        l_encoded = "".join(map(chr, self.instance.toAsciiBytes(bits)))
        self.assertEqual("0000000001111111", l_encoded)

        bits = bytearray(2)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        l_encoded = "".join(map(chr, self.instance.toAsciiBytes(bits)))
        self.assertEqual("0000000011111111", l_encoded)

        bits = bytearray(2)
        bits[1] = self.__BIT_0
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        l_encoded = "".join(map(chr, self.instance.toAsciiBytes(bits)))
        self.assertEqual("0000000111111111", l_encoded)

        bits = bytearray(2)
        bits[1] = self.__BIT_0 | self.__BIT_1
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        l_encoded = "".join(map(chr, self.instance.toAsciiBytes(bits)))
        self.assertEqual("0000001111111111", l_encoded)

        bits = bytearray(2)
        bits[1] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        l_encoded = "".join(map(chr, self.instance.toAsciiBytes(bits)))
        self.assertEqual("0000011111111111", l_encoded)

        bits = bytearray(2)
        bits[1] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        l_encoded = "".join(map(chr, self.instance.toAsciiBytes(bits)))
        self.assertEqual("0000111111111111", l_encoded)

        bits = bytearray(2)
        bits[1] = (
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        )
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        l_encoded = "".join(map(chr, self.instance.toAsciiBytes(bits)))
        self.assertEqual("0001111111111111", l_encoded)

        bits = bytearray(2)
        bits[1] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
        )
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        l_encoded = "".join(map(chr, self.instance.toAsciiBytes(bits)))
        self.assertEqual("0011111111111111", l_encoded)

        bits = bytearray(2)
        bits[1] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
        )
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        l_encoded = "".join(map(chr, self.instance.toAsciiBytes(bits)))
        self.assertEqual("0111111111111111", l_encoded)

        bits = bytearray(2)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        bits[1] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        l_encoded = "".join(map(chr, self.instance.toAsciiBytes(bits)))
        self.assertEqual("1111111111111111", l_encoded)

    def testToAsciiBytes_test24_decomposed(self) -> None:
        bits = bytearray(1)
        l_encoded = "".join(map(chr, BinaryCodec.toAsciiBytes(bits)))
        self.assertEqual("00000000", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0
        l_encoded = "".join(map(chr, BinaryCodec.toAsciiBytes(bits)))
        self.assertEqual("00000001", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1
        l_encoded = "".join(map(chr, BinaryCodec.toAsciiBytes(bits)))
        self.assertEqual("00000011", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        l_encoded = "".join(map(chr, BinaryCodec.toAsciiBytes(bits)))
        self.assertEqual("00000111", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        l_encoded = "".join(map(chr, BinaryCodec.toAsciiBytes(bits)))
        self.assertEqual("00001111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        )
        l_encoded = "".join(map(chr, BinaryCodec.toAsciiBytes(bits)))
        self.assertEqual("00011111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
        )
        l_encoded = "".join(map(chr, BinaryCodec.toAsciiBytes(bits)))
        self.assertEqual("00111111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
        )
        l_encoded = "".join(map(chr, BinaryCodec.toAsciiBytes(bits)))
        self.assertEqual("01111111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        l_encoded = "".join(map(chr, BinaryCodec.toAsciiBytes(bits)))
        self.assertEqual("11111111", l_encoded)

        bits = bytearray(2)
        l_encoded = "".join(map(chr, BinaryCodec.toAsciiBytes(bits)))
        self.assertEqual("0000000000000000", l_encoded)

        bits = bytearray(2)
        bits[0] = self.__BIT_0
        l_encoded = "".join(map(chr, BinaryCodec.toAsciiBytes(bits)))
        self.assertEqual("0000000000000001", l_encoded)

        bits = bytearray(2)
        bits[0] = self.__BIT_0 | self.__BIT_1
        l_encoded = "".join(map(chr, BinaryCodec.toAsciiBytes(bits)))
        self.assertEqual("0000000000000011", l_encoded)

        bits = bytearray(2)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        l_encoded = "".join(map(chr, BinaryCodec.toAsciiBytes(bits)))
        self.assertEqual("0000000000000111", l_encoded)

        bits = bytearray(2)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        l_encoded = "".join(map(chr, BinaryCodec.toAsciiBytes(bits)))
        self.assertEqual("0000000000001111", l_encoded)

        bits = bytearray(2)
        bits[0] = (
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        )
        l_encoded = "".join(map(chr, BinaryCodec.toAsciiBytes(bits)))
        self.assertEqual("0000000000011111", l_encoded)

        bits = bytearray(2)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
        )
        l_encoded = "".join(map(chr, BinaryCodec.toAsciiBytes(bits)))
        self.assertEqual("0000000000111111", l_encoded)

        bits = bytearray(2)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
        )
        l_encoded = "".join(map(chr, BinaryCodec.toAsciiBytes(bits)))
        self.assertEqual("0000000001111111", l_encoded)

        bits = bytearray(2)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        l_encoded = "".join(map(chr, BinaryCodec.toAsciiBytes(bits)))
        self.assertEqual("0000000011111111", l_encoded)

        bits = bytearray(2)
        bits[1] = self.__BIT_0
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        l_encoded = "".join(map(chr, BinaryCodec.toAsciiBytes(bits)))
        self.assertEqual("0000000111111111", l_encoded)

        bits = bytearray(2)
        bits[1] = self.__BIT_0 | self.__BIT_1
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        l_encoded = "".join(map(chr, BinaryCodec.toAsciiBytes(bits)))
        self.assertEqual("0000001111111111", l_encoded)

        bits = bytearray(2)
        bits[1] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        l_encoded = "".join(map(chr, BinaryCodec.toAsciiBytes(bits)))
        self.assertEqual("0000011111111111", l_encoded)

        bits = bytearray(2)
        bits[1] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        l_encoded = "".join(map(chr, BinaryCodec.toAsciiBytes(bits)))
        self.assertEqual("0000111111111111", l_encoded)

        bits = bytearray(2)
        bits[1] = (
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        )
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        l_encoded = "".join(map(chr, BinaryCodec.toAsciiBytes(bits)))
        self.assertEqual("0001111111111111", l_encoded)

        bits = bytearray(2)
        bits[1] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
        )
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        l_encoded = "".join(map(chr, BinaryCodec.toAsciiBytes(bits)))
        self.assertEqual("0011111111111111", l_encoded)

        bits = bytearray(2)
        bits[1] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
        )
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        l_encoded = "".join(map(chr, BinaryCodec.toAsciiBytes(bits)))
        self.assertEqual("0111111111111111", l_encoded)

    def testToAsciiBytes_test23_decomposed(self) -> None:
        bits = bytearray(1)
        l_encoded = "".join(map(chr, self.instance.toAsciiBytes(bits)))
        self.assertEqual("00000000", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0
        l_encoded = "".join(map(chr, self.instance.toAsciiBytes(bits)))
        self.assertEqual("00000001", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1
        l_encoded = "".join(map(chr, self.instance.toAsciiBytes(bits)))
        self.assertEqual("00000011", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        l_encoded = "".join(map(chr, self.instance.toAsciiBytes(bits)))
        self.assertEqual("00000111", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        l_encoded = "".join(map(chr, self.instance.toAsciiBytes(bits)))
        self.assertEqual("00001111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        )
        l_encoded = "".join(map(chr, self.instance.toAsciiBytes(bits)))
        self.assertEqual("00011111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
        )
        l_encoded = "".join(map(chr, self.instance.toAsciiBytes(bits)))
        self.assertEqual("00111111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
        )
        l_encoded = "".join(map(chr, self.instance.toAsciiBytes(bits)))
        self.assertEqual("01111111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        l_encoded = "".join(map(chr, self.instance.toAsciiBytes(bits)))
        self.assertEqual("11111111", l_encoded)

        bits = bytearray(2)
        l_encoded = "".join(map(chr, self.instance.toAsciiBytes(bits)))
        self.assertEqual("0000000000000000", l_encoded)

        bits = bytearray(2)
        bits[0] = self.__BIT_0
        l_encoded = "".join(map(chr, self.instance.toAsciiBytes(bits)))
        self.assertEqual("0000000000000001", l_encoded)

        bits = bytearray(2)
        bits[0] = self.__BIT_0 | self.__BIT_1
        l_encoded = "".join(map(chr, self.instance.toAsciiBytes(bits)))
        self.assertEqual("0000000000000011", l_encoded)

        bits = bytearray(2)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        l_encoded = "".join(map(chr, self.instance.toAsciiBytes(bits)))
        self.assertEqual("0000000000000111", l_encoded)

        bits = bytearray(2)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        l_encoded = "".join(map(chr, self.instance.toAsciiBytes(bits)))
        self.assertEqual("0000000000001111", l_encoded)

        bits = bytearray(2)
        bits[0] = (
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        )
        l_encoded = "".join(map(chr, self.instance.toAsciiBytes(bits)))
        self.assertEqual("0000000000011111", l_encoded)

        bits = bytearray(2)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
        )
        l_encoded = "".join(map(chr, self.instance.toAsciiBytes(bits)))
        self.assertEqual("0000000000111111", l_encoded)

        bits = bytearray(2)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
        )
        l_encoded = "".join(map(chr, self.instance.toAsciiBytes(bits)))
        self.assertEqual("0000000001111111", l_encoded)

        bits = bytearray(2)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        l_encoded = "".join(map(chr, self.instance.toAsciiBytes(bits)))
        self.assertEqual("0000000011111111", l_encoded)

        bits = bytearray(2)
        bits[1] = self.__BIT_0
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        l_encoded = "".join(map(chr, self.instance.toAsciiBytes(bits)))
        self.assertEqual("0000000111111111", l_encoded)

        bits = bytearray(2)
        bits[1] = self.__BIT_0 | self.__BIT_1
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        l_encoded = "".join(map(chr, self.instance.toAsciiBytes(bits)))
        self.assertEqual("0000001111111111", l_encoded)

        bits = bytearray(2)
        bits[1] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        l_encoded = "".join(map(chr, self.instance.toAsciiBytes(bits)))
        self.assertEqual("0000011111111111", l_encoded)

        bits = bytearray(2)
        bits[1] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        l_encoded = "".join(map(chr, self.instance.toAsciiBytes(bits)))
        self.assertEqual("0000111111111111", l_encoded)

        bits = bytearray(2)
        bits[1] = (
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        )
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        l_encoded = "".join(map(chr, self.instance.toAsciiBytes(bits)))
        self.assertEqual("0001111111111111", l_encoded)

        bits = bytearray(2)
        bits[1] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
        )
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        l_encoded = "".join(map(chr, self.instance.toAsciiBytes(bits)))
        self.assertEqual("0001111111111111", l_encoded)

    def testToAsciiBytes_test22_decomposed(self) -> None:
        bits = bytearray(1)
        l_encoded = "".join(map(chr, BinaryCodec.toAsciiBytes(bits)))
        self.assertEqual("00000000", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0
        l_encoded = "".join(map(chr, BinaryCodec.toAsciiBytes(bits)))
        self.assertEqual("00000001", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1
        l_encoded = "".join(map(chr, BinaryCodec.toAsciiBytes(bits)))
        self.assertEqual("00000011", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        l_encoded = "".join(map(chr, BinaryCodec.toAsciiBytes(bits)))
        self.assertEqual("00000111", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        l_encoded = "".join(map(chr, BinaryCodec.toAsciiBytes(bits)))
        self.assertEqual("00001111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        )
        l_encoded = "".join(map(chr, BinaryCodec.toAsciiBytes(bits)))
        self.assertEqual("00011111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
        )
        l_encoded = "".join(map(chr, BinaryCodec.toAsciiBytes(bits)))
        self.assertEqual("00111111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
        )
        l_encoded = "".join(map(chr, BinaryCodec.toAsciiBytes(bits)))
        self.assertEqual("01111111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        l_encoded = "".join(map(chr, BinaryCodec.toAsciiBytes(bits)))
        self.assertEqual("11111111", l_encoded)

        bits = bytearray(2)
        l_encoded = "".join(map(chr, BinaryCodec.toAsciiBytes(bits)))
        self.assertEqual("0000000000000000", l_encoded)

        bits = bytearray(2)
        bits[0] = self.__BIT_0
        l_encoded = "".join(map(chr, BinaryCodec.toAsciiBytes(bits)))
        self.assertEqual("0000000000000001", l_encoded)

        bits = bytearray(2)
        bits[0] = self.__BIT_0 | self.__BIT_1
        l_encoded = "".join(map(chr, BinaryCodec.toAsciiBytes(bits)))
        self.assertEqual("0000000000000011", l_encoded)

        bits = bytearray(2)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        l_encoded = "".join(map(chr, BinaryCodec.toAsciiBytes(bits)))
        self.assertEqual("0000000000000111", l_encoded)

        bits = bytearray(2)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        l_encoded = "".join(map(chr, BinaryCodec.toAsciiBytes(bits)))
        self.assertEqual("0000000000001111", l_encoded)

        bits = bytearray(2)
        bits[0] = (
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        )
        l_encoded = "".join(map(chr, BinaryCodec.toAsciiBytes(bits)))
        self.assertEqual("0000000000011111", l_encoded)

        bits = bytearray(2)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
        )
        l_encoded = "".join(map(chr, BinaryCodec.toAsciiBytes(bits)))
        self.assertEqual("0000000000111111", l_encoded)

        bits = bytearray(2)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
        )
        l_encoded = "".join(map(chr, BinaryCodec.toAsciiBytes(bits)))
        self.assertEqual("0000000001111111", l_encoded)

        bits = bytearray(2)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        l_encoded = "".join(map(chr, BinaryCodec.toAsciiBytes(bits)))
        self.assertEqual("0000000011111111", l_encoded)

        bits = bytearray(2)
        bits[1] = self.__BIT_0
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        l_encoded = "".join(map(chr, BinaryCodec.toAsciiBytes(bits)))
        self.assertEqual("0000000111111111", l_encoded)

        bits = bytearray(2)
        bits[1] = self.__BIT_0 | self.__BIT_1
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        l_encoded = "".join(map(chr, BinaryCodec.toAsciiBytes(bits)))
        self.assertEqual("0000001111111111", l_encoded)

        bits = bytearray(2)
        bits[1] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        l_encoded = "".join(map(chr, BinaryCodec.toAsciiBytes(bits)))
        self.assertEqual("0000011111111111", l_encoded)

        bits = bytearray(2)
        bits[1] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        l_encoded = "".join(map(chr, BinaryCodec.toAsciiBytes(bits)))
        self.assertEqual("0000111111111111", l_encoded)

        bits = bytearray(2)
        bits[1] = (
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        )
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        l_encoded = "".join(map(chr, BinaryCodec.toAsciiBytes(bits)))
        self.assertEqual("0001111111111111", l_encoded)

    def testToAsciiBytes_test21_decomposed(self) -> None:
        bits = bytearray(1)
        l_encoded = "".join(map(chr, BinaryCodec.toAsciiBytes(bits)))
        self.assertEqual("00000000", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0
        l_encoded = "".join(map(chr, BinaryCodec.toAsciiBytes(bits)))
        self.assertEqual("00000001", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1
        l_encoded = "".join(map(chr, BinaryCodec.toAsciiBytes(bits)))
        self.assertEqual("00000011", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        l_encoded = "".join(map(chr, BinaryCodec.toAsciiBytes(bits)))
        self.assertEqual("00000111", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        l_encoded = "".join(map(chr, BinaryCodec.toAsciiBytes(bits)))
        self.assertEqual("00001111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        )
        l_encoded = "".join(map(chr, BinaryCodec.toAsciiBytes(bits)))
        self.assertEqual("00011111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
        )
        l_encoded = "".join(map(chr, BinaryCodec.toAsciiBytes(bits)))
        self.assertEqual("00111111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
        )
        l_encoded = "".join(map(chr, BinaryCodec.toAsciiBytes(bits)))
        self.assertEqual("01111111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        l_encoded = "".join(map(chr, BinaryCodec.toAsciiBytes(bits)))
        self.assertEqual("11111111", l_encoded)

        bits = bytearray(2)
        l_encoded = "".join(map(chr, BinaryCodec.toAsciiBytes(bits)))
        self.assertEqual("0000000000000000", l_encoded)

        bits = bytearray(2)
        bits[0] = self.__BIT_0
        l_encoded = "".join(map(chr, BinaryCodec.toAsciiBytes(bits)))
        self.assertEqual("0000000000000001", l_encoded)

        bits = bytearray(2)
        bits[0] = self.__BIT_0 | self.__BIT_1
        l_encoded = "".join(map(chr, BinaryCodec.toAsciiBytes(bits)))
        self.assertEqual("0000000000000011", l_encoded)

        bits = bytearray(2)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        l_encoded = "".join(map(chr, BinaryCodec.toAsciiBytes(bits)))
        self.assertEqual("0000000000000111", l_encoded)

        bits = bytearray(2)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        l_encoded = "".join(map(chr, BinaryCodec.toAsciiBytes(bits)))
        self.assertEqual("0000000000001111", l_encoded)

        bits = bytearray(2)
        bits[0] = (
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        )
        l_encoded = "".join(map(chr, BinaryCodec.toAsciiBytes(bits)))
        self.assertEqual("0000000000011111", l_encoded)

        bits = bytearray(2)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
        )
        l_encoded = "".join(map(chr, BinaryCodec.toAsciiBytes(bits)))
        self.assertEqual("0000000000111111", l_encoded)

        bits = bytearray(2)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
        )
        l_encoded = "".join(map(chr, BinaryCodec.toAsciiBytes(bits)))
        self.assertEqual("0000000001111111", l_encoded)

        bits = bytearray(2)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        l_encoded = "".join(map(chr, BinaryCodec.toAsciiBytes(bits)))
        self.assertEqual("0000000011111111", l_encoded)

        bits = bytearray(2)
        bits[1] = self.__BIT_0
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        l_encoded = "".join(map(chr, BinaryCodec.toAsciiBytes(bits)))
        self.assertEqual("0000000111111111", l_encoded)

        bits = bytearray(2)
        bits[1] = self.__BIT_0 | self.__BIT_1
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        l_encoded = "".join(map(chr, BinaryCodec.toAsciiBytes(bits)))
        self.assertEqual("0000001111111111", l_encoded)

        bits = bytearray(2)
        bits[1] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        l_encoded = "".join(map(chr, BinaryCodec.toAsciiBytes(bits)))
        self.assertEqual("0000011111111111", l_encoded)

        bits = bytearray(2)
        bits[1] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        l_encoded = "".join(map(chr, BinaryCodec.toAsciiBytes(bits)))
        self.assertEqual("0000111111111111", l_encoded)

    def testToAsciiBytes_test20_decomposed(self) -> None:
        bits = bytearray(1)
        l_encoded = "".join(map(chr, BinaryCodec.toAsciiBytes(bits)))
        self.assertEqual("00000000", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0
        l_encoded = "".join(map(chr, BinaryCodec.toAsciiBytes(bits)))
        self.assertEqual("00000001", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1
        l_encoded = "".join(map(chr, BinaryCodec.toAsciiBytes(bits)))
        self.assertEqual("00000011", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        l_encoded = "".join(map(chr, BinaryCodec.toAsciiBytes(bits)))
        self.assertEqual("00000111", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        l_encoded = "".join(map(chr, BinaryCodec.toAsciiBytes(bits)))
        self.assertEqual("00001111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        )
        l_encoded = "".join(map(chr, BinaryCodec.toAsciiBytes(bits)))
        self.assertEqual("00011111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
        )
        l_encoded = "".join(map(chr, BinaryCodec.toAsciiBytes(bits)))
        self.assertEqual("00111111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
        )
        l_encoded = "".join(map(chr, BinaryCodec.toAsciiBytes(bits)))
        self.assertEqual("01111111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        l_encoded = "".join(map(chr, BinaryCodec.toAsciiBytes(bits)))
        self.assertEqual("11111111", l_encoded)

        bits = bytearray(2)
        l_encoded = "".join(map(chr, BinaryCodec.toAsciiBytes(bits)))
        self.assertEqual("0000000000000000", l_encoded)

        bits = bytearray(2)
        bits[0] = self.__BIT_0
        l_encoded = "".join(map(chr, BinaryCodec.toAsciiBytes(bits)))
        self.assertEqual("0000000000000001", l_encoded)

        bits = bytearray(2)
        bits[0] = self.__BIT_0 | self.__BIT_1
        l_encoded = "".join(map(chr, BinaryCodec.toAsciiBytes(bits)))
        self.assertEqual("0000000000000011", l_encoded)

        bits = bytearray(2)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        l_encoded = "".join(map(chr, BinaryCodec.toAsciiBytes(bits)))
        self.assertEqual("0000000000000111", l_encoded)

        bits = bytearray(2)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        l_encoded = "".join(map(chr, BinaryCodec.toAsciiBytes(bits)))
        self.assertEqual("0000000000001111", l_encoded)

        bits = bytearray(2)
        bits[0] = (
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        )
        l_encoded = "".join(map(chr, BinaryCodec.toAsciiBytes(bits)))
        self.assertEqual("0000000000011111", l_encoded)

        bits = bytearray(2)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
        )
        l_encoded = "".join(map(chr, BinaryCodec.toAsciiBytes(bits)))
        self.assertEqual("0000000000111111", l_encoded)

        bits = bytearray(2)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
        )
        l_encoded = "".join(map(chr, BinaryCodec.toAsciiBytes(bits)))
        self.assertEqual("0000000001111111", l_encoded)

        bits = bytearray(2)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        l_encoded = "".join(map(chr, BinaryCodec.toAsciiBytes(bits)))
        self.assertEqual("0000000011111111", l_encoded)

        bits = bytearray(2)
        bits[1] = self.__BIT_0
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        l_encoded = "".join(map(chr, BinaryCodec.toAsciiBytes(bits)))
        self.assertEqual("0000000111111111", l_encoded)

        bits = bytearray(2)
        bits[1] = self.__BIT_0 | self.__BIT_1
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        l_encoded = "".join(map(chr, BinaryCodec.toAsciiBytes(bits)))
        self.assertEqual("0000001111111111", l_encoded)

        bits = bytearray(2)
        bits[1] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        l_encoded = "".join(map(chr, BinaryCodec.toAsciiBytes(bits)))
        self.assertEqual("0000011111111111", l_encoded)

    def testToAsciiBytes_test19_decomposed(self) -> None:
        bits = [0]
        l_encoded = "".join(map(chr, self.instance.toAsciiBytes(bits)))
        self.assertEqual("00000000", l_encoded)

        bits = [self.__BIT_0]
        l_encoded = "".join(map(chr, self.instance.toAsciiBytes(bits)))
        self.assertEqual("00000001", l_encoded)

        bits = [self.__BIT_0 | self.__BIT_1]
        l_encoded = "".join(map(chr, self.instance.toAsciiBytes(bits)))
        self.assertEqual("00000011", l_encoded)

        bits = [self.__BIT_0 | self.__BIT_1 | self.__BIT_2]
        l_encoded = "".join(map(chr, self.instance.toAsciiBytes(bits)))
        self.assertEqual("00000111", l_encoded)

        bits = [self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3]
        l_encoded = "".join(map(chr, self.instance.toAsciiBytes(bits)))
        self.assertEqual("00001111", l_encoded)

        bits = [
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        ]
        l_encoded = "".join(map(chr, self.instance.toAsciiBytes(bits)))
        self.assertEqual("00011111", l_encoded)

        bits = [
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
        ]
        l_encoded = "".join(map(chr, self.instance.toAsciiBytes(bits)))
        self.assertEqual("00111111", l_encoded)

        bits = [
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
        ]
        l_encoded = "".join(map(chr, self.instance.toAsciiBytes(bits)))
        self.assertEqual("01111111", l_encoded)

        bits = [
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        ]
        l_encoded = "".join(map(chr, self.instance.toAsciiBytes(bits)))
        self.assertEqual("11111111", l_encoded)

        bits = [0, 0]
        l_encoded = "".join(map(chr, self.instance.toAsciiBytes(bits)))
        self.assertEqual("0000000000000000", l_encoded)

        bits = [self.__BIT_0, 0]
        l_encoded = "".join(map(chr, self.instance.toAsciiBytes(bits)))
        self.assertEqual("0000000000000001", l_encoded)

        bits = [self.__BIT_0 | self.__BIT_1, 0]
        l_encoded = "".join(map(chr, self.instance.toAsciiBytes(bits)))
        self.assertEqual("0000000000000011", l_encoded)

        bits = [self.__BIT_0 | self.__BIT_1 | self.__BIT_2, 0]
        l_encoded = "".join(map(chr, self.instance.toAsciiBytes(bits)))
        self.assertEqual("0000000000000111", l_encoded)

        bits = [self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3, 0]
        l_encoded = "".join(map(chr, self.instance.toAsciiBytes(bits)))
        self.assertEqual("0000000000001111", l_encoded)

        bits = [
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4,
            0,
        ]
        l_encoded = "".join(map(chr, self.instance.toAsciiBytes(bits)))
        self.assertEqual("0000000000011111", l_encoded)

        bits = [
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5,
            0,
        ]
        l_encoded = "".join(map(chr, self.instance.toAsciiBytes(bits)))
        self.assertEqual("0000000000111111", l_encoded)

        bits = [
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6,
            0,
        ]
        l_encoded = "".join(map(chr, self.instance.toAsciiBytes(bits)))
        self.assertEqual("0000000001111111", l_encoded)

        bits = [
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7,
            0,
        ]
        l_encoded = "".join(map(chr, self.instance.toAsciiBytes(bits)))
        self.assertEqual("0000000011111111", l_encoded)

        bits = [
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7,
            self.__BIT_0,
        ]
        l_encoded = "".join(map(chr, self.instance.toAsciiBytes(bits)))
        self.assertEqual("0000000111111111", l_encoded)

        bits = [
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7,
            self.__BIT_0 | self.__BIT_1,
        ]
        l_encoded = "".join(map(chr, self.instance.toAsciiBytes(bits)))
        self.assertEqual("0000001111111111", l_encoded)

    def testToAsciiBytes_test18_decomposed(self) -> None:
        bits = [0]
        l_encoded = "".join(map(chr, BinaryCodec.toAsciiBytes(bits)))
        self.assertEqual("00000000", l_encoded)

        bits = [self.__BIT_0]
        l_encoded = "".join(map(chr, BinaryCodec.toAsciiBytes(bits)))
        self.assertEqual("00000001", l_encoded)

        bits = [self.__BIT_0 | self.__BIT_1]
        l_encoded = "".join(map(chr, BinaryCodec.toAsciiBytes(bits)))
        self.assertEqual("00000011", l_encoded)

        bits = [self.__BIT_0 | self.__BIT_1 | self.__BIT_2]
        l_encoded = "".join(map(chr, BinaryCodec.toAsciiBytes(bits)))
        self.assertEqual("00000111", l_encoded)

        bits = [self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3]
        l_encoded = "".join(map(chr, BinaryCodec.toAsciiBytes(bits)))
        self.assertEqual("00001111", l_encoded)

        bits = [
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        ]
        l_encoded = "".join(map(chr, BinaryCodec.toAsciiBytes(bits)))
        self.assertEqual("00011111", l_encoded)

        bits = [
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
        ]
        l_encoded = "".join(map(chr, BinaryCodec.toAsciiBytes(bits)))
        self.assertEqual("00111111", l_encoded)

        bits = [
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
        ]
        l_encoded = "".join(map(chr, BinaryCodec.toAsciiBytes(bits)))
        self.assertEqual("01111111", l_encoded)

        bits = [
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        ]
        l_encoded = "".join(map(chr, BinaryCodec.toAsciiBytes(bits)))
        self.assertEqual("11111111", l_encoded)

        bits = [0, 0]
        l_encoded = "".join(map(chr, BinaryCodec.toAsciiBytes(bits)))
        self.assertEqual("0000000000000000", l_encoded)

        bits = [self.__BIT_0, 0]
        l_encoded = "".join(map(chr, BinaryCodec.toAsciiBytes(bits)))
        self.assertEqual("0000000000000001", l_encoded)

        bits = [self.__BIT_0 | self.__BIT_1, 0]
        l_encoded = "".join(map(chr, BinaryCodec.toAsciiBytes(bits)))
        self.assertEqual("0000000000000011", l_encoded)

        bits = [self.__BIT_0 | self.__BIT_1 | self.__BIT_2, 0]
        l_encoded = "".join(map(chr, BinaryCodec.toAsciiBytes(bits)))
        self.assertEqual("0000000000000111", l_encoded)

        bits = [self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3, 0]
        l_encoded = "".join(map(chr, BinaryCodec.toAsciiBytes(bits)))
        self.assertEqual("0000000000001111", l_encoded)

        bits = [
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4,
            0,
        ]
        l_encoded = "".join(map(chr, BinaryCodec.toAsciiBytes(bits)))
        self.assertEqual("0000000000011111", l_encoded)

        bits = [
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5,
            0,
        ]
        l_encoded = "".join(map(chr, BinaryCodec.toAsciiBytes(bits)))
        self.assertEqual("0000000000111111", l_encoded)

        bits = [
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6,
            0,
        ]
        l_encoded = "".join(map(chr, BinaryCodec.toAsciiBytes(bits)))
        self.assertEqual("0000000001111111", l_encoded)

        bits = [
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7,
            0,
        ]
        l_encoded = "".join(map(chr, BinaryCodec.toAsciiBytes(bits)))
        self.assertEqual("0000000011111111", l_encoded)

        bits = [
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7,
            self.__BIT_0,
        ]
        l_encoded = "".join(map(chr, BinaryCodec.toAsciiBytes(bits)))
        self.assertEqual("1111111100000001", l_encoded)

    def testToAsciiBytes_test17_decomposed(self) -> None:
        bits = bytearray(1)
        l_encoded = "".join(map(chr, BinaryCodec.toAsciiBytes(bits)))
        self.assertEqual("00000000", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0
        l_encoded = "".join(map(chr, BinaryCodec.toAsciiBytes(bits)))
        self.assertEqual("00000001", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1
        l_encoded = "".join(map(chr, BinaryCodec.toAsciiBytes(bits)))
        self.assertEqual("00000011", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        l_encoded = "".join(map(chr, BinaryCodec.toAsciiBytes(bits)))
        self.assertEqual("00000111", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        l_encoded = "".join(map(chr, BinaryCodec.toAsciiBytes(bits)))
        self.assertEqual("00001111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        )
        l_encoded = "".join(map(chr, BinaryCodec.toAsciiBytes(bits)))
        self.assertEqual("00011111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
        )
        l_encoded = "".join(map(chr, BinaryCodec.toAsciiBytes(bits)))
        self.assertEqual("00111111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
        )
        l_encoded = "".join(map(chr, BinaryCodec.toAsciiBytes(bits)))
        self.assertEqual("01111111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        l_encoded = "".join(map(chr, BinaryCodec.toAsciiBytes(bits)))
        self.assertEqual("11111111", l_encoded)

        bits = bytearray(2)
        l_encoded = "".join(map(chr, BinaryCodec.toAsciiBytes(bits)))
        self.assertEqual("0000000000000000", l_encoded)

        bits = bytearray(2)
        bits[0] = self.__BIT_0
        l_encoded = "".join(map(chr, BinaryCodec.toAsciiBytes(bits)))
        self.assertEqual("0000000000000001", l_encoded)

        bits = bytearray(2)
        bits[0] = self.__BIT_0 | self.__BIT_1
        l_encoded = "".join(map(chr, BinaryCodec.toAsciiBytes(bits)))
        self.assertEqual("0000000000000011", l_encoded)

        bits = bytearray(2)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        l_encoded = "".join(map(chr, BinaryCodec.toAsciiBytes(bits)))
        self.assertEqual("0000000000000111", l_encoded)

        bits = bytearray(2)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        l_encoded = "".join(map(chr, BinaryCodec.toAsciiBytes(bits)))
        self.assertEqual("0000000000001111", l_encoded)

        bits = bytearray(2)
        bits[0] = (
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        )
        l_encoded = "".join(map(chr, BinaryCodec.toAsciiBytes(bits)))
        self.assertEqual("0000000000011111", l_encoded)

        bits = bytearray(2)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
        )
        l_encoded = "".join(map(chr, BinaryCodec.toAsciiBytes(bits)))
        self.assertEqual("0000000000111111", l_encoded)

        bits = bytearray(2)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
        )
        l_encoded = "".join(map(chr, BinaryCodec.toAsciiBytes(bits)))
        self.assertEqual("0000000001111111", l_encoded)

        bits = bytearray(2)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        l_encoded = "".join(map(chr, BinaryCodec.toAsciiBytes(bits)))
        self.assertEqual("1111111111111111", l_encoded)

    def testToAsciiBytes_test16_decomposed(self) -> None:
        bits = bytearray(1)
        l_encoded = "".join(map(chr, BinaryCodec.toAsciiBytes(bits)))
        self.assertEqual("00000000", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0
        l_encoded = "".join(map(chr, BinaryCodec.toAsciiBytes(bits)))
        self.assertEqual("00000001", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1
        l_encoded = "".join(map(chr, BinaryCodec.toAsciiBytes(bits)))
        self.assertEqual("00000011", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        l_encoded = "".join(map(chr, BinaryCodec.toAsciiBytes(bits)))
        self.assertEqual("00000111", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        l_encoded = "".join(map(chr, BinaryCodec.toAsciiBytes(bits)))
        self.assertEqual("00001111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        )
        l_encoded = "".join(map(chr, BinaryCodec.toAsciiBytes(bits)))
        self.assertEqual("00011111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
        )
        l_encoded = "".join(map(chr, BinaryCodec.toAsciiBytes(bits)))
        self.assertEqual("00111111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
        )
        l_encoded = "".join(map(chr, BinaryCodec.toAsciiBytes(bits)))
        self.assertEqual("01111111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        l_encoded = "".join(map(chr, BinaryCodec.toAsciiBytes(bits)))
        self.assertEqual("11111111", l_encoded)

        bits = bytearray(2)
        l_encoded = "".join(map(chr, BinaryCodec.toAsciiBytes(bits)))
        self.assertEqual("0000000000000000", l_encoded)

        bits = bytearray(2)
        bits[0] = self.__BIT_0
        l_encoded = "".join(map(chr, BinaryCodec.toAsciiBytes(bits)))
        self.assertEqual("0000000000000001", l_encoded)

        bits = bytearray(2)
        bits[0] = self.__BIT_0 | self.__BIT_1
        l_encoded = "".join(map(chr, BinaryCodec.toAsciiBytes(bits)))
        self.assertEqual("0000000000000011", l_encoded)

        bits = bytearray(2)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        l_encoded = "".join(map(chr, BinaryCodec.toAsciiBytes(bits)))
        self.assertEqual("0000000000000111", l_encoded)

        bits = bytearray(2)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        l_encoded = "".join(map(chr, BinaryCodec.toAsciiBytes(bits)))
        self.assertEqual("0000000000001111", l_encoded)

        bits = bytearray(2)
        bits[0] = (
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        )
        l_encoded = "".join(map(chr, BinaryCodec.toAsciiBytes(bits)))
        self.assertEqual("0000000000011111", l_encoded)

        bits = bytearray(2)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
        )
        l_encoded = "".join(map(chr, BinaryCodec.toAsciiBytes(bits)))
        self.assertEqual("0000000000111111", l_encoded)

        bits = bytearray(2)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
        )
        l_encoded = "".join(map(chr, BinaryCodec.toAsciiBytes(bits)))
        self.assertEqual("0000000001111111", l_encoded)

    def testToAsciiBytes_test15_decomposed(self) -> None:
        bits = bytearray(1)
        l_encoded = "".join(map(chr, BinaryCodec.toAsciiBytes(bits)))
        self.assertEqual("00000000", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0
        l_encoded = "".join(map(chr, BinaryCodec.toAsciiBytes(bits)))
        self.assertEqual("00000001", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1
        l_encoded = "".join(map(chr, BinaryCodec.toAsciiBytes(bits)))
        self.assertEqual("00000011", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        l_encoded = "".join(map(chr, BinaryCodec.toAsciiBytes(bits)))
        self.assertEqual("00000111", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        l_encoded = "".join(map(chr, BinaryCodec.toAsciiBytes(bits)))
        self.assertEqual("00001111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        )
        l_encoded = "".join(map(chr, BinaryCodec.toAsciiBytes(bits)))
        self.assertEqual("00011111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
        )
        l_encoded = "".join(map(chr, BinaryCodec.toAsciiBytes(bits)))
        self.assertEqual("00111111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
        )
        l_encoded = "".join(map(chr, BinaryCodec.toAsciiBytes(bits)))
        self.assertEqual("01111111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        l_encoded = "".join(map(chr, BinaryCodec.toAsciiBytes(bits)))
        self.assertEqual("11111111", l_encoded)

        bits = bytearray(2)
        l_encoded = "".join(map(chr, BinaryCodec.toAsciiBytes(bits)))
        self.assertEqual("0000000000000000", l_encoded)

        bits = bytearray(2)
        bits[0] = self.__BIT_0
        l_encoded = "".join(map(chr, BinaryCodec.toAsciiBytes(bits)))
        self.assertEqual("0000000000000001", l_encoded)

        bits = bytearray(2)
        bits[0] = self.__BIT_0 | self.__BIT_1
        l_encoded = "".join(map(chr, BinaryCodec.toAsciiBytes(bits)))
        self.assertEqual("0000000000000011", l_encoded)

        bits = bytearray(2)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        l_encoded = "".join(map(chr, BinaryCodec.toAsciiBytes(bits)))
        self.assertEqual("0000000000000111", l_encoded)

        bits = bytearray(2)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        l_encoded = "".join(map(chr, BinaryCodec.toAsciiBytes(bits)))
        self.assertEqual("0000000000001111", l_encoded)

        bits = bytearray(2)
        bits[0] = (
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        )
        l_encoded = "".join(map(chr, BinaryCodec.toAsciiBytes(bits)))
        self.assertEqual("0000000000011111", l_encoded)

        bits = bytearray(2)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
        )
        l_encoded = "".join(map(chr, BinaryCodec.toAsciiBytes(bits)))
        self.assertEqual("0000000000111111", l_encoded)

    def testToAsciiBytes_test14_decomposed(self) -> None:
        bits = [0]
        l_encoded = "".join(map(chr, BinaryCodec.toAsciiBytes(bits)))
        self.assertEqual("00000000", l_encoded)

        bits = [self.__BIT_0]
        l_encoded = "".join(map(chr, BinaryCodec.toAsciiBytes(bits)))
        self.assertEqual("00000001", l_encoded)

        bits = [self.__BIT_0 | self.__BIT_1]
        l_encoded = "".join(map(chr, BinaryCodec.toAsciiBytes(bits)))
        self.assertEqual("00000011", l_encoded)

        bits = [self.__BIT_0 | self.__BIT_1 | self.__BIT_2]
        l_encoded = "".join(map(chr, BinaryCodec.toAsciiBytes(bits)))
        self.assertEqual("00000111", l_encoded)

        bits = [self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3]
        l_encoded = "".join(map(chr, BinaryCodec.toAsciiBytes(bits)))
        self.assertEqual("00001111", l_encoded)

        bits = [
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        ]
        l_encoded = "".join(map(chr, BinaryCodec.toAsciiBytes(bits)))
        self.assertEqual("00011111", l_encoded)

        bits = [
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
        ]
        l_encoded = "".join(map(chr, BinaryCodec.toAsciiBytes(bits)))
        self.assertEqual("00111111", l_encoded)

        bits = [
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
        ]
        l_encoded = "".join(map(chr, BinaryCodec.toAsciiBytes(bits)))
        self.assertEqual("01111111", l_encoded)

        bits = [
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        ]
        l_encoded = "".join(map(chr, BinaryCodec.toAsciiBytes(bits)))
        self.assertEqual("11111111", l_encoded)

        bits = [0, 0]
        l_encoded = "".join(map(chr, BinaryCodec.toAsciiBytes(bits)))
        self.assertEqual("0000000000000000", l_encoded)

        bits = [self.__BIT_0, 0]
        l_encoded = "".join(map(chr, BinaryCodec.toAsciiBytes(bits)))
        self.assertEqual("0000000000000001", l_encoded)

        bits = [self.__BIT_0 | self.__BIT_1, 0]
        l_encoded = "".join(map(chr, BinaryCodec.toAsciiBytes(bits)))
        self.assertEqual("0000000000000011", l_encoded)

        bits = [self.__BIT_0 | self.__BIT_1 | self.__BIT_2, 0]
        l_encoded = "".join(map(chr, BinaryCodec.toAsciiBytes(bits)))
        self.assertEqual("0000000000000111", l_encoded)

        bits = [self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3, 0]
        l_encoded = "".join(map(chr, BinaryCodec.toAsciiBytes(bits)))
        self.assertEqual("0000000000001111", l_encoded)

        bits = [
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4,
            0,
        ]
        l_encoded = "".join(map(chr, BinaryCodec.toAsciiBytes(bits)))
        self.assertEqual("0000000000011111", l_encoded)

    def testToAsciiBytes_test13_decomposed(self) -> None:
        bits = bytearray(1)
        l_encoded = "".join(map(chr, BinaryCodec.toAsciiBytes(bits)))
        self.assertEqual("00000000", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0
        l_encoded = "".join(map(chr, BinaryCodec.toAsciiBytes(bits)))
        self.assertEqual("00000001", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1
        l_encoded = "".join(map(chr, BinaryCodec.toAsciiBytes(bits)))
        self.assertEqual("00000011", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        l_encoded = "".join(map(chr, BinaryCodec.toAsciiBytes(bits)))
        self.assertEqual("00000111", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        l_encoded = "".join(map(chr, BinaryCodec.toAsciiBytes(bits)))
        self.assertEqual("00001111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        )
        l_encoded = "".join(map(chr, BinaryCodec.toAsciiBytes(bits)))
        self.assertEqual("00011111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
        )
        l_encoded = "".join(map(chr, BinaryCodec.toAsciiBytes(bits)))
        self.assertEqual("00111111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
        )
        l_encoded = "".join(map(chr, BinaryCodec.toAsciiBytes(bits)))
        self.assertEqual("01111111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        l_encoded = "".join(map(chr, BinaryCodec.toAsciiBytes(bits)))
        self.assertEqual("11111111", l_encoded)

        bits = bytearray(2)
        l_encoded = "".join(map(chr, BinaryCodec.toAsciiBytes(bits)))
        self.assertEqual("0000000000000000", l_encoded)

        bits = bytearray(2)
        bits[0] = self.__BIT_0
        l_encoded = "".join(map(chr, BinaryCodec.toAsciiBytes(bits)))
        self.assertEqual("0000000000000001", l_encoded)

        bits = bytearray(2)
        bits[0] = self.__BIT_0 | self.__BIT_1
        l_encoded = "".join(map(chr, BinaryCodec.toAsciiBytes(bits)))
        self.assertEqual("0000000000000011", l_encoded)

        bits = bytearray(2)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        l_encoded = "".join(map(chr, BinaryCodec.toAsciiBytes(bits)))
        self.assertEqual("0000000000000111", l_encoded)

        bits = bytearray(2)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        l_encoded = "".join(map(chr, BinaryCodec.toAsciiBytes(bits)))
        self.assertEqual("0000000000001111", l_encoded)

    def testToAsciiBytes_test12_decomposed(self) -> None:
        bits = [0]
        l_encoded = "".join(map(chr, BinaryCodec.toAsciiBytes(bits)))
        self.assertEqual("00000000", l_encoded)

        bits = [self.__BIT_0]
        l_encoded = "".join(map(chr, BinaryCodec.toAsciiBytes(bits)))
        self.assertEqual("00000001", l_encoded)

        bits = [self.__BIT_0 | self.__BIT_1]
        l_encoded = "".join(map(chr, BinaryCodec.toAsciiBytes(bits)))
        self.assertEqual("00000011", l_encoded)

        bits = [self.__BIT_0 | self.__BIT_1 | self.__BIT_2]
        l_encoded = "".join(map(chr, BinaryCodec.toAsciiBytes(bits)))
        self.assertEqual("00000111", l_encoded)

        bits = [self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3]
        l_encoded = "".join(map(chr, BinaryCodec.toAsciiBytes(bits)))
        self.assertEqual("00001111", l_encoded)

        bits = [
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        ]
        l_encoded = "".join(map(chr, BinaryCodec.toAsciiBytes(bits)))
        self.assertEqual("00011111", l_encoded)

        bits = [
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
        ]
        l_encoded = "".join(map(chr, BinaryCodec.toAsciiBytes(bits)))
        self.assertEqual("00111111", l_encoded)

        bits = [
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
        ]
        l_encoded = "".join(map(chr, BinaryCodec.toAsciiBytes(bits)))
        self.assertEqual("01111111", l_encoded)

        bits = [
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        ]
        l_encoded = "".join(map(chr, BinaryCodec.toAsciiBytes(bits)))
        self.assertEqual("11111111", l_encoded)

        bits = [0, 0]
        l_encoded = "".join(map(chr, BinaryCodec.toAsciiBytes(bits)))
        self.assertEqual("0000000000000000", l_encoded)

        bits = [self.__BIT_0, 0]
        l_encoded = "".join(map(chr, BinaryCodec.toAsciiBytes(bits)))
        self.assertEqual("0000000000000001", l_encoded)

        bits = [self.__BIT_0 | self.__BIT_1, 0]
        l_encoded = "".join(map(chr, BinaryCodec.toAsciiBytes(bits)))
        self.assertEqual("0000000000000011", l_encoded)

        bits = [self.__BIT_0 | self.__BIT_1 | self.__BIT_2, 0]
        l_encoded = "".join(map(chr, BinaryCodec.toAsciiBytes(bits)))
        self.assertEqual("0000000000000111", l_encoded)

    def testToAsciiBytes_test11_decomposed(self) -> None:
        bits = bytearray(1)
        l_encoded = "".join(map(chr, BinaryCodec.toAsciiBytes(bits)))
        self.assertEqual("00000000", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0
        l_encoded = "".join(map(chr, BinaryCodec.toAsciiBytes(bits)))
        self.assertEqual("00000001", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1
        l_encoded = "".join(map(chr, BinaryCodec.toAsciiBytes(bits)))
        self.assertEqual("00000011", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        l_encoded = "".join(map(chr, BinaryCodec.toAsciiBytes(bits)))
        self.assertEqual("00000111", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        l_encoded = "".join(map(chr, BinaryCodec.toAsciiBytes(bits)))
        self.assertEqual("00001111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        )
        l_encoded = "".join(map(chr, BinaryCodec.toAsciiBytes(bits)))
        self.assertEqual("00011111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
        )
        l_encoded = "".join(map(chr, BinaryCodec.toAsciiBytes(bits)))
        self.assertEqual("00111111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
        )
        l_encoded = "".join(map(chr, BinaryCodec.toAsciiBytes(bits)))
        self.assertEqual("01111111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        l_encoded = "".join(map(chr, BinaryCodec.toAsciiBytes(bits)))
        self.assertEqual("11111111", l_encoded)

        bits = bytearray(2)
        l_encoded = "".join(map(chr, BinaryCodec.toAsciiBytes(bits)))
        self.assertEqual("0000000000000000", l_encoded)

        bits = bytearray(2)
        bits[0] = self.__BIT_0
        l_encoded = "".join(map(chr, BinaryCodec.toAsciiBytes(bits)))
        self.assertEqual("0000000000000001", l_encoded)

        bits = bytearray(2)
        bits[0] = self.__BIT_0 | self.__BIT_1
        l_encoded = "".join(map(chr, BinaryCodec.toAsciiBytes(bits)))
        self.assertEqual("0000000000000011", l_encoded)

    def testToAsciiBytes_test10_decomposed(self) -> None:
        bits = bytearray(1)
        l_encoded = "".join(map(chr, BinaryCodec.toAsciiBytes(bits)))
        self.assertEqual("00000000", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0
        l_encoded = "".join(map(chr, BinaryCodec.toAsciiBytes(bits)))
        self.assertEqual("00000001", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1
        l_encoded = "".join(map(chr, BinaryCodec.toAsciiBytes(bits)))
        self.assertEqual("00000011", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        l_encoded = "".join(map(chr, BinaryCodec.toAsciiBytes(bits)))
        self.assertEqual("00000111", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        l_encoded = "".join(map(chr, BinaryCodec.toAsciiBytes(bits)))
        self.assertEqual("00001111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        )
        l_encoded = "".join(map(chr, BinaryCodec.toAsciiBytes(bits)))
        self.assertEqual("00011111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
        )
        l_encoded = "".join(map(chr, BinaryCodec.toAsciiBytes(bits)))
        self.assertEqual("00111111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
        )
        l_encoded = "".join(map(chr, BinaryCodec.toAsciiBytes(bits)))
        self.assertEqual("01111111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        l_encoded = "".join(map(chr, BinaryCodec.toAsciiBytes(bits)))
        self.assertEqual("11111111", l_encoded)

        bits = bytearray(2)
        l_encoded = "".join(map(chr, BinaryCodec.toAsciiBytes(bits)))
        self.assertEqual("0000000000000000", l_encoded)

        bits = bytearray(2)
        bits[0] = self.__BIT_0
        l_encoded = "".join(map(chr, BinaryCodec.toAsciiBytes(bits)))
        self.assertEqual("0000000100000000", l_encoded)

    def testToAsciiBytes_test9_decomposed(self) -> None:
        bits = bytearray(1)
        l_encoded = "".join(map(chr, BinaryCodec.toAsciiBytes(bits)))
        self.assertEqual("00000000", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0
        l_encoded = "".join(map(chr, BinaryCodec.toAsciiBytes(bits)))
        self.assertEqual("00000001", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1
        l_encoded = "".join(map(chr, BinaryCodec.toAsciiBytes(bits)))
        self.assertEqual("00000011", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        l_encoded = "".join(map(chr, BinaryCodec.toAsciiBytes(bits)))
        self.assertEqual("00000111", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        l_encoded = "".join(map(chr, BinaryCodec.toAsciiBytes(bits)))
        self.assertEqual("00001111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        )
        l_encoded = "".join(map(chr, BinaryCodec.toAsciiBytes(bits)))
        self.assertEqual("00011111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
        )
        l_encoded = "".join(map(chr, BinaryCodec.toAsciiBytes(bits)))
        self.assertEqual("00111111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
        )
        l_encoded = "".join(map(chr, BinaryCodec.toAsciiBytes(bits)))
        self.assertEqual("01111111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        l_encoded = "".join(map(chr, BinaryCodec.toAsciiBytes(bits)))
        self.assertEqual("11111111", l_encoded)

        bits = bytearray(2)
        l_encoded = "".join(map(chr, BinaryCodec.toAsciiBytes(bits)))

    def testToAsciiBytes_test8_decomposed(self) -> None:
        bits = bytearray(1)
        l_encoded = "".join(map(chr, BinaryCodec.toAsciiBytes(bits)))
        self.assertEqual("00000000", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0
        l_encoded = "".join(map(chr, BinaryCodec.toAsciiBytes(bits)))
        self.assertEqual("00000001", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1
        l_encoded = "".join(map(chr, BinaryCodec.toAsciiBytes(bits)))
        self.assertEqual("00000011", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        l_encoded = "".join(map(chr, BinaryCodec.toAsciiBytes(bits)))
        self.assertEqual("00000111", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        l_encoded = "".join(map(chr, BinaryCodec.toAsciiBytes(bits)))
        self.assertEqual("00001111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        )
        l_encoded = "".join(map(chr, BinaryCodec.toAsciiBytes(bits)))
        self.assertEqual("00011111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
        )
        l_encoded = "".join(map(chr, BinaryCodec.toAsciiBytes(bits)))
        self.assertEqual("00111111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
        )
        l_encoded = "".join(map(chr, BinaryCodec.toAsciiBytes(bits)))
        self.assertEqual("01111111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        l_encoded = "".join(map(chr, BinaryCodec.toAsciiBytes(bits)))
        self.assertEqual("11111111", l_encoded)

    def testToAsciiBytes_test7_decomposed(self) -> None:
        bits = [0]
        l_encoded = "".join(map(chr, self.instance.toAsciiBytes(bits)))
        self.assertEqual("00000000", l_encoded)

        bits = [0]
        bits[0] = self.__BIT_0
        l_encoded = "".join(map(chr, self.instance.toAsciiBytes(bits)))
        self.assertEqual("00000001", l_encoded)

        bits = [0]
        bits[0] = self.__BIT_0 | self.__BIT_1
        l_encoded = "".join(map(chr, self.instance.toAsciiBytes(bits)))
        self.assertEqual("00000011", l_encoded)

        bits = [0]
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        l_encoded = "".join(map(chr, self.instance.toAsciiBytes(bits)))
        self.assertEqual("00000111", l_encoded)

        bits = [0]
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        l_encoded = "".join(map(chr, self.instance.toAsciiBytes(bits)))
        self.assertEqual("00001111", l_encoded)

        bits = [0]
        bits[0] = (
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        )
        l_encoded = "".join(map(chr, self.instance.toAsciiBytes(bits)))
        self.assertEqual("00011111", l_encoded)

        bits = [0]
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
        )
        l_encoded = "".join(map(chr, self.instance.toAsciiBytes(bits)))
        self.assertEqual("00111111", l_encoded)

        bits = [0]
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
        )
        l_encoded = "".join(map(chr, self.instance.toAsciiBytes(bits)))
        self.assertEqual("01111111", l_encoded)

    def testToAsciiBytes_test6_decomposed(self) -> None:
        bits = bytearray(1)
        l_encoded = "".join(map(chr, self.instance.toAsciiBytes(bits)))
        self.assertEqual("00000000", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0
        l_encoded = "".join(map(chr, self.instance.toAsciiBytes(bits)))
        self.assertEqual("00000001", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1
        l_encoded = "".join(map(chr, self.instance.toAsciiBytes(bits)))
        self.assertEqual("00000011", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        l_encoded = "".join(map(chr, self.instance.toAsciiBytes(bits)))
        self.assertEqual("00000111", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        l_encoded = "".join(map(chr, self.instance.toAsciiBytes(bits)))
        self.assertEqual("00001111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        )
        l_encoded = "".join(map(chr, self.instance.toAsciiBytes(bits)))
        self.assertEqual("00011111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
        )
        l_encoded = "".join(map(chr, self.instance.toAsciiBytes(bits)))
        self.assertEqual("00111111", l_encoded)

    def testToAsciiBytes_test5_decomposed(self) -> None:
        bits = bytearray(1)
        l_encoded = "".join(map(chr, BinaryCodec.toAsciiBytes(bits)))
        self.assertEqual("00000000", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0
        l_encoded = "".join(map(chr, BinaryCodec.toAsciiBytes(bits)))
        self.assertEqual("00000001", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1
        l_encoded = "".join(map(chr, BinaryCodec.toAsciiBytes(bits)))
        self.assertEqual("00000011", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        l_encoded = "".join(map(chr, BinaryCodec.toAsciiBytes(bits)))
        self.assertEqual("00000111", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        l_encoded = "".join(map(chr, BinaryCodec.toAsciiBytes(bits)))
        self.assertEqual("00001111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        )
        l_encoded = "".join(map(chr, BinaryCodec.toAsciiBytes(bits)))
        self.assertEqual("00011111", l_encoded)

    def testToAsciiBytes_test4_decomposed(self) -> None:
        bits = bytearray(1)
        l_encoded = "".join(map(chr, self.instance.toAsciiBytes(bits)))
        self.assertEqual("00000000", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0
        l_encoded = "".join(map(chr, self.instance.toAsciiBytes(bits)))
        self.assertEqual("00000001", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1
        l_encoded = "".join(map(chr, self.instance.toAsciiBytes(bits)))
        self.assertEqual("00000011", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        l_encoded = "".join(map(chr, self.instance.toAsciiBytes(bits)))
        self.assertEqual("00000111", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        l_encoded = "".join(map(chr, self.instance.toAsciiBytes(bits)))
        self.assertEqual("00001111", l_encoded)

    def testToAsciiBytes_test3_decomposed(self) -> None:
        bits = [0]  # Initialize a byte array with one element set to 0
        l_encoded = "".join(
            map(chr, BinaryCodec.toAsciiBytes(bits))
        )  # Convert ASCII bytes to string
        self.assertEqual("00000000", l_encoded)

        bits = [0]  # Reset the byte array
        bits[0] = self.__BIT_0  # Set the first bit
        l_encoded = "".join(map(chr, BinaryCodec.toAsciiBytes(bits)))
        self.assertEqual("00000001", l_encoded)

        bits = [0]  # Reset the byte array
        bits[0] = self.__BIT_0 | self.__BIT_1  # Set the first and second bits
        l_encoded = "".join(map(chr, BinaryCodec.toAsciiBytes(bits)))
        self.assertEqual("00000011", l_encoded)

        bits = [0]  # Reset the byte array
        bits[0] = (
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        )  # Set the first, second, and third bits
        l_encoded = "".join(map(chr, BinaryCodec.toAsciiBytes(bits)))
        self.assertEqual("00000111", l_encoded)

    def testToAsciiBytes_test2_decomposed(self) -> None:
        bits = bytearray(1)  # Create a byte array of size 1
        l_encoded = "".join(
            map(chr, BinaryCodec.toAsciiBytes(bits))
        )  # Convert ASCII bytes to string
        self.assertEqual("00000000", l_encoded)

        bits = bytearray(1)  # Reset bits to a new byte array of size 1
        bits[0] = self.__BIT_0  # Set the first bit
        l_encoded = "".join(
            map(chr, BinaryCodec.toAsciiBytes(bits))
        )  # Convert ASCII bytes to string
        self.assertEqual("00000001", l_encoded)

        bits = bytearray(1)  # Reset bits to a new byte array of size 1
        bits[0] = self.__BIT_0 | self.__BIT_1  # Set the first and second bits
        l_encoded = "".join(
            map(chr, BinaryCodec.toAsciiBytes(bits))
        )  # Convert ASCII bytes to string
        self.assertEqual("00000011", l_encoded)

    def testToAsciiBytes_test1_decomposed(self) -> None:
        bits = bytearray(1)  # Create a byte array of size 1
        l_encoded = "".join(
            map(chr, BinaryCodec.toAsciiBytes(bits))
        )  # Convert ASCII bytes to string
        self.assertEqual(
            "00000000", l_encoded
        )  # Assert the encoded string matches "00000000"

        bits = bytearray(1)  # Reset the byte array
        bits[0] = self.__BIT_0  # Set the first byte to BIT_0
        l_encoded = "".join(
            map(chr, BinaryCodec.toAsciiBytes(bits))
        )  # Convert ASCII bytes to string
        # You can add further assertions here if needed

    def testToAsciiBytes_test0_decomposed(self) -> None:
        bits = [0]  # Equivalent to `new byte[1]` in Java
        l_encoded = "".join(
            map(chr, self.instance.toAsciiBytes(bits))
        )  # Convert ASCII byte values to a string

    def testEncodeByteArray_test26_decomposed(self) -> None:
        bits = bytearray(1)
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("00000000", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("00000001", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("00000011", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("00000111", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("00001111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        )
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("00011111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
        )
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("00111111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
        )
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("01111111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("11111111", l_encoded)

        bits = bytearray(2)
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("0000000000000000", l_encoded)

        bits = bytearray(2)
        bits[0] = self.__BIT_0
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("0000000000000001", l_encoded)

        bits = bytearray(2)
        bits[0] = self.__BIT_0 | self.__BIT_1
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("0000000000000011", l_encoded)

        bits = bytearray(2)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("0000000000000111", l_encoded)

        bits = bytearray(2)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("0000000000001111", l_encoded)

        bits = bytearray(2)
        bits[0] = (
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        )
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("0000000000011111", l_encoded)

        bits = bytearray(2)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
        )
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("0000000000111111", l_encoded)

        bits = bytearray(2)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
        )
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("0000000001111111", l_encoded)

        bits = bytearray(2)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("0000000011111111", l_encoded)

        bits = bytearray(2)
        bits[1] = self.__BIT_0
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("0000000111111111", l_encoded)

        bits = bytearray(2)
        bits[1] = self.__BIT_0 | self.__BIT_1
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("0000001111111111", l_encoded)

        bits = bytearray(2)
        bits[1] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("0000011111111111", l_encoded)

        bits = bytearray(2)
        bits[1] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("0000111111111111", l_encoded)

        bits = bytearray(2)
        bits[1] = (
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        )
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("0001111111111111", l_encoded)

        bits = bytearray(2)
        bits[1] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
        )
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("0011111111111111", l_encoded)

        bits = bytearray(2)
        bits[1] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
        )
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("0111111111111111", l_encoded)

        bits = bytearray(2)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        bits[1] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("1111111111111111", l_encoded)

        self.assertEqual(0, len(self.instance.encode0(None)))

    def testEncodeByteArray_test25_decomposed(self) -> None:
        bits = bytearray(1)
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("00000000", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("00000001", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("00000011", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("00000111", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("00001111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        )
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("00011111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
        )
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("00111111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
        )
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("01111111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("11111111", l_encoded)

        bits = bytearray(2)
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("0000000000000000", l_encoded)

        bits = bytearray(2)
        bits[0] = self.__BIT_0
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("0000000000000001", l_encoded)

        bits = bytearray(2)
        bits[0] = self.__BIT_0 | self.__BIT_1
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("0000000000000011", l_encoded)

        bits = bytearray(2)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("0000000000000111", l_encoded)

        bits = bytearray(2)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("0000000000001111", l_encoded)

        bits = bytearray(2)
        bits[0] = (
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        )
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("0000000000011111", l_encoded)

        bits = bytearray(2)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
        )
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("0000000000111111", l_encoded)

        bits = bytearray(2)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
        )
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("0000000001111111", l_encoded)

        bits = bytearray(2)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("0000000011111111", l_encoded)

        bits = bytearray(2)
        bits[1] = self.__BIT_0
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("0000000111111111", l_encoded)

        bits = bytearray(2)
        bits[1] = self.__BIT_0 | self.__BIT_1
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("0000001111111111", l_encoded)

        bits = bytearray(2)
        bits[1] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("0000011111111111", l_encoded)

        bits = bytearray(2)
        bits[1] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("0000111111111111", l_encoded)

        bits = bytearray(2)
        bits[1] = (
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        )
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("0001111111111111", l_encoded)

        bits = bytearray(2)
        bits[1] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
        )
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("0011111111111111", l_encoded)

        bits = bytearray(2)
        bits[1] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
        )
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("0111111111111111", l_encoded)

        bits = bytearray(2)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        bits[1] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("1111111111111111", l_encoded)

    def testEncodeByteArray_test24_decomposed(self) -> None:
        bits = bytearray(1)
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("00000000", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("00000001", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("00000011", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("00000111", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("00001111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        )
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("00011111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
        )
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("00111111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
        )
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("01111111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("11111111", l_encoded)

        bits = bytearray(2)
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("0000000000000000", l_encoded)

        bits = bytearray(2)
        bits[0] = self.__BIT_0
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("0000000000000001", l_encoded)

        bits = bytearray(2)
        bits[0] = self.__BIT_0 | self.__BIT_1
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("0000000000000011", l_encoded)

        bits = bytearray(2)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("0000000000000111", l_encoded)

        bits = bytearray(2)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("0000000000001111", l_encoded)

        bits = bytearray(2)
        bits[0] = (
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        )
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("0000000000011111", l_encoded)

        bits = bytearray(2)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
        )
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("0000000000111111", l_encoded)

        bits = bytearray(2)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
        )
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("0000000001111111", l_encoded)

        bits = bytearray(2)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("0000000011111111", l_encoded)

        bits = bytearray(2)
        bits[1] = self.__BIT_0
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("0000000111111111", l_encoded)

        bits = bytearray(2)
        bits[1] = self.__BIT_0 | self.__BIT_1
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("0000001111111111", l_encoded)

        bits = bytearray(2)
        bits[1] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("0000011111111111", l_encoded)

        bits = bytearray(2)
        bits[1] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("0000111111111111", l_encoded)

        bits = bytearray(2)
        bits[1] = (
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        )
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("0001111111111111", l_encoded)

        bits = bytearray(2)
        bits[1] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
        )
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("0011111111111111", l_encoded)

        bits = bytearray(2)
        bits[1] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
        )
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("0111111111111111", l_encoded)

    def testEncodeByteArray_test23_decomposed(self) -> None:
        bits = bytearray(1)
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("00000000", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("00000001", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("00000011", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("00000111", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("00001111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        )
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("00011111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
        )
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("00111111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
        )
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("01111111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("11111111", l_encoded)

        bits = bytearray(2)
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("0000000000000000", l_encoded)

        bits = bytearray(2)
        bits[0] = self.__BIT_0
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("0000000000000001", l_encoded)

        bits = bytearray(2)
        bits[0] = self.__BIT_0 | self.__BIT_1
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("0000000000000011", l_encoded)

        bits = bytearray(2)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("0000000000000111", l_encoded)

        bits = bytearray(2)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("0000000000001111", l_encoded)

        bits = bytearray(2)
        bits[0] = (
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        )
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("0000000000011111", l_encoded)

        bits = bytearray(2)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
        )
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("0000000000111111", l_encoded)

        bits = bytearray(2)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
        )
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("0000000001111111", l_encoded)

        bits = bytearray(2)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("0000000011111111", l_encoded)

        bits = bytearray(2)
        bits[1] = self.__BIT_0
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("0000000111111111", l_encoded)

        bits = bytearray(2)
        bits[1] = self.__BIT_0 | self.__BIT_1
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("0000001111111111", l_encoded)

        bits = bytearray(2)
        bits[1] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("0000011111111111", l_encoded)

        bits = bytearray(2)
        bits[1] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("0000111111111111", l_encoded)

        bits = bytearray(2)
        bits[1] = (
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        )
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("0001111111111111", l_encoded)

        bits = bytearray(2)
        bits[1] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
        )
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("0001111111111111", l_encoded)

    def testEncodeByteArray_test22_decomposed(self) -> None:
        bits = bytearray(1)
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("00000000", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("00000001", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("00000011", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("00000111", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("00001111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        )
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("00011111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
        )
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("00111111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
        )
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("01111111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("11111111", l_encoded)

        bits = bytearray(2)
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("0000000000000000", l_encoded)

        bits = bytearray(2)
        bits[0] = self.__BIT_0
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("0000000000000001", l_encoded)

        bits = bytearray(2)
        bits[0] = self.__BIT_0 | self.__BIT_1
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("0000000000000011", l_encoded)

        bits = bytearray(2)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("0000000000000111", l_encoded)

        bits = bytearray(2)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("0000000000001111", l_encoded)

        bits = bytearray(2)
        bits[0] = (
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        )
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("0000000000011111", l_encoded)

        bits = bytearray(2)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
        )
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("0000000000111111", l_encoded)

        bits = bytearray(2)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
        )
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("0000000001111111", l_encoded)

        bits = bytearray(2)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("0000000011111111", l_encoded)

        bits = bytearray(2)
        bits[1] = self.__BIT_0
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("0000000111111111", l_encoded)

        bits = bytearray(2)
        bits[1] = self.__BIT_0 | self.__BIT_1
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("0000001111111111", l_encoded)

        bits = bytearray(2)
        bits[1] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("0000011111111111", l_encoded)

        bits = bytearray(2)
        bits[1] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("0000111111111111", l_encoded)

        bits = bytearray(2)
        bits[1] = (
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        )
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("0001111111111111", l_encoded)

    def testEncodeByteArray_test21_decomposed(self) -> None:
        bits = bytearray(1)
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("00000000", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("00000001", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("00000011", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("00000111", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("00001111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        )
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("00011111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
        )
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("00111111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
        )
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("01111111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("11111111", l_encoded)

        bits = bytearray(2)
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("0000000000000000", l_encoded)

        bits = bytearray(2)
        bits[0] = self.__BIT_0
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("0000000000000001", l_encoded)

        bits = bytearray(2)
        bits[0] = self.__BIT_0 | self.__BIT_1
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("0000000000000011", l_encoded)

        bits = bytearray(2)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("0000000000000111", l_encoded)

        bits = bytearray(2)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("0000000000001111", l_encoded)

        bits = bytearray(2)
        bits[0] = (
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        )
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("0000000000011111", l_encoded)

        bits = bytearray(2)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
        )
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("0000000000111111", l_encoded)

        bits = bytearray(2)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
        )
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("0000000001111111", l_encoded)

        bits = bytearray(2)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("0000000011111111", l_encoded)

        bits = bytearray(2)
        bits[1] = self.__BIT_0
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("0000000111111111", l_encoded)

        bits = bytearray(2)
        bits[1] = self.__BIT_0 | self.__BIT_1
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("0000001111111111", l_encoded)

        bits = bytearray(2)
        bits[1] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("0000011111111111", l_encoded)

        bits = bytearray(2)
        bits[1] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("0000111111111111", l_encoded)

    def testEncodeByteArray_test20_decomposed(self) -> None:
        bits = bytearray(1)
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("00000000", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("00000001", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("00000011", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("00000111", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("00001111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        )
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("00011111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
        )
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("00111111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
        )
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("01111111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("11111111", l_encoded)

        bits = bytearray(2)
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("0000000000000000", l_encoded)

        bits = bytearray(2)
        bits[0] = self.__BIT_0
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("0000000000000001", l_encoded)

        bits = bytearray(2)
        bits[0] = self.__BIT_0 | self.__BIT_1
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("0000000000000011", l_encoded)

        bits = bytearray(2)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("0000000000000111", l_encoded)

        bits = bytearray(2)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("0000000000001111", l_encoded)

        bits = bytearray(2)
        bits[0] = (
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        )
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("0000000000011111", l_encoded)

        bits = bytearray(2)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
        )
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("0000000000111111", l_encoded)

        bits = bytearray(2)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
        )
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("0000000001111111", l_encoded)

        bits = bytearray(2)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("0000000011111111", l_encoded)

        bits = bytearray(2)
        bits[1] = self.__BIT_0
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("0000000111111111", l_encoded)

        bits = bytearray(2)
        bits[1] = self.__BIT_0 | self.__BIT_1
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("0000001111111111", l_encoded)

        bits = bytearray(2)
        bits[1] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("0000011111111111", l_encoded)

    def testEncodeByteArray_test19_decomposed(self) -> None:
        bits = bytearray(1)
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("00000000", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("00000001", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("00000011", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("00000111", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("00001111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        )
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("00011111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
        )
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("00111111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
        )
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("01111111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("11111111", l_encoded)

        bits = bytearray(2)
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("0000000000000000", l_encoded)

        bits = bytearray(2)
        bits[0] = self.__BIT_0
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("0000000000000001", l_encoded)

        bits = bytearray(2)
        bits[0] = self.__BIT_0 | self.__BIT_1
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("0000000000000011", l_encoded)

        bits = bytearray(2)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("0000000000000111", l_encoded)

        bits = bytearray(2)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("0000000000001111", l_encoded)

        bits = bytearray(2)
        bits[0] = (
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        )
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("0000000000011111", l_encoded)

        bits = bytearray(2)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
        )
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("0000000000111111", l_encoded)

        bits = bytearray(2)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
        )
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("0000000001111111", l_encoded)

        bits = bytearray(2)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("0000000011111111", l_encoded)

        bits = bytearray(2)
        bits[1] = self.__BIT_0
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("0000000111111111", l_encoded)

        bits = bytearray(2)
        bits[1] = self.__BIT_0 | self.__BIT_1
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("0000001111111111", l_encoded)

    def testEncodeByteArray_test18_decomposed(self) -> None:
        bits = bytearray(1)
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("00000000", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("00000001", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("00000011", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("00000111", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("00001111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        )
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("00011111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
        )
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("00111111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
        )
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("01111111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("11111111", l_encoded)

        bits = bytearray(2)
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("0000000000000000", l_encoded)

        bits = bytearray(2)
        bits[0] = self.__BIT_0
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("0000000000000001", l_encoded)

        bits = bytearray(2)
        bits[0] = self.__BIT_0 | self.__BIT_1
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("0000000000000011", l_encoded)

        bits = bytearray(2)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("0000000000000111", l_encoded)

        bits = bytearray(2)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("0000000000001111", l_encoded)

        bits = bytearray(2)
        bits[0] = (
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        )
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("0000000000011111", l_encoded)

        bits = bytearray(2)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
        )
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("0000000000111111", l_encoded)

        bits = bytearray(2)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
        )
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("0000000001111111", l_encoded)

        bits = bytearray(2)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("0000000011111111", l_encoded)

        bits = bytearray(2)
        bits[1] = self.__BIT_0
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("1111111100000001", l_encoded)

    def testEncodeByteArray_test17_decomposed(self) -> None:
        bits = bytearray(1)
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("00000000", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("00000001", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("00000011", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("00000111", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("00001111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        )
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("00011111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
        )
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("00111111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
        )
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("01111111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("11111111", l_encoded)

        bits = bytearray(2)
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("0000000000000000", l_encoded)

        bits = bytearray(2)
        bits[0] = self.__BIT_0
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("0000000000000001", l_encoded)

        bits = bytearray(2)
        bits[0] = self.__BIT_0 | self.__BIT_1
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("0000000000000011", l_encoded)

        bits = bytearray(2)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("0000000000000111", l_encoded)

        bits = bytearray(2)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("0000000000001111", l_encoded)

        bits = bytearray(2)
        bits[0] = (
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        )
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("0000000000011111", l_encoded)

        bits = bytearray(2)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
        )
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("0000000000111111", l_encoded)

        bits = bytearray(2)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
        )
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("0000000001111111", l_encoded)

        bits = bytearray(2)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("0000000011111111", l_encoded)

    def testEncodeByteArray_test16_decomposed(self) -> None:
        bits = bytearray(1)
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("00000000", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("00000001", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("00000011", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("00000111", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("00001111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        )
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("00011111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
        )
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("00111111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
        )
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("01111111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("11111111", l_encoded)

        bits = bytearray(2)
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("0000000000000000", l_encoded)

        bits = bytearray(2)
        bits[0] = self.__BIT_0
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("0000000000000001", l_encoded)

        bits = bytearray(2)
        bits[0] = self.__BIT_0 | self.__BIT_1
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("0000000000000011", l_encoded)

        bits = bytearray(2)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("0000000000000111", l_encoded)

        bits = bytearray(2)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("0000000000001111", l_encoded)

        bits = bytearray(2)
        bits[0] = (
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        )
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("0000000000011111", l_encoded)

        bits = bytearray(2)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
        )
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("0000000000111111", l_encoded)

        bits = bytearray(2)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
        )
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("0000000001111111", l_encoded)

    def testEncodeByteArray_test15_decomposed(self) -> None:
        bits = bytearray(1)
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("00000000", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("00000001", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("00000011", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("00000111", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("00001111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        )
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("00011111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
        )
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("00111111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
        )
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("01111111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("11111111", l_encoded)

        bits = bytearray(2)
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("0000000000000000", l_encoded)

        bits = bytearray(2)
        bits[0] = self.__BIT_0
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("0000000000000001", l_encoded)

        bits = bytearray(2)
        bits[0] = self.__BIT_0 | self.__BIT_1
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("0000000000000011", l_encoded)

        bits = bytearray(2)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("0000000000000111", l_encoded)

        bits = bytearray(2)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("0000000000001111", l_encoded)

        bits = bytearray(2)
        bits[0] = (
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        )
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("0000000000011111", l_encoded)

        bits = bytearray(2)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
        )
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("0000000000111111", l_encoded)

    def testEncodeByteArray_test14_decomposed(self) -> None:
        bits = bytearray(1)
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("00000000", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("00000001", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("00000011", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("00000111", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("00001111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        )
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("00011111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
        )
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("00111111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
        )
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("01111111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("11111111", l_encoded)

        bits = bytearray(2)
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("0000000000000000", l_encoded)

        bits = bytearray(2)
        bits[0] = self.__BIT_0
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("0000000000000001", l_encoded)

        bits = bytearray(2)
        bits[0] = self.__BIT_0 | self.__BIT_1
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("0000000000000011", l_encoded)

        bits = bytearray(2)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("0000000000000111", l_encoded)

        bits = bytearray(2)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("0000000000001111", l_encoded)

        bits = bytearray(2)
        bits[0] = (
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        )
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("0000000000011111", l_encoded)

    def testEncodeByteArray_test13_decomposed(self) -> None:
        bits = bytearray(1)
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("00000000", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("00000001", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("00000011", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("00000111", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("00001111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        )
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("00011111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
        )
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("00111111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
        )
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("01111111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("11111111", l_encoded)

        bits = bytearray(2)
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("0000000000000000", l_encoded)

        bits = bytearray(2)
        bits[0] = self.__BIT_0
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("0000000000000001", l_encoded)

        bits = bytearray(2)
        bits[0] = self.__BIT_0 | self.__BIT_1
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("0000000000000011", l_encoded)

        bits = bytearray(2)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("0000000000000111", l_encoded)

        bits = bytearray(2)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("0000000000001111", l_encoded)

    def testEncodeByteArray_test12_decomposed(self) -> None:
        bits = bytearray(1)
        l_encoded = "".join(map(chr, self.instance.encode0(bits)))
        self.assertEqual("00000000", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0
        l_encoded = "".join(map(chr, self.instance.encode0(bits)))
        self.assertEqual("00000001", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1
        l_encoded = "".join(map(chr, self.instance.encode0(bits)))
        self.assertEqual("00000011", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        l_encoded = "".join(map(chr, self.instance.encode0(bits)))
        self.assertEqual("00000111", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        l_encoded = "".join(map(chr, self.instance.encode0(bits)))
        self.assertEqual("00001111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        )
        l_encoded = "".join(map(chr, self.instance.encode0(bits)))
        self.assertEqual("00011111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
        )
        l_encoded = "".join(map(chr, self.instance.encode0(bits)))
        self.assertEqual("00111111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
        )
        l_encoded = "".join(map(chr, self.instance.encode0(bits)))
        self.assertEqual("01111111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        l_encoded = "".join(map(chr, self.instance.encode0(bits)))
        self.assertEqual("11111111", l_encoded)

        bits = bytearray(2)
        l_encoded = "".join(map(chr, self.instance.encode0(bits)))
        self.assertEqual("0000000000000000", l_encoded)

        bits = bytearray(2)
        bits[0] = self.__BIT_0
        l_encoded = "".join(map(chr, self.instance.encode0(bits)))
        self.assertEqual("0000000000000001", l_encoded)

        bits = bytearray(2)
        bits[0] = self.__BIT_0 | self.__BIT_1
        l_encoded = "".join(map(chr, self.instance.encode0(bits)))
        self.assertEqual("0000000000000011", l_encoded)

        bits = bytearray(2)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        l_encoded = "".join(map(chr, self.instance.encode0(bits)))
        # The final assertion is missing in the original Java code, so it is omitted here as well.

    def testEncodeByteArray_test11_decomposed(self) -> None:
        bits = bytearray(1)
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("00000000", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("00000001", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("00000011", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("00000111", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("00001111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        )
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("00011111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
        )
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("00111111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
        )
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("01111111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("11111111", l_encoded)

        bits = bytearray(2)
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("0000000000000000", l_encoded)

        bits = bytearray(2)
        bits[0] = self.__BIT_0
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("0000000000000001", l_encoded)

        bits = bytearray(2)
        bits[0] = self.__BIT_0 | self.__BIT_1
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("0000000000000011", l_encoded)

    def testEncodeByteArray_test10_decomposed(self) -> None:
        bits = bytearray(1)
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("00000000", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("00000001", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("00000011", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("00000111", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("00001111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        )
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("00011111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
        )
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("00111111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
        )
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("01111111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("11111111", l_encoded)

        bits = bytearray(2)
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("0000000000000000", l_encoded)

        bits = bytearray(2)
        bits[0] = self.__BIT_0
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("0000000100000000", l_encoded)

    def testEncodeByteArray_test9_decomposed(self) -> None:
        bits = bytearray(1)
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("00000000", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("00000001", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("00000011", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("00000111", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("00001111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        )
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("00011111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
        )
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("00111111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
        )
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("01111111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("11111111", l_encoded)

        bits = bytearray(2)
        l_encoded = self.instance.encode0(bits).decode("utf-8")

    def testEncodeByteArray_test8_decomposed(self) -> None:
        bits = bytearray(1)
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("00000000", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("00000001", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("00000011", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("00000111", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("00001111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        )
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("00011111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
        )
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("00111111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
        )
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("01111111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("11111111", l_encoded)

    def testEncodeByteArray_test7_decomposed(self) -> None:
        bits = bytearray(1)
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("00000000", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("00000001", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("00000011", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("00000111", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("00001111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        )
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("00011111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
        )
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("00111111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
        )
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("01111111", l_encoded)

    def testEncodeByteArray_test6_decomposed(self) -> None:
        bits = bytearray(1)
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("00000000", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("00000001", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("00000011", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("00000111", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("00001111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        )
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("00011111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
        )
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("00111111", l_encoded)

    def testEncodeByteArray_test5_decomposed(self) -> None:
        bits = bytearray(1)
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("00000000", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("00000001", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("00000011", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("00000111", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("00001111", l_encoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        )
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("00011111", l_encoded)

    def testEncodeByteArray_test4_decomposed(self) -> None:
        bits = bytearray(1)
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("00000000", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("00000001", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("00000011", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("00000111", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        l_encoded = self.instance.encode0(bits).decode("utf-8")
        self.assertEqual("00001111", l_encoded)

    def testEncodeByteArray_test3_decomposed(self) -> None:
        bits = bytearray(1)
        l_encoded = "".join(map(chr, self.instance.encode0(bits)))
        self.assertEqual("00000000", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0
        l_encoded = "".join(map(chr, self.instance.encode0(bits)))
        self.assertEqual("00000001", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1
        l_encoded = "".join(map(chr, self.instance.encode0(bits)))
        self.assertEqual("00000011", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        l_encoded = "".join(map(chr, self.instance.encode0(bits)))
        self.assertEqual("00000111", l_encoded)

    def testEncodeByteArray_test2_decomposed(self) -> None:
        bits = bytearray(1)
        l_encoded = str(self.instance.encode0(bits), "utf-8")
        self.assertEqual("00000000", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0
        l_encoded = str(self.instance.encode0(bits), "utf-8")
        self.assertEqual("00000001", l_encoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1
        l_encoded = str(self.instance.encode0(bits), "utf-8")
        # Add an assertion here if needed, as the original Java code does not include one

    def testEncodeByteArray_test1_decomposed(self) -> None:
        bits = bytearray(1)  # Create a byte array of size 1
        l_encoded = str(
            self.instance.encode0(bits), "utf-8"
        )  # Encode and convert to string
        self.assertEqual(
            "00000000", l_encoded
        )  # Assert the encoded string matches expected value

        bits = bytearray(1)  # Reset the byte array
        bits[0] = self.__BIT_0  # Set the first bit to BIT_0
        l_encoded = str(
            self.instance.encode0(bits), "utf-8"
        )  # Encode and convert to string

    def testEncodeByteArray_test0_decomposed(self) -> None:
        bits = bytearray(1)  # Create a byte array of size 1
        l_encoded = str(
            self.instance.encode0(bits)
        )  # Call encode0 and convert the result to a string

    def testFromAsciiByteArray_test37_decomposed(self) -> None:
        self.assertEqual(0, len(self.instance.fromAscii0(None)))
        self.assertEqual(0, len(self.instance.fromAscii0([])))

        bits = bytearray(1)
        decoded = self.instance.fromAscii0("00000000".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits[0] = self.__BIT_0
        decoded = self.instance.fromAscii0("00000001".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits[0] = self.__BIT_0 | self.__BIT_1
        decoded = self.instance.fromAscii0("00000011".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        decoded = self.instance.fromAscii0("00000111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        decoded = self.instance.fromAscii0("00001111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits[0] = (
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        )
        decoded = self.instance.fromAscii0("00011111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
        )
        decoded = self.instance.fromAscii0("00111111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
        )
        decoded = self.instance.fromAscii0("01111111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = self.instance.fromAscii0("11111111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits = bytearray(2)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = self.instance.fromAscii0(
            "0000000011111111".encode(self.__CHARSET_UTF8)
        )
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits[1] = self.__BIT_0
        decoded = self.instance.fromAscii0(
            "0000000111111111".encode(self.__CHARSET_UTF8)
        )
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits[1] = self.__BIT_0 | self.__BIT_1
        decoded = self.instance.fromAscii0(
            "0000001111111111".encode(self.__CHARSET_UTF8)
        )
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits[1] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        decoded = self.instance.fromAscii0(
            "0000011111111111".encode(self.__CHARSET_UTF8)
        )
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits[1] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        decoded = self.instance.fromAscii0(
            "0000111111111111".encode(self.__CHARSET_UTF8)
        )
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits[1] = (
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        )
        decoded = self.instance.fromAscii0(
            "0001111111111111".encode(self.__CHARSET_UTF8)
        )
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits[1] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
        )
        decoded = self.instance.fromAscii0(
            "0011111111111111".encode(self.__CHARSET_UTF8)
        )
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits[1] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
        )
        decoded = self.instance.fromAscii0(
            "0111111111111111".encode(self.__CHARSET_UTF8)
        )
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits[1] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = self.instance.fromAscii0(
            "1111111111111111".encode(self.__CHARSET_UTF8)
        )
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        self.assertEqual(0, len(self.instance.fromAscii0(None)))

    def testFromAsciiByteArray_test36_decomposed(self) -> None:
        self.assertEqual(0, len(self.instance.fromAscii0(None)))
        self.assertEqual(0, len(self.instance.fromAscii0([])))

        bits = bytearray(1)
        decoded = self.instance.fromAscii0("00000000".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits[0] = self.__BIT_0
        decoded = self.instance.fromAscii0("00000001".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits[0] = self.__BIT_0 | self.__BIT_1
        decoded = self.instance.fromAscii0("00000011".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        decoded = self.instance.fromAscii0("00000111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        decoded = self.instance.fromAscii0("00001111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits[0] = (
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        )
        decoded = self.instance.fromAscii0("00011111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
        )
        decoded = self.instance.fromAscii0("00111111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
        )
        decoded = self.instance.fromAscii0("01111111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = self.instance.fromAscii0("11111111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits = bytearray(2)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = self.instance.fromAscii0(
            "0000000011111111".encode(self.__CHARSET_UTF8)
        )
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits[1] = self.__BIT_0
        decoded = self.instance.fromAscii0(
            "0000000111111111".encode(self.__CHARSET_UTF8)
        )
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits[1] = self.__BIT_0 | self.__BIT_1
        decoded = self.instance.fromAscii0(
            "0000001111111111".encode(self.__CHARSET_UTF8)
        )
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits[1] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        decoded = self.instance.fromAscii0(
            "0000011111111111".encode(self.__CHARSET_UTF8)
        )
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits[1] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        decoded = self.instance.fromAscii0(
            "0000111111111111".encode(self.__CHARSET_UTF8)
        )
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits[1] = (
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        )
        decoded = self.instance.fromAscii0(
            "0001111111111111".encode(self.__CHARSET_UTF8)
        )
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits[1] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
        )
        decoded = self.instance.fromAscii0(
            "0011111111111111".encode(self.__CHARSET_UTF8)
        )
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits[1] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
        )
        decoded = self.instance.fromAscii0(
            "0111111111111111".encode(self.__CHARSET_UTF8)
        )
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits[1] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = self.instance.fromAscii0(
            "1111111111111111".encode(self.__CHARSET_UTF8)
        )
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

    def testFromAsciiByteArray_test35_decomposed(self) -> None:
        self.assertEqual(len(BinaryCodec.fromAscii0(None)), 0)
        self.assertEqual(len(BinaryCodec.fromAscii0([])), 0)

        bits = bytearray(1)
        decoded = BinaryCodec.fromAscii0("00000000".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits[0] = self.__BIT_0
        decoded = BinaryCodec.fromAscii0("00000001".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits[0] = self.__BIT_0 | self.__BIT_1
        decoded = BinaryCodec.fromAscii0("00000011".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        decoded = BinaryCodec.fromAscii0("00000111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        decoded = BinaryCodec.fromAscii0("00001111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits[0] = (
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        )
        decoded = BinaryCodec.fromAscii0("00011111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
        )
        decoded = BinaryCodec.fromAscii0("00111111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
        )
        decoded = BinaryCodec.fromAscii0("01111111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = BinaryCodec.fromAscii0("11111111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits = bytearray(2)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = BinaryCodec.fromAscii0("0000000011111111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits[1] = self.__BIT_0
        decoded = BinaryCodec.fromAscii0("0000000111111111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits[1] = self.__BIT_0 | self.__BIT_1
        decoded = BinaryCodec.fromAscii0("0000001111111111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits[1] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        decoded = BinaryCodec.fromAscii0("0000011111111111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits[1] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        decoded = BinaryCodec.fromAscii0("0000111111111111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits[1] = (
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        )
        decoded = BinaryCodec.fromAscii0("0001111111111111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits[1] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
        )
        decoded = BinaryCodec.fromAscii0("0011111111111111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits[1] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
        )
        decoded = BinaryCodec.fromAscii0("0111111111111111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits[1] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = BinaryCodec.fromAscii0("1111111111111111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

    def testFromAsciiByteArray_test34_decomposed(self) -> None:
        self.assertEqual(len(BinaryCodec.fromAscii0(None)), 0)
        self.assertEqual(len(BinaryCodec.fromAscii0([])), 0)

        bits = bytearray(1)
        decoded = BinaryCodec.fromAscii0("00000000".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits[0] = self.__BIT_0
        decoded = BinaryCodec.fromAscii0("00000001".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits[0] = self.__BIT_0 | self.__BIT_1
        decoded = BinaryCodec.fromAscii0("00000011".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        decoded = BinaryCodec.fromAscii0("00000111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        decoded = BinaryCodec.fromAscii0("00001111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits[0] = (
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        )
        decoded = BinaryCodec.fromAscii0("00011111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
        )
        decoded = BinaryCodec.fromAscii0("00111111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
        )
        decoded = BinaryCodec.fromAscii0("01111111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = BinaryCodec.fromAscii0("11111111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits = bytearray(2)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = BinaryCodec.fromAscii0("0000000011111111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits[1] = self.__BIT_0
        decoded = BinaryCodec.fromAscii0("0000000111111111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits[1] = self.__BIT_0 | self.__BIT_1
        decoded = BinaryCodec.fromAscii0("0000001111111111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits[1] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        decoded = BinaryCodec.fromAscii0("0000011111111111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits[1] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        decoded = BinaryCodec.fromAscii0("0000111111111111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits[1] = (
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        )
        decoded = BinaryCodec.fromAscii0("0001111111111111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits[1] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
        )
        decoded = BinaryCodec.fromAscii0("0011111111111111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits[1] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
        )
        decoded = BinaryCodec.fromAscii0("0111111111111111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

    def testFromAsciiByteArray_test33_decomposed(self) -> None:
        self.assertEqual(0, len(self.instance.fromAscii0(None)))
        self.assertEqual(0, len(self.instance.fromAscii0([])))

        bits = bytearray(1)
        decoded = self.instance.fromAscii0("00000000".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits[0] = self.__BIT_0
        decoded = self.instance.fromAscii0("00000001".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits[0] = self.__BIT_0 | self.__BIT_1
        decoded = self.instance.fromAscii0("00000011".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        decoded = self.instance.fromAscii0("00000111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        decoded = self.instance.fromAscii0("00001111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits[0] = (
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        )
        decoded = self.instance.fromAscii0("00011111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
        )
        decoded = self.instance.fromAscii0("00111111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
        )
        decoded = self.instance.fromAscii0("01111111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = self.instance.fromAscii0("11111111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits = bytearray(2)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = self.instance.fromAscii0(
            "0000000011111111".encode(self.__CHARSET_UTF8)
        )
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits[1] = self.__BIT_0
        decoded = self.instance.fromAscii0(
            "0000000111111111".encode(self.__CHARSET_UTF8)
        )
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits[1] = self.__BIT_0 | self.__BIT_1
        decoded = self.instance.fromAscii0(
            "0000001111111111".encode(self.__CHARSET_UTF8)
        )
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits[1] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        decoded = self.instance.fromAscii0(
            "0000011111111111".encode(self.__CHARSET_UTF8)
        )
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits[1] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        decoded = self.instance.fromAscii0(
            "0000111111111111".encode(self.__CHARSET_UTF8)
        )
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits[1] = (
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        )
        decoded = self.instance.fromAscii0(
            "0001111111111111".encode(self.__CHARSET_UTF8)
        )
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits[1] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
        )
        decoded = self.instance.fromAscii0(
            "0011111111111111".encode(self.__CHARSET_UTF8)
        )
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits[1] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
        )
        decoded = self.instance.fromAscii0(
            "0111111111111111".encode(self.__CHARSET_UTF8)
        )
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

    def testFromAsciiByteArray_test32_decomposed(self) -> None:
        self.assertEqual(len(BinaryCodec.fromAscii0(None)), 0)
        self.assertEqual(len(BinaryCodec.fromAscii0([])), 0)

        bits = bytearray(1)
        decoded = BinaryCodec.fromAscii0("00000000".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits[0] = self.__BIT_0
        decoded = BinaryCodec.fromAscii0("00000001".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits[0] = self.__BIT_0 | self.__BIT_1
        decoded = BinaryCodec.fromAscii0("00000011".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        decoded = BinaryCodec.fromAscii0("00000111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        decoded = BinaryCodec.fromAscii0("00001111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits[0] = (
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        )
        decoded = BinaryCodec.fromAscii0("00011111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
        )
        decoded = BinaryCodec.fromAscii0("00111111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
        )
        decoded = BinaryCodec.fromAscii0("01111111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = BinaryCodec.fromAscii0("11111111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits = bytearray(2)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = BinaryCodec.fromAscii0("0000000011111111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits[1] = self.__BIT_0
        decoded = BinaryCodec.fromAscii0("0000000111111111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits[1] = self.__BIT_0 | self.__BIT_1
        decoded = BinaryCodec.fromAscii0("0000001111111111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits[1] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        decoded = BinaryCodec.fromAscii0("0000011111111111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits[1] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        decoded = BinaryCodec.fromAscii0("0000111111111111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits[1] = (
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        )
        decoded = BinaryCodec.fromAscii0("0001111111111111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits[1] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
        )
        decoded = BinaryCodec.fromAscii0("0011111111111111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

    def testFromAsciiByteArray_test31_decomposed(self) -> None:
        self.assertEqual(0, len(self.instance.fromAscii0(None)))
        self.assertEqual(0, len(self.instance.fromAscii0([])))

        bits = bytearray(1)
        decoded = self.instance.fromAscii0("00000000".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits[0] = self.__BIT_0
        decoded = self.instance.fromAscii0("00000001".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits[0] = self.__BIT_0 | self.__BIT_1
        decoded = self.instance.fromAscii0("00000011".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        decoded = self.instance.fromAscii0("00000111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        decoded = self.instance.fromAscii0("00001111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits[0] = (
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        )
        decoded = self.instance.fromAscii0("00011111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
        )
        decoded = self.instance.fromAscii0("00111111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
        )
        decoded = self.instance.fromAscii0("01111111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = self.instance.fromAscii0("11111111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits = bytearray(2)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = self.instance.fromAscii0(
            "0000000011111111".encode(self.__CHARSET_UTF8)
        )
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits[1] = self.__BIT_0
        decoded = self.instance.fromAscii0(
            "0000000111111111".encode(self.__CHARSET_UTF8)
        )
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits[1] = self.__BIT_0 | self.__BIT_1
        decoded = self.instance.fromAscii0(
            "0000001111111111".encode(self.__CHARSET_UTF8)
        )
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits[1] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        decoded = self.instance.fromAscii0(
            "0000011111111111".encode(self.__CHARSET_UTF8)
        )
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits[1] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        decoded = self.instance.fromAscii0(
            "0000111111111111".encode(self.__CHARSET_UTF8)
        )
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits[1] = (
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        )
        decoded = self.instance.fromAscii0(
            "0001111111111111".encode(self.__CHARSET_UTF8)
        )
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits[1] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
        )
        decoded = self.instance.fromAscii0(
            "0011111111111111".encode(self.__CHARSET_UTF8)
        )
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

    def testFromAsciiByteArray_test30_decomposed(self) -> None:
        self.assertEqual(0, len(self.instance.fromAscii0(None)))
        self.assertEqual(0, len(self.instance.fromAscii0([])))

        bits = bytearray(1)
        decoded = self.instance.fromAscii0("00000000".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits = bytearray(1)
        bits[0] = self.__BIT_0
        decoded = self.instance.fromAscii0("00000001".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1
        decoded = self.instance.fromAscii0("00000011".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        decoded = self.instance.fromAscii0("00000111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        decoded = self.instance.fromAscii0("00001111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        )
        decoded = self.instance.fromAscii0("00011111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
        )
        decoded = self.instance.fromAscii0("00111111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
        )
        decoded = self.instance.fromAscii0("01111111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = self.instance.fromAscii0("11111111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits = bytearray(2)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = self.instance.fromAscii0(
            "0000000011111111".encode(self.__CHARSET_UTF8)
        )
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits = bytearray(2)
        bits[1] = self.__BIT_0
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = self.instance.fromAscii0(
            "0000000111111111".encode(self.__CHARSET_UTF8)
        )
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits = bytearray(2)
        bits[1] = self.__BIT_0 | self.__BIT_1
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = self.instance.fromAscii0(
            "0000001111111111".encode(self.__CHARSET_UTF8)
        )
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits = bytearray(2)
        bits[1] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = self.instance.fromAscii0(
            "0000011111111111".encode(self.__CHARSET_UTF8)
        )
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits = bytearray(2)
        bits[1] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = self.instance.fromAscii0(
            "0000111111111111".encode(self.__CHARSET_UTF8)
        )
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits = bytearray(2)
        bits[1] = (
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        )
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = self.instance.fromAscii0(
            "0001111111111111".encode(self.__CHARSET_UTF8)
        )
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

    def testFromAsciiByteArray_test29_decomposed(self) -> None:
        self.assertEqual(0, len(self.instance.fromAscii0(None)))
        self.assertEqual(0, len(self.instance.fromAscii0([])))

        bits = bytearray(1)
        decoded = self.instance.fromAscii0("00000000".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits[0] = self.__BIT_0
        decoded = self.instance.fromAscii0("00000001".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits[0] = self.__BIT_0 | self.__BIT_1
        decoded = self.instance.fromAscii0("00000011".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        decoded = self.instance.fromAscii0("00000111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        decoded = self.instance.fromAscii0("00001111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits[0] = (
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        )
        decoded = self.instance.fromAscii0("00011111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
        )
        decoded = self.instance.fromAscii0("00111111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
        )
        decoded = self.instance.fromAscii0("01111111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = self.instance.fromAscii0("11111111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits = bytearray(2)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = self.instance.fromAscii0(
            "0000000011111111".encode(self.__CHARSET_UTF8)
        )
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits[1] = self.__BIT_0
        decoded = self.instance.fromAscii0(
            "0000000111111111".encode(self.__CHARSET_UTF8)
        )
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits[1] = self.__BIT_0 | self.__BIT_1
        decoded = self.instance.fromAscii0(
            "0000001111111111".encode(self.__CHARSET_UTF8)
        )
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits[1] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        decoded = self.instance.fromAscii0(
            "0000011111111111".encode(self.__CHARSET_UTF8)
        )
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits[1] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        decoded = self.instance.fromAscii0(
            "0000111111111111".encode(self.__CHARSET_UTF8)
        )
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits[1] = (
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        )
        decoded = self.instance.fromAscii0(
            "0001111111111111".encode(self.__CHARSET_UTF8)
        )
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

    def testFromAsciiByteArray_test28_decomposed(self) -> None:
        self.assertEqual(0, len(self.instance.fromAscii0(None)))
        self.assertEqual(0, len(self.instance.fromAscii0([])))

        bits = bytearray(1)
        decoded = self.instance.fromAscii0("00000000".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits[0] = self.__BIT_0
        decoded = self.instance.fromAscii0("00000001".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits[0] = self.__BIT_0 | self.__BIT_1
        decoded = self.instance.fromAscii0("00000011".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        decoded = self.instance.fromAscii0("00000111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        decoded = self.instance.fromAscii0("00001111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits[0] = (
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        )
        decoded = self.instance.fromAscii0("00011111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
        )
        decoded = self.instance.fromAscii0("00111111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
        )
        decoded = self.instance.fromAscii0("01111111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = self.instance.fromAscii0("11111111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits = bytearray(2)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = self.instance.fromAscii0(
            "0000000011111111".encode(self.__CHARSET_UTF8)
        )
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits[1] = self.__BIT_0
        decoded = self.instance.fromAscii0(
            "0000000111111111".encode(self.__CHARSET_UTF8)
        )
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits[1] = self.__BIT_0 | self.__BIT_1
        decoded = self.instance.fromAscii0(
            "0000001111111111".encode(self.__CHARSET_UTF8)
        )
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits[1] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        decoded = self.instance.fromAscii0(
            "0000011111111111".encode(self.__CHARSET_UTF8)
        )
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits[1] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        decoded = self.instance.fromAscii0(
            "0000111111111111".encode(self.__CHARSET_UTF8)
        )
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

    def testFromAsciiByteArray_test27_decomposed(self) -> None:
        self.assertEqual(len(self.instance.fromAscii0(None)), 0)
        self.assertEqual(len(self.instance.fromAscii0([])), 0)

        bits = bytearray(1)
        decoded = self.instance.fromAscii0("00000000".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits[0] = self.__BIT_0
        decoded = self.instance.fromAscii0("00000001".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits[0] = self.__BIT_0 | self.__BIT_1
        decoded = self.instance.fromAscii0("00000011".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        decoded = self.instance.fromAscii0("00000111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        decoded = self.instance.fromAscii0("00001111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits[0] = (
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        )
        decoded = self.instance.fromAscii0("00011111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
        )
        decoded = self.instance.fromAscii0("00111111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
        )
        decoded = self.instance.fromAscii0("01111111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = self.instance.fromAscii0("11111111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits = bytearray(2)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = self.instance.fromAscii0(
            "0000000011111111".encode(self.__CHARSET_UTF8)
        )
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits[1] = self.__BIT_0
        decoded = self.instance.fromAscii0(
            "0000000111111111".encode(self.__CHARSET_UTF8)
        )
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits[1] = self.__BIT_0 | self.__BIT_1
        decoded = self.instance.fromAscii0(
            "0000001111111111".encode(self.__CHARSET_UTF8)
        )
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits[1] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        decoded = self.instance.fromAscii0(
            "0000011111111111".encode(self.__CHARSET_UTF8)
        )
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits[1] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        decoded = self.instance.fromAscii0(
            "0000111111111111".encode(self.__CHARSET_UTF8)
        )
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

    def testFromAsciiByteArray_test26_decomposed(self) -> None:
        self.assertEqual(0, len(self.instance.fromAscii0(None)))
        self.assertEqual(0, len(self.instance.fromAscii0([])))

        bits = bytearray(1)
        decoded = self.instance.fromAscii0("00000000".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits = bytearray(1)
        bits[0] = self.__BIT_0
        decoded = self.instance.fromAscii0("00000001".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1
        decoded = self.instance.fromAscii0("00000011".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        decoded = self.instance.fromAscii0("00000111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        decoded = self.instance.fromAscii0("00001111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        )
        decoded = self.instance.fromAscii0("00011111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
        )
        decoded = self.instance.fromAscii0("00111111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
        )
        decoded = self.instance.fromAscii0("01111111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = self.instance.fromAscii0("11111111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits = bytearray(2)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = self.instance.fromAscii0(
            "0000000011111111".encode(self.__CHARSET_UTF8)
        )
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits = bytearray(2)
        bits[1] = self.__BIT_0
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = self.instance.fromAscii0(
            "0000000111111111".encode(self.__CHARSET_UTF8)
        )
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits = bytearray(2)
        bits[1] = self.__BIT_0 | self.__BIT_1
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = self.instance.fromAscii0(
            "0000001111111111".encode(self.__CHARSET_UTF8)
        )
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits = bytearray(2)
        bits[1] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = self.instance.fromAscii0(
            "0000011111111111".encode(self.__CHARSET_UTF8)
        )
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

    def testFromAsciiByteArray_test25_decomposed(self) -> None:
        self.assertEqual(0, len(self.instance.fromAscii0(None)))
        self.assertEqual(0, len(self.instance.fromAscii0([])))

        bits = bytearray(1)
        decoded = self.instance.fromAscii0("00000000".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits = bytearray(1)
        bits[0] = self.__BIT_0
        decoded = self.instance.fromAscii0("00000001".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1
        decoded = self.instance.fromAscii0("00000011".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        decoded = self.instance.fromAscii0("00000111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        decoded = self.instance.fromAscii0("00001111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        )
        decoded = self.instance.fromAscii0("00011111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
        )
        decoded = self.instance.fromAscii0("00111111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
        )
        decoded = self.instance.fromAscii0("01111111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = self.instance.fromAscii0("11111111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits = bytearray(2)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = self.instance.fromAscii0(
            "0000000011111111".encode(self.__CHARSET_UTF8)
        )
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits = bytearray(2)
        bits[1] = self.__BIT_0
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = self.instance.fromAscii0(
            "0000000111111111".encode(self.__CHARSET_UTF8)
        )
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits = bytearray(2)
        bits[1] = self.__BIT_0 | self.__BIT_1
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = self.instance.fromAscii0(
            "0000001111111111".encode(self.__CHARSET_UTF8)
        )
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits = bytearray(2)
        bits[1] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = self.instance.fromAscii0(
            "0000011111111111".encode(self.__CHARSET_UTF8)
        )
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

    def testFromAsciiByteArray_test24_decomposed(self) -> None:
        self.assertEqual(len(self.instance.fromAscii0(None)), 0)
        self.assertEqual(len(self.instance.fromAscii0([])), 0)

        bits = bytearray(1)
        decoded = self.instance.fromAscii0("00000000".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits = bytearray(1)
        bits[0] = self.__BIT_0
        decoded = self.instance.fromAscii0("00000001".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1
        decoded = self.instance.fromAscii0("00000011".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        decoded = self.instance.fromAscii0("00000111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        decoded = self.instance.fromAscii0("00001111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        )
        decoded = self.instance.fromAscii0("00011111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
        )
        decoded = self.instance.fromAscii0("00111111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
        )
        decoded = self.instance.fromAscii0("01111111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = self.instance.fromAscii0("11111111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits = bytearray(2)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = self.instance.fromAscii0(
            "0000000011111111".encode(self.__CHARSET_UTF8)
        )
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits = bytearray(2)
        bits[1] = self.__BIT_0
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = self.instance.fromAscii0(
            "0000000111111111".encode(self.__CHARSET_UTF8)
        )
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits = bytearray(2)
        bits[1] = self.__BIT_0 | self.__BIT_1
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = self.instance.fromAscii0(
            "0000001111111111".encode(self.__CHARSET_UTF8)
        )
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

    def testFromAsciiByteArray_test23_decomposed(self) -> None:
        self.assertEqual(0, len(self.instance.fromAscii0(None)))
        self.assertEqual(0, len(self.instance.fromAscii0([])))

        bits = bytearray(1)
        decoded = self.instance.fromAscii0("00000000".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits = bytearray(1)
        bits[0] = self.__BIT_0
        decoded = self.instance.fromAscii0("00000001".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1
        decoded = self.instance.fromAscii0("00000011".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        decoded = self.instance.fromAscii0("00000111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        decoded = self.instance.fromAscii0("00001111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        )
        decoded = self.instance.fromAscii0("00011111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
        )
        decoded = self.instance.fromAscii0("00111111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
        )
        decoded = self.instance.fromAscii0("01111111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = self.instance.fromAscii0("11111111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits = bytearray(2)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = self.instance.fromAscii0(
            "0000000011111111".encode(self.__CHARSET_UTF8)
        )
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits = bytearray(2)
        bits[1] = self.__BIT_0
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = self.instance.fromAscii0(
            "0000000111111111".encode(self.__CHARSET_UTF8)
        )
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits = bytearray(2)
        bits[1] = self.__BIT_0 | self.__BIT_1
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = self.instance.fromAscii0(
            "0000001111111111".encode(self.__CHARSET_UTF8)
        )
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

    def testFromAsciiByteArray_test22_decomposed(self) -> None:
        self.assertEqual(0, len(self.instance.fromAscii0(None)))
        self.assertEqual(0, len(self.instance.fromAscii0([])))

        bits = bytearray(1)
        decoded = self.instance.fromAscii0("00000000".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits = bytearray(1)
        bits[0] = self.__BIT_0
        decoded = self.instance.fromAscii0("00000001".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1
        decoded = self.instance.fromAscii0("00000011".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        decoded = self.instance.fromAscii0("00000111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        decoded = self.instance.fromAscii0("00001111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        )
        decoded = self.instance.fromAscii0("00011111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
        )
        decoded = self.instance.fromAscii0("00111111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
        )
        decoded = self.instance.fromAscii0("01111111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = self.instance.fromAscii0("11111111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits = bytearray(2)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = self.instance.fromAscii0(
            "0000000011111111".encode(self.__CHARSET_UTF8)
        )
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits = bytearray(2)
        bits[1] = self.__BIT_0
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = self.instance.fromAscii0(
            "0000000111111111".encode(self.__CHARSET_UTF8)
        )
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

    def testFromAsciiByteArray_test21_decomposed(self) -> None:
        self.assertEqual(0, len(self.instance.fromAscii0(None)))
        self.assertEqual(0, len(self.instance.fromAscii0([])))

        bits = bytearray(1)
        decoded = self.instance.fromAscii0("00000000".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits = bytearray(1)
        bits[0] = self.__BIT_0
        decoded = self.instance.fromAscii0("00000001".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1
        decoded = self.instance.fromAscii0("00000011".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        decoded = self.instance.fromAscii0("00000111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        decoded = self.instance.fromAscii0("00001111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        )
        decoded = self.instance.fromAscii0("00011111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
        )
        decoded = self.instance.fromAscii0("00111111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
        )
        decoded = self.instance.fromAscii0("01111111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = self.instance.fromAscii0("11111111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits = bytearray(2)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = self.instance.fromAscii0(
            "0000000011111111".encode(self.__CHARSET_UTF8)
        )
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits = bytearray(2)
        bits[1] = self.__BIT_0
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = self.instance.fromAscii0(
            "0000000111111111".encode(self.__CHARSET_UTF8)
        )
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

    def testFromAsciiByteArray_test20_decomposed(self) -> None:
        self.assertEqual(0, len(self.instance.fromAscii0(None)))
        self.assertEqual(0, len(self.instance.fromAscii0([])))

        bits = bytearray(1)
        decoded = self.instance.fromAscii0("00000000".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits = bytearray(1)
        bits[0] = self.__BIT_0
        decoded = self.instance.fromAscii0("00000001".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1
        decoded = self.instance.fromAscii0("00000011".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        decoded = self.instance.fromAscii0("00000111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        decoded = self.instance.fromAscii0("00001111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        )
        decoded = self.instance.fromAscii0("00011111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
        )
        decoded = self.instance.fromAscii0("00111111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
        )
        decoded = self.instance.fromAscii0("01111111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = self.instance.fromAscii0("11111111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits = bytearray(2)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = self.instance.fromAscii0(
            "0000000011111111".encode(self.__CHARSET_UTF8)
        )
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

    def testFromAsciiByteArray_test19_decomposed(self) -> None:
        self.assertEqual(0, len(self.instance.fromAscii0(None)))
        self.assertEqual(0, len(self.instance.fromAscii0([])))

        bits = bytearray(1)
        decoded = self.instance.fromAscii0("00000000".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits[0] = self.__BIT_0
        decoded = self.instance.fromAscii0("00000001".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits[0] = self.__BIT_0 | self.__BIT_1
        decoded = self.instance.fromAscii0("00000011".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        decoded = self.instance.fromAscii0("00000111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        decoded = self.instance.fromAscii0("00001111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits[0] = (
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        )
        decoded = self.instance.fromAscii0("00011111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
        )
        decoded = self.instance.fromAscii0("00111111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
        )
        decoded = self.instance.fromAscii0("01111111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = self.instance.fromAscii0("11111111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits = bytearray(2)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = self.instance.fromAscii0(
            "0000000011111111".encode(self.__CHARSET_UTF8)
        )
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

    def testFromAsciiByteArray_test18_decomposed(self) -> None:
        self.assertEqual(0, len(self.instance.fromAscii0(None)))
        self.assertEqual(0, len(self.instance.fromAscii0([])))

        bits = bytearray(1)
        decoded = self.instance.fromAscii0("00000000".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits = bytearray(1)
        bits[0] = self.__BIT_0
        decoded = self.instance.fromAscii0("00000001".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1
        decoded = self.instance.fromAscii0("00000011".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        decoded = self.instance.fromAscii0("00000111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        decoded = self.instance.fromAscii0("00001111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        )
        decoded = self.instance.fromAscii0("00011111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
        )
        decoded = self.instance.fromAscii0("00111111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
        )
        decoded = self.instance.fromAscii0("01111111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = self.instance.fromAscii0("11111111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

    def testFromAsciiByteArray_test17_decomposed(self) -> None:
        self.assertEqual(0, len(self.instance.fromAscii0(None)))
        self.assertEqual(0, len(self.instance.fromAscii0([])))

        bits = bytearray(1)
        decoded = self.instance.fromAscii0("00000000".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits = bytearray(1)
        bits[0] = self.__BIT_0
        decoded = self.instance.fromAscii0("00000001".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1
        decoded = self.instance.fromAscii0("00000011".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        decoded = self.instance.fromAscii0("00000111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        decoded = self.instance.fromAscii0("00001111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        )
        decoded = self.instance.fromAscii0("00011111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
        )
        decoded = self.instance.fromAscii0("00111111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
        )
        decoded = self.instance.fromAscii0("01111111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = self.instance.fromAscii0("11111111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

    def testFromAsciiByteArray_test16_decomposed(self) -> None:
        self.assertEqual(0, len(self.instance.fromAscii0(None)))
        self.assertEqual(0, len(self.instance.fromAscii0([])))

        bits = bytearray(1)
        decoded = self.instance.fromAscii0("00000000".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits = bytearray(1)
        bits[0] = self.__BIT_0
        decoded = self.instance.fromAscii0("00000001".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1
        decoded = self.instance.fromAscii0("00000011".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        decoded = self.instance.fromAscii0("00000111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        decoded = self.instance.fromAscii0("00001111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        )
        decoded = self.instance.fromAscii0("00011111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
        )
        decoded = self.instance.fromAscii0("00111111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
        )
        decoded = self.instance.fromAscii0("01111111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

    def testFromAsciiByteArray_test15_decomposed(self) -> None:
        self.assertEqual(0, len(BinaryCodec.fromAscii0(None)))
        self.assertEqual(0, len(BinaryCodec.fromAscii0([])))

        bits = bytearray(1)
        decoded = BinaryCodec.fromAscii0("00000000".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits = bytearray(1)
        bits[0] = self.__BIT_0
        decoded = BinaryCodec.fromAscii0("00000001".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1
        decoded = BinaryCodec.fromAscii0("00000011".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        decoded = BinaryCodec.fromAscii0("00000111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        decoded = BinaryCodec.fromAscii0("00001111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        )
        decoded = BinaryCodec.fromAscii0("00011111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
        )
        decoded = BinaryCodec.fromAscii0("00111111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
        )
        decoded = BinaryCodec.fromAscii0("01111111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

    def testFromAsciiByteArray_test14_decomposed(self) -> None:
        self.assertEqual(0, len(self.instance.fromAscii0(None)))
        self.assertEqual(0, len(self.instance.fromAscii0([])))

        bits = bytearray(1)
        decoded = self.instance.fromAscii0("00000000".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits = bytearray(1)
        bits[0] = self.__BIT_0
        decoded = self.instance.fromAscii0("00000001".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1
        decoded = self.instance.fromAscii0("00000011".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        decoded = self.instance.fromAscii0("00000111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        decoded = self.instance.fromAscii0("00001111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        )
        decoded = self.instance.fromAscii0("00011111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
        )
        decoded = self.instance.fromAscii0("00111111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

    def testFromAsciiByteArray_test13_decomposed(self) -> None:
        self.assertEqual(0, len(self.instance.fromAscii0(None)))
        self.assertEqual(0, len(self.instance.fromAscii0([])))

        bits = bytearray(1)
        decoded = self.instance.fromAscii0("00000000".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits = bytearray(1)
        bits[0] = self.__BIT_0
        decoded = self.instance.fromAscii0("00000001".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1
        decoded = self.instance.fromAscii0("00000011".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        decoded = self.instance.fromAscii0("00000111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        decoded = self.instance.fromAscii0("00001111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        )
        decoded = self.instance.fromAscii0("00011111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
        )
        decoded = self.instance.fromAscii0("00111111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

    def testFromAsciiByteArray_test12_decomposed(self) -> None:
        self.assertEqual(0, len(self.instance.fromAscii0(None)))
        self.assertEqual(0, len(self.instance.fromAscii0([])))

        bits = bytearray(1)
        decoded = self.instance.fromAscii0("00000000".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits = bytearray(1)
        bits[0] = self.__BIT_0
        decoded = self.instance.fromAscii0("00000001".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1
        decoded = self.instance.fromAscii0("00000011".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        decoded = self.instance.fromAscii0("00000111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        decoded = self.instance.fromAscii0("00001111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        )
        decoded = self.instance.fromAscii0("00011111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

    def testFromAsciiByteArray_test11_decomposed(self) -> None:
        self.assertEqual(0, len(self.instance.fromAscii0(None)))
        self.assertEqual(0, len(self.instance.fromAscii0([])))

        bits = bytearray(1)
        decoded = self.instance.fromAscii0("00000000".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits = bytearray(1)
        bits[0] = self.__BIT_0
        decoded = self.instance.fromAscii0("00000001".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1
        decoded = self.instance.fromAscii0("00000011".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        decoded = self.instance.fromAscii0("00000111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        decoded = self.instance.fromAscii0("00001111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        )
        decoded = self.instance.fromAscii0("00011111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

    def testFromAsciiByteArray_test10_decomposed(self) -> None:
        self.assertEqual(0, len(self.instance.fromAscii0(None)))
        self.assertEqual(0, len(self.instance.fromAscii0([])))

        bits = bytearray(1)
        decoded = self.instance.fromAscii0("00000000".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits = bytearray(1)
        bits[0] = self.__BIT_0
        decoded = self.instance.fromAscii0("00000001".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1
        decoded = self.instance.fromAscii0("00000011".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        decoded = self.instance.fromAscii0("00000111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        decoded = self.instance.fromAscii0("00001111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

    def testFromAsciiByteArray_test9_decomposed(self) -> None:
        self.assertEqual(0, len(BinaryCodec.fromAscii0(None)))
        self.assertEqual(0, len(BinaryCodec.fromAscii0([])))

        bits = bytearray(1)
        decoded = BinaryCodec.fromAscii0("00000000".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits = bytearray(1)
        bits[0] = self.__BIT_0
        decoded = BinaryCodec.fromAscii0("00000001".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1
        decoded = BinaryCodec.fromAscii0("00000011".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        decoded = BinaryCodec.fromAscii0("00000111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        decoded = BinaryCodec.fromAscii0("00001111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

    def testFromAsciiByteArray_test8_decomposed(self) -> None:
        self.assertEqual(0, len(BinaryCodec.fromAscii0(None)))
        self.assertEqual(0, len(BinaryCodec.fromAscii0([])))

        bits = bytearray(1)
        decoded = BinaryCodec.fromAscii0("00000000".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits = bytearray(1)
        bits[0] = self.__BIT_0
        decoded = BinaryCodec.fromAscii0("00000001".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1
        decoded = BinaryCodec.fromAscii0("00000011".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        decoded = BinaryCodec.fromAscii0("00000111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

    def testFromAsciiByteArray_test7_decomposed(self) -> None:
        self.assertEqual(0, len(self.instance.fromAscii0(None)))
        self.assertEqual(0, len(self.instance.fromAscii0([])))

        bits = bytearray(1)
        decoded = self.instance.fromAscii0("00000000".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits = bytearray(1)
        bits[0] = self.__BIT_0
        decoded = self.instance.fromAscii0("00000001".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1
        decoded = self.instance.fromAscii0("00000011".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        decoded = self.instance.fromAscii0("00000111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

    def testFromAsciiByteArray_test6_decomposed(self) -> None:
        self.assertEqual(0, len(BinaryCodec.fromAscii0(None)))
        self.assertEqual(0, len(BinaryCodec.fromAscii0([])))

        bits = bytearray(1)
        "00000000".encode(self.__CHARSET_UTF8)
        decoded = BinaryCodec.fromAscii0(list("00000000".encode(self.__CHARSET_UTF8)))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits = bytearray(1)
        bits[0] = self.__BIT_0
        "00000001".encode(self.__CHARSET_UTF8)
        decoded = BinaryCodec.fromAscii0(list("00000001".encode(self.__CHARSET_UTF8)))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1
        "00000011".encode(self.__CHARSET_UTF8)
        decoded = BinaryCodec.fromAscii0(list("00000011".encode(self.__CHARSET_UTF8)))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

    def testFromAsciiByteArray_test5_decomposed(self) -> None:
        self.assertEqual(0, len(BinaryCodec.fromAscii0(None)))
        self.assertEqual(0, len(BinaryCodec.fromAscii0([])))

        bits = bytearray(1)
        decoded = BinaryCodec.fromAscii0("00000000".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits = bytearray(1)
        bits[0] = self.__BIT_0
        decoded = BinaryCodec.fromAscii0("00000001".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1
        decoded = BinaryCodec.fromAscii0("00000011".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

    def testFromAsciiByteArray_test4_decomposed(self) -> None:
        self.assertEqual(0, len(BinaryCodec.fromAscii0(None)))
        self.assertEqual(0, len(BinaryCodec.fromAscii0([])))

        bits = bytearray(1)
        "00000000".encode(self.__CHARSET_UTF8)
        decoded = BinaryCodec.fromAscii0("00000000".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits = bytearray(1)
        bits[0] = self.__BIT_0
        "00000001".encode(self.__CHARSET_UTF8)
        decoded = BinaryCodec.fromAscii0("00000001".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

    def testFromAsciiByteArray_test3_decomposed(self) -> None:
        self.assertEqual(0, len(BinaryCodec.fromAscii0(None)))
        self.assertEqual(0, len(BinaryCodec.fromAscii0([])))

        bits = bytearray(1)
        "00000000".encode(self.__CHARSET_UTF8)
        decoded = BinaryCodec.fromAscii0("00000000".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8),
            bytearray(decoded).decode(self.__CHARSET_UTF8),
        )

        bits = bytearray(1)
        bits[0] = self.__BIT_0
        "00000001".encode(self.__CHARSET_UTF8)

    def testFromAsciiByteArray_test2_decomposed(self) -> None:
        self.assertEqual(0, len(BinaryCodec.fromAscii0(None)))
        self.assertEqual(0, len(BinaryCodec.fromAscii0([])))
        bits = bytearray(1)
        "00000000".encode(self.__CHARSET_UTF8)
        decoded = BinaryCodec.fromAscii0("00000000".encode(self.__CHARSET_UTF8))

    def testFromAsciiByteArray_test1_decomposed(self) -> None:
        self.assertEqual(0, len(BinaryCodec.fromAscii0(None)))
        self.assertEqual(0, len(BinaryCodec.fromAscii0([])))
        bits = bytearray(1)
        "00000000".encode(self.__CHARSET_UTF8)

    def testFromAsciiByteArray_test0_decomposed(self) -> None:
        self.assertEqual(0, len(BinaryCodec.fromAscii0(None)))
        self.assertEqual(0, len(BinaryCodec.fromAscii0([])))

    def testFromAsciiCharArray_test19_decomposed(self) -> None:
        self.assertEqual(0, len(BinaryCodec.fromAscii1(None)))
        self.assertEqual(0, len(BinaryCodec.fromAscii1([])))

        bits = bytearray(1)
        decoded = BinaryCodec.fromAscii1(list("00000000"))
        self.assertEqual(bits, bytearray(decoded))

        bits = bytearray(1)
        bits[0] = self.__BIT_0
        decoded = BinaryCodec.fromAscii1(list("00000001"))
        self.assertEqual(bits, bytearray(decoded))

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1
        decoded = BinaryCodec.fromAscii1(list("00000011"))
        self.assertEqual(bits, bytearray(decoded))

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        decoded = BinaryCodec.fromAscii1(list("00000111"))
        self.assertEqual(bits, bytearray(decoded))

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        decoded = BinaryCodec.fromAscii1(list("00001111"))
        self.assertEqual(bits, bytearray(decoded))

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        )
        decoded = BinaryCodec.fromAscii1(list("00011111"))
        self.assertEqual(bits, bytearray(decoded))

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
        )
        decoded = BinaryCodec.fromAscii1(list("00111111"))
        self.assertEqual(bits, bytearray(decoded))

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
        )
        decoded = BinaryCodec.fromAscii1(list("01111111"))
        self.assertEqual(bits, bytearray(decoded))

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = BinaryCodec.fromAscii1(list("11111111"))
        self.assertEqual(bits, bytearray(decoded))

        bits = bytearray(2)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = BinaryCodec.fromAscii1(list("0000000011111111"))
        self.assertEqual(bits, bytearray(decoded))

        bits = bytearray(2)
        bits[1] = self.__BIT_0
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = BinaryCodec.fromAscii1(list("0000000111111111"))
        self.assertEqual(bits, bytearray(decoded))

        bits = bytearray(2)
        bits[1] = self.__BIT_0 | self.__BIT_1
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = BinaryCodec.fromAscii1(list("0000001111111111"))
        self.assertEqual(bits, bytearray(decoded))

        bits = bytearray(2)
        bits[1] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = BinaryCodec.fromAscii1(list("0000011111111111"))
        self.assertEqual(bits, bytearray(decoded))

        bits = bytearray(2)
        bits[1] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = BinaryCodec.fromAscii1(list("0000111111111111"))
        self.assertEqual(bits, bytearray(decoded))

        bits = bytearray(2)
        bits[1] = (
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        )
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = BinaryCodec.fromAscii1(list("0001111111111111"))
        self.assertEqual(bits, bytearray(decoded))

        bits = bytearray(2)
        bits[1] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
        )
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = BinaryCodec.fromAscii1(list("0011111111111111"))
        self.assertEqual(bits, bytearray(decoded))

        bits = bytearray(2)
        bits[1] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
        )
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = BinaryCodec.fromAscii1(list("0111111111111111"))
        self.assertEqual(bits, bytearray(decoded))

        bits = bytearray(2)
        bits[1] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = BinaryCodec.fromAscii1(list("1111111111111111"))
        self.assertEqual(bits, bytearray(decoded))

        self.assertEqual(0, len(BinaryCodec.fromAscii1(None)))

    def testFromAsciiCharArray_test18_decomposed(self) -> None:
        self.assertEqual(len(BinaryCodec.fromAscii1(None)), 0)
        self.assertEqual(len(BinaryCodec.fromAscii1([])), 0)

        bits = bytearray(1)
        decoded = BinaryCodec.fromAscii1(list("00000000"))
        self.assertEqual(bytes(bits), bytes(decoded))

        bits = bytearray(1)
        bits[0] = self.__BIT_0
        decoded = BinaryCodec.fromAscii1(list("00000001"))
        self.assertEqual(bytes(bits), bytes(decoded))

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1
        decoded = BinaryCodec.fromAscii1(list("00000011"))
        self.assertEqual(bytes(bits), bytes(decoded))

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        decoded = BinaryCodec.fromAscii1(list("00000111"))
        self.assertEqual(bytes(bits), bytes(decoded))

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        decoded = BinaryCodec.fromAscii1(list("00001111"))
        self.assertEqual(bytes(bits), bytes(decoded))

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        )
        decoded = BinaryCodec.fromAscii1(list("00011111"))
        self.assertEqual(bytes(bits), bytes(decoded))

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
        )
        decoded = BinaryCodec.fromAscii1(list("00111111"))
        self.assertEqual(bytes(bits), bytes(decoded))

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
        )
        decoded = BinaryCodec.fromAscii1(list("01111111"))
        self.assertEqual(bytes(bits), bytes(decoded))

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = BinaryCodec.fromAscii1(list("11111111"))
        self.assertEqual(bytes(bits), bytes(decoded))

        bits = bytearray(2)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = BinaryCodec.fromAscii1(list("0000000011111111"))
        self.assertEqual(bytes(bits), bytes(decoded))

        bits = bytearray(2)
        bits[1] = self.__BIT_0
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = BinaryCodec.fromAscii1(list("0000000111111111"))
        self.assertEqual(bytes(bits), bytes(decoded))

        bits = bytearray(2)
        bits[1] = self.__BIT_0 | self.__BIT_1
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = BinaryCodec.fromAscii1(list("0000001111111111"))
        self.assertEqual(bytes(bits), bytes(decoded))

        bits = bytearray(2)
        bits[1] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = BinaryCodec.fromAscii1(list("0000011111111111"))
        self.assertEqual(bytes(bits), bytes(decoded))

        bits = bytearray(2)
        bits[1] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = BinaryCodec.fromAscii1(list("0000111111111111"))
        self.assertEqual(bytes(bits), bytes(decoded))

        bits = bytearray(2)
        bits[1] = (
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        )
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = BinaryCodec.fromAscii1(list("0001111111111111"))
        self.assertEqual(bytes(bits), bytes(decoded))

        bits = bytearray(2)
        bits[1] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
        )
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = BinaryCodec.fromAscii1(list("0011111111111111"))
        self.assertEqual(bytes(bits), bytes(decoded))

        bits = bytearray(2)
        bits[1] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
        )
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = BinaryCodec.fromAscii1(list("0111111111111111"))
        self.assertEqual(bytes(bits), bytes(decoded))

        bits = bytearray(2)
        bits[1] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = BinaryCodec.fromAscii1(list("1111111111111111"))
        self.assertEqual(bytes(bits), bytes(decoded))

    def testFromAsciiCharArray_test17_decomposed(self) -> None:
        self.assertEqual(0, len(BinaryCodec.fromAscii1(None)))
        self.assertEqual(0, len(BinaryCodec.fromAscii1([])))

        bits = bytearray(1)
        decoded = BinaryCodec.fromAscii1(list("00000000"))
        self.assertEqual(bits, bytearray(decoded))

        bits = bytearray(1)
        bits[0] = self.__BIT_0
        decoded = BinaryCodec.fromAscii1(list("00000001"))
        self.assertEqual(bits, bytearray(decoded))

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1
        decoded = BinaryCodec.fromAscii1(list("00000011"))
        self.assertEqual(bits, bytearray(decoded))

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        decoded = BinaryCodec.fromAscii1(list("00000111"))
        self.assertEqual(bits, bytearray(decoded))

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        decoded = BinaryCodec.fromAscii1(list("00001111"))
        self.assertEqual(bits, bytearray(decoded))

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        )
        decoded = BinaryCodec.fromAscii1(list("00011111"))
        self.assertEqual(bits, bytearray(decoded))

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
        )
        decoded = BinaryCodec.fromAscii1(list("00111111"))
        self.assertEqual(bits, bytearray(decoded))

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
        )
        decoded = BinaryCodec.fromAscii1(list("01111111"))
        self.assertEqual(bits, bytearray(decoded))

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = BinaryCodec.fromAscii1(list("11111111"))
        self.assertEqual(bits, bytearray(decoded))

        bits = bytearray(2)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = BinaryCodec.fromAscii1(list("0000000011111111"))
        self.assertEqual(bits, bytearray(decoded))

        bits = bytearray(2)
        bits[1] = self.__BIT_0
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = BinaryCodec.fromAscii1(list("0000000111111111"))
        self.assertEqual(bits, bytearray(decoded))

        bits = bytearray(2)
        bits[1] = self.__BIT_0 | self.__BIT_1
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = BinaryCodec.fromAscii1(list("0000001111111111"))
        self.assertEqual(bits, bytearray(decoded))

        bits = bytearray(2)
        bits[1] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = BinaryCodec.fromAscii1(list("0000011111111111"))
        self.assertEqual(bits, bytearray(decoded))

        bits = bytearray(2)
        bits[1] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = BinaryCodec.fromAscii1(list("0000111111111111"))
        self.assertEqual(bits, bytearray(decoded))

        bits = bytearray(2)
        bits[1] = (
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        )
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = BinaryCodec.fromAscii1(list("0001111111111111"))
        self.assertEqual(bits, bytearray(decoded))

        bits = bytearray(2)
        bits[1] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
        )
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = BinaryCodec.fromAscii1(list("0011111111111111"))
        self.assertEqual(bits, bytearray(decoded))

        bits = bytearray(2)
        bits[1] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
        )
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = BinaryCodec.fromAscii1(list("0111111111111111"))
        self.assertEqual(bits, bytearray(decoded))

    def testFromAsciiCharArray_test16_decomposed(self) -> None:
        self.assertEqual(len(BinaryCodec.fromAscii1(None)), 0)
        self.assertEqual(len(BinaryCodec.fromAscii1([])), 0)

        bits = bytearray(1)
        decoded = BinaryCodec.fromAscii1(list("00000000"))
        self.assertEqual(bytes(bits), bytes(decoded))

        bits = bytearray(1)
        bits[0] = self.__BIT_0
        decoded = BinaryCodec.fromAscii1(list("00000001"))
        self.assertEqual(bytes(bits), bytes(decoded))

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1
        decoded = BinaryCodec.fromAscii1(list("00000011"))
        self.assertEqual(bytes(bits), bytes(decoded))

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        decoded = BinaryCodec.fromAscii1(list("00000111"))
        self.assertEqual(bytes(bits), bytes(decoded))

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        decoded = BinaryCodec.fromAscii1(list("00001111"))
        self.assertEqual(bytes(bits), bytes(decoded))

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        )
        decoded = BinaryCodec.fromAscii1(list("00011111"))
        self.assertEqual(bytes(bits), bytes(decoded))

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
        )
        decoded = BinaryCodec.fromAscii1(list("00111111"))
        self.assertEqual(bytes(bits), bytes(decoded))

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
        )
        decoded = BinaryCodec.fromAscii1(list("01111111"))
        self.assertEqual(bytes(bits), bytes(decoded))

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = BinaryCodec.fromAscii1(list("11111111"))
        self.assertEqual(bytes(bits), bytes(decoded))

        bits = bytearray(2)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = BinaryCodec.fromAscii1(list("0000000011111111"))
        self.assertEqual(bytes(bits), bytes(decoded))

        bits = bytearray(2)
        bits[1] = self.__BIT_0
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = BinaryCodec.fromAscii1(list("0000000111111111"))
        self.assertEqual(bytes(bits), bytes(decoded))

        bits = bytearray(2)
        bits[1] = self.__BIT_0 | self.__BIT_1
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = BinaryCodec.fromAscii1(list("0000001111111111"))
        self.assertEqual(bytes(bits), bytes(decoded))

        bits = bytearray(2)
        bits[1] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = BinaryCodec.fromAscii1(list("0000011111111111"))
        self.assertEqual(bytes(bits), bytes(decoded))

        bits = bytearray(2)
        bits[1] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = BinaryCodec.fromAscii1(list("0000111111111111"))
        self.assertEqual(bytes(bits), bytes(decoded))

        bits = bytearray(2)
        bits[1] = (
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        )
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = BinaryCodec.fromAscii1(list("0001111111111111"))
        self.assertEqual(bytes(bits), bytes(decoded))

        bits = bytearray(2)
        bits[1] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
        )
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = BinaryCodec.fromAscii1(list("0011111111111111"))
        self.assertEqual(bytes(bits), bytes(decoded))

    def testFromAsciiCharArray_test15_decomposed(self) -> None:
        self.assertEqual(len(BinaryCodec.fromAscii1(None)), 0)
        self.assertEqual(len(BinaryCodec.fromAscii1([])), 0)

        bits = bytearray(1)
        decoded = BinaryCodec.fromAscii1(list("00000000"))
        self.assertEqual(bytes(bits), bytes(decoded))

        bits = bytearray(1)
        bits[0] = self.__BIT_0
        decoded = BinaryCodec.fromAscii1(list("00000001"))
        self.assertEqual(bytes(bits), bytes(decoded))

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1
        decoded = BinaryCodec.fromAscii1(list("00000011"))
        self.assertEqual(bytes(bits), bytes(decoded))

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        decoded = BinaryCodec.fromAscii1(list("00000111"))
        self.assertEqual(bytes(bits), bytes(decoded))

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        decoded = BinaryCodec.fromAscii1(list("00001111"))
        self.assertEqual(bytes(bits), bytes(decoded))

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        )
        decoded = BinaryCodec.fromAscii1(list("00011111"))
        self.assertEqual(bytes(bits), bytes(decoded))

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
        )
        decoded = BinaryCodec.fromAscii1(list("00111111"))
        self.assertEqual(bytes(bits), bytes(decoded))

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
        )
        decoded = BinaryCodec.fromAscii1(list("01111111"))
        self.assertEqual(bytes(bits), bytes(decoded))

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = BinaryCodec.fromAscii1(list("11111111"))
        self.assertEqual(bytes(bits), bytes(decoded))

        bits = bytearray(2)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = BinaryCodec.fromAscii1(list("0000000011111111"))
        self.assertEqual(bytes(bits), bytes(decoded))

        bits = bytearray(2)
        bits[1] = self.__BIT_0
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = BinaryCodec.fromAscii1(list("0000000111111111"))
        self.assertEqual(bytes(bits), bytes(decoded))

        bits = bytearray(2)
        bits[1] = self.__BIT_0 | self.__BIT_1
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = BinaryCodec.fromAscii1(list("0000001111111111"))
        self.assertEqual(bytes(bits), bytes(decoded))

        bits = bytearray(2)
        bits[1] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = BinaryCodec.fromAscii1(list("0000011111111111"))
        self.assertEqual(bytes(bits), bytes(decoded))

        bits = bytearray(2)
        bits[1] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = BinaryCodec.fromAscii1(list("0000111111111111"))
        self.assertEqual(bytes(bits), bytes(decoded))

        bits = bytearray(2)
        bits[1] = (
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        )
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = BinaryCodec.fromAscii1(list("0001111111111111"))
        self.assertEqual(bytes(bits), bytes(decoded))

    def testFromAsciiCharArray_test14_decomposed(self) -> None:
        self.assertEqual(len(BinaryCodec.fromAscii1(None)), 0)
        self.assertEqual(len(BinaryCodec.fromAscii1([])), 0)

        bits = bytearray(1)
        decoded = BinaryCodec.fromAscii1(list("00000000"))
        self.assertEqual(bits, bytearray(decoded))

        bits = bytearray(1)
        bits[0] = self.__BIT_0
        decoded = BinaryCodec.fromAscii1(list("00000001"))
        self.assertEqual(bits, bytearray(decoded))

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1
        decoded = BinaryCodec.fromAscii1(list("00000011"))
        self.assertEqual(bits, bytearray(decoded))

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        decoded = BinaryCodec.fromAscii1(list("00000111"))
        self.assertEqual(bits, bytearray(decoded))

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        decoded = BinaryCodec.fromAscii1(list("00001111"))
        self.assertEqual(bits, bytearray(decoded))

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        )
        decoded = BinaryCodec.fromAscii1(list("00011111"))
        self.assertEqual(bits, bytearray(decoded))

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
        )
        decoded = BinaryCodec.fromAscii1(list("00111111"))
        self.assertEqual(bits, bytearray(decoded))

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
        )
        decoded = BinaryCodec.fromAscii1(list("01111111"))
        self.assertEqual(bits, bytearray(decoded))

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = BinaryCodec.fromAscii1(list("11111111"))
        self.assertEqual(bits, bytearray(decoded))

        bits = bytearray(2)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = BinaryCodec.fromAscii1(list("0000000011111111"))
        self.assertEqual(bits, bytearray(decoded))

        bits = bytearray(2)
        bits[1] = self.__BIT_0
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = BinaryCodec.fromAscii1(list("0000000111111111"))
        self.assertEqual(bits, bytearray(decoded))

        bits = bytearray(2)
        bits[1] = self.__BIT_0 | self.__BIT_1
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = BinaryCodec.fromAscii1(list("0000001111111111"))
        self.assertEqual(bits, bytearray(decoded))

        bits = bytearray(2)
        bits[1] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = BinaryCodec.fromAscii1(list("0000011111111111"))
        self.assertEqual(bits, bytearray(decoded))

        bits = bytearray(2)
        bits[1] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = BinaryCodec.fromAscii1(list("0000111111111111"))
        self.assertEqual(bits, bytearray(decoded))

    def testFromAsciiCharArray_test13_decomposed(self) -> None:
        self.assertEqual(0, len(BinaryCodec.fromAscii1(None)))
        self.assertEqual(0, len(BinaryCodec.fromAscii1([])))

        bits = bytearray(1)
        decoded = BinaryCodec.fromAscii1(list("00000000"))
        self.assertEqual(bytes(bits), bytes(decoded))

        bits = bytearray(1)
        bits[0] = self.__BIT_0
        decoded = BinaryCodec.fromAscii1(list("00000001"))
        self.assertEqual(bytes(bits), bytes(decoded))

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1
        decoded = BinaryCodec.fromAscii1(list("00000011"))
        self.assertEqual(bytes(bits), bytes(decoded))

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        decoded = BinaryCodec.fromAscii1(list("00000111"))
        self.assertEqual(bytes(bits), bytes(decoded))

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        decoded = BinaryCodec.fromAscii1(list("00001111"))
        self.assertEqual(bytes(bits), bytes(decoded))

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        )
        decoded = BinaryCodec.fromAscii1(list("00011111"))
        self.assertEqual(bytes(bits), bytes(decoded))

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
        )
        decoded = BinaryCodec.fromAscii1(list("00111111"))
        self.assertEqual(bytes(bits), bytes(decoded))

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
        )
        decoded = BinaryCodec.fromAscii1(list("01111111"))
        self.assertEqual(bytes(bits), bytes(decoded))

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = BinaryCodec.fromAscii1(list("11111111"))
        self.assertEqual(bytes(bits), bytes(decoded))

        bits = bytearray(2)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = BinaryCodec.fromAscii1(list("0000000011111111"))
        self.assertEqual(bytes(bits), bytes(decoded))

        bits = bytearray(2)
        bits[1] = self.__BIT_0
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = BinaryCodec.fromAscii1(list("0000000111111111"))
        self.assertEqual(bytes(bits), bytes(decoded))

        bits = bytearray(2)
        bits[1] = self.__BIT_0 | self.__BIT_1
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = BinaryCodec.fromAscii1(list("0000001111111111"))
        self.assertEqual(bytes(bits), bytes(decoded))

        bits = bytearray(2)
        bits[1] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = BinaryCodec.fromAscii1(list("0000011111111111"))
        self.assertEqual(bytes(bits), bytes(decoded))

    def testFromAsciiCharArray_test12_decomposed(self) -> None:
        self.assertEqual(len(BinaryCodec.fromAscii1(None)), 0)
        self.assertEqual(len(BinaryCodec.fromAscii1([])), 0)

        bits = bytearray(1)
        decoded = BinaryCodec.fromAscii1(list("00000000"))
        self.assertEqual(bits.decode("latin1"), bytearray(decoded).decode("latin1"))

        bits = bytearray(1)
        bits[0] = self.__BIT_0
        decoded = BinaryCodec.fromAscii1(list("00000001"))
        self.assertEqual(bits.decode("latin1"), bytearray(decoded).decode("latin1"))

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1
        decoded = BinaryCodec.fromAscii1(list("00000011"))
        self.assertEqual(bits.decode("latin1"), bytearray(decoded).decode("latin1"))

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        decoded = BinaryCodec.fromAscii1(list("00000111"))
        self.assertEqual(bits.decode("latin1"), bytearray(decoded).decode("latin1"))

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        decoded = BinaryCodec.fromAscii1(list("00001111"))
        self.assertEqual(bits.decode("latin1"), bytearray(decoded).decode("latin1"))

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        )
        decoded = BinaryCodec.fromAscii1(list("00011111"))
        self.assertEqual(bits.decode("latin1"), bytearray(decoded).decode("latin1"))

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
        )
        decoded = BinaryCodec.fromAscii1(list("00111111"))
        self.assertEqual(bits.decode("latin1"), bytearray(decoded).decode("latin1"))

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
        )
        decoded = BinaryCodec.fromAscii1(list("01111111"))
        self.assertEqual(bits.decode("latin1"), bytearray(decoded).decode("latin1"))

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = BinaryCodec.fromAscii1(list("11111111"))
        self.assertEqual(bits.decode("latin1"), bytearray(decoded).decode("latin1"))

        bits = bytearray(2)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = BinaryCodec.fromAscii1(list("0000000011111111"))
        self.assertEqual(bits.decode("latin1"), bytearray(decoded).decode("latin1"))

        bits = bytearray(2)
        bits[1] = self.__BIT_0
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = BinaryCodec.fromAscii1(list("0000000111111111"))
        self.assertEqual(bits.decode("latin1"), bytearray(decoded).decode("latin1"))

        bits = bytearray(2)
        bits[1] = self.__BIT_0 | self.__BIT_1
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = BinaryCodec.fromAscii1(list("0000001111111111"))
        self.assertEqual(bits.decode("latin1"), bytearray(decoded).decode("latin1"))

    def testFromAsciiCharArray_test11_decomposed(self) -> None:
        self.assertEqual(0, len(BinaryCodec.fromAscii1(None)))
        self.assertEqual(0, len(BinaryCodec.fromAscii1([])))

        bits = bytearray(1)
        decoded = BinaryCodec.fromAscii1(list("00000000"))
        self.assertEqual(bits.decode("latin1"), bytearray(decoded).decode("latin1"))

        bits = bytearray(1)
        bits[0] = self.__BIT_0
        decoded = BinaryCodec.fromAscii1(list("00000001"))
        self.assertEqual(bits.decode("latin1"), bytearray(decoded).decode("latin1"))

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1
        decoded = BinaryCodec.fromAscii1(list("00000011"))
        self.assertEqual(bits.decode("latin1"), bytearray(decoded).decode("latin1"))

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        decoded = BinaryCodec.fromAscii1(list("00000111"))
        self.assertEqual(bits.decode("latin1"), bytearray(decoded).decode("latin1"))

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        decoded = BinaryCodec.fromAscii1(list("00001111"))
        self.assertEqual(bits.decode("latin1"), bytearray(decoded).decode("latin1"))

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        )
        decoded = BinaryCodec.fromAscii1(list("00011111"))
        self.assertEqual(bits.decode("latin1"), bytearray(decoded).decode("latin1"))

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
        )
        decoded = BinaryCodec.fromAscii1(list("00111111"))
        self.assertEqual(bits.decode("latin1"), bytearray(decoded).decode("latin1"))

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
        )
        decoded = BinaryCodec.fromAscii1(list("01111111"))
        self.assertEqual(bits.decode("latin1"), bytearray(decoded).decode("latin1"))

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = BinaryCodec.fromAscii1(list("11111111"))
        self.assertEqual(bits.decode("latin1"), bytearray(decoded).decode("latin1"))

        bits = bytearray(2)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = BinaryCodec.fromAscii1(list("0000000011111111"))
        self.assertEqual(bits.decode("latin1"), bytearray(decoded).decode("latin1"))

        bits = bytearray(2)
        bits[1] = self.__BIT_0
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = BinaryCodec.fromAscii1(list("0000000111111111"))
        self.assertEqual(bits.decode("latin1"), bytearray(decoded).decode("latin1"))

    def testFromAsciiCharArray_test10_decomposed(self) -> None:
        self.assertEqual(0, len(BinaryCodec.fromAscii1(None)))
        self.assertEqual(0, len(BinaryCodec.fromAscii1([])))

        bits = bytearray(1)
        decoded = BinaryCodec.fromAscii1(list("00000000"))
        self.assertEqual(bytes(bits), bytes(decoded))

        bits = bytearray(1)
        bits[0] = self.__BIT_0
        decoded = BinaryCodec.fromAscii1(list("00000001"))
        self.assertEqual(bytes(bits), bytes(decoded))

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1
        decoded = BinaryCodec.fromAscii1(list("00000011"))
        self.assertEqual(bytes(bits), bytes(decoded))

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        decoded = BinaryCodec.fromAscii1(list("00000111"))
        self.assertEqual(bytes(bits), bytes(decoded))

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        decoded = BinaryCodec.fromAscii1(list("00001111"))
        self.assertEqual(bytes(bits), bytes(decoded))

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        )
        decoded = BinaryCodec.fromAscii1(list("00011111"))
        self.assertEqual(bytes(bits), bytes(decoded))

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
        )
        decoded = BinaryCodec.fromAscii1(list("00111111"))
        self.assertEqual(bytes(bits), bytes(decoded))

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
        )
        decoded = BinaryCodec.fromAscii1(list("01111111"))
        self.assertEqual(bytes(bits), bytes(decoded))

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = BinaryCodec.fromAscii1(list("11111111"))
        self.assertEqual(bytes(bits), bytes(decoded))

        bits = bytearray(2)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = BinaryCodec.fromAscii1(list("0000000011111111"))
        self.assertEqual(bytes(bits), bytes(decoded))

    def testFromAsciiCharArray_test9_decomposed(self) -> None:
        self.assertEqual(0, len(BinaryCodec.fromAscii1(None)))
        self.assertEqual(0, len(BinaryCodec.fromAscii1([])))

        bits = bytearray(1)
        decoded = BinaryCodec.fromAscii1(list("00000000"))
        self.assertEqual(bytes(bits), bytes(decoded))

        bits = bytearray(1)
        bits[0] = self.__BIT_0
        decoded = BinaryCodec.fromAscii1(list("00000001"))
        self.assertEqual(bytes(bits), bytes(decoded))

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1
        decoded = BinaryCodec.fromAscii1(list("00000011"))
        self.assertEqual(bytes(bits), bytes(decoded))

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        decoded = BinaryCodec.fromAscii1(list("00000111"))
        self.assertEqual(bytes(bits), bytes(decoded))

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        decoded = BinaryCodec.fromAscii1(list("00001111"))
        self.assertEqual(bytes(bits), bytes(decoded))

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        )
        decoded = BinaryCodec.fromAscii1(list("00011111"))
        self.assertEqual(bytes(bits), bytes(decoded))

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
        )
        decoded = BinaryCodec.fromAscii1(list("00111111"))
        self.assertEqual(bytes(bits), bytes(decoded))

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
        )
        decoded = BinaryCodec.fromAscii1(list("01111111"))
        self.assertEqual(bytes(bits), bytes(decoded))

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = BinaryCodec.fromAscii1(list("11111111"))
        self.assertEqual(bytes(bits), bytes(decoded))

    def testFromAsciiCharArray_test8_decomposed(self) -> None:
        self.assertEqual(0, len(BinaryCodec.fromAscii1(None)))
        self.assertEqual(0, len(BinaryCodec.fromAscii1([])))

        bits = bytearray(1)
        decoded = BinaryCodec.fromAscii1(list("00000000"))
        self.assertEqual(bytes(bits), bytes(decoded))

        bits = bytearray(1)
        bits[0] = self.__BIT_0
        decoded = BinaryCodec.fromAscii1(list("00000001"))
        self.assertEqual(bytes(bits), bytes(decoded))

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1
        decoded = BinaryCodec.fromAscii1(list("00000011"))
        self.assertEqual(bytes(bits), bytes(decoded))

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        decoded = BinaryCodec.fromAscii1(list("00000111"))
        self.assertEqual(bytes(bits), bytes(decoded))

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        decoded = BinaryCodec.fromAscii1(list("00001111"))
        self.assertEqual(bytes(bits), bytes(decoded))

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        )
        decoded = BinaryCodec.fromAscii1(list("00011111"))
        self.assertEqual(bytes(bits), bytes(decoded))

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
        )
        decoded = BinaryCodec.fromAscii1(list("00111111"))
        self.assertEqual(bytes(bits), bytes(decoded))

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
        )
        decoded = BinaryCodec.fromAscii1(list("01111111"))
        self.assertEqual(bytes(bits), bytes(decoded))

    def testFromAsciiCharArray_test7_decomposed(self) -> None:
        self.assertEqual(0, len(self.instance.fromAscii1(None)))
        self.assertEqual(0, len(self.instance.fromAscii1([])))

        bits = bytearray(1)
        decoded = self.instance.fromAscii1(list("00000000"))
        self.assertEqual(bytes(bits), bytes(decoded))

        bits = bytearray(1)
        bits[0] = self.__BIT_0
        decoded = self.instance.fromAscii1(list("00000001"))
        self.assertEqual(bytes(bits), bytes(decoded))

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1
        decoded = self.instance.fromAscii1(list("00000011"))
        self.assertEqual(bytes(bits), bytes(decoded))

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        decoded = self.instance.fromAscii1(list("00000111"))
        self.assertEqual(bytes(bits), bytes(decoded))

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        decoded = self.instance.fromAscii1(list("00001111"))
        self.assertEqual(bytes(bits), bytes(decoded))

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        )
        decoded = self.instance.fromAscii1(list("00011111"))
        self.assertEqual(bytes(bits), bytes(decoded))

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
        )
        decoded = self.instance.fromAscii1(list("00111111"))
        self.assertEqual(bytes(bits), bytes(decoded))

    def testFromAsciiCharArray_test6_decomposed(self) -> None:
        self.assertEqual(0, len(BinaryCodec.fromAscii1(None)))
        self.assertEqual(0, len(BinaryCodec.fromAscii1([])))

        bits = bytearray(1)
        decoded = BinaryCodec.fromAscii1(list("00000000"))
        self.assertEqual(bytes(bits), bytes(decoded))

        bits = bytearray(1)
        bits[0] = self.__BIT_0
        decoded = BinaryCodec.fromAscii1(list("00000001"))
        self.assertEqual(bytes(bits), bytes(decoded))

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1
        decoded = BinaryCodec.fromAscii1(list("00000011"))
        self.assertEqual(bytes(bits), bytes(decoded))

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        decoded = BinaryCodec.fromAscii1(list("00000111"))
        self.assertEqual(bytes(bits), bytes(decoded))

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        decoded = BinaryCodec.fromAscii1(list("00001111"))
        self.assertEqual(bytes(bits), bytes(decoded))

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        )
        decoded = BinaryCodec.fromAscii1(list("00011111"))
        self.assertEqual(bytes(bits), bytes(decoded))

    def testFromAsciiCharArray_test5_decomposed(self) -> None:
        self.assertEqual(0, len(BinaryCodec.fromAscii1(None)))
        self.assertEqual(0, len(BinaryCodec.fromAscii1([])))

        bits = bytearray(1)
        decoded = BinaryCodec.fromAscii1(list("00000000"))
        self.assertEqual(bytes(bits), bytes(decoded))

        bits = bytearray(1)
        bits[0] = self.__BIT_0
        decoded = BinaryCodec.fromAscii1(list("00000001"))
        self.assertEqual(bytes(bits), bytes(decoded))

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1
        decoded = BinaryCodec.fromAscii1(list("00000011"))
        self.assertEqual(bytes(bits), bytes(decoded))

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        decoded = BinaryCodec.fromAscii1(list("00000111"))
        self.assertEqual(bytes(bits), bytes(decoded))

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        decoded = BinaryCodec.fromAscii1(list("00001111"))
        self.assertEqual(bytes(bits), bytes(decoded))

    def testFromAsciiCharArray_test4_decomposed(self) -> None:
        self.assertEqual(0, len(self.instance.fromAscii1(None)))
        self.assertEqual(0, len(self.instance.fromAscii1([])))

        bits = bytearray(1)
        decoded = self.instance.fromAscii1(list("00000000"))
        self.assertEqual(bytes(bits), bytes(decoded))

        bits = bytearray(1)
        bits[0] = self.__BIT_0
        decoded = self.instance.fromAscii1(list("00000001"))
        self.assertEqual(bytes(bits), bytes(decoded))

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1
        decoded = self.instance.fromAscii1(list("00000011"))
        self.assertEqual(bytes(bits), bytes(decoded))

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        decoded = self.instance.fromAscii1(list("00000111"))
        self.assertEqual(bytes(bits), bytes(decoded))

    def testFromAsciiCharArray_test3_decomposed(self) -> None:
        self.assertEqual(0, len(BinaryCodec.fromAscii1(None)))
        self.assertEqual(0, len(BinaryCodec.fromAscii1([])))

        bits = bytearray(1)
        decoded = BinaryCodec.fromAscii1(list("00000000"))
        self.assertEqual(bytes(bits), bytes(decoded))

        bits = bytearray(1)
        bits[0] = self.__BIT_0
        decoded = BinaryCodec.fromAscii1(list("00000001"))
        self.assertEqual(bytes(bits), bytes(decoded))

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1
        decoded = BinaryCodec.fromAscii1(list("00000011"))
        self.assertEqual(bytes(bits), bytes(decoded))

    def testFromAsciiCharArray_test2_decomposed(self) -> None:
        self.assertEqual(0, len(BinaryCodec.fromAscii1(None)))
        self.assertEqual(0, len(BinaryCodec.fromAscii1([])))

        bits = bytearray(1)
        decoded = BinaryCodec.fromAscii1(list("00000000"))
        self.assertEqual(bytes(bits), bytes(decoded))

        bits = bytearray(1)
        bits[0] = self.__BIT_0
        decoded = BinaryCodec.fromAscii1(list("00000001"))

    def testFromAsciiCharArray_test1_decomposed(self) -> None:
        self.assertEqual(0, len(BinaryCodec.fromAscii1(None)))
        self.assertEqual(0, len(BinaryCodec.fromAscii1([])))
        bits = [0]  # Equivalent to `byte[] bits = new byte[1];` in Java
        decoded = BinaryCodec.fromAscii1(list("00000000"))

    def testFromAsciiCharArray_test0_decomposed(self) -> None:
        self.assertEqual(0, len(BinaryCodec.fromAscii1(None)))
        self.assertEqual(0, len(BinaryCodec.fromAscii1([])))

    def testToByteArrayFromString_test18_decomposed(self) -> None:
        bits = bytearray(1)
        decoded = self.instance.toByteArray("00000000")
        self.assertEqual(bytes(bits).decode(), bytes(decoded).decode())

        bits = bytearray(1)
        bits[0] = self.__BIT_0
        decoded = self.instance.toByteArray("00000001")
        self.assertEqual(bytes(bits).decode(), bytes(decoded).decode())

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1
        decoded = self.instance.toByteArray("00000011")
        self.assertEqual(bytes(bits).decode(), bytes(decoded).decode())

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        decoded = self.instance.toByteArray("00000111")
        self.assertEqual(bytes(bits).decode(), bytes(decoded).decode())

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        decoded = self.instance.toByteArray("00001111")
        self.assertEqual(bytes(bits).decode(), bytes(decoded).decode())

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        )
        decoded = self.instance.toByteArray("00011111")
        self.assertEqual(bytes(bits).decode(), bytes(decoded).decode())

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
        )
        decoded = self.instance.toByteArray("00111111")
        self.assertEqual(bytes(bits).decode(), bytes(decoded).decode())

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
        )
        decoded = self.instance.toByteArray("01111111")
        self.assertEqual(bytes(bits).decode(), bytes(decoded).decode())

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = self.instance.toByteArray("11111111")
        self.assertEqual(bytes(bits).decode(), bytes(decoded).decode())

        bits = bytearray(2)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = self.instance.toByteArray("0000000011111111")
        self.assertEqual(bytes(bits).decode(), bytes(decoded).decode())

        bits = bytearray(2)
        bits[1] = self.__BIT_0
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = self.instance.toByteArray("0000000111111111")
        self.assertEqual(bytes(bits).decode(), bytes(decoded).decode())

        bits = bytearray(2)
        bits[1] = self.__BIT_0 | self.__BIT_1
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = self.instance.toByteArray("0000001111111111")
        self.assertEqual(bytes(bits).decode(), bytes(decoded).decode())

        bits = bytearray(2)
        bits[1] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = self.instance.toByteArray("0000011111111111")
        self.assertEqual(bytes(bits).decode(), bytes(decoded).decode())

        bits = bytearray(2)
        bits[1] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = self.instance.toByteArray("0000111111111111")
        self.assertEqual(bytes(bits).decode(), bytes(decoded).decode())

        bits = bytearray(2)
        bits[1] = (
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        )
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = self.instance.toByteArray("0001111111111111")
        self.assertEqual(bytes(bits).decode(), bytes(decoded).decode())

        bits = bytearray(2)
        bits[1] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
        )
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = self.instance.toByteArray("0011111111111111")
        self.assertEqual(bytes(bits).decode(), bytes(decoded).decode())

        bits = bytearray(2)
        bits[1] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
        )
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = self.instance.toByteArray("0111111111111111")
        self.assertEqual(bytes(bits).decode(), bytes(decoded).decode())

        bits = bytearray(2)
        bits[1] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = self.instance.toByteArray("1111111111111111")
        self.assertEqual(bytes(bits).decode(), bytes(decoded).decode())

        self.assertEqual(0, len(self.instance.toByteArray(None)))

    def testToByteArrayFromString_test17_decomposed(self) -> None:
        bits = bytearray(1)
        decoded = self.instance.toByteArray("00000000")
        self.assertEqual(bytes(bits).decode(), bytes(decoded).decode())

        bits = bytearray(1)
        bits[0] = self.__BIT_0
        decoded = self.instance.toByteArray("00000001")
        self.assertEqual(bytes(bits).decode(), bytes(decoded).decode())

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1
        decoded = self.instance.toByteArray("00000011")
        self.assertEqual(bytes(bits).decode(), bytes(decoded).decode())

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        decoded = self.instance.toByteArray("00000111")
        self.assertEqual(bytes(bits).decode(), bytes(decoded).decode())

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        decoded = self.instance.toByteArray("00001111")
        self.assertEqual(bytes(bits).decode(), bytes(decoded).decode())

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        )
        decoded = self.instance.toByteArray("00011111")
        self.assertEqual(bytes(bits).decode(), bytes(decoded).decode())

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
        )
        decoded = self.instance.toByteArray("00111111")
        self.assertEqual(bytes(bits).decode(), bytes(decoded).decode())

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
        )
        decoded = self.instance.toByteArray("01111111")
        self.assertEqual(bytes(bits).decode(), bytes(decoded).decode())

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = self.instance.toByteArray("11111111")
        self.assertEqual(bytes(bits).decode(), bytes(decoded).decode())

        bits = bytearray(2)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = self.instance.toByteArray("0000000011111111")
        self.assertEqual(bytes(bits).decode(), bytes(decoded).decode())

        bits = bytearray(2)
        bits[1] = self.__BIT_0
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = self.instance.toByteArray("0000000111111111")
        self.assertEqual(bytes(bits).decode(), bytes(decoded).decode())

        bits = bytearray(2)
        bits[1] = self.__BIT_0 | self.__BIT_1
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = self.instance.toByteArray("0000001111111111")
        self.assertEqual(bytes(bits).decode(), bytes(decoded).decode())

        bits = bytearray(2)
        bits[1] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = self.instance.toByteArray("0000011111111111")
        self.assertEqual(bytes(bits).decode(), bytes(decoded).decode())

        bits = bytearray(2)
        bits[1] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = self.instance.toByteArray("0000111111111111")
        self.assertEqual(bytes(bits).decode(), bytes(decoded).decode())

        bits = bytearray(2)
        bits[1] = (
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        )
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = self.instance.toByteArray("0001111111111111")
        self.assertEqual(bytes(bits).decode(), bytes(decoded).decode())

        bits = bytearray(2)
        bits[1] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
        )
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = self.instance.toByteArray("0011111111111111")
        self.assertEqual(bytes(bits).decode(), bytes(decoded).decode())

        bits = bytearray(2)
        bits[1] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
        )
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = self.instance.toByteArray("0111111111111111")
        self.assertEqual(bytes(bits).decode(), bytes(decoded).decode())

        bits = bytearray(2)
        bits[1] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = self.instance.toByteArray("1111111111111111")
        self.assertEqual(bytes(bits).decode(), bytes(decoded).decode())

    def testToByteArrayFromString_test16_decomposed(self) -> None:
        bits = bytearray(1)
        decoded = self.instance.toByteArray("00000000")
        self.assertEqual(bytes(bits), bytes(decoded))

        bits = bytearray(1)
        bits[0] = self.__BIT_0
        decoded = self.instance.toByteArray("00000001")
        self.assertEqual(bytes(bits), bytes(decoded))

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1
        decoded = self.instance.toByteArray("00000011")
        self.assertEqual(bytes(bits), bytes(decoded))

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        decoded = self.instance.toByteArray("00000111")
        self.assertEqual(bytes(bits), bytes(decoded))

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        decoded = self.instance.toByteArray("00001111")
        self.assertEqual(bytes(bits), bytes(decoded))

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        )
        decoded = self.instance.toByteArray("00011111")
        self.assertEqual(bytes(bits), bytes(decoded))

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
        )
        decoded = self.instance.toByteArray("00111111")
        self.assertEqual(bytes(bits), bytes(decoded))

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
        )
        decoded = self.instance.toByteArray("01111111")
        self.assertEqual(bytes(bits), bytes(decoded))

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = self.instance.toByteArray("11111111")
        self.assertEqual(bytes(bits), bytes(decoded))

        bits = bytearray(2)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = self.instance.toByteArray("0000000011111111")
        self.assertEqual(bytes(bits), bytes(decoded))

        bits = bytearray(2)
        bits[1] = self.__BIT_0
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = self.instance.toByteArray("0000000111111111")
        self.assertEqual(bytes(bits), bytes(decoded))

        bits = bytearray(2)
        bits[1] = self.__BIT_0 | self.__BIT_1
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = self.instance.toByteArray("0000001111111111")
        self.assertEqual(bytes(bits), bytes(decoded))

        bits = bytearray(2)
        bits[1] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = self.instance.toByteArray("0000011111111111")
        self.assertEqual(bytes(bits), bytes(decoded))

        bits = bytearray(2)
        bits[1] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = self.instance.toByteArray("0000111111111111")
        self.assertEqual(bytes(bits), bytes(decoded))

        bits = bytearray(2)
        bits[1] = (
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        )
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = self.instance.toByteArray("0001111111111111")
        self.assertEqual(bytes(bits), bytes(decoded))

        bits = bytearray(2)
        bits[1] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
        )
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = self.instance.toByteArray("0011111111111111")
        self.assertEqual(bytes(bits), bytes(decoded))

        bits = bytearray(2)
        bits[1] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
        )
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = self.instance.toByteArray("0111111111111111")
        self.assertEqual(bytes(bits), bytes(decoded))

    def testToByteArrayFromString_test15_decomposed(self) -> None:
        bits = bytearray(1)
        decoded = self.instance.toByteArray("00000000")
        self.assertEqual(bytes(bits), bytes(decoded))

        bits = bytearray(1)
        bits[0] = self.__BIT_0
        decoded = self.instance.toByteArray("00000001")
        self.assertEqual(bytes(bits), bytes(decoded))

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1
        decoded = self.instance.toByteArray("00000011")
        self.assertEqual(bytes(bits), bytes(decoded))

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        decoded = self.instance.toByteArray("00000111")
        self.assertEqual(bytes(bits), bytes(decoded))

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        decoded = self.instance.toByteArray("00001111")
        self.assertEqual(bytes(bits), bytes(decoded))

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        )
        decoded = self.instance.toByteArray("00011111")
        self.assertEqual(bytes(bits), bytes(decoded))

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
        )
        decoded = self.instance.toByteArray("00111111")
        self.assertEqual(bytes(bits), bytes(decoded))

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
        )
        decoded = self.instance.toByteArray("01111111")
        self.assertEqual(bytes(bits), bytes(decoded))

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = self.instance.toByteArray("11111111")
        self.assertEqual(bytes(bits), bytes(decoded))

        bits = bytearray(2)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = self.instance.toByteArray("0000000011111111")
        self.assertEqual(bytes(bits), bytes(decoded))

        bits = bytearray(2)
        bits[1] = self.__BIT_0
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = self.instance.toByteArray("0000000111111111")
        self.assertEqual(bytes(bits), bytes(decoded))

        bits = bytearray(2)
        bits[1] = self.__BIT_0 | self.__BIT_1
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = self.instance.toByteArray("0000001111111111")
        self.assertEqual(bytes(bits), bytes(decoded))

        bits = bytearray(2)
        bits[1] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = self.instance.toByteArray("0000011111111111")
        self.assertEqual(bytes(bits), bytes(decoded))

        bits = bytearray(2)
        bits[1] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = self.instance.toByteArray("0000111111111111")
        self.assertEqual(bytes(bits), bytes(decoded))

        bits = bytearray(2)
        bits[1] = (
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        )
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = self.instance.toByteArray("0001111111111111")
        self.assertEqual(bytes(bits), bytes(decoded))

        bits = bytearray(2)
        bits[1] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
        )
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = self.instance.toByteArray("0011111111111111")
        self.assertEqual(bytes(bits), bytes(decoded))

    def testToByteArrayFromString_test14_decomposed(self) -> None:
        bits = bytearray(1)
        decoded = self.instance.toByteArray("00000000")
        self.assertEqual(bytes(bits), bytes(decoded))

        bits = bytearray(1)
        bits[0] = self.__BIT_0
        decoded = self.instance.toByteArray("00000001")
        self.assertEqual(bytes(bits), bytes(decoded))

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1
        decoded = self.instance.toByteArray("00000011")
        self.assertEqual(bytes(bits), bytes(decoded))

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        decoded = self.instance.toByteArray("00000111")
        self.assertEqual(bytes(bits), bytes(decoded))

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        decoded = self.instance.toByteArray("00001111")
        self.assertEqual(bytes(bits), bytes(decoded))

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        )
        decoded = self.instance.toByteArray("00011111")
        self.assertEqual(bytes(bits), bytes(decoded))

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
        )
        decoded = self.instance.toByteArray("00111111")
        self.assertEqual(bytes(bits), bytes(decoded))

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
        )
        decoded = self.instance.toByteArray("01111111")
        self.assertEqual(bytes(bits), bytes(decoded))

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = self.instance.toByteArray("11111111")
        self.assertEqual(bytes(bits), bytes(decoded))

        bits = bytearray(2)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = self.instance.toByteArray("0000000011111111")
        self.assertEqual(bytes(bits), bytes(decoded))

        bits = bytearray(2)
        bits[1] = self.__BIT_0
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = self.instance.toByteArray("0000000111111111")
        self.assertEqual(bytes(bits), bytes(decoded))

        bits = bytearray(2)
        bits[1] = self.__BIT_0 | self.__BIT_1
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = self.instance.toByteArray("0000001111111111")
        self.assertEqual(bytes(bits), bytes(decoded))

        bits = bytearray(2)
        bits[1] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = self.instance.toByteArray("0000011111111111")
        self.assertEqual(bytes(bits), bytes(decoded))

        bits = bytearray(2)
        bits[1] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = self.instance.toByteArray("0000111111111111")
        self.assertEqual(bytes(bits), bytes(decoded))

        bits = bytearray(2)
        bits[1] = (
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        )
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = self.instance.toByteArray("0001111111111111")
        self.assertEqual(bytes(bits), bytes(decoded))

    def testToByteArrayFromString_test13_decomposed(self) -> None:
        bits = bytearray(1)
        decoded = self.instance.toByteArray("00000000")
        self.assertEqual(bytes(bits).decode(), bytes(decoded).decode())

        bits = bytearray(1)
        bits[0] = self.__BIT_0
        decoded = self.instance.toByteArray("00000001")
        self.assertEqual(bytes(bits).decode(), bytes(decoded).decode())

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1
        decoded = self.instance.toByteArray("00000011")
        self.assertEqual(bytes(bits).decode(), bytes(decoded).decode())

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        decoded = self.instance.toByteArray("00000111")
        self.assertEqual(bytes(bits).decode(), bytes(decoded).decode())

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        decoded = self.instance.toByteArray("00001111")
        self.assertEqual(bytes(bits).decode(), bytes(decoded).decode())

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        )
        decoded = self.instance.toByteArray("00011111")
        self.assertEqual(bytes(bits).decode(), bytes(decoded).decode())

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
        )
        decoded = self.instance.toByteArray("00111111")
        self.assertEqual(bytes(bits).decode(), bytes(decoded).decode())

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
        )
        decoded = self.instance.toByteArray("01111111")
        self.assertEqual(bytes(bits).decode(), bytes(decoded).decode())

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = self.instance.toByteArray("11111111")
        self.assertEqual(bytes(bits).decode(), bytes(decoded).decode())

        bits = bytearray(2)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = self.instance.toByteArray("0000000011111111")
        self.assertEqual(bytes(bits).decode(), bytes(decoded).decode())

        bits = bytearray(2)
        bits[1] = self.__BIT_0
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = self.instance.toByteArray("0000000111111111")
        self.assertEqual(bytes(bits).decode(), bytes(decoded).decode())

        bits = bytearray(2)
        bits[1] = self.__BIT_0 | self.__BIT_1
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = self.instance.toByteArray("0000001111111111")
        self.assertEqual(bytes(bits).decode(), bytes(decoded).decode())

        bits = bytearray(2)
        bits[1] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = self.instance.toByteArray("0000011111111111")
        self.assertEqual(bytes(bits).decode(), bytes(decoded).decode())

        bits = bytearray(2)
        bits[1] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = self.instance.toByteArray("0000111111111111")
        self.assertEqual(bytes(bits).decode(), bytes(decoded).decode())

    def testToByteArrayFromString_test12_decomposed(self) -> None:
        bits = bytearray(1)
        decoded = self.instance.toByteArray("00000000")
        self.assertEqual(bytes(bits).decode(), bytes(decoded).decode())

        bits = bytearray(1)
        bits[0] = self.__BIT_0
        decoded = self.instance.toByteArray("00000001")
        self.assertEqual(bytes(bits).decode(), bytes(decoded).decode())

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1
        decoded = self.instance.toByteArray("00000011")
        self.assertEqual(bytes(bits).decode(), bytes(decoded).decode())

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        decoded = self.instance.toByteArray("00000111")
        self.assertEqual(bytes(bits).decode(), bytes(decoded).decode())

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        decoded = self.instance.toByteArray("00001111")
        self.assertEqual(bytes(bits).decode(), bytes(decoded).decode())

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        )
        decoded = self.instance.toByteArray("00011111")
        self.assertEqual(bytes(bits).decode(), bytes(decoded).decode())

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
        )
        decoded = self.instance.toByteArray("00111111")
        self.assertEqual(bytes(bits).decode(), bytes(decoded).decode())

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
        )
        decoded = self.instance.toByteArray("01111111")
        self.assertEqual(bytes(bits).decode(), bytes(decoded).decode())

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = self.instance.toByteArray("11111111")
        self.assertEqual(bytes(bits).decode(), bytes(decoded).decode())

        bits = bytearray(2)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = self.instance.toByteArray("0000000011111111")
        self.assertEqual(bytes(bits).decode(), bytes(decoded).decode())

        bits = bytearray(2)
        bits[1] = self.__BIT_0
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = self.instance.toByteArray("0000000111111111")
        self.assertEqual(bytes(bits).decode(), bytes(decoded).decode())

        bits = bytearray(2)
        bits[1] = self.__BIT_0 | self.__BIT_1
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = self.instance.toByteArray("0000001111111111")
        self.assertEqual(bytes(bits).decode(), bytes(decoded).decode())

        bits = bytearray(2)
        bits[1] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = self.instance.toByteArray("0000011111111111")
        self.assertEqual(bytes(bits).decode(), bytes(decoded).decode())

    def testToByteArrayFromString_test11_decomposed(self) -> None:
        bits = bytearray(1)
        decoded = self.instance.toByteArray("00000000")
        self.assertEqual(str(bits), str(decoded))

        bits = bytearray(1)
        bits[0] = self.__BIT_0
        decoded = self.instance.toByteArray("00000001")
        self.assertEqual(str(bits), str(decoded))

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1
        decoded = self.instance.toByteArray("00000011")
        self.assertEqual(str(bits), str(decoded))

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        decoded = self.instance.toByteArray("00000111")
        self.assertEqual(str(bits), str(decoded))

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        decoded = self.instance.toByteArray("00001111")
        self.assertEqual(str(bits), str(decoded))

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        )
        decoded = self.instance.toByteArray("00011111")
        self.assertEqual(str(bits), str(decoded))

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
        )
        decoded = self.instance.toByteArray("00111111")
        self.assertEqual(str(bits), str(decoded))

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
        )
        decoded = self.instance.toByteArray("01111111")
        self.assertEqual(str(bits), str(decoded))

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = self.instance.toByteArray("11111111")
        self.assertEqual(str(bits), str(decoded))

        bits = bytearray(2)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = self.instance.toByteArray("0000000011111111")
        self.assertEqual(str(bits), str(decoded))

        bits = bytearray(2)
        bits[1] = self.__BIT_0
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = self.instance.toByteArray("0000000111111111")
        self.assertEqual(str(bits), str(decoded))

        bits = bytearray(2)
        bits[1] = self.__BIT_0 | self.__BIT_1
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = self.instance.toByteArray("0000001111111111")
        self.assertEqual(str(bits), str(decoded))

    def testToByteArrayFromString_test10_decomposed(self) -> None:
        bits = bytearray(1)
        decoded = self.instance.toByteArray("00000000")
        self.assertEqual(str(bits), str(decoded))

        bits = bytearray(1)
        bits[0] = self.__BIT_0
        decoded = self.instance.toByteArray("00000001")
        self.assertEqual(str(bits), str(decoded))

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1
        decoded = self.instance.toByteArray("00000011")
        self.assertEqual(str(bits), str(decoded))

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        decoded = self.instance.toByteArray("00000111")
        self.assertEqual(str(bits), str(decoded))

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        decoded = self.instance.toByteArray("00001111")
        self.assertEqual(str(bits), str(decoded))

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        )
        decoded = self.instance.toByteArray("00011111")
        self.assertEqual(str(bits), str(decoded))

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
        )
        decoded = self.instance.toByteArray("00111111")
        self.assertEqual(str(bits), str(decoded))

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
        )
        decoded = self.instance.toByteArray("01111111")
        self.assertEqual(str(bits), str(decoded))

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = self.instance.toByteArray("11111111")
        self.assertEqual(str(bits), str(decoded))

        bits = bytearray(2)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = self.instance.toByteArray("0000000011111111")
        self.assertEqual(str(bits), str(decoded))

        bits = bytearray(2)
        bits[1] = self.__BIT_0
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = self.instance.toByteArray("0000000111111111")
        self.assertEqual(str(bits), str(decoded))

    def testToByteArrayFromString_test9_decomposed(self) -> None:
        bits = bytearray(1)
        decoded = self.instance.toByteArray("00000000")
        self.assertEqual(str(bits), str(bytearray(decoded)))

        bits = bytearray(1)
        bits[0] = self.__BIT_0
        decoded = self.instance.toByteArray("00000001")
        self.assertEqual(str(bits), str(bytearray(decoded)))

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1
        decoded = self.instance.toByteArray("00000011")
        self.assertEqual(str(bits), str(bytearray(decoded)))

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        decoded = self.instance.toByteArray("00000111")
        self.assertEqual(str(bits), str(bytearray(decoded)))

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        decoded = self.instance.toByteArray("00001111")
        self.assertEqual(str(bits), str(bytearray(decoded)))

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        )
        decoded = self.instance.toByteArray("00011111")
        self.assertEqual(str(bits), str(bytearray(decoded)))

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
        )
        decoded = self.instance.toByteArray("00111111")
        self.assertEqual(str(bits), str(bytearray(decoded)))

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
        )
        decoded = self.instance.toByteArray("01111111")
        self.assertEqual(str(bits), str(bytearray(decoded)))

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = self.instance.toByteArray("11111111")
        self.assertEqual(str(bits), str(bytearray(decoded)))

        bits = bytearray(2)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = self.instance.toByteArray("0000000011111111")
        self.assertEqual(str(bits), str(bytearray(decoded)))

    def testToByteArrayFromString_test8_decomposed(self) -> None:
        bits = bytearray(1)
        decoded = self.instance.toByteArray("00000000")
        self.assertEqual(str(bits), str(decoded))

        bits = bytearray(1)
        bits[0] = self.__BIT_0
        decoded = self.instance.toByteArray("00000001")
        self.assertEqual(str(bits), str(decoded))

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1
        decoded = self.instance.toByteArray("00000011")
        self.assertEqual(str(bits), str(decoded))

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        decoded = self.instance.toByteArray("00000111")
        self.assertEqual(str(bits), str(decoded))

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        decoded = self.instance.toByteArray("00001111")
        self.assertEqual(str(bits), str(decoded))

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        )
        decoded = self.instance.toByteArray("00011111")
        self.assertEqual(str(bits), str(decoded))

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
        )
        decoded = self.instance.toByteArray("00111111")
        self.assertEqual(str(bits), str(decoded))

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
        )
        decoded = self.instance.toByteArray("01111111")
        self.assertEqual(str(bits), str(decoded))

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = self.instance.toByteArray("11111111")
        self.assertEqual(str(bits), str(decoded))

    def testToByteArrayFromString_test7_decomposed(self) -> None:
        bits = bytearray(1)
        decoded = self.instance.toByteArray("00000000")
        self.assertEqual(str(bits), str(decoded))

        bits = bytearray(1)
        bits[0] = self.__BIT_0
        decoded = self.instance.toByteArray("00000001")
        self.assertEqual(str(bits), str(decoded))

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1
        decoded = self.instance.toByteArray("00000011")
        self.assertEqual(str(bits), str(decoded))

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        decoded = self.instance.toByteArray("00000111")
        self.assertEqual(str(bits), str(decoded))

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        decoded = self.instance.toByteArray("00001111")
        self.assertEqual(str(bits), str(decoded))

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        )
        decoded = self.instance.toByteArray("00011111")
        self.assertEqual(str(bits), str(decoded))

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
        )
        decoded = self.instance.toByteArray("00111111")
        self.assertEqual(str(bits), str(decoded))

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
        )
        decoded = self.instance.toByteArray("01111111")
        self.assertEqual(str(bits), str(decoded))

    def testToByteArrayFromString_test6_decomposed(self) -> None:
        bits = bytearray(1)
        decoded = self.instance.toByteArray("00000000")
        self.assertEqual(str(bits), str(decoded))

        bits = bytearray(1)
        bits[0] = self.__BIT_0
        decoded = self.instance.toByteArray("00000001")
        self.assertEqual(str(bits), str(decoded))

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1
        decoded = self.instance.toByteArray("00000011")
        self.assertEqual(str(bits), str(decoded))

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        decoded = self.instance.toByteArray("00000111")
        self.assertEqual(str(bits), str(decoded))

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        decoded = self.instance.toByteArray("00001111")
        self.assertEqual(str(bits), str(decoded))

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        )
        decoded = self.instance.toByteArray("00011111")
        self.assertEqual(str(bits), str(decoded))

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
        )
        decoded = self.instance.toByteArray("00111111")
        self.assertEqual(str(bits), str(decoded))

    def testToByteArrayFromString_test5_decomposed(self) -> None:
        bits = bytearray(1)
        decoded = self.instance.toByteArray("00000000")
        self.assertEqual(str(bits), str(decoded))

        bits = bytearray(1)
        bits[0] = self.__BIT_0
        decoded = self.instance.toByteArray("00000001")
        self.assertEqual(str(bits), str(decoded))

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1
        decoded = self.instance.toByteArray("00000011")
        self.assertEqual(str(bits), str(decoded))

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        decoded = self.instance.toByteArray("00000111")
        self.assertEqual(str(bits), str(decoded))

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        decoded = self.instance.toByteArray("00001111")
        self.assertEqual(str(bits), str(decoded))

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        )
        decoded = self.instance.toByteArray("00011111")
        self.assertEqual(str(bits), str(decoded))

    def testToByteArrayFromString_test4_decomposed(self) -> None:
        bits = bytearray(1)
        decoded = self.instance.toByteArray("00000000")
        self.assertEqual(str(bits), str(decoded))

        bits = bytearray(1)
        bits[0] = self.__BIT_0
        decoded = self.instance.toByteArray("00000001")
        self.assertEqual(str(bits), str(decoded))

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1
        decoded = self.instance.toByteArray("00000011")
        self.assertEqual(str(bits), str(decoded))

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        decoded = self.instance.toByteArray("00000111")
        self.assertEqual(str(bits), str(decoded))

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        decoded = self.instance.toByteArray("00001111")
        self.assertEqual(str(bits), str(decoded))

    def testToByteArrayFromString_test3_decomposed(self) -> None:
        bits = bytearray(1)
        decoded = self.instance.toByteArray("00000000")
        self.assertEqual(str(bits), str(bytearray(decoded)))

        bits = bytearray(1)
        bits[0] = self.__BIT_0
        decoded = self.instance.toByteArray("00000001")
        self.assertEqual(str(bits), str(bytearray(decoded)))

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1
        decoded = self.instance.toByteArray("00000011")
        self.assertEqual(str(bits), str(bytearray(decoded)))

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        decoded = self.instance.toByteArray("00000111")
        self.assertEqual(str(bits), str(bytearray(decoded)))

    def testToByteArrayFromString_test2_decomposed(self) -> None:
        bits = bytearray(1)
        decoded = self.instance.toByteArray("00000000")
        self.assertEqual(str(bits), str(bytearray(decoded)))

        bits = bytearray(1)
        bits[0] = self.__BIT_0
        decoded = self.instance.toByteArray("00000001")
        self.assertEqual(str(bits), str(bytearray(decoded)))

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1
        decoded = self.instance.toByteArray("00000011")

    def testToByteArrayFromString_test1_decomposed(self) -> None:
        bits = bytearray(1)  # Create a byte array of size 1, initialized to 0
        decoded = self.instance.toByteArray("00000000")  # Call the toByteArray method
        self.assertEqual(
            str(bits), str(bytearray(decoded))
        )  # Compare the string representations of the byte arrays

        bits = bytearray(1)  # Reset the byte array
        bits[0] = self.__BIT_0  # Set the first byte to BIT_0
        decoded = self.instance.toByteArray(
            "00000001"
        )  # Call the toByteArray method again

    def testToByteArrayFromString_test0_decomposed(self) -> None:
        bits = bytearray(1)
        decoded = self.instance.toByteArray("00000000")

    def testDecodeByteArray_test36_decomposed(self) -> None:
        bits = bytearray(1)
        decoded = self.instance.decode0("00000000".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(1)
        bits[0] = self.__BIT_0
        decoded = self.instance.decode0("00000001".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1
        decoded = self.instance.decode0("00000011".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        decoded = self.instance.decode0("00000111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        decoded = self.instance.decode0("00001111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        )
        decoded = self.instance.decode0("00011111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
        )
        decoded = self.instance.decode0("00111111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
        )
        decoded = self.instance.decode0("01111111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = self.instance.decode0("11111111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(2)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = self.instance.decode0("0000000011111111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(2)
        bits[1] = self.__BIT_0
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = self.instance.decode0("0000000111111111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(2)
        bits[1] = self.__BIT_0 | self.__BIT_1
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = self.instance.decode0("0000001111111111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(2)
        bits[1] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = self.instance.decode0("0000011111111111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(2)
        bits[1] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = self.instance.decode0("0000111111111111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(2)
        bits[1] = (
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        )
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = self.instance.decode0("0001111111111111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(2)
        bits[1] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
        )
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = self.instance.decode0("0011111111111111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(2)
        bits[1] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
        )
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = self.instance.decode0("0111111111111111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(2)
        bits[1] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = self.instance.decode0("1111111111111111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

    def testDecodeByteArray_test35_decomposed(self) -> None:
        bits = bytearray(1)
        decoded = self.instance.decode0("00000000".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(1)
        bits[0] = self.__BIT_0
        decoded = self.instance.decode0("00000001".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1
        decoded = self.instance.decode0("00000011".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        decoded = self.instance.decode0("00000111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        decoded = self.instance.decode0("00001111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        )
        decoded = self.instance.decode0("00011111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
        )
        decoded = self.instance.decode0("00111111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
        )
        decoded = self.instance.decode0("01111111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = self.instance.decode0("11111111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(2)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = self.instance.decode0("0000000011111111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(2)
        bits[1] = self.__BIT_0
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = self.instance.decode0("0000000111111111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(2)
        bits[1] = self.__BIT_0 | self.__BIT_1
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = self.instance.decode0("0000001111111111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(2)
        bits[1] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = self.instance.decode0("0000011111111111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(2)
        bits[1] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = self.instance.decode0("0000111111111111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(2)
        bits[1] = (
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        )
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = self.instance.decode0("0001111111111111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(2)
        bits[1] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
        )
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = self.instance.decode0("0011111111111111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(2)
        bits[1] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
        )
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = self.instance.decode0("0111111111111111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(2)
        bits[1] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = self.instance.decode0("1111111111111111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

    def testDecodeByteArray_test34_decomposed(self) -> None:
        bits = bytearray(1)
        decoded = self.instance.decode0("00000000".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(1)
        bits[0] = self.__BIT_0
        decoded = self.instance.decode0("00000001".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1
        decoded = self.instance.decode0("00000011".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        decoded = self.instance.decode0("00000111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        decoded = self.instance.decode0("00001111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        )
        decoded = self.instance.decode0("00011111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
        )
        decoded = self.instance.decode0("00111111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
        )
        decoded = self.instance.decode0("01111111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = self.instance.decode0("11111111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(2)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = self.instance.decode0("0000000011111111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(2)
        bits[1] = self.__BIT_0
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = self.instance.decode0("0000000111111111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(2)
        bits[1] = self.__BIT_0 | self.__BIT_1
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = self.instance.decode0("0000001111111111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(2)
        bits[1] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = self.instance.decode0("0000011111111111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(2)
        bits[1] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = self.instance.decode0("0000111111111111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(2)
        bits[1] = (
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        )
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = self.instance.decode0("0001111111111111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(2)
        bits[1] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
        )
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = self.instance.decode0("0011111111111111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(2)
        bits[1] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
        )
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = self.instance.decode0("0111111111111111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(2)
        bits[1] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = self.instance.decode0("1111111111111111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

    def testDecodeByteArray_test33_decomposed(self) -> None:
        bits = bytearray(1)
        decoded = self.instance.decode0("00000000".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(1)
        bits[0] = self.__BIT_0
        decoded = self.instance.decode0("00000001".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1
        decoded = self.instance.decode0("00000011".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        decoded = self.instance.decode0("00000111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        decoded = self.instance.decode0("00001111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        )
        decoded = self.instance.decode0("00011111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
        )
        decoded = self.instance.decode0("00111111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
        )
        decoded = self.instance.decode0("01111111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = self.instance.decode0("11111111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(2)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = self.instance.decode0("0000000011111111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(2)
        bits[1] = self.__BIT_0
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = self.instance.decode0("0000000111111111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(2)
        bits[1] = self.__BIT_0 | self.__BIT_1
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = self.instance.decode0("0000001111111111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(2)
        bits[1] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = self.instance.decode0("0000011111111111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(2)
        bits[1] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = self.instance.decode0("0000111111111111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(2)
        bits[1] = (
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        )
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = self.instance.decode0("0001111111111111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(2)
        bits[1] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
        )
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = self.instance.decode0("0011111111111111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(2)
        bits[1] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
        )
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = self.instance.decode0("0111111111111111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

    def testDecodeByteArray_test32_decomposed(self) -> None:
        bits = bytearray(1)
        decoded = self.instance.decode0("00000000".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(1)
        bits[0] = self.__BIT_0
        decoded = self.instance.decode0("00000001".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1
        decoded = self.instance.decode0("00000011".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        decoded = self.instance.decode0("00000111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        decoded = self.instance.decode0("00001111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        )
        decoded = self.instance.decode0("00011111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
        )
        decoded = self.instance.decode0("00111111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
        )
        decoded = self.instance.decode0("01111111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = self.instance.decode0("11111111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(2)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = self.instance.decode0("0000000011111111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(2)
        bits[1] = self.__BIT_0
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = self.instance.decode0("0000000111111111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(2)
        bits[1] = self.__BIT_0 | self.__BIT_1
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = self.instance.decode0("0000001111111111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(2)
        bits[1] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = self.instance.decode0("0000011111111111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(2)
        bits[1] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = self.instance.decode0("0000111111111111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(2)
        bits[1] = (
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        )
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = self.instance.decode0("0001111111111111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(2)
        bits[1] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
        )
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = self.instance.decode0("0011111111111111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(2)
        bits[1] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
        )
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = self.instance.decode0("0111111111111111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

    def testDecodeByteArray_test31_decomposed(self) -> None:
        bits = bytearray(1)
        decoded = self.instance.decode0("00000000".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(1)
        bits[0] = self.__BIT_0
        decoded = self.instance.decode0("00000001".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1
        decoded = self.instance.decode0("00000011".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        decoded = self.instance.decode0("00000111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        decoded = self.instance.decode0("00001111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        )
        decoded = self.instance.decode0("00011111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
        )
        decoded = self.instance.decode0("00111111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
        )
        decoded = self.instance.decode0("01111111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = self.instance.decode0("11111111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(2)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = self.instance.decode0("0000000011111111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(2)
        bits[1] = self.__BIT_0
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = self.instance.decode0("0000000111111111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(2)
        bits[1] = self.__BIT_0 | self.__BIT_1
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = self.instance.decode0("0000001111111111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(2)
        bits[1] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = self.instance.decode0("0000011111111111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(2)
        bits[1] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = self.instance.decode0("0000111111111111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(2)
        bits[1] = (
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        )
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = self.instance.decode0("0001111111111111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(2)
        bits[1] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
        )
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = self.instance.decode0("0011111111111111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

    def testDecodeByteArray_test30_decomposed(self) -> None:
        bits = bytearray(1)
        decoded = self.instance.decode0("00000000".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(1)
        bits[0] = self.__BIT_0
        decoded = self.instance.decode0("00000001".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1
        decoded = self.instance.decode0("00000011".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        decoded = self.instance.decode0("00000111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        decoded = self.instance.decode0("00001111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        )
        decoded = self.instance.decode0("00011111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
        )
        decoded = self.instance.decode0("00111111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
        )
        decoded = self.instance.decode0("01111111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = self.instance.decode0("11111111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(2)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = self.instance.decode0("0000000011111111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(2)
        bits[1] = self.__BIT_0
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = self.instance.decode0("0000000111111111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(2)
        bits[1] = self.__BIT_0 | self.__BIT_1
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = self.instance.decode0("0000001111111111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(2)
        bits[1] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = self.instance.decode0("0000011111111111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(2)
        bits[1] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = self.instance.decode0("0000111111111111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(2)
        bits[1] = (
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        )
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = self.instance.decode0("0001111111111111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(2)
        bits[1] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
        )
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = self.instance.decode0("0011111111111111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

    def testDecodeByteArray_test29_decomposed(self) -> None:
        bits = bytearray(1)
        decoded = self.instance.decode0("00000000".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(1)
        bits[0] = self.__BIT_0
        decoded = self.instance.decode0("00000001".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1
        decoded = self.instance.decode0("00000011".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        decoded = self.instance.decode0("00000111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        decoded = self.instance.decode0("00001111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        )
        decoded = self.instance.decode0("00011111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
        )
        decoded = self.instance.decode0("00111111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
        )
        decoded = self.instance.decode0("01111111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = self.instance.decode0("11111111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(2)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = self.instance.decode0("0000000011111111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(2)
        bits[1] = self.__BIT_0
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = self.instance.decode0("0000000111111111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(2)
        bits[1] = self.__BIT_0 | self.__BIT_1
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = self.instance.decode0("0000001111111111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(2)
        bits[1] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = self.instance.decode0("0000011111111111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(2)
        bits[1] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = self.instance.decode0("0000111111111111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(2)
        bits[1] = (
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        )
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = self.instance.decode0("0001111111111111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

    def testDecodeByteArray_test28_decomposed(self) -> None:
        bits = bytearray(1)
        decoded = self.instance.decode0("00000000".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(1)
        bits[0] = self.__BIT_0
        decoded = self.instance.decode0("00000001".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1
        decoded = self.instance.decode0("00000011".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        decoded = self.instance.decode0("00000111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        decoded = self.instance.decode0("00001111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        )
        decoded = self.instance.decode0("00011111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
        )
        decoded = self.instance.decode0("00111111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
        )
        decoded = self.instance.decode0("01111111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = self.instance.decode0("11111111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(2)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = self.instance.decode0("0000000011111111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(2)
        bits[1] = self.__BIT_0
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = self.instance.decode0("0000000111111111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(2)
        bits[1] = self.__BIT_0 | self.__BIT_1
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = self.instance.decode0("0000001111111111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(2)
        bits[1] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = self.instance.decode0("0000011111111111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(2)
        bits[1] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = self.instance.decode0("0000111111111111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(2)
        bits[1] = (
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        )
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = self.instance.decode0("0001111111111111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

    def testDecodeByteArray_test27_decomposed(self) -> None:
        bits = bytearray(1)
        decoded = self.instance.decode0("00000000".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(1)
        bits[0] = self.__BIT_0
        decoded = self.instance.decode0("00000001".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1
        decoded = self.instance.decode0("00000011".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        decoded = self.instance.decode0("00000111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        decoded = self.instance.decode0("00001111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        )
        decoded = self.instance.decode0("00011111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
        )
        decoded = self.instance.decode0("00111111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
        )
        decoded = self.instance.decode0("01111111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = self.instance.decode0("11111111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(2)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = self.instance.decode0("0000000011111111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(2)
        bits[1] = self.__BIT_0
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = self.instance.decode0("0000000111111111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(2)
        bits[1] = self.__BIT_0 | self.__BIT_1
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = self.instance.decode0("0000001111111111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(2)
        bits[1] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = self.instance.decode0("0000011111111111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(2)
        bits[1] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = self.instance.decode0("0000111111111111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

    def testDecodeByteArray_test26_decomposed(self) -> None:
        bits = bytearray(1)
        decoded = self.instance.decode0("00000000".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(1)
        bits[0] = self.__BIT_0
        decoded = self.instance.decode0("00000001".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1
        decoded = self.instance.decode0("00000011".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        decoded = self.instance.decode0("00000111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        decoded = self.instance.decode0("00001111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        )
        decoded = self.instance.decode0("00011111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
        )
        decoded = self.instance.decode0("00111111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
        )
        decoded = self.instance.decode0("01111111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = self.instance.decode0("11111111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(2)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = self.instance.decode0("0000000011111111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(2)
        bits[1] = self.__BIT_0
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = self.instance.decode0("0000000111111111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(2)
        bits[1] = self.__BIT_0 | self.__BIT_1
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = self.instance.decode0("0000001111111111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(2)
        bits[1] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = self.instance.decode0("0000011111111111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(2)
        bits[1] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = self.instance.decode0("0000111111111111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

    def testDecodeByteArray_test25_decomposed(self) -> None:
        bits = bytearray(1)
        decoded = self.instance.decode0("00000000".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(1)
        bits[0] = self.__BIT_0
        decoded = self.instance.decode0("00000001".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1
        decoded = self.instance.decode0("00000011".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        decoded = self.instance.decode0("00000111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        decoded = self.instance.decode0("00001111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        )
        decoded = self.instance.decode0("00011111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
        )
        decoded = self.instance.decode0("00111111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
        )
        decoded = self.instance.decode0("01111111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = self.instance.decode0("11111111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(2)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = self.instance.decode0("0000000011111111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(2)
        bits[1] = self.__BIT_0
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = self.instance.decode0("0000000111111111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(2)
        bits[1] = self.__BIT_0 | self.__BIT_1
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = self.instance.decode0("0000001111111111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(2)
        bits[1] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = self.instance.decode0("0000011111111111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

    def testDecodeByteArray_test24_decomposed(self) -> None:
        bits = bytearray(1)
        decoded = self.instance.decode0("00000000".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(1)
        bits[0] = self.__BIT_0
        decoded = self.instance.decode0("00000001".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1
        decoded = self.instance.decode0("00000011".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        decoded = self.instance.decode0("00000111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        decoded = self.instance.decode0("00001111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        )
        decoded = self.instance.decode0("00011111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
        )
        decoded = self.instance.decode0("00111111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
        )
        decoded = self.instance.decode0("01111111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = self.instance.decode0("11111111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(2)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = self.instance.decode0("0000000011111111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(2)
        bits[1] = self.__BIT_0
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = self.instance.decode0("0000000111111111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(2)
        bits[1] = self.__BIT_0 | self.__BIT_1
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = self.instance.decode0("0000001111111111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(2)
        bits[1] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = self.instance.decode0("0000011111111111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

    def testDecodeByteArray_test23_decomposed(self) -> None:
        bits = bytearray(1)
        decoded = self.instance.decode0("00000000".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(1)
        bits[0] = self.__BIT_0
        decoded = self.instance.decode0("00000001".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1
        decoded = self.instance.decode0("00000011".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        decoded = self.instance.decode0("00000111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        decoded = self.instance.decode0("00001111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        )
        decoded = self.instance.decode0("00011111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
        )
        decoded = self.instance.decode0("00111111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
        )
        decoded = self.instance.decode0("01111111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = self.instance.decode0("11111111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(2)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = self.instance.decode0("0000000011111111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(2)
        bits[1] = self.__BIT_0
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = self.instance.decode0("0000000111111111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(2)
        bits[1] = self.__BIT_0 | self.__BIT_1
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = self.instance.decode0("0000001111111111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

    def testDecodeByteArray_test22_decomposed(self) -> None:
        bits = bytearray(1)
        decoded = self.instance.decode0("00000000".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(1)
        bits[0] = self.__BIT_0
        decoded = self.instance.decode0("00000001".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1
        decoded = self.instance.decode0("00000011".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        decoded = self.instance.decode0("00000111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        decoded = self.instance.decode0("00001111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        )
        decoded = self.instance.decode0("00011111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
        )
        decoded = self.instance.decode0("00111111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
        )
        decoded = self.instance.decode0("01111111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = self.instance.decode0("11111111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(2)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = self.instance.decode0("0000000011111111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(2)
        bits[1] = self.__BIT_0
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = self.instance.decode0("0000000111111111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(2)
        bits[1] = self.__BIT_0 | self.__BIT_1
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = self.instance.decode0("0000001111111111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

    def testDecodeByteArray_test21_decomposed(self) -> None:
        bits = bytearray(1)
        decoded = self.instance.decode0("00000000".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(1)
        bits[0] = self.__BIT_0
        decoded = self.instance.decode0("00000001".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1
        decoded = self.instance.decode0("00000011".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        decoded = self.instance.decode0("00000111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        decoded = self.instance.decode0("00001111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        )
        decoded = self.instance.decode0("00011111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
        )
        decoded = self.instance.decode0("00111111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
        )
        decoded = self.instance.decode0("01111111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = self.instance.decode0("11111111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(2)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = self.instance.decode0("0000000011111111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(2)
        bits[1] = self.__BIT_0
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = self.instance.decode0("0000000111111111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

    def testDecodeByteArray_test20_decomposed(self) -> None:
        bits = bytearray(1)
        decoded = self.instance.decode0("00000000".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(1)
        bits[0] = self.__BIT_0
        decoded = self.instance.decode0("00000001".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1
        decoded = self.instance.decode0("00000011".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        decoded = self.instance.decode0("00000111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        decoded = self.instance.decode0("00001111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        )
        decoded = self.instance.decode0("00011111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
        )
        decoded = self.instance.decode0("00111111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
        )
        decoded = self.instance.decode0("01111111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = self.instance.decode0("11111111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(2)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = self.instance.decode0("0000000011111111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(2)
        bits[1] = self.__BIT_0
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = self.instance.decode0("0000000111111111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

    def testDecodeByteArray_test19_decomposed(self) -> None:
        bits = bytearray(1)
        decoded = self.instance.decode0("00000000".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(1)
        bits[0] = self.__BIT_0
        decoded = self.instance.decode0("00000001".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1
        decoded = self.instance.decode0("00000011".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        decoded = self.instance.decode0("00000111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        decoded = self.instance.decode0("00001111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        )
        decoded = self.instance.decode0("00011111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
        )
        decoded = self.instance.decode0("00111111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
        )
        decoded = self.instance.decode0("01111111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = self.instance.decode0("11111111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(2)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = self.instance.decode0("0000000011111111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

    def testDecodeByteArray_test18_decomposed(self) -> None:
        bits = bytearray(1)
        decoded = self.instance.decode0("00000000".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(1)
        bits[0] = self.__BIT_0
        decoded = self.instance.decode0("00000001".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1
        decoded = self.instance.decode0("00000011".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        decoded = self.instance.decode0("00000111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        decoded = self.instance.decode0("00001111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        )
        decoded = self.instance.decode0("00011111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
        )
        decoded = self.instance.decode0("00111111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
        )
        decoded = self.instance.decode0("01111111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = self.instance.decode0("11111111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(2)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = self.instance.decode0("0000000011111111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

    def testDecodeByteArray_test17_decomposed(self) -> None:
        bits = bytearray(1)
        decoded = self.instance.decode0("00000000".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(1)
        bits[0] = self.__BIT_0
        decoded = self.instance.decode0("00000001".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1
        decoded = self.instance.decode0("00000011".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        decoded = self.instance.decode0("00000111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        decoded = self.instance.decode0("00001111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        )
        decoded = self.instance.decode0("00011111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
        )
        decoded = self.instance.decode0("00111111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
        )
        decoded = self.instance.decode0("01111111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = self.instance.decode0("11111111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

    def testDecodeByteArray_test16_decomposed(self) -> None:
        bits = bytearray(1)
        decoded = self.instance.decode0("00000000".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(1)
        bits[0] = self.__BIT_0
        decoded = self.instance.decode0("00000001".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1
        decoded = self.instance.decode0("00000011".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        decoded = self.instance.decode0("00000111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        decoded = self.instance.decode0("00001111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        )
        decoded = self.instance.decode0("00011111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
        )
        decoded = self.instance.decode0("00111111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
        )
        decoded = self.instance.decode0("01111111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = self.instance.decode0("11111111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

    def testDecodeByteArray_test15_decomposed(self) -> None:
        bits = bytearray(1)
        decoded = self.instance.decode0("00000000".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(1)
        bits[0] = self.__BIT_0
        decoded = self.instance.decode0("00000001".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1
        decoded = self.instance.decode0("00000011".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        decoded = self.instance.decode0("00000111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        decoded = self.instance.decode0("00001111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        )
        decoded = self.instance.decode0("00011111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
        )
        decoded = self.instance.decode0("00111111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
        )
        decoded = self.instance.decode0("01111111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

    def testDecodeByteArray_test14_decomposed(self) -> None:
        bits = bytearray(1)
        decoded = self.instance.decode0("00000000".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(1)
        bits[0] = self.__BIT_0
        decoded = self.instance.decode0("00000001".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1
        decoded = self.instance.decode0("00000011".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        decoded = self.instance.decode0("00000111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        decoded = self.instance.decode0("00001111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        )
        decoded = self.instance.decode0("00011111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
        )
        decoded = self.instance.decode0("00111111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
        )
        decoded = self.instance.decode0("01111111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

    def testDecodeByteArray_test13_decomposed(self) -> None:
        bits = bytearray(1)
        decoded = self.instance.decode0("00000000".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(1)
        bits[0] = self.__BIT_0
        decoded = self.instance.decode0("00000001".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1
        decoded = self.instance.decode0("00000011".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        decoded = self.instance.decode0("00000111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        decoded = self.instance.decode0("00001111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        )
        decoded = self.instance.decode0("00011111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
        )
        decoded = self.instance.decode0("00111111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

    def testDecodeByteArray_test12_decomposed(self) -> None:
        bits = bytearray(1)
        decoded = self.instance.decode0("00000000".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(1)
        bits[0] = self.__BIT_0
        decoded = self.instance.decode0("00000001".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1
        decoded = self.instance.decode0("00000011".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        decoded = self.instance.decode0("00000111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        decoded = self.instance.decode0("00001111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        )
        decoded = self.instance.decode0("00011111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
        )
        decoded = self.instance.decode0("00111111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

    def testDecodeByteArray_test11_decomposed(self) -> None:
        bits = bytearray(1)
        decoded = self.instance.decode0("00000000".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(1)
        bits[0] = self.__BIT_0
        decoded = self.instance.decode0("00000001".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1
        decoded = self.instance.decode0("00000011".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        decoded = self.instance.decode0("00000111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        decoded = self.instance.decode0("00001111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        )
        decoded = self.instance.decode0("00011111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

    def testDecodeByteArray_test10_decomposed(self) -> None:
        bits = bytearray(1)
        decoded = self.instance.decode0("00000000".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(1)
        bits[0] = self.__BIT_0
        decoded = self.instance.decode0("00000001".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1
        decoded = self.instance.decode0("00000011".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        decoded = self.instance.decode0("00000111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        decoded = self.instance.decode0("00001111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        )
        # The last line in the Java code does not perform any assertion or decoding, so no further action is needed.

    def testDecodeByteArray_test9_decomposed(self) -> None:
        bits = bytearray(1)
        decoded = self.instance.decode0("00000000".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(1)
        bits[0] = self.__BIT_0
        decoded = self.instance.decode0("00000001".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1
        decoded = self.instance.decode0("00000011".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        decoded = self.instance.decode0("00000111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        decoded = self.instance.decode0("00001111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

    def testDecodeByteArray_test8_decomposed(self) -> None:
        bits = bytearray(1)
        decoded = self.instance.decode0("00000000".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(1)
        bits[0] = self.__BIT_0
        decoded = self.instance.decode0("00000001".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1
        decoded = self.instance.decode0("00000011".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        decoded = self.instance.decode0("00000111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        decoded = self.instance.decode0("00001111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

    def testDecodeByteArray_test7_decomposed(self) -> None:
        bits = bytearray(1)
        decoded = self.instance.decode0("00000000".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(1)
        bits[0] = self.__BIT_0
        decoded = self.instance.decode0("00000001".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1
        decoded = self.instance.decode0("00000011".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        decoded = self.instance.decode0("00000111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

    def testDecodeByteArray_test6_decomposed(self) -> None:
        bits = bytearray(1)
        decoded = self.instance.decode0("00000000".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(1)
        bits[0] = self.__BIT_0
        decoded = self.instance.decode0("00000001".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1
        decoded = self.instance.decode0("00000011".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        decoded = self.instance.decode0("00000111".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

    def testDecodeByteArray_test5_decomposed(self) -> None:
        bits = bytearray(1)
        "00000000".encode(self.__CHARSET_UTF8)
        decoded = self.instance.decode0("00000000".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(1)
        bits[0] = self.__BIT_0
        "00000001".encode(self.__CHARSET_UTF8)
        decoded = self.instance.decode0("00000001".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1
        "00000011".encode(self.__CHARSET_UTF8)
        decoded = self.instance.decode0("00000011".encode(self.__CHARSET_UTF8))

    def testDecodeByteArray_test4_decomposed(self) -> None:
        bits = bytearray(1)
        decoded = self.instance.decode0("00000000".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(1)
        bits[0] = self.__BIT_0
        decoded = self.instance.decode0("00000001".encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bits.decode(self.__CHARSET_UTF8), decoded.decode(self.__CHARSET_UTF8)
        )

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1
        # The last line in the Java code does not perform any operation, so no further translation is needed.

    def testDecodeByteArray_test3_decomposed(self) -> None:
        bits = bytearray(1)  # Create a byte array of size 1
        "00000000".encode(self.__CHARSET_UTF8)  # Encode the string to bytes using UTF-8
        decoded = self.instance.decode0(
            "00000000".encode(self.__CHARSET_UTF8)
        )  # Decode the byte array
        self.assertEqual(
            str(bits), str(decoded)
        )  # Assert that the string representations are equal

        bits = bytearray(1)  # Reset the byte array
        bits[0] = self.__BIT_0  # Set the first bit to BIT_0
        "00000001".encode(self.__CHARSET_UTF8)  # Encode the string to bytes using UTF-8
        decoded = self.instance.decode0(
            "00000001".encode(self.__CHARSET_UTF8)
        )  # Decode the byte array

    def testDecodeByteArray_test2_decomposed(self) -> None:
        bits = bytearray(1)  # Create a byte array of size 1
        "00000000".encode(self.__CHARSET_UTF8)  # Encode the string using UTF-8
        decoded = self.instance.decode0(
            "00000000".encode(self.__CHARSET_UTF8)
        )  # Decode the encoded string
        self.assertEqual(
            str(bits), str(decoded)
        )  # Assert that the string representations of bits and decoded are equal
        bits = bytearray(1)  # Reset bits to a new byte array of size 1
        bits[0] = self.__BIT_0  # Set the first byte to BIT_0
        "00000001".encode(
            self.__CHARSET_UTF8
        )  # Encode the string "00000001" using UTF-8

    def testDecodeByteArray_test1_decomposed(self) -> None:
        bits = bytearray(1)  # Equivalent to `new byte[1]` in Java
        "00000000".encode(
            self.__CHARSET_UTF8
        )  # Encoding the string to bytes using UTF-8
        decoded = self.instance.decode0(
            "00000000".encode(self.__CHARSET_UTF8)
        )  # Calling the decode0 method

    def testDecodeByteArray_test0_decomposed(self) -> None:
        bits: bytearray = bytearray(1)
        "00000000".encode(self.__CHARSET_UTF8)

    def testDecodeObject_test18_decomposed(self) -> None:
        bits = bytearray(1)
        self.assertDecodeObject(bits, "00000000")

        bits = bytearray(1)
        bits[0] = self.__BIT_0
        self.assertDecodeObject(bits, "00000001")

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1
        self.assertDecodeObject(bits, "00000011")

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        self.assertDecodeObject(bits, "00000111")

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        self.assertDecodeObject(bits, "00001111")

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        )
        self.assertDecodeObject(bits, "00011111")

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
        )
        self.assertDecodeObject(bits, "00111111")

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
        )
        self.assertDecodeObject(bits, "01111111")

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        self.assertDecodeObject(bits, "11111111")

        bits = bytearray(2)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        self.assertDecodeObject(bits, "0000000011111111")

        bits = bytearray(2)
        bits[1] = self.__BIT_0
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        self.assertDecodeObject(bits, "0000000111111111")

        bits = bytearray(2)
        bits[1] = self.__BIT_0 | self.__BIT_1
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        self.assertDecodeObject(bits, "0000001111111111")

        bits = bytearray(2)
        bits[1] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        self.assertDecodeObject(bits, "0000011111111111")

        bits = bytearray(2)
        bits[1] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        self.assertDecodeObject(bits, "0000111111111111")

        bits = bytearray(2)
        bits[1] = (
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        )
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        self.assertDecodeObject(bits, "0001111111111111")

        bits = bytearray(2)
        bits[1] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
        )
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        self.assertDecodeObject(bits, "0011111111111111")

        bits = bytearray(2)
        bits[1] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
        )
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        self.assertDecodeObject(bits, "0111111111111111")

        bits = bytearray(2)
        bits[1] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        self.assertDecodeObject(bits, "1111111111111111")

        self.assertDecodeObject(bytearray(0), None)

    def testDecodeObject_test17_decomposed(self) -> None:
        bits = bytearray(1)
        self.assertDecodeObject(bits, "00000000")

        bits = bytearray(1)
        bits[0] = self.__BIT_0
        self.assertDecodeObject(bits, "00000001")

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1
        self.assertDecodeObject(bits, "00000011")

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        self.assertDecodeObject(bits, "00000111")

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        self.assertDecodeObject(bits, "00001111")

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        )
        self.assertDecodeObject(bits, "00011111")

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
        )
        self.assertDecodeObject(bits, "00111111")

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
        )
        self.assertDecodeObject(bits, "01111111")

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        self.assertDecodeObject(bits, "11111111")

        bits = bytearray(2)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        self.assertDecodeObject(bits, "0000000011111111")

        bits = bytearray(2)
        bits[1] = self.__BIT_0
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        self.assertDecodeObject(bits, "0000000111111111")

        bits = bytearray(2)
        bits[1] = self.__BIT_0 | self.__BIT_1
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        self.assertDecodeObject(bits, "0000001111111111")

        bits = bytearray(2)
        bits[1] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        self.assertDecodeObject(bits, "0000011111111111")

        bits = bytearray(2)
        bits[1] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        self.assertDecodeObject(bits, "0000111111111111")

        bits = bytearray(2)
        bits[1] = (
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        )
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        self.assertDecodeObject(bits, "0001111111111111")

        bits = bytearray(2)
        bits[1] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
        )
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        self.assertDecodeObject(bits, "0011111111111111")

        bits = bytearray(2)
        bits[1] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
        )
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        self.assertDecodeObject(bits, "0111111111111111")

        bits = bytearray(2)
        bits[1] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        self.assertDecodeObject(bits, "1111111111111111")

    def testDecodeObject_test16_decomposed(self) -> None:
        bits = bytearray(1)
        self.assertDecodeObject(bits, "00000000")

        bits = bytearray(1)
        bits[0] = self.__BIT_0
        self.assertDecodeObject(bits, "00000001")

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1
        self.assertDecodeObject(bits, "00000011")

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        self.assertDecodeObject(bits, "00000111")

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        self.assertDecodeObject(bits, "00001111")

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        )
        self.assertDecodeObject(bits, "00011111")

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
        )
        self.assertDecodeObject(bits, "00111111")

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
        )
        self.assertDecodeObject(bits, "01111111")

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        self.assertDecodeObject(bits, "11111111")

        bits = bytearray(2)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        self.assertDecodeObject(bits, "0000000011111111")

        bits = bytearray(2)
        bits[1] = self.__BIT_0
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        self.assertDecodeObject(bits, "0000000111111111")

        bits = bytearray(2)
        bits[1] = self.__BIT_0 | self.__BIT_1
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        self.assertDecodeObject(bits, "0000001111111111")

        bits = bytearray(2)
        bits[1] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        self.assertDecodeObject(bits, "0000011111111111")

        bits = bytearray(2)
        bits[1] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        self.assertDecodeObject(bits, "0000111111111111")

        bits = bytearray(2)
        bits[1] = (
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        )
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        self.assertDecodeObject(bits, "0001111111111111")

        bits = bytearray(2)
        bits[1] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
        )
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        self.assertDecodeObject(bits, "0011111111111111")

        bits = bytearray(2)
        bits[1] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
        )
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        self.assertDecodeObject(bits, "0111111111111111")

    def testDecodeObject_test15_decomposed(self) -> None:
        bits = bytearray(1)
        self.assertDecodeObject(bits, "00000000")

        bits = bytearray(1)
        bits[0] = self.__BIT_0
        self.assertDecodeObject(bits, "00000001")

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1
        self.assertDecodeObject(bits, "00000011")

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        self.assertDecodeObject(bits, "00000111")

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        self.assertDecodeObject(bits, "00001111")

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        )
        self.assertDecodeObject(bits, "00011111")

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
        )
        self.assertDecodeObject(bits, "00111111")

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
        )
        self.assertDecodeObject(bits, "01111111")

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        self.assertDecodeObject(bits, "11111111")

        bits = bytearray(2)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        self.assertDecodeObject(bits, "0000000011111111")

        bits = bytearray(2)
        bits[1] = self.__BIT_0
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        self.assertDecodeObject(bits, "0000000111111111")

        bits = bytearray(2)
        bits[1] = self.__BIT_0 | self.__BIT_1
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        self.assertDecodeObject(bits, "0000001111111111")

        bits = bytearray(2)
        bits[1] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        self.assertDecodeObject(bits, "0000011111111111")

        bits = bytearray(2)
        bits[1] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        self.assertDecodeObject(bits, "0000111111111111")

        bits = bytearray(2)
        bits[1] = (
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        )
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        self.assertDecodeObject(bits, "0001111111111111")

        bits = bytearray(2)
        bits[1] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
        )
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        self.assertDecodeObject(bits, "0011111111111111")

    def testDecodeObject_test14_decomposed(self) -> None:
        bits = bytearray(1)
        self.assertDecodeObject(bits, "00000000")

        bits = bytearray(1)
        bits[0] = self.__BIT_0
        self.assertDecodeObject(bits, "00000001")

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1
        self.assertDecodeObject(bits, "00000011")

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        self.assertDecodeObject(bits, "00000111")

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        self.assertDecodeObject(bits, "00001111")

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        )
        self.assertDecodeObject(bits, "00011111")

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
        )
        self.assertDecodeObject(bits, "00111111")

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
        )
        self.assertDecodeObject(bits, "01111111")

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        self.assertDecodeObject(bits, "11111111")

        bits = bytearray(2)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        self.assertDecodeObject(bits, "0000000011111111")

        bits = bytearray(2)
        bits[1] = self.__BIT_0
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        self.assertDecodeObject(bits, "0000000111111111")

        bits = bytearray(2)
        bits[1] = self.__BIT_0 | self.__BIT_1
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        self.assertDecodeObject(bits, "0000001111111111")

        bits = bytearray(2)
        bits[1] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        self.assertDecodeObject(bits, "0000011111111111")

        bits = bytearray(2)
        bits[1] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        self.assertDecodeObject(bits, "0000111111111111")

        bits = bytearray(2)
        bits[1] = (
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        )
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        self.assertDecodeObject(bits, "0001111111111111")

    def testDecodeObject_test13_decomposed(self) -> None:
        bits = bytearray(1)
        self.assertDecodeObject(bits, "00000000")

        bits = bytearray(1)
        bits[0] = self.__BIT_0
        self.assertDecodeObject(bits, "00000001")

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1
        self.assertDecodeObject(bits, "00000011")

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        self.assertDecodeObject(bits, "00000111")

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        self.assertDecodeObject(bits, "00001111")

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        )
        self.assertDecodeObject(bits, "00011111")

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
        )
        self.assertDecodeObject(bits, "00111111")

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
        )
        self.assertDecodeObject(bits, "01111111")

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        self.assertDecodeObject(bits, "11111111")

        bits = bytearray(2)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        self.assertDecodeObject(bits, "0000000011111111")

        bits = bytearray(2)
        bits[1] = self.__BIT_0
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        self.assertDecodeObject(bits, "0000000111111111")

        bits = bytearray(2)
        bits[1] = self.__BIT_0 | self.__BIT_1
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        self.assertDecodeObject(bits, "0000001111111111")

        bits = bytearray(2)
        bits[1] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        self.assertDecodeObject(bits, "0000011111111111")

        bits = bytearray(2)
        bits[1] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        self.assertDecodeObject(bits, "0000111111111111")

    def testDecodeObject_test12_decomposed(self) -> None:
        bits = bytearray(1)
        self.assertDecodeObject(bits, "00000000")

        bits = bytearray(1)
        bits[0] = self.__BIT_0
        self.assertDecodeObject(bits, "00000001")

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1
        self.assertDecodeObject(bits, "00000011")

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        self.assertDecodeObject(bits, "00000111")

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        self.assertDecodeObject(bits, "00001111")

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        )
        self.assertDecodeObject(bits, "00011111")

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
        )
        self.assertDecodeObject(bits, "00111111")

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
        )
        self.assertDecodeObject(bits, "01111111")

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        self.assertDecodeObject(bits, "11111111")

        bits = bytearray(2)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        self.assertDecodeObject(bits, "0000000011111111")

        bits = bytearray(2)
        bits[1] = self.__BIT_0
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        self.assertDecodeObject(bits, "0000000111111111")

        bits = bytearray(2)
        bits[1] = self.__BIT_0 | self.__BIT_1
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        self.assertDecodeObject(bits, "0000001111111111")

        bits = bytearray(2)
        bits[1] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        self.assertDecodeObject(bits, "0000011111111111")

    def testDecodeObject_test11_decomposed(self) -> None:
        bits = bytearray(1)
        self.assertDecodeObject(bits, "00000000")

        bits = bytearray(1)
        bits[0] = self.__BIT_0
        self.assertDecodeObject(bits, "00000001")

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1
        self.assertDecodeObject(bits, "00000011")

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        self.assertDecodeObject(bits, "00000111")

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        self.assertDecodeObject(bits, "00001111")

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        )
        self.assertDecodeObject(bits, "00011111")

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
        )
        self.assertDecodeObject(bits, "00111111")

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
        )
        self.assertDecodeObject(bits, "01111111")

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        self.assertDecodeObject(bits, "11111111")

        bits = bytearray(2)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        self.assertDecodeObject(bits, "0000000011111111")

        bits = bytearray(2)
        bits[1] = self.__BIT_0
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        self.assertDecodeObject(bits, "0000000111111111")

        bits = bytearray(2)
        bits[1] = self.__BIT_0 | self.__BIT_1
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        self.assertDecodeObject(bits, "0000001111111111")

    def testDecodeObject_test10_decomposed(self) -> None:
        bits = bytearray(1)
        self.assertDecodeObject(bits, "00000000")

        bits = bytearray(1)
        bits[0] = self.__BIT_0
        self.assertDecodeObject(bits, "00000001")

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1
        self.assertDecodeObject(bits, "00000011")

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        self.assertDecodeObject(bits, "00000111")

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        self.assertDecodeObject(bits, "00001111")

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        )
        self.assertDecodeObject(bits, "00011111")

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
        )
        self.assertDecodeObject(bits, "00111111")

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
        )
        self.assertDecodeObject(bits, "01111111")

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        self.assertDecodeObject(bits, "11111111")

        bits = bytearray(2)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        self.assertDecodeObject(bits, "0000000011111111")

        bits = bytearray(2)
        bits[1] = self.__BIT_0
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        self.assertDecodeObject(bits, "0000000111111111")

    def testDecodeObject_test9_decomposed(self) -> None:
        bits = bytearray(1)
        self.assertDecodeObject(bits, "00000000")

        bits = bytearray(1)
        bits[0] = self.__BIT_0
        self.assertDecodeObject(bits, "00000001")

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1
        self.assertDecodeObject(bits, "00000011")

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        self.assertDecodeObject(bits, "00000111")

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        self.assertDecodeObject(bits, "00001111")

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        )
        self.assertDecodeObject(bits, "00011111")

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
        )
        self.assertDecodeObject(bits, "00111111")

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
        )
        self.assertDecodeObject(bits, "01111111")

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        self.assertDecodeObject(bits, "11111111")

        bits = bytearray(2)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        self.assertDecodeObject(bits, "0000000011111111")

    def testDecodeObject_test8_decomposed(self) -> None:
        bits = bytearray(1)
        self.assertDecodeObject(bits, "00000000")

        bits = bytearray(1)
        bits[0] = self.__BIT_0
        self.assertDecodeObject(bits, "00000001")

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1
        self.assertDecodeObject(bits, "00000011")

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        self.assertDecodeObject(bits, "00000111")

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        self.assertDecodeObject(bits, "00001111")

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        )
        self.assertDecodeObject(bits, "00011111")

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
        )
        self.assertDecodeObject(bits, "00111111")

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
        )
        self.assertDecodeObject(bits, "01111111")

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        self.assertDecodeObject(bits, "11111111")

    def testDecodeObject_test7_decomposed(self) -> None:
        bits = bytearray(1)
        self.assertDecodeObject(bits, "00000000")

        bits = bytearray(1)
        bits[0] = self.__BIT_0
        self.assertDecodeObject(bits, "00000001")

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1
        self.assertDecodeObject(bits, "00000011")

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        self.assertDecodeObject(bits, "00000111")

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        self.assertDecodeObject(bits, "00001111")

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        )
        self.assertDecodeObject(bits, "00011111")

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
        )
        self.assertDecodeObject(bits, "00111111")

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
        )
        self.assertDecodeObject(bits, "01111111")

    def testDecodeObject_test6_decomposed(self) -> None:
        bits = bytearray(1)
        self.assertDecodeObject(bits, "00000000")

        bits = bytearray(1)
        bits[0] = self.__BIT_0
        self.assertDecodeObject(bits, "00000001")

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1
        self.assertDecodeObject(bits, "00000011")

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        self.assertDecodeObject(bits, "00000111")

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        self.assertDecodeObject(bits, "00001111")

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        )
        self.assertDecodeObject(bits, "00011111")

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
        )
        self.assertDecodeObject(bits, "00111111")

    def testDecodeObject_test5_decomposed(self) -> None:
        bits = bytearray(1)
        self.assertDecodeObject(bits, "00000000")

        bits = bytearray(1)
        bits[0] = self.__BIT_0
        self.assertDecodeObject(bits, "00000001")

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1
        self.assertDecodeObject(bits, "00000011")

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        self.assertDecodeObject(bits, "00000111")

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        self.assertDecodeObject(bits, "00001111")

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        )
        self.assertDecodeObject(bits, "00011111")

    def testDecodeObject_test4_decomposed(self) -> None:
        bits = bytearray(1)
        self.assertDecodeObject(bits, "00000000")

        bits = bytearray(1)
        bits[0] = self.__BIT_0
        self.assertDecodeObject(bits, "00000001")

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1
        self.assertDecodeObject(bits, "00000011")

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        self.assertDecodeObject(bits, "00000111")

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        self.assertDecodeObject(bits, "00001111")

    def testDecodeObject_test3_decomposed(self) -> None:
        bits = bytearray(1)
        self.assertDecodeObject(bits, "00000000")

        bits = bytearray(1)
        bits[0] = self.__BIT_0
        self.assertDecodeObject(bits, "00000001")

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1
        self.assertDecodeObject(bits, "00000011")

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        self.assertDecodeObject(bits, "00000111")

    def testDecodeObject_test2_decomposed(self) -> None:
        bits = bytearray(1)
        self.assertDecodeObject(bits, "00000000")

        bits = bytearray(1)
        bits[0] = self.__BIT_0
        self.assertDecodeObject(bits, "00000001")

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1
        self.assertDecodeObject(bits, "00000011")

    def testDecodeObject_test1_decomposed(self) -> None:
        bits = bytearray(1)  # Create a byte array of size 1, initialized to 0
        self.assertDecodeObject(bits, "00000000")  # Test with all bits set to 0

        bits = bytearray(1)  # Create a new byte array of size 1
        bits[0] = self.__BIT_0  # Set the first bit to BIT_0 (0x01)
        self.assertDecodeObject(bits, "00000001")  # Test with the first bit set to 1

    def testDecodeObject_test0_decomposed(self) -> None:
        bits = bytearray(1)  # Equivalent to `new byte[1]` in Java
        self.assertDecodeObject(bits, "00000000")

    def testDecodeObjectException_test1_decomposed(self) -> None:
        with pytest.raises(DecoderException):
            self.instance.decode1(object())

    def testDecodeObjectException_test0_decomposed(self) -> None:
        try:
            self.instance.decode1(object())
        except DecoderException:
            return

    def tearDown(self) -> None:
        self.instance = None

    def setUp(self) -> None:
        self.instance = BinaryCodec()

    def assertDecodeObject(self, bits: typing.List[int], encodeMe: str) -> None:
        # Decode the string using instance.decode1 and compare with the expected bits
        decoded = self.instance.decode1(encodeMe)
        self.assertEqual(
            bytes(bits).decode(self.__CHARSET_UTF8),
            bytes(decoded).decode(self.__CHARSET_UTF8),
        )

        # Handle the case where encodeMe is None
        if encodeMe is None:
            decoded = self.instance.decode0(None)
        else:
            decoded = self.instance.decode1(encodeMe.encode(self.__CHARSET_UTF8))
        self.assertEqual(
            bytes(bits).decode(self.__CHARSET_UTF8),
            bytes(decoded).decode(self.__CHARSET_UTF8),
        )

        # Handle the case where encodeMe is None for char[] equivalent
        if encodeMe is None:
            decoded = self.instance.decode1(None)
        else:
            decoded = self.instance.decode1(list(encodeMe))
        self.assertEqual(
            bytes(bits).decode(self.__CHARSET_UTF8),
            bytes(decoded).decode(self.__CHARSET_UTF8),
        )
