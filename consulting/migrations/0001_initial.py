# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('slug', models.SlugField(unique=True, max_length=40)),
                ('title', models.CharField(unique=True, max_length=40)),
                ('description', models.TextField()),
                ('body', models.TextField()),
                ('position', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ClientReference',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=40)),
                ('sort_name', models.CharField(max_length=40)),
                ('job_title', models.CharField(max_length=40)),
                ('phone', models.CharField(max_length=15, blank=True)),
                ('email', models.EmailField(max_length=40, blank=True)),
                ('client', models.ForeignKey(to='consulting.Client')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ClientWork',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=40)),
                ('description', models.TextField()),
                ('client', models.ForeignKey(to='consulting.Client')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Consultant',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('slug', models.SlugField(unique=True, max_length=20)),
                ('name', models.CharField(unique=True, max_length=40)),
                ('name_sort', models.CharField(unique=True, max_length=40)),
                ('description', models.TextField()),
                ('body', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PracticeArea',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('slug', models.SlugField(unique=True, max_length=20)),
                ('title', models.CharField(unique=True, max_length=30)),
                ('description', models.TextField()),
                ('body', models.TextField()),
            ],
            options={
                'ordering': ['title'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='QAndA',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('slug', models.SlugField()),
                ('title', models.CharField(unique=True, max_length=75)),
                ('question', models.TextField()),
                ('answer', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Quote',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('quote', models.TextField()),
                ('name', models.CharField(max_length=40)),
                ('job_title', models.CharField(max_length=40, blank=True)),
                ('organization', models.CharField(max_length=50, blank=True)),
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
            unique_together=set([('client', 'sort_name'), ('client', 'name')]),
        ),
        migrations.AddField(
            model_name='client',
            name='practice_areas',
            field=models.ManyToManyField(to='consulting.PracticeArea', null=True),
            preserve_default=True,
        ),
    ]
