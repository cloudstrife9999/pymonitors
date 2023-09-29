from enum import Enum


class OSNames(Enum):
    LINUX = "linux"
    MACOS = "darwin"
    WINDOWS = "windows"
    SOLARIS = "sunos"
    FREEBSD = "freebsd"
    OPENBSD = "openbsd"
    NETBSD = "netbsd"
    UNKNOWN = "unknown"
