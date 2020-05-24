import logging, json, sys
from commando.recording import filters, formatters

"""
Defines a base handler that returns a logging.StreamHandler which logs
to stderr.
"""
class BaseStreamHandler(logging.StreamHandler):
    def __init__(self, stream=sys.stderr, level=logging.ERROR):
        logging.StreamHandler.__init__(self, stream)
        self.setLevel(level)

"""
Returns a logging.StreamHandler that writes INFO and WARNING logs to stdout.
Expects a 'name' argument to be used as a suffix in the 'msg_type' value
set by the filter we attach to the handler.
"""
class CommandoServiceHandler(BaseStreamHandler):
    def __init__(self, name='generic'):
        super().__init__(sys.stdout, logging.INFO)
        warningAndBelow = filters.MaxSeverityFilter(logging.WARNING)
        self.addFilter(warningAndBelow)
        self.addFilter(filters.CommandoServiceFilter(name))
        self.setFormatter(formatters.CommandoServiceFormatter())

"""
Returns a logging.StreamHandler that writes ERROR and higher logs to stderr.
Expects a 'name' argument to be used as a suffix in the 'msg_type' value
set by the filter we attach to the handler.
"""
class CommandoServiceErrorHandler(BaseStreamHandler):
    def __init__(self, name='generic'):
        super().__init__()
        self.addFilter(filters.CommandoServiceFilter(name))
        self.setFormatter(formatters.CommandoServiceFormatter())
