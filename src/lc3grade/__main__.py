"""Run the lc3grade command-line interface"""

import sys
from .cli import main

# The Python zip binary generated by the Makefile will put the output of
# `git describe' into the VERSION global, so use it if we can
try:
    VERSION
except NameError:
    VERSION = None

main(sys.argv, version=VERSION)