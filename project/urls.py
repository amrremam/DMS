from django.contrib import admin
from django.urls import path, include, reverse_lazy
from rest_framework.routers import DefaultRouter
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic.base import RedirectView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('APIs.urls')),
    path('' ,RedirectView.as_view(url=reverse_lazy('admin:index'))),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
