# Datenbanksysteme

## MariaDB

### Beispiel 1: mysql shell starten

``` 
docker run --name mariadb-test --rm -d -e MYSQL_ROOT_PASSWORD=geheim mariadb:latest
docker exec -it mariadb-test musql -u root -p
```

### Beispel 2: mit eigenem Volume

``` 
mkdir mariadb_volume
docker run --name mariadb-test --rm -d -e MYSQL_ROOT_PASSWORD=geheim \
    -v $(pwd)/mariadb_volume:/var/lib/mysql mariadb:latest 
```

## Postgres

### Beispiel 1: psql shell starten

``` 
docker run --name postgres-test -e POSTGRES_PASSWORD=geheim -d postgres
docker exec -it postgres-test psql -h localhost -U postgres
```

