# -*- coding: utf-8 -*-


"""setup.py: setuptools control."""


import re
from setuptools import setup


version = re.search(
    '^__version__\s*=\s*"(.*)"',
    open('minos/minos.py').read(),
    re.M
    ).group(1)


with open("README.rst", "rb") as f:
    long_descr = f.read().decode("utf-8")


setup(
    name = "cmdline-minos",
    packages = ["minos"],
    entry_points = {
        "console_scripts": ['minos = minos.minos:main']
        },
    version = version,
    description = "Framework for distributed backtracking searches.",
    long_description = long_descr,
    author = "Marcus Brinkmann",
    author_email = "marcus.brinkmann@ruhr-uni-bochum.de",
    url = "https://lambdafu.net",
    )
