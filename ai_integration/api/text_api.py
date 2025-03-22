from fastapi import APIRouter

text_router = APIRouter()

@text_router.post("/moderate_text/")
async def moderate_text(text: str):
    return {"status": "not toxic"}