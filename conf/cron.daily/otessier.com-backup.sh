#!/bin/sh

cd /home/django/otessier.com/
source venv/bin/activate
python project/manage.py dbbackup
python project/manage.py mediabackup
s3cmd put /home/django/otessier.com/backups/* s3://otessier-com-backup/`date +"%Y-%m-%d-%H%M%S"`/