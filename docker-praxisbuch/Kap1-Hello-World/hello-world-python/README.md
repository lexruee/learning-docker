# PHP7/Apache Hello World

## Build

To create a docker image based on the `Dockerfile` run the command below.
The command will create a tagged docker image `hello-world-python`.

```
docker build -t hello-world-python .
```

## Running 

To run the docker image, enter:

```
docker run -p 8080:8080 hello-world-python
```

This commands runs the docker image and maps the port 8080 of the host machine
to the port 8080 of the container system.
