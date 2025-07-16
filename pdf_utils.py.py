from PyPDF2 import PdfReader
import io

def extract_text_from_pdf(pdf_bytes):
    text = ""
    reader = PdfReader(io.BytesIO(pdf_bytes))
    for page in reader.pages:
        text += page.extract_text()
    return text
