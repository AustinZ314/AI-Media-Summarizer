from pdf2image import convert_from_path
from transformers import pipeline

def summarize_pdf(pdf_path):
    images = convert_from_path(pdf_path)
    text = ""
    for image in images:
        text += pytesseract.image_to_string(image)

    summarizer = pipeline('summarization')
    summary = summarizer(text, max_length=150, min_length=50, do_sample=False)

    return summary[0]['summary_text']