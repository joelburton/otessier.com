from django.test import TestCase

from .factories import QuoteFactory


class QuoteModelTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.quote = QuoteFactory()

    def test_model(self):
        self.quote.full_clean()


class QuoteViewTests(TestCase):

    def setUp(self):
        self.quote = QuoteFactory()

    def test_missing(self):
        response = self.client.get('/library/')
        self.assertNotContains(response, 'Oliver is love.?', status_code=200)

    def test_published(self):
        self.quote.status = 'published'
        self.quote.save()

        response = self.client.get('/library/')
        self.assertContains(response, 'Oliver is love.', status_code=200)
        self.assertContains(response, 'Gandhi', status_code=200)
