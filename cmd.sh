#!/bin/sh
set -e

if [ "$ENV" = 'DEV' ]; then
  echo "Running Development Server"
  exec python ../manage.py runserver 0.0.0.0:8000
elif [ "$ENV" = 'STAGE' ]; then
  echo "Running Staging Server"
  cd .. && gunicorn --bind 0.0.0.0:8000 stream_app.wsgi:application --timeout 60
  # cd .. && gunicorn --reload -k gevent -w 1 stream_app.wsgi:application --bind 0.0.0.0:8000 --log-level debug
elif [ "$ENV" = 'PROD' ]; then
  echo "Running Production Server"
  gunicorn stream_app.wsgi:application --bind 0.0.0.0:8000
fi
