from fastapi import FastAPI
from starlette.responses import FileResponse


app = FastAPI(name="monitor")


@app.get("/download")
async def download():
    # 处理完毕文件以后，生成了文件路径
    filename = "/storage/lol/test/fastapi/Juzibot_tts/output.wav"
    return FileResponse(
            filename,  # 这里的文件名是你要发送的文件名
            filename="a.wav", # 这里的文件名是你要给用户展示的下载的文件名，比如我这里叫lol.exe
        )