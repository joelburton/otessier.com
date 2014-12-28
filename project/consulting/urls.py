from django.conf.urls import patterns, url

from .views import ClientListView, ClientDetailView
from .views import ConsultantListView, ConsultantDetailView
from .views import LibraryCategoryListView
from .views import ContactUsFormView
from .views import PracticeAreaListView, PracticeAreaDetailView
from .views import QAndAListView, QAndADetailView

urlpatterns = patterns(
    '',

    url(r'^clients/$',
        ClientListView.as_view(),
        name='client.list'),
    url(r'^clients/(?P<slug>[a-z\d-]+)/$',
        ClientDetailView.as_view(),
        name='client.detail'),

    url(r'^practices/$',
        PracticeAreaListView.as_view(),
        name='practicearea.list'),
    url(r'^practices/(?P<slug>[a-z\d-]+)/$',
        PracticeAreaDetailView.as_view(),
        name='practicearea.detail'),

    url(r'^questions/$',
        QAndAListView.as_view(),
        name='qanda.list'),
    url(r'^questions/(?P<slug>[a-z\d-]+)/$',
        QAndADetailView.as_view(),
        name='qanda.detail'),

    url(r'^who/$',
        ConsultantListView.as_view(),
        name='consultant.list'),
    url(r'^who/(?P<slug>[a-z\d-]+)/$',
        ConsultantDetailView.as_view(),
        name='consultant.detail'),

    url(r'^library/$',
        LibraryCategoryListView.as_view(),
        name='librarycategory.list'),

    url(r'^contact-info/$',
        ContactUsFormView.as_view(),
        name='contact-us'),

)
