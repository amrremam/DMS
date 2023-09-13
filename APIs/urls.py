from django.urls import path, include
from rest_framework import routers
from .views import NewViewSet, CompanyViewSet



router = routers.DefaultRouter()
router.register('news', NewViewSet)
router.register('img', CompanyViewSet)



urlpatterns = [
    path('', include(router.urls)),
]