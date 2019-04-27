FROM ubuntu:18.04
RUN apt-get -y update \
    && apt-get -y install apache2 \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*
EXPOSE 80
CMD ["apache2ctl", "-DFOREGROUND"]
