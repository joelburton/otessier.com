# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('consulting', '0011_auto_20150103_1926'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='description',
            field=models.TextField(help_text=b'Short description of client and work. Show on listing and detail page.'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='client',
            name='image',
            field=models.ImageField(help_text=b'Logo for client, which is resized automatically . Make as square as possible.', upload_to=b'clients'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='client',
            name='organization',
            field=models.CharField(help_text=b'Long name for organization. Only used on client detail page.', unique=True, max_length=70),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='client',
            name='slug',
            field=models.SlugField(help_text=b'Determines the URL. Do not change this after an item is published.', unique=True, max_length=40),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='client',
            name='title',
            field=models.CharField(help_text=b'Short name of client, used throughout site.', unique=True, max_length=40),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='client',
            name='url',
            field=models.URLField(help_text=b"URL for this client (don't forget the http://).", max_length=100, verbose_name=b'URL', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='clientwork',
            name='body',
            field=models.TextField(help_text=b'Long description of work. Shows up on client detail page.'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='clientwork',
            name='description',
            field=models.TextField(help_text=b'Short description of work. Shows up in bold on client detail page.'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='clientwork',
            name='references',
            field=models.ManyToManyField(help_text=b'References for this client work.', to='consulting.ClientReference', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='consultant',
            name='description',
            field=models.TextField(help_text=b'Short description of consultant. Shows on listing page and detail page.'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='consultant',
            name='photo',
            field=models.ImageField(help_text=b'Resized automatically. Make as square as possible.', null=True, upload_to=b'consultants', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='consultant',
            name='slug',
            field=models.SlugField(help_text=b'Determines the URL. Do not change this after an item is published.', unique=True, max_length=20),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='consultant',
            name='title',
            field=models.CharField(unique=True, max_length=40, verbose_name=b'name'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='librarycategory',
            name='description',
            field=models.TextField(help_text=b'Description of category. Shows up on listing page and detail page.'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='librarycategory',
            name='slug',
            field=models.SlugField(help_text=b'Determines the URL. Do not change this after an item is published.', unique=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='libraryfile',
            name='asset',
            field=models.FileField(help_text=b'File asset.', max_length=255, null=True, upload_to=b'library', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='libraryfile',
            name='description',
            field=models.TextField(help_text=b'Description of file/link. Shows up on category detail page.'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='libraryfile',
            name='slug',
            field=models.SlugField(help_text=b'Determines the URL. Do not change this after an item is published.', unique=True, max_length=100),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='libraryfile',
            name='url',
            field=models.URLField(help_text=b"Link URL (don't forget the http://)", max_length=255, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='practicearea',
            name='icon_name',
            field=models.CharField(help_text=b'Font Awesome icon name (without the leading "fa-").', unique=True, max_length=15),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='practicearea',
            name='short_description',
            field=models.CharField(help_text=b'Appears on home page carousel.', unique=True, max_length=100),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='practicearea',
            name='slug',
            field=models.SlugField(help_text=b'Determines the URL. Do not change this after an item is published.', unique=True, max_length=25),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='qanda',
            name='credit',
            field=models.CharField(help_text=b'Appears at bottom of answer. Used for providing publishing credit.', max_length=100, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='qanda',
            name='description',
            field=models.TextField(help_text=b'Short description of the question. Shows up on the listing page.'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='qanda',
            name='question',
            field=models.TextField(help_text=b'Full question. Shows on the detail page.'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='qanda',
            name='slug',
            field=models.SlugField(help_text=b'Determines the URL. Do not change this after an item is published.', unique=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='qanda',
            name='title',
            field=models.CharField(help_text=b'Shows up in portlets, search results, and on the listing page.', unique=True, max_length=75),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='quote',
            name='author',
            field=models.CharField(help_text=b'Entire text for author, like "T.S. Eliot, Curmudgeon, Bank of England".', max_length=75),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='siteconfiguration',
            name='email',
            field=models.EmailField(default=b'oliver@otessier.com', help_text=b'Email address shown on the site.', max_length=255),
            preserve_default=True,
        ),
    ]
