#!/bin/sh

if [ "$DATABASE" = "new_db" ]
then
    echo "Waiting for postgres..."

    while ! nc -z $SQL_HOST $SQL_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi

python manage.py migrate

gunicorn --bind 0.0.0.0:8000 stocks_products.wsgi

gunicorn stocks_products.wsgi:application --bind 0.0.0.0:8000

exec "$@"