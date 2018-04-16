# Trex Gui Client
>It's a container for the Trex Gui part, you can manage your TrexServ from this module and show differents graph of the flux.
![](Login.png)

## Installation

Linux:

```sh
	docker build -t trex_gui .
	docker run -v /tmp/.X11-unix:/tmp/.X11-unix -e DISPLAY=unix$DISPLAY trex_gui:latest
```

## Explication of the Readme

Update and Upgrade ==> Basic
Add Webupd8 repository ==> Installe the Personal Package Archive for Oracle Java JDK 8 par webupd8
Install Addictional Pack ==> Installe  des packs graphiques
Install Java ==> Instalation de Orcale Java 8
Clean Up ==> Clean l'ensemble de fichier pour java
CMD => crée la commande de lancement automatique
TresGui Part ==> Clone depuis git le trex-stateless-gui dans le dossier /usr/local/gui/ et le tar

## Release History

* 0.1.2
    * Create the Reame.md
* 0.1.1
    * Adding sfr.yaml
    * Adding imix.yaml
* 0.1.0
    * Create the DockerFile
* 0.0.1
    * Work in progress

## Meta

1. Fork it (<https://github.com/Lluyssen/TrexDockerImplementation>)
2. Form (<https://github.com/cisco-system-traffic-generator>)