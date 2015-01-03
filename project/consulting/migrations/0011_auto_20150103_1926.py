# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('consulting', '0010_auto_20150103_1924'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='clientreference',
            unique_together=set([('client', 'title')]),
        ),
    ]
