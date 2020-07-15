#!/bin/bash 

docker build -t gaze . && docker tag gaze cpheinrich/gaze:latest && docker push cpheinrich/gaze:latest