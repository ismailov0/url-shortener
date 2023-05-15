from rest_framework import generics
from .services.shortener import generate_short_code
from .models import ShortenedURL
from .serializers import ShortenedURLSerializer


class ShortenedURLListCreateView(generics.ListCreateAPIView):
    """
    View for listing and creating ShortenedURL objects.
    """
    queryset = ShortenedURL.objects.all()
    serializer_class = ShortenedURLSerializer

    def perform_create(self, serializer: ShortenedURLSerializer) -> None:
        """
        Creates a new ShortenedURL object with a generated short code.
        """
        short_code = generate_short_code()
        serializer.save(short_code=short_code)


class ShortenedURLRetrieveView(generics.RetrieveAPIView):
    """
    View for retrieving a ShortenedURL object by its short code.
    """
    queryset = ShortenedURL.objects.all()
    serializer_class = ShortenedURLSerializer
    lookup_field: str = 'short_code'
