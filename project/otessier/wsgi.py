"""
WSGI config for otessier project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/howto/deployment/wsgi/
"""

from django.core.wsgi import get_wsgi_application
from dotenv import load_dotenv

load_dotenv(verbose=True)

application = get_wsgi_application()
