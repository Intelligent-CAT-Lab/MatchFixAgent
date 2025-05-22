from __future__ import annotations
import re
from abc import ABC
import io
import typing
from typing import *


class DefaultPooledObjectInfoMBean(ABC):

    def getPooledObjectType(self) -> str:
        return "PooledObjectType"

    def getPooledObjectToString(self) -> str:
        return "PooledObjectToString"

    def getLastReturnTimeFormatted(self) -> str:
        # Placeholder implementation, as the Java method does not provide details.
        # Replace with actual logic if available.
        return ""

    def getLastReturnTime(self) -> int:
        return 0  # Replace 0 with the actual logic if needed

    def getLastBorrowTrace(self) -> str:
        return ""

    def getLastBorrowTimeFormatted(self) -> str:
        # Placeholder implementation, replace with actual logic
        return "Last Borrow Time: Not Implemented"

    def getLastBorrowTime(self) -> int:
        return 0  # Replace 0 with the actual logic if needed

    def getCreateTimeFormatted(self) -> str:
        # Placeholder implementation, as the actual logic is not provided in the Java code.
        # Replace this with the appropriate logic if needed.
        return "Formatted Create Time"

    def getCreateTime(self) -> int:
        return 0  # Replace 0 with the actual logic if needed

    def getBorrowedCount(self) -> int:
        return 0
