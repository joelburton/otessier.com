from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.views.decorators.cache import cache_page, cache_control

from .views import HomepageView

import consulting.urls
import watson.views

urlpatterns = patterns(
    '',

    url(r'^$', HomepageView.as_view(), name='homepage'),
    url(r'^', include(consulting.urls)),

    # url(r'^search/$', watson.views.SearchView.as_view(template_name='watson/search_results.html')),
    url(r"^search/", include("watson.urls", namespace="watson")),

    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/', include(admin.site.urls)),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
