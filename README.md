## 📌 Project Overview

This project is a **FastAPI-based backend** focused on **AI-powered processing** of YouTube video transcripts.  
It will receive transcripts (already extracted by an existing Flask API) and provide intelligent features such as **summarization** and **interactive Q&A**.

---

### 🎯 Goal
To build a backend service that:
1. **Summarizes transcripts** of YouTube videos into easy-to-read formats.
2. **Provides AI chat** so users can ask questions and get accurate answers based on the video’s transcript.

---

### 🔑 Core Features

#### **1. Transcript Summarization**
- Accept full transcripts as input.
- Use AI models to produce:
  - **Concise bullet-point summaries** for quick understanding.
  - **Detailed paragraph summaries** for deeper context.
- Handle long transcripts by breaking them into manageable chunks.

#### **2. AI Q&A Chat**
- Allow users to ask questions about a video’s content.
- Retrieve relevant transcript sections and generate context-aware answers.
- Use Retrieval-Augmented Generation (RAG) for improved accuracy.

---

### 🏗 Tech Stack
- **Framework:** FastAPI (Python)
- **Server:** Uvicorn
- **AI Processing:** OpenAI API (or similar LLM provider)
- **Containerization:** Docker

---

By the end of development, this FastAPI backend will:
- Take transcripts from our existing transcript extraction service.
- Generate high-quality AI summaries.
- Provide an AI-driven chat interface for interactive Q&A based on the video’s content.

---

# Minimal FastAPI Project (Hello World)

This project is a minimal **FastAPI** application running inside Docker.  
It exposes a single endpoint that returns a `Hello World` message and includes automatic API documentation.

---

## 📂 Project Structure
```
├── Dockerfile
├── main.py
└── requirements.txt
└── README.md
````

## 🚀 Steps to Create & Run

### 1. Create `requirements.txt`
```txt
fastapi
uvicorn[standard]
````

### 2. Create `main.py`

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World from FastAPI"}
```

### 3. Create `Dockerfile`

```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

---

## 🛠 Build & Run (Docker)

```bash
# Build the Docker image
docker build -t fastapi-hello .

# Run the container
docker run -d -p 8000:8000 fastapi-hello
```

---

## 🌐 Test the API

Open in browser:

```
http://localhost:8000
```

Or via curl:

```bash
curl http://localhost:8000
```

Response:

```json
{"message":"Hello World from FastAPI"}
```

---

## 📄 API Documentation (Auto-generated)

FastAPI provides interactive API docs automatically:

* Swagger UI → [http://localhost:8000/docs](http://localhost:8000/docs)
* ReDoc → [http://localhost:8000/redoc](http://localhost:8000/redoc)

---

## 📌 Overview

* **Framework:** FastAPI (modern, async-first Python web framework)
* **Server:** Uvicorn (ASGI server for FastAPI)
* **Containerized:** Yes, using Docker
* **Purpose:** Serve as a minimal starting point for building APIs with FastAPI
* **Key Feature:** Out-of-the-box automatic OpenAPI documentation



> # AI Summarization API Integration

## What We Have Implemented

We developed a new FastAPI endpoint `/summarize` that:

- Accepts a **YouTube video transcript** as input in JSON format.
- Returns an AI-generated **summary** of the transcript.

## Modular LLM Integration

To keep the system flexible and future-proof, the summarization logic is modular and supports multiple LLM providers.  

Currently supported providers:

- **OpenAI**  
  - Uses the latest OpenAI Python SDK (v1.x).  
  - Summarizes transcripts by sending prompts to GPT-3.5 or GPT-4 models.  
  - Requires an OpenAI API key configured via environment variables.

- **Hugging Face Inference API**  
  - Uses the `facebook/bart-large-cnn` summarization model.  
  - Calls Hugging Face's public API with an API token.  
  - Free tier available with some usage limits.

## How It Works

- The API endpoint accepts a POST request with a JSON body containing the `transcript` text.  
- Based on the configured provider (`LLM_PROVIDER` environment variable), it forwards the transcript to the selected summarizer implementation.  
- The summarizer calls the corresponding LLM API to generate and return a concise summary.

## Configuration

- Environment variables control API keys and provider selection:

```env
OPENAI_API_KEY=your_openai_key
HF_API_TOKEN=your_huggingface_token
LLM_PROVIDER=huggingface  # or "openai"
OPENAI_MODEL=gpt-3.5-turbo
````
## Usage Example

Request:

```http
POST /summarize
Content-Type: application/json

{
  "transcript": "Long YouTube transcript text..."
}
```

Response:

```json
{
  "summary": "Concise AI-generated summary of the transcript."
}
```

This setup allows easy addition of new LLM providers without modifying the API endpoint or request handling code — just add a new summarizer module and update configuration.

