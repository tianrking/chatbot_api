## 目录

- fastapi
  - fastapi_sts
  - fastapi_asr

## 注意事项

!!! silk解码务必重新编译
!!! 务必确保软件包与 requirements.txt一致 留意 numpy librosa==0.8.1 

## 请求接口

### sts

/sts        测试
/sts/{data} 文字向量

### asr

/api/audio   测试
/api/audio/  post 语音-> 文字

### tts

/api/tts   测试
/api/tts/  文字->语音
