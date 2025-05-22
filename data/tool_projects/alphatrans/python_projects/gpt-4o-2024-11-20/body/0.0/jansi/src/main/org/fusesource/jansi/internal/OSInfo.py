from __future__ import annotations
import re
import sys
import pathlib
from io import StringIO
import io
from io import BytesIO
import typing
from typing import *
import os


class OSInfo:

    ARM64: str = "arm64"
    PPC64: str = "ppc64"
    PPC: str = "ppc"
    IA64: str = "ia64"
    IA64_32: str = "ia64_32"
    X86_64: str = "x86_64"
    X86: str = "x86"
    __archMapping: typing.Dict[str, str] = {}

    @staticmethod
    def run_static_init():
        # x86 mappings
        OSInfo.__archMapping[OSInfo.X86] = OSInfo.X86
        OSInfo.__archMapping["i386"] = OSInfo.X86
        OSInfo.__archMapping["i486"] = OSInfo.X86
        OSInfo.__archMapping["i586"] = OSInfo.X86
        OSInfo.__archMapping["i686"] = OSInfo.X86
        OSInfo.__archMapping["pentium"] = OSInfo.X86

        # x86_64 mappings
        OSInfo.__archMapping[OSInfo.X86_64] = OSInfo.X86_64
        OSInfo.__archMapping["amd64"] = OSInfo.X86_64
        OSInfo.__archMapping["em64t"] = OSInfo.X86_64
        OSInfo.__archMapping["universal"] = OSInfo.X86_64  # Needed for openjdk7 in Mac

        # Itanium 64-bit mappings
        OSInfo.__archMapping[OSInfo.IA64] = OSInfo.IA64
        OSInfo.__archMapping["ia64w"] = OSInfo.IA64

        # Itanium 32-bit mappings, usually an HP-UX construct
        OSInfo.__archMapping[OSInfo.IA64_32] = OSInfo.IA64_32
        OSInfo.__archMapping["ia64n"] = OSInfo.IA64_32

        # PowerPC mappings
        OSInfo.__archMapping[OSInfo.PPC] = OSInfo.PPC
        OSInfo.__archMapping["power"] = OSInfo.PPC
        OSInfo.__archMapping["powerpc"] = OSInfo.PPC
        OSInfo.__archMapping["power_pc"] = OSInfo.PPC
        OSInfo.__archMapping["power_rs"] = OSInfo.PPC

        # TODO: PowerPC 64-bit mappings
        OSInfo.__archMapping[OSInfo.PPC64] = OSInfo.PPC64
        OSInfo.__archMapping["power64"] = OSInfo.PPC64
        OSInfo.__archMapping["powerpc64"] = OSInfo.PPC64
        OSInfo.__archMapping["power_pc64"] = OSInfo.PPC64
        OSInfo.__archMapping["power_rs64"] = OSInfo.PPC64

        # aarch64 mappings
        OSInfo.__archMapping["aarch64"] = OSInfo.ARM64

    @staticmethod
    def translateArchNameToFolderName(archName: str) -> str:
        return "".join(char for char in archName if char.isalnum())

    @staticmethod
    def translateOSNameToFolderName(osName: str) -> str:
        if "Windows" in osName:
            return "Windows"
        elif "Mac" in osName or "Darwin" in osName:
            return "Mac"
            # elif isAlpine():  # Uncomment and implement if needed
            #     return "Linux-Alpine"
        elif "Linux" in osName:
            return "Linux"
        elif "AIX" in osName:
            return "AIX"
        else:
            return "".join(char for char in osName if char.isalnum())

    @staticmethod
    def getArchName() -> str:
        os_arch = os.getenv("os.arch", "")

        # For Android
        if OSInfo.isAndroid():
            return "android-arm"

        if os_arch.startswith("arm"):
            os_arch = OSInfo.resolveArmArchType()
        else:
            lc = os_arch.lower()
            if lc in OSInfo.__archMapping:
                return OSInfo.__archMapping[lc]

        return OSInfo.translateArchNameToFolderName(os_arch)

    @staticmethod
    def resolveArmArchType() -> str:
        if "Linux" in os.uname().sysname:
            armType = OSInfo.getHardwareName()
            # armType (uname -m) can be armv5t, armv5te, armv5tej, armv5tejl, armv6, armv7, armv7l, aarch64, i686
            if armType.startswith("armv6"):
                # Raspberry PI
                return "armv6"
            elif armType.startswith("armv7"):
                # Generic
                return "armv7"
            elif armType.startswith("armv5"):
                # Use armv5, soft-float ABI
                return "arm"
            elif armType == "aarch64":
                # Use arm64
                return "arm64"

            # Java 1.8 introduces a system property to determine armel or armhf
            # http://bugs.java.com/bugdatabase/view_bug.do?bug_id=8005545
            abi = os.getenv("sun.arch.abi")
            if abi is not None and abi.startswith("gnueabihf"):
                return "armv7"

        # Use armv5, soft-float ABI
        return "arm"

    @staticmethod
    def getHardwareName() -> str:
        try:
            process = os.popen("uname -m")
            try:
                output = process.read()
                return output.strip()
            finally:
                process.close()
        except Exception as e:
            print(f"Error while running uname -m: {e}")
            return "unknown"

    @staticmethod
    def isAlpine() -> bool:
        try:
            with open("/etc/os-release", "r") as file:
                for line in file:
                    if line.startswith("ID") and "alpine" in line.lower():
                        return True
        except Exception:
            pass

        return False

    @staticmethod
    def isAndroid() -> bool:
        return "android" in os.getenv("JAVA_RUNTIME_NAME", "").lower()

    @staticmethod
    def getOSName() -> str:
        return OSInfo.translateOSNameToFolderName(os.getenv("OS", os.uname().sysname))

    @staticmethod
    def getNativeLibFolderPathForCurrentOS() -> str:
        return OSInfo.getOSName() + "/" + OSInfo.getArchName()

    @staticmethod
    def main(args: typing.List[str]) -> None:
        if len(args) >= 1:
            if args[0] == "--os":
                print(OSInfo.getOSName(), end="")
                return
            elif args[0] == "--arch":
                print(OSInfo.getArchName(), end="")
                return

        print(OSInfo.getNativeLibFolderPathForCurrentOS(), end="")

    @staticmethod
    def __readFully(
        in_: typing.Union[io.BytesIO, io.StringIO, io.BufferedReader],
    ) -> str:
        read_len = 0
        b = io.BytesIO()
        buf = bytearray(32)
        while (read_len := in_.readinto(buf)) > 0:
            b.write(buf[:read_len])
        return b.getvalue().decode()


OSInfo.run_static_init()
