from celery import Celery
from server import app
from pymongo import MongoClient

MONGODB = os.getenv("MONGODB")
client = MongoClient(MONGODB)
db = client["taskdb"]["ta"]

@app.task()
def clean_pptx(self):
    #TODO: delete all entries with kwargs.downloaded = True