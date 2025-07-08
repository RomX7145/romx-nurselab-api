# RomX Nurselab AI Backend

This is a FastAPI backend for the RomX Nurselab AI Chrome Extension. It accepts POST requests with a question and responds with an AI-generated answer using OpenAI's API.

## Endpoint

POST `/ask`  
Body: `{ "message": "your question here" }`  
Response: `{ "reply": "AI answer" }`

## Deploy on Render

Use the following:

- Build Command: `pip install -r requirements.txt`
- Start Command: `uvicorn main:app --host 0.0.0.0 --port 10000`
- Add Env Variable: `OPENAI_API_KEY`