#!/bin/sh

cd /home/django/otessier.com/
venv/bin/python project/manage.py dbbackup
venv/bin/python project/manage.py mediabackup