FROM ubuntu:latest

LABEL maintainer="tian.r.king@gmail.com"
LABEL version="v0.1"

RUN apt-get update && apt-get upgrade -y
RUN apt install python3.9
RUN pip install fastapi
RUN pip install "uvicorn[standard]"
RUN pip install opensearch-py

ENV FLASK_HOST=0.0.0.0
ENV FLASK_PORT=51234
ENV FLASK_RES=fast_test
ENV FLASK_ROUTE=app

EXPOSE 51234
CMD uvicorn FLASK_RES:FLASK_ROUTE --reload --host FLASK_HOST --port FLASK_PORT