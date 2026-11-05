import os
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from dotenv import load_dotenv

from core.models import GeminiCloudModel
from services.ai_service import AIService

load_dotenv()

MODEL_NAME = os.getenv("AI_MODEL_NAME", "Default-Model")
API_KEY = os.getenv("GEMINI_API_KEY", "default-fallback-key")

app = FastAPI(title="SignAssist AI Service")

model = GeminiCloudModel(name=MODEL_NAME, api_key=API_KEY)
ai_service = AIService(model=model)


class QueryRequest(BaseModel):
    prompt: str


# (Endpoints)
@app.get("/")
def home():
    return {
        "status": "online",
        "service": "SignAssist AI Production Core",
        "loaded_model": MODEL_NAME,
    }


@app.post("/generate")
def generate_endpoint(request: QueryRequest):
    result = ai_service.handle_query(request.prompt)
    if result.get("status") == "error":
        raise HTTPException(status_code=400, detail=result.get("message"))
    return result


@app.get("/history")
def history_endpoint():
    return {
        "total_queries": len(ai_service.get_history()),
        "data": ai_service.get_history(),
    }
