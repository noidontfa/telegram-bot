#!/bin/sh

python manage.py collectstatic --noinput
gunicorn telebot.wsgi:application --bind=0.0.0.0:8000 --workers=3