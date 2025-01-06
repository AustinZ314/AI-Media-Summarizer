from PIL import Image, ImageEnhance, ImageFilter
import pytesseract
from transformers import pipeline
from summarizer.utils import clean_text

def summarize_image(image_path):
    image = Image.open(image_path)

    # Change image dimensions, contrast, reduce noise
    image = image.convert("L")
    enhancer = ImageEnhance.Contrast(image)
    image = enhancer.enhance(2.0)
    image = image.filter(ImageFilter.GaussianBlur(1))
    
    text = pytesseract.image_to_string(image)

    summarizer = pipeline('summarization', model="sshleifer/distilbart-cnn-12-6")
    summary = summarizer(text, max_length=200, min_length=50, do_sample=False, truncation=True)

    return summary[0]['summary_text']