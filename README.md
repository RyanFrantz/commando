# Commando

The Commando Slack App

## Running the Service

The simplest way to get `commando` started is to run `make serve`. This will
test that you have an activated virtualenv [1] and launch the FastAPI service.

### Binding an Interface and Port

By default, the uvicorn server will bind to host `0.0.0.0` and port `5000`. To
override the default behavior, define one or both of `COMMANDO_PORT` and
`COMMANDO_HOST` like so:

```bash
$ COMMANDO_HOST=127.0.0.1 COMMANDO_PORT=1234 make serve`
```

#### Binding a Port < 1024

To bind the service on a port below 1024 requires elevated privileges. To run
the Slack app on port 80, run the following command:

```bash
$ sudo COMMANDO_PORT=80 make serve`
```

## Footnotes

[1] You can validate you are operating in an activated virtualenv by running
`make venv`. See the `venv` target in the `Makefile` for more details. Note that
`make serve` automatically calls the `venv` target.
