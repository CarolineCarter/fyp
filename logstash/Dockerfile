FROM ubuntu:latest

RUN apt-get update -qq 
RUN apt-get install -y -qq wget python oracle-java7-installer
RUN echo 'deb http://packages.elasticsearch.org/logstash/1.4/debian stable main' | sudo tee /etc/apt/sources.list.d/logstash.list
RUN apt-get install logstash=1.4.2-1-2c0f5a1
WORKDIR /opt
