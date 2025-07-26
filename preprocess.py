import fitz
import re

def extract_text_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    text = ""
    for page in doc:
        text += page.get_text()
    return text

def clean_text(text):
    text = re.sub(r'\n+', ' ', text)
    text = re.sub(r'[^\u0980-\u09FFA-Za-z0-9\s.,?!]', ' ', text)
    return text.strip()

def extract_and_clean_text(pdf_path):
    raw = extract_text_from_pdf(pdf_path)
    return clean_text(raw)
