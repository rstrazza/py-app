# py-app
Simple Python App

## dependencies

* [podman](https://podman.io/)

## Running local

```shell
python3 app.py
```

## Endpoints

* `/` simple healthcheck
* `/ip` returns the IP address of the container processing the request
* `/outgoing-http-call` tracing outgoing http call
* `/aws-sdk-call` tracing aws sdk call