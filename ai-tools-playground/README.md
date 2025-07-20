# Python

## Installation

I'm using [uv](https://docs.astral.sh/uv/guides/install-python/#installing-a-specific-version) to manage Python dependencies.

I installed it with

```
uv python install --default
```

which put `python` and `python3` into my PATH, as seen from the output of

```
which python
which python3
uv python list
```

## Project/Dependency Management

To initialize a project:

```
uv init current-time
```

To run a file:

```
uv run main.py
```

To [add a dependency](https://docs.astral.sh/uv/guides/projects/#managing-dependencies):

```
uv add ollama
```

# Local LLM Usage (Ollama)

I'm using [Ollama](https://ollama.com/) to run LLMs locally.

After installation, I had to add a symlink to get `ollama` to be in the PATH.

```
sudo ln -s /Applications/Ollama.app/Contents/Resources/ollama /usr/local/bin/ollama
```

## Operation

To see a list of models I have available locally:

```
ollama list
```

A model can be invoked via a POST request to the REST API:

```
curl http://localhost:11434/api/generate --data '{
  "model": "llama3.1:8b",
  "prompt": "What is the Answer to the Ultimate Question of Life, the Universe, and Everything?",
  "stream": false
}'
```

It will keep running in the background, as can be seen via

```
ollama ps
```

We can also pull models using `ollama pull`. The interface is very inspired by Docker. It appears that LangChain:Ollama::Kubernetes::Docker.

# Remote LLM usage

## Cline

I installed the [Cline](https://cline.bot/) VS Code extension. I was able to get it to work with a free model by supplying my OpenRouter API key (which has a limit of $0 on it).

TODO: can I use this same API key in an app?

## OpenRouter

[OpenRouter](https://openrouter.ai/settings/keys) provides free access to certain models, including the 685B param [DeepSeek: DeepSeek V3 0324 (free)](https://openrouter.ai/deepseek/deepseek-chat-v3-0324:free).

I think the free access is limited to 50 requests per day?

## DeepSeek

Using [DeepSeek](https://platform.deepseek.com/api_keys) directly via its API might be cheaper.
