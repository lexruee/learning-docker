# Flask Hello World

## Build the image

``` 
docker build -t flask-hello-world . 
```

## Run the container
``` 
docker run -it -p 5000:5000 flask-hello-world
```