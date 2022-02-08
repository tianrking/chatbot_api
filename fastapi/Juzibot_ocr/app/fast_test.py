from typing import Optional
from fastapi import FastAPI , Form
from typing import Optional
from pydantic import BaseModel
import base64
import os
import paddle
app = FastAPI()

@app.get("/api/ocr")
async def audio_help():
    return "send pic to get text "

class Item_ocr(BaseModel):
    lol: Optional[str] = None
    pic_name: Optional[str] = None
    pic_data: Optional[str] = None

@app.post("/api/ocr/")
async def create_item(item: Item_ocr):
   return "todo"