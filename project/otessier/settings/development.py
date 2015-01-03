"""
Development settings for otessier project.
"""

from .base import *


SECRET_KEY = 'i^ari$22!b+&pwhm=o7h-%vr-%us)#k=q0!g9qcaz*a#!h!k*c'

DEBUG = True
TEMPLATE_DEBUG = True

INSTALLED_APPS += (
    'debug_toolbar',
    'django_extensions',
)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'otessier',
        'HOST': 'localhost',
    }
}

MIDDLEWARE_CLASSES += (
    'otessier.timing.TimingMiddleware',
)


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

# Blather on about every little thing that happens. We programmers get lonely.

LOGGING = {
    'version': 1,

    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        '': {
            'handlers': ['console'],
            'level': 'DEBUG',
        },
    },
}
