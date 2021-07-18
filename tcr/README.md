Experiment with `t && c || r`, as [described by Kent Beck](https://medium.com/@kentbeck_7670/test-commit-revert-870bbd756864).

## Setup

VS Code keyboard shortcut to run TCR on demand:

```
  {
    "key": "cmd+shift+r",
    "command": "workbench.action.terminal.sendSequence",
    "args": {
      "text": "~/source/explorations/tcr/tcr.sh\u000D"
    }
  }
```

## Earlier setup, which didn't work

It didn't work because I can save neither a production or test file in isolation. Therefore it's impossible to make progress.

### The setup

VS Code config to setup a TCR script to run on save.

```
//   "files.autoSave": "afterDelay",
//   "files.autoSaveDelay": 500,
  "saveAndRun": {
    "commands": [
      {
        "match": ".*",
        "cmd": "~/source/explorations/tcr/tcr.sh",
        "useShortcut": false,
        "silent": false
      }
    ]
  },
```

I normally use `autoSave` so I have to disable that temporarily. I don't know how to override settings for a single directory.

## Intended Workflow!

1. Run TCR (`cmd+shift+r`) and hope for the best. This runs the tests. If tests pass a `working` commit is made. Else, all changes are removed!
2. Repeat 1 indefinitely or until feature complete.
3. `make branch_as_one_commit` to soft reset + recommit;
4. Manually rename commit from previous step.
5. Merge to master.

## My experience with it!

- The first time I wrote a bunch of code and felt reluctant to run TCR was interesting. Felt a sense of a risk. Then saw all my code disappear. Then laughed. High stakes.
- The requirement to make a change small enough to succeed induces continuous refactoring to "make ready" to implement the change.

## Project I'm implementing in this directory

https://codingdojo.org/kata/PacMan/
