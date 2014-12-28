"""
Deployment settings for otessier project.
"""

import os

from .base import *


SECRET_KEY = os.environ['SECRET_KEY']