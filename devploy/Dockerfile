FROM python:3.7

ARG SERVICE_DIR
WORKDIR /usr/src/app

COPY ${SERVICE_DIR}/requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY ${SERVICE_DIR} .

ENV PYTHONDONTWRITEBYTECODE=1
CMD [ "python", "src/app.py" ]