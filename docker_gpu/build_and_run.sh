#!/usr/bin/env bash
set -e

docker build -t docker_gpu .
docker run -it --gpus=all docker_gpu
