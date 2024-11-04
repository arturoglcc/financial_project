#!/bin/sh
# Wait for the backend service to become reachable
until curl -s http://backend:8000 > /dev/null; do
  echo "Waiting for backend..."
  sleep 2
done

# Start Nginx
nginx -g "daemon off;"


