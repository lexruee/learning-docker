FROM alpine:3.9.3
RUN apk add --update --no-cache nginx
RUN mkdir /run/nginx
COPY default.conf /etc/nginx/conf.d/default.conf
COPY html/ /var/www/html
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
