import fitz     # PyMuPDF
import pytesseract
from PIL import Image
from transformers import pipeline
import io
from utils import clean_text

def summarize_pdf(pdf_path):
    pdf = fitz.open(pdf_path)

    # Check if there's selectable text
    text = ""
    for page_ind in range(pdf.page_count):
        page = pdf.load_page(page_ind)
        text += page.get_text("text")
    
    # If the PDF is all images, extract text
    if not text.strip():
        text = ""
        for page_ind in range(pdf.page_count):
            page = pdf.load_page(page_ind)
            pixmap = page.get_pixmap()
            image = Image.open(io.BytesIO(pixmap.tobytes()))
            text += pytesseract.image_to_string(image)

    text = clean_text(text)
    summarizer = pipeline('summarization')
    summary = summarizer(text, max_length=150, min_length=50, do_sample=False)
    
    return summary[0]['summary_text']