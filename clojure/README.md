To generate a project:

```sh
docker run -it -v $(PWD):/tmp clojure lein new hello-world
```

Having a project, start a repl:

```sh
docker run -it -v $(PWD)/hello-world:/tmp clojure lein repl
```

Source: https://github.com/Quantisan/docker-clojure
