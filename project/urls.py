from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from django.conf import settings
from django.conf.urls.static import static

# from .import views

# router = DefaultRouter()
# router.register(r'news', views.NewViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('APIs.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)