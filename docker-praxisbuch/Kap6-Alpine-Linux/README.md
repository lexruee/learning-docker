# Alpine Linux - Grundlagen

## Container starten und verwenden

Docker Image Apline Linux herunterladen:

``` 
docker pull alpine
```

Einen Alpine Linux Container erstellen und starten:

``` 
docker run -it -h alpine --name alpine alpine
```

## Pakerverwaltung mit apk

| Command            |    Beschreibung                                   |
|:------------------:|:-------------------------------------------------:|
| apk add <pkg>      | Installiert das Paket <pkg>                       |
| apk del <pkg>      | Entfernt  das Paket <pkg>                         |
| apk info           | Listet die installierten Pakete auf               |
| apk search <pkg>   | Sucht nach Paketen in den Paketquellen            |
| apk stats          | Zeigt an, wie viele Pakete installiert sind       |
| apk update         | Ermittelt, welche Pakete aktuell verfügbar sind   |
| apk upgrade        | Aktualisiert alle installierte Pakete             |
