FROM python:3.9.1-slim-buster

COPY req.txt /req.txt
RUN pip install -r /req.txt

COPY server.py worker.py pptx_handler.py core.py master.pptx /celery/
WORKDIR /celery/
RUN mkdir output 

ENTRYPOINT celery -A worker worker -E --loglevel=info -n celeryworker -Q presentations