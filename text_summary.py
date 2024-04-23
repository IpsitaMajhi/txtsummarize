# text_summary.py

from transformers import pipeline

def summarizer(rawdocs):
    
    summarizer = pipeline("summarization", model="KishalayGhoshKIIT/bbc_news_summarization")
    summary=summarizer(text)[0]
    print(summary)
    return "summary"
