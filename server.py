import os, uvicorn
from commando import create_app
from commando.logging import CommandoAccessFormatter
"""
This file is an entrypoint for running our application. Run this from the
command line or use this as the entrypoint in an ASGI web server like uvicorn.
NOTE: A full-fledged web server like nginx would be configured to proxy requests
from the outside world to uvicorn.

From the command line:

$ python3 server.py
"""
app = create_app()

# Use a host and/or port defined in the environment or fall back to a default.
commando_host = os.environ.get('COMMANDO_HOST', '0.0.0.0')
commando_port = int(os.environ.get('COMMANDO_PORT', 5000))

# Override uvicorn's simple access log format.
access_log_format = (
    '{"timestamp": "%(asctime)s", "level": "%(levelname)s", '
    '"client_ip": "%(client_ip)s", "fqdn": "%(fqdn)s", '
    '"headers": "%(headers)s", "http_version": "%(http_version)s", '
    '"method": "%(method)s", "path": "%(path)s", '
    '"query_string": "%(query_string)s", "server": "%(server)s", '
    '"status_code": "%(status_code)s"}'
)
log_config = uvicorn.config.LOGGING_CONFIG
log_config['formatters']['access']['()']  = CommandoAccessFormatter
log_config['formatters']['access']['fmt'] = access_log_format

# To run in development mode:
# python3 -m uvicorn server:app --host 0.0.0.0 --port 5000 --reload
if __name__ == "__main__":
    uvicorn.run(app, host=commando_host, port=commando_port, log_config=log_config)
