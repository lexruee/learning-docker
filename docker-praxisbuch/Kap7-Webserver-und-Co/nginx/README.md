# nginx

## Beispiel mit Alpine Linux

```
docker build -t nginx-alpine .
``` 

``` 
docker run -it -p 8080:80 --name nginx-alpine-test --rm -d nginx-alpine
docker ps
docker stop nginx-alpine-test
```

## Beispiel mit Debian Stretch

```
docker build -t nginx-debian .
``` 

``` 
docker run -it -p 8080:80 --name nginx-debian-test --rm -d nginx-debian
docker ps
docker stop nginx-debian-test
```
