#!/bin/sh

echo "Postgres server starting....."

while ! nc -z test-db 5432; do
  sleep 0.1
done

echo " postgres server has started.."

python manage.py run -h 0.0.0.0