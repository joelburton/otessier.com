# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('consulting', '0008_siteconfiguration_phone'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='consultant',
            options={'ordering': ['position', 'title']},
        ),
        migrations.AddField(
            model_name='clientreference',
            name='title',
            field=models.CharField(default='', max_length=40, verbose_name=b'name'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='consultant',
            name='title',
            field=models.CharField(default='', max_length=40, verbose_name=b'name'),
            preserve_default=False,
        ),
        migrations.RunSQL(
            """UPDATE consulting_clientreference SET title = name;
               UPDATE consulting_consultant SET title = name;"""
        ),
        migrations.RemoveField(
            model_name='consultant',
            name='name',
        ),
    ]
