# Maria DB

## Beispel 1 - Grundlagen

1) Container erstellen

MariaDB Container erstellen:

```
docker run -d --name mariadb-test1 -e MYSSQL_ROOT_PASSWORD=geheim mariadb
```

#### Container stoppen

Container mariadb-test1 stoppen:

```
docker stop mariadb-test1
```

#### Container details anzeigen

Details über den Container mariadb-test1 anzeigen:

```
docker inspect mariadb-test1
```

#### Container starten

Container mariadb-test1 starten:

```
docker start mariadb-test1
```

#### MySQL shell starten

```
docker exec -it mariadb-test1 mysql -u root -p
```


#### Bash shell starten

```
docker exec -it mariadb-test1 bash
```

#### Logs anzeigen

```
docker logs mariadb-test1
```

#### Container löschen

```
docker rm mariadb-test1
```


#### Containerlose Volumes löschen

```
docker prune volumes
```

## Beispiel 2 - Mit einem Volume

Host Verzeichnis erstellen für das Volume:

``` 
mkdir -p /home/xander/docker/varlibmysql
```

MariaDB Container erstellen und starten:

```
docker run -d --name mariadb-test2 \
    -e MYSQL_ROOT_PASSWORD=geheim \
    -v /home/xander/docker/varlibmysql:/var/lib/mysql \
    mariadb
```

In den Container springen und die mysql shell starten:

```
docker exec -it mariadb-test2 mysql -u root -p
```

Eine Test-Datenbank erstellen:

``` 
CREATE DATABASE db;
```


Den Container stoppen:

```
docker stop mariadb-test2
```


Den Container wiederstarten und in die mysql shell springen:

``` 
docker exec -it mariadb-test2 mysql -u root -p
```

Überprüfen ob die Test-Datenbank immer noch da ist:

``` 
show databases;
```

## Beispiel 3 - Mit Port-Weiterleitung

MariaDB Container erstellen und starten:

```
docker run -d --name mariadb-test3 \
    -e MYSQL_ROOT_PASSWORD=geheim \
    -v /home/xander/docker/varlibmysql:/var/lib/mysql \
    -p 13306:3306 \
    mariadb
```

Host Port ist 13306.

``` 
mysql -u root -p --port 13306 --protocol tcp
```

``` 
show databases;
```

## Beispiel 4 - Mit Docker-Netzwerk

Docker-Netzwerk erstellen mit Namen `test-net`:

``` 
docker network create test-net
```

MariaDB Container erstellen, welcher das Netzwerk `test-net` verwendet:

``` 
docker run -d --name mariadb-test4 \
    --network test-net \
    -v /home/xander/docker/varlibmysql/:/var/lib/mysql \
    mariadb

```

Als PHPMyAdmin Container erstellen, welcher auch das Netzwerk `test-net` verwendet:

``` 
docker run -d --name pma \
    -p 8080:80 \
    --network test-net \
    -e PMA_HOST=mariadb-test4 \
    phpmyadmin/phpmyadmin
```

Nun den Browser starten und auf `http://localhost:8080/` gehen.

Mit `docker ps` sehen wir nun, dass zwei Container gleichzeitig laufen.

Alle Container stoppen:

``` 
docker stop pma mariadb-test4
```

## Beispiel 5 - WordPress installieren

MariaDB Container erstellen, welcher das Netzwerk `test-net` verwendet:

``` 
docker run -d --name mariadb-test5 \
    --network test-net \
    -v /home/xander/docker/varlibmysql/:/var/lib/mysql \
    mariadb

```

WordPress Container erstellen und starten:

``` 
docker run -d --name wp-test1 \
    -p 8080:80 \
    --network test-net \
    -v /home/xander/docker/wp-html:/var/html \
    -e WORDPRESS_DB_PASSWORD=geheim \
    -e WORDPRESS_DB_HOST=mariadb-test5 \
    wordpress
```


Wordpress installieren und danach die DB anschauen:

``` 
docker exec -it mariadb-test5 mysql -u root -p
use wordpress;
show tables;
exit
```


