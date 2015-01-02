from django.apps import AppConfig

import watson

from .models import SearchAdapter, ClientSearchAdapter


class ConsultingAppConfig(AppConfig):
    name = "consulting"

    def ready(self):
        watson.register(self.get_model("PracticeArea").published.all(), SearchAdapter)
        watson.register(self.get_model("Client").published.all(), ClientSearchAdapter)
        watson.register(self.get_model("Consultant").published.all(), SearchAdapter)
        watson.register(self.get_model("QAndA").published.all(), SearchAdapter)
        watson.register(self.get_model("LibraryFile").published.all(), SearchAdapter)
        watson.register(self.get_model("LibraryCategory").published.all(), SearchAdapter)