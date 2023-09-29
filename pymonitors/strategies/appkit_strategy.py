from typing import Any, Callable

from ..common.os_detector import OSDetector

if OSDetector.is_macos():
    from AppKit import NSScreen

from .strategy import Strategy
from ..common.monitor import Monitor


class AppKitStrategy(Strategy):
    def __init__(self, verbose: bool) -> None:
        super(AppKitStrategy, self).__init__(verbose=verbose)

    def run(self) -> None:
        try:
            if not OSDetector.is_macos():
                print(f"ERROR: {self.__class__.__name__} is only supported on macOS.")

                self.print_error_message()
            else:
                self.__look_for_monitors()
        except Exception:
            self.print_error_message()

    def __look_for_monitors(self) -> None:
        screens: list[Any] = NSScreen.screens()

        if not isinstance(screens, list):
            raise ValueError("Invalid raw data.")

        for screen in screens:
            data: dict[str, int | bool] = AppKitStrategy.__parse_screen(screen=screen)
            self.add_monitor(monitor=Monitor(data=data))

    @staticmethod
    def __parse_screen(screen: Any) -> dict[str, int | bool]:
        successfully_parsed: bool = False
        width: int = -1
        height: int = -1

        try:
            f: Callable[..., Any] | Any | None = screen.frame

            if not f:
                raise ValueError("Invalid raw data.")
            elif callable(f):
                data: Any = f()
            else:
                data: Any = f

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
