# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster

WORKDIR /app

# OS dependencies
RUN apt-get update
RUN apt-get install -y watch

# Application dependencies
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

# Source code
COPY . .

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONPATH=.

CMD ["python3", "src/game.py"]