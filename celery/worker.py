from celery import current_task
from celery import states
import os
from celery import Celery
from time import sleep
from celery.exceptions import Ignore
from pptx import Presentation
from pymongo import MongoClient
from pptx_handler import create_pptx
import json


from server import app
MONGODB = os.getenv("MONGODB")
client = MongoClient(MONGODB)
db = client["taskdb"]["ta"]


@app.task(name='pptx', bind=True, max_retries=3)
def generate_pptx(self, sections, customID,downloaded,date_started):

    try:
        pptx_path = "master.pptx"
        task_id=self.request.id

        pres= Presentation(pptx_path)
        file_path=create_pptx(pres,sections)


    
    except Exception as exec:
        self.retry(exec=exec, countdown = 2 ** self.request.retries)

    output = {
        'filePath':file_path
    }

    
    return output

