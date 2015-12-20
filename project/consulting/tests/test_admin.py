from django.contrib.auth.models import User
from django.test import TestCase

from consulting.tests.factories import ClientFactory, PracticeAreaFactory, ConsultantFactory, QAndAFactory, QuoteFactory, \
    LibraryCategoryFactory, LibraryFileFactory


class AdminTestCase(TestCase):
    """These are basic tests, but enough to prove the admin views aren't totally broken."""

    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_superuser("admin", "admin@admin.com", "password")

    def setUp(self):
        self.client.force_login(self.user)


class PracticeAreaTestCase(AdminTestCase):

    def setUp(self):
        AdminTestCase.setUp(self)
        self.obj = PracticeAreaFactory()

    def test_practicearea_list(self):
        results = self.client.get("/admin/consulting/practicearea/")
        self.assertEqual(results.status_code, 200)

    def test_practicearea(self):
        results = self.client.get("/admin/consulting/practicearea/%s/change/" % self.obj.pk)
        self.assertEqual(results.status_code, 200)


class ClientTestCase(AdminTestCase):

    def setUp(self):
        AdminTestCase.setUp(self)
        self.obj = ClientFactory()

    def test_client_list(self):
        results = self.client.get("/admin/consulting/client/")
        self.assertEqual(results.status_code, 200)

    def test_client(self):
        results = self.client.get("/admin/consulting/client/%s/change/" % self.obj.pk)
        self.assertEqual(results.status_code, 200)


class ConsultantTestCase(AdminTestCase):

    def setUp(self):
        AdminTestCase.setUp(self)
        self.obj = ConsultantFactory()

    def test_consultant_list(self):
        results = self.client.get("/admin/consulting/consultant/")
        self.assertEqual(results.status_code, 200)

    def test_consultant(self):
        results = self.client.get("/admin/consulting/consultant/%s/change/" % self.obj.pk)
        self.assertEqual(results.status_code, 200)


class QAndATestCase(AdminTestCase):

    def setUp(self):
        AdminTestCase.setUp(self)
        self.obj = QAndAFactory()

    def test_qanda_list(self):
        results = self.client.get("/admin/consulting/qanda/")
        self.assertEqual(results.status_code, 200)

    def test_qanda(self):
        results = self.client.get("/admin/consulting/qanda/%s/change/" % self.obj.pk)
        self.assertEqual(results.status_code, 200)


class QuoteTestCase(AdminTestCase):

    def setUp(self):
        AdminTestCase.setUp(self)
        self.obj = QuoteFactory()

    def test_quote_list(self):
        results = self.client.get("/admin/consulting/quote/")
        self.assertEqual(results.status_code, 200)

    def test_quote(self):
        results = self.client.get("/admin/consulting/quote/%s/change/" % self.obj.pk)
        self.assertEqual(results.status_code, 200)


class LibraryCategoryTestCase(AdminTestCase):

    def setUp(self):
        AdminTestCase.setUp(self)
        self.obj = LibraryCategoryFactory()

    def test_librarycategory_list(self):
        results = self.client.get("/admin/consulting/librarycategory/")
        self.assertEqual(results.status_code, 200)

    def test_librarycategory(self):
        results = self.client.get("/admin/consulting/librarycategory/%s/change/" % self.obj.pk)
        self.assertEqual(results.status_code, 200)


class LibraryFileTestCase(AdminTestCase):

    def setUp(self):
        AdminTestCase.setUp(self)
        self.obj = LibraryFileFactory()

    def test_libraryfile_list(self):
        results = self.client.get("/admin/consulting/libraryfile/")
        self.assertEqual(results.status_code, 200)

    def test_libraryfile(self):
        results = self.client.get("/admin/consulting/libraryfile/%s/change/" % self.obj.pk)
        self.assertEqual(results.status_code, 200)
