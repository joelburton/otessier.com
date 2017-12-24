"""Test caching setup.

The site should cache pages, except in admin mode.
"""


import os

from django.test import override_settings, TestCase
from django.conf import settings

from consulting.tests.factories import ConsultantFactory, QuoteFactory

MIDDLEWARE = (
    ['otessier.cache.PreviewAwareUpdateCacheMiddleware'] +
    settings.MIDDLEWARE +
    ['otessier.cache.PreviewAwareFetchFromCacheMiddleware']
)

CACHE = {'default':
    {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'TIMEOUT': 600,
        'KEY_PREFIX': 'otessier-com',
    }
}

# This tests using Django's LocMemCache; if you wanted to be even closer to a
# production-like setup, you should use this for the MIDDLEWARE_CLASSES

if os.environ.get("TEST_MEMCACHE"):    # pragma: no cover
    CACHE = {'default':
        {
            'BACKEND': 'django.core.cache.backends.memcached.PyLibMCCache',
            'LOCATION': '127.0.0.1:11211',
            'TIMEOUT': 600,
            'KEY_PREFIX': 'otessier-com',
        }
    }


@override_settings(
        CACHES=CACHE,
        MIDDLEWARE=MIDDLEWARE,
        CACHE_MIDDLEWARE_ALIAS='default',
        CACHE_MIDDLEWARE_SECONDS=600,
        CACHE_MIDDLEWARE_KEY_PREFIX='otessier-com-site')
class CachingTestCase(TestCase):
    """Test caching."""

    def test_cache(self):
        joel = ConsultantFactory(status='published')

        results = self.client.get('/consultants/joel-burton/')

        self.assertContains(results, "<h1>Joel Burton</h1>", status_code=200, html=True)
        self.assertFalse(results.wsgi_request.preview_mode)

        joel.title = "Jorge Burton"
        joel.save()

        results = self.client.get('/consultants/joel-burton/')

        self.assertContains(results, "<h1>Joel Burton</h1>", status_code=200, html=True)
        self.assertNotContains(results, "Jorge", status_code=200, html=True)

        joel.title = "Jane Burton"
        joel.save()

        results = self.client.get('/consultants/joel-burton/')

        self.assertContains(results, "<h1>Joel Burton</h1>", status_code=200, html=True)
        self.assertNotContains(results, "Jane", status_code=200, html=True)

    def test_quote_portlet_cache(self):
        """Test if test portlet caches."""

        quote = QuoteFactory(status='published')

        results = self.client.get("/")

        self.assertContains(results, "Oliver is love.", status_code=200)
        self.assertFalse(results.wsgi_request.preview_mode)

        quote.quote = "Changed."
        quote.save()

        results = self.client.get("/")

        self.assertContains(results, "Oliver is love.", status_code=200)
        self.assertNotContains(results, "Changed.", status_code=200)

    @override_settings(PREVIEW_MODE=True)
    def test_admin_doesnt_cache(self):
        joel = ConsultantFactory(status='published')

        results = self.client.get('/consultants/joel-burton/')

        self.assertContains(results, "<h1>Joel Burton</h1>", status_code=200, html=True)
        self.assertTrue(results.wsgi_request.preview_mode)

        joel.title = "Jorge Burton"
        joel.save()

        results = self.client.get('/consultants/joel-burton/')

        self.assertContains(results, "<h1>Jorge Burton</h1>", status_code=200, html=True)
        self.assertNotContains(results, "Joel", status_code=200, html=True)

        joel.title = "Jane Burton"
        joel.save()

        results = self.client.get('/consultants/joel-burton/')

        self.assertContains(results, "<h1>Jane Burton</h1>", status_code=200, html=True)
        self.assertNotContains(results, "Joel", status_code=200, html=True)

    @override_settings(PREVIEW_MODE=True)
    def test_quote_portlet_no_cache_admin_mode(self):
        """Test if test portlet caches."""

        quote = QuoteFactory(status='published')

        results = self.client.get("/")

        self.assertContains(results, "Oliver is love.", status_code=200)
        self.assertTrue(results.wsgi_request.preview_mode)

        quote.quote = "Changed."
        quote.save()

        results = self.client.get("/")

        self.assertNotContains(results, "Oliver is love.", status_code=200)
        self.assertContains(results, "Changed.", status_code=200)

