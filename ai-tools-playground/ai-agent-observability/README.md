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

## LLM tooling

I've switched to the VS Code Continue extension. Cline generated heavy-duty prompts and generally did not work with local Ollama models.
