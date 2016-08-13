#!/bin/sh

set -ev

cd ChMS_project/
python manage.py migrate --noinput
python manage.py runserver 
