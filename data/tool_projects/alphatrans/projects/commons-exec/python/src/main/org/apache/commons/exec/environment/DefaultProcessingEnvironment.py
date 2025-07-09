from __future__ import annotations
import copy
import re
import sys
import os
from io import BytesIO
from io import StringIO
import io
import typing
from typing import *
from src.main.org.apache.commons.exec.CommandLine import *
from src.main.org.apache.commons.exec.OS import *


class DefaultProcessingEnvironment:

    _procEnvironment: typing.Dict[str, str] = None

    def _runProcEnvCommand(self) -> io.BufferedReader:
        # Create a ByteArrayOutputStream equivalent
        out = io.BytesIO()

        # Create an Executor instance (assuming DefaultExecutor.builder().get() is equivalent to some Python implementation)
        exe = DefaultExecutor.builder().get()

        # Set the stream handler to capture the output
        exe.setStreamHandler(PumpStreamHandler(out))

        # Execute the command and ignore the exit value
        exe.execute(self._getProcEnvCommand())

        # Convert the output to a string and return a BufferedReader
        return io.BufferedReader(io.StringIO(out.getvalue().decode("utf-8")))

    def _getProcEnvCommand(self) -> CommandLine:
        executable = None
        arguments = None

        if OS.isFamilyOS2():
            # OS/2 - use same mechanism as Windows 2000
            executable = "cmd"
            arguments = ["/c", "set"]
        elif OS.isFamilyWindows():
            # Determine if we're running under XP/2000/NT or 98/95
            if OS.isFamilyWin9x():
                # Windows 98/95
                executable = "command.com"
            else:
                # Windows XP/2000/NT/2003
                executable = "cmd"
            arguments = ["/c", "set"]
        elif OS.isFamilyZOS() or OS.isFamilyUnix():
            # On most systems one could use: /bin/sh -c env
            # Some systems have /bin/env, others /usr/bin/env, just try
            if os.path.isfile("/bin/env"):
                executable = "/bin/env"
            elif os.path.isfile("/usr/bin/env"):
                executable = "/usr/bin/env"
            else:
                # rely on PATH
                executable = "env"
        elif OS.isFamilyNetware() or OS.isFamilyOS400():
            # rely on PATH
            executable = "env"
        else:
            # macOS 9 and previous
            # TODO: I have no idea how to get it, someone must fix it
            executable = None

        command_line = None
        if executable is not None:
            command_line = CommandLine(executable)
            if arguments:
                command_line.addArguments(arguments)

        return command_line

    def getProcEnvironment(self) -> typing.Dict[str, str]:
        if self._procEnvironment is None:
            self._procEnvironment = self._createProcEnvironment()

        # Create a copy of the environment map to avoid modifications
        copy = self.__createEnvironmentMap()
        copy.update(self._procEnvironment)
        return copy

    def _createProcEnvironment(self) -> typing.Dict[str, str]:
        if self._procEnvironment is None:
            self._procEnvironment = self.__createEnvironmentMap()
            self._procEnvironment.update(os.environ)
        return self._procEnvironment

    def __createEnvironmentMap(self) -> typing.Dict[str, str]:
        if OS.isFamilyWindows():
            return dict()  # Python's `dict` is case-sensitive by default
        return {}
