FROM python:3.9.1-slim-buster

COPY req.txt /req.txt
RUN pip install -r /req.txt

COPY server.py worker.py /celery-beat/
WORKDIR /celery-beat/

ENTRYPOINT celery -A worker beat --loglevel=info  