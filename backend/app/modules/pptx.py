from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import JSONResponse, FileResponse
import app.utils.auth as utils
from app.utils.server import celery
from pydantic import BaseModel
from typing import List, Optional
import json
import uuid
from pptx import Presentation
from pymongo import MongoClient
import pymongo
from app.pptx.main import create_pptx, get_sections
import os
from datetime import datetime, timedelta


file_path = "app/master.pptx"
print(os.path)
pres = Presentation(file_path)
MONGODB = os.getenv("MONGODB")
client = MongoClient(MONGODB)
db = client["taskdb"]["ta"]

router = APIRouter(
    prefix="/v1/pptx",
    tags=["powerpoint"],
)

class PPTX(BaseModel):
    sections: List[str]

class Download(BaseModel):
    taskID: str

@router.get("/sections", tags=["powerpoint"])
async def provide_sections(token: bool = Depends(utils.is_access_token_valid)):

    sections = get_sections(pres)

    if (not sections) or (len(sections) == 0):
        raise HTTPException(
            status_code=404, detail="No Sections in Master pptx")

    return JSONResponse(sections, status_code=200)


@router.post("/pptxjob", tags=["job management"])
async def trigger_pptx_task(pptx: PPTX, token: bool = Depends(utils.is_access_token_valid)):
    task_name = "pptx"
    sections = pptx.sections
    no_sections = len(sections)
    sections_available = True
    exists_already = False
    status = None
    custom_id = str(uuid.uuid4().hex)
    timestamp = datetime.now().isoformat()

    kwargs = {
        'sections': sections,
        'customID': custom_id,
        'downloaded': False,
        'date_started': timestamp

    }

    if no_sections != 0:
        exists_already = utils.check_existence(sections, db)
    else:
        sections_available = False

    if not exists_already and sections_available:
        task = celery.send_task(task_name, kwargs=kwargs, serializer='json')

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


@router.post("/download", tags=["powerpoint"])
async def download_pptx(download: Download, token: bool = Depends(utils.is_access_token_valid)):

    task_id = download.taskID

    result = db.find_one({"kwargs.customID": task_id}, {'result': 1, '_id': 0})
    unpack = result["result"]
    unpack = json.loads(unpack)
    file_path = unpack["filePath"]

    # return file_path
    return FileResponse(file_path)


@router.post("/registerDownload", tags=["powerpoint"], status_code=201)
async def register_download(task_id: Download, token: bool = Depends(utils.is_access_token_valid)):
    task_id = task_id.taskID

    res = db.update_one({"kwargs.customID": task_id},
                        {"$set": {"kwargs.downloaded": True}
                         })

    changed_docs = res.modified_count

    return {'changedDocuments': changed_docs}


@router.get("/getDownloads", tags=["powerpoint"])
async def getDownloads(token: bool = Depends(utils.is_access_token_valid)):
    res = db.find({}).sort(
        [("kwargs.date_started", pymongo.DESCENDING)]).limit(10)
    results = list()

    for item in res:
        taskID = item["kwargs"]["customID"]
        date_started = item["kwargs"]["date_started"]
        status = item["status"]
        sections = item["kwargs"]["sections"]

        package = {
            'taskID': taskID,
            'date_started': date_started,
            'status': status,
            'sections': sections
        }
        results.append(package)

    return JSONResponse(results, status_code=200)
