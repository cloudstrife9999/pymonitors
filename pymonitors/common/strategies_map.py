from typing import Type

from .strategies import Strategies
from ..strategies.xrandr_strategy import XrandrStrategy
from ..strategies.appkit_strategy import AppKitStrategy
from ..strategies.mswindows_strategy import MSWindowsStrategy
from ..strategies.strategy import Strategy


def get_strategies() -> dict[Strategies, Type[Strategy]]:
    return {
        Strategies.XRANDR: XrandrStrategy,
        Strategies.APPKIT: AppKitStrategy,
        Strategies.MSWINDOWS: MSWindowsStrategy
    }
