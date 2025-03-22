from fastapi import APIRouter

video_router = APIRouter()

@video_router.post("/apply_filter/")
async def apply_filter(video_path: str, filter_type: str):
    return {"message": f"Applying {filter_type} filter to {video_path}"}