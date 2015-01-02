"""
Base settings for otessier project.
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

SETTINGS_DIR = os.path.dirname(__file__)
PROJECT_DIR = os.path.abspath(SETTINGS_DIR + "/../..")
GIT_DIR = os.path.abspath(PROJECT_DIR + "/..")

# Where we want to store media files. This setting is ignored when we're using S3 storage.
MEDIA_ROOT = GIT_DIR + "/media/"
MEDIA_URL = "/media/"

# Where we want to store static files. This settings is ignored when we're using S3 storage.
STATIC_ROOT = GIT_DIR + "/static/"
STATIC_URL = "/static/"

# We keep our static source files in the "static" directory.
STATICFILES_DIRS = [os.path.join(PROJECT_DIR, "static")]

# We keep our template files in the project "template" directory.
TEMPLATE_DIRS = (os.path.join(PROJECT_DIR, "templates"),)

INSTALLED_APPS = (
    'grappelli',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.webdesign',
    'model_utils',
    'bootstrap3',
    'consulting',
    'watson',
    'imagekit',
    'solo',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'otessier.urls'

WSGI_APPLICATION = 'otessier.wsgi.application'


LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

DEFAULT_FROM_EMAIL = 'joel@joelburton.com'

SESSION_ENGINE = 'django.contrib.sessions.backends.signed_cookies'

GRAPPELLI_ADMIN_TITLE = "Oliver Tessier and Associates Admin"

TEMPLATE_CONTEXT_PROCESSORS = [
    'django.core.context_processors.request',
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.tz',
    'django.contrib.messages.context_processors.messages',
    'consulting.context_processors.random_quote',
    'consulting.context_processors.random_qanda',
    'consulting.context_processors.site_navigation',
]
