from django.test import TestCase


class HomepageTests(TestCase):
    def testHomepage(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Welcome', response.content)