I was learning Giant Steps and wanted a quick way to transpose the entire tune, using technology.

## To use

Put a tune's changes into a file in `tunes` dir.  
Changes formatted as _n_ lines of space-separated chords.  
Optional second argument to specify _n_ half-steps to transpose up.

```bash
# e.g.
docker-compose run --rm transpose giant_steps.txt
# perfect fifth up
docker-compose run --rm transpose tune_up.txt 7
```

## Desired Features

- [x] Transpose up half-step.
- [x] Transpose up _n_ half-steps.
- [ ] Transpose down _n_ half-steps.
- [ ] Transpose by interval (`M3`, `P5`, `m6`, etc.)
- [ ] Some chords not implemented.
- [x] Some chords get transposed into awkward keys (e.g. "A# D#" vs "Bb Eb").

  - [ ] Need chord-context-aware solution.

- [ ] "X over Y" chords like `Bb/F`
- [x] Pass through non-chord-symbol chars for repeats, like `||:` and `:||`
