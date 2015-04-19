FROM ubuntu:latest
MAINTAINER cazza/Carolin

RUN apt-get update
RUN apt-get install -y python python-dev python-distribute python-pip python-pymongo
RUN mkdir /project
#ADD requirements.txt /project/requirements.txt
RUN pip install simplejson
RUN pip install -U flask-cors
WORKDIR /project
RUN pip install -r requirements.txt
EXPOSE 8000
CMD python cpyserver.py
