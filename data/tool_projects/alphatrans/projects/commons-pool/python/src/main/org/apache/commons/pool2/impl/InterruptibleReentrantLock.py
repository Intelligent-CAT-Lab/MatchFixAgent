from __future__ import annotations
import re
import io
import threading


class InterruptibleReentrantLock:

    __serialVersionUID: int = 1

    def interruptWaiters(self, condition: threading.Condition) -> None:
        for thread in self.getWaitingThreads(condition):
            thread.interrupt()

    def __init__(self, fairness: bool) -> None:
        super().__init__(fairness)
