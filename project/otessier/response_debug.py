"""Add a debug method onto the response object, as a convenience for tests."""

import re

from django.http import HttpResponse
from django.test import TestCase


def _debug(self, tag="***"):
    """Print response body, first removing blank lines."""

    print("\n", tag, self)
    content = re.sub(r"\n\s*\n", "\n", self.content.decode("utf8"))
    print(content)


def add_debug_to_response():
    """Monkey-patch the debug method onto Django's normal HttpResponse."""

    HttpResponse.debug = _debug
    TestCase.maxDiff = None

