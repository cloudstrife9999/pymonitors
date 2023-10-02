#!/bin/bash

/usr/bin/env python setup.py sdist bdist_wheel
/usr/bin/env python -m twine upload dist/* -r pymonitors --skip-existing
