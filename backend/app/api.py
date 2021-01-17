from fastapi import FastAPI
from .modules import auth, pptx, stats

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
    description="API Hub for the LeanIX Knowledge Center",
    version="1.0.0",
    
    openapi_tags=tags_metadata)

app.include_router(stats.router)
app.include_router(pptx.router)
app.include_router(auth.router) 

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_hesaders=["*"],
#     expose_headers=[]
# )
