## Run tests continuously

```bash
lein test-refresh
```

This works by virtue of:

```
$ cat /Users/mikegolubitsky/.lein/profiles.clj
{:user {:plugins [[venantius/ultra "0.6.0"]
                  [proto-repl "0.3.1"]
                  [com.jakemccrary/lein-test-refresh "0.24.1"]]}}
```
