# text_summary.py

from transformers import pipeline

def summarizer(rawdocs):
    
    summarizer = pipeline("summarization", model="KishalayGhoshKIIT/bbc_news_summarization")
    summary=summarizer(text)[0]
    print(summary)
    return "summary"



# txtsummarize
 The objective of this project is to implement a Deep Reinforcement Learning based system for text summarization and question answering. Given a source text document or chat history, the system should perform the following tasks:

Text Summarization: Generate a concise and coherent summary of the input text, capturing the essential information.

Web or Mobile Application: Develop a user-friendly application.

Approach Used : Transformers 
Models Used ; Hugging Face
gopalkalpande/bbc-news-summary

Content This dataset for extractive text summarization has four hundred and seventeen political news articles of BBC from 2004 to 2005 in the News Articles folder. For each articles, five summaries are provided in the Summaries folder. The first clause of the text of articles is the respective title
