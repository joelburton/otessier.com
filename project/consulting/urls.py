from django.conf.urls import url, include

from .views import ClientListView, ClientDetailView
from .views import PracticeAreaListView, PracticeAreaDetailView
from .views import QAndAListView, QAndADetailView
from .views import ConsultantListView, ConsultantDetailView
from .views import LibraryCategoryListView, LibraryCategoryDetailView
from .views import ContactUsFormView


def make_urls(url_fragment, list_view, detail_view, namespace):
    return url(url_fragment,
               include(
                   [url(r'^$', list_view.as_view(), name='list'),
                    url(r'^(?P<slug>[a-z\d-]+)/$', detail_view.as_view(), name='detail')],
                   namespace=namespace))

urlpatterns = [
    make_urls(r'^clients/', ClientListView, ClientDetailView, 'client'),
    make_urls(r'^practices/', PracticeAreaListView, PracticeAreaDetailView, 'practicearea'),
    make_urls(r'^questions/', QAndAListView, QAndADetailView, 'qanda'),
    make_urls(r'^consultants/', ConsultantListView, ConsultantDetailView, 'consultant'),
    make_urls(r'^library/', LibraryCategoryListView, LibraryCategoryDetailView, 'librarycategory'),

    url(r'^contact-info/$', ContactUsFormView.as_view(), name='contact-us'),
]