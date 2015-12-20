# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-20 02:37
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('consulting', '0002_db_fixes'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='qanda',
            options={'ordering': ['position', '-id'], 'verbose_name': 'Question and answer', 'verbose_name_plural': 'Questions and answers'},
        ),
        migrations.AlterModelOptions(
            name='siteconfiguration',
            options={'verbose_name': 'Site configuration'},
        ),
    ]
