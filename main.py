import os
from fastapi import FastAPI
from pydantic import BaseModel
from schemas.transcript_request import TranscriptRequest
from services.summarizer_base import SummarizerBase

# Import summarizers
from services.summarizer_huggingface import HuggingFaceSummarizer
from services.summarizer_openai import OpenAISummarizer



app = FastAPI()

# # Future-proof: If we add more LLMs, we just change this one line
# summarizer = HuggingFaceSummarizer()


def get_summarizer() -> SummarizerBase:
    provider = os.getenv("LLM_PROVIDER", "huggingface").lower()
    if provider == "huggingface":
        return HuggingFaceSummarizer()
    elif provider == "openai":
        return OpenAISummarizer()
    else:
        raise HTTPException(status_code=400, detail=f"Unknown LLM_PROVIDER: {provider}")

summarizer = get_summarizer()

@app.get("/")
async def root():
    return {"message": "Hello World from FastAPI"}


@app.post("/summarize")
async def summarize_transcript(request: TranscriptRequest):
    summary = await summarizer.summarize(request.transcript)
    return {"summary": summary}