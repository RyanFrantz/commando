import json, logging, socket

"""
This formatter class will be used to override uvicorn's default behavior for
access log. We've reused some code from uvicorn.logging.AccessFormatter.
"""
class CommandoAccessFormatter(logging.Formatter):
    def path(self, scope):
        return scope.get('root_path', '') + scope['path']

    def query_string(self, scope):
        return scope.get('query_string', b'').decode('ascii')

    def full_path(self, scope):
        path         = scope.get('root_path', '') + scope['path']
        query_string = self.query_string(scope)
        if query_string:
            return path + '?' + query_string
        return path

    """
    'record' is generated in uvicorn/protocols/http/httptools_impl.py
    when self.access_logger.info() is called. self.access_logger in that
    context is the 'uvicorn.access' logger.
    """
    def formatMessage(self, record):
        # 'scope' is defined in uvicorn.
        scope = record.__dict__['scope']

        client_ip, client_port = scope.get('client')
        fqdn                   = socket.getfqdn()
        full_client            = f"{client_ip}:{client_port}"
        full_path              = self.full_path(scope)
        headers                = json.dumps(
            {k.decode('ascii'):v.decode('ascii') for (k,v) in scope['headers']}
        )
        http_version           = scope['http_version']
        method                 = scope['method']
        path                   = self.path(scope)
        query_string           = self.query_string(scope)
        server                 = scope['server']  
        status_code            = record.__dict__['status_code']

        record.__dict__.update({
            'client_ip':    client_ip,
            'fqdn':         fqdn,
            'full_client':  full_client,
            'full_path':    full_path,
            'headers':      headers,
            'http_version': http_version,
            'method':       method,
            'path':         path,
            'query_string': query_string,
            'server':       server,
            'status_code':  status_code
        })
        return super().formatMessage(record)
