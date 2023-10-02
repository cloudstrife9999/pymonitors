from typing import Any, Callable, TypeAlias, Iterable
from pyoptional.pyoptional import PyOptional

from ..common.os_detector import OSDetector


if OSDetector.is_macos():
    from AppKit import NSScreen

from .strategy import Strategy, T
from ..common.monitor import Monitor


F: TypeAlias = Callable[..., Any] | Any | None


class AppKitStrategy(Strategy):
    def __init__(self, verbose: bool) -> None:
        super(AppKitStrategy, self).__init__(verbose=verbose)

    def run(self) -> None:
        try:
            if not OSDetector.is_macos():
                self.print_error_message(f"ERROR: {self.__class__.__name__} is only supported on macOS.")
                self.print_error_message()
            else:
                self.__look_for_monitors()
        except Exception:
            self.print_error_message()

    def __look_for_monitors(self) -> None:
        screens: list[Any] = NSScreen.screens()

        if not isinstance(screens, Iterable):
            raise ValueError("Invalid raw data.")

        for screen in screens:
            data: dict[str, T] = self.parse_data(raw_data=screen)

            if data["successfully_parsed"]:
                self.add_monitor(monitor=Monitor(data=data))

    def parse_data(self, raw_data: Any) -> dict[str, T]:
        successfully_parsed: bool = False
        width: int = -1
        height: int = -1

        try:
            f: PyOptional[F] = PyOptional[F].of_nullable(raw_data.frame)

            if f.is_empty():
                raise ValueError("Invalid raw data.")
            else:
                unwrapped: F = f.or_else_raise()
                data: Any = unwrapped() if callable(unwrapped) else unwrapped

            width = int(data.size.width)
            height = int(data.size.height)
            successfully_parsed = True
        except Exception:
            successfully_parsed = False

        return {
            "width": width,
            "height": height,
            "successfully_parsed": successfully_parsed
        }
