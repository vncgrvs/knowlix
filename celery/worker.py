from celery import current_task
from celery import states
import os
from celery import Celery
from time import sleep
from celery.exceptions import Ignore
from pptx import Presentation
import redis
from pptx_handler import create_pptx
import json

CELERY_BROKER_URL = os.getenv("RABBITMQ")
CELERY_RESULT_BACKEND = os.getenv("REDISSERVER")
from server import app



@app.task(name='pptx', bind=True, max_retries=3)
def generate_pptx(self, sections, downloadStatus):

    try:
        pptx_path = "master.pptx"
        task_id=self.request.id
        # task_prefix = "celery-task-meta-"
        # task_str = task_prefix + task_id
        

        pres= Presentation(pptx_path)
        file_path=create_pptx(pres,sections)
    
    except Exception as exec:
        self.retry(exec=exec, countdown = 2 ** self.request.retries)


    return f"{task_id} finished. stored {file_path}"

