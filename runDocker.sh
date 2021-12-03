#!/bin/bash 

exec docker run -i -v /tmp/.X11-unix:/tmp/.X11-unix -e DISPLAY=unix$DISPLAY -p 5000:5000 l-systems "$@"

containerId=$(docker ps -aq -n 1)

mkdir -p ~/l-systems/Docker/History/

docker cp $containerId:/l-systems/History/History.txt ~/l-systems/Docker/History/History.txt
