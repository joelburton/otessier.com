from django.test import TestCase, SimpleTestCase, override_settings
from django.core import mail

from consulting.models import Consultant, QAndA, Quote

# FIXME: a little anemic

class HomepageTests(TestCase):
    def testHomepage(self):
        response = self.client.get('/')
        self.assertContains(response, 'Welcome', status_code=200)

