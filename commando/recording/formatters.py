import logging, socket

"""
Return a logging.Formatter with a base format we can build on.
The base format will be a JSON string that includes a timestamp and severity
level. If an optional format (fmt) is passed to the constructor it will be
concatenated with the base format.
"""
class BaseFormatter(logging.Formatter):
    def __init__(self, fmt=None):
        self.style = '{' # str.format() style.
        # time.strftime() format. UTC? datetime.utcnow()
        self.datefmt = "%Y-%m-%d %H:%M:%S.%f %z"
        self.fqdn    = socket.getfqdn()
        """
        In a '{'-style format string, literal curly braces specified by
        doubling them. We need this so that we can build a proper JSON string.
        """
        self.this_format = '{{"timestamp": "{asctime}", ' \
                           '"level": "{levelname}", "msg_type": "{msg_type}"' 
        self.this_format += ', "fqdn": "{}"'.format(self.fqdn)

        if fmt:
            self.this_format += ', {}'.format(fmt)

        self.this_format += '}}' # Terminate the JSON structure.
        # Instantiate our formatter. We'll use the default datefmt but tweak
        # the milliseconds format a bit.
        super().__init__(fmt=self.this_format, style=self.style)
        # Format milliseconds: use a period as delimiter; 4 digits of precision
        self.default_msec_format = '%s.%04d'

"""
Access-like log format for the API.
"""
class AccessLogFormatter(BaseFormatter):
    def __init__(self):
        """
        NOTE: The 'headers' positional argument is not double-quoted because
        it will be a dictionary. To quote it would result in invalid JSON.
        """
        self.fmt = '"client_ip": "{client_ip}", "headers": {headers}, ' \
                   '"method": "{method}", "path": "{path}", ' \
                   '"query_string": "{query_string}", ' \
                   '"user_agent": "{user_agent}", "status": {status_code}, ' \
                   '"duration": {duration}'
        super().__init__(self.fmt)

"""
Error log format for the API.
"""
class ErrorLogFormatter(BaseFormatter):
    def __init__(self):
        # Start with the access log format...
        error_format = AccessLogFormatter().fmt
        # ...then concatenate our error-related fields.
        error_format += ', "exc_info": "{exc_info}", "lineno": "{lineno}", ' \
                        '"failing_file": "{pathname}"'
        super().__init__(error_format)

"""
General purpose log format.

We'll add the default 'message' LogRecord attribute here so that we can easily
insert messages passed as the first arugment to a given logging call.
"""
class CommandoServiceFormatter(BaseFormatter):
    def __init__(self):
        self.fmt = '"message": "{message}"'
        super().__init__(self.fmt)
