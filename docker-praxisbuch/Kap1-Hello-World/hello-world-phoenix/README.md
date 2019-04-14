# Phoenix Hello World

## Development

To start your Phoenix server:

  * Install dependencies with `mix deps.get`
  * Create and migrate your database with `mix ecto.setup`
  * Install Node.js dependencies with `cd assets && npm install`
  * Start Phoenix endpoint with `mix phx.server`

Now you can visit [`localhost:4000`](http://localhost:4000) from your browser.

Ready to run in production? Please [check our deployment guides](https://hexdocs.pm/phoenix/deployment.html).

### Learn more

  * Official website: http://www.phoenixframework.org/
  * Guides: https://hexdocs.pm/phoenix/overview.html
  * Docs: https://hexdocs.pm/phoenix
  * Mailing list: http://groups.google.com/group/phoenix-talk
  * Source: https://github.com/phoenixframework/phoenix

## Build

To create a docker image based on the `Dockerfile` run the command below.
The command will create a tagged docker image `hello-world-phoenix`.

```
docker build -t hello-world-phoenix .
```

## Running 

To run the docker image, enter:

```
docker run -p 5000:5000 hello-world-phoenix
```

This commands runs the docker image and maps the port 5000 of the host machine
to the port 5000 of the container system.
