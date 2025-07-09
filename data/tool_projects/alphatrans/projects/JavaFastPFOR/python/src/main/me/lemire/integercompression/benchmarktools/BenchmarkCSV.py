from __future__ import annotations
import time
import re
import enum
import io
import typing
from typing import *
import os
from src.main.me.lemire.integercompression.BinaryPacking import *
from src.main.me.lemire.integercompression.ByteIntegerCODEC import *
from src.main.me.lemire.integercompression.Composition import *
from src.main.me.lemire.integercompression.FastPFOR import *
from src.main.me.lemire.integercompression.FastPFOR128 import *
from src.main.me.lemire.integercompression.IntWrapper import *
from src.main.me.lemire.integercompression.IntegerCODEC import *
from src.main.me.lemire.integercompression.VariableByte import *
from src.main.me.lemire.integercompression.differential.IntegratedBinaryPacking import *
from src.main.me.lemire.integercompression.differential.IntegratedByteIntegerCODEC import *
from src.main.me.lemire.integercompression.differential.IntegratedComposition import *
from src.main.me.lemire.integercompression.differential.IntegratedIntegerCODEC import *
from src.main.me.lemire.integercompression.differential.IntegratedVariableByte import *


class BenchmarkCSV:

    regbcodecs: typing.List[ByteIntegerCODEC] = [VariableByte()]
    regcodecs: typing.List[IntegerCODEC] = [
        Composition(FastPFOR128.FastPFOR1281(), VariableByte()),
        Composition(FastPFOR.FastPFOR1(), VariableByte()),
        Composition(BinaryPacking(), VariableByte()),
    ]
    bcodecs: typing.List[IntegratedByteIntegerCODEC] = [IntegratedVariableByte()]
    codecs: typing.List[IntegratedIntegerCODEC] = [
        IntegratedComposition(IntegratedBinaryPacking(), IntegratedVariableByte())
    ]

    @staticmethod
    def main(args: List[str]) -> None:
        myformat = Format.ONEARRAYPERLINE
        cm = CompressionMode.DELTA
        files = []

        for s in args:
            if s.startswith("-"):  # it is a flag
                if s == "--onearrayperfile":
                    myformat = Format.ONEARRAYPERFILE
                elif s == "--nodelta":
                    cm = CompressionMode.AS_IS
                elif s == "--oneintperline":
                    myformat = Format.ONEINTPERLINE
                else:
                    raise RuntimeError(f"I don't understand: {s}")
            else:  # it is a filename
                files.append(s)

        if myformat == Format.ONEARRAYPERFILE:
            print("Treating each file as one array.")
        elif myformat == Format.ONEARRAYPERLINE:
            print(
                "Each line of each file is an array: use --onearrayperfile or --oneintperline to change."
            )
        elif myformat == Format.ONEINTPERLINE:
            print("Treating each file as one array, with one integer per line.")

        if cm == CompressionMode.AS_IS:
            print("Compressing the integers 'as is' (no differential coding)")
        else:
            print(
                "Using differential coding (arrays will be sorted): use --nodelta to prevent sorting"
            )

        data = []
        for fn in files:
            for x in BenchmarkCSV.__loadIntegers(fn, myformat):
                data.append(x)

        print(f"Loaded {len(data)} array(s)")

        if cm == CompressionMode.DELTA:
            print("Sorting the array(s) because you are using differential coding")
            for x in data:
                x.sort()

        BenchmarkCSV.__bench(data, cm, False)
        BenchmarkCSV.__bench(data, cm, False)
        BenchmarkCSV.__bench(data, cm, True)
        BenchmarkCSV.__bytebench(data, cm, False)
        BenchmarkCSV.__bytebench(data, cm, False)
        BenchmarkCSV.__bytebench(data, cm, True)

    @staticmethod
    def __bytebench(
        postings: typing.List[typing.List[int]], cm: CompressionMode, verbose: bool
    ) -> None:
        maxlength = 0
        for x in postings:
            if maxlength < len(x):
                maxlength = len(x)
        if verbose:
            print(f"Max array length: {maxlength}")

        compbuffer = bytearray(6 * (maxlength + 1024))
        decompbuffer = [0] * maxlength

        if verbose:
            print("Scheme -- bits/int -- speed (mis)")

        codecs_to_use = (
            BenchmarkCSV.bcodecs
            if cm == CompressionMode.DELTA
            else BenchmarkCSV.regbcodecs
        )

        for c in codecs_to_use:
            bef = 0
            aft = 0
            decomptime = 0
            volumein = 0
            volumeout = 0
            compdata = []

            for k in range(len(postings)):
                in_ = postings[k]
                inpos = IntWrapper(0)
                outpos = IntWrapper(0)

                c.compress1(in_, inpos, len(in_), compbuffer, outpos)
                clength = outpos.get()

                inpos = IntWrapper(0)
                outpos = IntWrapper(0)

                c.uncompress1(compbuffer, inpos, clength, decompbuffer, outpos)
                volumein += len(in_)
                volumeout += clength

                if outpos.get() != len(in_):
                    raise RuntimeError("bug")

                for z in range(len(in_)):
                    if in_[z] != decompbuffer[z]:
                        raise RuntimeError("bug")

                compdata.append(compbuffer[:clength])

            bef = time.time_ns()
            for cin in compdata:
                inpos = IntWrapper(0)
                outpos = IntWrapper(0)

                c.uncompress1(cin, inpos, len(cin), decompbuffer, outpos)

                if inpos.get() != len(cin):
                    raise RuntimeError("bug")
            aft = time.time_ns()

            decomptime += aft - bef
            bitsPerInt = volumeout * 8.0 / volumein
            decompressSpeed = volumein * 1000.0 / decomptime

            if verbose:
                print(f"{c}\t{bitsPerInt:.2f}\t{decompressSpeed:.2f}")

    @staticmethod
    def __bench(
        postings: typing.List[typing.List[int]], cm: CompressionMode, verbose: bool
    ) -> None:
        maxlength = 0
        for x in postings:
            if maxlength < len(x):
                maxlength = len(x)
        if verbose:
            print(f"Max array length: {maxlength}")

        compbuffer = [0] * (2 * maxlength + 1024)
        decompbuffer = [0] * maxlength

        if verbose:
            print("Scheme -- bits/int -- speed (mis)")

        codecs_to_use = (
            BenchmarkCSV.codecs
            if cm == CompressionMode.DELTA
            else BenchmarkCSV.regcodecs
        )

        for c in codecs_to_use:
            bef = 0
            aft = 0
            decomptime = 0
            volumein = 0
            volumeout = 0
            compdata = [None] * len(postings)

            for k, in_ in enumerate(postings):
                inpos = IntWrapper(0)
                outpos = IntWrapper(0)

                # Compress
                c.compress0(in_, inpos, len(in_), compbuffer, outpos)
                clength = outpos.get()

                # Uncompress
                inpos = IntWrapper(0)
                outpos = IntWrapper(0)
                c.uncompress0(compbuffer, inpos, clength, decompbuffer, outpos)

                volumein += len(in_)
                volumeout += clength

                if outpos.get() != len(in_):
                    raise RuntimeError("bug")

                for z in range(len(in_)):
                    if in_[z] != decompbuffer[z]:
                        raise RuntimeError("bug")

                compdata[k] = compbuffer[:clength]

            # Measure decompression time
            bef = time.time_ns()
            for cin in compdata:
                inpos = IntWrapper(0)
                outpos = IntWrapper(0)
                c.uncompress0(cin, inpos, len(cin), decompbuffer, outpos)
                if inpos.get() != len(cin):
                    raise RuntimeError("bug")
            aft = time.time_ns()

            decomptime += aft - bef
            bitsPerInt = volumeout * 32.0 / volumein
            decompressSpeed = volumein * 1000.0 / decomptime

            if verbose:
                print(f"{c}\t\t{bitsPerInt:.2f}\t{decompressSpeed:.2f}")

    @staticmethod
    def __loadIntegers(filename: str, f: Format) -> typing.List[typing.List[int]]:

        pass  # LLM could not translate this method


class Format:

    ONEINTPERLINE: Format = None

    ONEARRAYPERFILE: Format = None

    ONEARRAYPERLINE: Format = None


class CompressionMode:

    DELTA: CompressionMode = None

    AS_IS: CompressionMode = None
