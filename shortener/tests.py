from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from .services.shortener import generate_short_code
from .models import ShortenedURL
from .serializers import ShortenedURLSerializer


class ShortenedURLTests(TestCase):
    """
    Test case for the ShortenedURL views and functionality.
    """

    def setUp(self):
        self.client = APIClient()

    def test_generate_short_code(self):
        """
        Test the generate_short_code function.
        """
        code = generate_short_code()
        # Check that the generated code has the expected length
        self.assertEqual(len(code), 6)

    def test_create_shortened_url(self):
        """
        Test creating a shortened URL.
        """
        url = 'http://www.example.com/'
        response = self.client.post(
            reverse('shortenedurl-list-create'), {'original_url': url}, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(ShortenedURL.objects.count(), 1)
        shortened_url = ShortenedURL.objects.first()
        self.assertEqual(shortened_url.original_url, url)

    def test_retrieve_shortened_url(self):
        """
        Test retrieving a shortened URL.
        """
        url = 'http://www.example.com/'
        short_code = generate_short_code()
        ShortenedURL.objects.create(original_url=url, short_code=short_code)
        response = self.client.get(
            reverse('shortenedurl-retrieve', args=[short_code]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        shortened_url = ShortenedURL.objects.get(short_code=short_code)
        serializer = ShortenedURLSerializer(shortened_url)
        self.assertEqual(response.data, serializer.data)
