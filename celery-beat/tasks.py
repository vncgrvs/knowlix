from celery import Celery
from server import app
from pymongo import MongoClient
import os

MONGODB = os.getenv("MONGODB")
client = MongoClient(MONGODB)
db = client["taskdb"]["ta"]


@app.task(name="clean_pptx", bind=True)
def clean_pptx(self):
    delete_items = list()
    db_delete_list = db.find({"kwargs.downloaded":True})

    for item in db_delete_list:
        raw=item["result"]
        filepath=parse_filepath(raw)
        delete_items.append(filepath)

    # delete = db.delete_many({"kwargs.downloaded": True})
    # deleted_count = delete.deleted_count

    return delete_items


def parse_filepath(item):
    json_item = json.loads(item)
    filepath = json_item["filePath"]
    
    return filepath