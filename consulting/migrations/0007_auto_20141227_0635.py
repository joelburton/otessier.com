# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('consulting', '0006_auto_20141227_0633'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='clientreference',
            options={'ordering': ['position']},
        ),
        migrations.AddField(
            model_name='clientreference',
            name='position',
            field=models.PositiveSmallIntegerField(default=0),
            preserve_default=False,
        ),
    ]
