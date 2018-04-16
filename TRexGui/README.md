# Trex Gui Client
>It's a container for the Trex Gui part, you can manage your TrexServ from this module and show differents graph of the flux.
![](Login.png)

## Installation

Linux:

```sh
	docker build -t trex_gui .
	docker run -v /tmp/.X11-unix:/tmp/.X11-unix -e DISPLAY=unix$DISPLAY trex_gui:latest
```


## Release History

* 0.1.1
    * Adding sfr.yaml
    * Adding imix.yaml
* 0.1.0
    * Create the Reame.md
* 0.0.1
    * Work in progress

## Meta

Fork it (<https://github.com/Lluyssen/TrexDockerImplementation>)
Form (<https://github.com/cisco-system-traffic-generator>)