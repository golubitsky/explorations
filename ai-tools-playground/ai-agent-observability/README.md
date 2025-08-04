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

TODO: Still haven't figured out how to ingest logs from Python app. The Loki Docker Driver causes app to hang when shutting it down. Unable to easily kill container even. Maybe have the Python app send logs directly?

### Viewing: Grafana

http://localhost:3000/ admin/admin

Hitting the http://localhost:8000/ Python App endpoint should be sending logs.

This query returns all logs in Grafana > Explore > Code: `{job=~".+"}`

## LLM tooling

I've switched to the VS Code Continue extension. Cline generated heavy-duty prompts and generally did not work with local Ollama models.
