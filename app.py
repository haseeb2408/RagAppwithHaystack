from fastapi import FastAPI , Request , Form , Response
from fastapi.templating import Jinja2Templates
from fastapi.encoders import jsonable_encoder
import uvicorn
from fastapi import FastAPI
import json
import os
from dotenv import load_dotenv



app = FastAPI()
templates = Jinja2Templates(directory='templates')


@app.get('/')
async def index(request : Request):
    return templates.TemplateResponse("index.html" , {"request" : request})

@app.post("/post_answer")
async def get_answer(request : Request , questions : str=Form(...)):
    pass    

if __name__ == '__main':
    uvicorn.run(app)