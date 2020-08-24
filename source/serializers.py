from rest_framework import serializers

from source.models import GaiaSource


class GaiaSourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = GaiaSource
        fields = '__all__'
