from __future__ import annotations
import time
import re
import sys
import os
from io import BytesIO
from io import IOBase
import io
import typing
from typing import *


class MingwSupport:

    __columnsPatterns: re.Pattern = None

    __ttyCommand: str = ""

    __sttyCommand: str = ""

    def getTerminalWidth(self, name: str) -> int:
        try:
            # Start the process with the stty command
            p = subprocess.Popen(
                [self.__sttyCommand, "-F", name, "-a"],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
            )

            # Capture the output of the process
            result = self.__waitAndCapture(p)

            # Check the exit value of the process
            if p.returncode != 0:
                raise IOError(f"Error executing '{self.__sttyCommand}': {result}")

            # Match the output against the columns pattern
            matcher = self.__columnsPatterns.search(result)
            if matcher:
                return int(matcher.group(1))

            # Raise an exception if the columns pattern is not found
            raise IOError("Unable to parse columns")

        except Exception as e:
            # Wrap any exception in a RuntimeError
            raise RuntimeError(e)

    def getConsoleName(self, stdout: bool) -> str:
        try:
            # Determine the file descriptor to redirect (stdout or stderr)
            redirect = self.__getRedirect(io.FileIO(1 if stdout else 2))

            # Create and start the process
            p = subprocess.Popen(
                [self.__ttyCommand],
                stdin=redirect.fd,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
            )

            # Wait for the process to complete and capture its output
            result = self.__waitAndCapture(p)

            # Check the exit value of the process
            if p.returncode == 0:
                return result.strip()
        except Exception as t:
            # Handle specific exception for InaccessibleObjectException
            if t.__class__.__name__ == "InaccessibleObjectException":
                print(
                    "MINGW support requires --add-opens java.base/java.lang=ALL-UNNAMED",
                    file=sys.stderr,
                )
            # Ignore other exceptions silently
            pass

        return None

    def __init__(self) -> None:
        tty = None
        stty = None
        path = os.getenv("PATH")
        if path is not None:
            paths = path.split(os.pathsep)
            for p in paths:
                tty_file = os.path.join(p, "tty.exe")
                if (
                    tty is None
                    and os.path.isfile(tty_file)
                    and os.access(tty_file, os.X_OK)
                ):
                    tty = tty_file
                stty_file = os.path.join(p, "stty.exe")
                if (
                    stty is None
                    and os.path.isfile(stty_file)
                    and os.access(stty_file, os.X_OK)
                ):
                    stty = stty_file
        if tty is None:
            tty = "tty.exe"
        if stty is None:
            stty = "stty.exe"
        self.__ttyCommand = tty
        self.__sttyCommand = stty
        # Compute patterns
        self.__columnsPatterns = re.compile(r"\bcolumns\s+(\d+)\b")

    def __getRedirect(self, fd: io.RawIOBase) -> typing.Any:
        # This is not really allowed, but this is the only way to redirect the output or error stream
        # to the input. This is definitely not something you'd usually want to do, but in the case of
        # the `tty` utility, it provides a way to get
        rpi = type(
            "RedirectPipeImpl", (), {}
        )  # Simulating the creation of a dynamic class
        cns = rpi.__new__(rpi)  # Simulating the constructor
        setattr(cns, "fd", fd)  # Setting the 'fd' field dynamically
        return cns

    @staticmethod
    def __waitAndCapture(p: subprocess.Popen) -> str:
        bout = io.BytesIO()
        try:
            with p.stdout as out, p.stderr as err:
                while c := out.read(1):
                    bout.write(c)
                while c := err.read(1):
                    bout.write(c)
            p.wait()
        except Exception as e:
            raise e
        return bout.getvalue().decode()
