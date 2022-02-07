# FROM python:3.9
FROM ubuntu
LABEL maintainer="tian.r.king@gmail.com"
LABEL version="v0.1"
WORKDIR /code
# 
COPY ./requirements.txt /code/requirements.txt


#
RUN sed -i s/archive.ubuntu.com/mirrors.aliyun.com/g /etc/apt/sources.list && sed -i s/security.ubuntu.com/mirrors.aliyun.com/g /etc/apt/sources.list


RUN apt-get update && apt-get install ffmpeg -y
RUN apt-get install python -y  && apt-get install python3-pip -y
#RUN /usr/local/bin/python -m pip install --upgrade pip
RUN pip config set global.index-url http://mirrors.aliyun.com/pypi/simple
RUN pip config set install.trusted-host mirrors.aliyun.com
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
RUN echo "Make sure Fastapi is installed:"
# 
COPY ./app /code/app

# 
CMD ["uvicorn", "app.fast_test:app", "--host", "0.0.0.0", "--port", "19912"]
