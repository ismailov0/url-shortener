from rest_framework import serializers
from .models import ShortenedURL


class ShortenedURLSerializer(serializers.ModelSerializer):
    """
    Serializer for the ShortenedURL model.
    """
    short_code = serializers.ReadOnlyField()

    class Meta:
        model = ShortenedURL
        fields = ('id', 'original_url', 'short_code', 'created_at')
