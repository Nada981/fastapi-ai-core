from abc import ABC, abstractmethod


class ModelInferenceError(Exception):
    """استثناء مخصص لأخطاء التوليد"""
    pass


class AIModel(ABC):
    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def generate_text(self, prompt: str) -> dict:
        pass


class CloudModel(AIModel):
    def __init__(self, name: str, api_key: str):
        super().__init__(name=name)
        self.api_key = api_key

    def generate_text(self, prompt: str) -> dict:
        if not prompt.strip():
            raise ModelInferenceError("Prompt cannot be empty!")
        return {
            "model": self.name,
            "prompt": prompt,
            "response": f"Mock response for: '{prompt}' via Cloud API",
            "status": "success"
        }