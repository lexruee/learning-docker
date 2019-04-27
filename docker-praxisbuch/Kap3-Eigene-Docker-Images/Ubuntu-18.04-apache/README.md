# Ubuntu 18.04 Apache - Beispiel Dockerfile

## Building

``` 
docker build -t ubuntu-apache .
```

## Running

``` 
docker run -it --rm -p 8080:80 -d ubuntu-apache
```