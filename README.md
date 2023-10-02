# PyMonitors

A Python library to programatically get your monitor's resolution info.

It supports multiple strategies:

- `xrandr`: Linux only, requires `x11-xserver-utils` to be installed.
- `appkit`: MacOS only, requires `pyobjc`, `AppKit`, and `cairo` to be installed.
- `mswindows`: Windows only, requires the Powershell to be installed.

## Usage

```python
from pymonitors import get_monitors


for monitor in get_monitors():
    width: int = monitor.width
    height: int = monitor.height

    print(f"Monitor {monitor.name} has resolution {width}x{height}.")
```
