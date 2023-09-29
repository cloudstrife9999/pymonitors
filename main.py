#!/usr/bin/env python3

from pymonitors.strategies.xrandr_strategy import XrandrStrategy
from pymonitors.strategies.appkit_strategy import AppKitStrategy


def main() -> None:
    s: XrandrStrategy = XrandrStrategy(verbose=True)
    s.run()
    print([m.data for m in s.monitors])

    s2: AppKitStrategy = AppKitStrategy(verbose=True)
    s2.run()
    print([m.data for m in s2.monitors])


if __name__ == "__main__":
    main()
