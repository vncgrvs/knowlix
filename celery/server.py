import os
from celery import Celery


CELERY_BROKER_URL = os.getenv("RABBITMQ")
CELERY_RESULT_BACKEND = os.getenv("MONGODB")

app = Celery("worker", backend=CELERY_RESULT_BACKEND,
             broker=CELERY_BROKER_URL)

app.conf.update(
    result_extended=True,
    enable_utc=False,
    mongodb_backend_settings={
        'database': 'taskdb',
        'taskmeta_collection': 'ta',
    },
    task_routes={
        'worker.*':{'queue':'presentations'},
        
    },
    task_default_queue = 'presentations'
    
)
