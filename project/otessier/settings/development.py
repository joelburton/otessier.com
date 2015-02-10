"""
Development settings for otessier project.
"""

from .base import *


SECRET_KEY = 'i^ari$22!b+&pwhm=o7h-%vr-%us)#k=q0!g9qcaz*a#!h!k*c'

DEBUG = True
TEMPLATE_DEBUG = True

INSTALLED_APPS += (
    'debug_toolbar',
    'memcache_toolbar',
    'django_extensions',
)

MIDDLEWARE_CLASSES += (
    'otessier.timing.TimingMiddleware',
)


##################################################################################################
# Database

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

# Blather on about every little thing that happens. We programmers get lonely.

LOGGING = {
    'disable_existing_loggers': False,
    'version': 1,
    'filters': {
        'readable_sql': {
            '()': 'project_runpy.ReadableSqlFilter',
        },
    },
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(name)s %(message)s'
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'project_runpy.ColorizingStreamHandler',
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
            'filters': ['readable_sql'],
            'propagate': False,
        }
    },
}

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
    }
}

# Uncomment to debug basic memcache stuff
#
# CACHES = {
#     'default': {
#         'BACKEND': 'django.core.cache.backends.memcached.PyLibMCCache',
#         'LOCATION': '127.0.0.1:11211',
#         'TIMEOUT': 600,
#         'KEY_PREFIX': 'otessier-com',
#     }
# }

if 'memcached' in CACHES['default']['BACKEND']:
    DEBUG_TOOLBAR_PANELS = [
        'debug_toolbar.panels.versions.VersionsPanel',
        'debug_toolbar.panels.timer.TimerPanel',
        'debug_toolbar.panels.settings.SettingsPanel',
        'debug_toolbar.panels.headers.HeadersPanel',
        'debug_toolbar.panels.request.RequestPanel',
        'debug_toolbar.panels.sql.SQLPanel',
        'debug_toolbar.panels.staticfiles.StaticFilesPanel',
        'debug_toolbar.panels.templates.TemplatesPanel',
        'debug_toolbar.panels.cache.CachePanel',
        'debug_toolbar.panels.signals.SignalsPanel',
        'debug_toolbar.panels.logging.LoggingPanel',
        'memcache_toolbar.panels.pylibmc.PylibmcPanel',  # <-- this is new
        'debug_toolbar.panels.redirects.RedirectsPanel',
    ]

    import memcache_toolbar.panels.pylibmc
