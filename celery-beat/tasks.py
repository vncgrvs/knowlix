from celery import Celery
from server import app
from pymongo import MongoClient
import os
import json

MONGODB = os.getenv("MONGODB")
client = MongoClient(MONGODB)
db = client["taskdb"]["ta"]


@app.task(name="clean_pptx", bind=True)
def clean_pptx(self):
    deleted_filepath = list()
    deleted_taskid = list()
    db_delete_list = db.find({"kwargs.downloaded": True})

    for item in db_delete_list:
        raw_filepath = item["result"]
        taskID = item["kwargs"]["customID"]
        filepath = parse_filepath(raw_filepath)
        os.remove(filepath)

        deleted_filepath.append(filepath)
        deleted_taskid.append(taskID)

    delete = db.delete_many({"kwargs.customID": {"$in": deleted_taskid}})
    deleted_count = delete.deleted_count

    package = {
        'tasks': deleted_taskid,
        'filePaths': deleted_filepath,
        'deleted_count': deleted_count
    }

    return package


def parse_filepath(item):
    json_item = json.loads(item)
    filepath = json_item["filePath"]

    return filepath
