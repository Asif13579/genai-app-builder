from fastapi import FastAPI
from .schemas import GenerateRequest,GeneratedApplication
from .llm import OpenAIProvider

app=FastAPI(title="GenAI Application Builder",version="0.1.0")

provider=OpenAIProvider()

@app.get("/")
async def root():
    return {
        "message": "GenAI Application Builder is running"
    }

@app.post("/generate",response_model=GeneratedApplication)
async def generate(request:GenerateRequest):
    result=await provider.generate(request)
    return result

