# Support for logging to stdout and stderr.

import sys

# TODO: Add more structure (JSON), including timestamps!

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
