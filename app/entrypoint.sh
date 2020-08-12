#!/bin/sh

echo "Waiting for postgres..."

while ! nc -z 0.0.0.0 5432; do
  sleep 0.5
  echo "wait..."
done

echo "PostgreSQL started"


sleep 5
python3 manage.py migrate
python3 manage.py runserver 0.0.0.0:8000 & celery worker -A dj_api.celery -B

exec "$@"
