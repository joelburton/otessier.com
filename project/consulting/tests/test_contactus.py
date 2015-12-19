from django.core import mail
from django.test import TestCase


class TestContactUsForm(TestCase):
    def test_contact_submission(self):
        self.assertEqual(len(mail.outbox), 0)
        response = self.client.post('/contact-info/', {'subject': 'MySubject',
                                                       'from_email': 'test@test.com',
                                                       'body': 'MyBody'})
        self.assertRedirects(response, '/', target_status_code=200)
        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(mail.outbox[0].subject, '[Contact Us Form] MySubject')
        self.assertEqual(mail.outbox[0].body, 'MyBody')
