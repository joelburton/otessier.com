from django.test import TestCase, override_settings

from consulting.tests.factories import ConsultantFactory, QAndAFactory, QuoteFactory


class PortletTestCase(TestCase):
    def setUp(self):
        self.consultant = ConsultantFactory()

    @override_settings(PREVIEW_MODE=True)
    def test_admin_portlets(self):
        response = self.client.get('/consultants/joel-burton/')
        self.assertEqual(list(response.context['consultant_list']), [self.consultant])

    @override_settings(PREVIEW_MODE=True)
    def test_missing_portlets(self):
        response = self.client.get('/consultants/joel-burton/')
        self.assertNotContains(response, "Our Clients Say", status_code=200)
        self.assertNotContains(response, "Our Nonprofit Q&amp;A", status_code=200)

    @override_settings(PREVIEW_MODE=True)
    def test_present_portlets(self):
        QAndAFactory(status='published')
        QuoteFactory(status='published')

        response = self.client.get('/consultants/joel-burton/')
        self.assertContains(response, "Our Clients Say")
        self.assertContains(response, "Oliver is love.")
        self.assertContains(response, "Nonprofit Q&amp;A")
        self.assertContains(response, "Why do birds sing?")
