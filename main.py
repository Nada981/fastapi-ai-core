import os
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from dotenv import load_dotenv

from core.models import CloudModel
from services.ai_service import AIService

# تحميل المتغيرات من ملف .env
load_dotenv()

# قراءة المتغيرات بأمان من نظام التشغيل
MODEL_NAME = os.getenv("AI_MODEL_NAME", "Default-Model")
API_KEY = os.getenv("AI_API_KEY", "default-fallback-key")

# 1. إنشاء التطبيق
app = FastAPI(title="SignAssist AI Service")

# 2. حقن الاعتمادية باستخدام القيم الآمنة
model = CloudModel(name=MODEL_NAME, api_key=API_KEY)
ai_service = AIService(model=model)


# 3. مخطط البيانات المدخلة
class QueryRequest(BaseModel):
    prompt: str


# 4. المسارات (Endpoints)
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