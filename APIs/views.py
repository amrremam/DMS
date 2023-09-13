from django.shortcuts import render
from rest_framework import viewsets
from .models import New, CompanyImg
from .serializers import NewSerializer, CompanySerialiazer

# Create your views here.

class NewViewSet(viewsets.ModelViewSet):
    queryset = New.objects.all()
    serializer_class = NewSerializer


class CompanyViewSet(viewsets.ModelViewSet):
    queryset = CompanyImg.objects.all()
    serializer_class = CompanySerialiazer