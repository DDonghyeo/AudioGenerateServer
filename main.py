from typing import Union
from fastapi import FastAPI
from fastapi.responses import FileResponse

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
    

@app.post("/voice/file")
def get_voice_file(fileName:str, gender:str):
    return FileResponse("/files/" + fileName + "_" + gender + ".wav")
