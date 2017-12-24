"""Development settings for otessier project."""

import logging
import warnings

from django.conf import settings
from django.test.runner import DiscoverRunner

from .base import *


SECRET_KEY = 'i^ari$22!b+&pwhm=o7h-%vr-%us)#k=q0!g9qcaz*a#!h!k*c'

DEBUG = True


INSTALLED_APPS = INSTALLED_APPS + [
    'debug_toolbar',
    'django_extensions',
]

MIDDLEWARE += [
    'otessier.timing.TimingMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

##################################################################################################
# Database
#
# Use development PG database

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'otessier',
        'HOST': 'localhost',
    }
}


##################################################################################################
# Email
#
# We don't want to send real email, so just print to the console

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Joel's MacBook can timeout when at a cafe with incorrectly-set DNS settings, as it doesn't know
# the hostname of the laptop. So let's hack this in:

from django.core.mail.utils import DNS_NAME
DNS_NAME._fqdn = "localhost"


##################################################################################################
# Logging & Error Reporting
#
# Blather on about every little thing that happens. We programmers get lonely.

LOGGING = {
    'disable_existing_loggers': False,
    'version': 1,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(name)s %(message)s'
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose',
        },
    },
    'loggers': {
        'otessier': {
            'handlers': ['console'],
            'level': 'DEBUG',
        },
        'django.db.backends': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': False,
        },
    },
}


##################################################################################################
# Caches
#
# Cache nothing

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
    }
}


##################################################################################################
# Testing
#
# We don't want to spray all sorts of factory-made fake media stuff in the media folder
# (it won't hurt things, but will take up space), so let's use the temp directory for that.


class MediaTempTestSuiteRunner(DiscoverRunner):
    def __init__(self, *args, **kwargs):
        settings.MEDIA_ROOT = "/tmp"
        super(MediaTempTestSuiteRunner, self).__init__(*args, **kwargs)


TEST_RUNNER = 'otessier.settings.development.MediaTempTestSuiteRunner'
