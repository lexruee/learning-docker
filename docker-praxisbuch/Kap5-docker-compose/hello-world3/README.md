# Hello World mit secrets

## docker-compose.yml

```
version: '3.1'

services:
    db:
        image: mariadb:latest
        secrets:
            - mysql_root
            - mysql_user
        volumes:
            - /home/xander/docker/var/dc-test-db:/var/lib/mysql
        environment:
            MYSQL_ROOT_PASSWORD_FILE: /run/secrets/mysql_root
            MYSQL_PASSWORD_FILE: /run/secrets/mysql_user
        restart: always

    wordpress:
        image: wordpress:latest
        secrets:
            - mysql_user
        volumes:
            - /home/xander/docker/var/dc-test-www:/var/www/html
        ports:
            - "8082:80"
        environment:
            WORDPRESS_DB_HOST: db:3306
            WORDPRESS_DB_PASSWORD_FILE: /run/secrets/mysql_user
        restart: always

secrets:
    mysql_root:
        file: ./mysql_root.txt
    mysql_user:
        file: ./mysql_user.txt



```

## Running

``` 
docker-compose up -d
```

```  
docker ps
```

## Stopping

```
docker-compose down 
```