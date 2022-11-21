#!/bin/sh

python src/manage.py migrate --no-input
python src/manage.py collectstatic --no-input

DJANGO_SUPERUSER_PASSWORD=$SUPER_USER_PASSWORD python src/manage.py createsuperuser --username $SUPER_USER_NAME --email $SUPER_USER_EMAIL --noinput

gunicorn src.Eshop.wsgi:application --bind 0.0.0.0:8000
