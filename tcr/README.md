Experiment with `t && c || r`, as [described by Kent Beck](https://medium.com/@kentbeck_7670/test-commit-revert-870bbd756864).

VS Code config to setup a TCR script to run on save.

```
//   "files.autoSave": "afterDelay",
//   "files.autoSaveDelay": 500,
  "saveAndRun": {
    "commands": [
      {
        "match": ".*",
        "cmd": "/Users/mikegolubitsky/source/explorations/tcr/tcr.sh",
        "useShortcut": false,
        "silent": false
      }
    ]
  },
```

I normally use `autoSave` so I have to disable that temporarily. I don't know how to override settings for a single directory.
