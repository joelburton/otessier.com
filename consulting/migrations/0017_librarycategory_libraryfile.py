# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('consulting', '0016_auto_20141227_1452'),
    ]

    operations = [
        migrations.CreateModel(
            name='LibraryCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(unique=True, max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='LibraryFile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False)),
                ('status', model_utils.fields.StatusField(default=b'private', max_length=100, verbose_name='status', no_check_for_status=True, choices=[(b'private', b'private'), (b'published', b'published')])),
                ('status_changed', model_utils.fields.MonitorField(default=django.utils.timezone.now, verbose_name='status changed', monitor='status')),
                ('slug', models.SlugField(unique=True, max_length=100)),
                ('title', models.CharField(unique=True, max_length=100)),
                ('description', models.TextField()),
                ('asset', models.FileField(null=True, upload_to=b'library', blank=True)),
                ('url', models.URLField(blank=True)),
                ('position', models.PositiveSmallIntegerField()),
                ('librarycategory', models.ForeignKey(to='consulting.LibraryCategory')),
            ],
            options={
                'ordering': ['title'],
            },
            bases=(models.Model,),
        ),
    ]
