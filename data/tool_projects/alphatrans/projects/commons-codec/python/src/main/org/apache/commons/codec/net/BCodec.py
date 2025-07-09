from __future__ import annotations
import re
import io
import typing
from typing import *
from src.main.org.apache.commons.codec.CodecPolicy import *
from src.main.org.apache.commons.codec.DecoderException import *
from src.main.org.apache.commons.codec.EncoderException import *
from src.main.org.apache.commons.codec.StringDecoder import *
from src.main.org.apache.commons.codec.StringEncoder import *
from src.main.org.apache.commons.codec.binary.Base64 import *
from src.main.org.apache.commons.codec.binary.BaseNCodec import *
from src.main.org.apache.commons.codec.net.RFC1522Codec import *


class BCodec(StringDecoder, StringEncoder, RFC1522Codec):

    __decodingPolicy: CodecPolicy = None

    __charset: str = ""

    __DECODING_POLICY_DEFAULT: CodecPolicy = CodecPolicy.LENIENT

    def _doDecoding(self, bytes_: typing.List[int]) -> typing.List[int]:
        if bytes_ is None:
            return None
        base64_decoder = Base64(
            0, BaseNCodec.getChunkSeparator(), False, self.__decodingPolicy
        )
        return base64_decoder.decode0(bytes_)

    def _doEncoding(self, bytes_: typing.List[int]) -> typing.List[int]:
        if bytes_ is None:
            return None
        return Base64.encodeBase640(bytes_)

    def _getEncoding(self) -> str:
        return "B"

    def getDefaultCharset(self) -> str:
        return self.__charset

    def getCharset(self) -> str:
        return self.__charset

    def decode1(self, value: typing.Any) -> typing.Any:
        if value is None:
            return None
        if isinstance(value, str):
            return self.decode0(value)
        raise DecoderException(
            f"Objects of type {type(value).__name__} cannot be decoded using BCodec",
            None,
        )

    def encode3(self, value: typing.Any) -> typing.Any:
        if value is None:
            return None
        if isinstance(value, str):
            return self.encode2(value)
        raise EncoderException(
            f"Objects of type {type(value).__name__} cannot be encoded using BCodec",
            None,
        )

    def decode0(self, value: str) -> str:
        if value is None:
            return None
        try:
            return self._decodeText(value)
        except (ValueError, DecoderException) as e:
            raise DecoderException(e.args[0], e)

    def encode2(self, strSource: str) -> str:
        if strSource is None:
            return None
        return self.encode0(strSource, self.getCharset())

    def encode1(self, strSource: str, sourceCharset: str) -> str:
        if strSource is None:
            return None
        try:
            return self._encodeText1(strSource, sourceCharset)
        except UnicodeEncodeError as e:
            raise EncoderException(e.args[0], e)

    def encode0(self, strSource: str, sourceCharset: str) -> str:
        if strSource is None:
            return None
        return self._encodeText0(strSource, sourceCharset)

    def isStrictDecoding(self) -> bool:
        return self.__decodingPolicy == CodecPolicy.STRICT

    @staticmethod
    def BCodec2(charsetName: str) -> BCodec:
        return BCodec.BCodec1(charsetName)

    def __init__(self, charset: str, decodingPolicy: CodecPolicy) -> None:

        pass  # LLM could not translate this method

    @staticmethod
    def BCodec1(charset: str) -> BCodec:
        return BCodec(charset, BCodec._DECODING_POLICY_DEFAULT)

    @staticmethod
    def BCodec0() -> BCodec:
        return BCodec.BCodec1("UTF-8")
