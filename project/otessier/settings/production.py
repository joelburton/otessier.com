"""
Deployment settings for otessier project.
"""

from .base import *


SECRET_KEY = os.environ['SECRET_KEY']

ALLOWED_HOSTS = ['new.otessier.com', 'otessier.com', 'www.otessier.com',
                 'olivertessier.com', 'www.olivertessier.com', 'admin.otessier.com',
]

##################################################################################################
# Database

# Use production PG database

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'otessier',
        'HOST': 'localhost',
        'USER': 'otessier',
        'PASSWORD': os.environ['PG_PASSWORD'],
        'PORT': os.environ['PG_PORT'],
        'CONN_MAX_AGE': None,
    }
}


##################################################################################################
# Logging & Error Reporting

# By default, we write reasonably important things (INFO and above) to the console
# We email admins on a site error or a security issue and also propagate
# this up to the Heroku logs. This is obviously overriden in the development settings.

LOGGING = {
    'version': 1,

    'handlers': {
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
        },
        'mail_admins': {
            'level': 'WARNING',
            'class': 'django.utils.log.AdminEmailHandler'
        },
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
        'django.security': {
            'handlers': ['mail_admins'],
            'level': 'WARNING',
            'propagate': True,
        },
        '': {
            'handlers': ['console'],
            'level': 'INFO',
        },
    },
}

##################################################################################################
# Email
#
# We use AWS SES for sending email (except on development, where we override this)

EMAIL_HOST = "email-smtp.us-east-1.amazonaws.com"
EMAIL_HOST_USER = "AKIAIDQJEDLNTSM73G7A"
EMAIL_HOST_PASSWORD = os.environ['AWS_EMAIL_PASSWORD']
EMAIL_USE_TLS = True

##################################################################################################
# Caches
#
# We use AWS SES for sending email (except on development, where we override this)

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.PyLibMCCache',
        'LOCATION': '127.0.0.1:11211',
        'TIMEOUT': 600,
        'KEY_PREFIX': 'otessier-com',
    }
}

TEMPLATE_LOADERS = (
    ('django.template.loaders.cached.Loader', (
        'django.template.loaders.filesystem.Loader',
        'django.template.loaders.app_directories.Loader',
    )),
)

MIDDLEWARE_CLASSES = (
    ('otessier.cache.PreviewAwareUpdateCacheMiddleware',) +
    MIDDLEWARE_CLASSES +
    ('django.middleware.cache.FetchFromCacheMiddleware',)
)

CACHE_MIDDLEWARE_ALIAS = 'default'
CACHE_MIDDLEWARE_SECONDS = 600
CACHE_MIDDLEWARE_KEY_PREFIX = 'otessier-com-site'