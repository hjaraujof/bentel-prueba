#!/bin/sh
python ../manage.py makemigrations --settings config.settings.production
python ../manage.py migrate --settings config.settings.production