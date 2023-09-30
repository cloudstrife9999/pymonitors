from typing import Any
from subprocess import Popen, PIPE

from .strategy import Strategy, T
from ..common.monitor import Monitor
from ..common.os_detector import OSDetector

import os


class MSWindowsStrategy(Strategy):
    def __init__(self, verbose: bool) -> None:
        super(MSWindowsStrategy, self).__init__(verbose=verbose)

    def run(self) -> None:
        try:
            if not OSDetector.is_windows():
                self.print_error_message(message=f"ERROR: {self.__class__.__name__} is only supported on Microsoft Windows.")
                self.print_error_message()

                return

            script_path: str = os.path.join(os.path.dirname(os.path.dirname(__file__)), "res", "script.ps1")
            process: Popen[bytes] = Popen(["powershell", "-ExecutionPolicy", "Bypass", script_path], stdout=PIPE, stderr=PIPE)
            return_code: int = process.wait()

            if return_code != 0:
                self.print_error_message()
            else:
                output: tuple[bytes, bytes] = process.communicate()

                data: dict[str, T] = self.parse_data(raw_data=output[0].decode("utf-8"))

                self.add_monitor(monitor=Monitor(data=data))
        except Exception:
            self.print_error_message()

    def parse_data(self, raw_data: Any) -> dict[str, T]:
        successfully_parsed: bool = False
        width: int = -1
        height: int = -1

        try:
            if not isinstance(raw_data, str):
                raise ValueError("Invalid raw data.")

            newline: str = "\n" if "\n" in raw_data else "\r"
            tokens: list[str] = raw_data.split(newline)
            width = int(tokens[0].replace("\n", "").replace("\r", ""))
            height = int(tokens[1].replace("\n", "").replace("\r", ""))
            successfully_parsed = True
        except Exception:
            successfully_parsed = False

        return {
            "width": width,
            "height": height,
            "successfully_parsed": successfully_parsed
        }
