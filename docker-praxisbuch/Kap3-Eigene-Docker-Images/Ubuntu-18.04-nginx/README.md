# Ubuntu 18.04 - Beispiel Dockerfile

## Building

``` 
docker build -t ubuntu-nginx .
```

## Running

``` 
docker run -it --rm -p 8080:80 -d ubuntu-nginx
```