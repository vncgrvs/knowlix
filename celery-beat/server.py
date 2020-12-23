import os
from celery import Celery
from celery.schedules import crontab


CELERY_BROKER_URL = os.getenv("RABBITMQ")
CELERY_RESULT_BACKEND = os.getenv("MONGODB")

app = Celery("scheduler", backend=CELERY_RESULT_BACKEND,
             broker=CELERY_BROKER_URL)

app.conf.update(
    result_extended=True,
    enable_utc=False,
    mongodb_backend_settings={
        'database': 'crontasks',
        'taskmeta_collection': 'ta',
    },
    task_routes={
        'tasks.*':{'queue':'crontasks'},
        
    },
    task_default_queue = 'crontasks'
    

)

app.conf.beat_schedule={
        "pptx-cleaner": { 
            "task": "clean_pptx", 
            "schedule": crontab(minute='*/2')
        }
    }
