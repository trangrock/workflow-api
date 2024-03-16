from fastapi import APIRouter

router = APIRouter()


# Health check endpoint
@router.get("/ping")
async def pong():
    return {"ping": "pong!"}
