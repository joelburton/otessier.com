import watson.search as watson


class SearchAdapter(watson.SearchAdapter):
    """Standard search adapter for our site."""

    def get_url(self, obj):
        return obj.get_absolute_url()

    def get_description(self, obj):
        return obj.description

    def get_model_name(self, obj):
        # noinspection PyProtectedMember
        return obj._meta.verbose_name.title()


class ClientSearchAdapter(SearchAdapter):
    """Search adapter for clients.

    Adds in info from references and client work.
    """

    def get_content(self, obj):
        """Content to search."""

        def _mash(items, attrs):  # _mash(cats, ['name', 'color']) => 'auden grey ezra orange'
            return " ".join(" ".join(getattr(item, attr) for attr in attrs) for item in items)

        return " ".join([super(SearchAdapter, self).get_content(obj),
                         _mash(obj.clientreference_set.all(), ['job_title', 'phone', 'email']),
                         _mash(obj.clientwork_set.all(),      ['title', 'description', 'body'])])
