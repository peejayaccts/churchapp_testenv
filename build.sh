#!/bin/sh

set -ev

cd ChMS_project/
python manage.py migrate --noinput
python manage.py runserver 
python api_functional_tests.py
python functional_tests.py
