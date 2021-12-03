from rest_framework import serializers, viewsets, routers
from .models import ApiData

class ApiDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApiData
        fields = '__all__'