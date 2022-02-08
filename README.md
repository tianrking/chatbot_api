# 开箱即用的 chatbot 互动 API

## 目录

- fastapi
  - fastapi_sts ✅
  - fastapi_asr ✅
  - fastapi_tts ✅
  - fastapi_style ❌
  - fastapi_ocr   ❌
  - fastapi_ocr_mm ❌


- golang
  - ...
- nodejs
  - ...

## 注意事项

!!! silk解码务必重新编译
!!! 务必确保软件包与 requirements.txt一致 留意 numpy librosa==0.8.1 

## 请求接口

|  功能   | 接口  | 请求方式 | 功能 | 完成编写 |
|  ----  | ----  | ----  | ----  |----|
| sts  | /sts | get |测试| ✅|
| ...  | /sts/ |get|文字->向量|✅|
| asr  | /api/audio |get|测试|✅|
| ... | /api/audio/ |post |语音->文字|✅|
| tts  | /api/tts |get|测试|✅|
| ... | /api/tts/ |post |文字->语音|✅|
| ... | 
