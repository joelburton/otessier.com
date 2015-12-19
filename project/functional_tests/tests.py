from django.test import LiveServerTestCase


class MySeleniumTests(LiveServerTestCase):
    def test_story(self):
        import doctest
        self.assertEqual(
                doctest.testfile("test_story.rst",
                                 globs={'url': self.live_server_url}
                                 ).failed,
                0)
