from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel

from models import *


app = FastAPI()


@app.get("/posts")
def get_posts():
    return {"posts": "There would be some posts from db"}


@app.post("/posts")
def create_post(post: Post):
    return {"data": post}


@app.put("/posts")
def update_post():
    pass


@app.delete("/posts")
def delete_post():
    pass

