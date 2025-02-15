#!/bin/bash

echo "Applying database migrations..."
python manage.py migrate

echo "Collecting static files..."
mkdir -p staticfiles
python manage.py collectstatic --noinput

echo "Starting Django app..."
exec python manage.py runserver 0.0.0.0:8000
