#!/bin/bash 

docker build -t gaze . && docker tag 139b6a5b56d5 cpheinrich/gaze:latest && git push cpheinrich/gaze:latest