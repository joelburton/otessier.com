"""App configuration for consuting project.

We need this because we need to register watson search for the models.
"""

from django.apps import AppConfig


class ConsultingAppConfig(AppConfig):
    """Application config for consulting."""

    name = "consulting"

    def ready(self):
        """Register search adapters for watson."""

        import watson.search as watson
        from .search import SearchAdapter, ClientSearchAdapter

        def watson_register(model_name, adapter=SearchAdapter):
            watson.register(self.get_model(model_name).published.all(),
                            adapter,
                            store=['get_model_name'])

        watson_register("PracticeArea")
        watson_register("Client", adapter=ClientSearchAdapter)
        watson_register("Consultant")
        watson_register("QAndA")
        watson_register("LibraryFile")
        watson_register("LibraryCategory")
