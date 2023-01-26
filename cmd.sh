#!/bin/sh
set -e

if [ "$ENV" = 'DEV' ]; then
  echo "Running Development Server"
  exec python stream_app/manage.py runserver 0.0.0.0:8000

elif [ "$ENV" = 'STAGE' ]; then
  echo "Running Staging Server"
  # exec uwsgi --http 0.0.0.0:9090 --wsgi-file /app/stream_app/stream_app/wsgi.py --callable application
  gunicorn stream_app.wsgi:application --bind 0.0.0.0:8000
fi
