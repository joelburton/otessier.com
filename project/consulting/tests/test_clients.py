from django.test import override_settings, TestCase

from consulting.models import Client, ClientWork, ClientReference
from .factories import ClientFactory, ClientReferenceFactory, ClientWorkFactory, PracticeAreaFactory


class ClientModelTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.ibm = ClientFactory()

    def test_model(self):
        self.ibm.full_clean()
        self.assertEqual(str(self.ibm), 'IBM')

    def test_ordering(self):
        ibm = self.ibm
        xerox = ClientFactory(title="Xerox", position=1)
        apple = ClientFactory(title="Apple", position=1)
        msoft = ClientFactory(title="Microsloth", position=2)

        self.assertEqual(list(Client.objects.all()), [apple, ibm, xerox, msoft])

    def test_url(self):
        self.assertEqual(self.ibm.get_absolute_url(), '/clients/ibm/')


class ClientReferenceModelTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.herman = ClientReferenceFactory()

    def test_model(self):
        self.herman.full_clean()
        self.assertEqual(str(self.herman), 'Herman Miller')

    def test_ordering(self):
        herman = self.herman
        aaron = ClientReferenceFactory(title="Aaron", position=3)
        jane = ClientReferenceFactory(title="Jane", position=2)

        self.assertEqual(list(ClientReference.objects.all()), [herman, jane, aaron])


class ClientWorkModelTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.coaching = ClientWorkFactory()

    def test_model(self):
        self.coaching.full_clean()
        self.assertEqual(str(self.coaching), 'Coaching Project')

    def test_ordering(self):
        coaching = self.coaching
        arguing = ClientWorkFactory(title="Arguing", position=3)
        dancing = ClientWorkFactory(title="Dancing", position=1)

        self.assertEqual(list(ClientWork.objects.all()), [coaching, dancing, arguing])


class ClientViewTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        from django.core import management

        management.call_command("installwatson")

    def setUp(self):
        self.ibm = ClientFactory()
        self.herman = ClientReferenceFactory()
        self.ibm_coaching = ClientWorkFactory()
        self.coaching = PracticeAreaFactory()

        self.ibm_coaching.references.add(self.herman)
        self.ibm.practiceareas.add(self.coaching)

    def test_missing(self):
        response = self.client.get('/clients/')
        self.assertNotContains(response, 'IBM', status_code=200)

        response = self.client.get('/clients/ibm/')
        self.assertEqual(response.status_code, 404)

    def test_published_list_no_areas(self):
        self.ibm.status = 'published'
        self.ibm.save()

        response = self.client.get('/clients/')
        self.assertContains(response, '<a href="/clients/ibm/">IBM</a>', status_code=200, html=True)
        self.assertContains(response, 'Description of Client', status_code=200)

        self.assertNotContains(response, "Practice Areas", html=True)

    def test_published_list_published_areas(self):
        self.ibm.status = 'published'
        self.ibm.save()

        self.coaching.status = 'published'
        self.coaching.save()

        response = self.client.get('/clients/')
        self.assertContains(response, '<a href="/clients/ibm/">IBM</a>', status_code=200, html=True)
        self.assertContains(response, 'Description of Client', status_code=200)

        self.assertContains(
                response,
                """
                <div class="small">
                    Practice Areas:
                    <ul class="barlist">
                        <li>
                            <a href="/practices/coaching/">
                                <span class="fa fa-coaching"></span>
                                &nbsp;Coaching
                            </a>
                        </li>
                    </ul>
                </div>
                """, html=True)

    def test_published_detail(self):
        self.ibm.status = 'published'
        self.ibm.save()

        response = self.client.get('/clients/ibm/')
        self.assertContains(
                response,
                '<h1>IBM</h1>',
                status_code=200,
                html=True)

        self.assertNotContains(response, "Practice Areas", html=True)
        self.assertNotContains(
                response,
                "<h3>Coaching Project</h3>",
                status_code=200,
                html=True)

        # Now let's publish the work and make sure it appears

        self.coaching.status = 'published'
        self.coaching.save()

        self.ibm_coaching.status = 'published'
        self.ibm_coaching.save()

        response = self.client.get('/clients/ibm/')

        self.assertContains(
                response,
                "<h3>Coaching Project</h3>",
                status_code=200,
                html=True)

        self.assertContains(
                response,
                """
                <ul class="barlist">
                    <li>
                        <a href="/practices/coaching/">
                            <i class="fa fa-coaching"></i>
                            &nbsp;Coaching
                        </a>
                    </li>
                </ul>
                """, html=True)

    def test_search_not_published(self):
        response = self.client.get('/search/?q=ibm')
        self.assertNotContains(response, 'IBM', status_code=200)

    def test_search_published(self):
        # we only index published stuff, so this needs to be published
        self.ibm.status = 'published'
        self.ibm.save()

        response = self.client.get('/search/?q=ibm')
        self.assertContains(response, 'IBM', status_code=200)
        self.assertContains(response, 'Description of Client', status_code=200)

        response = self.client.get('/search/?q=coaching')
        self.assertContains(response, 'IBM', status_code=200)
        self.assertContains(response, 'Description of Client', status_code=200)

        response = self.client.get('/search/?q=herman')
        self.assertContains(response, 'IBM', status_code=200)
        self.assertContains(response, 'Description of Client', status_code=200)

    def test_portlet(self):
        # Make a published area so we can get a page view
        ClientFactory(title="Apple", status='published')
        response = self.client.get('/clients/apple/')

        self.assertNotContains(response, "IBM", status_code=200)

        self.ibm.status = 'published'
        self.ibm.save()

        response = self.client.get('/clients/apple/')
        self.assertContains(response, """
            <div class="panel panel-default">
                <div class="panel-heading"><h3 class="panel-title">Clients</h3></div>
                <ul class="list-group">
                    <li class="list-group-item"><b> Apple</b></li>
                    <li class="list-group-item"><a href="/clients/ibm/"> IBM</a></li>
                </ul>
            </div>
        """, status_code=200, html=True)


@override_settings(PREVIEW_MODE=True)
class ClientAdminViewTests(TestCase):
    """Tests using preview mode."""

    @classmethod
    def setUpTestData(cls):
        from django.core import management

        management.call_command("installwatson")

    def setUp(self):
        self.ibm = ClientFactory()

    def test_admin_there(self):
        response = self.client.get('/clients/')
        self.assertContains(response, 'IBM', status_code=200)
        self.assertTemplateUsed(response, 'consulting/client_list.html')

        response = self.client.get('/clients/ibm/')
        self.assertContains(response,
                            '<h1>IBM</h1>',
                            status_code=200,
                            html=True)
        self.assertTemplateUsed(response, 'consulting/client_detail.html')
