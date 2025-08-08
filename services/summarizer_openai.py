import os
from openai import OpenAI
from .summarizer_base import SummarizerBase

class OpenAISummarizer(SummarizerBase):
    def __init__(self):
        self.client = OpenAI()

    async def summarize(self, transcript: str) -> str:
        prompt = f"Summarize the following transcript:\n\n{transcript}"
        response = self.client.chat.completions.create(
            model=os.getenv("OPENAI_MODEL", "gpt-3.5-turbo"),
            messages=[
                {"role": "system", "content": "You are a helpful assistant that creates concise summaries."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=200
        )
        return response.choices[0].message.content.strip()
