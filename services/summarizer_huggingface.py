import os
import requests
from .summarizer_base import SummarizerBase

class HuggingFaceSummarizer(SummarizerBase):
    def __init__(self):
        self.api_token = os.getenv("HUGGING_FACE_API_KEY")
        self.api_url = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"
        self.headers = {"Authorization": f"Bearer {self.api_token}"}

    async def summarize(self, transcript: str) -> str:
        payload = {"inputs": transcript}
        response = requests.post(self.api_url, headers=self.headers, json=payload)
        response.raise_for_status()
        data = response.json()

        # The HF summarization API returns a list of summaries
        if isinstance(data, list) and "summary_text" in data[0]:
            return data[0]["summary_text"]
        else:
            return "Summary not available."
