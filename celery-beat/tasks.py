from celery import Celery
from server import app
from pymongo import MongoClient
import os

MONGODB = os.getenv("MONGODB")
client = MongoClient(MONGODB)
db = client["crontasks"]["ta"]


@app.task(name="clean_pptx", bind=True)
def clean_pptx(self):
    # print("fired clean task", self.request.id)

    # delete = db.delete_many({"kwargs.downloaded": True})
    # deleted_count = delete.deleted_count

    return "test"
