FROM python:3.9.1-slim-buster

ENV PYTHONUNBUFFERED 1

COPY req.txt /req.txt
RUN pip install -r /req.txt

COPY server.py tasks.py beat.sh /celery-beat/
WORKDIR /celery-beat


# ENTRYPOINT celery -A worker beat --loglevel=debug  