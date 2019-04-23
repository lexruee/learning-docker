# Apache Webserver

## Beispiel: Apache Container starten

``` 
docker run -it -p 8080:80 --rm --name apache \
    -v /home/xander/docker/apache/:/usr/local/bin/apache2/htdocs/ \
    httpd:2.4
```


## Beispiel: Mit Alpine Linux und eigenem Dockerfile

``` 
cd apache-alpine
docker build -t apache-alpine .
docker run -it -p 8080:80 apache-alpine
```

``` 
docker run -it -p 8080:80 -d --rm --name apache-test apache-alpine
docker ps
docker stop apache-test
```

## Beispiel: Mit Debian Stretch und eigenem Dockerfile

``` 
cd apache-debian
docker build -t apache-debian .
docker run -it -p 8080:80 --name apache-debian-test --rm -d apache-debian
docker ps
docker stop apache-debian-test
```