If you don't have `docker` or `docker-compose` commands, see [here](https://golubitsky.github.io/blog/2021/03/08/Getting-Started-With-Docker.html).

## Dockerized Jupyter

To spin up a Jupyter server:

```sh
docker-compose up
```

Navigate to http://localhost:8888

- Notebooks will be saved to the host's `./notebooks` directory.
- To change the port, change the `NOTEBOOK_PORT` in `./.env`.

## Bookmark

http://localhost:8888/notebooks/jupyter-notebook-tutorial.ipynb#Array-indexing
