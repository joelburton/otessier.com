from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin

from .views import HomepageView

import consulting.urls

urlpatterns = patterns(
    '',

    url(r'^$', HomepageView.as_view(), name='homepage'),
    url(r'^', include(consulting.urls)),

    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/', include(admin.site.urls)),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
