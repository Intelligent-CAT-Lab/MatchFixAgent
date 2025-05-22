from __future__ import annotations
import time
import re
import sys
import io
import threading
import typing
from typing import *
from src.main.org.apache.commons.exec.ProcessDestroyer import *


class ShutdownHookProcessDestroyer(ProcessDestroyer):

    __running: bool = False

    __added: bool = False

    __destroyProcessThread: ProcessDestroyerThread = None

    __processes: typing.List[subprocess.Popen] = []

    def size(self) -> int:
        return len(self.__processes)

    def run(self) -> None:
        with threading.Lock():  # Using threading.Lock to synchronize access
            self.__running = True
            for process in self.__processes:
                try:
                    process.terminate()  # Equivalent to Java's process.destroy()
                except Exception as e:
                    print(
                        "Unable to terminate process during process shutdown",
                        file=sys.stderr,
                    )

    def remove(self, process: subprocess.Popen) -> bool:
        with threading.Lock():  # Synchronize access to the processes list
            process_removed = process in self.__processes and self.__processes.remove(
                process
            )
            if process_removed and not self.__processes:
                self.__removeShutdownHook()
            return process_removed

    def add(self, process: subprocess.Popen) -> bool:
        with threading.Lock():  # Simulating synchronized block
            # if this list is empty, register the shutdown hook
            if not self.__processes:
                self.__addShutdownHook()
            self.__processes.append(process)
            return process in self.__processes

    def isEmpty(self) -> bool:
        return self.size() == 0

    def isAddedAsShutdownHook(self) -> bool:
        return self.__added

    def __init__(self) -> None:
        pass

    def __removeShutdownHook(self) -> None:
        if self.__added and not self.__running:
            removed = (
                threading.main_thread()._shutdown_hooks.remove(
                    self.__destroyProcessThread
                )
                if self.__destroyProcessThread
                in threading.main_thread()._shutdown_hooks
                else False
            )
            if not removed:
                print("Could not remove shutdown hook", file=sys.stderr)

            # Start the hook thread, as an unstarted thread may not be eligible for garbage collection
            self.__destroyProcessThread.setShouldDestroy(False)
            self.__destroyProcessThread.start()

            # This should return quickly, since it basically is a NO-OP.
            try:
                self.__destroyProcessThread.join(20)  # 20 seconds
            except Exception as e:
                # The thread didn't die in time
                # It should not kill any processes unexpectedly
                pass

            self.__destroyProcessThread = None
            self.__added = False

    def __addShutdownHook(self) -> None:
        if not self.__running:
            self.__destroyProcessThread = ProcessDestroyerThread()
            threading.get_native_id()  # Simulating Runtime.getRuntime() in Python
            import atexit

            atexit.register(self.__destroyProcessThread)
            self.__added = True


class ProcessDestroyerThread(threading.Thread):

    __shouldDestroy: bool = True

    def run(self) -> None:
        if self.__shouldDestroy:
            ShutdownHookProcessDestroyer().run()

    def setShouldDestroy(self, shouldDestroy: bool) -> None:
        self.__shouldDestroy = shouldDestroy

    def __init__(self) -> None:
        super().__init__(name="ProcessDestroyer Shutdown Hook")
