from typing import Any
from subprocess import Popen, PIPE

from .strategy import Strategy, T
from ..common.os_detector import OSDetector


class WMICStrategy(Strategy):
    def __init__(self, verbose: bool) -> None:
        super(WMICStrategy, self).__init__(verbose=verbose)

    def run(self) -> None:
        try:
            if not OSDetector.is_windows():
                print(f"ERROR: {self.__class__.__name__} is only supported on Microsoft Windows.")

                self.print_error_message()

                return

            process: Popen[bytes] = Popen(["wmic", "PATH", "Win32_VideoController", "GET", "CurrentVerticalResolution,CurrentHorizontalResolution"], stdout=PIPE, stderr=PIPE)
            return_code: int = process.wait()

            if return_code != 0:
                self.print_error_message()
            else:
                output: tuple[bytes, bytes] = process.communicate()

                self.__parse_wmic_output(raw_data=output[0].decode("utf-8"))
        except Exception:
            self.print_error_message()

    def __parse_wmic_output(self, raw_data: str) -> None:
        # TODO: Implement this method.
        pass

    def parse_data(self, raw_data: Any) -> dict[str, T]:
        successfully_parsed: bool = False
        width: int = -1
        height: int = -1

        return {}
