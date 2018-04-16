create the images from the dockerfile : 'docker build -t trex_gui .'
run the image with the graphical mod : 'docker run -v /tmp/.X11-unix:/tmp/.X11-unix -e DISPLAY=unix$DISPLAY trex_gui:latest'