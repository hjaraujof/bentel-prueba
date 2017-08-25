#!/bin/sh

# wait for Postgres to start
sleep 10

python bentel/manage.py migrate

python bentel/manage.py runserver 0.0.0.0:8000

DJANGO_SU_NAME=admin
DJANGO_SU_EMAIL=admin@prueba.com
DJANGO_SU_PASSWORD=bentel-prueba

python -c "import django; django.setup(); \
   from django.contrib.auth.management.commands.createsuperuser import get_user_model; \
   get_user_model()._default_manager.db_manager('default').create_superuser( \
   username='$DJANGO_SU_NAME', \
   email='$DJANGO_SU_EMAIL', \
   password='$DJANGO_SU_PASSWORD')"