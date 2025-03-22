from fastapi import APIRouter

feed_router = APIRouter()

@feed_router.get("/")
async def root():
    return {"message": "AI Feed Processing API is running successfully!"}