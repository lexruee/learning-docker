# PHP7/Apache Hello World

## Build

To create a docker image based on the `Dockerfile` run the command below.
The command will create a tagged docker image `hello-world-app`.

```
docker build -t hello-world-node .
```

## Running 

To run the docker image, enter:

```
docker run -p 8080:8080 hello-world-node
```

This commands runs the docker image and maps the port 8080 of the host machine
to the port 80 of the container system.
