# Commando

Jeli's Commando Slack App

## Binding an Interface and Port

By default, the uvicorn server will bind to host `0.0.0.0` and port `5000`. To
override the default behavior, define one or both of `COMMANDO_PORT` and
`COMMANDO_HOST` like so:

```bash
$ COMMANDO_HOST=127.0.0.1 COMMANDO_PORT=1234 python3 server.py`
```

### Binding a Port < 1024

To bind the service on a port below 1024 requires elevated privileges. To run
the Slack app on port 80, run the following command:

```bash
$ sudo COMMANDO_PORT=80 python3 server.py
```
