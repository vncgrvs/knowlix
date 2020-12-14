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


file_path = "master.pptx"
pres= Presentation(file_path)

tags_metadata= [
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
    title= "SurfBoard",
    description= "API Hub for the LeanIX Onboarding Deck",
    version= "1.0.0",
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
    
    
@app.get("/v1/sections", tags = ["powerpoint"])
async def provide_sections():

    sections = get_sections(pres)

    if (not sections) or (len(sections)==0):
        raise HTTPException(status_code=404, detail="No Sections in Master pptx")

    return JSONResponse(sections,status_code=200)


@app.post("/v1/pptxjob", tags = ["job management"])
async def deliver_pptx(pptx: PPTX):
    task_name = "pptx"
    sections = pptx.sections
    kwargs ={
        'sections':sections,
        'downloadStatus': 'ready'
        }
    


    task = celery.send_task(task_name, kwargs = kwargs, serializer='json')

    package = {
        'taskID': task.id,
        'sections': sections
    }

    
    return JSONResponse(package)
    
    
    
    
