FROM ubuntu:latest
MAINTAINER cazza/caroline

RUN apt-get install -y curl nginx  


ADD mime_types /etc/nginx/
ADD querycalc.js /var/www/
#ADD base.css /var/www/
RUN rm -v /etc/nginx/nginx.conf
ADD nginx.conf /etc/nginx/nginx.conf
ADD base.css /var/www/
ADD index.html /var/www/

EXPOSE 90
CMD nginx

