FROM pytorch/pytorch

RUN apt-get update
RUN apt-get -y install gcc
RUN apt-get -y install python-pyaudio
RUN apt-get -y install swig
RUN apt-get -y install libpulse-dev
RUN apt-get -y install libasound2-dev
RUN conda install -c anaconda pyaudio

# Hack because latest version of howl has bug, but fix is already on master.
WORKDIR /howl
COPY ./howl-master-5ee0fbc .
RUN python setup.py bdist_wheel
RUN pip install dist/howl-0.1.2-py3-none-any.whl

WORKDIR /app
COPY . .

CMD [ "python3", "demo.py"]