from django.apps import AppConfig

import watson.search as watson


class ConsultingAppConfig(AppConfig):
    name = "consulting"

    def ready(self):
        from .models import SearchAdapter, ClientSearchAdapter

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
