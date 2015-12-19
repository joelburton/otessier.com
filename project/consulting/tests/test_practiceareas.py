from django.test import override_settings, TestCase

from consulting.models import PracticeArea
from .factories import PracticeAreaFactory, ClientWorkFactory, ClientFactory


class PracticeAreaModelTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.area = PracticeAreaFactory()

    def test_model(self):
        self.area.full_clean()
        self.assertEqual(str(self.area), 'Coaching')

    def test_ordering(self):
        coaching = self.area
        jumping = PracticeAreaFactory(title="Jumping", position=1)
        dancing = PracticeAreaFactory(title="Dancing", position=1)
        arguing = PracticeAreaFactory(title="Arguing", position=2)

        self.assertEqual(list(PracticeArea.objects.all()), [coaching, dancing, jumping, arguing])

    def test_url(self):
        self.assertEqual(self.area.get_absolute_url(), '/practices/coaching/')


class PracticeAreaViewTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        from django.core import management

        management.call_command("installwatson")

    def setUp(self):
        self.area = PracticeAreaFactory()

    def test_missing(self):
        response = self.client.get('/practices/')
        self.assertNotContains(response, 'Coaching', status_code=200)

        response = self.client.get('/practices/coaching/')
        self.assertEqual(response.status_code, 404)

    def test_published(self):
        self.area.status = 'published'
        self.area.save()

        response = self.client.get('/practices/')
        self.assertContains(response, '<a href="/practices/coaching/">Coaching</a>', status_code=200, html=True)
        self.assertContains(response, 'Description of PracticeArea', status_code=200)

        response = self.client.get('/practices/coaching/')
        self.assertContains(response,
                            '<h1>Coaching<i class="pull-right fa fa-coaching"></i></h1>',
                            status_code=200,
                            html=True)

    def test_search_not_published(self):
        response = self.client.get('/search/?q=coaching')
        self.assertNotContains(response, 'Coaching', status_code=200)

    def test_search_published(self):
        # we only index published stuff, so this needs to be published
        self.area.status = 'published'
        self.area.save()
        response = self.client.get('/search/?q=coaching')
        self.assertContains(response, 'Coaching', status_code=200)
        self.assertContains(response, 'Description of PracticeArea', status_code=200)

    def test_portlet(self):
        # Make a published area so we can get a page view
        dancing = PracticeAreaFactory(title="Dancing", status='published')
        response = self.client.get('/practices/dancing/')

        self.assertNotContains(response, "Coaching", status_code=200)

        self.area.status = 'published'
        self.area.save()

        response = self.client.get('/practices/dancing/')
        self.assertContains(response, """
            <div class="panel panel-default">
                <div class="panel-heading"><h3 class="panel-title">Practices</h3></div>
                <ul class="list-group">
                    <li class="list-group-item"><a href="/practices/coaching/"><i class="fa fa-coaching"></i> Coaching</a></li>
                    <li class="list-group-item"><b><i class="fa fa-dancing"></i> Dancing</b></li>
                </ul>
            </div>
        """, status_code=200, html=True)

    def test_show_clients(self):
        ibm = ClientFactory(status='published')
        ibm.practiceareas.add(self.area)

        self.area.status = 'published'
        self.area.save()

        response = self.client.get("/practices/")
        self.assertContains(
            response,
            """<ul class="barlist"><li><a href="/clients/ibm/">IBM</a></li></ul>""",
            html=True,
        )

        response = self.client.get("/practices/coaching/")
        self.assertContains(
            response,
            """<ul><li><a href="/clients/ibm/">IBM</a></li></ul>""",
            html=True,
        )


@override_settings(PREVIEW_MODE=True)
class PracticeAreaAdminViewTests(TestCase):
    """Tests using preview mode."""

    @classmethod
    def setUpTestData(cls):
        from django.core import management

        management.call_command("installwatson")

    def setUp(self):
        self.area = PracticeAreaFactory()

    def test_admin_there(self):
        response = self.client.get('/practices/')
        self.assertContains(response, 'Coaching', status_code=200)
        self.assertTemplateUsed(response, 'consulting/practicearea_list.html')

        response = self.client.get('/practices/coaching/')
        self.assertContains(response,
                            '<h1>Coaching<i class="pull-right fa fa-coaching"></i></h1>',
                            status_code=200,
                            html=True)
        self.assertTemplateUsed(response, 'consulting/practicearea_detail.html')
