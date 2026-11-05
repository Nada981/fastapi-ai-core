from abc import ABC, abstractmethod
import os
from google import genai

import time


class ModelInferenceError(Exception):
    
    pass


class AIModel(ABC):
    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def generate_text(self, prompt: str) -> dict:
        pass


class GeminiCloudModel(AIModel):
    def __init__(self, name: str = None, api_key: str = None):
        model_name = name or os.getenv("AI_MODEL_NAME", "gemini-flash-lite-latest")
        super().__init__(name=model_name)
        
        resolved_key = api_key or os.getenv("GEMINI_API_KEY")
        if not resolved_key or resolved_key == "default-fallback-key":
            raise ValueError("GEMINI_API_KEY is not set or invalid.")
            
        self.client = genai.Client(api_key=resolved_key)

    def generate_text(self, prompt: str) -> dict:
       max_retries = 3
       for attempt in range(max_retries):
           try:
               response = self.client.models.generate_content(
                   model=self.name,
                   contents=prompt,
               )
               return {"text": response.text}
           except Exception as e:
            if "503" in str(e) and attempt < max_retries - 1:
                time.sleep(2)
                continue
            raise ModelInferenceError(str(e))
        
