# Using `docker-compose` for Development and Testing

This repo contains a Docker Compose configuration that allows folks to spin up
containers that run a `commando` instance. This is useful when developing
and testing services.

## `docker-compose.yml`

The `docker-compose` command expects a configuration file describing the
containers to run. If not explicitly defined on the command line,
`docker-compose` will look for `docker-compose.yml` in the directory in which it
was called.

For our purposes, this repo contains a configuration file at
`support/docker-compose/docker-compose.yml`. This document assumes all example
commands are executed from `support/docker-compose/`.

**NOTE**: You may need to run these commands using elevated privileges (i.e.
`sudo`).

## Starting `commando` Services

To spin up a `commando` instance, use `docker-compose up -d`. This runs all
the defined containers in detached mode (in the background). You can list the
running containers via `docker-compose ps`:

```bash
$ sudo docker-compose up -d
Creating network "dockercompose_default" with the default driver
Creating commando ...
Creating commando ... done

$ sudo docker-compose ps
    Name            Command        State          Ports
---------------------------------------------------------------
commando   python3 server.py   Up      0.0.0.0:80->5000/tcp
```

In this example, the `commando` container is running, with port `80` on the
host translated to port `5000` in the container.

## Container Logs

`commando` writes logs to `stdout` and `stderr`. To review those logs,
use `docker-compose logs`:

```bash
$ sudo docker-compose logs
Attaching to commando
commando    | INFO:     Started server process [1]
commando    | INFO:     Waiting for application startup.
commando    | INFO:     Application startup complete.
commando    | INFO:     Uvicorn running on http://0.0.0.0:5000 (Press CTRL+C to quit)
commando    | {"timestamp": "2020-05-21 14:55:59,833", "level": "INFO", "client_ip": "172.31.22.125", "fqdn": "033e9cf9eb91", "headers": "{"host": "172.31.15.104", "connection": "close", "user-agent": "ELB-HealthChecker/2.0", "accept-encoding": "gzip, compressed"}", "http_version": "1.1", "method": "GET", "path": "/", "query_string": "", "server": "('172.21.0.2', 5000)", "status_code": "200"}
...
```

To follow (i.e. tail) the logs, use the `--follow` argument.

## Stopping `commando`

Stopping the `commando` service is easy: run `docker-compose down`:

```bash
$ sudo docker-compose down
Stopping commando ... done
Removing commando ... done
Removing network dockercompose_default
```
