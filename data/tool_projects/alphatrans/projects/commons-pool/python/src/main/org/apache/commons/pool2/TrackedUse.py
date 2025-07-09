from __future__ import annotations
import time
import re
from abc import ABC
import io
import datetime


class TrackedUse(ABC):

    def getLastUsed(self) -> int:
        return 0  # Replace with actual implementation

    def getLastUsedInstant(self) -> datetime.datetime:
        return datetime.datetime.fromtimestamp(self.getLastUsed() / 1000.0)
