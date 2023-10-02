from setuptools import setup, find_packages

from pymonitors.common.os_detector import OSDetector


# All reusable metadata should go here.

name: str = "pymonitors"
description: str = "PyMonitors: a Python library to obtain info about available screens (monitors)."

with open("README.md", "r") as f:
    long_description = f.read()

author: str = "Emanuele Uliana"
author_email: str = "vw@dicelab-rhul.org"
license: str = "GNU3"
classifiers: list[str] = [
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.10",
    "Programming Language :: Python :: 3.11",
    "Programming Language :: Python :: 3 :: Only",
    "Development Status :: 4 - Beta",
    "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    "Operating System :: OS Independent",
]

dependencies: list[str] = ["wheel", "pyjoptional>=1.1.0"]

if OSDetector.is_macos():
    dependencies += ["AppKit", "pyobjc"]

# End of metadata

setup(
    name=name,
    version="1.0.1",
    description=description,
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/cloudstrife9999/pymonitors",
    author=author,
    author_email=author_email,
    license=license,
    packages=find_packages(),
    include_package_data=True,
    install_requires=dependencies,
    classifiers=classifiers
)
