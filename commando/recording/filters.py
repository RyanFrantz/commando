import logging, json

"""
Handlers support filtering messages whose severity is less than their
setLevel() value. However, lower-severity handlers may still accept
higher-severity messages leading to duplicate logs. This filter allows one
to set a maximum severity level to avoid this.

Expects an integer representing a typical logging severity. This
defaults to logging.CRITICAL.
"""
class MaxSeverityFilter(logging.Filter):
    def __init__(self, severity=logging.CRITICAL):
        self.severity = severity

    def filter(self, record):
        # If the message severity is <= maximum, allow it.
        if record.levelno <= self.severity:
            return True

"""
A generic filter.
This filter primarily serves to set the proper msg_type value so that we can
more easily query messages where they're stored.
The 'name' attribute is set when the filter is assigned to to its respective
handler.
"""
class CommandoServiceFilter(logging.Filter):
    def filter(self, record):
        record.msg_type = 'commando-{}'.format(self.name)
        return True
