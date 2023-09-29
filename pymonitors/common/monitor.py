from typing import Any


class Monitor():
    def __init__(self, data: dict[str, int | bool]) -> None:
        self.__data: dict[str, int | bool] = data

    @property
    def data(self) -> dict[str, int | bool]:
        return self.__data

    @data.setter
    def data(self, _: Any) -> None:
        raise AttributeError("Read only property.")
