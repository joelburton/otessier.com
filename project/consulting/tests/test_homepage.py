from django.test import TestCase, SimpleTestCase, override_settings
from django.core import mail

from consulting.models import Consultant, QAndA, Quote, SiteConfiguration
from consulting.tests.factories import PracticeAreaFactory, ConsultantFactory
from consulting.tests.factories import QuoteFactory


class HomepageTests(TestCase):
    def setUp(self):
        self.area = PracticeAreaFactory(status='published')
        self.quote = QuoteFactory(status='published')
        self.consultant = ConsultantFactory(status='published')

    def test_navigation(self):
        response = self.client.get("/")

        self.assertContains(
                response,
                """
                <ul class="dropdown-menu">
                    <li><a href="/consultants/joel-burton/">Joel Burton</a></li>
                </ul>
                """,
                status_code=200,
                html=True
        )

        self.assertContains(
                response,
                """
                <ul class="dropdown-menu">
                    <li><a href="/practices/coaching/">Coaching</a></li>
                </ul>
                """,
                status_code=200,
                html=True
        )

    def test_homepage(self):
        response = self.client.get('/')
        self.assertContains(response, 'Welcome', status_code=200)

        # Find practicearea in carousel
        self.assertContains(response, "<h2>Coaching</h2>")

        # Find in what-we-do section
        self.assertContains(
                response,
                """
                <h4>
                    <a href="/practices/coaching/">
                        <i class="fa fa-coaching fa-2x"></i>
                        Coaching
                    </a>
                </h4>
                """,
                html=True
        )


class HomepageUnpbulishedTests(TestCase):
    def setUp(self):
        self.area = PracticeAreaFactory()
        self.quote = QuoteFactory()
        self.consultant = ConsultantFactory()

    def test_homepage_unpub(self):
        response = self.client.get('/')
        self.assertContains(response, 'Welcome', status_code=200)

        # Find practicearea in carousel
        self.assertNotContains(response, "<h2>Coaching</h2>")

        # Find in what-we-do section
        self.assertNotContains(
                response,
                """
                <h4>
                    <a href="/practices/coaching/">
                        <i class="fa fa-coaching fa-2x"></i>
                        Coaching
                    </a>
                </h4>
                """,
                html=True
        )

    @override_settings(PREVIEW_MODE=True)
    def test_homepage_pub(self):
        response = self.client.get('/')
        self.assertContains(response, 'Welcome', status_code=200)

        # Find practicearea in carousel
        self.assertContains(response, "<h2>Coaching</h2>")

        # Find in what-we-do section
        self.assertContains(
                response,
                """
                <h4>
                    <a href="/practices/coaching/">
                        <i class="fa fa-coaching fa-2x"></i>
                        Coaching
                    </a>
                </h4>
                """,
                html=True
        )


class FooterTests(TestCase):

    def test_phone(self):
        config = SiteConfiguration.get_solo()
        config.phone = "555-1234"
        self.assertEqual(config.phone_digits(), '5551234')

    def test_footer_solo_config(self):
        config = SiteConfiguration.get_solo()
        config.phone = "555-1234"
        config.save()

        self.assertEqual(config.get_absolute_url(), '/')
        self.assertEqual(str(config), 'Site Configuration')

        response = self.client.get('/')
        self.assertContains(response, '555-1234', status_code=200)
