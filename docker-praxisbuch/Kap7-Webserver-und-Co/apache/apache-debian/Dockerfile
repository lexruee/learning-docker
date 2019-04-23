FROM debian:stretch
RUN apt-get update -y && apt-get install -y apache2 \
    && rm -rf /var/lib/apt/lists/*
RUN mkdir -p /var/www/example.com/html \
    && mkdir -p /var/www/example.com/logs
COPY html /var/www/example.com/html
COPY example.com.conf /etc/apache2/sites-available/
RUN a2ensite example.com.conf && a2dissite 000-default.conf

EXPOSE 80
CMD ["/usr/sbin/apache2ctl", "-DFOREGROUND"]