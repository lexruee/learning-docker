# Hello World

Erstelle die Ordner:

```
mkdir -p /home/xander/docker/var/dc-test-db
mkdir -p /home/xander/docker/var/dc-test-www
```

Den Stack erstellen und starten via:

``` 
docker stack deploy -c dokcer-compose.yml stacktest
```

Mit `docker stack ls` den erstellten Stack auflisten:

``` 
NAME                SERVICES            ORCHESTRATOR
stacktest           2                   Swarm

```

Mit `docker network ls` anschauen, was für ein Netzwerk erstellt wurde,
damit die Container untereinander kommunizieren können:

``` 
NETWORK ID          NAME                DRIVER              SCOPE
b6644ba1ad9a        bridge              bridge              local
0fe5dc49b05a        docker_gwbridge     bridge              local
6afac2aea1de        host                host                local
pujb3dvwit5z        ingress             overlay             swarm
64d27fe5b525        none                null                local
rwug7d1xxkc0        stacktest_default   overlay             swarm
```


Schauen ob der Stack läuft:

``` 
▶ docker stack ps stacktest
ID                  NAME                    IMAGE               NODE                DESIRED STATE       CURRENT STATE                ERROR               PORTS
zq4uxlil50ln        stacktest_db.1          mariadb:latest      xonix               Running             Running about a minute ago                       
8hmoxdajoy4d        stacktest_wordpress.1   wordpress:latest    xonix               Running             Running 2 minutes ago                            
```

Schauen ob die Services laufen:

``` 
▶ docker service ls
ID                  NAME                  MODE                REPLICAS            IMAGE               PORTS
cse2mfyk5wfq        stacktest_db          replicated          1/1                 mariadb:latest      
y4p9d2fgd3v6        stacktest_wordpress   replicated          1/1                 wordpress:latest    *:8090->80/tcp

```

Die laufenden Prozesse eines Services anzeigen:

``` 
docker service ps stacktest_db
```


Die laufenden Container auflisten:

```
▶ docker ps
CONTAINER ID        IMAGE               COMMAND                  CREATED              STATUS              PORTS               NAMES
cf16bb33a89f        mariadb:latest      "docker-entrypoint.s…"   About a minute ago   Up About a minute   3306/tcp            stacktest_db.1.zq4uxlil50lnblzi9larue4i3
b786eac5c451        wordpress:latest    "docker-entrypoint.s…"   About a minute ago   Up About a minute   80/tcp              stacktest_wordpress.1.8hmoxdajoy4dovkwv1zoavv1t
``` 

Nun den Browser starten und `http://127.0.0.1:8090` besuchen.

Wordpress installieren und überprüfen, ob im MariaDB Container eine DB für Wordpress erstellt wurde:

``` 
docker exec -it stacktest_db.1.zq4uxlil50lnblzi9larue4i3 /bin/bash
```

``` 
mysql -u root -p
use wordpress;
show tables;
exit
```

Den Stack wieder stoppen und löschen mit:

``` 
docker stack rm stacktest
```

