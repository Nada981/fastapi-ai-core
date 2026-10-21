from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from core.models import CloudModel
from services.ai_service import AIService

# 1. إنشاء التطبيق
app = FastAPI(title="SignAssist AI Service")

# 2. حقن الاعتمادية (Dependency Injection)
model = CloudModel(name="GPT-4-Turbo", api_key="sk-test-live-key")
ai_service = AIService(model=model)


# 3. مخطط البيانات المدخلة
class QueryRequest(BaseModel):
    prompt: str


# 4. المسارات (Endpoints)
@app.get("/")
def home():
    return {
        "status": "online",
        "service": "SignAssist AI Production Core"
    }


@app.post("/generate")
def generate_endpoint(request: QueryRequest):
    result = ai_service.handle_query(request.prompt)
    if result.get("status") == "error":
        raise HTTPException(
            status_code=400,
            detail=result.get("message")
        )
    return result


@app.get("/history")
def history_endpoint():
    """مسار جديد يعرض سجل كل الأسئلة والأجوبة السابقة"""
    return {
        "total_queries": len(ai_service.get_history()),
        "data": ai_service.get_history()
    }