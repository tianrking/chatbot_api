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
    return "API server is running on /api/tts"   

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

    tts_data = base64.b64decode(str(item.tts_data)).decode('utf-8')
    # print(tts_data)
    output_dir ='output.wav'
    tts_executor = TTSExecutor()
    wav_file = tts_executor(
    text= tts_data,
    output='output.wav',
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
    
    base64_data = '' 
    with open(output_dir, 'rb') as fileObj:
        wav_data = fileObj.read()
        base64_data = base64.b64encode(wav_data)

    print(tts_data)
    return base64_data

# def ToBase64(file, txt):
#     with open(file, 'rb') as fileObj:
#         image_data = fileObj.read()
#         base64_data = base64.b64encode(image_data)
#         fout = open(txt, 'w')
#         fout.write(base64_data.decode())
#         fout.close()


# def ToFile(txt, file):
#     with open(txt, 'r') as fileObj:
#         base64_data = fileObj.read()
#         ori_image_data = base64.b64decode(base64_data)
#         fout = open(file, 'wb')
#         fout.write(ori_image_data)
#         fout.close()
