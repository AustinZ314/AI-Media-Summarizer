import requests
from bs4 import BeautifulSoup
from transformers import pipeline
from utils import clean_text

def summarize_article(article_url):
    response = requests.get(article_url)
    if response.status_code != 200:
        raise Exception("Error fetching the article")
    
    page_contents = BeautifulSoup(response.text, 'html.parser')
    tags = ['h1', 'h2', 'h3', 'p', 'article']
    parsed = ''

    # Extract text from relevant elements
    for tag in tags:
        elements = page_contents.find_all(tag)
        for element in elements:
            parsed += element.get_text() + ' '

    text = parsed.strip()
    text = clean_text(text)

    summarizer = pipeline('summarization')
    summary = summarizer(text, max_length=150, min_length=50, do_sample=False)

    return summary[0]['summary_text']