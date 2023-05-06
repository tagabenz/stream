#! /bin/sh
docker exec stream-web-1 bash -c "cd /app && ./manage.py makemigrations && ./manage.py migrate"