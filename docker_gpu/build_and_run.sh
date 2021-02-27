#!/usr/bin/env bash
set -e

docker build -t quickstart .
docker run -it --gpus=all quickstart
