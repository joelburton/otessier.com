from django.test import TestCase, SimpleTestCase, override_settings
from django.core import mail

from consulting.models import Consultant, QAndA, Client, Quote


class HomepageTests(TestCase):
    def testHomepage(self):
        response = self.client.get('/')
        self.assertContains(response, 'Welcome', status_code=200)


class ConsultantTests(TestCase):
    def setUp(self):
        from django.core import management

        management.call_command("installwatson")
        self.consultant = Consultant.objects.create(
            slug='senor-frog',
            title='Senor Frog',
            description='Awesome',
            body='<i>OT!</i>',
            position=1,
        )

    def test_nonadmin_missing(self):
        response = self.client.get('/consultants/')
        self.assertNotContains(response, 'Senor Frog', status_code=200)

        response = self.client.get('/consultants/senor-frog/')
        self.assertEqual(response.status_code, 404)

    @override_settings(PREVIEW_MODE=True)
    def test_admin_there(self):
        response = self.client.get('/consultants/')
        self.assertContains(response, 'Senor Frog', status_code=200)
        self.assertTemplateUsed(response, 'consulting/consultant_list.html')

        response = self.client.get('/consultants/senor-frog/')
        self.assertContains(response, 'Senor Frog', status_code=200)
        self.assertTemplateUsed(response, 'consulting/consultant_detail.html')

    def test_nonadmin_published(self):
        self.consultant.status = 'published'
        self.consultant.save()

        response = self.client.get('/consultants/')
        self.assertContains(response, 'Senor Frog', status_code=200)

        response = self.client.get('/consultants/senor-frog/')
        self.assertContains(response, 'Senor Frog', status_code=200)

    def test_search_not_published(self):
        response = self.client.get('/search/?q=frog')
        self.assertNotContains(response, 'Senor Frog', status_code=200)

    def test_search_published(self):
        # we only index published stuff, so this needs to be published
        self.consultant.status = 'published'
        self.consultant.save()
        response = self.client.get('/search/?q=frog')
        self.assertContains(response, 'Senor Frog', status_code=200)

    @override_settings(PREVIEW_MODE=True)
    def test_admin_portlets(self):
        response = self.client.get('/consultants/senor-frog/')
        self.assertEqual(list(response.context['consultant_list']), [self.consultant])

    @override_settings(PREVIEW_MODE=True)
    def test_missing_portlets(self):
        response = self.client.get('/consultants/senor-frog/')
        self.assertNotContains(response, "Our Clients Say", status_code=200)
        self.assertNotContains(response, "Our Nonprofit Q&amp;A", status_code=200)

    @override_settings(PREVIEW_MODE=True)
    def test_present_portlets(self):
        qanda = QAndA.objects.create(slug="q",
                                     title="MyQuestion",
                                     description="Descrip",
                                     question="Why is the Sky blue?",
                                     answer="Because.",
                                     status='published',
        )
        quote = Quote.objects.create(quote='MyQuote', author='Bob', status='published')

        # client = Client.objects.create(slug='c',
        #                                title='MyClient',
        #                                organization='MyOrg',
        #                                description='Descrip',
        #                                body='My body',
        #                                status='published',
        # )

        response = self.client.get('/consultants/senor-frog/')
        self.assertContains(response, "Our Clients Say")
        self.assertContains(response, "MyQuote")
        self.assertContains(response, "Nonprofit Q&amp;A")
        self.assertContains(response, "MyQuestion")


class TestContactUsForm(SimpleTestCase):

    def test_contact_submission(self):
        self.assertEqual(len(mail.outbox), 0)
        response = self.client.post('/contact-info/', {'subject': 'MySubject',
                                                       'from_email': 'test@test.com',
                                                       'body': 'MyBody'})
        self.assertRedirects(response, '/', target_status_code=200)
        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(mail.outbox[0].subject, '[Contact Us Form] MySubject')
        self.assertEqual(mail.outbox[0].body, 'MyBody')
