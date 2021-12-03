from django.shortcuts import render
from rest_framework import serializers, viewsets, routers
from .models import ApiData
from .serializer import ApiDataSerializer

# Create your views here.

class Apidata(viewsets.ModelViewSet):
    queryset = ApiData.objects.all()
    serializer_class = ApiDataSerializer
