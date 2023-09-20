from django.urls import path, include ,reverse_lazy
from rest_framework import routers
from .views import NewViewSet, CompanyViewSet
from django.views.generic.base import RedirectView


router = routers.DefaultRouter()
router.register('news', NewViewSet)
router.register('img', CompanyViewSet)



urlpatterns = [
    path('', include(router.urls)),
    path('' ,RedirectView.as_view(url=reverse_lazy('admin:index'))),
]