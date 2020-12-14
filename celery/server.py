import os
from celery import Celery
import redis

CELERY_BROKER_URL = os.getenv("RABBITMQ")
CELERY_RESULT_BACKEND = os.getenv("REDISSERVER")

app = Celery("worker", backend=CELERY_RESULT_BACKEND,
                 broker=CELERY_BROKER_URL)

app.conf.update(
    result_extended=True,

   )
