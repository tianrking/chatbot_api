from typing import Optional
from fastapi import FastAPI , Form
from opensearchpy import OpenSearch
from sentence_transformers import SentenceTransformer, util
from typing import Optional
from pydantic import BaseModel
import base64
import cv2
import os


app = FastAPI()

model = SentenceTransformer('all-roberta-large-v1')

# host = 'localhost'
# port = 9200
# auth = ('admin', 'admin')

# client = OpenSearch(
#     hosts = [{'host': host, 'port': port}],
#     http_compress = True, # enables gzip compression for request bodies
#     http_auth = auth,
#     # client_cert = client_cert_path,
#     # client_key = client_key_path,
#     use_ssl = True,
#     verify_certs = True,
#     ssl_assert_hostname = False,
#     ssl_show_warn = False,
#     # ca_certs = ca_certs_path
# )

@app.get("/sts")
async def sts_help():
    return "send_data"

@app.get("/sts/{_text}")
async def read_sentence(_text):
    embedding = model.encode(_text, convert_to_tensor=True)
    # # Add a document to the index.
    # document = {
    # 'text': _text,
    # 'embedding': embedding,   
    # }
    # response = client.index(
    #     index = "xiaojuzi",
    #     body = document,
    #     # id = id,
    #     # refresh = True
    # )

    print(embedding)
    return {"txt": _text,"embedding":embedding.tolist()}


class Item(BaseModel):
    a: str
    # name: str
    # description: Optional[str] = None
    # price: float
    # tax: Optional[float] = None
    
    
    

@app.get("/sts_post/")
async def read_sentence_post(item: Item):
    print("recieve\n")
    _text = item
    print(item)
    embedding = model.encode(_text, convert_to_tensor=True)
    print(embedding)

    #return {"txt": _text,"embedding":embedding.tolist()


# class Item(BaseModel):
#     name: str
#     # description: Optional[str] = None
#     # price: float
#     # tax: Optional[float] = None

# def Base64ToFile(txt,file):
#     with open(txt,'rb') as fileOBJ:
#         base64_data = fileOBJ.read()
#         file_data = base64.b64enode(base64_data)
#         fout = open(file,'wb')
#         fout.write(file_data)
#         fout.close()

class Item(BaseModel):
    aaa: Optional[str] = "value"
    bbb: Optional[float] = None
    imgg: Optional[str] = "value"

@app.post("/ttt/")
async def create_item(item: Item):
   
    gg=item.imgg.replace("data:image/gif;base64,","")
    file_data = base64.b64decode(str(gg))
    fout = open("gg.png",'wb')
    fout.write(file_data)
    fout.close()
    return gg

class Item(BaseModel):
    field: str = "value"

@app.post("/items/")
async def create_item(item: Item):
    return item.dict(exclude_unset=True)

class Item_audio(BaseModel):
    aaa: Optional[str] = None
    bbb: Optional[float] = None
    audio: Optional[str] = None

@app.post("/api/audio/")
async def create_item(item: Item_audio):
   
    gg=item.audio.replace("data:audio/silk;base64,","")
    print(gg)
    audio_data = base64.b64decode(str(gg))
    fout = open("test.silk",'wb')
    fout.write(audio_data)
    fout.close()
    os.system("bash ./silk-v3-decoder/converter.sh "+"/storage/lol/test/fastapi/test.silk"+" aaa.mp3")
    
    from pydub import AudioSegment
    song = AudioSegment.from_mp3("/storage/lol/test/fastapi/test.aaa.mp3")
    song.export("test.wav", format="wav")

    import paddle
    from paddlespeech.cli import ASRExecutor

    asr_executor = ASRExecutor()
    text = asr_executor(
        model='conformer_wenetspeech',
        lang='zh',
        sample_rate=16000,
        config=None,  # Set `config` and `ckpt_path` to None to use pretrained model.
        ckpt_path=None,
        audio_file='/storage/lol/test/fastapi/test.wav',
        force_yes=True,
        device=paddle.get_device())
    print('ASR Result: \n{}'.format(text)
    )

    # file_data = base64.b64decode(str(gg))
    # fout = open("gg.png",'wb')
    # fout.write(file_data)
    # fout.close()
    return str("recieve")