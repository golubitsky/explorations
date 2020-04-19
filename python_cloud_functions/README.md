## Development

### Build

```sh
docker build -t cf .
```

### Run

([--debug](https://github.com/GoogleCloudPlatform/functions-framework-python/blob/master/src/functions_framework/_cli.py#L33) causes auto-reload)

```sh
docker run -p 8080:8080 -v $PWD:/usr/src/app -it cf functions-framework --target=hello --debug
```

```sh
$ curl localhost:8080
Hello world!
```

## Deployment

- https://github.com/GoogleCloudPlatform/functions-framework-python#google-cloud-functions

- https://cloud.google.com/functions/docs/quickstart

```sh
gcloud config set project thebiglove
gcloud functions deploy hello --runtime python37 --trigger-http
```
