from typing import Any

from ..common.monitor import Monitor


class Strategy():
    def __init__(self, verbose: bool) -> None:
        self.__verbose: bool = verbose
        self.__monitors: list[Monitor] = []

    def run(self) -> None:
        # This method must be implemented by subclasses.
        raise NotImplementedError()

    def parse_data(self, raw_data: str) -> dict[str, int | bool]:
        # This method must be implemented by subclasses.
        raise NotImplementedError()

    def add_monitor(self, monitor: Monitor) -> None:
        self.__monitors.append(monitor)

    def print_error_message(self) -> None:
        if self.__verbose:
            print(f"INFO: {self.__class__.__name__} failed to identify a monitor.")

    @property
    def monitors(self) -> list[Monitor]:
        return self.__monitors

    @monitors.setter
    def monitors(self, _: Any) -> None:
        raise AttributeError("Read only property.")
