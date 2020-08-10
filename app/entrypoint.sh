#!/bin/sh

echo "Waiting for postgres..."

while ! nc -z 0.0.0.0 5432; do
  sleep 0.1
done

echo "PostgreSQL started"

python3 manage.py makemigration
python3 manage.py migrate
python3 manage.py runserver


exec "$@"
© 2020 GitHub, Inc.
