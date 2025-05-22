from __future__ import annotations
import re
import io
import typing
from typing import *
from src.main.org.apache.commons.codec.DecoderException import *
from src.main.org.apache.commons.codec.EncoderException import *
from src.main.org.apache.commons.codec.StringDecoder import *
from src.main.org.apache.commons.codec.StringEncoder import *
from src.main.org.apache.commons.codec.net.QuotedPrintableCodec import *
from src.main.org.apache.commons.codec.net.RFC1522Codec import *


class QCodec(StringDecoder, StringEncoder, RFC1522Codec):

    __encodeBlanks: bool = False
    __UNDERSCORE: int = 95
    __SPACE: int = 32
    __PRINTABLE_CHARS: typing.List[bool] = [False] * 256
    __charset: str = ""

    @staticmethod
    def run_static_init():
        QCodec.__PRINTABLE_CHARS[ord(" ")] = True
        QCodec.__PRINTABLE_CHARS[ord("!")] = True
        QCodec.__PRINTABLE_CHARS[ord('"')] = True
        QCodec.__PRINTABLE_CHARS[ord("#")] = True
        QCodec.__PRINTABLE_CHARS[ord("$")] = True
        QCodec.__PRINTABLE_CHARS[ord("%")] = True
        QCodec.__PRINTABLE_CHARS[ord("&")] = True
        QCodec.__PRINTABLE_CHARS[ord("'")] = True
        QCodec.__PRINTABLE_CHARS[ord("(")] = True
        QCodec.__PRINTABLE_CHARS[ord(")")] = True
        QCodec.__PRINTABLE_CHARS[ord("*")] = True
        QCodec.__PRINTABLE_CHARS[ord("+")] = True
        QCodec.__PRINTABLE_CHARS[ord(",")] = True
        QCodec.__PRINTABLE_CHARS[ord("-")] = True
        QCodec.__PRINTABLE_CHARS[ord(".")] = True
        QCodec.__PRINTABLE_CHARS[ord("/")] = True
        for i in range(ord("0"), ord("9") + 1):
            QCodec.__PRINTABLE_CHARS[i] = True
        QCodec.__PRINTABLE_CHARS[ord(":")] = True
        QCodec.__PRINTABLE_CHARS[ord(";")] = True
        QCodec.__PRINTABLE_CHARS[ord("<")] = True
        QCodec.__PRINTABLE_CHARS[ord(">")] = True
        QCodec.__PRINTABLE_CHARS[ord("@")] = True
        for i in range(ord("A"), ord("Z") + 1):
            QCodec.__PRINTABLE_CHARS[i] = True
        QCodec.__PRINTABLE_CHARS[ord("[")] = True
        QCodec.__PRINTABLE_CHARS[ord("\\")] = True
        QCodec.__PRINTABLE_CHARS[ord("]")] = True
        QCodec.__PRINTABLE_CHARS[ord("^")] = True
        QCodec.__PRINTABLE_CHARS[ord("`")] = True
        for i in range(ord("a"), ord("z") + 1):
            QCodec.__PRINTABLE_CHARS[i] = True
        QCodec.__PRINTABLE_CHARS[ord("{")] = True
        QCodec.__PRINTABLE_CHARS[ord("|")] = True
        QCodec.__PRINTABLE_CHARS[ord("}")] = True
        QCodec.__PRINTABLE_CHARS[ord("~")] = True

    def _doDecoding(self, bytes_: typing.List[int]) -> typing.List[int]:
        if bytes_ is None:
            return None

        has_underscores = any(b == self.__UNDERSCORE for b in bytes_)

        if has_underscores:
            tmp = [self.__SPACE if b == self.__UNDERSCORE else b for b in bytes_]
            return QuotedPrintableCodec.decodeQuotedPrintable(tmp)

        return QuotedPrintableCodec.decodeQuotedPrintable(bytes_)

    def _doEncoding(self, bytes_: typing.List[int]) -> typing.List[int]:
        if bytes_ is None:
            return None
        data = QuotedPrintableCodec.encodeQuotedPrintable1(
            self.__PRINTABLE_CHARS, bytes_
        )
        if self.__encodeBlanks:
            for i in range(len(data)):
                if data[i] == self.__SPACE:
                    data[i] = self.__UNDERSCORE
        return data

    def _getEncoding(self) -> str:
        return "Q"

    def setEncodeBlanks(self, b: bool) -> None:
        self.__encodeBlanks = b

    def isEncodeBlanks(self) -> bool:
        return self.__encodeBlanks

    def getDefaultCharset(self) -> str:
        return self.__charset

    def getCharset(self) -> str:
        return self.__charset

    def decode1(self, obj: typing.Any) -> typing.Any:
        if obj is None:
            return None
        if isinstance(obj, str):
            return self.decode0(obj)
        raise DecoderException(
            f"Objects of type {type(obj).__name__} cannot be decoded using Q codec",
            None,
        )

    def encode3(self, obj: typing.Any) -> typing.Any:
        if obj is None:
            return None
        if isinstance(obj, str):
            return self.encode2(obj)
        raise EncoderException(
            f"Objects of type {type(obj).__name__} cannot be encoded using Q codec",
            None,
        )

    def decode0(self, str_: str) -> str:
        if str_ is None:
            return None
        try:
            return self._decodeText(str_)
        except UnicodeDecodeError as e:
            raise DecoderException(e.args[0], e)

    def encode2(self, sourceStr: str) -> str:
        if sourceStr is None:
            return None
        try:
            return self.encode0(sourceStr, self.getCharset())
        except Exception as e:
            raise EncoderException("Encoding error occurred") from e

    def encode1(self, sourceStr: str, sourceCharset: str) -> str:
        if sourceStr is None:
            return None
        try:
            return self._encodeText1(sourceStr, sourceCharset)
        except ValueError as e:
            raise EncoderException(e.args[0], e)

    def encode0(self, sourceStr: str, sourceCharset: str) -> str:
        if sourceStr is None:
            return None
        return self._encodeText0(sourceStr, sourceCharset)

    @staticmethod
    def QCodec2() -> QCodec:
        return QCodec(1, None, "UTF-8")

    @staticmethod
    def QCodec0(charsetName: str) -> QCodec:
        return QCodec(1, charsetName, charsetName)

    def __init__(self, constructorId: int, charsetName: str, charset: str) -> None:
        if constructorId == 1:
            self.__charset = charset
        else:
            self.__charset = charset


QCodec.run_static_init()
