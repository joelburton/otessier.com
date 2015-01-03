import time


class TimingMiddleware(object):
    """Times a request and adds timing information to the content.

    Adds an attribute, `_timing`, onto the request, and uses this at the end
    of the rendering chain to find the time difference. It replaces a token in
    the HTML, "<!-- RENDER_TIME -->", with the rendered time.
    """

    # Keep these out here so they can be modified in Django settings.

    REQUEST_ANNOTATION_KEY = "_timing"
    REPLACE = b"<!-- RENDER_TIME -->"
    REPLACE_TEMPLATE = b"<span>Handsomely rendered in {}ms.</span>"

    def process_request(self, request):
        """Add current time to the request."""

        setattr(request, self.REQUEST_ANNOTATION_KEY, time.time())

        # We do not return a request; doing so would say that we want to skip
        # all other middleware and Django processing. Instead, we return None.

    def process_response(self, request, response):
        """Compare current time to request start, and update content."""

        # In unusual situations (tests, etc), it's possible that we don't have
        # the same request, so let's check for our attribute before doing
        # anything

        then = getattr(request, self.REQUEST_ANNOTATION_KEY, None)
        if then:
            now = time.time()
            msg = self.REPLACE_TEMPLATE.format(int((now - then) * 1000))
            response.content = response.content.replace(self.REPLACE, msg)
        return response