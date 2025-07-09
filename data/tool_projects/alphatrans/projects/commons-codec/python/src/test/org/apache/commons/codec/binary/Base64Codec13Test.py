from __future__ import annotations
import re
import enum
import unittest
import pytest
import io
import typing
from typing import *
import os
import unittest
from src.main.org.apache.commons.codec.BinaryDecoder import *
from src.main.org.apache.commons.codec.BinaryEncoder import *
from src.main.org.apache.commons.codec.Decoder import *
from src.main.org.apache.commons.codec.DecoderException import *
from src.main.org.apache.commons.codec.Encoder import *
from src.main.org.apache.commons.codec.EncoderException import *
from src.main.org.apache.commons.codec.binary.Base64 import *


class Base64Codec13Test(unittest.TestCase):

    __STRINGS: typing.List[str] = [None] * 181

    __BYTES: typing.List[typing.List[int]] = None  # LLM could not translate this field

    __CHUNKED_STRINGS: typing.List[str] = [None] * len(__STRINGS) if __STRINGS else []

    @staticmethod
    def run_static_init():
        Base64Codec13Test.__initSTRINGS()
        Base64Codec13Test.__initCHUNKED_STRINGS()
        Base64Codec13Test.__initBYTES()

    def testStaticDecodeChunked_test0_decomposed(self) -> None:
        for i in range(len(self.__STRINGS)):
            if self.__STRINGS[i] is not None:
                base64_chunked = self.__utf8(self.__CHUNKED_STRINGS[i])
                binary = self.__BYTES[i]
                decoded = Base64.decodeBase640(base64_chunked)
                self.assertTrue(
                    binary == decoded, f"static Base64.decodeBase64Chunked() test-{i}"
                )

    def testStaticEncodeChunked_test0_decomposed(self) -> None:
        for i in range(len(self.__STRINGS)):
            if self.__STRINGS[i] is not None:
                base64_chunked = self.__utf8(self.__CHUNKED_STRINGS[i])
                binary = self.__BYTES[i]
                b = base64_chunked == Base64.encodeBase64Chunked(binary)
                self.assertTrue(b, f"static Base64.encodeBase64Chunked() test-{i}")

    def testStaticDecode_test0_decomposed(self) -> None:
        for i in range(len(self.__STRINGS)):
            if self.__STRINGS[i] is not None:
                base64 = self.__utf8(self.__STRINGS[i])
                binary = self.__BYTES[i]
                b = binary == Base64.decodeBase640(base64)
                self.assertTrue(b, f"static Base64.decodeBase64() test-{i}")

    def testStaticEncode_test0_decomposed(self) -> None:
        for i in range(len(self.__STRINGS)):
            if self.__STRINGS[i] is not None:
                base64 = self.__utf8(self.__STRINGS[i])
                binary = self.__BYTES[i]
                b = base64 == Base64.encodeBase640(binary)
                self.assertTrue(b, f"static Base64.encodeBase64() test-{i}")

    def testBinaryDecoder_test1_decomposed(self) -> None:
        dec = Base64.Base645()
        for i, string in enumerate(self.__STRINGS):
            if string is not None:
                base64 = self.__utf8(string)
                binary = self.__BYTES[i]
                b = binary == dec.decode(base64)
                self.assertTrue(b, f"BinaryDecoder test-{i}")

    def testBinaryDecoder_test0_decomposed(self) -> None:
        dec = Base64.Base645()

    def testBinaryEncoder_test1_decomposed(self) -> None:
        enc = Base64.Base645()
        for i in range(len(self.__STRINGS)):
            if self.__STRINGS[i] is not None:
                base64 = self.__utf8(self.__STRINGS[i])
                binary = self.__BYTES[i]
                b = base64 == enc.encode(binary)
                self.assertTrue(b, f"BinaryEncoder test-{i}")

    def testBinaryEncoder_test0_decomposed(self) -> None:
        enc = Base64.Base645()

    def testDecoder_test1_decomposed(self) -> None:
        dec = Base64.Base645()
        for i in range(len(self.__STRINGS)):
            if self.__STRINGS[i] is not None:
                base64 = self.__utf8(self.__STRINGS[i])
                binary = self.__BYTES[i]
                b = binary == dec.decode(base64)
                self.assertTrue(b, f"Decoder test-{i}")

    def testDecoder_test0_decomposed(self) -> None:
        dec = Base64.Base645()

    def testEncoder_test1_decomposed(self) -> None:
        enc = Base64.Base645()
        for i in range(len(self.__STRINGS)):
            if self.__STRINGS[i] is not None:
                base64 = self.__utf8(self.__STRINGS[i])
                binary = self.__BYTES[i]
                b = base64 == list(enc.encode(binary))
                self.assertTrue(b, f"Encoder test-{i}")

    def testEncoder_test0_decomposed(self) -> None:
        enc = Base64.Base645()

    @staticmethod
    def __utf8(s: str) -> typing.List[int]:
        return list(s.encode("utf-8")) if s is not None else None

    @staticmethod
    def __initBYTES() -> None:
        b = Base64Codec13Test.__BYTES
        b[0] = []
        b[1] = [-72]
        b[2] = [-49, -36]
        b[3] = [77, 15, -103]
        b[4] = [110, 24, -44, 96]
        b[5] = [-43, -61, -67, -75, -33]
        b[6] = [-80, -52, 71, -96, -105, -7]
        b[7] = [-115, 7, 15, -108, 59, 25, -49]
        b[8] = [76, 6, -113, -99, -11, -65, 9, -123]
        b[9] = [113, 116, -39, -69, 12, -41, 60, -29, 82]
        b[10] = [46, -39, -1, 101, 53, 120, 34, 52, -6, 56]
        b[11] = [-23, -8, 126, -115, -43, 55, -43, 35, -90, 90, -73]
        b[12] = [19, -2, 76, -96, 62, 42, 10, -16, -18, 77, -63, 64]
        b[13] = [-38, 127, 88, -55, -16, -116, -56, -59, -34, -103, -69, 108, -79]
        b[14] = [-88, 25, 26, -36, 26, -70, 87, 125, 71, -103, -55, -121, -114, 70]
        b[15] = [
            90,
            -4,
            -103,
            123,
            -87,
            16,
            -14,
            -100,
            -69,
            -101,
            110,
            110,
            113,
            -84,
            9,
        ]
        b[16] = [
            -95,
            -118,
            113,
            51,
            46,
            -127,
            74,
            -106,
            87,
            -123,
            90,
            78,
            71,
            -89,
            87,
            -104,
        ]
        b[63] = [
            -55,
            -20,
            69,
            104,
            -46,
            -102,
            63,
            -27,
            100,
            87,
            1,
            20,
            -65,
            20,
            23,
            108,
            45,
            7,
            72,
            40,
            -65,
            -78,
            -77,
            -104,
            -19,
            -51,
            55,
            -22,
            84,
            -10,
            -27,
            -6,
            -20,
            -29,
            24,
            -56,
            -66,
            -99,
            -75,
            -32,
            -111,
            -62,
            -125,
            -77,
            -117,
            -3,
            118,
            86,
            -36,
            -125,
            30,
            -24,
            32,
            -32,
            72,
            -64,
            -102,
            104,
            -113,
            117,
            121,
            24,
            12,
        ]
        b[64] = [
            -66,
            74,
            -96,
            -98,
            -30,
            119,
            -90,
            92,
            77,
            -74,
            -117,
            -34,
            -120,
            -62,
            110,
            96,
            -77,
            122,
            -63,
            -108,
            11,
            -91,
            -67,
            -59,
            -125,
            -113,
            63,
            -52,
            121,
            29,
            22,
            -32,
            -18,
            114,
            -29,
            10,
            89,
            84,
            78,
            -2,
            120,
            -123,
            70,
            2,
            -84,
            22,
            -89,
            49,
            -85,
            -91,
            96,
            11,
            28,
            16,
            109,
            -29,
            -30,
            63,
            -37,
            17,
            -97,
            28,
            -5,
            -62,
        ]
        b[65] = [
            96,
            121,
            44,
            -36,
            96,
            -101,
            -38,
            -27,
            69,
            -29,
            -74,
            54,
            -76,
            40,
            -98,
            -120,
            49,
            -119,
            -13,
            -65,
            81,
            -101,
            -105,
            65,
            -123,
            8,
            80,
            -117,
            54,
            33,
            125,
            99,
            -88,
            -8,
            26,
            -63,
            -37,
            -14,
            -66,
            19,
            -68,
            25,
            89,
            56,
            -99,
            -41,
            -119,
            76,
            -92,
            -50,
            -76,
            -5,
            -112,
            -76,
            55,
            -46,
            77,
            40,
            7,
            1,
            17,
            39,
            -86,
            101,
            -110,
        ]
        b[66] = [
            -49,
            -50,
            121,
            -42,
            57,
            -112,
            -89,
            -12,
            44,
            -9,
            -101,
            112,
            -37,
            110,
            -66,
            28,
            33,
            -42,
            -82,
            -30,
            -79,
            -4,
            -101,
            -33,
            4,
            39,
            -48,
            -26,
            -99,
            31,
            23,
            -66,
            -26,
            -111,
            42,
            105,
            -21,
            -95,
            57,
            -25,
            104,
            -92,
            -38,
            12,
            -100,
            -84,
            16,
            108,
            48,
            47,
            -51,
            111,
            57,
            -64,
            -127,
            54,
            104,
            51,
            54,
            113,
            122,
            23,
            -55,
            -62,
            -18,
            61,
        ]
        b[67] = [
            86,
            -60,
            118,
            -62,
            26,
            -86,
            -2,
            -92,
            38,
            -33,
            -115,
            -66,
            76,
            -36,
            -11,
            -106,
            3,
            -103,
            50,
            -123,
            -101,
            -92,
            44,
            -2,
            -110,
            61,
            -77,
            126,
            90,
            -76,
            -97,
            30,
            -46,
            -3,
            23,
            -124,
            84,
            -11,
            9,
            114,
            -88,
            12,
            -75,
            92,
            -21,
            -81,
            97,
            85,
            64,
            -9,
            -63,
            0,
            126,
            85,
            70,
            52,
            126,
            -122,
            76,
            112,
            -65,
            -122,
            -20,
            -79,
            9,
            -84,
            -15,
        ]
        b[68] = [
            -25,
            25,
            -120,
            -89,
            -57,
            84,
            37,
            -100,
            -28,
            -118,
            -62,
            36,
            -72,
            67,
            -20,
            -100,
            -11,
            -17,
            -52,
            55,
            -116,
            -93,
            -113,
            42,
            88,
            87,
            -57,
            34,
            125,
            -102,
            -65,
            120,
            -21,
            -26,
            -86,
            25,
            28,
            43,
            52,
            45,
            -13,
            68,
            -55,
            -22,
            66,
            -34,
            -3,
            -84,
            107,
            73,
            -62,
            83,
            65,
            101,
            -86,
            -55,
            -125,
            -55,
            50,
            57,
            -1,
            104,
            -19,
            -25,
            59,
            11,
            -75,
            93,
        ]
        b[69] = [
            -76,
            97,
            32,
            94,
            56,
            37,
            80,
            31,
            77,
            108,
            43,
            98,
            75,
            -49,
            0,
            122,
            -46,
            -19,
            70,
            -88,
            66,
            2,
            120,
            115,
            57,
            66,
            -107,
            -126,
            -10,
            -55,
            100,
            122,
            -114,
            3,
            -84,
            124,
            -72,
            -22,
            43,
            3,
            91,
            119,
            53,
            -58,
            -120,
            3,
            77,
            25,
            -87,
            -77,
            -40,
            0,
            -69,
            -72,
            47,
            50,
            38,
            -30,
            46,
            37,
            0,
            -65,
            80,
            -126,
            33,
            -1,
            38,
            14,
            -37,
        ]
        b[70] = [
            -128,
            91,
            113,
            18,
            22,
            9,
            106,
            16,
            -26,
            83,
            -105,
            105,
            -71,
            -42,
            44,
            -23,
            -108,
            -20,
            -88,
            12,
            126,
            -77,
            104,
            -2,
            -45,
            -96,
            52,
            -51,
            -20,
            -101,
            -35,
            78,
            -25,
            -123,
            -111,
            108,
            110,
            64,
            -125,
            -107,
            -37,
            52,
            17,
            -123,
            40,
            -87,
            -22,
            -39,
            -87,
            -109,
            -26,
            -20,
            94,
            -126,
            12,
            -29,
            -125,
            -35,
            -43,
            59,
            -99,
            -119,
            -98,
            -108,
            77,
            3,
            -57,
            35,
            14,
            -12,
        ]

    @staticmethod
    def __initCHUNKED_STRINGS() -> None:
        c = Base64Codec13Test.__CHUNKED_STRINGS
        c[0] = ""
        c[1] = "uA==\r\n"
        c[2] = "z9w=\r\n"
        c[3] = "TQ+Z\r\n"
        c[4] = "bhjUYA==\r\n"
        c[5] = "1cO9td8=\r\n"
        c[6] = "sMxHoJf5\r\n"
        c[7] = "jQcPlDsZzw==\r\n"
        c[8] = "TAaPnfW/CYU=\r\n"
        c[9] = "cXTZuwzXPONS\r\n"
        c[10] = "Ltn/ZTV4IjT6OA==\r\n"
        c[11] = "6fh+jdU31SOmWrc=\r\n"
        c[12] = "E/5MoD4qCvDuTcFA\r\n"
        c[13] = "2n9YyfCMyMXembtssQ==\r\n"
        c[14] = "qBka3Bq6V31HmcmHjkY=\r\n"
        c[15] = "WvyZe6kQ8py7m25ucawJ\r\n"
        c[16] = "oYpxMy6BSpZXhVpOR6dXmA==\r\n"
        c[63] = (
            "yexFaNKaP+VkVwEUvxQXbC0HSCi/srOY7c036lT25frs4xjIvp214JHCg7OL/XZW3IMe6CDgSMCa\r\n"
            "aI91eRgM\r\n"
        )
        c[64] = (
            "vkqgnuJ3plxNtoveiMJuYLN6wZQLpb3Fg48/zHkdFuDucuMKWVRO/niFRgKsFqcxq6VgCxwQbePi\r\n"
            "P9sRnxz7wg==\r\n"
        )
        c[65] = (
            "YHks3GCb2uVF47Y2tCieiDGJ879Rm5dBhQhQizYhfWOo+BrB2/K+E7wZWTid14lMpM60+5C0N9JN\r\n"
            "KAcBESeqZZI=\r\n"
        )
        c[66] = (
            "z8551jmQp/Qs95tw226+HCHWruKx/JvfBCfQ5p0fF77mkSpp66E552ik2gycrBBsMC/NbznAgTZo\r\n"
            "MzZxehfJwu49\r\n"
        )
        c[67] = (
            "VsR2whqq/qQm342+TNz1lgOZMoWbpCz+kj2zflq0nx7S/ReEVPUJcqgMtVzrr2FVQPfBAH5VRjR+\r\n"
            "hkxwv4bssQms8Q==\r\n"
        )
        c[68] = (
            "5xmIp8dUJZzkisIkuEPsnPXvzDeMo48qWFfHIn2av3jr5qoZHCs0LfNEyepC3v2sa0nCU0FlqsmD\r\n"
            "yTI5/2jt5zsLtV0=\r\n"
        )
        c[69] = (
            "tGEgXjglUB9NbCtiS88AetLtRqhCAnhzOUKVgvbJZHqOA6x8uOorA1t3NcaIA00ZqbPYALu4LzIm\r\n"
            "4i4lAL9QgiH/Jg7b\r\n"
        )
        c[70] = (
            "gFtxEhYJahDmU5dpudYs6ZTsqAx+s2j+06A0zeyb3U7nhZFsbkCDlds0EYUoqerZqZPm7F6CDOOD\r\n"
            "3dU7nYmelE0DxyMO9A==\r\n"
        )
        c[71] = (
            "j/h/1JygYA5bjttxzQxr5gBtgh+AYVozhF4WgvcU/g49v0hUy6FdhfZewGK+Phtzj7RabI5p2zXy\r\n"
            "zvkmLQdFhdI5Um4O5sw=\r\n"
        )
        c[72] = (
            "m+kYVGojIR5pgbz7pGJm2g+3qqk7fhl3cowa2eVrhki7WofyywnRezqTxOkBgVFz6nKs8qxpbbbz\r\n"
            "ALctcPeMsp9dpXUfuUJr\r\n"
        )
        c[73] = (
            "pPaGnMr0UYmldnJVk/F+3WCJJ1r2otvD5KJdt2u1RnS6LwhHhwLCqfW8O/QEg43WdxKomGL/JM33\r\n"
            "tn/B9pMPoIU0QTGjq2GRow==\r\n"
        )
        c[74] = (
            "mOxzGyym6T/BxCV5nSiIYMlfAUmCN7gt7+ZTMg1kd8Ptirk+JF5dk8USbWBu/9ZvNg5ZuiJCeGwf\r\n"
            "aVpqpZ3K9ySF7C87Jvu1RUE=\r\n"
        )
        c[75] = (
            "VYLOIE4DnhxJn3FKS/2RHHHYLlZiGVdV/k4uBbtAYHUSTpRzaaYPGNAVjdNwbTHIihmeuk/5YQUy\r\n"
            "8NFsxIom+Li7bnWiBoHKBPP7\r\n"
        )
        c[76] = (
            "7foMpJ0TknCatjUiSxtnuKSiz4Qvl/idWY9UKiTljoQHZ+C8bcUscnI/bZr13e6AvyUh47MlpdGv\r\n"
            "zIm05qUdMWWLoZJOaGYvDmvrWQ==\r\n"
        )
        c[77] = (
            "jxQSGiFs+b1TfE4lDUAPUPJ0SWeUgl03rK6auieWJcarDIHM97gGOHMmyHudRMqkZmIkxYRgYgCC\r\n"
            "Ug/JeU91OZD3tL4U+wNhShywe88=\r\n"
        )
        c[78] = (
            "UGmH/gl7t3Dk801vRhRDEbgsfShtHZ1gZQn4KNZ5Qsw3WiGjW0ImInVHa+LSHBzLUjwC0Z3nXO4i\r\n"
            "4+CiKYqAspOViE6WqVUY8ZSV0Og4\r\n"
        )
        c[79] = (
            "wdEoYmJuRng2z2IkAiSgJ1CW2VE7H7oXpYWEFFO8nG0bZn7PHhT8KyhaO2ridl8eUEysja0VXFDy\r\n"
            "QqSgZnvdUKrCGepWGZbw0/0bDws3Ag==\r\n"
        )
        c[80] = (
            "5kZqgrUbt+rN5BWAddeUtm9TGT43vYpB6PeyQwTyy9Vbr0+U/4Qzy0Iw37Ra293HmkmpgQzuScVp\r\n"
            "cIiFGXPAFWwToR+bovwu7aXji/FnMwk=\r\n"
        )
        c[81] = (
            "E467MMmJbmwv8Omc2TdcyMr/30B8izWbf+CAuJtw67b1g9trhC6n4GYnXjeW9DYvmWoIJPx0zvU/\r\n"
            "Q+gqv0cteg2bx9P2mrgMDARb6egowqjx\r\n"
        )
        c[82] = (
            "Vpt8hYb4jx1F+7REX7K65v6eO5F1GDg/K8SVLWDSp0srupYEQkBVRxnB9dmhSo9XHpz4C8pRl8r8\r\n"
            "2fxXZummEf4U2Oh0Dip5rnNtDL+IJvL8lQ==\r\n"
        )
        c[121] = (
            "hf69xr9mtFf4N3j2uA9MgLL5Zy94Hjv+VQi94+LS8972JJgDHCQOwP5whdQkV+SJpXkiyHGaSsQ4\r\n"
            "fhepPwzuZcEpYER+beny1j+M0HSZe36MdRIhlTqno+4qsXckL0CjXsYkJJM0NAfOYjHAus5G1bgi\r\n"
            "9VhmiMfAMA==\r\n"
        )
        # Continue for other indices...

    @staticmethod
    def __initSTRINGS() -> None:
        s = Base64Codec13Test.__STRINGS
        s[0] = ""
        s[1] = "uA=="
        s[2] = "z9w="
        s[3] = "TQ+Z"
        s[4] = "bhjUYA=="
        s[5] = "1cO9td8="
        s[6] = "sMxHoJf5"
        s[7] = "jQcPlDsZzw=="
        s[8] = "TAaPnfW/CYU="
        s[9] = "cXTZuwzXPONS"
        s[10] = "Ltn/ZTV4IjT6OA=="
        s[11] = "6fh+jdU31SOmWrc="
        s[12] = "E/5MoD4qCvDuTcFA"
        s[13] = "2n9YyfCMyMXembtssQ=="
        s[14] = "qBka3Bq6V31HmcmHjkY="
        s[15] = "WvyZe6kQ8py7m25ucawJ"
        s[16] = "oYpxMy6BSpZXhVpOR6dXmA=="
        s[63] = (
            "yexFaNKaP+VkVwEUvxQXbC0HSCi/srOY7c036lT25frs4xjIvp214JHCg7OL/XZW3IMe6CDgSMCaaI91eRgM"
        )
        s[64] = (
            "vkqgnuJ3plxNtoveiMJuYLN6wZQLpb3Fg48/zHkdFuDucuMKWVRO/niFRgKsFqcxq6VgCxwQbePiP9sRnxz7wg=="
        )
        s[65] = (
            "YHks3GCb2uVF47Y2tCieiDGJ879Rm5dBhQhQizYhfWOo+BrB2/K+E7wZWTid14lMpM60+5C0N9JNKAcBESeqZZI="
        )
        s[66] = (
            "z8551jmQp/Qs95tw226+HCHWruKx/JvfBCfQ5p0fF77mkSpp66E552ik2gycrBBsMC/NbznAgTZoMzZxehfJwu49"
        )
        s[67] = (
            "VsR2whqq/qQm342+TNz1lgOZMoWbpCz+kj2zflq0nx7S/ReEVPUJcqgMtVzrr2FVQPfBAH5VRjR+hkxwv4bssQms8Q=="
        )
        s[68] = (
            "5xmIp8dUJZzkisIkuEPsnPXvzDeMo48qWFfHIn2av3jr5qoZHCs0LfNEyepC3v2sa0nCU0FlqsmDyTI5/2jt5zsLtV0="
        )
        s[69] = (
            "tGEgXjglUB9NbCtiS88AetLtRqhCAnhzOUKVgvbJZHqOA6x8uOorA1t3NcaIA00ZqbPYALu4LzIm4i4lAL9QgiH/Jg7b"
        )
        s[70] = (
            "gFtxEhYJahDmU5dpudYs6ZTsqAx+s2j+06A0zeyb3U7nhZFsbkCDlds0EYUoqerZqZPm7F6CDOOD3dU7nYmelE0DxyMO9A=="
        )
        s[71] = (
            "j/h/1JygYA5bjttxzQxr5gBtgh+AYVozhF4WgvcU/g49v0hUy6FdhfZewGK+Phtzj7RabI5p2zXyzvkmLQdFhdI5Um4O5sw="
        )
        s[72] = (
            "m+kYVGojIR5pgbz7pGJm2g+3qqk7fhl3cowa2eVrhki7WofyywnRezqTxOkBgVFz6nKs8qxpbbbzALctcPeMsp9dpXUfuUJr"
        )
        s[73] = (
            "pPaGnMr0UYmldnJVk/F+3WCJJ1r2otvD5KJdt2u1RnS6LwhHhwLCqfW8O/QEg43WdxKomGL/JM33tn/B9pMPoIU0QTGjq2GRow=="
        )
        s[74] = (
            "mOxzGyym6T/BxCV5nSiIYMlfAUmCN7gt7+ZTMg1kd8Ptirk+JF5dk8USbWBu/9ZvNg5ZuiJCeGwfaVpqpZ3K9ySF7C87Jvu1RUE="
        )
        s[75] = (
            "VYLOIE4DnhxJn3FKS/2RHHHYLlZiGVdV/k4uBbtAYHUSTpRzaaYPGNAVjdNwbTHIihmeuk/5YQUy8NFsxIom+Li7bnWiBoHKBPP7"
        )
        s[76] = (
            "7foMpJ0TknCatjUiSxtnuKSiz4Qvl/idWY9UKiTljoQHZ+C8bcUscnI/bZr13e6AvyUh47MlpdGvzIm05qUdMWWLoZJOaGYvDmvrWQ=="
        )
        s[77] = (
            "jxQSGiFs+b1TfE4lDUAPUPJ0SWeUgl03rK6auieWJcarDIHM97gGOHMmyHudRMqkZmIkxYRgYgCCUg/JeU91OZD3tL4U+wNhShywe88="
        )
        s[78] = (
            "UGmH/gl7t3Dk801vRhRDEbgsfShtHZ1gZQn4KNZ5Qsw3WiGjW0ImInVHa+LSHBzLUjwC0Z3nXO4i4+CiKYqAspOViE6WqVUY8ZSV0Og4"
        )
        s[79] = (
            "wdEoYmJuRng2z2IkAiSgJ1CW2VE7H7oXpYWEFFO8nG0bZn7PHhT8KyhaO2ridl8eUEysja0VXFDyQqSgZnvdUKrCGepWGZbw0/0bDws3Ag=="
        )
        s[80] = (
            "5kZqgrUbt+rN5BWAddeUtm9TGT43vYpB6PeyQwTyy9Vbr0+U/4Qzy0Iw37Ra293HmkmpgQzuScVpcIiFGXPAFWwToR+bovwu7aXji/FnMwk="
        )
        s[81] = (
            "E467MMmJbmwv8Omc2TdcyMr/30B8izWbf+CAuJtw67b1g9trhC6n4GYnXjeW9DYvmWoIJPx0zvU/Q+gqv0cteg2bx9P2mrgMDARb6egowqjx"
        )
        s[82] = (
            "Vpt8hYb4jx1F+7REX7K65v6eO5F1GDg/K8SVLWDSp0srupYEQkBVRxnB9dmhSo9XHpz4C8pRl8r82fxXZummEf4U2Oh0Dip5rnNtDL+IJvL8lQ=="
        )
        s[121] = (
            "hf69xr9mtFf4N3j2uA9MgLL5Zy94Hjv+VQi94+LS8972JJgDHCQOwP5whdQkV+SJpXkiyHGaSsQ4fhepPwzuZcEpYER+beny1j+M0HSZe36MdRIhlTqno+4qsXckL0CjXsYkJJM0NAfOYjHAus5G1bgi9VhmiMfAMA=="
        )
        s[122] = (
            "yKzTh5hPp9/PBeZtrZXsFHAR9ywOM3hRaBDkgG9E09wFW8MZD0xMGegcp0QrTJcP8QYOaYhTDVimPqsNTVOmjdjkvS+2WhjJW4mVOXQ8KID91yaBtPo+DStL5GMgctcP5MoVf1Vp8w/mYtofqbllfDm5NfYzh2A7ijY="
        )
        s[123] = (
            "csFmwvDzoO4IO6ySDA4B2V7emEetAwCgO66zzlfWb3KDrPfFZc3Jgr4+dlaUkEIDHYeLHETdTssWOl2KrPHBEsULpDTR+3OhurXb1Qr2NvHiHFuqT3Geb6EYw2albfTmXxch82ablt4WKl4qPcSey54v6tsCuUuZzrkt"
        )
        s[124] = (
            "5InxvKwpoCV7EK78OzU/tL9/NmK14Prw9tOCAyK+xpUNLZriuVEVdgpoZ05rliufaUDGHH8dPAem8G9DN/VOPktB6vXKtc2kMUgnMTiZwv/UVd+xyqnT8PLEdNQ8rCWxyiCcLdXFf0+xcE7qCcwzC+D7+cRW+i6dnpZkyw=="
        )
        s[125] = (
            "cEx7oTsSHWUFPj92cstdy5wGbRcxH+VRWN8kaNTTCPWqSckyU9Xk/jj5/gj9DFwjfsCSp60xutf4/rFanjtwqtRg6dJLP4JAgpOKswDlHi6Vt7zF/w7HidMf2sdtlsqzayZmT2Hn7iOo3CExzr5Z5JfmMFAX8R9peUN4t5U="
        )
        s[126] = (
            "AeXetVbj+7mmGiCs3BGUSZDLlq2odMsN8JAHQM64Cly8y5jw75PpISocWRFFQmmXYP7ckKmtuhIvD69HtZxGhNRsl1l1gXzKFhsWykcRtG87F8sS1Uv/i6QvGiRIDVEGGIzWrzRIISkBb9wCxJ2HESfleWwrz/GqryjoN26B"
        )
        s[127] = (
            "aj1/8/+U8VO3D2iAwvQXZ4H0KwtuzDm4JCC8+22ccqk+UzKvqjGs87XngwfsMfSkeGVAi6VB6tfNJTjYctaj7R8dwh2PIfLSrvaphw4wNB2REjplnPojoOb9bNUNtUvdK3b1bArOWugIRJWLnMl72yEHFb1iBfBmn7uIa7KT2Q=="
        )
        s[128] = (
            "kiMuF/1CMRlgoS/uLKn1mNZFZNHJNkRQnivOrzj8HQAagwzvTXvsGgI9hXX3qaeZL9/x/Oq+Y5F6Dh+wXo+0kp6JagFjvbTJcQSowFzIwg7/V9sans0NE0Ejow5BfZKvihFI46sHiALl1qzoXqLQq+5fZGIFRyyY8wFW1uiNu9k="
        )
        s[129] = (
            "YXmCWhiNz4/IhyxQIYjgNvjX+XwDiPTSBMaFELm5X8Y4knGRnkF4/zix8l9wHBb+7Cgfrr46rF7eiIzaAFLjLjjewy63duBJiVbEWjqFO0fu6T9iIjuEaF2sTppvuZNPHx80vN+HLAnAVmgFESw5APXWn15dizvuUfVHd5isCqbA"
        )
        s[130] = (
            "GJfUoBivW5uqDpUxTRfjGWNYfN3/dTFtdRqCIH5L2c1nWX0dgY3ba1+fW/YX1Oh5aw4lC6BIiiThjJoV1VrNnlXzbcUcMy+GsDUUB8Qe8lBvfe/t4RmNPB0hVgrS89ntbuU0SsCmWw+9DqM3nidPebANKERig1zZTBBKgpVf7HPFCA=="
        )
        s[131] = (
            "eTerNs7dOqJAxAxcMQRnUDc2cBj2x0jU1g1D3G+b22kDz7JBzOy/mxhGXAQ3130lavWMhImSBkReU+z0A13EYVMUv9PFzD747KCvns+SCo52YNHB0896b4l47q8hu8jsD17TZ2uWWJhS4cNnSE1jeM6NoXGKvf90yxfzwucNYc4RdaQ="
        )
        s[132] = (
            "lbrGsjbzE521q8tzVHV7vcTPchUnzI/UfeR2R+cmOa29YljPWLht9Wx2JrjiKv4Of5nXe7kvhi+LYUuFVqgaqIFhC/PLbqOFiT2VZcXorToaRT9CLiqV5b6nHN/Txz6SI7MiD3hnk7psDbglPOo+ytqc9sFHj7UkR1ZctQjwFYwJjlxf"
        )
        s[133] = (
            "mQwAPzYzfxz9FXEiZ6M8u1oN3EJbFYmNVfpm+j0DqgU+OPI4URHBIrF4xvdMvAPn0WuarbQy/ZVN0eKL7S4K3Mvan0flAwaZdI+e5HpkfxOoGTp8Dk5EFTXjmZ/s+GonePEQEGNVPL1WYoD6xXqAAvMLKtyrFcpoiGS9eDBlsZDQzPzz/g=="
        )
        s[134] = (
            "3G6d12UY4l5W7Nnw0BL0HnViVg9SdEuLMqeZwy0RlJR/Ytcgd/mIxIuXXAlGhvhoX6Xc2BGU7RpTi1jYKzA86yul0j96dbcE4OtrP9lUBJlcY9eWz59dvLqKxwt3cEOBwrPf69MHuIa256es3AOCobfC8RQScW0PQ0QUa1VHB/eXSsVTSWg="
        )
        s[135] = (
            "AxgrZKTFk5JvLC3DBACHwp266FxKI/yn9F+1tYkzL57RVs5HCJYS47VuG0T0E2wqzHqcLKPQMZWU7vbRoyMGNL3ZtaHoZqTqcq9KWtODC+OnEvSS7+1P4SmQDuyL2MJ/eJABJKNcu1K/Lk0buAaO0FvX6OGBcPzu1+dv/ZkwuORK07qRnxqQ"
        )
        s[136] = (
            "atkG8l2U/Nnm+zLu7zjenrfcAVQJMUqHimFZ3cQfaUp4qyrFn1UiwZ33j66Vt63eVaT/FXx+LlEnsHn6ATPBMp3iEYoBJYyNpjz/zROhBbcznQAMdWUTcyKInvnG3x6ExgBXpyqfxxp/Pm8by7LlSUT5MKHdcu+TEfUXRokCr2iPnt7NYsNDfA=="
        )
        s[137] = (
            "dciU1mSHGcBxOAVBgJx75J6DaQdBZfTIzQ04WhkkdRMupOZWSnv19xhz8hiO+ZnbBtDJuO5rHsUGzH/jYacfZyCQ924roRvkh3T1yxsLq3abZJUCD9HYnPTELVhv1+cEF4aoO3vGOu2FpfLUn5QTd0PozsIqcqZVB2V57B7DjfizUe3D8Yf5Vco="
        )
        s[138] = (
            "dgR1PPacBvtILBmg33s9KWtuc67ndh3rCHZ/lIN7sENgbFqJQy5DC3XIeHTV7oWd+tJQaXxoC71/SU7Rz6OClAMKXLbMz8U6RPiqn3M7MRCQcDfNjA5cCNknXT9Ehz/IZF/7lcWrwxBKYm4B98lPkpZtR2QHndiQ3venzWrP0P5y27mReaFuaJ++"
        )
        s[139] = (
            "1Q8rfp1HuGsxurTgGMakxj5SwNF7EixXxVPnfGADWDcygh5C1BMXqiL1AuVXOVFOsaydfLWGC8Kbh/JiL6H+12lYrNGUT9yJRIzRDi4XylMnrYwBtwCJjoHSi4exz5K2ih54utVAuzXZg6mnc9ied/mNRjj9d2HFD5mv0w/qTN/WFxEmtuZM/nMMag=="
        )
        s[140] = (
            "w01TnPP/F3Vni3fBdV32Bnbb4J1FcbaE+Xn44no5ug77U8FS1gSm3LqJ8yTyXduzl5v2dwBEfziEfTuyqgeLLsCYTBjXmYOIHQosEl6DyAknu4XK52eQW+Fes9eSs2Nq+G4aaR4y4leeFNmCoZ9BQmAAZr0LFkqnvqaKmBVgcgxPs7/8SQHnpqvaU6Y="
        )
        s[141] = (
            "OfzIF38Tp5g1W5eVbrkrMe0Mm7e0wBYg5hVvLpn/5MW5OFcmRDuBp15ayRBnJ1sBI93+CNl0LwP8Q0z9IXFjTER5gHZ1KfG8NV+oacKNG7aYrbUftkSL/oPfRNPez6U0FuWgvVrXUB6cwKTWvwb9KoD7s6AGYRdH50ZgJdBniFD7dKoOQnJ/ECuTUXI+"
        )
        s[142] = (
            "4hoX0sjqlkSJPUq627iJkNYRbtD+V2qErCuTikaeRDEZvVHWvzdvwj4W1xxJjz+yHAN6z2EjCWidcSsVgTejQ1bH8uTzJgh/zq3yGUSsJoJWrecqxsge8bEBjkm+qUO8G3kAnC6FMjJ2NYQeXf6OK6OgsqyJwlHPTyAms2/IoYTB4iEqgIFG/2fNEJEIag=="
        )
        s[143] = (
            "M/dy14xNbZMRfHiKKFdmD/OrEB+8MexrRO8mMh0i5LrNA5WUtLXdwUfAysYmal94MSoNJfgmwGCoqNwlWZBW1kpQaPdqsrn2cvc6JcZW9FlOx07DERJGbZ6l6ofbzZWgF+yf+hvT6jnJvXBVCTT3lfO3qo4leNuEJwsuU6erXGC3Ch53uPtGIrdDUpcX6/U="
        )
        s[144] = (
            "GgLr2hd3nK64IZv0JksKAT/yJNQ38ayuWyBnWLjXbEmT048UDppsrrnP6hikRo5v2TlHGhD2dcwG9NLK3Ph8IoIo9Wf2vZWBB+SMI9FpgZxBWLEjwHbOWsHaEQMVsQfk38EWQP0Fr6VyMKlEQfpsRkuCpp1KxscaxK7g5BgXUlb0a2x0F+C9hEB0OVPsj4JN"
        )
        s[145] = (
            "W9lKcLDqNGQAG/sKQNaRmeOUmLJ7GcMNqBaGZ659Rnjr6RTrfnmkp5Z9meALnwXoHjPjzSQDJnVYsY+xyMnuPgl6gMVAhAm+XprYVpsne4vt+7ojUqavVPBqLy5dtnhp1qfcnAiV5cZhHXX7NbxkUOzptjEGCQjnhSH4rPbZtgoIWE8Z6boF3l/thLnFX+AiiQ=="
        )
        s[146] = (
            "iYLn5h9lIhD/x9moaPRnTX6mJEJKThg4WXxS7IrR2zblH26uOkINz0dJNTJVets0ZNYDnsnT7J2iI3Y6hTVWPGoYU49J3B2LhCREs0DZQ3C7080FtiOcfHbfBLNn0DyCK1LeAC7YB/bNdiyhLqH8fKl+0+KhiPDIUBJY2e7IbZR/9t0sxJbIXx6cRvI5AXex12o="
        )
        s[147] = (
            "SlRJEc7npTUvQq8SgBYKmVY/3wHYp2gsDxafN/JLUuEqEjmWMtW7fxASi+ePX4gmJJqLhD5t+AZxiCwYK3L3ceuJx4TiqVgJz8d6sc7fgWXluh1K+BcGPbZ7+Cq4Vsga7JEBVekviEZ5Ah4apNr8RkB7oMOUVPGxRcyyaVE4zBW+scA6c1yi/HQXddQ9rWyLUsVo"
        )
        s[148] = (
            "AAlbGR6ekLOzx4hpqZTUqVUQ0FL2CFpgCMOp6CuuUzkSnWXpUjvOiSDkNPgoTPgpgmg3uYvMsX43mkPGUGC9awDThXyGQh6u3WfWtmhiPRqXnjFek+EPd0LYXps71non6C9m7nUlYNWzBJ1YzrzWjlB5LLPBN8bsZG6RbdZkYMxJ9J5ta/c30m8wDDNuTm0nEE0ZVQ=="
        )
        s[149] = (
            "nWWbBhzObqwEFh/TiKREcsqLYbRjIcZflJpol16Mi4YDL6EZri22qRnTgrBtIY+HieTYWuLaCSk/B9WcYujoS6Jb5dyg3FQ6XF9bYaNQGx2w8DHgx0k2nqH/0U1sAU0kft32aD2orqCMIprbO1WJIt2auRnvcOTFoOax926nAkxvR3nrFVDevFjDbugpWHkGwic6G7o="
        )
        s[150] = (
            "WNk1Rn2qtG+gk0AEewrgo+aRbNrG4CgQpOR8Uo7c2m2XQY8MVDu4uRA6rzYGGdgqTcICKky9MvHeJeNWVAXOxmA4EdXQ2xItFJdQtxBt56cad9FBXXsz21yVsPr5d453abi7T3XfHVTToekiOlxAJs+bpat9cFRbIdHghO9wc/ucoArT53vpYsnyeVnmZG2PX48lXpNS"
        )
        s[151] = (
            "wVmiO6mdf2aahrJlcmnBD0Qa58y8AvzXtJ54ImxgPLPn0NCQIrmUxzNZNTODE3WO6kZMECaT/REqT3PoOBp9stCHCFNXOM7979J44C1ZRU0yPCha00kQZBF5EmcLitVCz10tP8gG1fiIvMjwpd2ZTOaY4/g4NeJHLjJPll0c5nbH7n4v+1I+xG7/7k7G6N8sp21pbgpTYA=="
        )
        s[152] = (
            "OoiVZosI+KG0EZTu+WpH7kKISxmO1zRYaSPMBMW0AyRiC2iZVEkOMiKn12XPqIDSW/kVA58cvv/ysTAzKLTu78Uo+sVcJe3AtLdgeA9vORFELTP4v9DQ/mAmehe3N8xk+VTLY6xHWi6f4j9cTDW/BDyJSDRY00oYoHlvnjgHo4CHBo0sMGgX3CwcnK2hpMFVtB/3qPl6v2w="
        )
        s[153] = (
            "97ZVsTYwD8VrgN1FOIRZ8jm8OMgrxG3o1aJoYtPVWXp9cjjlgXqTMZVsoWr3pr7pudw+LYo1Ejz3JpiUPHqWcZ2PWrWs7PR1akYGuwdCBHYvCGTcZYFe/yu1AB8w5zYsl1eJR45g0u1DlXfx5BUAUzc4yJDjc48Ls62bn8t0EJ7+30sWwifqKuz2EHpsqp1j/iMlwzKJGjGE"
        )
        s[154] = (
            "0NSYKTvBKKInwL9PJ/pWUWVX4gjF3igsA2qqQMsRew0lI1LcCB18eGCYk0AnyUCe99w5lWHGFUMMeH6DZciAylWGeDn19JdzVOTevBWk3LIujI1GvsEB3oVqf2Zl9IZeDGCT4+bQKBWvgcXHjysZfnn/5z9Xz06qrPqac5LfS36fDcwnkrUYQWDsL2Ike32ALmOnkcDjNq1BoA=="
        )
        s[155] = (
            "5ok+rYI4LCgGa2psGUN/fdkT2gQEToB9HRiFXQpe2YcQvEN2z7YlJCETx4jSWw06p5Y8tZcp08moKNYwUJ40DvPpGlDG+wUpFhC4kkfo6vj6TrCj5yoWJi5D+qdgH2T0JeWM80cYN0bsOsetdaqNhDONlYXZ2lVYkyVS/wzw8K5xX87EWktwOwFq/yYhuWCYJ9GZL7QuDipJjEE="
        )
        s[156] = (
            "KHzTalU9wPSnIjh5g0eHi1HUaFufxJpXpjDe0N3wEKINqbgzhbj3Kf4qWjb2d1A+0Mlu9tYF/kA9ONjda5jYfRgCHm5mUrjU0TAyT7EQFZ2u6WFK/sFHP++ycJQk8k7KLPUWA5OWScy1EO+dYF4d0r6K5O+7H/rpknxN6M9FlP8sH83DXK1Sd+UXL32D+4flF580FaZ5B3Tkx3dH"
        )
        s[157] = (
            "RrJVxIKoDXtCviWMv/SXMO42Dn6UWOKDy2hh2ASXssT0e+G6m7F1230iJWlEN0wBR8p+BlTdBhQrn25098P3K16rBmZpzw/5dmesIJxhYPaM4GiaOgztFjuScTgkmV0Jl/vZ9eCXdEVNISeXkIixM4pssTFuUV7PY/Upzdj55rDKGLr1eT7AFVSNP30PhL8zZs8MANqKBeKBBDvtww=="
        )
        s[158] = (
            "sy4t5rFA75GRBE+Dqa9sQxjPluKt/JnEY54guHnKqccmx3HGiyJ0jUA+et4XO8Xg69wCA9xVxJZQL73z80mVfIf43HIKOxgxT2IjG7EKMOD/qx6NnMTve4BryggLtbLQUeRfhriQeY7h65tD9ierhccXoXDpGnmBn9m2BQP78y+Qhc4eIsa3LcxbQJUIwvURjFp/rgMD7lhOLboa/2Y="
        )
        s[159] = (
            "Zs/BfFoWImYau2dZLb7JneeTQp7sQ06yonEq0Ya4BNOJGy/5dGH42ozt0PpP2IZ/S58X7esVgc6jA1y3Bcxj3MPoDjQJSZHFEtR3G31T8eF5OpPVC4dw9s9clllM05tvcemssLdcd85UP/xBaDrmpAl8ZDSc73zflK3nJw8e0HQFYntNnlZPFyyyBLHnLycb6Jlvq7F2OqrZR+FXZnL3"
        )
        s[160] = (
            "hdeDJuRnmb8q9EYec8+futT/CvqhpqoUdtmG6E31RrYJDs96M5Wfng90IEqrncZe4rVYDocRZK23dvqtJaPhTUBXXh42IyMlUnro69KI+075FvYYwgVaUd10r7ExWM5Z7DCQ2x8Tm1meK2YCTPkF1VXXexl1UjYCnRQuQxppdophMwroJK8VqlJbFFslchTSBFuI7wgcdy+f/LHMbMsusQ=="
        )
        s[161] = (
            "ClCCOv0mD9//LR0OisHfamxcTvmlwMLgAIQt3hbOjRPkXwEgaDzP0u6LN8BNwdOVw+LhrbzMI8zQzHvo7mGPkQICeeim/x+xmGPQtmWnXxCWiL1uf/8eR5Wuy9Er8skTB8rG4/ubb2ssvCkubObPAkMSOgFnX9UtxnCN4+nMNV2vvn4xMTSvvQyYWewfnlNkflTyva1epE9RVW2RqRtJikY="
        )
        s[162] = (
            "Fs+AmFCnUr/imw8D0GpNidIP9qwW8yRAzmtqPS+vT6n5U4YFQcpgbznrYO4TPqkVF2oz1mpgLYIgx/u2XsrtljGX46LfY8OyUPaw4/da38QGngoIlS2cN01cgN3efSjMlnZFo1x8T9p0Nn1IgRgevOd5ezVUL7WdY7eeiE1pXXcGBgDYn7NDQph0dC6HDlBiS95bDFcZ+6FYigE4WybpsOHL"
        )
        s[163] = (
            "wgO4DdGZy9g13IuOhkJGJcToyLuCBVm9T/c8qY4NOheVU1NW2g8sPIo+RiEsSST8sx6+Jh/A/kaCxYvJ9CsgnBjZMMWRsd383HZAoJtkxwKvyoeXzzD+puFvqKQBEKrlBEwffXhLDoFQAW2ycYtBGztl0GsUtoOob2nv7ienx1xD6KNZNaxYx2ObRAYS/e8LS3pg5dku9MPBp1X12m8ZIXRAaw=="
        )
        s[164] = (
            "EkXt02SaRUIjFmoLxyO6N+giL4iA4fY0Exao+mjgEfZ+Wv6w95GXHBI1xlYMVLkOcnu9nescvcXQH0OrqL9uforEUTGTSg2ci67m4GrwAryMy+5eUo77Q5GpWKfsg8nDbD8a3gUI/9EE0sCNp7tMaKwoJ56cxhbG3TJYpqWTpq3/S3q76x+3ETL+zxh6EMh8MJPfWcIxlDS7evKqdPgS00KgUtk="
        )
        s[165] = (
            "OuBqx5LFJroRbDn41+4azFHlKgw6bMgbsRGaK9UnPvi5xfmV4SLQ2YzIhopGi1F57L6vKukaW0XlFk/Ff5Td5IMC7U+kvXKlf8fGIIQ8FaHI0vbIX89OJlBqlICqftSNiVRxtaE+aCh0rBoDfgPwuC8qBC20I1O3ZLuKfeUVGkMOLEWeZLS6mmcn3cSERj9o/dEl8QYwQvhH+VG6YWF//yki1Vu8"
        )
        s[166] = (
            "SO/vDsqZDdImOdH19sZI7FUVhlx1EI0XRr8ArTuAG5F8LDK76Bct2C7fXTUowilXnJWhQxvbGiulkUGSuVjVP12zac9bShRpr1L3ucde7n1f9y/NcHJCwdqTLq7RYygItQ4ppQGiP9jXf2Dn/qmVZZTh+SY3AZCIS+OVo2LAiYJHWnzzoX8Zt+dOYiOA/ZQKZieVJlc8ks+2xqYPD55eH0btZn5hzA=="
        )
        s[167] = (
            "tZL/qACMO9SzmgJhWQMsbKgE5lPAEbxn3NR7504ilgArR8j7uv1KF46uQyjrkEnyBormYB/6nLGlHht62IQftMYf5gHpHFfTvukRKF8728yIYAAYHPQ/WjHzHdVSqUJqF2a8RE6SvvY+KSKWLMU3hjn1f6dqX599hYD7AnbPGTpFKDU5sLFOXbuynU1sPUhP+a4Hev9yNU6atLDo4CkX/Yq3FbpWVuQ="
        )
        s[168] = (
            "GRe7uF1wH5/71B3vmGF+pN3H9PKO1tLwsnb0D4/Pm7Pu5KAe4OfelkfFIBgyjuoZrpeEkGZnb+qf+Kn7Kt1hDwYr/Mb9ewuwOXsbIpLQMgfh0I5XsPrWocduVzn+u/cm3cr0Z11zsx0AZjTqvslACkDqiquY41JhtGdc22RCvIYom2l+zzMIMyCPsHeCSB1MBu8EWK3iP7SD3dWttwzMg0xanoPDgk0U"
        )
        s[169] = (
            "8BDFu+29lptlGSjcZe7ghWaUgIzbuUpM5XDFbtJVQPEd3bAE0cGRlQE9EhKXi5J/IskYNrQ357tBhA+UNDNXCibT2AZGpzWAcwE6dP+14FuRL5Gxqh/teuPYKr5IIn7M3SbgOychZzLI7HGCvVhBUiJBu8orI3WmAIVcUhAsMGHsFveck/ZCXQA+Uq/WVnW1VNs6hSmIhsAFc51qsmsQK07z2Wptx4rRjw=="
        )
        s[170] = (
            "siPSXD4u36WYtTvvDzRlFPiuZMnRczrL3eA15955JDCc6/V2Cvu6m/HPO6JxogxO0aYTZ5tejYDOIZgBy40DgUZMqPJ2IpYjsmUbjjJU8u/OpwhMon525m3v0EYlvyj2Qp3pwFKDkvncK3aNjN3KaaX6HuIy6kyqsDl0BTEnB5iJyHLRBCkeznTK019u48Yfsrz2oGuZcWzNj5/vKMdxQPiyJ9EHyox8Ark="
        )
        s[171] = (
            "+/14PnFQVZ7BTHKUvkTtRrYS7WnPND5gZ5byMhUrDLkJa6UPBV7z0nrDMifEo/dQfUq3EjCiG6xGVhrUvAzgxqOQZTW1Y9p9M0KWW+E0XvCQppHFpuMqF1vYsF0OD6AMiE9JtGnWs3JcaWP/XBF/CvhQlFGbHi3fbrD/haTEBnmpJWBgMdKribdbXHtBSFZ2MzCX2eDtxoDdRdEVGs4v/q8gVBS+WsnZ3TTF"
        )
        s[172] = (
            "31I1ja+B+aopKkztGzJYvJEWAshyoAAV5yve4LnP0kdImUQaVETSuo5CDIYr7zM8MCD1eYPpLicmGnA+C927o9QGAVL3ctO/DCWhNinW7NmeYIM+o4diKBkDPjHmSWa+nq4nr+gOap4CtwL2wW2B5Yqt26pKgN9uAU5CmTL26hYFgMEOZfrkQ7XdYGy2CN8RJLmjeSFVVNBG/FTaK7tpuy0LQSkko6wczBYGeg=="
        )
        s[173] = (
            "XbRfDqGe3eeI1tHx8UnPneDB57N8VeSSzXzVCNSgxOEfd6d/un5CDxHG+m4w3tIbtSky4R2+zMF+S5cRvTOwZ/veegYtLKTxA0mVedWLFkfh/v4NgPJ+NEU+cylbSSZLAeBofDvoJwnYKujN2KFa8PGAxr3Y8ry3qdkS8Ob1ZiHYAmLvKS9sGb/vjTvRy+a4Q7kOepsm7PYisinKelBAvDnjli6/lOutGrenjX4="
        )
        s[174] = (
            "jGEj/AaBefac9uOcmGuO9nH+N+zMsC4qAe6ZUEMMIXdTGnSWl7Xt0/nKqyOj3ZH249HwkJ8bn5C+0bzOpQ1eA3PxEq6RfKMrjHJPJmTZXrSESTjfj3oNLU/CqqDOqd8znTgN6nvnUdCeStLMh9bmWF1+0G11nDwg6GQWWQ0zjVDTq5j7ocXcFOyUcu0cyl5YDcUP0i2mA2JullInU2uBte7nToeSGB3FJxKueBbv"
        )
        s[175] = (
            "RAzNCxlP2S/8LfbGtlSDShox8cSgmJMOc2xPFs8egZVJiwlmnS3aBWKPRbbxkZiVVYlu4GNJNwbocc6dgrl28HXAsYikE5wwoQ1MeOJWU3zzFiYENh7SLBQfjVPQHucctr8P6Rl7YL5wHc+aC+m92R3bnzm5rp1PeHm7uzy2iUUN0cgfbwJ4FrpXhVMTsAUpTbg1+037EWcGOuxir4dG2xBfgOwa+ejFHkw7y0LWRw=="
        )
        s[176] = (
            "08hmZptBGKKqR6Qz9GNc2Wk1etgU/KogbiPQmAh5IXlTBc97DuEToL4Bb889nfObVQ/WelmiCS8wEjSBdmnlkkU7/b5UT3P4k1pB6ZxPH9Qldj5aazkA/yCb0kzDfJlcdFOh1eAcu5LvwTXOizmPwsDvJEnOkaDZrKESZshsHU2A6Mx6awk9/orf6iBlJHQIIH3l4o3b1gx2TNb/hUgdAlwtQDhvKO3skB0PS+rcWAw="
        )
        s[177] = (
            "0GhrgbSSHPLWtyS2mnSxrNAj/dyrFQcxIgPjT7+78SZ1ZTGc03vsmlZ4Z/bOO84E9yKblaI5dSHVXrx57L0kikL8tgKCsAkUNO3l/4zv5FfCrRTgGx4sFTFB1NNcLcwagkvFzde764DjYmj4YZhYsXSZCVKi0uu5M8fpgGDZ9UMSFR008cbhaIoFLWSANqiNJYSvTQZhGWfLtIPGLN+gIOMcaKhx1b5vg6OYSz6ScAM/"
        )
        s[178] = (
            "2VGiMV/f2hNZAjw3fdeHx/wRIVzeP018lZynzwSySG/zQBxyRmi3YmKVZmh3aJunuiqmvdt0kJ6lX7M8BajYHPCBkqJOx8oPJ/K1oADxVgnavZ69dKYrSy9/Pm6sHxjFrdSz9TelUK9sgoFTWS6GxgzWEqXRBDDpGUnsNbSEcWLPKVLNNoYAcltY98JZaNSZBXcpa9FeSN7sVU43q2IEcDx3ZkJzRJpl/lb7n+ivMwX/OQ=="
        )
        s[179] = (
            "iMSCh1m5vct3C7LEn5wKRYtalzvG6pKahG19rTb6Z9q7+buDsML5yM6NqDvoVxt3Dv7KRwdS3xG/Pyb7bJGvQ2a4FhRnTa4HvPvl3cpJdMgCCvsXeXXoML4pHzFlpP0bNsMoupmhQ0khAW51PAr4B165u1y5ULpruxE+dGx/HJUQyMfGhOSZ5jDKKxD5TNYQkDEY28Xqln6Fj8duzQLzMIgSoD8KGZKD8jm6/f8Vwvf43NE="
        )
        s[180] = (
            "hN4+x/sK9FRZn5llaw7/XDGwht3BcIxAFP4JoGqVQCw8c5IOlSqKEOViYss1mnvko6kVrc2iMEA8h8RssJ4dJBpFDZ/bkehCyhQmWpspZtAvRN59mj6nx0SBglYGccPyrn3e0uvvGJ5nYmjTA7gqB0Y+FFGAYwgAO345ipxTrMFsnJ8a913GzpobJdcHiw5hfqYK2iqo8STzVljaGMc5WSzP69vFDTHSS39YSfbE890TPBgm"
        )


Base64Codec13Test.run_static_init()
