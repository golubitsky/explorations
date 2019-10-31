Bookmark:

https://elmprogramming.com/array.html

```sh
docker run -it --init -p 8000:8000 -v $PWD:/src elm elm reactor
open http://localhost:8000/src/Playground.elm
```

```sh
docker run -it --init elm elm repl --no-colors
```

# Dev setup

How did we get here?

```sh
docker build -t elm .
docker run -v $PWD:/src -it elm elm init
docker run -v $PWD:/src -it elm elm-test init
```

Run tests!

```sh
docker run -it --init -v $PWD:/src elm elm-test --watch
```

Run live server!

```sh
docker run -it --init \
    -p 8000:8000 \
    -v $PWD:/src \
    elm elm-live src/Main.elm --host 0.0.0.0
```
