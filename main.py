from typing import Union

from fastapi import FastAPI

import barkServer


app = FastAPI()


@app.post("/voice")
def read_prompt(prompt: str, gender: str):
    barkServer.createVoice("this is test input voice")
    return "done"

@app.get("/voice")
def get_prompt(prompt):
    with open ("./files/"+ prompt) as file:
        return file
    
