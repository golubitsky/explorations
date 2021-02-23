#!/usr/bin/env bash
set -e

# Only for local use: token and password are disabled.
/opt/conda/bin/jupyter notebook \
    --notebook-dir=/usr/src/notebooks \
    --ip='*' --port=$NOTEBOOK_PORT \
    --no-browser --allow-root \
    --NotebookApp.token='' --NotebookApp.password=''
