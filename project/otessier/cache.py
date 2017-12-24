"""Caching middleware.

We want to be able to cache pages and use things from cache--but if we're in
preview mode, there's the risk that the results created for us will list things
the public shouldn't see, and therefore this would leak into the cache. Therefore,
we don't want to store things in cache when in preview mode.

There are two parts to Django's cache middleware. This subclasses the "Store things
in cache" and doesn't update the cache when in preview mode.
"""


from django.middleware.cache import UpdateCacheMiddleware, FetchFromCacheMiddleware


class PreviewAwareUpdateCacheMiddleware(UpdateCacheMiddleware):
    """If we're at the preview URL, don't cache."""

    def _should_update_cache(self, request, response):

        preview_mode = getattr(request, 'preview_mode', False)

        if preview_mode:
            return False

        return super()._should_update_cache(request, response)


class PreviewAwareFetchFromCacheMiddleware(FetchFromCacheMiddleware):
    """If we're in preview mode, don't use cache."""

    def process_request(self, request):

        preview_mode = getattr(request, 'preview_mode', False)

        if preview_mode:
            return

        return super().process_request(request)
