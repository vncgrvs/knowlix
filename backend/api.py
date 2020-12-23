from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from fastapi.responses import FileResponse
from pydantic import BaseModel
from typing import List
from main import create_pptx, get_sections
import os
from pptx import Presentation
from server import celery
import json
import uuid
from datetime import datetime
from pymongo import MongoClient


file_path = "master.pptx"
pres = Presentation(file_path)
MONGODB = os.getenv("MONGODB")
client = MongoClient(MONGODB)
db = client["taskdb"]["ta"]

tags_metadata = [
    {
        "name": "powerpoint",
        "description": "handling powerpoint"
    },
    {
        "name": "job management",
        "description": "managing celery tasks"
    },

]

app = FastAPI(
    title="Knowlix",
    description="API Hub for the LeanIX Onboarding Deck",
    version="1.0.0",
    openapi_tags=tags_metadata)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=[]
)


class PPTX(BaseModel):
    sections: List[str]


class Download(BaseModel):
    taskID: str


## API ENDPOINTS ##
@app.get("/v1/sections", tags=["powerpoint"])
async def provide_sections():

    sections = get_sections(pres)

    if (not sections) or (len(sections) == 0):
        raise HTTPException(
            status_code=404, detail="No Sections in Master pptx")

    return JSONResponse(sections, status_code=200)


@app.post("/v1/pptxjob", tags=["job management"])
async def trigger_pptx_task(pptx: PPTX):
    task_name = "pptx"
    sections = pptx.sections
    no_sections = len(sections)
    sections_available = True
    exists_already = False
    status = None
    custom_id = str(uuid.uuid4().hex)
    kwargs = {
        'sections': sections,
        'customID': custom_id,
        'downloaded': False

    }

    if no_sections != 0:
        exists_already = check_existence(sections, db)
    else:
        sections_available = False

    if not exists_already and sections_available:
        task = celery.send_task(task_name, kwargs=kwargs, serializer='json', track_started = True)

    if sections_available and not exists_already:
        status = "success"

    elif not sections_available:
        status = "no_sections"

    elif exists_already:
        status = "pptx_exists"

    package = {
        'taskID': custom_id,
        'sections': sections,
        'status': status
    }

    return JSONResponse(package)


@app.post("/v1/download", tags=["powerpoint"])
async def download_pptx(download: Download):

    task_id = download.taskID

    result = db.find_one({"kwargs.customID": task_id}, {'result': 1, '_id': 0})
    unpack = result["result"]
    unpack = json.loads(unpack)
    file_path = unpack["filePath"]

    # return file_path
    return FileResponse(file_path)


@app.post("/v1/registerDownload", tags=["powerpoint"], status_code=201)
async def register_download(task_id: Download):
    task_id = task_id.taskID

    res = db.update_one({"kwargs.customID": task_id},
                        {"$set": {"kwargs.downloaded": True}
                         })

    changed_docs = res.modified_count

    return {'changedDocuments': changed_docs}


### UTILS ###

def check_existence(sections, db):
    exists_already = False
    no_sections = len(sections)
    query = {"kwargs.sections": {"$size": no_sections, "$all": sections}}

    hits = db.count_documents(query)

    if hits > 0:
        exists_already = True

    return exists_already
