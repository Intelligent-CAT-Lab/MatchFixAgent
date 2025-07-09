from __future__ import annotations
import re
import os
import io


class OS:

    FAMILY_ZOS: str = "z/os"
    FAMILY_WINDOWS: str = "windows"
    FAMILY_VMS: str = "openvms"
    FAMILY_UNIX: str = "unix"
    FAMILY_TANDEM: str = "tandem"
    FAMILY_OS400: str = "os/400"
    FAMILY_OS2: str = "os/2"
    FAMILY_NT: str = "winnt"
    FAMILY_NETWARE: str = "netware"
    FAMILY_MAC: str = "mac"
    FAMILY_DOS: str = "dos"
    FAMILY_9X: str = "win9x"
    __PATH_SEP: str = os.pathsep
    __OS_VERSION: str = None
    __OS_ARCH: str = os.uname().machine.lower()
    __OS_NAME: str = os.name.lower()
    __DARWIN: str = "darwin"

    @staticmethod
    def initialize_fields() -> None:
        OS.__OS_VERSION: str = os.getenv("OS_VERSION", "").lower()

    @staticmethod
    def isVersion(version: str) -> bool:
        return OS.isOs(None, None, None, version)

    @staticmethod
    def isOs(family: str, name: str, arch: str, version: str) -> bool:
        ret_value = False
        if family or name or arch or version:
            is_family = True
            is_name = True
            is_arch = True
            is_version = True

            if family:
                is_windows = OS.__OS_NAME.find(OS.FAMILY_WINDOWS) != -1
                is_9x = False
                is_nt = False

                if is_windows:
                    is_9x = any(sub in OS.__OS_NAME for sub in ["95", "98", "me", "ce"])
                    is_nt = not is_9x

                if family == OS.FAMILY_WINDOWS:
                    is_family = is_windows
                elif family == OS.FAMILY_9X:
                    is_family = is_windows and is_9x
                elif family == OS.FAMILY_NT:
                    is_family = is_windows and is_nt
                elif family == OS.FAMILY_OS2:
                    is_family = OS.FAMILY_OS2 in OS.__OS_NAME
                elif family == OS.FAMILY_NETWARE:
                    is_family = OS.FAMILY_NETWARE in OS.__OS_NAME
                elif family == OS.FAMILY_DOS:
                    is_family = OS.__PATH_SEP == ";" and not OS.__isFamily(
                        OS.FAMILY_NETWARE
                    )
                elif family == OS.FAMILY_MAC:
                    is_family = (
                        OS.FAMILY_MAC in OS.__OS_NAME or OS.__DARWIN in OS.__OS_NAME
                    )
                elif family == OS.FAMILY_TANDEM:
                    is_family = "nonstop_kernel" in OS.__OS_NAME
                elif family == OS.FAMILY_UNIX:
                    is_family = (
                        OS.__PATH_SEP == ":"
                        and not OS.__isFamily(OS.FAMILY_VMS)
                        and (
                            not OS.__isFamily(OS.FAMILY_MAC)
                            or OS.__OS_NAME.endswith("x")
                            or OS.__DARWIN in OS.__OS_NAME
                        )
                    )
                elif family == OS.FAMILY_ZOS:
                    is_family = (
                        OS.FAMILY_ZOS in OS.__OS_NAME or "os/390" in OS.__OS_NAME
                    )
                elif family == OS.FAMILY_OS400:
                    is_family = OS.FAMILY_OS400 in OS.__OS_NAME
                elif family == OS.FAMILY_VMS:
                    is_family = OS.FAMILY_VMS in OS.__OS_NAME
                else:
                    raise ValueError(f'Don\'t know how to detect OS family "{family}"')

            if name:
                is_name = name == OS.__OS_NAME
            if arch:
                is_arch = arch == OS.__OS_ARCH
            if version:
                is_version = version == OS.__OS_VERSION

            ret_value = is_family and is_name and is_arch and is_version

        return ret_value

    @staticmethod
    def isName(name: str) -> bool:
        return OS.isOs(None, name, None, None)

    @staticmethod
    def isFamilyZOS() -> bool:
        return OS.__isFamily(OS.FAMILY_ZOS)

    @staticmethod
    def isFamilyWinNT() -> bool:
        return OS.__isFamily(OS.FAMILY_NT)

    @staticmethod
    def isFamilyWindows() -> bool:
        return OS.__isFamily(OS.FAMILY_WINDOWS)

    @staticmethod
    def isFamilyWin9x() -> bool:
        return OS.__isFamily(OS.FAMILY_9X)

    @staticmethod
    def isFamilyUnix() -> bool:
        return OS.__isFamily(OS.FAMILY_UNIX)

    @staticmethod
    def isFamilyTandem() -> bool:
        return OS.__isFamily(OS.FAMILY_TANDEM)

    @staticmethod
    def isFamilyOS400() -> bool:
        return OS.__isFamily(OS.FAMILY_OS400)

    @staticmethod
    def isFamilyOS2() -> bool:
        return OS.__isFamily(OS.FAMILY_OS2)

    @staticmethod
    def isFamilyOpenVms() -> bool:
        return OS.__isFamily(OS.FAMILY_VMS)

    @staticmethod
    def isFamilyNetware() -> bool:
        return OS.__isFamily(OS.FAMILY_NETWARE)

    @staticmethod
    def isFamilyMac() -> bool:
        return OS.__isFamily(OS.FAMILY_MAC)

    @staticmethod
    def isFamilyDOS() -> bool:
        return OS.__isFamily(OS.FAMILY_DOS)

    @staticmethod
    def isArch(arch: str) -> bool:
        return OS.isOs(None, None, arch, None)

    def __init__(self) -> None:
        raise NotImplementedError("This class cannot be instantiated")

    @staticmethod
    def __isFamily(family: str) -> bool:
        return OS.isOs(family, None, None, None)


OS.initialize_fields()
