import os
from celery import Celery

CELERY_BROKER_URL = os.getenv("RABBITMQ")
CELERY_RESULT_BACKEND = os.getenv("REDISSERVER")

celery = Celery("worker", backend=CELERY_RESULT_BACKEND, broker=CELERY_BROKER_URL)

celery.conf.update(
   result_extended=True
)
