from __future__ import annotations
import re
import sys
import enum
import pathlib
import io
import typing
from typing import *
import os
from src.main.org.fusesource.jansi.Ansi import *
from src.main.org.fusesource.jansi.AnsiColors import *
from src.main.org.fusesource.jansi.AnsiConsole import *
from src.main.org.fusesource.jansi.AnsiMode import *
from src.main.org.fusesource.jansi.AnsiPrintStream import *
from src.main.org.fusesource.jansi.AnsiType import *
from src.main.org.fusesource.jansi.internal.CLibrary import *
from src.main.org.fusesource.jansi.internal.JansiLoader import *
from src.main.org.fusesource.jansi.internal.Kernel32 import *
from src.main.org.fusesource.jansi.internal.MingwSupport import *


class AnsiMain:

    @staticmethod
    def main(args: typing.List[str]) -> None:
        print(f"Jansi {AnsiMain.__getJansiVersion()}")

        print()

        # Info on native library
        print(f"library.jansi.path= {os.getenv('library.jansi.path', '')}")
        print(f"library.jansi.version= {os.getenv('library.jansi.version', '')}")
        loaded = JansiLoader.initialize()
        if loaded:
            print(
                f"Jansi native library loaded from {JansiLoader.getNativeLibraryPath()}"
            )
            if JansiLoader.getNativeLibrarySourceUrl() is not None:
                print(
                    f"   which was auto-extracted from {JansiLoader.getNativeLibrarySourceUrl()}"
                )
        else:
            prev = os.getenv(AnsiConsole.JANSI_GRACEFUL)
            try:
                os.environ[AnsiConsole.JANSI_GRACEFUL] = "false"
                JansiLoader.initialize()
            except Exception as e:
                print(e, file=sys.stdout)
            finally:
                if prev is not None:
                    os.environ[AnsiConsole.JANSI_GRACEFUL] = prev
                else:
                    os.environ.pop(AnsiConsole.JANSI_GRACEFUL, None)

        print()

        print(
            f"os.name= {os.name}, os.version= {os.getenv('os.version', '')}, os.arch= {os.getenv('os.arch', '')}"
        )
        print(f"file.encoding= {os.getenv('file.encoding', '')}")
        print(
            f"sun.stdout.encoding= {os.getenv('sun.stdout.encoding', '')}, sun.stderr.encoding= {os.getenv('sun.stderr.encoding', '')}"
        )
        print(
            f"stdout.encoding= {os.getenv('stdout.encoding', '')}, stderr.encoding= {os.getenv('stderr.encoding', '')}"
        )
        print(
            f"java.version= {os.getenv('java.version', '')}, java.vendor= {os.getenv('java.vendor', '')}, java.home= {os.getenv('java.home', '')}"
        )
        print(f"Console: {sys.stdout.isatty()}")

        print()

        print(
            f"{AnsiConsole.JANSI_GRACEFUL}= {os.getenv(AnsiConsole.JANSI_GRACEFUL, '')}"
        )
        print(f"{AnsiConsole.JANSI_MODE}= {os.getenv(AnsiConsole.JANSI_MODE, '')}")
        print(
            f"{AnsiConsole.JANSI_OUT_MODE}= {os.getenv(AnsiConsole.JANSI_OUT_MODE, '')}"
        )
        print(
            f"{AnsiConsole.JANSI_ERR_MODE}= {os.getenv(AnsiConsole.JANSI_ERR_MODE, '')}"
        )
        print(f"{AnsiConsole.JANSI_COLORS}= {os.getenv(AnsiConsole.JANSI_COLORS, '')}")
        print(
            f"{AnsiConsole.JANSI_OUT_COLORS}= {os.getenv(AnsiConsole.JANSI_OUT_COLORS, '')}"
        )
        print(
            f"{AnsiConsole.JANSI_ERR_COLORS}= {os.getenv(AnsiConsole.JANSI_ERR_COLORS, '')}"
        )
        print(
            f"{AnsiConsole.JANSI_PASSTHROUGH}= {JansiLoader.getBoolean(AnsiConsole.JANSI_PASSTHROUGH)}"
        )
        print(
            f"{AnsiConsole.JANSI_STRIP}= {JansiLoader.getBoolean(AnsiConsole.JANSI_STRIP)}"
        )
        print(
            f"{AnsiConsole.JANSI_FORCE}= {JansiLoader.getBoolean(AnsiConsole.JANSI_FORCE)}"
        )
        print(
            f"{AnsiConsole.JANSI_NORESET}= {JansiLoader.getBoolean(AnsiConsole.JANSI_NORESET)}"
        )
        print(f"{Ansi.DISABLE}= {JansiLoader.getBoolean(Ansi.DISABLE)}")

        print()

        print(f"IS_WINDOWS: {AnsiConsole.IS_WINDOWS}")
        if AnsiConsole.IS_WINDOWS:
            print(f"IS_CONEMU: {AnsiConsole.IS_CONEMU}")
            print(f"IS_CYGWIN: {AnsiConsole.IS_CYGWIN}")
            print(f"IS_MSYSTEM: {AnsiConsole.IS_MSYSTEM}")

        print()

        AnsiMain.__diagnoseTty(False)  # System.out
        AnsiMain.__diagnoseTty(True)  # System.err

        AnsiConsole.systemInstall()

        print()

        print("Resulting Jansi modes for stout/stderr streams:")
        print(f"  - System.out: {AnsiConsole.out().toString()}")
        print(f"  - System.err: {AnsiConsole.err().toString()}")
        print("Processor types description:")
        for type_ in AnsiType.values():
            print(f"  - {type_}: {type_.getDescription()}")
        print("Colors support description:")
        for colors in AnsiColors.values():
            print(f"  - {colors}: {colors.getDescription()}")
        print("Modes description:")
        for mode in AnsiMode.values():
            print(f"  - {mode}: {mode.getDescription()}")

        try:
            print()

            AnsiMain.__testAnsi(False)
            AnsiMain.__testAnsi(True)

            if len(args) == 0:
                AnsiMain.__printJansiLogoDemo()
                return

            print()

            if len(args) == 1:
                f = pathlib.Path(args[0])
                if f.exists():
                    # Write file content
                    print(
                        AnsiPrintStream.ansi0()
                        .bold()
                        .a1(f'"{args[0]}" content:')
                        .reset()
                    )
                    AnsiMain.__writeFileContent(f)
                    return

            # Write args without Jansi then with Jansi AnsiConsole
            print(AnsiPrintStream.ansi0().bold().a1("original args:").reset())
            for i, arg in enumerate(args, start=1):
                AnsiConsole.system_out.write(f"{i}: ")
                AnsiConsole.system_out.write(f"{arg}\n")

            print(AnsiPrintStream.ansi0().bold().a1("Jansi filtered args:").reset())
            for i, arg in enumerate(args, start=1):
                print(f"{i}: {arg}")
        finally:
            AnsiConsole.systemUninstall()

    @staticmethod
    def __closeQuietly(c: Closeable) -> None:
        try:
            c.close()
        except IOError as ioe:
            print(ioe, file=AnsiConsole.err)

    @staticmethod
    def __writeFileContent(f: pathlib.Path) -> None:
        try:
            with f.open("rb") as in_file:  # Open the file in binary read mode
                buf = bytearray(1024)  # Create a buffer of size 1024 bytes
                while True:
                    l = in_file.readinto(buf)  # Read into the buffer
                    if l == 0:  # If no more data is read, break the loop
                        break
                    os.write(1, buf[:l])  # Write the buffer content to stdout
        except IOError as ioe:
            print(ioe, file=AnsiConsole.err)

    @staticmethod
    def __printJansiLogoDemo() -> None:
        try:
            with open(
                pathlib.Path(__file__).parent / "jansi.txt", encoding="utf-8"
            ) as in_file:
                for line in in_file:
                    print(line, end="")
        except IOError as e:
            print(e, file=AnsiConsole.err)

    @staticmethod
    def __getPomPropertiesVersion(path: str) -> str:
        resource_path = f"/META-INF/maven/{path}/pom.properties"
        in_stream = AnsiMain.__getResourceAsStream(resource_path)
        if in_stream is None:
            return None
        try:
            properties = {}
            for line in in_stream.read().decode("utf-8").splitlines():
                if "=" in line:
                    key, value = line.split("=", 1)
                    properties[key.strip()] = value.strip()
            return properties.get("version")
        finally:
            AnsiMain.__closeQuietly(in_stream)

    @staticmethod
    def __testAnsi(stderr: bool) -> None:
        s = AnsiConsole.err if stderr else AnsiConsole.out
        s.write(f"test on System.{'err' if stderr else 'out'}:")
        for c in Ansi.Color.values():
            s.write(f" {Ansi.ansi0().fg0(c)}{c}{Ansi.ansi0().reset()}")
        s.write("\n")
        s.write("            bright:")
        for c in Ansi.Color.values():
            s.write(f" {Ansi.ansi0().fgBright(c)}{c}{Ansi.ansi0().reset()}")
        s.write("\n")
        s.write("              bold:")
        for c in Ansi.Color.values():
            s.write(f" {Ansi.ansi0().bold().fg0(c)}{c}{Ansi.ansi0().reset()}")
        s.write("\n")
        s.write("             faint:")
        for c in Ansi.Color.values():
            s.write(
                f" {Ansi.ansi0().a0(Attribute.INTENSITY_FAINT).fg0(c)}{c}{Ansi.ansi0().reset()}"
            )
        s.write("\n")
        s.write("        bold+faint:")
        for c in Ansi.Color.values():
            s.write(
                f" {Ansi.ansi0().bold().a0(Attribute.INTENSITY_FAINT).fg0(c)}{c}{Ansi.ansi0().reset()}"
            )
        s.write("\n")

        ansi = Ansi.ansi0()
        ansi.a1("        256 colors: ")
        for i in range(6 * 6 * 6):
            if i > 0 and i % 36 == 0:
                ansi.reset()
                ansi.newline()
                ansi.a1("                    ")
            elif i > 0 and i % 6 == 0:
                ansi.reset()
                ansi.a1("  ")
            a0 = i % 6
            a1 = (i // 6) % 6
            a2 = i // 36
            ansi.bg1(16 + a0 + a2 * 6 + a1 * 36).a3(" ")
        ansi.reset()
        s.write(str(ansi) + "\n")

        ansi = Ansi.ansi0()
        ansi.a1("         truecolor: ")
        for i in range(256):
            if i > 0 and i % 48 == 0:
                ansi.reset()
                ansi.newline()
                ansi.a1("                    ")
            r = 255 - i
            g = 255 - 2 * i if i * 2 > 255 else 2 * i
            b = i
            ansi.bgRgb1(r, g, b).fgRgb1(255 - r, 255 - g, 255 - b).a3(
                "/" if i % 2 == 0 else "\\"
            )
        ansi.reset()
        s.write(str(ansi) + "\n")

    @staticmethod
    def __diagnoseTty(stderr: bool) -> None:
        isatty = 0
        width = 0

        if AnsiConsole.IS_WINDOWS:
            console = Kernel32.GetStdHandle(
                Kernel32.STD_ERROR_HANDLE if stderr else Kernel32.STD_OUTPUT_HANDLE
            )
            mode = [0]
            isatty = Kernel32.GetConsoleMode(console, mode)

            if (
                AnsiConsole.IS_CONEMU or AnsiConsole.IS_CYGWIN or AnsiConsole.IS_MSYSTEM
            ) and isatty == 0:
                mingw = MingwSupport()
                name = mingw.getConsoleName(not stderr)
                if name and name.strip():
                    isatty = 1
                    width = mingw.getTerminalWidth(name)
                else:
                    isatty = 0
                    width = 0
            else:
                info = CONSOLE_SCREEN_BUFFER_INFO()
                Kernel32.GetConsoleScreenBufferInfo(console, info)
                width = info.windowWidth()
        else:
            fd = CLibrary.STDERR_FILENO if stderr else CLibrary.STDOUT_FILENO
            isatty = CLibrary.isatty(fd) if CLibrary.LOADED else 0
            ws = WinSize(0, 0)
            CLibrary.ioctl(fd, CLibrary.TIOCGWINSZ, ws)
            width = ws.ws_col

        print(
            f"isatty(STD{'ERR' if stderr else 'OUT'}_FILENO): {isatty}, System."
            f"{'err' if stderr else 'out'} {'is *NOT*' if isatty == 0 else 'is'} a terminal"
        )
        print(f"width(STD{'ERR' if stderr else 'OUT'}_FILENO): {width}")

    @staticmethod
    def __getJansiVersion() -> str:
        package = AnsiMain.__module__
        return None if package is None else getattr(package, "__version__", None)
