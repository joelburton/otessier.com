#!/bin/sh

cd /home/django/otessier.com/
venv/bin/python project/manage.py dbbackup
venv/bin/python project/manage.py mediabackup
s3cmd put /home/django/otessier.com/backups/* s3://otessier-com-backup