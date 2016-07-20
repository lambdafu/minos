# -*- coding: utf-8 -*-


"""minos.minos: provides entry point main()."""


__version__ = "0.0.1"


import sys


def main():
    print("Executing minos version %s." % __version__)
    print("List of argument strings: %s" % sys.argv[1:])
