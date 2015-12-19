from django.core.exceptions import ValidationError
from django.test import override_settings, TestCase

from .factories import LibraryCategoryFactory, LibraryFileFactory


class LibraryModelTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.cat = LibraryCategoryFactory()
        cls.file = LibraryFileFactory(url='', title="File Budget")
        cls.web = LibraryFileFactory(asset=None, title="Web Budget")

    def test_validation(self):
        bad = LibraryFileFactory.build()
        self.assertRaises(ValidationError, bad.full_clean)

    def test_model(self):
        self.cat.full_clean()
        self.file.full_clean()
        self.web.full_clean()

    def test_urls(self):
        self.assertEqual(self.cat.get_absolute_url(), '/library/sample-budgets/')
        self.assertEqual(self.web.get_absolute_url(), 'http://url.com/libraryfile')
        self.assertIn("/media/library/file-", self.file.get_absolute_url())
        self.assertRegexpMatches(
                self.file.get_absolute_url(),
                r'^/media/library/file-budget.*txt$')


class LibraryCategoryViewTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        from django.core import management

        management.call_command("installwatson")

    def setUp(self):
        self.cat = LibraryCategoryFactory()

    def test_missing(self):
        response = self.client.get('/library/')
        self.assertNotContains(response, 'Sample Budgets', status_code=200)

        response = self.client.get('/library/sample-budgets/')
        self.assertEqual(response.status_code, 404)

    def test_published(self):
        self.cat.status = 'published'
        self.cat.save()

        response = self.client.get('/library/')
        self.assertContains(
                response,
                '<a href="/library/sample-budgets/">Sample Budgets</a>',
                status_code=200)
        self.assertContains(response, 'Description of LibraryCategory', status_code=200)

        response = self.client.get('/library/sample-budgets/')
        self.assertContains(response, 'Sample Budgets', status_code=200)

    def test_search_not_published(self):
        response = self.client.get('/search/?q=budgets')
        self.assertNotContains(response, 'Sample Budgets', status_code=200)

    def test_search_published(self):
        # we only index published stuff, so this needs to be published
        self.cat.status = 'published'
        self.cat.save()
        response = self.client.get('/search/?q=budgets')
        self.assertContains(response, 'Sample Budgets', status_code=200)
        self.assertContains(response, 'Description of LibraryCategory', status_code=200)

    def test_portlet(self):
        # Make a published cat so we can get a page view
        movies = LibraryCategoryFactory(title="Movies", status='published')
        response = self.client.get('/library/movies/')

        self.assertNotContains(response, "Sample Budgets", status_code=200)

        self.cat.status = 'published'
        self.cat.save()

        response = self.client.get('/library/movies/')

        print response.content

        self.assertContains(response, """
            <div class="panel panel-default">
                <div class="panel-heading"><h3 class="panel-title">Library Categories</h3></div>
                <ul class="list-group">
                    <li class="list-group-item"><b>Movies</b></li>
                    <li class="list-group-item"><a href="/library/sample-budgets/">Sample Budgets</a></li>
                </ul>
            </div>
        """, status_code=200, html=True)


class LibraryFileViewTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        from django.core import management

        management.call_command("installwatson")
        cls.cat = LibraryCategoryFactory(status='published')

    def setUp(self):
        self.web = LibraryFileFactory(asset=None, title="Web Budget")

    def test_missing(self):
        response = self.client.get('/library/sample-budgets/')
        self.assertNotContains(response, 'Web Budget', status_code=200)

    def test_published(self):
        self.web.status = 'published'
        self.web.save()

        response = self.client.get('/library/sample-budgets/')
        self.assertContains(
                response,
                'Web Budget',
                status_code=200)

    def test_search_not_published(self):
        response = self.client.get('/search/?q=web')
        self.assertNotContains(response, 'Web Budget', status_code=200)

    def test_search_published(self):
        # we only index published stuff, so this needs to be published
        self.web.status = 'published'
        self.web.save()
        response = self.client.get('/search/?q=web')
        self.assertContains(response, 'Web Budget', status_code=200)


@override_settings(PREVIEW_MODE=True)
class LibraryFileAdminViewTests(TestCase):
    """Tests using preview mode."""

    @classmethod
    def setUpTestData(cls):
        from django.core import management

        management.call_command("installwatson")
        cls.cat = LibraryCategoryFactory(status='published')

    def setUp(self):
        self.web = LibraryFileFactory(asset=None, title="Web Budget")

    def test_admin_there(self):
        response = self.client.get('/library/sample-budgets/')
        self.assertContains(response, 'Web Budget', status_code=200)

        response = self.client.get('/library/sample-budgets/')
        self.assertContains(response, 'Web Budget', status_code=200)
