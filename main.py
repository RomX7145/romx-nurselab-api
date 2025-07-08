from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import openai
import os

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

openai.api_key = os.getenv("OPENAI_API_KEY")

@app.post("/ask")
async def ask(req: Request):
    body = await req.json()
    question = body.get("message", "")

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a clinical assistant for nurses, midwives, and doctors."},
            {"role": "user", "content": question}
        ]
    )

    reply = response.choices[0].message.content.strip()
    return { "reply": reply }