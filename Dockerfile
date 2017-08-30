FROM python:3.6

MAINTAINER Harold Araujo "haroldj.araujof@gmail.com"

ENV PYTHONUNBUFFERED 1

RUN git clone https://github.com/hjaraujof/bentel-prueba.git bentel

RUN pip install -Ur bentel/requirements/production.txt

WORKDIR /bentel

