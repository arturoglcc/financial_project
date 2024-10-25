#!/bin/bash

# build image for data base
docker build -t my-mysql -f docker/Dockerfile.bd .

# build image for http server
docker build -t my-http -f docker/Dockerfile.http .

# execute dockers
docker run -d --name mysql-container -p 3306:3306 my-mysql
docker run -d --name http-container -p 8000:8000 --link mysql-container my-http

