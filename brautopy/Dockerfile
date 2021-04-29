FROM python:3.8-slim-buster

RUN apt-get update
RUN apt-get -y install gcc ffmpeg libsm6 libxext6

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .