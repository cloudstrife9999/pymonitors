from typing import Any, TypeAlias

from ..common.monitor import Monitor


T: TypeAlias = int | bool


class Strategy():
    def __init__(self, verbose: bool) -> None:
        self.__verbose: bool = verbose
        self.__monitors: list[Monitor] = []

    def run(self) -> None:
        # This method must be implemented by subclasses.
        raise NotImplementedError()

    def parse_data(self, raw_data: Any) -> dict[str, T]:
        # This method must be implemented by subclasses.
        raise NotImplementedError()

    def add_monitor(self, monitor: Monitor) -> None:
        self.__monitors.append(monitor)

    def print_error_message(self, message: str="") -> None:
        if not self.__verbose:
            return

        if not message:
            message = f"INFO: {self.__class__.__name__} failed to identify a monitor."

        print(message)

    @property
    def monitors(self) -> list[Monitor]:
        return self.__monitors

    @monitors.setter
    def monitors(self, _: Any) -> None:
        raise AttributeError("Read only property.")

    @property
    def verbose(self) -> bool:
        return self.__verbose

    @verbose.setter
    def verbose(self, _: Any) -> None:
        raise AttributeError("Read only property.")
