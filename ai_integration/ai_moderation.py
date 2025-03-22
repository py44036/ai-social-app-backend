from fastapi import APIRouter
from transformers import pipeline

router = APIRouter()

# Hugging Face का Pre-trained Model Use कर रहे हैं
moderation_pipeline = pipeline("text-classification", model="facebook/bart-large-mnli")

@router.post("/moderate")
def moderate_text(text: str):
    """यह API Text को Scan करके उसे Moderation के लिए Classify करेगी"""
    result = moderation_pipeline(text)
    return {"text": text, "moderation_result": result}
