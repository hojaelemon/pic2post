# Dockerfile
FROM python:3.11

RUN mkdir /server
COPY ./server /server
WORKDIR /server

RUN pip install --upgrade pip
RUN pip install -r requirements.txt