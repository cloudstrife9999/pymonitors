from .common.monitor import Monitor
from .common.strategies_map import get_strategies


def get_monitors(print_info: bool) -> list[Monitor]:
    monitors: list[Monitor] = []

    for S in get_strategies().values():
        s = S(verbose=print_info)

        s.run()

        monitors.extend(s.monitors)

    return monitors
