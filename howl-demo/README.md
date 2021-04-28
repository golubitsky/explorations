The intent of this folder is to run the quickstart of https://github.com/castorini/howl. All the dependencies are satisfied (at least in that there are no errors in fetching them).

To do so:

```sh
# running the build ensures the latest version of code is used
docker-compose build && docker-compose run --rm develop
```

However, there is an error caused by the `howl` quickstart code itself. It is unable to pull the dataset with the error:

```
Traceback (most recent call last):
  File "demo.py", line 17, in <module>
    client.from_pretrained("hey_fire_fox", force_reload=False)
  File "/opt/conda/lib/python3.8/site-packages/howl/client/howl_client.py", line 136, in from_pretrained
    engine, ctx = torch.hub.load(
  File "/opt/conda/lib/python3.8/site-packages/torch/hub.py", line 339, in load
    model = _load_local(repo_or_dir, model, *args, **kwargs)
  File "/opt/conda/lib/python3.8/site-packages/torch/hub.py", line 368, in _load_local
    model = entry(*args, **kwargs)
  File "/root/.cache/torch/hub/castorini_howl_master/hubconf.py", line 32, in hey_fire_fox
    engine, ctx = _load_model(pretrained, "res8", "howl/hey-fire-fox", **kwargs)
TypeError: _load_model() missing 1 required positional argument: 'device'
```

I observed the same error in Colab.
