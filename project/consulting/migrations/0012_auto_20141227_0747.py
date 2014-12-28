# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('consulting', '0011_auto_20141227_0739'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='clientwork',
            options={'ordering': ['position']},
        ),
        migrations.AlterUniqueTogether(
            name='clientreference',
            unique_together=set([('client', 'name')]),
        ),
    ]
