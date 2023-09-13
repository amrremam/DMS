from rest_framework import serializers
from .models import New, CompanyImg


class NewSerializer(serializers.ModelSerializer):
    class Meta:
        model = New
        fields = '__all__'



class CompanySerialiazer(serializers.ModelSerializer):
    class Meta:
        model = CompanyImg
        fields = '__all__'
