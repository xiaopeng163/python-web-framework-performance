FROM python:3.11-slim-buster

LABEL maintainer="Peng Xiao<xiaoquwl@gmail.com>"

COPY . /

RUN pip install -r requirements.txt

ENTRYPOINT ["/run_server.sh"]