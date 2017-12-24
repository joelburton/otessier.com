"""Preview-mode support.

In preview mode, we can see content that is not yet published.

A user is in preview mode when their hostname starts with "admin." (like
"admin.otessier.com" or when their global settings say so (we change
manually into preview mode in tests to simulate being at a preview-mode
hostname).

The caching system will not cache things when we're in preview mode.
"""

from django.conf import settings


class PreviewMiddleware(object):
    """Notes on the request when we are in preview mode."""

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        """Notes on the request when we are in preview mode."""

        request.preview_mode = (
            request.environ.get('HTTP_HOST', '').startswith('admin.') or
            getattr(settings, 'PREVIEW_MODE', False)
        )

        return self.get_response(request)