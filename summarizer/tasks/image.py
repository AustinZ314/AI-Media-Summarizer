from PIL import Image, ImageEnhance, ImageFilter
import pytesseract
from transformers import pipeline

def summarize_image(image_path):
    image = Image.open(image_path)

    # Change image dimensions, contrast, reduce noise
    image = image.convert("L")
    enhancer = ImageEnhance.Contrast(image)
    image = enhancer.enhance(2.0)
    image = image.filter(ImageFilter.GaussianBlur(1))
    
    text = pytesseract.image_to_string(image_path)

    summarizer = pipeline('summarization')
    summary = summarizer(text, max_length=150, min_length=50, do_sample=False)

    return summary[0]['summary_text']