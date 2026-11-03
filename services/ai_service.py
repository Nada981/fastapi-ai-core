from core.models import AIModel, ModelInferenceError

class AIService:
    def __init__(self, model: AIModel):
        self.model = model
        self.history = []

    def handle_query(self, prompt: str) -> dict:
        try:
            output = self.model.generate_text(prompt)
            record = {"prompt": prompt, "response": output.get("text", "")}
            self.history.append(record)
            return {"status": "success", "data": record}
        except ModelInferenceError as e:
            return {"status": "error", "message": str(e)}

    def get_history(self) -> list:
        return self.history