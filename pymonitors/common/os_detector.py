from platform import system

from .os_names import OSNames


class OSDetector():
    @staticmethod
    def __get_os_name() -> str:
        return system().lower()

    @staticmethod
    def is_macos() -> bool:
        return OSDetector.__get_os_name() == OSNames.MACOS.value

    @staticmethod
    def is_windows() -> bool:
        return OSDetector.__get_os_name() == OSNames.WINDOWS.value
