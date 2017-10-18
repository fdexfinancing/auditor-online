FROM python:latest

RUN mkdir -p /scrapper

WORKDIR /scrapper

COPY requirements.txt /scrapper

RUN pip install -r requirements.txt

COPY . /scrapper
