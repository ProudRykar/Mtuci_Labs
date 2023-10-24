from fastapi import FastAPI 
from pydantic import BaseModel
import wikipedia
from typing import Optional

app = FastAPI()

class Article(BaseModel):
    title: str

# PATH запрос
@app.get("/article/{title}")
def search_by_path(title: str):
    try:
        data = wikipedia.summary(title, sentences=4)
    except wikipedia.exceptions.DisambiguationError as e:
        data = e.options
    return data

# QUERY запрос
@app.get("/query_search/")
def search_by_query(title: str):
    articles = wikipedia.search(title)
    data = {
        "articles": articles
    }
    return data

# BODY запрос
@app.post("/post_search/")
def search_by_body(article: Article):
    try:
        data = wikipedia.summary(article.title, sentences=4)
    except wikipedia.exceptions.DisambiguationError as e:
        data = e.options
    return data
