#!/bin/sh

exec docker rm $(docker ps -a | grep "litr" | awk '{print $1}') && docker rmi buri_litr litr