#!/bin/sh
set -e

if [ "$ENV" = 'DEV' ]; then
  echo "Running Development Server"
  #exec python manage.py runserver 0.0.0.0:8000
  exec la -la
  #exec pwd
elif [ "$ENV" = 'STAGE' ]; then
  echo "Running Staging Server"

fi
