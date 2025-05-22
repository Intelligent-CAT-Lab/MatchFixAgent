from __future__ import annotations
import re
import io
import typing
from typing import *
import os
from src.main.me.lemire.integercompression.BitPacking import *
from src.main.me.lemire.integercompression.IntWrapper import *
from src.main.me.lemire.integercompression.IntegerCODEC import *
from src.main.me.lemire.integercompression.SkippableIntegerCODEC import *
from src.main.me.lemire.integercompression.Util import *


class FastPFOR(IntegerCODEC, SkippableIntegerCODEC):

    bestbbestcexceptmaxb: typing.List[int] = [0, 0, 0]
    freqs: typing.List[int] = [0] * 33
    dataPointers: typing.List[int] = [0] * 33
    byteContainer: typing.Union[bytearray, memoryview] = None

    dataTobePacked: typing.List[typing.List[int]] = [[] for _ in range(33)]
    pageSize: int = 0

    BLOCK_SIZE: int = 256
    DEFAULT_PAGE_SIZE: int = 65536
    OVERHEAD_OF_EACH_EXCEPT: int = 8

    def toString(self) -> str:
        return self.__class__.__name__

    def uncompress0(
        self,
        in_: typing.List[int],
        inpos: IntWrapper,
        inlength: int,
        out: typing.List[int],
        outpos: IntWrapper,
    ) -> None:
        if inlength == 0:
            return
        outlength = in_[inpos.get()]
        inpos.increment()
        self.headlessUncompress(in_, inpos, inlength, out, outpos, outlength)

    def compress0(
        self,
        in_: typing.List[int],
        inpos: IntWrapper,
        inlength: int,
        out: typing.List[int],
        outpos: IntWrapper,
    ) -> None:
        inlength = Util.greatestMultiple(inlength, self.BLOCK_SIZE)
        if inlength == 0:
            return
        out[outpos.get()] = inlength
        outpos.increment()
        self.headlessCompress(in_, inpos, inlength, out, outpos)

    def headlessUncompress(
        self,
        in_: typing.List[int],
        inpos: IntWrapper,
        inlength: int,
        out: typing.List[int],
        outpos: IntWrapper,
        mynvalue: int,
    ) -> None:
        mynvalue = Util.greatestMultiple(mynvalue, self.BLOCK_SIZE)
        finalout = outpos.get() + mynvalue
        while outpos.get() != finalout:
            thissize = min(self.pageSize, finalout - outpos.get())
            self.__decodePage(in_, inpos, out, outpos, thissize)

    def headlessCompress(
        self,
        in_: typing.List[int],
        inpos: IntWrapper,
        inlength: int,
        out: typing.List[int],
        outpos: IntWrapper,
    ) -> None:
        inlength = Util.greatestMultiple(inlength, self.BLOCK_SIZE)
        # Allocate memory for working area.

        finalinpos = inpos.get() + inlength
        while inpos.get() != finalinpos:
            thissize = min(self.pageSize, finalinpos - inpos.get())
            self.__encodePage(in_, inpos, thissize, out, outpos)

    return memoryview(bytearray(sizeInBytes))

    @staticmethod
    def FastPFOR1() -> FastPFOR:
        return FastPFOR(FastPFOR.DEFAULT_PAGE_SIZE)

    def __init__(self, pagesize: int) -> None:
        self.pageSize = pagesize
        # Initialize byteContainer
        self.byteContainer = memoryview(
            bytearray(3 * self.pageSize // self.BLOCK_SIZE + self.pageSize)
        )
        # Initialize dataTobePacked
        self.dataTobePacked = [[] for _ in range(33)]
        for k in range(1, len(self.dataTobePacked)):
            self.dataTobePacked[k] = [0] * (self.pageSize // 32 * 4)  # heuristic

    def __decodePage(
        self,
        in_: typing.List[int],
        inpos: IntWrapper,
        out: typing.List[int],
        outpos: IntWrapper,
        thissize: int,
    ) -> None:
        initpos = inpos.get()
        wheremeta = in_[inpos.get()]
        inpos.increment()
        inexcept = initpos + wheremeta
        bytesize = in_[inexcept]
        inexcept += 1
        self.byteContainer.clear()
        self.byteContainer[: (bytesize + 3) // 4 * 4] = in_[
            inexcept : inexcept + (bytesize + 3) // 4
        ]
        inexcept += (bytesize + 3) // 4

        bitmap = in_[inexcept]
        inexcept += 1
        for k in range(2, 33):
            if (bitmap & (1 << (k - 1))) != 0:
                size = in_[inexcept]
                inexcept += 1
                roundedup = Util.greatestMultiple(size + 31, 32)
                if len(self.dataTobePacked[k]) < roundedup:
                    self.dataTobePacked[k] = [0] * roundedup
                if inexcept + roundedup // 32 * k <= len(in_):
                    j = 0
                    while j < size:
                        BitPacking.fastunpack(
                            in_, inexcept, self.dataTobePacked[k], j, k
                        )
                        inexcept += k
                        j += 32
                    overflow = j - size
                    inexcept -= overflow * k // 32
                else:
                    j = 0
                    buf = [0] * (roundedup // 32 * k)
                    initinexcept = inexcept
                    buf[: len(in_) - inexcept] = in_[inexcept:]
                    while j < size:
                        BitPacking.fastunpack(
                            buf, inexcept - initinexcept, self.dataTobePacked[k], j, k
                        )
                        inexcept += k
                        j += 32
                    overflow = j - size
                    inexcept -= overflow * k // 32

        self.dataPointers = [0] * 33
        tmpoutpos = outpos.get()
        tmpinpos = inpos.get()

        for run in range(thissize // self.BLOCK_SIZE):
            b = self.byteContainer[0]
            self.byteContainer = self.byteContainer[1:]
            cexcept = self.byteContainer[0] & 0xFF
            self.byteContainer = self.byteContainer[1:]
            for k in range(0, self.BLOCK_SIZE, 32):
                BitPacking.fastunpack(in_, tmpinpos, out, tmpoutpos + k, b)
                tmpinpos += b
            if cexcept > 0:
                maxbits = self.byteContainer[0]
                self.byteContainer = self.byteContainer[1:]
                index = maxbits - b
                if index == 1:
                    for k in range(cexcept):
                        pos = self.byteContainer[0] & 0xFF
                        self.byteContainer = self.byteContainer[1:]
                        out[pos + tmpoutpos] |= 1 << b
                else:
                    for k in range(cexcept):
                        pos = self.byteContainer[0] & 0xFF
                        self.byteContainer = self.byteContainer[1:]
                        exceptvalue = self.dataTobePacked[index][
                            self.dataPointers[index]
                        ]
                        self.dataPointers[index] += 1
                        out[pos + tmpoutpos] |= exceptvalue << b

            tmpoutpos += self.BLOCK_SIZE

        outpos.set_(tmpoutpos)
        inpos.set_(inexcept)

    def __encodePage(
        self,
        in_: typing.List[int],
        inpos: IntWrapper,
        thissize: int,
        out: typing.List[int],
        outpos: IntWrapper,
    ) -> None:
        headerpos = outpos.get()
        outpos.increment()
        tmpoutpos = outpos.get()

        # Clear working area
        self.dataPointers = [0] * len(self.dataPointers)
        self.byteContainer = bytearray()

        tmpinpos = inpos.get()
        finalinpos = tmpinpos + thissize - self.BLOCK_SIZE

        while tmpinpos <= finalinpos:
            self.__getBestBFromData(in_, tmpinpos)
            tmpbestb = self.bestbbestcexceptmaxb[0]
            self.byteContainer.append(self.bestbbestcexceptmaxb[0])
            self.byteContainer.append(self.bestbbestcexceptmaxb[1])

            if self.bestbbestcexceptmaxb[1] > 0:
                self.byteContainer.append(self.bestbbestcexceptmaxb[2])
                index = self.bestbbestcexceptmaxb[2] - self.bestbbestcexceptmaxb[0]

                if self.dataPointers[index] + self.bestbbestcexceptmaxb[1] >= len(
                    self.dataTobePacked[index]
                ):
                    newsize = 2 * (
                        self.dataPointers[index] + self.bestbbestcexceptmaxb[1]
                    )
                    newsize = Util.greatestMultiple(newsize + 31, 32)
                    self.dataTobePacked[index] = self.dataTobePacked[index][:newsize]

                for k in range(self.BLOCK_SIZE):
                    if (in_[k + tmpinpos] >> self.bestbbestcexceptmaxb[0]) != 0:
                        self.byteContainer.append(k)
                        self.dataTobePacked[index][self.dataPointers[index]] = (
                            in_[k + tmpinpos] >> tmpbestb
                        )
                        self.dataPointers[index] += 1

            for k in range(0, self.BLOCK_SIZE, 32):
                BitPacking.fastpack(in_, tmpinpos + k, out, tmpoutpos, tmpbestb)
                tmpoutpos += tmpbestb

            tmpinpos += self.BLOCK_SIZE

        inpos.set_(tmpinpos)
        out[headerpos] = tmpoutpos - headerpos
        bytesize = len(self.byteContainer)

        while len(self.byteContainer) % 4 != 0:
            self.byteContainer.append(0)

        out[tmpoutpos] = bytesize
        tmpoutpos += 1

        howmanyints = len(self.byteContainer) // 4
        int_buffer = memoryview(self.byteContainer).cast("I")
        out[tmpoutpos : tmpoutpos + howmanyints] = int_buffer[:howmanyints]
        tmpoutpos += howmanyints

        bitmap = 0
        for k in range(2, 33):
            if self.dataPointers[k] != 0:
                bitmap |= 1 << (k - 1)

        out[tmpoutpos] = bitmap
        tmpoutpos += 1

        for k in range(2, 33):
            if self.dataPointers[k] != 0:
                out[tmpoutpos] = self.dataPointers[k]
                tmpoutpos += 1
                j = 0
                while j < self.dataPointers[k]:
                    BitPacking.fastpack(self.dataTobePacked[k], j, out, tmpoutpos, k)
                    tmpoutpos += k
                    j += 32

                overflow = j - self.dataPointers[k]
                tmpoutpos -= overflow * k // 32

        outpos.set_(tmpoutpos)

    def __getBestBFromData(self, in_: typing.List[int], pos: int) -> None:
        # Reset the frequency array
        self.freqs = [0] * 33

        # Calculate the frequency of bit lengths
        for k in range(pos, pos + self.BLOCK_SIZE):
            self.freqs[Util.bits(in_[k])] += 1

        # Initialize bestbbestcexceptmaxb[0] to 32
        self.bestbbestcexceptmaxb[0] = 32

        # Find the largest bit length with a non-zero frequency
        while self.freqs[self.bestbbestcexceptmaxb[0]] == 0:
            self.bestbbestcexceptmaxb[0] -= 1

        # Set initial values for bestbbestcexceptmaxb[2] and bestcost
        self.bestbbestcexceptmaxb[2] = self.bestbbestcexceptmaxb[0]
        bestcost = self.bestbbestcexceptmaxb[0] * self.BLOCK_SIZE
        cexcept = 0
        self.bestbbestcexceptmaxb[1] = cexcept

        # Iterate over possible bit lengths
        for b in range(self.bestbbestcexceptmaxb[0] - 1, -1, -1):
            cexcept += self.freqs[b + 1]
            if cexcept == self.BLOCK_SIZE:
                break

            # Calculate the cost for the current bit length
            thiscost = (
                cexcept * self.OVERHEAD_OF_EACH_EXCEPT
                + cexcept * (self.bestbbestcexceptmaxb[2] - b)
                + b * self.BLOCK_SIZE
                + 8
            )

            # Adjust cost if the difference in bit lengths is 1
            if self.bestbbestcexceptmaxb[2] - b == 1:
                thiscost -= cexcept

            # Update the best cost and corresponding values
            if thiscost < bestcost:
                bestcost = thiscost
                self.bestbbestcexceptmaxb[0] = b
                self.bestbbestcexceptmaxb[1] = cexcept
