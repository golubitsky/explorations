## Development

### Build

```sh
docker build -t cf .
```

### Run

```sh
docker run -p 8080:8080 -v $PWD:/usr/src/app -it cf functions-framework --target=hello --debug
```

[--debug](https://github.com/GoogleCloudPlatform/functions-framework-python/blob/master/src/functions_framework/_cli.py#L33) -> auto-reload

```sh
$ curl localhost:8080
Hello world!
```

## Deployment

https://github.com/GoogleCloudPlatform/functions-framework-python#google-cloud-functions
