# Set the base image to Ubuntu
FROM ubuntu:latest
MAINTAINER Maintaner Name

# Update the repository
#RUN apt-get update

# Install necessary tools
RUN apt-get install -y curl

# Download and Install Nginx
RUN apt-get install -y nginx 

#ADD index.html /var/www/
ADD mime_types /etc/nginx/
#ADD querycalc.js /var/www/static/
#ADD base.css /var/www/

# Remove the default Nginx configuration file
RUN rm -v /etc/nginx/nginx.conf

# Copy a configuration file from the current directory
ADD nginx.conf /etc/nginx/nginx.conf

EXPOSE 80

# Set the default command to execute
# when creating a new container
CMD nginx
