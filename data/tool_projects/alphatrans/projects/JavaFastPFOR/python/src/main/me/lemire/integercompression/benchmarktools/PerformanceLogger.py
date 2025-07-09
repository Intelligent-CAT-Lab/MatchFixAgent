from __future__ import annotations
import time
import re
import io


class PerformanceLogger:

    decompressionTimer: Timer = None
    compressionTimer: Timer = None
    __compressedSize: int = 0
    __originalSize: int = 0

    @staticmethod
    def initialize_fields() -> None:
        PerformanceLogger.compressionTimer: Timer = Timer()

    @staticmethod
    def __getMiS(size: int, nanoTime: int) -> float:
        return (size * 1e-6) / (nanoTime * 1.0e-9)

    def getDecompressSpeed(self) -> float:
        return self.__getMiS(self.__originalSize, self.decompressionTimer.getDuration())

    def getCompressSpeed(self) -> float:
        return self.__getMiS(self.__originalSize, self.compressionTimer.getDuration())

    def getBitPerInt(self) -> float:
        return self.__compressedSize * 32.0 / self.__originalSize

    def getCompressedSize(self) -> int:
        return self.__compressedSize

    def getOriginalSize(self) -> int:
        return self.__originalSize

    def addCompressedSize(self, value: int) -> int:
        self.__compressedSize += value
        return self.__compressedSize

    def addOriginalSize(self, value: int) -> int:
        self.__originalSize += value
        return self.__originalSize


class Timer:

    __duration: int = 0
    __startNano: int = 0

    def getDuration(self) -> int:
        return self.__duration

    def end(self) -> int:
        self.__duration += time.time_ns() - self.__startNano
        return self.__duration

    def start(self) -> None:
        self.__startNano = time.time_ns()

    def __init__(self) -> None:
        pass


PerformanceLogger.initialize_fields()
