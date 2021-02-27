#!/usr/bin/env bash
set -e

docker build -t quickstart .
docker run -it quickstart
