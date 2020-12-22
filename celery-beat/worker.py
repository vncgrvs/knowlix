from celery import Celery
from server import app
from pymongo import MongoClient

MONGODB = os.getenv("MONGODB")
client = MongoClient(MONGODB)
db = client["taskdb"]["ta"]


@app.task()
def clean_pptx(self):
    delete = db.delete_many({"kwargs.downloaded": True})
    deleted_count = delete.deleted_count

    return deleted_count
