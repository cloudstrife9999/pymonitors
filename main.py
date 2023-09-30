#!/usr/bin/env python3

from pymonitors.strategies.xrandr_strategy import XrandrStrategy
from pymonitors.strategies.appkit_strategy import AppKitStrategy
from pymonitors.strategies.mswindows_strategy import MSWindowsStrategy


def main() -> None:
    for S in [XrandrStrategy, AppKitStrategy, MSWindowsStrategy]:
        s = S(verbose=True)

        s.run()

        print([m.data for m in s.monitors])


if __name__ == "__main__":
    main()
