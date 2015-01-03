import random


class PreviewMiddleware(object):
    """Notes on the request when we are in preview mode.
    """

    def process_request(self, request):
        """Add current time to the request."""

        request.preview_mode = request.environ['HTTP_HOST'].startswith('preview.')

        # We do not return a request; doing so would say that we want to skip
        # all other middleware and Django processing. Instead, we return None.