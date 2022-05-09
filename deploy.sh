#!/bin/bash

echo "deploying images..."
docker-compose build
docker-compose up --detach --remove-orphans --force-recreate
docker system prune -f
