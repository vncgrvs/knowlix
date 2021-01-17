from fastapi import APIRouter

router = APIRouter(
    prefix="/v1/external",
    tags=["thrid-parties"],
)

@router.post("/trello", tags=["third-parties"])
async def webhook_trello():
    
    
