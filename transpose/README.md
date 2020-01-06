I was learning Giant Steps and wanted a quick way to transpose the entire tune, using technology.

## To use

Put a tune's changes into a file in `tunes` dir.  
Changes formatted as _n_ lines of space-separated chords.

```bash
# e.g.
docker-compose run --rm transpose giant_steps.txt
```

## Limitations!

- Currently only transposing up half step.
- Tested only with Giant Steps. Some chords not implemented.
- Some chords get transposed into awkward keys (e.g. "A# D#" vs "Bb Eb").

## Desired Features

- "X over Y" chords like `Bb/F`
- Pass through non-chord-symbol chars (like repeats `||:` and `:||`)
