# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('consulting', '0018_auto_20150105_0257'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='client',
            options={'ordering': ['position', 'title']},
        ),
        migrations.AlterModelOptions(
            name='clientreference',
            options={'ordering': ['position', 'created']},
        ),
        migrations.AlterModelOptions(
            name='clientwork',
            options={'ordering': ['position', 'created']},
        ),
        migrations.AlterModelOptions(
            name='libraryfile',
            options={'ordering': ['position', 'title']},
        ),
        migrations.AlterModelOptions(
            name='qanda',
            options={'ordering': ['position', '-id'], 'verbose_name': 'Question and Answer'},
        ),
    ]
