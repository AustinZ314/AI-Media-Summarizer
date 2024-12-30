import requests
from transformers import pipeline

def summarize_article(article_url):
    response = requests.get(article_url)
    if response.status_code != 200:
        raise Exception("Error fetching the article.")
    
    text = response.text[:10000] 

    summarizer = pipeline('summarization')
    summary = summarizer(text, max_length=150, min_length=50, do_sample=False)

    return summary[0]['summary_text']