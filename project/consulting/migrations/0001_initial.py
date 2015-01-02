# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False)),
                ('status', model_utils.fields.StatusField(default=b'private', max_length=100, verbose_name='status', no_check_for_status=True, choices=[(b'private', b'private'), (b'published', b'published')])),
                ('status_changed', model_utils.fields.MonitorField(default=django.utils.timezone.now, verbose_name='status changed', monitor='status')),
                ('slug', models.SlugField(unique=True, max_length=40)),
                ('title', models.CharField(unique=True, max_length=40)),
                ('organization', models.CharField(help_text=b'Long name for organization', unique=True, max_length=70)),
                ('description', models.TextField()),
                ('body', models.TextField()),
                ('url', models.URLField(max_length=100, verbose_name=b'URL', blank=True)),
                ('position', models.PositiveSmallIntegerField(default=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ClientReference',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False)),
                ('name', models.CharField(max_length=40)),
                ('job_title', models.CharField(max_length=40)),
                ('phone', models.CharField(max_length=20, blank=True)),
                ('email', models.EmailField(max_length=40, blank=True)),
                ('position', models.PositiveSmallIntegerField()),
                ('client', models.ForeignKey(to='consulting.Client')),
            ],
            options={
                'ordering': ['position'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ClientWork',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False)),
                ('status', model_utils.fields.StatusField(default=b'private', max_length=100, verbose_name='status', no_check_for_status=True, choices=[(b'private', b'private'), (b'published', b'published')])),
                ('status_changed', model_utils.fields.MonitorField(default=django.utils.timezone.now, verbose_name='status changed', monitor='status')),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('body', models.TextField()),
                ('position', models.PositiveSmallIntegerField()),
                ('client', models.ForeignKey(to='consulting.Client')),
                ('references', models.ManyToManyField(to='consulting.ClientReference', blank=True)),
            ],
            options={
                'ordering': ['position'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Consultant',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False)),
                ('status', model_utils.fields.StatusField(default=b'private', max_length=100, verbose_name='status', no_check_for_status=True, choices=[(b'private', b'private'), (b'published', b'published')])),
                ('status_changed', model_utils.fields.MonitorField(default=django.utils.timezone.now, verbose_name='status changed', monitor='status')),
                ('slug', models.SlugField(unique=True, max_length=20)),
                ('name', models.CharField(unique=True, max_length=40)),
                ('photo', models.ImageField(null=True, upload_to=b'consultants', blank=True)),
                ('description', models.TextField()),
                ('body', models.TextField()),
                ('position', models.PositiveSmallIntegerField(default=100)),
            ],
            options={
                'ordering': ['position', 'name'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='LibraryCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(unique=True, max_length=100)),
            ],
            options={
                'verbose_name_plural': 'library categories',
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
                ('position', models.PositiveSmallIntegerField(default=100)),
                ('librarycategory', models.ForeignKey(to='consulting.LibraryCategory')),
            ],
            options={
                'ordering': ['title'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PracticeArea',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False)),
                ('status', model_utils.fields.StatusField(default=b'private', max_length=100, verbose_name='status', no_check_for_status=True, choices=[(b'private', b'private'), (b'published', b'published')])),
                ('status_changed', model_utils.fields.MonitorField(default=django.utils.timezone.now, verbose_name='status changed', monitor='status')),
                ('slug', models.SlugField(unique=True, max_length=25)),
                ('title', models.CharField(unique=True, max_length=40)),
                ('short_description', models.CharField(help_text=b'Appears on home page carousel.', max_length=100)),
                ('icon_name', models.CharField(help_text=b'Font Awesome icon name.', max_length=15)),
                ('description', models.TextField(help_text=b'Appears on listing page, but not on detail page.')),
                ('body', models.TextField()),
                ('position', models.PositiveSmallIntegerField(default=100)),
            ],
            options={
                'ordering': ['position', 'title'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='QAndA',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False)),
                ('status', model_utils.fields.StatusField(default=b'private', max_length=100, verbose_name='status', no_check_for_status=True, choices=[(b'private', b'private'), (b'published', b'published')])),
                ('status_changed', model_utils.fields.MonitorField(default=django.utils.timezone.now, verbose_name='status changed', monitor='status')),
                ('slug', models.SlugField(unique=True)),
                ('title', models.CharField(unique=True, max_length=75)),
                ('description', models.TextField()),
                ('question', models.TextField()),
                ('answer', models.TextField()),
                ('credit', models.CharField(max_length=100, blank=True)),
                ('position', models.PositiveSmallIntegerField(default=100)),
            ],
            options={
                'ordering': ['position', '-created'],
                'verbose_name': 'Question and Answer',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Quote',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False)),
                ('status', model_utils.fields.StatusField(default=b'private', max_length=100, verbose_name='status', no_check_for_status=True, choices=[(b'private', b'private'), (b'published', b'published')])),
                ('status_changed', model_utils.fields.MonitorField(default=django.utils.timezone.now, verbose_name='status changed', monitor='status')),
                ('quote', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=75)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='clientwork',
            unique_together=set([('client', 'title')]),
        ),
        migrations.AlterUniqueTogether(
            name='clientreference',
            unique_together=set([('client', 'name')]),
        ),
        migrations.AddField(
            model_name='client',
            name='practiceareas',
            field=models.ManyToManyField(to='consulting.PracticeArea', null=True, verbose_name=b'practice areas'),
            preserve_default=True,
        ),
    ]
