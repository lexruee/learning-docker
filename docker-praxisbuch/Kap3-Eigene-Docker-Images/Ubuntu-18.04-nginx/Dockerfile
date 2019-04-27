FROM ubuntu:18.04
RUN apt-get -y update \
    && apt-get -y install nginx \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]