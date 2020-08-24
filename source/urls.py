from django.urls import path, include
from rest_framework import routers

from source.views import GaiaSourceViewSet

router = routers.DefaultRouter()
router.register(r'source', GaiaSourceViewSet, basename='source')

urlpatterns = [
    path('', include(router.urls)),
]
