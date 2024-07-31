#!/bin/bash

# Number of workers to start
NUM_WORKERS=3

# Start the master service using the specified Docker Compose file
docker-compose -f docker-compose.multi-worker.yml up -d main

# Start the worker services with dynamic names
for i in $(seq 1 $NUM_WORKERS); do
    WORKER_NAME="worker${i}"
    docker-compose -f docker-compose.multi-worker.yml run -d \
        -e LOCUST_WORKER_NAME=$WORKER_NAME \
        --name locust-$WORKER_NAME \
        worker
done
