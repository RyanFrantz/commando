# Support for logging to stdout and stderr.

import sys

"""
Log a message to stdout.
"""
def info(msg: str):
    print(msg)

"""
Log a message to stderr.
"""
def error(msg: str):
    print(msg, file=sys.stderr)
