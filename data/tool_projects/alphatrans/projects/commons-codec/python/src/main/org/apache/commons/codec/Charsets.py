from __future__ import annotations
import re
import io


class Charsets:

    UTF_8: str = "utf-8"
    UTF_16LE: str = "UTF-16LE"
    UTF_16BE: str = "UTF-16BE"
    UTF_16: str = "UTF-16"
    US_ASCII: str = "US-ASCII"
    ISO_8859_1: str = "ISO-8859-1"

    @staticmethod
    def toCharset1(charset: str) -> str:
        return io.TextIOWrapper().encoding if charset is None else charset

    @staticmethod
    def toCharset0(charset: str | None) -> str:
        return charset if charset is not None else io.TextIOWrapper().encoding
