from transformers import pipeline
import re

t5 = pipeline('text2text-generation', model='t5-small')

def clean_text(text):
    text = re.sub(r'\[\d{1,2}:\d{2}(:\d{2})?\]', '', text)  # Remove timestamps from video subtitles
    text = re.sub(r'[^\w\s.,!?\'-]', '', text)              # Remove special characters
    prompt = "Clean and refine this text to improve clarity and grammar: " + text
    
    try:
        #result = t5(prompt)
        return t5(prompt)[0]['generated_text']
    except Exception as e:
        print(f"Error: {e}")
        return ""