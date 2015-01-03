from django.middleware.cache import UpdateCacheMiddleware


class PreviewAwareUpdateCacheMiddleware(UpdateCacheMiddleware):
    """If we're at the preview URL, don't cache."""

    def _should_update_cache(self, request, response):
        return not request.preview_mode