from subprocess import Popen, PIPE
from typing import Any

from .strategy import Strategy, T
from ..common.monitor import Monitor


class XrandrStrategy(Strategy):
    def __init__(self, verbose: bool) -> None:
        super(XrandrStrategy, self).__init__(verbose=verbose)

    def run(self) -> None:
        try:
            process: Popen[bytes] = Popen(["xrandr"], stdout=PIPE, stderr=PIPE)
            return_code: int = process.wait()

            if return_code != 0:
                self.print_error_message()
            else:
                output: tuple[bytes, bytes] = process.communicate()

                self.__parse_xrandr_output(raw_data=output[0].decode("utf-8"))
        except Exception:
            self.print_error_message()

    def __parse_xrandr_output(self, raw_data: str) -> None:
        process: Popen[bytes] = Popen[bytes](["grep", "Screen"], stdin=PIPE, stdout=PIPE, stderr=PIPE)
        output: tuple[bytes, bytes] = process.communicate(input=raw_data.encode("utf-8"))

        return_code: int = process.wait()

        if return_code != 0:
            self.print_error_message()
        else:
            raw_lines: list[str] = output[0].decode("utf-8").split("\n")[0:-1]

            self.__add_monitors(raw_lines=raw_lines)

    def __add_monitors(self, raw_lines: list[str]) -> None:
        for raw_line in raw_lines:
            data: dict[str, T] = self.parse_data(raw_data=raw_line)

            self.add_monitor(monitor=Monitor(data=data))

    def parse_data(self, raw_data: Any) -> dict[str, T]:
        successfully_parsed: bool = False
        width: int = -1
        height: int = -1

        try:
            if not isinstance(raw_data, str):
                raise ValueError("Invalid raw data.")

            tokens: list[str] = raw_data.split(" ")

            if "current" not in tokens:
                raise ValueError("Invalid raw data.")

            width = int(tokens[tokens.index("current") + 1].replace(",", ""))
            height = int(tokens[tokens.index("current") + 3].replace(",", ""))

            successfully_parsed = True
        except Exception:
            successfully_parsed = False

        return {"width": width, "height": height, "successfully_parsed": successfully_parsed}
