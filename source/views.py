from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from source.models import GaiaSource
from source.serializers import GaiaSourceSerializer

# Create your views here.


class GaiaSourceViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    serializer_class = GaiaSourceSerializer
    queryset = GaiaSource.objects.all()
