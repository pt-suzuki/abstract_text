from typing import Optional
from fastapi import FastAPI
import run_summarization_ja
from pydantic import BaseModel
from agraffe import Agraffe, Service

app = FastAPI()

class Body(BaseModel):
    text: str

@app.post("/summarization")
async def summarization(body: Body):
    result = run_summarization_ja.summarization(body.text)
    return {"result": result}

entry_point = Agraffe.entry_point(app, Service.google_cloud_functions)
