FROM debian:stretch
RUN apt-get -y update && apt-get -y install nginx \
    && rm -rf /var/lib/apt/lists/*
COPY html/ /var/www/html
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
