FROM pytorch/pytorch

RUN apt-get update
RUN apt-get -y install gcc
RUN apt-get -y install python-pyaudio
RUN apt-get -y install swig
RUN apt-get -y install libpulse-dev
RUN apt-get -y install libasound2-dev
RUN conda install -c anaconda pyaudio

WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

CMD [ "python3", "demo.py"]