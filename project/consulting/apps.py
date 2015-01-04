from django.apps import AppConfig

import watson

from .models import SearchAdapter, ClientSearchAdapter


class ConsultingAppConfig(AppConfig):
    name = "consulting"

    def ready(self):
        watson.register(self.get_model("PracticeArea").published.all(), SearchAdapter, store=['get_model_name'])
        watson.register(self.get_model("Client").published.all(), ClientSearchAdapter, store=['get_model_name'])
        watson.register(self.get_model("Consultant").published.all(), SearchAdapter, store=['get_model_name'])
        watson.register(self.get_model("QAndA").published.all(), SearchAdapter, store=['get_model_name'])
        watson.register(self.get_model("LibraryFile").published.all(), SearchAdapter, store=['get_model_name'])
        watson.register(self.get_model("LibraryCategory").published.all(), SearchAdapter, store=['get_model_name'])