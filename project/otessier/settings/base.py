"""
Base settings for otessier project.
"""

import os

##################################################################################################
# Directories

SETTINGS_DIR = os.path.dirname(__file__)
PROJECT_DIR = os.path.abspath(SETTINGS_DIR + "/../..")
GIT_DIR = os.path.abspath(PROJECT_DIR + "/..")

##################################################################################################
# Core Settings

# We keep our template files in the project "template" directory.
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'APP_DIRS': True,
        'DIRS': [os.path.join(PROJECT_DIR, "templates")],
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# BUGFIX: 2015-07-22: imagekit includes a library, 'compat', which clashes with the one in the
# debug toolbar. We need to load imagekit at the end of the installed apps -- but make sure all
# the normal stuff appears before the developer tools, like the debug toolbar. So, for now, let's
# split our apps into non-imagekit and imagekit, so we can add them in this very strict order
# in development.py. At some point, this can be re-evaluated to return to a simple list, once
# imagekit and the debugtoolbar kiss and make up.

NONIMAGEKIT_INSTALLED_APPS = (
    'django_admin_bootstrapped',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'model_utils',  # provides TimestampedModel, StatusModel
    'bootstrap3',  # provides bootstrap tags, forms
    'otessier',
    'consulting.apps.ConsultingAppConfig',  # core product for OTessier consulting
    'watson',  # search
    'solo',  # SiteConfiguration object
    'tinymce',  # HTML editor
    'dbbackup',  # management commands for backing up DB
)

IMAGEKIT_APPS = (
    'imagekit',  # resizes images
)

INSTALLED_APPS = NONIMAGEKIT_INSTALLED_APPS + IMAGEKIT_APPS

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'otessier.previewmode.PreviewMiddleware',  # <-- added
)

ROOT_URLCONF = 'otessier.urls'

WSGI_APPLICATION = 'otessier.wsgi.application'

TIME_ZONE = 'UTC'
USE_TZ = True

LANGUAGE_CODE = 'en-us'
USE_I18N = True
USE_L10N = True

##################################################################################################
# Media/Static Files
#
# This site doesn't do anything fancy for media/static--they're just kept on
# the filesystem. If we deployed at a PaaS place, we'd want to move to S3.

# Where we want to store media files.
MEDIA_ROOT = GIT_DIR + "/media/"
MEDIA_URL = "/media/"

# Where we want to store static files.
STATIC_ROOT = GIT_DIR + "/static/"
STATIC_URL = "/static/"

# We keep our collected static source files in the "static" directory.
STATICFILES_DIRS = [os.path.join(PROJECT_DIR, "static")]

##################################################################################################
# Sessions
#
# We don't need any server-side storage of sessions, so just use cookies

SESSION_ENGINE = 'django.contrib.sessions.backends.signed_cookies'

##################################################################################################
# django-solo SiteConfiguration cache
#
# Cache the django-solo SiteConfiguration object for 5 mins
# In development, we might be using the DummyCache so this is a no-op cache there.

SOLO_CACHE = 'default'
SOLO_CACHE_TIMEOUT = 60 * 5

##################################################################################################
# Admin emails
#
# Email these people when errors happen on production sites

ADMINS = (('Joel', 'joel@joelburton.com'),)
SERVER_EMAIL = "joel@joelburton.com"
DEFAULT_FROM_EMAIL = 'joel@joelburton.com'

##################################################################################################
# TinyMCE (HTML editor)
#
# Simplify the TinyMCE to remove a lot of un-needed UI complexity

TINYMCE_JS_URL = "http://tinymce.cachefly.net/4.2/tinymce.min.js"
TINYMCE_DEFAULT_CONFIG = {
    'plugins': "paste,link",
    'cleanup_on_startup': True,
    'custom_undo_redo_levels': 10,
    'height': 100,
    'menubar': False,
    'toolbar': 'undo redo | cut copy paste pastetext | styleselect | removeformat | bold italic'
               ' | bullist numlist | blockquote | link unlink',
}
TINYMCE_SPELLCHECKER = False
TINYMCE_COMPRESSOR = False

##################################################################################################
# Backup config
#
# from django-dbbackup

DBBACKUP_DATE_FORMAT = ''
DBBACKUP_BACKUP_DIRECTORY = GIT_DIR + '/backups/'

##################################################################################################
# Bootstrap / Bootstrap Admin

# Use Bootstrap for rendering admin fields
DAB_FIELD_RENDERER = 'django_admin_bootstrapped.renderers.BootstrapFieldRenderer'

# 'required' html5 attribute does not play well with FF/Chrome and TinyMCE
BOOTSTRAP3 = {
    'set_required': False
}
