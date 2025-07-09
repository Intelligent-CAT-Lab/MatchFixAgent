from __future__ import annotations
import re
import os
import io
import typing
from typing import *
from src.main.me.lemire.integercompression.IntWrapper import *
from src.main.me.lemire.integercompression.UncompressibleInputException import *
from src.main.me.lemire.integercompression.differential.IntegratedBinaryPacking import *
from src.main.me.lemire.integercompression.differential.IntegratedVariableByte import *
from src.main.me.lemire.integercompression.differential.SkippableIntegratedComposition import *
from src.main.me.lemire.integercompression.differential.SkippableIntegratedIntegerCODEC import *


class IntegratedIntCompressor:

    codec: SkippableIntegratedIntegerCODEC = None

    def uncompress(self, compressed: typing.List[int]) -> typing.List[int]:
        decompressed = [0] * compressed[0]
        inpos = IntWrapper(1)
        self.codec.headlessUncompress(
            compressed,
            inpos,
            len(compressed) - inpos.intValue(),
            decompressed,
            IntWrapper(0),
            len(decompressed),
            IntWrapper(0),
        )
        return decompressed

    def compress(self, input_: typing.List[int]) -> typing.List[int]:
        compressed = [0] * (len(input_) + len(input_) // 100 + 1024)
        compressed[0] = len(input_)
        outpos = IntWrapper(1)
        initvalue = IntWrapper(0)
        try:
            self.codec.headlessCompress(
                input_, IntWrapper(0), len(input_), compressed, outpos, initvalue
            )
        except IndexError as ioebe:  # Corrected exception type
            raise UncompressibleInputException(
                f"Your input is too poorly compressible with the current codec: {self.codec}"
            )
        compressed = compressed[: outpos.intValue()]
        return compressed

    def __init__(self, constructorId: int, c: SkippableIntegratedIntegerCODEC) -> None:
        if constructorId == 0:
            self.codec = c
        else:
            self.codec = SkippableIntegratedComposition(
                IntegratedBinaryPacking(), IntegratedVariableByte()
            )
