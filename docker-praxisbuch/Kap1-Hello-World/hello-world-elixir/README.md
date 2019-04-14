# Elixir Hello World

## Build

To create a docker image based on the `Dockerfile` run the command below.
The command will create a tagged docker image `hello-world-elixir`.

```
docker build -t hello-world-elixir .
```

## Running 

To run the docker image, enter:

```
docker run hello-world-elixir
```

This commands runs the docker image and maps the port 8080 of the host machine
to the port 8080 of the container system.
