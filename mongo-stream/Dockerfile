FROM python:3.7.9-slim-buster

WORKDIR /usr/app
COPY req.txt ./
COPY server.py  ./

RUN pip install --upgrade pip
RUN pip install -r req.txt --no-cache-dir

