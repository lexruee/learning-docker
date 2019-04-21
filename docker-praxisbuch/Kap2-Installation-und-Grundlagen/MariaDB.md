# Maria DB

## Beispel  1

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

