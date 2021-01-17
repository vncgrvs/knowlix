from fastapi import APIRouter

router = APIRouter(
    prefix="/v1/stats",
    tags=["stats"],
)


@router.get("/health", tags=["stats"])
async def health():
    return [{"health": "ok"}]
