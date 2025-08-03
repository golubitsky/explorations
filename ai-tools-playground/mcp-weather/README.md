Following this tutorial: https://modelcontextprotocol.io/quickstart/server

## Cline (VS Code extension) configuration

File: /Users/mgolubitsky/Library/Application Support/Code/User/globalStorage/saoudrizwan.claude-dev/settings/cline_mcp_settings.json

Contents (following the Claude config in the quickstart above):

```json
{
  "mcpServers": {
    "weather": {
      "disabled": false,
      "timeout": 60,
      "type": "stdio",
      "command": "uv",
      "args": [
        "--directory",
        "/Users/mgolubitsky/source/explorations/ai-tools-playground/mcp-weather",
        "run",
        "weather.py"
      ]
    }
  }
}
```

This configuration enables me to ask "what is the weather in Boston?". However, I quickly max out the free model OpenRouter rate limit. I tried configuring Cline to use the Ollama llama3.1:8b model running locally, but that results in failures such as:

```
Cline tried to use plan_mode_respond without value for required parameter 'response'. Retrying...

Cline uses complex prompts and iterative task execution that may be challenging for less capable models. For best results, it's recommended to use Claude 4 Sonnet for its advanced agentic coding capabilities.

API Request Failed
```


## TODO

Later I'll also look into https://gofastmcp.com/getting-started/welcome.

Here's another tutorial, to build a calculator MCP tool, which happens to use FastMCP: https://github.com/modelcontextprotocol/python-sdk.
