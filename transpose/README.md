I was learning Giant Steps and wanted a quick way to transpose the entire tune, using technology.

## To use

Put a tune's changes into a file in `tunes` dir.  
Changes formatted as _n_ lines of space-separated chords.

```bash
# e.g.
docker-compose run --rm transpose giant_steps.txt
```

## Desired Features

- [ ] Currently only transposing up half step.
- [ ] Some chords not implemented.
- [x] Some chords get transposed into awkward keys (e.g. "A# D#" vs "Bb Eb").

  - [ ] Need chord-context-aware solution.

- [ ] "X over Y" chords like `Bb/F`
- [x] Pass through non-chord-symbol chars for repeats, like `||:` and `:||`
