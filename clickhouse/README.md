Spin up a Clickhouse server:

```sh
docker-compose up
```

In a separate terminal, run the client inside the same docker container:

```sh
docker exec -it clickhouse-server clickhouse-client
```
