FROM ubuntu:latest
MAINTAINER cazza/Carolin

RUN apt-get update
RUN apt-get install -y openssh-server
RUN mkdir /var/run/sshd

RUN adduser jenkins
CMD /usr/sbin/sshd


