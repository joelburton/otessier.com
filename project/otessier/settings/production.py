"""
Deployment settings for otessier project.
"""

import os

from .base import *


SECRET_KEY = os.environ['SECRET_KEY']

ALLOWED_HOSTS = ['127.0.0.1', 'localhost']