from fastapi import FastAPI
import pyjokes
from pydantic import BaseModel
import wikipedia
from typing import Optional

app = FastAPI()

class Joke(BaseModel):
    friend: str
    joke: str

class JokeInput(BaseModel):
    friend: str

@app.post("/", response_model=Joke)
def create_joke(joke_input: JokeInput):
    """Создание шутки"""
    return Joke(friend=joke_input.friend, joke=pyjokes.get_joke())

# Роут для получения шутки от друга
@app.get("/{friend}", response_model=Joke)
def friends_joke(friend: str):
    return friend + " tells his joke: " + pyjokes.get_joke()

# Роут для получения нескольких шуток от друга
@app.get("/multi/{friend}")
def multi_friends_joke(friend: str, jokes_number: int):
    result = ""
    for i in range(jokes_number):
        result += friend + f" tells his joke #{i + 1}: " + pyjokes.get_joke() + " "
    return result
