# Docker kennenlernen

## Begriffe

### Images und Container

 * Image: Ein Read-Only Dateisystem; stellt die Basis für einen Container zur Verfügung.
 * Container: Ein Container führt ein Image aus; erstellt über dem Image ein Overlay-Dateisystem.

 Die Trennung von immutable Images und mutable Containern ermöglicht es von
 einem Image beliebig viele Container abzuleiten, die parallel ausgeführt werden können.

### Volumes

Volumes sind von Containern getrennte Verzeichnisse im Host-Dateisystem. Dort 
werden Dateien gespeichert, die von einem Container zum nächsten Container erhalten
bleiben sollen.

Datenbankdaten werden zum Beispiel in einem Volumne gespeichert, sodass
ein neuer Container die alte Datenbank wiederverwenden kann.


### Services, Stacks und Cluster

 * Service: Ein Service beschreibt einen Dienst bzw. eine Aufgabe. Ist ähnlich wie ein Container,
 ausser, dass die Ausführung von Docker übernommen wird.
 * Stacks: Stacks sind grob gesagt eine Sammlung von Services, die mit Hilfe eines Stacks
 einfach administriert werden können.
 * Cluster/Schwarm: Ein Schwarm besteht aus mehreren Docker Instanzen.


### Kubernetes

 * Kubernetes: Eine Alternative zu einem Docker Schwarm. Es handelt sich dabei
 um ein von Google entwickeltes Open-Source-Program zur Verwaltung von Containern.
 Kubernetes wird oft in Kombination mit Docker verwendet.


## Befehl docker

Docker basiert auf einem Client-Server-Modell. Der Server ist dabei der
Docker daemon namens `dockerd`. Der Client ist das Program `docker`.

Unter Linux kann man Zustand des Docker Services via `systemctl status docker.service`
abfragen. Mittels `docker info` erhält man Docker Systeminformationen.


Eine nützliche Liste aller verfügbaren Commands bekommt via `docker help`.


## Spielwiese

### Beispiel 1: Hello World

Das klassiche Hello World Beispiel gibt es auch in der Docker Community:

```
docker run hello-world
```

### Statusinformationen

Liefert eine Liste aller laufenden und in der Vergangenheit ausgeführten Docker-Container. 

```
docker ps -a
```

Liefert eine Liste aller lokal verfügbaren Images:

```
docker images
```

### Beispiel 2: Basis-Images verwenden

Basis-Images sind Images die als Grundlage für das Zusammenstellen neuer Container
dienen. Für die gängigen GNU/Linux-Distributionen gibt es Basis-Images.

Um ein Ubuntu-Container interaktiv auszuführen ist der folgende Befehl hilfreich:

```
docker run -it ubuntu
```

 * Die Option `i` steht für interaktiv.
 * Die Option `t` steht für das Verwenden von TTY als Standard-Output aka stdout.

Dieser Befehlt ist dabei gleichbedeutend mit diesem hier:

```
docker run -it ubuntu:latest
```

Um einen ganz spezifischen Container auszuführen kann man auch die Versionnummer angeben:

```
docker run -it ubuntu:19.04
```
Um nur einen Befehl innerhalb des Containers auszuführen, können wir den
folgenden Befehl verwenden:

```
docker run -t ubuntu:latest cat /etc/os-release
```

### Aktuelles Base-Image downloaden

Den Download einer aktuelleren Image-Version kann man anstossen via:

```
docker pull ubuntu
```

### Container mit "docker start" erneut ausführen

Der Befehl `docker run` erstellt jeweils einen neuen Container.
Um einen Contaienr erneut auszuführen muss man den Befehl `docker start` verwenden.

```
docker start -i adoring_jackson
```

Als Name kann man die Hash-ID des Containers nutzen oder den zufällig erstellent Namen.
Die Hash-ID bzw. den Namen des Containers kann man mit Hilfe des Befehls `docker ps -a` 
herausfinden.


### Eigene Container-Namen

Mit der Option `--name` verwenden kann man selber einem Container einen Namen geben:

```
docker run --name descartes -it ubuntu:latest cat /etc/os-release
```

```
docker start -i descartes
```

### Parallel weitere Prozesse mit docker exec ausführen

```
docker run -it --name myubuntu -h myubuntu ubuntu:19.04
```

Mit `docker exec` kann ein weiterer Prozess in einem Container ausgeführt werden:

```
docker exec -it myubuntu /usr/bin/top
```

### Beispiel 3: MariaDB ausführen

MariaDB Container erstellen:

```
docker run -d --name mariadb-test1 -e MYSSQL_ROOT_PASSWORD=geheim mariadb
```

Container mariadb-test1 stoppen:

```
docker stop mariadb-test1
```

Details über den Container mariadb-test1 anzeigen:

```
docker inspect mariadb-test1
```

Container mariadb-test1 starten:

```
docker start mariadb-test1
```

Enter the mysql shell:

```
docker exec -it mariadb-test1 mysql -u root -p
```

Enter the bash:

```
docker exec -it mariadb-test1 bash
```

Show logs:

```
docker logs mariadb-test1
```

Delete container:

```
docker rm mariadb-test1
```


Delete volumes without containers:

```
docker prune volumes
```

### Beispiel 4: Postgres ausführen

```
docker run --name postgres-test1 -e POSTGRES_PASSWORD=geheim -d postgres
```

Enter the psql shell:

```
docker exec -it postgres-test1 psql -U postgres
```

```
docker stop postgres-test1
```


