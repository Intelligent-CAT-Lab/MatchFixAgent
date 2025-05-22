from __future__ import annotations
import re
import os
import typing
from typing import *
import threading
import io
import sys
import typing
from src.main.org.fusesource.jansi.AnsiColors import *
from src.main.org.fusesource.jansi.AnsiMode import *
from src.main.org.fusesource.jansi.AnsiPrintStream import *
from src.main.org.fusesource.jansi.AnsiType import *
from src.main.org.fusesource.jansi.internal.CLibrary import *
from src.main.org.fusesource.jansi.internal.Kernel32 import *
from src.main.org.fusesource.jansi.internal.MingwSupport import *
from src.main.org.fusesource.jansi.io.AnsiOutputStream import *
from src.main.org.fusesource.jansi.io.AnsiProcessor import *
from src.main.org.fusesource.jansi.io.FastBufferedOutputStream import *
from src.main.org.fusesource.jansi.io.WindowsAnsiProcessor import *


class AnsiConsole:

    STDERR_FILENO: int = 2
    STDOUT_FILENO: int = 1
    ENABLE_VIRTUAL_TERMINAL_PROCESSING: int = 0x0004
    IS_WINDOWS: bool = "win" in sys.platform.lower()
    err: typing.IO = None

    system_err: typing.IO = sys.stderr
    out: typing.IO = None

    system_out: typing.IO = sys.stdout
    JANSI_GRACEFUL: str = "jansi.graceful"
    JANSI_NORESET: str = "jansi.noreset"
    JANSI_EAGER: str = "jansi.eager"
    JANSI_FORCE: str = "jansi.force"
    JANSI_STRIP: str = "jansi.strip"
    JANSI_PASSTHROUGH: str = "jansi.passthrough"
    JANSI_COLORS_TRUECOLOR: str = "truecolor"
    JANSI_COLORS_256: str = "256"
    JANSI_COLORS_16: str = "16"
    JANSI_ERR_COLORS: str = "jansi.err.colors"
    JANSI_OUT_COLORS: str = "jansi.out.colors"
    JANSI_COLORS: str = "jansi.colors"
    JANSI_MODE_DEFAULT: str = "default"
    JANSI_MODE_FORCE: str = "force"
    JANSI_MODE_STRIP: str = "strip"
    JANSI_ERR_MODE: str = "jansi.err.mode"
    JANSI_OUT_MODE: str = "jansi.out.mode"
    JANSI_MODE: str = "jansi.mode"
    __virtualProcessing: int = 0

    __installed: int = 0

    __initialized: bool = False

    IS_CONEMU: bool = IS_WINDOWS and (os.getenv("ConEmuPID") is not None)
    IS_MSYSTEM: bool = (
        IS_WINDOWS
        and (msystem := os.getenv("MSYSTEM")) is not None
        and (msystem.startswith("MINGW") or msystem == "MSYS")
    )
    IS_CYGWIN: bool = (
        IS_WINDOWS
        and (os.getenv("PWD") is not None)
        and os.getenv("PWD").startswith("/")
    )

    @staticmethod
    def run_static_init():
        if AnsiConsole.getBoolean(AnsiConsole.JANSI_EAGER):
            AnsiConsole.initStreams()

    @staticmethod
    def initStreams() -> None:
        if not AnsiConsole.__initialized:
            AnsiConsole.out = AnsiConsole.__ansiStream(True)
            AnsiConsole.err = AnsiConsole.__ansiStream(False)
            AnsiConsole.__initialized = True

    @staticmethod
    def systemUninstall() -> None:
        AnsiConsole.__installed -= 1
        if AnsiConsole.__installed == 0:
            try:
                if isinstance(AnsiConsole.out, AnsiPrintStream):
                    AnsiConsole.out.uninstall()
                if isinstance(AnsiConsole.err, AnsiPrintStream):
                    AnsiConsole.err.uninstall()
            except IOError as e:
                raise OSError(e)
            AnsiConsole.__initialized = False
            sys.stdout = AnsiConsole.system_out
            sys.stderr = AnsiConsole.system_err

    @staticmethod
    def isInstalled() -> bool:
        return AnsiConsole.__installed > 0

    @staticmethod
    def systemInstall() -> None:
        if AnsiConsole.__installed == 0:
            AnsiConsole.initStreams()
            try:
                AnsiConsole.out.install()
                AnsiConsole.err.install()
            except IOError as e:
                raise OSError(e)
            sys.stdout = AnsiConsole.out
            sys.stderr = AnsiConsole.err
        AnsiConsole.__installed += 1

    @staticmethod
    def sysErr() -> typing.IO:
        return AnsiConsole.system_err

    @staticmethod
    def err() -> AnsiPrintStream:
        AnsiConsole.initStreams()
        return AnsiConsole.err

    @staticmethod
    def sysOut() -> typing.IO:
        return AnsiConsole.system_out

    @staticmethod
    def out() -> AnsiPrintStream:
        AnsiConsole.initStreams()
        return typing.cast(AnsiPrintStream, AnsiConsole.out)

    @staticmethod
    def getBoolean(name: str) -> bool:
        result = False
        try:
            val = sys.getProperty(name)  # Simulating System.getProperty in Python
            if val is not None:
                result = val == "" or val.lower() in ("true", "1", "yes")
        except (ValueError, TypeError):
            pass
        return result

    @staticmethod
    def getTerminalWidth() -> int:
        w = AnsiConsole.out().getTerminalWidth()
        if w <= 0:
            w = AnsiConsole.err().getTerminalWidth()
        return w

    @staticmethod
    def __newPrintStream(out: AnsiOutputStream, enc: str) -> AnsiPrintStream:
        if enc is not None:
            try:
                return AnsiPrintStream(out, True, enc)
            except ValueError:
                pass
        try:
            return AnsiPrintStream(out, True, None)
        except ValueError:
            pass
        return None

    @staticmethod
    def __ansiStream(stdout: bool) -> AnsiPrintStream:
        descriptor = sys.stdout.fileno() if stdout else sys.stderr.fileno()
        out = FastBufferedOutputStream(io.FileIO(descriptor, mode="wb"))

        enc = sys.getProperty(
            "stdout.encoding" if stdout else "stderr.encoding"
        ) or sys.getProperty("sun.stdout.encoding" if stdout else "sun.stderr.encoding")

        fd = AnsiConsole.STDOUT_FILENO if stdout else AnsiConsole.STDERR_FILENO
        try:
            isatty = os.isatty(fd)
            term = os.getenv("TERM")
            emacs = os.getenv("INSIDE_EMACS")
            if isatty and term == "dumb" and emacs and "comint" not in emacs:
                isatty = False
            with_exception = False
        except Exception:
            isatty = False
            with_exception = True

        if not isatty:
            processor = None
            type_ = AnsiType.Unsupported if with_exception else AnsiType.Redirected
            installer = uninstaller = None
            width = AnsiOutputStream.ZeroWidthSupplier()
        elif AnsiConsole.IS_WINDOWS:
            console = Kernel32.GetStdHandle(
                Kernel32.STD_OUTPUT_HANDLE if stdout else Kernel32.STD_ERROR_HANDLE
            )
            mode = [0]
            is_console = Kernel32.GetConsoleMode(console, mode) != 0

            def kernel32_width():
                info = CONSOLE_SCREEN_BUFFER_INFO()
                Kernel32.GetConsoleScreenBufferInfo(console, info)
                return info.windowWidth()

            if is_console and Kernel32.SetConsoleMode(
                console, mode[0] | AnsiConsole.ENABLE_VIRTUAL_TERMINAL_PROCESSING
            ):
                Kernel32.SetConsoleMode(console, mode[0])  # Reset for now
                processor = None
                type_ = AnsiType.VirtualTerminal

                def installer():
                    with threading.Lock():
                        AnsiConsole.__virtualProcessing += 1
                        Kernel32.SetConsoleMode(
                            console,
                            mode[0] | AnsiConsole.ENABLE_VIRTUAL_TERMINAL_PROCESSING,
                        )

                def uninstaller():
                    with threading.Lock():
                        AnsiConsole.__virtualProcessing -= 1
                        if AnsiConsole.__virtualProcessing == 0:
                            Kernel32.SetConsoleMode(console, mode[0])

                width = kernel32_width
            elif (
                AnsiConsole.IS_CONEMU or AnsiConsole.IS_CYGWIN or AnsiConsole.IS_MSYSTEM
            ) and not is_console:
                processor = None
                type_ = AnsiType.Native
                installer = uninstaller = None
                mingw = MingwSupport()
                name = mingw.getConsoleName(stdout)
                if name:
                    width = lambda: mingw.getTerminalWidth(name)
                else:
                    width = lambda: -1
            else:
                try:
                    processor = WindowsAnsiProcessor(out, console)
                    type_ = AnsiType.Emulation
                except Exception:
                    processor = AnsiProcessor(out)
                    type_ = AnsiType.Unsupported
                installer = uninstaller = None
                width = kernel32_width
        else:
            processor = None
            type_ = AnsiType.Native
            installer = uninstaller = None

            def unix_width():
                sz = WinSize(0, 0)
                ioctl(fd, CLibrary.TIOCGWINSZ, sz)
                return sz.ws_col

            width = unix_width

        jansi_mode = sys.getProperty(
            AnsiConsole.JANSI_OUT_MODE if stdout else AnsiConsole.JANSI_ERR_MODE,
            sys.getProperty(AnsiConsole.JANSI_MODE),
        )
        if jansi_mode == AnsiConsole.JANSI_MODE_FORCE:
            mode = AnsiMode.Force
        elif jansi_mode == AnsiConsole.JANSI_MODE_STRIP:
            mode = AnsiMode.Strip
        elif jansi_mode:
            mode = AnsiMode.Default if isatty else AnsiMode.Strip
        elif AnsiConsole.getBoolean(AnsiConsole.JANSI_PASSTHROUGH):
            mode = AnsiMode.Force
        elif AnsiConsole.getBoolean(AnsiConsole.JANSI_STRIP):
            mode = AnsiMode.Strip
        elif AnsiConsole.getBoolean(AnsiConsole.JANSI_FORCE):
            mode = AnsiMode.Force
        else:
            mode = AnsiMode.Default if isatty else AnsiMode.Strip

        jansi_colors = sys.getProperty(
            AnsiConsole.JANSI_OUT_COLORS if stdout else AnsiConsole.JANSI_ERR_COLORS,
            sys.getProperty(AnsiConsole.JANSI_COLORS),
        )
        if jansi_colors == AnsiConsole.JANSI_COLORS_TRUECOLOR:
            colors = AnsiColors.TrueColor
        elif jansi_colors == AnsiConsole.JANSI_COLORS_256:
            colors = AnsiColors.Colors256
        elif jansi_colors:
            colors = AnsiColors.Colors16
        elif (colorterm := os.getenv("COLORTERM")) and (
            "truecolor" in colorterm or "24bit" in colorterm
        ):
            colors = AnsiColors.TrueColor
        elif (term := os.getenv("TERM")) and "-direct" in term:
            colors = AnsiColors.TrueColor
        elif term and "-256color" in term:
            colors = AnsiColors.Colors256
        else:
            colors = AnsiColors.Colors16

        reset_at_uninstall = (
            type_ != AnsiType.Unsupported
            and not AnsiConsole.getBoolean(AnsiConsole.JANSI_NORESET)
        )

        cs = "utf-8"
        if enc:
            try:
                cs = enc
            except Exception:
                pass

        return AnsiConsole.__newPrintStream(
            AnsiOutputStream(
                out,
                width,
                mode,
                processor,
                type_,
                colors,
                cs,
                installer,
                uninstaller,
                reset_at_uninstall,
            ),
            cs,
        )

    def __init__(self) -> None:
        raise NotImplementedError("This class cannot be instantiated.")


AnsiConsole.run_static_init()
