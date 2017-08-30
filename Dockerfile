FROM python:3.6

MAINTAINER Harold Araujo "haroldj.araujof@gmail.com"

ENV PYTHONUNBUFFERED 1

RUN pip install -Ur requirements/production.txt
