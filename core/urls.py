from django.contrib import admin
from django.urls import path

from django.conf import settings
from django.conf.urls.static import static
# Documentation
from rest_framework.documentation import include_docs_urls

urlpatterns = [
    path('admin/', admin.site.urls),

    # Documentation
    path('', include_docs_urls(title="Courier")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
