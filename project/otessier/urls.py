from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin

import consulting.urls
# noinspection PyPackageRequirements
import watson.urls
import tinymce.urls

from .views import HomepageView

urlpatterns = [
    url(r'^$', HomepageView.as_view(), name='homepage'),

    url(r'^', include(consulting.urls, app_name='consulting')),
    url(r"^search/", include(watson.urls, namespace="watson")),
    url(r'^tinymce/', include(tinymce.urls)),
    url(r'^admin/', include(admin.site.urls)),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
