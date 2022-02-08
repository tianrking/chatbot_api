from typing import Optional
from fastapi import FastAPI , Form
from typing import Optional
from pydantic import BaseModel
import base64
import os
import paddle
app = FastAPI()

@app.get("/")
async def API_Server():
    return "API server is running on /api"

@app.get("/api")
async def API_help():
    return "API server is running on /api/style"   

@app.get("/api/style")
async def audio_help():
    return "send pic to get awesome style "

class Item_style(BaseModel):
    lol: Optional[str] = None
    pic_name: Optional[str] = None
    pic_data: Optional[str] = None

@app.post("/api/style/")
async def create_item(item: Item_style):
    gg=item.pic_data.replace("data:image/jpg;base64,","")
    pic_data = base64.b64decode(str(gg))
    print(gg)
    fout = open(item.pic_name,'wb')
    fout.write(pic_data)
    fout.close()
    
    print(item.lol)
    return item.pic_name