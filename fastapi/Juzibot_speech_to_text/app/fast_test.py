from typing import Optional
from fastapi import FastAPI , Form
from typing import Optional
from pydantic import BaseModel
import base64
import os
from pydub import AudioSegment
app = FastAPI()

@app.get("/api/audio")
async def audio_help():
    return "send_audio"

class Item_audio(BaseModel):
    lol: Optional[str] = None
    audio_name: Optional[str] = None
    audio_data: Optional[str] = None

@app.post("/api/audio/")
async def create_item(item: Item_audio):
   
    gg=item.audio_data.replace("data:audio/silk;base64,","")
    print(gg)
    audio_data = base64.b64decode(str(gg))
    # fout = open(item.audio_name+".silk",'wb')
    print("AA\n")
    dir = "/code/"+item.audio_name+".silk"
    fout = open(dir,'wb')
    fout.write(audio_data)
    fout.close()
    print("BB\n")
    os.system("bash ./converter.sh "+dir+" mid.mp3")
    
    print("CC\n")
    song = AudioSegment.from_mp3(dir+".mid.mp3")
    song.export(item.audio_name+".wav", format="wav")

    import paddle
    from paddlespeech.cli import ASRExecutor

    asr_executor = ASRExecutor()
    text = asr_executor(
        model='conformer_wenetspeech',
        lang='zh',
        sample_rate=16000,
        config=None,  # Set `config` and `ckpt_path` to None to use pretrained model.
        ckpt_path=None,
        audio_file=item.audio_name+".wav",
        force_yes=True,
        device=paddle.get_device())
    print('ASR Result: \n{}'.format(text)
    )
    return text
