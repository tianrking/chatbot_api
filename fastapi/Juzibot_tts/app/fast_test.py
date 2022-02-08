from typing import Optional
from fastapi import FastAPI , Form
from typing import Optional
from pydantic import BaseModel
import base64
import os
import paddle
from paddlespeech.cli import TTSExecutor
app = FastAPI()

@app.get("/")
async def API_Server():
    return "API server is running on /api"

@app.get("/api")
async def API_help():
    return "API server is running on /api/style"   

@app.get("/api/tts")
async def audio_help():
    return "send message to get speech "

class Item_tts(BaseModel):
    lol: Optional[str] = None
    tts_data: Optional[str] = None

@app.post("/api/tts/")
async def create_item(item: Item_tts):
    # tts_data=item.tts_data.replace("data:tts/message;base64,","")
    # pic_data = base64.b64decode(str(gg))
    output_dir ='output.wav'
    tts_executor = TTSExecutor()
    wav_file = tts_executor(
    text='今天的天气不错啊',
    output= output_dir,
    am='fastspeech2_csmsc',
    am_config=None,
    am_ckpt=None,
    am_stat=None,
    spk_id=0,
    phones_dict=None,
    tones_dict=None,
    speaker_dict=None,
    voc='pwgan_csmsc',
    voc_config=None,
    voc_ckpt=None,
    voc_stat=None,
    lang='zh',
    device=paddle.get_device())
    print('Wave file has been generated: {}'.format(wav_file))

    wav_data = base64.b64encode(output_dir)
    pic_data = base64.b64decode(wav_data)
    fout = open(("aa.wav"),'wb')
    fout.write(pic_data)
    fout.close()  # right
    print(item.tts_data)
    return item.pic_name
