from fastapi import APIRouter

voice_router = APIRouter()

@voice_router.get("/")
async def root():
    return {"message": "AI Voice Processing API is running successfully!"}