FROM ubuntu:latest
MAINTAINER cazza/caroline

RUN apt-get install -y curl nginx  

#ADD index.html /var/www/
ADD mime_types /etc/nginx/
#ADD querycalc.js /var/www/static/
#ADD base.css /var/www/
RUN rm -v /etc/nginx/nginx.conf
ADD nginx.conf /etc/nginx/nginx.conf
ADD base.css /var/www/base.css
ADD index.html /var/www/index.html

EXPOSE 90
CMD nginx

