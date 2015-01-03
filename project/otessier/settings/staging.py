"""
Staging settings for otessier project.

For this project, "staging" means "running on dev environment, but with caching and such set up
like production."
"""

from .base import *


SECRET_KEY = 'i^ari$22!b+&pwhm=o7h-%vr-%us)#k=q0!g9qcaz*a#!h!k*c'

MIDDLEWARE_CLASSES += (
    'otessier.timing.TimingMiddleware',
)

ALLOWED_HOSTS = ['localhost', 'preview.localhost', '127.0.0.1']


##################################################################################################
# Database

# Use development PG database

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'otessier',
        'HOST': 'localhost',
        'CONN_MAX_AGE': None,
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

# Be moderately chatty

LOGGING = {
    'version': 1,

    'handlers': {
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        '': {
            'handlers': ['console'],
            'level': 'INFO',
        },
    },
}

##################################################################################################
# Caches
#
# We use AWS SES for sending email (except on development, where we override this)

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.PyLibMCCache',
        'LOCATION': '127.0.0.1:11211',
    }
}

SOLO_CACHE = 'default'
SOLO_CACHE_TIMEOUT = 60 * 5

TEMPLATE_LOADERS = (
    ('django.template.loaders.cached.Loader', (
        'django.template.loaders.filesystem.Loader',
        'django.template.loaders.app_directories.Loader',
    )),
)