from typing import Union
from fastapi import FastAPI
from fastapi.responses import FileResponse

import barkServer


app = FastAPI()


@app.post("/voice/create")
def read_prompt(prompt: str, gender: str):
    barkServer.createVoice(prompt, gender)
    return "done"    

@app.get("/voice/get")
def get_voice_file(prompt:str, gender:str):
    return FileResponse("files/" + prompt + "_" + gender + ".wav")
