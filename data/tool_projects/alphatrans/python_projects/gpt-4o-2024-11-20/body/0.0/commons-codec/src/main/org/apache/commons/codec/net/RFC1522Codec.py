from __future__ import annotations
import re
from abc import ABC
import io
import typing
from typing import *
from src.main.org.apache.commons.codec.DecoderException import *
from src.main.org.apache.commons.codec.EncoderException import *
from src.main.org.apache.commons.codec.binary.StringUtils import *


class RFC1522Codec(ABC):

    _PREFIX: str = "=?"
    _POSTFIX: str = "?="
    _SEP: str = "?"

    def _decodeText(self, text: str) -> str:
        if text is None:
            return None
        if not text.startswith(self._PREFIX) or not text.endswith(self._POSTFIX):
            raise DecoderException(
                "RFC 1522 violation: malformed encoded content", None
            )

        terminator = len(text) - 2
        from_idx = 2
        to_idx = text.find(self._SEP, from_idx)
        if to_idx == terminator:
            raise DecoderException("RFC 1522 violation: charset token not found", None)

        charset = text[from_idx:to_idx]
        if charset == "":
            raise DecoderException("RFC 1522 violation: charset not specified", None)

        from_idx = to_idx + 1
        to_idx = text.find(self._SEP, from_idx)
        if to_idx == terminator:
            raise DecoderException("RFC 1522 violation: encoding token not found", None)

        encoding = text[from_idx:to_idx]
        if not self._getEncoding().lower() == encoding.lower():
            raise DecoderException(
                f"This codec cannot decode {encoding} encoded content", None
            )

        from_idx = to_idx + 1
        to_idx = text.find(self._SEP, from_idx)
        data = StringUtils.getBytesUsAscii(text[from_idx:to_idx])
        data = self._doDecoding(data)
        return str(bytearray(data), charset)

    def _encodeText1(self, text: str, charsetName: str) -> str:
        if text is None:
            return None
        return self._encodeText0(text, charsetName)

    def _encodeText0(self, text: str, charset: str) -> str:
        if text is None:
            return None
        buffer = []
        buffer.append(self._PREFIX)
        buffer.append(charset)
        buffer.append(self._SEP)
        encoding = self._getEncoding()
        if encoding is None:
            raise EncoderException("Encoding cannot be None")
        buffer.append(encoding)
        buffer.append(self._SEP)
        try:
            encoded_bytes = self._doEncoding(text.encode(charset))
            if encoded_bytes is None:
                raise EncoderException("Encoded bytes cannot be None")
            buffer.append(StringUtils.newStringUsAscii(encoded_bytes))
        except Exception as e:
            raise EncoderException("Encoding error occurred") from e
        buffer.append(self._POSTFIX)
        return "".join(buffer)

    def _doDecoding(self, bytes_: typing.List[int]) -> typing.List[int]:
        raise DecoderException("This method must be implemented by a subclass")

    def _doEncoding(self, bytes_: typing.List[int]) -> typing.List[int]:
        raise EncoderException("This method must be implemented by a subclass")

    def _getEncoding(self) -> str:
        raise NotImplementedError("Subclasses must implement this method")
