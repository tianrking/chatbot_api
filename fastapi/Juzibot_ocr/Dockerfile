FROM ubuntu
LABEL maintainer="tian.r.king@gmail.com"
LABEL author="w0x7ce"
LABEL version="v0.1"
WORKDIR /code
# 
COPY ./requirements.txt /code/requirements.txt
#
RUN sed -i s/archive.ubuntu.com/mirrors.aliyun.com/g /etc/apt/sources.list && sed -i s/security.ubuntu.com/mirrors.aliyun.com/g /etc/apt/sources.list

RUN apt-get update && apt-get install ffmpeg -y
RUN apt-get install python -y  && apt-get install python3-pip -y
RUN pip install paddlepaddle==2.2.2 -i https://mirror.baidu.com/pypi/simple && \
    pip install paddleocr -i https://pypi.tuna.tsinghua.edu.cn/simple && \
    pip3 install -U https://paddleocr.bj.bcebos.com/whl/layoutparser-0.0.0-py3-none-any.whl 
# 面板分析

RUN pip config set global.index-url http://mirrors.aliyun.com/pypi/simple
RUN pip config set install.trusted-host mirrors.aliyun.com
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
RUN echo "Make sure Fastapi is installed:"
# 
COPY ./app /code/app
# 
RUN echo "EXPOSE PORT 81 "
CMD ["uvicorn", "app.fast_test:app", "--host", "0.0.0.0", "--port", "81"]

