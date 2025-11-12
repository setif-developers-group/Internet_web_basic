from fastapi import FastAPI
import random
from pydantic import BaseModel

class RandomInt(BaseModel):
    value:int

class Comment(BaseModel):
    name:str
    comment:str
    rating:int
app = FastAPI()


@app.get('/')
def root():
    return {'hello':'world'}

@app.get('/random')
def random_val()->RandomInt:
    i = random.randint()
    r = RandomInt(value=i)
    return r

@app.post('/comment')
def comment_fun(comment:Comment)->None:
    print(f'name: {comment.name}, \t comment: {comment.comment}, \t {comment.rating}')
    return