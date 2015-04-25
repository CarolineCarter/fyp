FROM ubuntu:latest
MAINTAINER cazza/Caroline

RUN apt-get update
RUN apt-get install -y python python-dev python-distribute python-pip python-pymongo
RUN mkdir /project
RUN pip install simplejson
RUN pip install -U flask-cors
ADD requirements.txt /project/requirements.txt
WORKDIR /project
RUN pip install -r requirements.txt
EXPOSE 8000
CMD python app.py

