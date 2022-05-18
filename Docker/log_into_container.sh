#!/usr/bin/env bash

ID=`docker ps -aqf "name=training"`
docker start $ID && docker attach $ID
