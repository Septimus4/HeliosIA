#!/usr/bin/env bash

docker run --gpus all --name=training -it -d \
--user $(id -u):$(id -g) \
-v /home/$USER/Documents/SharedFolder:/home/training helios_ia
