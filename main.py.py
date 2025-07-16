from fastapi import FastAPI, File, UploadFile, Form, HTTPException
from utils.pdf_utils import extract_text_from_pdf
from utils.openai_utils import ask_medical_question

app = FastAPI()

@app.post("/ask/")
async def ask_question_from_pdf(
    question: str = Form(...),
    file: UploadFile = File(...)
):
    try:
        contents = await file.read()
        pdf_text = extract_text_from_pdf(contents)

        if not pdf_text.strip():
            raise HTTPException(status_code=400, detail="No readable text found in PDF.")

        answer = ask_medical_question(question, pdf_text)
        return {"answer": answer}
@app.post("/ask")
def ask_question(request: QueryRequest):
    # Your logic here
    return {"answer": "This is a response"}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
from fastapi import FastAPI, Request, UploadFile, File, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

# Serve static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# Jinja2 templates
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def read_index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi import FastAPI, Request

app = FastAPI()

# Serve static files (JS, CSS, icons, etc.)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Set up template rendering
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def serve_home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})
