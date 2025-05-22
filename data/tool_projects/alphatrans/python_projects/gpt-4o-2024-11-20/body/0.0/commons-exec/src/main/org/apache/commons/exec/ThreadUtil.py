from __future__ import annotations
import time
import re
import io
import threading
import typing
from typing import *


class ThreadUtil:

    @staticmethod
    def newThread(
        threadFactory: typing.Callable[[typing.Callable], threading.Thread],
        runnable: typing.Callable,
        prefix: str,
        daemon: bool,
    ) -> threading.Thread:
        thread = threadFactory(runnable)
        if thread is None:
            raise RuntimeError(
                f"The ThreadFactory {threadFactory} could not construct a thread for '{prefix}'"
            )
        thread.name = prefix + thread.name
        thread.daemon = daemon
        return thread
