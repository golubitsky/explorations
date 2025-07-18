# Python Installation

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
