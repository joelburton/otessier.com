"""
Deployment settings for otessier project.
"""

import os

from .base import *


SECRET_KEY = os.environ['SECRET_KEY']

ALLOWED_HOSTS = ['new.otessier.com', 'otessier.com']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'otessier',
        'HOST': 'localhost',
        'USER': 'otessier',
        'PASSWORD': os.environ['PG_PASSWORD'],
        'CONN_MAX_AGE': None,
    }
}