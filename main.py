from typing import Optional
from fastapi import FastAPI
import run_summarization_ja
from pydantic import BaseModel

app = FastAPI()

class Body(BaseModel):
    text: str

@app.post("/summarization")
async def summarization(body: Body):
    result = run_summarization_ja.summarization(body.text)
    return {"result": result}
