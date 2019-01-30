#!/bin/bash

# Pull image name from environment if set
if [ -z "$IMAGE" ]; then
  IMAGE="docker.wwt.com/wwt/kubeschedler-phoenix:local"
fi
echo "Building image named $IMAGE"

docker build -t $IMAGE .