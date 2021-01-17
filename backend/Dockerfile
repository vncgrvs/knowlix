FROM python:3.9.1-slim-buster

ENV PYTHONUNBUFFERED 1
WORKDIR /usr/app


COPY . .

RUN mkdir output  

RUN pip install --upgrade pip
RUN pip install -r req.txt --no-cache-dir


# CMD uvicorn --host=0.0.0.0 --port=8000 api:app