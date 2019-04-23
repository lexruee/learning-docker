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