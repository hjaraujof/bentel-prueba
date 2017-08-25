FROM python:3.6

MAINTAINER Harold Araujo "haroldj.araujof@gmail.com"

ENV PYTHONUNBUFFERED 1

RUN git clone https://github.com/hjaraujof/bentel-prueba.git bentel
RUN pip install -Ur bentel/requirements/production.txt 

RUN python bentel/manage.py migrate

#RUN python manage.py loaddata data/dummped.json

#docker-machine start default #starting docker virtual machine named default

#docker build -t bentel . #building docker image from the Docker file
#docker run -d -p 8000:8000 bentel #running the newly build docker image

#api=$(docker-machine ip default) #returns in which IP docker-machine is running
#curl $api:8000/cocineros/?format=json | json_pp