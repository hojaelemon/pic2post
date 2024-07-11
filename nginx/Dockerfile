FROM nginx:1.24.0

RUN apt-get -y update && apt-get -y install vim && apt-get clean

RUN rm /etc/nginx/nginx.conf
ADD nginx.conf /etc/nginx/
RUN rm /etc/nginx/conf.d/default.conf
ADD project.conf /etc/nginx/conf.d/