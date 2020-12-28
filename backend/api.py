from fastapi import FastAPI, HTTPException, Depends, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
import pymongo
from fastapi.responses import FileResponse
from pydantic import BaseModel
from typing import List, Optional
from main import create_pptx, get_sections
import os
from datetime import datetime
from pptx import Presentation
from server import celery
import json
import uuid
from datetime import datetime, timedelta
from pymongo import MongoClient
import api_utils as utils

## CONFIG ##
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
    {
        "name": "auth",
        "description": "authentication workflow endpoint"
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


class User(BaseModel):
    username: str
    password: str
    first_name: str
    last_name: str
    


class TokenData(BaseModel):
    username: Optional[str] = None


class Token(BaseModel):
    access_token: str
    token_type: str


class Download(BaseModel):
    taskID: str


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/v1/token")
## API ENDPOINTS ##


@app.get("/v1/sections", tags=["powerpoint"])
async def provide_sections(token: bool = Depends(utils.is_token_valid)):

    sections = get_sections(pres)

    if (not sections) or (len(sections) == 0):
        raise HTTPException(
            status_code=404, detail="No Sections in Master pptx")

    return JSONResponse(sections, status_code=200)


@app.post("/v1/pptxjob", tags=["job management"])
async def trigger_pptx_task(pptx: PPTX, token: bool = Depends(utils.is_token_valid)):
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


@app.post("/v1/download", tags=["powerpoint"])
async def download_pptx(download: Download, token: bool = Depends(utils.is_token_valid)):

    task_id = download.taskID

    result = db.find_one({"kwargs.customID": task_id}, {'result': 1, '_id': 0})
    unpack = result["result"]
    unpack = json.loads(unpack)
    file_path = unpack["filePath"]

    # return file_path
    return FileResponse(file_path)


@app.post("/v1/registerDownload", tags=["powerpoint"], status_code=201)
async def register_download(task_id: Download, token: bool = Depends(utils.is_token_valid)):
    task_id = task_id.taskID

    res = db.update_one({"kwargs.customID": task_id},
                        {"$set": {"kwargs.downloaded": True}
                         })

    changed_docs = res.modified_count

    return {'changedDocuments': changed_docs}


@app.get("/v1/getDownloads", tags=["powerpoint"])
async def getDownloads(token: bool = Depends(utils.is_token_valid)):
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


### AUTH ###
import config

@app.post("/v1/token", response_model=Token, tags=["auth"])
async def create_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = utils.authenticate_user(username=form_data.username,
                                   password=form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=config.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = utils.create_access_token(
        data={"sub": user["username"]}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}


@app.post("/v1/register", tags=["auth"])
async def register_user(user: User):
    username = user.username
    password = user.password
    first_name = user.first_name
    last_name = user.last_name
    role = "VIEWER"


    res = utils.create_user(username=username, password=password)

    return JSONResponse(res)

