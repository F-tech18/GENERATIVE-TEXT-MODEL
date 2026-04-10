from fastapi import FastAPI
from pydantic import BaseModel
from generator import TextGenerator
from utils import clean_text

app = FastAPI(title="AI Text Generator")

model = TextGenerator()

class RequestData(BaseModel):
    prompt: str
    max_length: int = 100
    temperature: float = 0.7

@app.post("/generate")
def generate(data: RequestData):
    text = model.generate_text(
        data.prompt,
        data.max_length,
        data.temperature
    )

    cleaned = clean_text(text)

    return {
        "prompt": data.prompt,
        "generated_text": cleaned
    }
