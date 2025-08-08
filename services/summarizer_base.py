from abc import ABC, abstractmethod

class SummarizerBase(ABC):
    @abstractmethod
    async def summarize(self, transcript: str) -> str:
        """Summarize the transcript."""
        pass
