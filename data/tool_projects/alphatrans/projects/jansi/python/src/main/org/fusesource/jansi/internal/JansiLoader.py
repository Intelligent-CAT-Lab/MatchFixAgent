from __future__ import annotations
import time
import copy
import re
import uuid
import sys
import threading
import pathlib
from io import StringIO
import io
from io import BytesIO
import typing
from typing import *
from src.main.org.fusesource.jansi.AnsiConsole import *
from src.main.org.fusesource.jansi.internal.OSInfo import *


class JansiLoader:

    __nativeLibrarySourceUrl: str = ""

    __nativeLibraryPath: str = ""

    __loaded: bool = False

    @staticmethod
    def getVersion() -> str:
        version_file = (
            pathlib.Path(__file__).parent / "org/fusesource/jansi/jansi.properties"
        )
        version = "unknown"
        try:
            if version_file.exists():
                with version_file.open("r", encoding="utf-8") as file:
                    version_data = {}
                    for line in file:
                        if "=" in line:
                            key, value = line.split("=", 1)
                            version_data[key.strip()] = value.strip()
                    version = version_data.get("version", version)
                    version = "".join(c for c in version if c.isdigit() or c == ".")
        except Exception as e:
            print(e, file=sys.stderr)
        return version

    @staticmethod
    def getMinorVersion() -> int:
        c = JansiLoader.getVersion().split(".")
        return int(c[1]) if len(c) > 1 else 0

    @staticmethod
    def getMajorVersion() -> int:
        c = JansiLoader.getVersion().split(".")
        return int(c[0]) if len(c) > 0 else 1

    @staticmethod
    def cleanup() -> None:
        temp_folder = JansiLoader.__getTempDir().absolute()
        dir_path = temp_folder

        search_pattern = f"jansi-{JansiLoader.__getVersion()}"
        native_lib_files = [
            file
            for file in dir_path.iterdir()
            if file.is_file()
            and file.name.startswith(search_pattern)
            and not file.name.endswith(".lck")
        ]

        for native_lib_file in native_lib_files:
            lck_file = native_lib_file.with_suffix(native_lib_file.suffix + ".lck")
            if not lck_file.exists():
                try:
                    native_lib_file.unlink()
                except PermissionError as e:
                    print(f"Failed to delete old native lib: {e}")

    @staticmethod
    def getNativeLibrarySourceUrl() -> str:
        return JansiLoader.__nativeLibrarySourceUrl

    @staticmethod
    def getNativeLibraryPath() -> str:
        return JansiLoader.__nativeLibraryPath

    @staticmethod
    def initialize() -> bool:
        # only cleanup before the first extract
        if not JansiLoader.__loaded:
            cleanup = threading.Thread(target=JansiLoader.cleanup, name="cleanup")
            cleanup.setDaemon(True)
            cleanup.setPriority(
                threading.MIN_PRIORITY
            )  # Note: Python does not have setPriority, so this line may need adjustment
            cleanup.start()

        try:
            JansiLoader.__loadJansiNativeLibrary()
        except Exception as e:
            if not bool(
                os.getenv(AnsiConsole.JANSI_GRACEFUL, "true").lower() in ["true", "1"]
            ):
                raise RuntimeError(
                    "Unable to load jansi native library. You may want to set the `jansi.graceful` system property to true to be able to use Jansi on your platform"
                ) from e

        return JansiLoader.__loaded

    @staticmethod
    def __hasResource(path: str) -> bool:
        return pathlib.Path(path).exists()

    @staticmethod
    def __loadJansiNativeLibrary() -> None:
        if JansiLoader.__loaded:
            return

        tried_paths = []

        # Try loading library from library.jansi.path property
        jansi_native_library_path = os.getenv("library.jansi.path")
        jansi_native_library_name = os.getenv("library.jansi.name")
        if jansi_native_library_name is None:
            jansi_native_library_name = ctypes.util.find_library("jansi")
            if (
                jansi_native_library_name is not None
                and jansi_native_library_name.endswith(".dylib")
            ):
                jansi_native_library_name = jansi_native_library_name.replace(
                    ".dylib", ".jnilib"
                )

        if jansi_native_library_path:
            with_os = f"{jansi_native_library_path}/{OSInfo.getNativeLibFolderPathForCurrentOS()}"
            if JansiLoader.__loadNativeLibrary(
                pathlib.Path(with_os) / jansi_native_library_name
            ):
                JansiLoader.__loaded = True
                return
            else:
                tried_paths.append(with_os)

            if JansiLoader.__loadNativeLibrary(
                pathlib.Path(jansi_native_library_path) / jansi_native_library_name
            ):
                JansiLoader.__loaded = True
                return
            else:
                tried_paths.append(jansi_native_library_path)

        # Load the OS-dependent library from the jar file
        package_path = JansiLoader.__module__.replace(".", "/")
        jansi_native_library_path = (
            f"/{package_path}/native/{OSInfo.getNativeLibFolderPathForCurrentOS()}"
        )
        has_native_lib = JansiLoader.__hasResource(
            f"{jansi_native_library_path}/{jansi_native_library_name}"
        )

        if has_native_lib:
            temp_folder = JansiLoader.__getTempDir()
            if JansiLoader.__extractAndLoadLibraryFile(
                jansi_native_library_path, jansi_native_library_name, str(temp_folder)
            ):
                JansiLoader.__loaded = True
                return
            else:
                tried_paths.append(jansi_native_library_path)

        # As a last resort, try from java.library.path
        java_library_path = os.getenv("java.library.path", "")
        for ld_path in java_library_path.split(os.pathsep):
            if not ld_path:
                continue
            if JansiLoader.__loadNativeLibrary(
                pathlib.Path(ld_path) / jansi_native_library_name
            ):
                JansiLoader.__loaded = True
                return
            else:
                tried_paths.append(ld_path)

        raise Exception(
            f"No native library found for os.name={OSInfo.getOSName()}, os.arch={OSInfo.getArchName()}, "
            f"paths=[{os.pathsep.join(tried_paths)}]"
        )

    @staticmethod
    def __loadNativeLibrary(libPath: pathlib.Path) -> bool:
        if libPath.exists():
            try:
                path = str(libPath.resolve())
                import ctypes

                ctypes.CDLL(path)  # Load the native library
                JansiLoader.__nativeLibraryPath = path
                return True
            except OSError as e:  # Equivalent to UnsatisfiedLinkError in Java
                if not os.access(libPath, os.X_OK):  # Check if the file is executable
                    print(
                        f"Failed to load native library: {libPath.name}. The native library file at {libPath} is not executable, "
                        f"make sure that the directory is mounted on a partition without the noexec flag, or set the "
                        f"jansi.tmpdir system property to point to a proper location. osinfo: {OSInfo.getNativeLibFolderPathForCurrentOS()}"
                    )
                else:
                    print(
                        f"Failed to load native library: {libPath.name}. osinfo: {OSInfo.getNativeLibFolderPathForCurrentOS()}"
                    )
                print(e)
                return False
        else:
            return False

    @staticmethod
    def __randomUUID() -> str:
        import random

        return hex(random.getrandbits(64))[2:]

    @staticmethod
    def __extractAndLoadLibraryFile(
        libFolderForCurrentOS: str, libraryFileName: str, targetFolder: str
    ) -> bool:
        import os
        import shutil
        from pathlib import Path

        nativeLibraryFilePath = f"{libFolderForCurrentOS}/{libraryFileName}"
        uuid = JansiLoader.__randomUUID()
        extractedLibFileName = (
            f"jansi-{JansiLoader.getVersion()}-{uuid}-{libraryFileName}"
        )
        extractedLckFileName = f"{extractedLibFileName}.lck"

        extractedLibFile = Path(targetFolder) / extractedLibFileName
        extractedLckFile = Path(targetFolder) / extractedLckFileName

        try:
            # Extract a native library file into the target directory
            resource_stream = JansiLoader.__getResourceAsStream(nativeLibraryFilePath)
            if resource_stream is None:
                raise FileNotFoundError(f"Resource {nativeLibraryFilePath} not found")

            if not extractedLckFile.exists():
                extractedLckFile.touch()

            with resource_stream as in_stream, extractedLibFile.open(
                "wb"
            ) as out_stream:
                shutil.copyfileobj(in_stream, out_stream)

            # Ensure the files are deleted on exit
            extractedLibFile.unlink(missing_ok=True)
            extractedLckFile.unlink(missing_ok=True)

            # Set executable (x) flag to enable loading the native library
            extractedLibFile.chmod(0o755)

            # Check whether the contents are properly copied from the resource folder
            with JansiLoader.__getResourceAsStream(
                nativeLibraryFilePath
            ) as nativeIn, extractedLibFile.open("rb") as extractedLibIn:
                eq = JansiLoader.__contentsEquals(nativeIn, extractedLibIn)
                if eq is not None:
                    raise RuntimeError(
                        f"Failed to write a native library file at {extractedLibFile} because {eq}"
                    )

            # Load library
            if JansiLoader.__loadNativeLibrary(extractedLibFile):
                JansiLoader.__nativeLibrarySourceUrl = JansiLoader.__getResource(
                    nativeLibraryFilePath
                ).geturl()
                return True

        except Exception as e:
            print(e, file=sys.stderr)

        return False

    @staticmethod
    def __contentsEquals(
        in1: typing.Union[io.BytesIO, io.StringIO, io.BufferedReader],
        in2: typing.Union[io.BytesIO, io.StringIO, io.BufferedReader],
    ) -> str:
        buffer1 = bytearray(8192)
        buffer2 = bytearray(8192)

        while True:
            numRead1 = JansiLoader.__readNBytes(in1, buffer1)
            numRead2 = JansiLoader.__readNBytes(in2, buffer2)

            if numRead1 > 0:
                if numRead2 <= 0:
                    return "EOF on second stream but not first"
                if numRead2 != numRead1:
                    return f"Read size different ({numRead1} vs {numRead2})"
                # Otherwise same number of bytes read
                if buffer1[:numRead1] != buffer2[:numRead2]:
                    return "Content differs"
                # Otherwise same bytes read, so continue ...
            else:
                # Nothing more in stream 1 ...
                if numRead2 > 0:
                    return "EOF on first stream but not second"
                else:
                    return None

    @staticmethod
    def __readNBytes(
        in_: typing.Union[io.BytesIO, io.StringIO, io.BufferedReader],
        b: typing.List[int],
    ) -> int:
        n = 0
        length = len(b)
        while n < length:
            count = in_.readinto(memoryview(b)[n:])
            if count <= 0:
                break
            n += count
        return n

    @staticmethod
    def __getTempDir() -> pathlib.Path:
        jansi_tmpdir = os.getenv("jansi.tmpdir")
        java_tmpdir = os.getenv("java.io.tmpdir")
        temp_dir = jansi_tmpdir if jansi_tmpdir is not None else java_tmpdir
        return pathlib.Path(temp_dir)
