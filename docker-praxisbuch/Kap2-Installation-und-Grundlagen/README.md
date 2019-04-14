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


