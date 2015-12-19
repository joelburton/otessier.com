from django.test import override_settings, TestCase

from consulting.models import QAndA
from .factories import QAndAFactory


class QAndAModelTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.qanda = QAndAFactory()

    def test_model(self):
        self.qanda.full_clean()

    def test_ordering(self):
        why = self.qanda
        are = QAndAFactory(title="Are kittens real?", position=1)
        do = QAndAFactory(title="Do penguins fly?", position=1)
        can = QAndAFactory(title="Can mice sleep?", position=2)

        self.assertEqual(list(QAndA.objects.all()), [do, are, why, can])

    def test_url(self):
        self.assertEqual(self.qanda.get_absolute_url(), '/questions/why-do-birds-sing/')


class QAndAViewTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        from django.core import management

        management.call_command("installwatson")

    def setUp(self):
        self.qanda = QAndAFactory()

    def test_missing(self):
        response = self.client.get('/questions/')
        self.assertNotContains(response, 'Why do birds sing?', status_code=200)

        response = self.client.get('/questions/why-do-birds-sing/')
        self.assertEqual(response.status_code, 404)

    def test_published(self):
        self.qanda.status = 'published'
        self.qanda.save()

        response = self.client.get('/questions/')
        self.assertContains(response, '<a href="/questions/why-do-birds-sing/">Why do birds sing?</a>', status_code=200)
        self.assertContains(response, 'Description of QAndA', status_code=200)

        response = self.client.get('/questions/why-do-birds-sing/')
        self.assertContains(response, '<h1>Why do birds sing?</h1>', status_code=200)

    def test_search_not_published(self):
        response = self.client.get('/search/?q=birds')
        self.assertNotContains(response, 'Why do birds sing?', status_code=200)

    def test_search_published(self):
        # we only index published stuff, so this needs to be published
        self.qanda.status = 'published'
        self.qanda.save()
        response = self.client.get('/search/?q=birds')
        self.assertContains(response, 'Why do birds sing?', status_code=200)
        self.assertContains(response, 'Description of QAndA', status_code=200)

    def test_portlet_list(self):
        # Make a published qanda so we can get a page view
        love = QAndAFactory(title="Can penguins love?", status='published')
        response = self.client.get('/questions/can-penguins-love/')

        self.assertNotContains(response, "Why do birds sing?", status_code=200)

        self.qanda.status = 'published'
        self.qanda.save()

        response = self.client.get('/questions/can-penguins-love/')
        self.assertContains(response, """
            <div class="panel panel-default">
                <div class="panel-heading"><h3 class="panel-title">Nonprofit Q&amp;A</h3></div>
                <ul class="list-group">
                    <li class="list-group-item"><b>Can penguins love?</b></li>
                    <li class="list-group-item"><a href="/questions/why-do-birds-sing/">Why do birds sing?</a></li>
                </ul>
            </div>
        """, status_code=200, html=True)

    def test_portlet_random_everywhere(self):
        """Does random qanda portlet work on site?"""

        response = self.client.get('/library/')

        self.assertNotContains(response, "Why do birds sing?", status_code=200)

        self.qanda.status = 'published'
        self.qanda.save()

        response = self.client.get('/library/')

        print response.content

        self.assertContains(response, """
            <div class="panel panel-default">
                <div class="panel-heading"><h3 class="panel-title">Nonprofit Q&amp;A</h3></div>
                <div class="panel-body">
                    <p><b><a href="/questions/why-do-birds-sing/">Why do birds sing?</a></b></p>
                    Description of QAndA.
                    <a href="/questions/why-do-birds-sing/">Read the answer&hellip;</a>
                </div>
            </div>
            """, status_code=200, html=True)


@override_settings(PREVIEW_MODE=True)
class QAndAAdminViewTests(TestCase):
    """Tests using preview mode."""

    @classmethod
    def setUpTestData(cls):
        from django.core import management

        management.call_command("installwatson")

    def setUp(self):
        self.qanda = QAndAFactory()

    def test_admin_there(self):
        response = self.client.get('/questions/')
        self.assertContains(response, 'Why do birds sing?', status_code=200)
        self.assertTemplateUsed(response, 'consulting/qanda_list.html')

        response = self.client.get('/questions/why-do-birds-sing/')
        self.assertContains(response, 'Why do birds sing?', status_code=200)
        self.assertTemplateUsed(response, 'consulting/qanda_detail.html')
