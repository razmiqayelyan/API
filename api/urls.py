from django.urls import path, include
from rest_framework import serializers, viewsets, routers
from .views import Apidata

router = routers.DefaultRouter()
router.register(r'', Apidata)

urlpatterns = [
    path('', include(router.urls))
]