from fastapi import FastAPI
from fastapi.responses import FileResponse
from ai_feed import feed_router
from ai_voice import voice_router
from ai_video_editing import video_router

app = FastAPI()

# ✅ AI API ko register karein
app.include_router(feed_router, prefix="/feed", tags=["Feed Processing"])
app.include_router(voice_router, prefix="/voice", tags=["Voice Processing"])
app.include_router(video_router, prefix="/video", tags=["Video Processing"])

# ✅ Favicon Fix Karein
@app.get("/favicon.ico", include_in_schema=False)
async def favicon():
    return FileResponse("static/favicon.ico")

@app.get("/")
async def root():
    return {"message": "AI Social App API is running successfully!"}