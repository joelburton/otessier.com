from django.apps import AppConfig

import watson

from .models import SearchAdapter, ClientSearchAdapter


class ConsultingAppConfig(AppConfig):
    name = "consulting"

    def ready(self):

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