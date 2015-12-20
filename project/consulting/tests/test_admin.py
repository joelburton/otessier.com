from django.contrib.auth.models import User
from django.test import TestCase

from consulting.tests.factories import ClientFactory, PracticeAreaFactory, ConsultantFactory, QAndAFactory, QuoteFactory, \
    LibraryCategoryFactory, LibraryFileFactory


class AdminTestCase(TestCase):
    """These are basic tests, but enough to prove the admin views aren't totally broken."""

    @classmethod
    def setUpTestData(cls):
        User.objects.create_superuser("admin", "admin@admin.com", "password")

    def setUp(self):
        self.client.login(username='admin', password='password')

    def test_practicearea_list(self):
        results = self.client.get("/admin/consulting/practicearea/")
        self.assertEqual(results.status_code, 200)

    def test_practicearea(self):
        obj = PracticeAreaFactory()
        results = self.client.get("/admin/consulting/practicearea/%s/change/" % obj.pk)
        self.assertEqual(results.status_code, 200)

    def test_client_list(self):
        results = self.client.get("/admin/consulting/client/")
        self.assertEqual(results.status_code, 200)

    def test_client(self):
        obj = ClientFactory()
        results = self.client.get("/admin/consulting/client/%s/change/" % obj.pk)
        self.assertEqual(results.status_code, 200)

    def test_consultant_list(self):
        results = self.client.get("/admin/consulting/consultant/")
        self.assertEqual(results.status_code, 200)

    def test_consultant(self):
        obj = ConsultantFactory()
        results = self.client.get("/admin/consulting/consultant/%s/change/" % obj.pk)
        self.assertEqual(results.status_code, 200)

    def test_qanda_list(self):
        results = self.client.get("/admin/consulting/qanda/")
        self.assertEqual(results.status_code, 200)

    def test_qanda(self):
        obj = QAndAFactory()
        results = self.client.get("/admin/consulting/qanda/%s/change/" % obj.pk)
        self.assertEqual(results.status_code, 200)

    def test_quote_list(self):
        results = self.client.get("/admin/consulting/quote/")
        self.assertEqual(results.status_code, 200)

    def test_quote(self):
        obj = QuoteFactory()
        results = self.client.get("/admin/consulting/quote/%s/change/" % obj.pk)
        self.assertEqual(results.status_code, 200)

    def test_librarycategory_list(self):
        results = self.client.get("/admin/consulting/librarycategory/")
        self.assertEqual(results.status_code, 200)

    def test_librarycategory(self):
        obj = LibraryCategoryFactory()
        results = self.client.get("/admin/consulting/librarycategory/%s/change/" % obj.pk)
        self.assertEqual(results.status_code, 200)

    def test_libraryfile_list(self):
        results = self.client.get("/admin/consulting/libraryfile/")
        self.assertEqual(results.status_code, 200)

    def test_libraryfile(self):
        obj = LibraryFileFactory()
        results = self.client.get("/admin/consulting/libraryfile/%s/change/" % obj.pk)
        self.assertEqual(results.status_code, 200)
