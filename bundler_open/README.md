https://boringrails.com/tips/bundle-open-debug-gems

For example, to read the code of the `pry` gem specified in the `Gemfile`:

```sh
docker build -t bundler_open .
docker run -it --rm bundler_open bundle open pry
```

To quit: press `esc`, type in `q!`, and press `Enter`.
