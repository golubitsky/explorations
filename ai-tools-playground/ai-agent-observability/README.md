## Development

Python app works:

```sh
docker compose run --build --rm --service-ports python-app
```

## Plan

```
ai-agent-observability/
├── docker-compose.yml
├── logs/                   # Shared volume for logs
├── loki-data/              # Loki storage
├── python-app/
│   ├── Dockerfile
│   ├── main.py
│   └── requirements.txt
├── git-mcp-server/
│   ├── Dockerfile
│   ├── main.py
│   └── requirements.txt
├── loki-mcp-server/
│   ├── Dockerfile
│   ├── main.py
│   └── requirements.txt
└── log-generator/          # Optional for testing
    ├── Dockerfile
    ├── main.py
    └── requirements.txt
```

## Logging

### Ingesting: Loki

Following https://grafana.com/docs/loki/latest/send-data/docker-driver/, I installed the Loki Docker driver:

```
docker plugin install grafana/loki-docker-driver --alias loki --grant-all-permissions
```

Then I configured each Docker container to use the driver https://grafana.com/docs/loki/latest/send-data/docker-driver/configuration/#configure-the-logging-driver-for-a-swarm-service-or-compose.

The endpoint comes from the [Loki HTTP API to ingest logs](https://grafana.com/docs/loki/latest/reference/loki-http-api/#ingest-logs).

Loki takes a while to be ready, but then it returns a 200: `curl http://localhost:3100/ready`.

Then I can send a test log to Loki and view it in grafana:

```
curl -X POST "http://localhost:3100/loki/api/v1/push" \
  -H "Content-Type: application/json" \
  -d '{
    "streams": [
      {
        "stream": {
          "job": "manual-test"
        },
        "values": [
          [ "'$(date +%s%N)'", "Hello from curl!" ]
        ]
      }
    ]
  }'
```

The Python app is configured in the `docker-compose.yml` to send logs via the Loki driver.

### Viewing: Grafana

http://localhost:3000/ admin/admin

Hitting the http://localhost:8000/ Python App endpoint should be sending logs.

[This query](http://localhost:3000/explore?schemaVersion=1&panes=%7B%22mi3%22%3A%7B%22datasource%22%3A%22P8E80F9AEF21F6940%22%2C%22queries%22%3A%5B%7B%22refId%22%3A%22A%22%2C%22expr%22%3A%22%7Bjob%3D%7E%5C%22.%2B%5C%22%7D%22%2C%22queryType%22%3A%22range%22%2C%22datasource%22%3A%7B%22type%22%3A%22loki%22%2C%22uid%22%3A%22P8E80F9AEF21F6940%22%7D%2C%22editorMode%22%3A%22code%22%2C%22direction%22%3A%22backward%22%7D%5D%2C%22range%22%3A%7B%22from%22%3A%22now-1h%22%2C%22to%22%3A%22now%22%7D%2C%22compact%22%3Afalse%7D%7D&orgId=1) returns all logs in Grafana > Explore > Code: `{job=~".+"}`

## LLM tooling

I've switched to the VS Code Continue extension. Cline generated heavy-duty prompts and generally did not work with local Ollama models.
