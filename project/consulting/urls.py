"""URLs for consulting project."""

from django.urls import include, path, re_path

from .views import ClientListView, ClientDetailView
from .views import PracticeAreaListView, PracticeAreaDetailView
from .views import QAndAListView, QAndADetailView
from .views import ConsultantListView, ConsultantDetailView
from .views import LibraryCategoryListView, LibraryCategoryDetailView
from .views import ContactUsFormView


def make_urls(url_fragment, list_view, detail_view, namespace):
    """Register list and detail view for each type of content."""

    return path(url_fragment,
                include((
                    [path('', list_view.as_view(), name='list'),
                     path('<slug:slug>/', detail_view.as_view(), name='detail')],
                    'consulting'),
                    namespace=namespace))


urlpatterns = [
    make_urls('clients/', ClientListView, ClientDetailView, 'client'),
    make_urls('practices/', PracticeAreaListView, PracticeAreaDetailView, 'practicearea'),
    make_urls('questions/', QAndAListView, QAndADetailView, 'qanda'),
    make_urls('consultants/', ConsultantListView, ConsultantDetailView, 'consultant'),
    make_urls('library/', LibraryCategoryListView, LibraryCategoryDetailView,
              'librarycategory'),

    path('contact-info/', ContactUsFormView.as_view(), name='contact-us'),
]
