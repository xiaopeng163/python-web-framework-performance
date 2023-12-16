FROM python:3.11-slim-buster

LABEL maintainer="Peng Xiao<xiaoquwl@gmail.com>"

COPY . /

RUN pip install -r requirements.txt

ENTRYPOINT ["sh", "/run_server.sh"]