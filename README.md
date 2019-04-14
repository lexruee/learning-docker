# Learning Docker

```
Docker is a utility to pack, ship and run any application as a lightweight container.
```

## Installation on Arch Linux

Install it with `pacman`:

```
sudo pacman -S docker
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



## Online Resources

 * [Arch Linux Wiki - Docker](https://wiki.archlinux.org/index.php/docker)
 * [Docker Documentation](https://wiki.archlinux.org/index.php/docker)

## Book Resources

 * [Docker - Kofler, Öggl](https://www.amazon.de/Docker-Praxisbuch-Entwickler-DevOps-Teams-Windows/dp/3836261766/ref=sr_1_1?__mk_de_DE=%C3%85M%C3%85%C5%BD%C3%95%C3%91&keywords=docker+kofler&qid=1555228385&s=gateway&sr=8-1)
