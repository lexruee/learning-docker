# MongoDB - Document-oriented Database

## Image downloaden

``` 
docker pull mongo
```

## Container starten

``` 
docker run --rm --name mongodb-test -d mongo
```

## Mongo Shell starten

``` 
docker exec -it mongodb-test mongo
```

```
show dbs
show collections
use testdb
db.users.insertOne({name: 'Alex'})
db.users.find()
db.users.find({name: 'Alex'})
exit
```

## Container stoppen

``` 
docker stop mongodb-test
```

## Docker compose

``` 
docker-compose up -d mongodb
``` 

``` 
docker-compose down mongodb
```