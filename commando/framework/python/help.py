from commando.framework.python.logging import error
import sys

"""
This function should be overridden by the code sourcing it
It exists here to ensure something is able to answer a help request just in case.
"""
def help():
    # TODO: Call on support to reply to Slack.
    error(f'{sys.argv[0]} has not defined a help() function.')
