Spin up a Clickhouse server:

```sh
docker-compose up
```

In a separate terminal, run the [client](https://clickhouse.com/docs/en/interfaces/cli) inside the same docker container:

```sh
docker exec -it clickhouse-server clickhouse-client
```

Access the web UI here: http://localhost:8123/play.

You can also use [DBeaver](https://dbeaver.io/download/).