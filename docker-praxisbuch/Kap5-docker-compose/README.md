# Docker compose

## Installation von docker compose

Unter Arch Linux installierbar via:

``` 
sudo pacman -S docker-compose
```

``` 
docker-compose --version
```

## Hello World

Erstelle `docker-compose.yml` Datei mit dem folgendem Inhalt:

```
version: '3'

services:
    db:
        image: mariadb:latest
        volumes:
            - /home/xander/docker/var/dc-test-db:/var/lib/mysql
        environment:
            MYSQL_ROOT_PASSWORD: geheim
        restart: always
        
    wordpress:
        image: wordpress:latest
        volumes:
            - /home/xander/docker/var/dc-test-www:/var/www/html
        ports:
            - "8082:80"
        environment:
            WORDPRESS_DB_HOST: db:3306
            WORDPRESS_DB_PASSWORD: geheim
        restart: always
```

Erstelle die Ordner:

```
mkdir -p /home/xander/docker/var/dc-test-db
mkdir -p /home/xander/docker/var/dc-test-www
```

Nun, die Container erstellen und starten via:

``` 
docker-compose up -d
```

Mit `docker ps` überprüfen ob die Container laufen:

``` 
CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS              PORTS                  NAMES
4c2a52b629cb        wordpress:latest    "docker-entrypoint.s…"   45 seconds ago      Up 44 seconds       0.0.0.0:8082->80/tcp   hello-world_wordpress_1
e7a7e338730d        mariadb:latest      "docker-entrypoint.s…"   45 seconds ago      Up 44 seconds       3306/tcp               hello-world_db_1

```

Mit `docker network ls` anschauen, was für ein Netzerk erstellt wurde,
damit die Container untereinander kommunizieren können:

``` 
NETWORK ID          NAME                  DRIVER              SCOPE
b6644ba1ad9a        bridge                bridge              local
379faf53b1d5        hello-world_default   bridge              local
```

In den MariaDB Container springen und die mysql shell starten:

``` 
docker exec -it hello-world_db_1 /bin/bash
```

Nun den Browser starten und `http://localhost:8082` besuchen.

Wordpress installieren und überprüfen, ob im MariaDB Container eine DB für Wordpress erstellt wurde:

``` 
mysql -u root -p
use wordpress;
show tables;
exit
```

Die Container wieder stoppen mit:

``` 
docker-compose stop
```

Die Container wieder starten mit:

``` 
docker-compose start
```

Und am Schluss die Container stoppen und löschen:

``` 
docker-compose down
```
