FROM python:latest

RUN ["apt-get", "update"]
RUN ["apt-get", "install", "-y", "vim"]

RUN mkdir -p /scrapper


WORKDIR /scrapper

COPY requirements.txt /scrapper

RUN pip install -r requirements.txt

COPY . /scrapper
