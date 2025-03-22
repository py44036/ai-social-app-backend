from fastapi import APIRouter
from pydantic import BaseModel

video_router = APIRouter()

# ✅ API ke request format ke liye model banayenge
class VideoFilterRequest(BaseModel):
    input: str  # Video file ka naam
    filter_type: str  # Filter ka type (cartoon, black_white, etc.)

@video_router.post("/apply_filter/")
async def apply_filter(request: VideoFilterRequest):
    return {"message": f"Applying {request.filter_type} filter on {request.input}"}