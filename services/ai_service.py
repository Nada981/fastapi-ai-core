from typing import List, Dict
from core.models import AIModel, ModelInferenceError


class AIService:
    def __init__(self, model: AIModel):
        self.model = model
        # قائمة لتخزين السجل (In-Memory Database خفيفة)
        self.history: List[Dict] = []

    def handle_query(self, user_text: str) -> dict:
        try:
            result = self.model.generate_text(user_text)
            # حفظ العملية الناجحة في السجل
            self.history.append(result)
            return result
        except ModelInferenceError as e:
            return {
                "status": "error",
                "message": str(e)
            }

    def get_history(self) -> List[Dict]:
        """دالة ترجع سجل جميع الطلبات السابقة"""
        return self.history