# Node Express Example

## Building the image

``` 
docker build -t node-test .
```

## Running the image

```
docker run --rm -it -p 3000:3000 node-test
```


## Docker compose

``` 
docker-compose up
```

To the container in daemon mode:

``` 
docker-compose up -d
```

To rebuild run 

``` 
docker-compose build
```

or

```
docker-compose up --build
```
