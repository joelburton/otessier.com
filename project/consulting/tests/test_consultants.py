from django.test import override_settings, TestCase

from consulting.models import Consultant
from .factories import ConsultantFactory


class ConsultantModelTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.consultant = ConsultantFactory()

    def test_model(self):
        self.consultant.full_clean()

    def test_ordering(self):
        joel = self.consultant
        zed = ConsultantFactory(title="Zed Zenefits", position=1)
        albert = ConsultantFactory(title="Albert Allington", position=1)
        bob = ConsultantFactory(title="Bob Slob", position=2)

        self.assertEqual(list(Consultant.objects.all()), [albert, joel, zed, bob])

    def test_url(self):
        self.assertEqual(self.consultant.get_absolute_url(), '/consultants/joel-burton/')


class ConsultantViewTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        from django.core import management

        management.call_command("installwatson")

    def setUp(self):
        self.consultant = ConsultantFactory()

    def test_missing(self):
        response = self.client.get('/consultants/')
        self.assertNotContains(response, 'Joel Burton', status_code=200)

        response = self.client.get('/consultants/joel-burton/')
        self.assertEqual(response.status_code, 404)

    def test_published(self):
        self.consultant.status = 'published'
        self.consultant.save()

        response = self.client.get('/consultants/')
        self.assertContains(response, '<a href="/consultants/joel-burton/">Joel Burton</a>', status_code=200)
        self.assertContains(response, 'Description of Consultant', status_code=200)

        response = self.client.get('/consultants/joel-burton/')
        self.assertContains(response, 'Joel Burton', status_code=200)

    def test_search_not_published(self):
        response = self.client.get('/search/?q=joel')
        self.assertNotContains(response, 'Joel Burton', status_code=200)

    def test_search_published(self):
        # we only index published stuff, so this needs to be published
        self.consultant.status = 'published'
        self.consultant.save()
        response = self.client.get('/search/?q=joel')
        self.assertContains(response, 'Joel Burton', status_code=200)
        self.assertContains(response, 'Description of Consultant', status_code=200)

    def test_portlet(self):
        # Make a published consultant so we can get a page view
        oliver = ConsultantFactory(title="Oliver Tessier", status='published')
        response = self.client.get('/consultants/oliver-tessier/')

        self.assertNotContains(response, "Joel Burton", status_code=200)

        self.consultant.status = 'published'
        self.consultant.save()

        response = self.client.get('/consultants/oliver-tessier/')
        self.assertContains(response, """
            <div class="panel panel-default">
                <div class="panel-heading"><h3 class="panel-title">Who We Are</h3></div>
                <ul class="list-group">
                    <li class="list-group-item"><a href="/consultants/joel-burton/">Joel Burton</a></li>
                    <li class="list-group-item"><b>Oliver Tessier</b></li>
                </ul>
            </div>
        """, status_code=200, html=True)


@override_settings(PREVIEW_MODE=True)
class ConsultantAdminViewTests(TestCase):
    """Tests using preview mode."""

    @classmethod
    def setUpTestData(cls):
        from django.core import management

        management.call_command("installwatson")

    def setUp(self):
        self.consultant = ConsultantFactory()

    def test_admin_there(self):
        response = self.client.get('/consultants/')
        self.assertContains(response, 'Joel Burton', status_code=200)
        self.assertTemplateUsed(response, 'consulting/consultant_list.html')

        response = self.client.get('/consultants/joel-burton/')
        self.assertContains(response, 'Joel Burton', status_code=200)
        self.assertTemplateUsed(response, 'consulting/consultant_detail.html')
