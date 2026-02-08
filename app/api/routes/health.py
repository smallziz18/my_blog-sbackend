from fastapi import APIRouter

health_router = APIRouter()


@health_router.get("", tags=["health"])
async def health():
    return {"status": "ok"}


