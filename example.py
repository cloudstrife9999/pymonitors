#!/usr/bin/env python3

from pymonitors import get_monitors


def main() -> None:
    print([m.data for m in get_monitors(print_info=False)])


if __name__ == "__main__":
    main()
