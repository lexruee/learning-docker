# Redis - InMemory Key-Value Store


## docker pull

``` 
docker pull redis:apline
```


## docker run

``` 
docker run --rm -it --name redis-test redis:apline 
```


## redis-cli

``` 
docker exec -it redis-test redis-cli
``` 

``` 
get mykey
set mykey "Hello World"
get mykey
```


## docker compose

``` 
docker-compose up
```