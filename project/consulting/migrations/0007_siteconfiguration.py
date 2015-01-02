# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('consulting', '0006_auto_20150102_2131'),
    ]

    operations = [
        migrations.CreateModel(
            name='SiteConfiguration',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('email', models.EmailField(default=b'oliver@otessier.com', max_length=255)),
                ('about_footer', models.TextField(help_text=b'Appears in site footer.')),
                ('about_homepage', models.TextField(help_text=b'Appears on home page.')),
            ],
            options={
                'verbose_name': 'Site Configuration',
            },
            bases=(models.Model,),
        ),
    ]
