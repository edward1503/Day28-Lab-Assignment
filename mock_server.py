from fastapi import FastAPI, Request
import uvicorn
import math

app = FastAPI()

@app.post("/v1/chat/completions")
async def chat_completions(request: Request):
    data = await request.json()
    # Dummy response passing the test length > 10 chars
    return {
        "model": "Qwen/Qwen2.5-7B-Instruct-GPTQ-Int4",
        "choices": [
            {
                "message": {
                    "role": "assistant",
                    "content": "This is a mocked answer from our Local Server! Platform engineering is cool."
                }
            }
        ]
    }

@app.post("/embed")
async def embed(request: Request):
    data = await request.json()
    texts = data.get("texts", [])
    # Return 384-dimensional fake embeddings for each text
    embeddings = [[0.1] * 384 for _ in texts]
    return {
        "embeddings": embeddings
    }

@app.get("/health")
def health():
    return {"status": "ok"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8001)
