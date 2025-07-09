from __future__ import annotations
import time
import re
from abc import ABC
from io import StringIO
import io
import typing
from typing import *
import datetime
from src.main.org.apache.commons.pool2.PooledObjectState import *


class PooledObject(ABC):

    def use(self) -> None:
        pass

    def toString(self) -> str:
        return str(self)

    def startEvictionTest(self) -> bool:
        return True

    def setLogAbandoned(self, logAbandoned: bool) -> None:
        self.logAbandoned = logAbandoned

    def printStackTrace(
        self, writer: typing.Union[io.TextIOWrapper, io.StringIO]
    ) -> None:
        import traceback

        # Capture the current exception's stack trace and write it to the writer
        traceback.print_exc(file=writer)

    def markReturning(self) -> None:
        pass

    def markAbandoned(self) -> None:
        # Implementation for marking the object as abandoned
        pass

    def invalidate(self) -> None:
        # Implementation for invalidating the object goes here
        pass

    def hashCode(self) -> int:
        return hash(self)

    def getState(self) -> PooledObjectState:
        return self._state

    def getObject(self) -> typing.Any:
        return self._object

    def getLastUsedTime(self) -> int:
        return int(datetime.datetime.now().timestamp() * 1000)

    def getLastReturnTime(self) -> int:
        return self._last_return_time

    def getLastBorrowTime(self) -> int:
        return int(datetime.datetime.now().timestamp() * 1000)

    def getIdleTimeMillis(self) -> int:
        current_time = (
            datetime.datetime.now().timestamp() * 1000
        )  # Current time in milliseconds
        return int(current_time - self.last_used_time)

    def getCreateTime(self) -> int:
        return int(datetime.datetime.now().timestamp() * 1000)

    def getActiveTimeMillis(self) -> int:
        # Placeholder implementation, replace with actual logic
        return 0

    def equals(self, obj: typing.Any) -> bool:
        return self == obj

    def endEvictionTest(self, idleQueue: typing.Deque[PooledObject]) -> bool:
        return len(idleQueue) == 0

    def deallocate(self) -> bool:
        return True

    def compareTo(self, other: PooledObject) -> int:
        if not isinstance(other, PooledObject):
            raise TypeError("Argument must be of type PooledObject")
        # Implement comparison logic here
        # Example placeholder logic (to be replaced with actual comparison logic):
        return 0  # Replace with actual comparison result

    def allocate(self) -> bool:
        return True

    def setRequireFullStackTrace(self, require_full_stack_trace: bool) -> None:
        pass

    def getLastUsedInstant(self) -> datetime.datetime:
        return datetime.datetime.fromtimestamp(self.getLastUsedTime() / 1000)

    def getLastReturnInstant(self) -> datetime.datetime:
        return datetime.datetime.fromtimestamp(self.getLastReturnTime() / 1000.0)

    def getLastBorrowInstant(self) -> datetime.datetime:
        return datetime.datetime.fromtimestamp(self.getLastBorrowTime() / 1000)

    def getIdleTime(self) -> datetime.timedelta:
        return datetime.timedelta(milliseconds=self.getIdleTimeMillis())

    def getIdleDuration(self) -> datetime.timedelta:
        return datetime.timedelta(milliseconds=self.getIdleTimeMillis())

    def getCreateInstant(self) -> datetime.datetime:
        return datetime.datetime.fromtimestamp(self.getCreateTime() / 1000)

    def getBorrowedCount(self) -> int:
        return -1

    def getActiveTime(self) -> datetime.timedelta:
        return self.getActiveDuration()

    def getActiveDuration(self) -> datetime.timedelta:
        last_return_instant = self.getLastReturnInstant()
        last_borrow_instant = self.getLastBorrowInstant()
        if last_return_instant > last_borrow_instant:
            return last_return_instant - last_borrow_instant
        else:
            return datetime.datetime.now() - last_borrow_instant
