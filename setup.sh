#!/usr/env bash

#exit on error
set -o errexit

##Install dependecies
pip install -r dependecies.txt

##Run migrations in case any migrations hadn't been run yet
python manage.py migrate