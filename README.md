# Learning Docker

The Arch Linux Wiki[1] says:
```
Docker is a utility to pack, ship and run any application as a lightweight container.
```

The docker documentation[2] describes docker as:

```
Docker is a platform for developers and sysadmins to develop, deploy, and run applications with containers. 
The use of Linux containers to deploy applications is called containerization. 
Containers are not new, but their use for easily deploying applications is.
```

Containerization is increasingly popular because containers are [2]:

 * Flexible: Even the most complex applications can be containerized.
 * Lightweight: Containers leverage and share the host kernel.
 * Interchangeable: You can deploy updates and upgrades on-the-fly.
 * Portable: You can build locally, deploy to the cloud, and run anywhere.
 * Scalable: You can increase and automatically distribute container replicas.
 * Stackable: You can stack services vertically and on-the-fly.

## Installation on Arch Linux

Install it with `pacman`:

```
sudo pacman -S docker docker-compose
```

Enable and start the docker service:

```
sudo systemctl enable docker.service
sudo systemctl start docker.service
```

Check if the docker service is working by running:

```
systemctl status docker.service
```

Check docker version and get some extra details:

```
docker -v
docker info
```

Depending on your system, you will need to fix your DNS config,
so the docker registry is accessible.
Quick fix: Edit your /etc/resolv.conf and add `nameserver 8.8.8.8`


## Installation on Ubuntu 18.04 Server

```
sudo apt update
sudo apt install apt-transport-https ca-certificates curl software-properties-common
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu bionic stable"
sudo apt update
sudo apt install docker-ce
sudo systemctl status docker
```

Resource: https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-ubuntu-18-04

## Docker CLI Overview

```
Usage:	docker [OPTIONS] COMMAND

A self-sufficient runtime for containers

Options:
      --config string      Location of client config files (default "/home/xander/.docker")
  -D, --debug              Enable debug mode
  -H, --host list          Daemon socket(s) to connect to
  -l, --log-level string   Set the logging level ("debug"|"info"|"warn"|"error"|"fatal") (default "info")
      --tls                Use TLS; implied by --tlsverify
      --tlscacert string   Trust certs signed only by this CA (default "/home/xander/.docker/ca.pem")
      --tlscert string     Path to TLS certificate file (default "/home/xander/.docker/cert.pem")
      --tlskey string      Path to TLS key file (default "/home/xander/.docker/key.pem")
      --tlsverify          Use TLS and verify the remote
  -v, --version            Print version information and quit

Management Commands:
  builder     Manage builds
  config      Manage Docker configs
  container   Manage containers
  engine      Manage the docker engine
  image       Manage images
  network     Manage networks
  node        Manage Swarm nodes
  plugin      Manage plugins
  secret      Manage Docker secrets
  service     Manage services
  stack       Manage Docker stacks
  swarm       Manage Swarm
  system      Manage Docker
  trust       Manage trust on Docker images
  volume      Manage volumes

Commands:
  attach      Attach local standard input, output, and error streams to a running container
  build       Build an image from a Dockerfile
  commit      Create a new image from a container's changes
  cp          Copy files/folders between a container and the local filesystem
  create      Create a new container
  diff        Inspect changes to files or directories on a container's filesystem
  events      Get real time events from the server
  exec        Run a command in a running container
  export      Export a container's filesystem as a tar archive
  history     Show the history of an image
  images      List images
  import      Import the contents from a tarball to create a filesystem image
  info        Display system-wide information
  inspect     Return low-level information on Docker objects
  kill        Kill one or more running containers
  load        Load an image from a tar archive or STDIN
  login       Log in to a Docker registry
  logout      Log out from a Docker registry
  logs        Fetch the logs of a container
  pause       Pause all processes within one or more containers
  port        List port mappings or a specific mapping for the container
  ps          List containers
  pull        Pull an image or a repository from a registry
  push        Push an image or a repository to a registry
  rename      Rename a container
  restart     Restart one or more containers
  rm          Remove one or more containers
  rmi         Remove one or more images
  run         Run a command in a new container
  save        Save one or more images to a tar archive (streamed to STDOUT by default)
  search      Search the Docker Hub for images
  start       Start one or more stopped containers
  stats       Display a live stream of container(s) resource usage statistics
  stop        Stop one or more running containers
  tag         Create a tag TARGET_IMAGE that refers to SOURCE_IMAGE
  top         Display the running processes of a container
  unpause     Unpause all processes within one or more containers
  update      Update configuration of one or more containers
  version     Show the Docker version information
  wait        Block until one or more containers stop, then print their exit codes

Run 'docker COMMAND --help' for more information on a command.
```

## Online Resources

 * [1] [Arch Linux Wiki - Docker](https://wiki.archlinux.org/index.php/docker)
 * [2] [Docker Documentation](https://wiki.archlinux.org/index.php/docker)

## Book Resources

 * [Docker - Kofler, Öggl](https://www.amazon.de/Docker-Praxisbuch-Entwickler-DevOps-Teams-Windows/dp/3836261766/ref=sr_1_1?__mk_de_DE=%C3%85M%C3%85%C5%BD%C3%95%C3%91&keywords=docker+kofler&qid=1555228385&s=gateway&sr=8-1)



