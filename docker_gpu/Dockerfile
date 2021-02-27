FROM nvcr.io/nvidia/tensorflow:20.12-tf2-py3

RUN /usr/bin/python -m pip install --upgrade pip

WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

CMD [ "python3", "quickstart.py"]